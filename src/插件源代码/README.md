<div align="center">

# 🫧 AstrBot Sora 视频生成插件 🫧

![:访问量](https://count.getloli.com/@astrbot_plugin_video_sora2?name=astrbot_plugin_video_sora2&theme=rule34&padding=7&offset=0&scale=1&pixelated=1&darkmode=auto)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org)
[![AstrBot](https://img.shields.io/badge/AstrBot-4.0%2B-75B9D8.svg)](https://github.com/AstrBotDevs/AstrBot)
[![Sora](https://img.shields.io/badge/OpenAI%20Sora-2-00aaff.svg)](https://sora.com)

</div>

## 介绍

通过调用 OpenAI Sora 的视频生成接口，实现机器人免费生成高质量视频并在聊天平台中发送的功能。支持配置正向代理和反向代理，适应复杂的网络环境。  
本插件适用于 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 框架，[帮助文档](https://astrbot.app)。

## 获取网页鉴权（accessToken）

插件支持两种方式获取ChatGPT AccessToken：

### 方式一：手动填写（传统方式）
> 📝 建议使用浏览器的隐身模式，避免切换账号导致 Token 失效。

1. 登录 https://chatgpt.com
2. 打开 https://chatgpt.com/api/auth/session
3. 复制返回内容中的 accessToken 字段填写进插件配置，不需要加 `Bearer ` 前缀。
4. 打开 https://sora.com 检查账号是否有 Sora 模型的使用权限。注意是新版 Sora。

### 方式二：自动获取（推荐）
通过Tampermonkey脚本自动获取并上报Token到本地HTTP服务器（解决CSP问题）。

#### 配置步骤：
1. **插件配置**：
   - 在插件配置中，将 `token_source` 设置为 `auto`（自动获取）
   - 启用HTTP服务器：`websocket_enabled` 设置为 `true`
   - 设置HTTP服务器端口：`websocket_port`（默认：5103）
   - 自动获取的Token列表：`auto_token_list` 会自动填充

2. **安装Tampermonkey脚本**：
   - 安装Tampermonkey浏览器扩展
   - 创建新脚本，复制 [ChatGPT AccessToken HTTP.js](https://github.com/maimai993/astrbot_plugin_video_sora2/blob/main/tampermonke/ChatGPT%20AccessToken%20HTTP.js) 文件内容
   - 保存并启用脚本

3. **使用流程**：
   - 启动插件，HTTP服务器会自动启动
   - 使用浏览器登录ChatGPT（https://chatgpt.com）
   - Tampermonkey脚本会自动提取AccessToken并通过HTTP POST上报到本地服务器
   - 插件会自动接收并更新Token列表

#### 脚本功能：
- 自动检测ChatGPT登录状态
- 提取AccessToken并通过HTTP POST上报（绕过CSP限制）
- 支持多账号切换自动更新
- 定时刷新机制保持Token有效

#### 管理命令：
- `/sora自动token状态` - 查看自动获取的Token状态
- `/sora自动token刷新` - 手动刷新自动获取的Token列表

## Sora2 邀请码

> 📝 这里会收集一些已知的 Sora2 邀请码分享网站：使用成功后务必将自己的邀请码分享出来，薪火相传。

- https://escaping.work/sora-invites
- https://www.kdocs.cn/l/cfM2efy2Miu9
- https://soraic.connectdev.io

## 使用说明

生成视频：

- /sora [横屏|竖屏] <提示>
- /生成视频 [横屏|竖屏] <提示>
- /视频生成 [横屏|竖屏] <提示>
- [横屏|竖屏] 参数是可选的

查询与重试：

- /sora 查询 <task_id>
- /sora 强制查询 <task_id>  
  可用来查询任务状态、重放已生成的视频或重试未完成的任务。强制查询将绕过数据库缓存的任务状态，从官方接口重新查询任务情况。

检测鉴权有效性：

- /sora 鉴权检测  
  仅管理员可用，一键检查鉴权是否有效。

## 反向代理

提供一个实验性的 Zako\~♡Zako\~♡ 反向代理，目前属于单节点单 IP 部署，暂不明确是否存在 429 等防刷机制。坏了可能来不及修复，请谨慎使用。  
使用方法：

- 将三个 URL 输入框（sora_base_url、chatgpt_base_url、speed_down_url）的内容全部改成 `https://sora.zakozako.de`
- speed_down_url_type 选项选择 <b>替换</b> 即可。

这个反向代理设置了较严格的访问频率限制和带宽控制，对于几个账号的日常使用应该已经足够了。如果你有更高的使用需求，相信你一定有自行解决网络问题的能力。

## 特性

- 支持自定义并发数；无可用 Token 时会提示并发过多或未配置。
- 任务状态同步更新到 Sqlite3 数据库，可在插件数据目录导出 video_data.db 文件。

## 发送视频失败的解决方案

> 📝 以下方案任选一个。
> 原因简单来说 AstrBot 发送视频给协议端（NapCat 等）的时候，有多种方案。

> 如果直接以 URL 的形式上报，协议端会直接从这个 URL 中下载视频，但是这将无法使用正向代理，可以直接在上报的 URL 中配置反向代理，解决方案见 1。

> 如果以本地文件的路径上报，并且配置了对外可达的回调接口地址，内部会生成一个 URL 回调接口，等待协议端自己请求这个接口下载视频。问题在于协议端可能无法访问这个回调接口，解决方案见 2。

> 如果以本地文件的路径上报，并且没有配置对外可达的回调接口地址，协议端会直接从 AstrBot 上报的文件路径中找视频文件。关键在于，AstrBot 的文件系统对于协议端容器可能不可见，解决方案见 3。

> 本插件的调度策略是：如果设置了正向代理，则以文件路径的形式上报给协议端（若发送视频失败见 2、3），否则以视频 URL 的形式上报（若发送失视频失败见 1）。

1. 在 speed_down_url 中填写反向代理，协议端直接通过这个反向代理下载视频，可以不依赖于 AstrBot 的回调接口和挂载映射路径。
2. 在 AstrBot 面板-配置文件-系统-对外可达的回调接口地址 配置回调接口，至少要求 <b>协议端</b> 能够访问这个回调接口。可以是容器网络的容器名称等，例如 `http://astrbot:6185`，前提是 AstrBot 和协议端容器在同一个容器网络内。也可以直接用 `http://ip:port`（不建议）、`http://host.docker.internal:6185`，也可以配置个 `https://example.com`，只要协议端能访问到就行。如果在 Astrbot 和协议端在同一台宿主机内，可以填写 `http://localhost:6185`、`http://127.0.0.1:6185`，用于解决方案 3 的文件权限问题。
3. 将 AstrBot 数据目录映射到协议端 Docker 容器中，以便于文件复制。如果复制文件出现权限问题，请改用解决方案 2。

- 参考示例：`-v ~/AstrBot/data:/AstrBot/data` 按照实际环境修改。

4. 如果问题仍然无法解决，请提交一个 issue，写明部署环境、配置文件信息等。

## 故障排查

- 网络相关错误：检查代理或主机网络访问能力，已知部分国家网络无法访问 Sora2，例如新加坡。
- 权限问题：检查账号是否有生成视频的权限，登录 https://sora.com 直接生成一个视频看看。

## 风险提示

- 本插件基于逆向工程技术调用官方接口，存在封号风险，请谨慎使用。
- 如果使用反向代理，请确保反向代理的来源可信，以保证账号安全。
