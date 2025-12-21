import re
import random
import asyncio
import sqlite3
import os
import astrbot.api.message_components as Comp
from datetime import datetime
from astrbot.api import logger
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, StarTools
from astrbot.api.message_components import Video
from astrbot.core.message.message_event_result import MessageChain
from .utils import Utils
from .hybrid_server import (
    start_http_server,
    stop_http_server,
    is_http_server_running,
    get_auto_tokens,
    get_auto_token_info,
    refresh_auto_tokens,
    AIOHTTP_AVAILABLE
)


# 获取视频下载地址
MAX_WAIT = 30  # 最大等待时间（秒）
INTERVAL = 3  # 每次轮询间隔（秒）


class VideoSora(Star):
    def __init__(self, context: Context, config):
        super().__init__(context)
        self.config = config  # 读取配置文件
        sora_base_url = self.config.get("sora_base_url", "https://sora.chatgpt.com")
        chatgpt_base_url = self.config.get("chatgpt_base_url", "https://chatgpt.com")
        self.proxy = self.config.get("proxy")
        model_config = self.config.get("model_config", {})
        self.speed_down_url_type = self.config.get("speed_down_url_type")
        self.speed_down_url = self.config.get("speed_down_url")
        self.save_video_enabled = self.config.get("save_video_enabled", False)
        self.watermark_enabled = self.config.get("watermark_enabled", False)
        self.video_data_dir = os.path.join(
            StarTools.get_data_dir("astrbot_plugin_video_sora2"), "videos"
        )
        self.utils = Utils(
            sora_base_url,
            chatgpt_base_url,
            self.proxy,
            model_config,
            self.video_data_dir,
            self.watermark_enabled,
        )
        
        # Token来源配置
        self.token_source = self.config.get("token_source", "手动填写")
        self.websocket_enabled = self.config.get("websocket_enabled", False)
        self.websocket_port = self.config.get("websocket_port", 5103)
        
        # 根据Token来源初始化auth_dict
        if self.token_source == "自动获取":
            # 自动获取模式：从HTTP服务器获取Token
            self.auth_dict = {}
            logger.info(f"🔧 Token获取模式: 自动获取 (HTTP端口: {self.websocket_port})")
        else:
            # 手动填写模式：从配置文件中读取
            self.auth_dict = dict.fromkeys(self.config.get("authorization_list", []), 0)
            logger.info(f"🔧 Token获取模式: 手动填写 (Token数量: {len(self.auth_dict)})")
        
        self.screen_mode = self.config.get("screen_mode", "自动")
        self.def_prompt = self.config.get("default_prompt", "生成一个多镜头视频")
        self.polling_task = set()
        self.task_limit = int(self.config.get("task_limit", 3))
        self.group_whitelist_enabled = self.config.get("group_whitelist_enabled")
        self.group_whitelist = self.config.get("group_whitelist")
        self.websocket_server_task = None
        
        # Token过期通知配置
        self.token_expiry_notification_enabled = self.config.get("token_expiry_notification_enabled", False)
        self.token_expiry_notification_interval = self.config.get("token_expiry_notification_interval", 30)
        self.token_expiry_check_task = None
        self.last_notification_time = {}  # token -> 上次通知时间，避免重复通知

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        # 创建视频缓存文件路径
        os.makedirs(self.video_data_dir, exist_ok=True)
        # 数据库文件路径
        video_db_path = os.path.join(
            StarTools.get_data_dir("astrbot_plugin_video_sora2"), "video_data.db"
        )
        # 打开持久化连接
        self.conn = sqlite3.connect(video_db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS video_data (
                task_id TEXT PRIMARY KEY NOT NULL,
                user_id INTEGER,
                nickname TEXT,
                prompt TEXT,
                image_url TEXT,
                status TEXT,
                video_url TEXT,
                generation_id TEXT,
                message_id INTEGER,
                auth_xor TEXT,
                error_msg TEXT,
                updated_at DATETIME,
                created_at DATETIME
            )
        """)
        self.conn.commit()
        
        # 如果配置为自动获取Token且启用了HTTP服务器，则启动HTTP服务器
        if self.token_source == "自动获取" and self.websocket_enabled:
            if not AIOHTTP_AVAILABLE:
                logger.error("❌ aiohttp模块未安装，无法启动HTTP服务器")
                logger.error("请运行: pip install aiohttp")
                return
                
            try:
                # 启动HTTP服务器
                success = await start_http_server(self.websocket_port)
                if success:
                    logger.info(f"✅ HTTP服务器已启动，端口: {self.websocket_port}")
                    logger.info("📡 等待浏览器脚本上报AccessToken...")
                    logger.info("💡 请确保Tampermonkey脚本已安装并启用")
                    
                    # 启动Token刷新任务
                    self.token_refresh_task = asyncio.create_task(self.refresh_auto_tokens_periodically())
                else:
                    logger.error("❌ HTTP服务器启动失败")
            except Exception as e:
                logger.error(f"❌ 启动HTTP服务器时发生错误: {e}")
        elif self.token_source == "自动获取" and not self.websocket_enabled:
            logger.warning("⚠️ Token获取模式为自动获取，但HTTP服务器未启用")
            logger.warning("💡 请在配置中启用websocket_enabled以使用自动获取功能")
        else:
            logger.info(f"🔧 Token获取模式: {self.token_source}")
        
        # 启动Token过期检查任务（如果启用）
        if self.token_expiry_notification_enabled and self.token_source == "自动获取" and self.websocket_enabled:
            self.token_expiry_check_task = asyncio.create_task(self.check_token_expiry_periodically())
            logger.info(f"✅ Token过期检查任务已启动，检查间隔: {self.token_expiry_notification_interval}分钟")

    async def queue_task(
        self,
        event: AstrMessageEvent,
        task_id: str,
        authorization: str,
        is_check=False,
    ) -> tuple[str | None, str | None]:
        """完成视频生成并返回视频链接或者错误信息"""

        # 检查是否已经有相同的任务在处理
        if task_id in self.polling_task:
            status, _, progress = await self.utils.pending_video(task_id, authorization)
            return (
                None,
                f"任务还在队列中，请稍后再看~\n状态：{status} 进度: {progress * 100:.2f}%",
            )
        # 优化人机交互
        if is_check:
            status, err, progress = await self.utils.pending_video(
                task_id, authorization
            )
            if err:
                return None, err
            if status != "Done":
                await event.send(
                    MessageChain(
                        [
                            Comp.Reply(id=event.message_obj.message_id),
                            Comp.Plain(
                                f"任务仍在队列中，请稍后再看~\n状态：{status} 进度: {progress * 100:.2f}%"
                            ),
                        ]
                    )
                )
            else:
                logger.debug("队列状态完成，正在查询视频直链...")

        # 记录正在处理的任务
        try:
            self.polling_task.add(task_id)

            # 等待视频生成
            result, err = await self.utils.poll_pending_video(task_id, authorization)

            # 更新任务进度
            self.cursor.execute(
                """
                UPDATE video_data SET status = ?, error_msg = ?, updated_at = ? WHERE task_id = ?
            """,
                (
                    result,
                    err,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    task_id,
                ),
            )
            self.conn.commit()

            if result != "Done" or err:
                return None, err

            elapsed = 0
            status = "Done"
            video_url = ""
            generation_id = None
            err = None
            # 获取视频下载地址
            while elapsed < MAX_WAIT:
            #    (
            #        status,
            #        video_url,
            #        generation_id,
            #        err,
            #    ) = await self.utils.fetch_video_url(task_id, authorization)
            #    if video_url or status == "EXCEPTION":
            #        break
            #    if status == "Failed":
                    # 降级查询，尝试通过web端点获取视频链接或者失败原因
                    (
                        status,
                        video_url,
                        generation_id,
                        err,
                    ) = await self.utils.get_video_by_web(task_id, authorization)
                    if video_url or status in {"Failed", "EXCEPTION"}:
                        break
                    await asyncio.sleep(INTERVAL)
                    elapsed += INTERVAL

            # 更新任务进度
            self.cursor.execute(
                """
                UPDATE video_data SET status = ?, video_url = ?, generation_id = ?, error_msg = ?, updated_at = ? WHERE task_id = ?
            """,
                (
                    status,
                    video_url,
                    generation_id,
                    err,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    task_id,
                ),
            )
            self.conn.commit()

            # 把错误信息返回给调用者
            if not video_url or err:
                return None, err or "生成视频超时"

            return video_url, None
        finally:
            if is_check:
                self.polling_task.remove(task_id)

    async def create_video(
        self,
        event: AstrMessageEvent,
        image_url: str,
        image_bytes: bytes | None,
        prompt: str,
        screen_mode: str,
        authorization: str,
    ) -> str | None:
        """创建视频生成任务"""
        # 如果消息中携带图片，上传图片到OpenAI端点
        images_id = ""
        if image_bytes:
            images_id, err = await self.utils.upload_images(authorization, image_bytes)
            if not images_id or err:
                return None, err

        # 生成视频
        task_id, err = await self.utils.create_video(
            prompt, screen_mode, images_id, authorization
        )
        if not task_id or err:
            return None, err

        # 记录任务数据
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            """
            INSERT INTO video_data (task_id, user_id, nickname, prompt, image_url, status, message_id, auth_xor, updated_at, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                task_id,
                event.message_obj.sender.user_id,
                event.message_obj.sender.nickname,
                prompt,
                image_url,
                "Queued",
                event.message_obj.message_id,
                authorization[-8:],  # 只存储token的最后8位以作区分
                datetime_now,
                datetime_now,
            ),
        )
        self.conn.commit()
        # 返回结果
        return task_id, None

    async def handle_video_comp(
        self, task_id: str, video_url: str
    ) -> tuple[Video | None, str | None]:
        """处理视频组件消息"""
        # 视频组件
        video_comp = None
        err_msg = None

        # 处理反向代理
        if self.speed_down_url_type == "拼接":
            video_url = self.speed_down_url + video_url
        elif self.speed_down_url_type == "替换":
            video_url = re.sub(r"^(https?://[^/]+)", self.speed_down_url, video_url)
        # 默认直接上报视频URL
        video_comp = Video.fromURL(video_url)

        # 下载视频到本地
        if self.proxy or self.save_video_enabled:
            video_path = os.path.join(self.video_data_dir, f"{task_id}.mp4")
            # 先检查本地文件是否有视频文件
            if not os.path.exists(video_path):
                video_path, err_msg = await self.utils.download_video(
                    video_url, task_id
                )
            # 如果设置了正向代理，则上报本地文件路径
            if self.proxy:
                if err_msg:
                    return None, err_msg
                video_comp = Video.fromFileSystem(video_path)
        return video_comp, None

    @filter.command("sora", alias={"生成视频", "视频生成"})
    async def video_sora(self, event: AstrMessageEvent):
        """生成视频"""

        # 检查群是否在白名单中
        if (
            self.group_whitelist_enabled
            and event.unified_msg_origin not in self.group_whitelist
        ):
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("当前群不在白名单中，请联系管理员添加sid白名单"),
                ]
            )
            return

        # 检查AccessToken是否存在
        if not self.auth_dict:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("请先在插件配置中添加 Authorization"),
                ]
            )
            return

        # 解析参数
        msg = re.match(
            r"^(?:生成视频|视频生成|sora)(?:\s+(横屏|竖屏)?\s*([\s\S]*))?$",
            event.message_str,
        )
        # 提取提示词
        prompt = msg.group(2).strip() if msg and msg.group(2) else self.def_prompt

        # 遍历消息链，获取第一张图片（Sora网页端点不支持多张图片的视频生成，至少测试的时候是这样）
        image_url = ""
        for comp in event.get_messages():
            if isinstance(comp, Comp.Image):
                image_url = comp.url
                break
            elif isinstance(comp, Comp.Reply):
                for quote in comp.chain:
                    if isinstance(quote, Comp.Image):
                        image_url = quote.url
                        break

        # 下载图片
        image_bytes = None
        if image_url:
            image_bytes, err = await self.utils.download_image(image_url)
            if not image_bytes or err:
                yield event.chain_result(
                    [
                        Comp.Reply(id=event.message_obj.message_id),
                        Comp.Plain(err),
                    ]
                )
                return

        # 竖屏还是横屏
        screen_mode = "portrait"
        if msg and msg.group(1):
            params = msg.group(1).strip()
            screen_mode = "landscape" if params == "横屏" else "portrait"
        elif self.screen_mode in ["横屏", "竖屏"]:
            screen_mode = "landscape" if self.screen_mode == "横屏" else "portrait"
        elif self.screen_mode == "自动" and image_bytes:
            screen_mode = self.utils.get_image_orientation(image_bytes)

        # 过滤出可用Authorization
        valid_tokens = [k for k, v in self.auth_dict.items() if v < self.task_limit]
        if not valid_tokens:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("当前并发数过多，请稍后再试~"),
                ]
            )
            return

        task_id = None
        auth_token = None
        authorization = None
        err = None

        # 打乱顺序，避免请求过于集中
        random.shuffle(valid_tokens)
        # 尝试循环使用所有可用 token
        for auth_token in valid_tokens:
            authorization = "Bearer " + auth_token
            # 调用创建视频的函数
            task_id, err = await self.create_video(
                event, image_url, image_bytes, prompt, screen_mode, authorization
            )
            # 如果成功拿到 task_id，则跳出循环
            if task_id:
                # 释放内存
                image_bytes = None
                # 回复用户
                yield event.chain_result(
                    [
                        Comp.Reply(id=event.message_obj.message_id),
                        Comp.Plain(f"正在生成视频，请稍候~\nID: {task_id}"),
                    ]
                )
                break

        # 尝试完所有 token 仍然请求失败
        if not task_id:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain(err),
                ]
            )
            return

        try:
            # 记录并发
            if self.auth_dict[auth_token] >= self.task_limit:
                self.auth_dict[auth_token] = self.task_limit
                logger.warning(f"Token {auth_token[-4:]} 并发数已达上限，但仍尝试使用")
            else:
                self.auth_dict[auth_token] += 1

            # 交给queue_task处理，直到返回视频链接或者错误信息
            video_url, err_msg = await self.queue_task(event, task_id, authorization)
            if not video_url:
                yield event.chain_result(
                    [
                        Comp.Reply(id=event.message_obj.message_id),
                        Comp.Plain(err_msg),
                    ]
                )
                return

            # 视频组件
            video_comp, err_msg = await self.handle_video_comp(task_id, video_url)
            if err_msg:
                yield event.chain_result(
                    [
                        Comp.Reply(id=event.message_obj.message_id),
                        Comp.Plain(err_msg),
                    ]
                )
                return

            # 发送视频
            if video_comp:
                yield event.chain_result([video_comp])
                # 删除视频文件，如果没有开启保存视频功能，那么只有在开启self.proxy以后才有可能下载视频
                if not self.save_video_enabled and self.proxy:
                    self.utils.delete_video(task_id)

        finally:
            if self.auth_dict[auth_token] <= 0:
                self.auth_dict[auth_token] = 0
                logger.warning(f"Token {auth_token[-4:]} 并发数计算错误，已重置为0")
            else:
                self.auth_dict[auth_token] -= 1
            # 确保发送完成后再释放并发计数，防止下载视频或者发送视频过程中查询导致重复发送
            self.polling_task.remove(task_id)

    @filter.command("sora查询", alias={"sora强制查询"})
    async def check_video_task(self, event: AstrMessageEvent, task_id: str):
        """
        重放过去生成的视频，或者查询视频生成状态以及重试未完成的生成任务。
        强制查询将绕过数据库缓存，调用接口重新查询任务情况
        """
        # 检查群是否在白名单中
        if (
            self.group_whitelist_enabled
            and event.unified_msg_origin not in self.group_whitelist
        ):
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("当前群不在白名单中，请联系管理员添加sid白名单"),
                ]
            )
            return
        self.cursor.execute(
            "SELECT status, video_url, error_msg, auth_xor FROM video_data WHERE task_id = ?",
            (task_id,),
        )
        row = self.cursor.fetchone()
        if not row:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("未找到对应的视频任务"),
                ]
            )
            return
        status, video_url, error_msg, auth_xor = row
        is_force_check = event.message_str.startswith("sora强制查询")
        if not is_force_check:
            # 先处理错误
            if status == "Failed":
                yield event.chain_result(
                    [
                        Comp.Reply(id=event.message_obj.message_id),
                        Comp.Plain(error_msg or "视频生成失败"),
                    ]
                )
                return
            # 有视频，直接发送视频
            if video_url:
                video_comp, err_msg = await self.handle_video_comp(task_id, video_url)
                if err_msg:
                    yield event.chain_result(
                        [
                            Comp.Reply(id=event.message_obj.message_id),
                            Comp.Plain(err_msg),
                        ]
                    )
                    return
                if video_comp:
                    yield event.chain_result([video_comp])
                    # 删除视频文件
                    if not self.save_video_enabled and self.proxy:
                        self.utils.delete_video(task_id)
                    return
        # 再次尝试完成视频生成
        # 尝试匹配auth_token
        auth_token = None
        for token in self.auth_dict.keys():
            if token.endswith(auth_xor):
                auth_token = token
                break
        if not auth_token:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain("Token不存在，无法查询视频生成状态"),
                ]
            )
            return
        # 交给queue_task处理，直到返回视频链接或者错误信息
        authorization = "Bearer " + auth_token
        video_url, msg = await self.queue_task(
            event, task_id, authorization, is_check=True
        )
        if not video_url:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain(msg),
                ]
            )
            return

        # 视频组件
        video_comp, err_msg = await self.handle_video_comp(task_id, video_url)
        if err_msg:
            yield event.chain_result(
                [
                    Comp.Reply(id=event.message_obj.message_id),
                    Comp.Plain(err_msg),
                ]
            )
            return

        # 发送处理后的视频
        if video_comp:
            yield event.chain_result([video_comp])
            # 删除视频文件
            if not self.save_video_enabled and self.proxy:
                self.utils.delete_video(task_id)

    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.command("sora鉴权检测")
    async def check_validity_check(self, event: AstrMessageEvent):
        """测试鉴权有效性"""
        yield event.chain_result(
            [
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("正在测试鉴权有效性，请稍候~"),
            ]
        )
        result = "✅ 有效  ❌ 无效  ⏳ 超时  ❓ 错误\n"
        for auth_token in self.auth_dict.keys():
            authorization = "Bearer " + auth_token
            is_valid = await self.utils.check_token_validity(authorization)
            if is_valid == "Success":
                result += f"✅ {auth_token[-8:]}\n"
            elif is_valid == "Invalid":
                result += f"❌ {auth_token[-8:]}\n"
            elif is_valid == "Timeout":
                result += f"⏳ {auth_token[-8:]}\n"
            elif is_valid == "EXCEPTION":
                result += f"❓ {auth_token[-8:]}\n"
        yield event.chain_result(
            [
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain(result),
            ]
        )

    async def refresh_auto_tokens_periodically(self):
        """定期刷新自动获取的Token"""
        try:
            while True:
                # 每30秒刷新一次Token
                await asyncio.sleep(30)
                await self.update_auth_dict_from_http()
        except asyncio.CancelledError:
            logger.info("Token刷新任务已取消")
        except Exception as e:
            logger.error(f"Token刷新任务发生错误: {e}")
    
    async def check_token_expiry_periodically(self):
        """定期检查Token是否过期"""
        try:
            while True:
                # 等待指定的检查间隔（分钟转换为秒）
                await asyncio.sleep(self.token_expiry_notification_interval * 60)
                
                # 检查Token是否过期
                await self.check_token_expiry()
        except asyncio.CancelledError:
            logger.info("Token过期检查任务已取消")
        except Exception as e:
            logger.error(f"Token过期检查任务发生错误: {e}")
    
    async def check_token_expiry(self):
        """检查Token是否过期"""
        if not self.token_expiry_notification_enabled:
            return
        
        if self.token_source != "自动获取" or not self.websocket_enabled:
            return
        
        try:
            # 获取Token信息
            token_info_list = get_auto_token_info()
            if not token_info_list:
                return
            
            current_time = datetime.now()
            expired_tokens = []
            
            for token_info in token_info_list:
                token = token_info.get('token', '')
                last_updated_str = token_info.get('last_updated', '')
                user_name = token_info.get('user_name', 'unknown')
                user_email = token_info.get('user_email', 'unknown')
                
                if not token or not last_updated_str:
                    continue
                
                try:
                    # 解析最后更新时间
                    last_updated = datetime.fromisoformat(last_updated_str.replace('Z', '+00:00'))
                    
                    # 计算时间差（分钟）
                    time_diff = (current_time - last_updated).total_seconds() / 60
                    
                    # 如果超过30分钟未更新，则视为过期
                    if time_diff > 30:
                        # 检查是否已经发送过通知（避免重复通知）
                        last_notified = self.last_notification_time.get(token)
                        if last_notified:
                            # 如果上次通知时间在1小时内，不再重复通知
                            if (current_time - last_notified).total_seconds() / 3600 < 1:
                                continue
                        
                        expired_tokens.append({
                            'token': token,
                            'user_name': user_name,
                            'user_email': user_email,
                            'last_updated': last_updated,
                            'minutes_since_update': int(time_diff)
                        })
                        
                except Exception as e:
                    logger.error(f"解析Token最后更新时间时发生错误: {e}")
                    continue
            
            # 如果有过期的Token，发送通知
            if expired_tokens:
                await self.send_token_expiry_notification(expired_tokens)
                
        except Exception as e:
            logger.error(f"检查Token过期时发生错误: {e}")
    
    async def send_token_expiry_notification(self, expired_tokens):
        """发送Token过期通知给主人"""
        try:
            # 构建通知消息
            message = "⚠️ Token长时间未更新通知\n\n"
            message += "检测到以下Token超过30分钟未更新，登录可能已过期，请检查浏览器登录状态：\n\n"
            
            for i, token_info in enumerate(expired_tokens, 1):
                user_name = token_info['user_name']
                user_email = token_info['user_email']
                last_updated = token_info['last_updated']
                minutes_since_update = token_info['minutes_since_update']
                
                message += f"{i}. {user_name} ({user_email})\n"
                message += f"   最后更新: {last_updated.strftime('%Y-%m-%d %H:%M:%S')}\n"
                message += f"   已 {minutes_since_update} 分钟未更新\n"
                message += f"   Token: {token_info['token'][:16]}...\n\n"
            
            message += "💡 请检查浏览器是否已退出登录，或重新登录ChatGPT以更新Token。"
            
            # 记录通知时间，避免重复通知
            for token_info in expired_tokens:
                self.last_notification_time[token_info['token']] = datetime.now()
            
            # 发送通知给主人
            # 参考ErrorFilter插件的实现，尝试获取管理员ID并发送消息
            try:
                # 尝试从配置中获取管理员ID列表
                # 首先尝试从插件的配置中获取
                admins_id = self.config.get("admins_id", [])
                
                # 如果插件配置中没有，尝试从全局配置中获取
                if not admins_id and hasattr(self.context, 'get_config'):
                    global_config = self.context.get_config()
                    if global_config:
                        admins_id = global_config.get("admins_id", [])
                
                # 如果还没有管理员ID，尝试从机器人配置中获取
                if not admins_id and hasattr(self, 'bot'):
                    # 尝试获取机器人实例
                    bot_config = getattr(self.bot, 'config', {})
                    admins_id = bot_config.get("admins_id", [])
                
                # 如果有管理员ID，发送消息
                if admins_id:
                    for admin_id in admins_id:
                        try:
                            # 尝试使用AstrBot的API发送私聊消息
                            # 首先检查是否有可用的发送消息方法
                            if hasattr(self.context, 'post_message'):
                                # 使用context.post_message方法
                                await self.context.post_message(message, admin_id)
                                logger.info(f"✅ Token过期通知已发送给管理员 {admin_id}")
                            elif hasattr(self, 'bot') and hasattr(self.bot, 'send_private_msg'):
                                # 使用bot.send_private_msg方法
                                await self.bot.send_private_msg(
                                    user_id=int(admin_id),
                                    message=message
                                )
                                logger.info(f"✅ Token过期通知已发送给管理员 {admin_id}")
                            else:
                                # 尝试使用更通用的方法
                                logger.warning(f"无法发送消息给管理员 {admin_id}：未找到可用的发送消息方法")
                        except Exception as e:
                            logger.error(f"发送Token过期通知给管理员 {admin_id} 失败: {e}")
                else:
                    logger.warning("未找到管理员ID，无法发送Token过期通知")
                    logger.warning(message)  # 记录日志作为备份
                    
            except Exception as e:
                logger.error(f"发送Token过期通知时发生错误: {e}")
                logger.warning(message)  # 记录日志作为备份
            
        except Exception as e:
            logger.error(f"发送Token过期通知时发生错误: {e}")
    
    async def update_auth_dict_from_http(self):
        """从HTTP服务器更新auth_dict"""
        if self.token_source != "自动获取" or not self.websocket_enabled:
            return
            
        try:
            # 获取自动获取的Token列表
            auto_tokens = get_auto_tokens()
            if not auto_tokens:
                # 如果没有Token，清空auth_dict
                if self.auth_dict:
                    self.auth_dict.clear()
                    logger.warning("⚠️ 自动获取的Token列表为空，已清空auth_dict")
                return
            
            # 更新auth_dict
            new_tokens = []
            for token in auto_tokens:
                if token not in self.auth_dict:
                    # 新Token，初始并发数为0
                    self.auth_dict[token] = 0
                    new_tokens.append(token)
            
            # 移除已过期的Token
            expired_tokens = []
            for token in list(self.auth_dict.keys()):
                if token not in auto_tokens:
                    expired_tokens.append(token)
                    del self.auth_dict[token]
            
            # 记录日志
            if new_tokens:
                logger.info(f"✅ 新增{len(new_tokens)}个自动获取的Token")
                for token in new_tokens:
                    logger.info(f"🔑 新Token: {token[:16]}...")
            
            if expired_tokens:
                logger.info(f"🗑️ 移除{len(expired_tokens)}个已过期的Token")
                for token in expired_tokens:
                    logger.info(f"🔑 已移除Token: {token[:16]}...")
            
            if new_tokens or expired_tokens:
                logger.info(f"📊 当前Token总数: {len(self.auth_dict)}")
                
        except Exception as e:
            logger.error(f"❌ 更新auth_dict时发生错误: {e}")
    
    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.command("sora自动token状态")
    async def check_auto_token_status(self, event: AstrMessageEvent):
        """查看自动获取的Token状态"""
        if self.token_source != "自动获取":
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("当前Token获取模式为手动填写，无法查看自动获取的Token状态")
            ])
            return
            
        if not self.websocket_enabled:
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("HTTP服务器未启用，无法查看自动获取的Token状态")
            ])
            return
            
        # 获取Token信息
        token_info_list = get_auto_token_info()
        if not token_info_list:
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("📭 当前没有自动获取的Token\n💡 请确保Tampermonkey脚本已安装并登录ChatGPT")
            ])
            return
        
        # 构建状态消息
        message = "📊 自动获取Token状态\n\n"
        message += f"🔗 HTTP服务器: {'✅ 运行中' if is_http_server_running() else '❌ 未运行'}\n"
        message += f"📡 端口: {self.websocket_port}\n"
        message += f"🔑 Token总数: {len(token_info_list)}\n\n"
        
        for i, token_info in enumerate(token_info_list, 1):
            token = token_info.get('token', '')
            user_name = token_info.get('user_name', 'unknown')
            user_email = token_info.get('user_email', 'unknown')
            last_updated = token_info.get('last_updated', '')
            status = token_info.get('status', 'unknown')
            
            # 格式化时间
            if last_updated:
                try:
                    dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                    last_updated_str = dt.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    last_updated_str = last_updated
            else:
                last_updated_str = "未知"
            
            # 并发数
            concurrent = self.auth_dict.get(token, 0)
            
            message += f"{i}. {user_name} ({user_email})\n"
            message += f"   状态: {status} | 并发: {concurrent}/{self.task_limit}\n"
            message += f"   最后更新: {last_updated_str}\n"
            message += f"   Token: {token[:16]}...\n\n"
        
        message += "💡 提示: 使用 'sora自动token刷新' 命令请求浏览器刷新Token"
        
        yield event.chain_result([
            Comp.Reply(id=event.message_obj.message_id),
            Comp.Plain(message)
        ])
    
    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.command("sora自动token刷新")
    async def refresh_auto_tokens_command(self, event: AstrMessageEvent):
        """请求刷新自动获取的Token"""
        if self.token_source != "自动获取":
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("当前Token获取模式为手动填写，无法刷新自动获取的Token")
            ])
            return
            
        if not self.websocket_enabled:
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("HTTP服务器未启用，无法刷新自动获取的Token")
            ])
            return
            
        yield event.chain_result([
            Comp.Reply(id=event.message_obj.message_id),
            Comp.Plain("🔄 正在请求浏览器刷新Token...")
        ])
        
        try:
            await refresh_auto_tokens()
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain("✅ 已发送Token刷新请求到所有连接的浏览器")
            ])
        except Exception as e:
            logger.error(f"❌ 刷新Token时发生错误: {e}")
            yield event.chain_result([
                Comp.Reply(id=event.message_obj.message_id),
                Comp.Plain(f"❌ 刷新Token失败: {str(e)}")
            ])
    
    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        try:
            # 停止Token刷新任务
            if hasattr(self, 'token_refresh_task') and self.token_refresh_task:
                self.token_refresh_task.cancel()
                try:
                    await self.token_refresh_task
                except asyncio.CancelledError:
                    pass
            
            # 停止Token过期检查任务
            if hasattr(self, 'token_expiry_check_task') and self.token_expiry_check_task:
                self.token_expiry_check_task.cancel()
                try:
                    await self.token_expiry_check_task
                except asyncio.CancelledError:
                    pass
            
            # 停止HTTP服务器
            if self.token_source == "自动获取" and self.websocket_enabled:
                await stop_http_server()
            
            # 关闭其他资源
            await self.utils.close()
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            logger.error(f"插件卸载时发生错误: {e}")
