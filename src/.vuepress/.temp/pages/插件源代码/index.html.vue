<template><div><div align="center">
<h1 id="🫧-astrbot-sora-视频生成插件-🫧" tabindex="-1"><a class="header-anchor" href="#🫧-astrbot-sora-视频生成插件-🫧"><span>🫧 AstrBot Sora 视频生成插件 🫧</span></a></h1>
<figure><img src="https://count.getloli.com/@astrbot_plugin_video_sora2?name=astrbot_plugin_video_sora2&amp;theme=rule34&amp;padding=7&amp;offset=0&amp;scale=1&amp;pixelated=1&amp;darkmode=auto" alt=":访问量" tabindex="0" loading="lazy"><figcaption>:访问量</figcaption></figure>
<p><a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" loading="lazy"></a><br>
<a href="https://www.python.org" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+" loading="lazy"></a><br>
<a href="https://github.com/AstrBotDevs/AstrBot" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/AstrBot-4.0%2B-75B9D8.svg" alt="AstrBot" loading="lazy"></a><br>
<a href="https://sora.com" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/OpenAI Sora-2-00aaff.svg" alt="Sora" loading="lazy"></a></p>
</div>
<h2 id="介绍" tabindex="-1"><a class="header-anchor" href="#介绍"><span>介绍</span></a></h2>
<p>通过调用 OpenAI Sora 的视频生成接口，实现机器人免费生成高质量视频并在聊天平台中发送的功能。支持配置正向代理和反向代理，适应复杂的网络环境。<br>
本插件适用于 <a href="https://github.com/AstrBotDevs/AstrBot" target="_blank" rel="noopener noreferrer">AstrBot</a> 框架，<a href="https://astrbot.app" target="_blank" rel="noopener noreferrer">帮助文档</a>。</p>
<h2 id="获取网页鉴权-accesstoken" tabindex="-1"><a class="header-anchor" href="#获取网页鉴权-accesstoken"><span>获取网页鉴权（accessToken）</span></a></h2>
<p>插件支持两种方式获取ChatGPT AccessToken：</p>
<h3 id="方式一-手动填写-传统方式" tabindex="-1"><a class="header-anchor" href="#方式一-手动填写-传统方式"><span>方式一：手动填写（传统方式）</span></a></h3>
<blockquote>
<p>📝 建议使用浏览器的隐身模式，避免切换账号导致 Token 失效。</p>
</blockquote>
<ol>
<li>登录 <a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">https://chatgpt.com</a></li>
<li>打开 <a href="https://chatgpt.com/api/auth/session" target="_blank" rel="noopener noreferrer">https://chatgpt.com/api/auth/session</a></li>
<li>复制返回内容中的 accessToken 字段填写进插件配置，不需要加 <code v-pre>Bearer </code> 前缀。</li>
<li>打开 <a href="https://sora.com" target="_blank" rel="noopener noreferrer">https://sora.com</a> 检查账号是否有 Sora 模型的使用权限。注意是新版 Sora。</li>
</ol>
<h3 id="方式二-自动获取-推荐" tabindex="-1"><a class="header-anchor" href="#方式二-自动获取-推荐"><span>方式二：自动获取（推荐）</span></a></h3>
<p>通过Tampermonkey脚本自动获取并上报Token到本地HTTP服务器（解决CSP问题）。</p>
<h4 id="配置步骤" tabindex="-1"><a class="header-anchor" href="#配置步骤"><span>配置步骤：</span></a></h4>
<ol>
<li>
<p><strong>插件配置</strong>：</p>
<ul>
<li>在插件配置中，将 <code v-pre>token_source</code> 设置为 <code v-pre>auto</code>（自动获取）</li>
<li>启用HTTP服务器：<code v-pre>websocket_enabled</code> 设置为 <code v-pre>true</code></li>
<li>设置HTTP服务器端口：<code v-pre>websocket_port</code>（默认：5103）</li>
<li>自动获取的Token列表：<code v-pre>auto_token_list</code> 会自动填充</li>
</ul>
</li>
<li>
<p><strong>安装Tampermonkey脚本</strong>：</p>
<ul>
<li>安装Tampermonkey浏览器扩展</li>
<li>创建新脚本，复制 <a href="https://github.com/maimai993/astrbot_plugin_video_sora2/blob/main/tampermonke/ChatGPT%20AccessToken%20HTTP.js" target="_blank" rel="noopener noreferrer">ChatGPT AccessToken HTTP.js</a> 文件内容</li>
<li>保存并启用脚本</li>
</ul>
</li>
<li>
<p><strong>使用流程</strong>：</p>
<ul>
<li>启动插件，HTTP服务器会自动启动</li>
<li>使用浏览器登录ChatGPT（<a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">https://chatgpt.com</a>）</li>
<li>Tampermonkey脚本会自动提取AccessToken并通过HTTP POST上报到本地服务器</li>
<li>插件会自动接收并更新Token列表</li>
</ul>
</li>
</ol>
<h4 id="脚本功能" tabindex="-1"><a class="header-anchor" href="#脚本功能"><span>脚本功能：</span></a></h4>
<ul>
<li>自动检测ChatGPT登录状态</li>
<li>提取AccessToken并通过HTTP POST上报（绕过CSP限制）</li>
<li>支持多账号切换自动更新</li>
<li>定时刷新机制保持Token有效</li>
</ul>
<h4 id="管理命令" tabindex="-1"><a class="header-anchor" href="#管理命令"><span>管理命令：</span></a></h4>
<ul>
<li><code v-pre>/sora自动token状态</code> - 查看自动获取的Token状态</li>
<li><code v-pre>/sora自动token刷新</code> - 手动刷新自动获取的Token列表</li>
</ul>
<h2 id="sora2-邀请码" tabindex="-1"><a class="header-anchor" href="#sora2-邀请码"><span>Sora2 邀请码</span></a></h2>
<blockquote>
<p>📝 这里会收集一些已知的 Sora2 邀请码分享网站：使用成功后务必将自己的邀请码分享出来，薪火相传。</p>
</blockquote>
<ul>
<li><a href="https://escaping.work/sora-invites" target="_blank" rel="noopener noreferrer">https://escaping.work/sora-invites</a></li>
<li><a href="https://www.kdocs.cn/l/cfM2efy2Miu9" target="_blank" rel="noopener noreferrer">https://www.kdocs.cn/l/cfM2efy2Miu9</a></li>
<li><a href="https://soraic.connectdev.io" target="_blank" rel="noopener noreferrer">https://soraic.connectdev.io</a></li>
</ul>
<h2 id="使用说明" tabindex="-1"><a class="header-anchor" href="#使用说明"><span>使用说明</span></a></h2>
<p>生成视频：</p>
<ul>
<li>/sora [横屏|竖屏] &lt;提示&gt;</li>
<li>/生成视频 [横屏|竖屏] &lt;提示&gt;</li>
<li>/视频生成 [横屏|竖屏] &lt;提示&gt;</li>
<li>[横屏|竖屏] 参数是可选的</li>
</ul>
<p>查询与重试：</p>
<ul>
<li>/sora 查询 &lt;task_id&gt;</li>
<li>/sora 强制查询 &lt;task_id&gt;<br>
可用来查询任务状态、重放已生成的视频或重试未完成的任务。强制查询将绕过数据库缓存的任务状态，从官方接口重新查询任务情况。</li>
</ul>
<p>检测鉴权有效性：</p>
<ul>
<li>/sora 鉴权检测<br>
仅管理员可用，一键检查鉴权是否有效。</li>
</ul>
<h2 id="反向代理" tabindex="-1"><a class="header-anchor" href="#反向代理"><span>反向代理</span></a></h2>
<p>提供一个实验性的 Zako~♡Zako~♡ 反向代理，目前属于单节点单 IP 部署，暂不明确是否存在 429 等防刷机制。坏了可能来不及修复，请谨慎使用。<br>
使用方法：</p>
<ul>
<li>将三个 URL 输入框（sora_base_url、chatgpt_base_url、speed_down_url）的内容全部改成 <code v-pre>https://sora.zakozako.de</code></li>
<li>speed_down_url_type 选项选择 <b>替换</b> 即可。</li>
</ul>
<p>这个反向代理设置了较严格的访问频率限制和带宽控制，对于几个账号的日常使用应该已经足够了。如果你有更高的使用需求，相信你一定有自行解决网络问题的能力。</p>
<h2 id="特性" tabindex="-1"><a class="header-anchor" href="#特性"><span>特性</span></a></h2>
<ul>
<li>支持自定义并发数；无可用 Token 时会提示并发过多或未配置。</li>
<li>任务状态同步更新到 Sqlite3 数据库，可在插件数据目录导出 video_data.db 文件。</li>
</ul>
<h2 id="发送视频失败的解决方案" tabindex="-1"><a class="header-anchor" href="#发送视频失败的解决方案"><span>发送视频失败的解决方案</span></a></h2>
<blockquote>
<p>📝 以下方案任选一个。<br>
原因简单来说 AstrBot 发送视频给协议端（NapCat 等）的时候，有多种方案。</p>
</blockquote>
<blockquote>
<p>如果直接以 URL 的形式上报，协议端会直接从这个 URL 中下载视频，但是这将无法使用正向代理，可以直接在上报的 URL 中配置反向代理，解决方案见 1。</p>
</blockquote>
<blockquote>
<p>如果以本地文件的路径上报，并且配置了对外可达的回调接口地址，内部会生成一个 URL 回调接口，等待协议端自己请求这个接口下载视频。问题在于协议端可能无法访问这个回调接口，解决方案见 2。</p>
</blockquote>
<blockquote>
<p>如果以本地文件的路径上报，并且没有配置对外可达的回调接口地址，协议端会直接从 AstrBot 上报的文件路径中找视频文件。关键在于，AstrBot 的文件系统对于协议端容器可能不可见，解决方案见 3。</p>
</blockquote>
<blockquote>
<p>本插件的调度策略是：如果设置了正向代理，则以文件路径的形式上报给协议端（若发送视频失败见 2、3），否则以视频 URL 的形式上报（若发送失视频失败见 1）。</p>
</blockquote>
<ol>
<li>在 speed_down_url 中填写反向代理，协议端直接通过这个反向代理下载视频，可以不依赖于 AstrBot 的回调接口和挂载映射路径。</li>
<li>在 AstrBot 面板-配置文件-系统-对外可达的回调接口地址 配置回调接口，至少要求 <b>协议端</b> 能够访问这个回调接口。可以是容器网络的容器名称等，例如 <code v-pre>http://astrbot:6185</code>，前提是 AstrBot 和协议端容器在同一个容器网络内。也可以直接用 <code v-pre>http://ip:port</code>（不建议）、<code v-pre>http://host.docker.internal:6185</code>，也可以配置个 <code v-pre>https://example.com</code>，只要协议端能访问到就行。如果在 Astrbot 和协议端在同一台宿主机内，可以填写 <code v-pre>http://localhost:6185</code>、<code v-pre>http://127.0.0.1:6185</code>，用于解决方案 3 的文件权限问题。</li>
<li>将 AstrBot 数据目录映射到协议端 Docker 容器中，以便于文件复制。如果复制文件出现权限问题，请改用解决方案 2。</li>
</ol>
<ul>
<li>参考示例：<code v-pre>-v ~/AstrBot/data:/AstrBot/data</code> 按照实际环境修改。</li>
</ul>
<ol start="4">
<li>如果问题仍然无法解决，请提交一个 issue，写明部署环境、配置文件信息等。</li>
</ol>
<h2 id="故障排查" tabindex="-1"><a class="header-anchor" href="#故障排查"><span>故障排查</span></a></h2>
<ul>
<li>网络相关错误：检查代理或主机网络访问能力，已知部分国家网络无法访问 Sora2，例如新加坡。</li>
<li>权限问题：检查账号是否有生成视频的权限，登录 <a href="https://sora.com" target="_blank" rel="noopener noreferrer">https://sora.com</a> 直接生成一个视频看看。</li>
</ul>
<h2 id="风险提示" tabindex="-1"><a class="header-anchor" href="#风险提示"><span>风险提示</span></a></h2>
<ul>
<li>本插件基于逆向工程技术调用官方接口，存在封号风险，请谨慎使用。</li>
<li>如果使用反向代理，请确保反向代理的来源可信，以保证账号安全。</li>
</ul>
</div></template>


