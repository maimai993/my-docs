import time
import asyncio
import json
import hashlib
import base64
import os
from PIL import Image
from io import BytesIO
from curl_cffi import requests, AsyncSession, CurlMime
from curl_cffi.requests.exceptions import Timeout
from astrbot.api import logger
from uuid import uuid4

# 轮询参数
MAX_INTERVAL = 90  # 最大间隔
MIN_INTERVAL = 5  # 最小间隔
TOTAL_WAIT = 600  # 最多等待10分钟


class Utils:
    def __init__(
        self,
        sora_base_url: str,
        chatgpt_base_url: str,
        proxy: str,
        model_config: dict,
        video_data_dir: str,
        watermark_enabled: bool,
    ):
        self.sora_base_url = sora_base_url
        self.chatgpt_base_url = chatgpt_base_url
        proxies = {"http": proxy, "https": proxy} if proxy else None
        self.session = AsyncSession(impersonate="chrome136", proxies=proxies)
        self.model_config = model_config
        self.UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
        self.video_data_dir = video_data_dir
        self.watermark_enabled = watermark_enabled

    def _handle_image(self, image_bytes: bytes) -> bytes:
        try:
            with Image.open(BytesIO(image_bytes)) as img:
                # 如果不是 GIF，直接返回原图
                if img.format != "GIF":
                    return image_bytes
                # 处理 GIF
                buf = BytesIO()
                # 判断是否为动画 GIF（多帧）
                if getattr(img, "is_animated", False) and img.n_frames > 1:
                    img.seek(0)  # 只取第一帧
                # 单帧 GIF 或者多帧 GIF 的第一帧都走下面的保存逻辑
                img = img.convert("RGBA")
                img.save(buf, format="PNG")
                return buf.getvalue()
        except Exception as e:
            logger.warning(f"GIF 处理失败，返回原图: {e}")
            return image_bytes

    async def download_image(self, url: str) -> tuple[bytes | None, str | None]:
        try:
            response = await self.session.get(url)
            content = self._handle_image(response.content)
            return content, None
        except (
            requests.exceptions.SSLError,
            requests.exceptions.CertificateVerifyError,
        ):
            # 关闭SSL验证
            response = await self.session.get(url, verify=False)
            content = self._handle_image(response.content)
            return content, None
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return None, "下载图片失败：网络请求超时，请检查网络连通性"
        except Exception as e:
            logger.error(f"下载图片失败: {e}")
            return None, "下载图片失败"

    @staticmethod
    def get_image_orientation(image_bytes: bytes) -> str:
        # 把 bytes 转成图片对象
        img = Image.open(BytesIO(image_bytes))

        width, height = img.size
        if width > height:
            return "landscape"
        elif width < height:
            return "portrait"
        else:
            return "portrait"

    async def upload_images(
        self, authorization: str, image_bytes: bytes
    ) -> tuple[str | None, str | None]:
        try:
            mp = CurlMime()
            mp.addpart(
                name="file",
                filename=f"{int(time.time() * 1000)}.png",
                content_type="image/png",
                data=image_bytes,
            )
            response = await self.session.post(
                self.sora_base_url + "/backend/uploads",
                multipart=mp,
                headers={"Authorization": authorization},
            )
            if response.status_code == 200:
                result = response.json()
                return result.get("id"), None
            else:
                result = response.json()
                err_str = f"上传图片失败: {result.get('error', {}).get('message')}"
                logger.error(err_str)
                return None, err_str
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return None, "上传图片失败：网络请求超时，请检查网络连通性"
        except Exception as e:
            logger.error(f"上传图片失败: {e}")
            return None, "上传图片失败"
        finally:
            mp.close()

    async def get_sentinel(self) -> tuple[str | None, str | None]:
        # 随便生成一个哈希值作为PoW证明，反正服务器也不验证，留空都可以
        id = str(uuid4())
        random_str = (self.UA + id).encode()
        stoken = base64.b64encode(hashlib.sha256(random_str).digest()).decode()
        flow = "sora_2_create_task"
        payload = {"flow": flow, "id": id, "p": stoken}
        try:
            response = await self.session.post(
                self.chatgpt_base_url + "/backend-api/sentinel/req", json=payload
            )
            if response.status_code == 200:
                result = response.json()
                # 组装Sentinel token
                sentinel_token = {
                    "p": stoken,
                    "t": result.get("turnstile", {}).get("dx", ""),
                    "c": result.get("token", ""),
                    "id": id,
                    "flow": flow,
                }
                return json.dumps(sentinel_token), None
            else:
                logger.error(f"获取Sentinel tokens失败: {response.text}")
                return None, "获取Sentinel tokens失败"
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return None, "获取Sentinel tokens失败：网络请求超时，请检查网络连通性"
        except Exception as e:
            logger.error(f"获取Sentinel tokens失败: {e}")
            return None, "获取Sentinel tokens失败"

    async def create_video(
        self, prompt: str, screen_mode: str, image_id: str, authorization: str
    ) -> tuple[str | None, str | None]:
        sentinel_token, err = await self.get_sentinel()
        if err:
            return None, err
        inpaint_items = [{"kind": "upload", "upload_id": image_id}] if image_id else []
        payload = {
            "kind": "video",
            "prompt": prompt,
            "title": None,
            "orientation": screen_mode,
            "size": self.model_config.get("size", "small"),
            "n_frames": self.model_config.get("n_frames", 300),
            "inpaint_items": inpaint_items,
            "remix_target_id": None,
            "cameo_ids": None,
            "cameo_replacements": None,
            "model": self.model_config.get("model", "sy_8"),
            "style_id": None,
            "audio_caption": None,
            "audio_transcript": None,
            "video_caption": None,
            "storyboard_id": None,
        }
        try:
            response = await self.session.post(
                self.sora_base_url + "/backend/nf/create",
                json=payload,
                headers={
                    "Authorization": authorization,
                    "openai-sentinel-token": sentinel_token,
                },
            )
            if response.status_code == 200:
                result = response.json()
                return result.get("id"), None
            else:
                result = response.json()
                err_str = f"提交任务失败: {result.get('error', {}).get('message')}"
                logger.error(f"{err_str}，Token: {authorization[-8:]}")
                return None, err_str
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return None, "提交任务失败：网络请求超时，请检查网络连通性"
        except Exception as e:
            logger.error(f"提交任务失败: {e}")
            return None, "提交任务失败"

    async def pending_video(
        self, task_id: str, authorization: str
    ) -> tuple[str | None, str | None, float]:
        try:
            response = await self.session.get(
                self.sora_base_url + "/backend/nf/pending",
                headers={"Authorization": authorization},
            )
            if response.status_code == 200:
                result = response.json()
                for item in result:
                    if item.get("id") == task_id:
                        return item.get("status"), None, item.get("progress_pct") or 0
                return (
                    "Done",
                    None,
                    0,
                )  # "Done"表示任务队列状态结束，至于任务是否成功，不知道
            else:
                result = response.json()
                err_str = f"视频状态查询失败: {result.get('error', {}).get('message')}"
                logger.error(err_str)
                return "Failed", result.get("error", {}).get("message"), 0
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return "Timeout", "视频状态查询失败：网络请求超时，请检查网络连通性", 0
        except Exception as e:
            logger.error(f"视频状态查询失败: {e}")
            return "EXCEPTION", "视频状态查询失败", 0

    async def poll_pending_video(
        self, task_id: str, authorization: str
    ) -> tuple[str, str | None]:
        """轮询等待视频生成完成"""
        interval = MAX_INTERVAL
        elapsed = 0  # 已等待时间
        timeout_num = 0  # 超时次数
        failed_num = 0  # 失败次数
        while elapsed < TOTAL_WAIT:
            status, err, progress = await self.pending_video(task_id, authorization)
            if status == "Done":
                # "Done"表示任务队列状态结束，至于任务是否成功，不知道
                return "Done", None
            elif status == "Failed":
                # 这个错误通常不是审查截断引起的，可能是服务器问题，重试几次
                failed_num += 1
                if failed_num > 3:
                    return (
                        "Failed",
                        f"视频状态查询失败，ID: {task_id}，进度: {progress * 100:.2f}%，错误: {err}",
                    )
            elif status == "Timeout":
                # 前面都过了，这里不太可能超时，但是处理一下吧
                timeout_num += 1
                if timeout_num > 3:
                    return (
                        "Timeout",
                        f"视频状态查询失败，ID: {task_id}，进度: {progress * 100:.2f}%，网络连接超时",
                    )
            elif status == "EXCEPTION":
                # 程序错误，直接返回
                return (
                    "EXCEPTION",
                    f"视频状态查询程序错误，ID: {task_id}，请前往控制台查看",
                )
            # 等待当前轮询间隔
            wait_time = min(interval, TOTAL_WAIT - elapsed)
            await asyncio.sleep(wait_time)
            elapsed += wait_time
            # 反向指数退避：间隔逐步减小
            interval = max(MIN_INTERVAL, interval // 2)
            logger.debug(
                f"视频处理中，{interval}s 后再次请求... 进度: {progress * 100:.2f}%"
            )
        logger.error("视频状态查询超时")
        return (
            "Timeout",
            f"视频状态查询超时，ID: {task_id}，生成进度: {progress * 100:.2f}%",
        )

    async def get_video_by_web(
        self, task_id: str, authorization: str
    ) -> tuple[str, str | None, str | None, str | None]:
        try:
            response = await self.session.get(
                self.sora_base_url + "/backend/project_y/profile/drafts?limit=15",
                headers={"Authorization": authorization},
            )
            if response.status_code == 200:
                result = response.json()
                for item in result.get("items", []):
                    if item.get("task_id") == task_id:
                        downloadable_url = item.get("downloadable_url")
                        if not downloadable_url:
                            err_str = (
                                item.get("reason_str")
                                or item.get("error_reason")
                                or "未知错误"
                            )
                            logger.error(
                                f"生成视频失败, task_id: {task_id}, sora_reason: {err_str}"
                            )
                            return (
                                "Failed",
                                None,
                                item.get("id"),
                                err_str,
                            )
                        return "Done", downloadable_url, item.get("id"), None
                return "NotFound", None, None, "未找到对应的视频"
            else:
                result = response.json()
                err_str = f"获取视频链接失败: {result.get('error', {}).get('message')}"
                logger.error(err_str)
                return "ServerError", None, None, err_str
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return (
                "Timeout",
                None,
                None,
                "获取视频链接失败：网络请求超时，请检查网络连通性",
            )
        except Exception as e:
            logger.error(f"获取视频链接失败: {e}")
            return "EXCEPTION", None, None, "获取视频链接失败"

    async def fetch_video_url(
        self, task_id: str, authorization: str
    ) -> tuple[str, str | None, str | None, str | None]:
        try:
            response = await self.session.get(
                self.sora_base_url + "/backend/video_gen",
                headers={"Authorization": authorization},
            )
            if response.status_code == 200:
                result = response.json()
                for item in result.get("task_responses", []):
                    if item.get("id") == task_id:
                        if not item.get("generations"):
                            return (
                                "Failed",
                                None,
                                None,
                                item.get("failure_reason"),
                            )
                        video_url = (
                            item.get("generations", [])[0]
                            .get("encodings", {})
                            .get(
                                "source_wm" if self.watermark_enabled else "source", {}
                            )
                            .get("path")
                        )
                        return (
                            "Done",
                            video_url,
                            item.get("generations", [])[0].get("id"),
                            None,
                        )
                return "NotFound", None, None, "未找到对应的视频"
            else:
                result = response.json()
                err_str = f"获取视频链接失败: {result.get('error', {}).get('message')}"
                logger.error(err_str)
                return "ServerError", None, None, err_str
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return (
                "Timeout",
                None,
                None,
                "获取视频链接失败：网络请求超时，请检查网络连通性",
            )
        except Exception as e:
            logger.error(f"获取视频链接失败: {e}")
            return "EXCEPTION", None, None, "获取视频链接失败"

    async def download_video(
        self, video_url: str, task_id: str
    ) -> tuple[str | None, str | None]:
        try:
            logger.debug(f"正在下载视频: {video_url}")
            response = await self.session.get(video_url)
            if response.status_code == 200:
                # 保存视频内容到本地文件
                video_path = os.path.join(self.video_data_dir, f"{task_id}.mp4")
                with open(video_path, "wb") as f:
                    f.write(response.content)
                return video_path, None
            else:
                return None, f"下载视频失败: {response.status_code}"
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return None, "下载视频失败：网络请求超时，请检查网络连通性"
        except Exception as e:
            logger.error(f"下载视频失败: {e}")
            return None, "下载视频失败"

    def delete_video(self, task_id: str) -> None:
        """删除视频文件，仅传递任务ID"""
        try:
            video_path = os.path.join(self.video_data_dir, f"{task_id}.mp4")
            if os.path.exists(video_path):
                os.remove(video_path)
                logger.debug(f"已删除视频文件：{task_id}")
            else:
                logger.warning(f"删除视频失败: 视频文件不存在：{video_path}")
        except Exception as e:
            logger.error(f"删除视频失败: {e}")

    async def check_token_validity(self, authorization: str) -> str:
        try:
            response = await self.session.get(
                self.sora_base_url + "/backend/nf/pending",
                headers={"Authorization": authorization},
            )
            if response.status_code == 200:
                return "Success"
            else:
                result = response.json()
                err_str = f"Token {authorization[-8:]} 无效: {result.get('error', {}).get('message')}"
                logger.error(err_str)
                return "Invalid"
        except Timeout as e:
            logger.error(f"网络请求超时: {e}")
            return "Timeout"
        except Exception as e:
            logger.error(f"程序错误: {e}")
            return "EXCEPTION"

    async def close(self):
        await self.session.close()
