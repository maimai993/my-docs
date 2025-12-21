<template><div><h1 id="sora视频生成" tabindex="-1"><a class="header-anchor" href="#sora视频生成"><span>Sora视频生成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://github.com/AstrBotDevs/AstrBot" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-AstrBot-75B9D8?style=flat" alt="" loading="lazy"></a> <a href="https://www.python.org" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="" loading="lazy"></a> <a href="https://github.com/maimai993/astrbot_plugin_video_sora2" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: sora, 生成视频, 视频生成</p>
<p><strong>功能描述</strong>: 通过调用 OpenAI Sora 的视频生成接口，实现机器人免费生成高质量视频并在聊天平台中发送的功能</p>
<p><strong>插件名称</strong>: astrbot_plugin_video_sora2</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstu2kAUhvd5iqOs2gWqou4rmbJoRQQ4XDZWFw64hTa1qW162YVeEKICk4RUaVUl4VZo0xhUqSSCtg9TecbOW8SeMRDHzixGM3O++WfO+c/jLelVNs/LKqxvrIA90pzZGuLq2SOyI5NS2nwi88U8rBfE0mty5DlmgGNZpHfsW+bJiF6cD5a1Y8sjQcyt+AViUk54qgCXeKPmJRE2SqJaeC54hRZwGLgYX8zyKv5aR7W2l3JGzI17I56XPYL3gWMUVQ5LKm5X8OHErxidA/4QE+f4HF9UBTkkicJmEJLMcElJ5q1B5aKzY7aOcLWJtV1jFvDQg1QqwTkTzQ19HvqZSJi7lXyxVVCFu3h/jOs6mu7d9ud6fb3IPw2h0D3bF7JhWXsHq/93jgFPqrg8umNMP9pfWyVQjDAxF2lDXBTsIsDLtTVU1yxdp1R02SlRF+0ABaxBFx82KcbECcLEXaYL9Cnjz/HF9u5VqblKD6zxO6cbSbUokcwQJJlxmT5YjTOkfWKyWUFRUtIzQaSgU0WCOgsX/ga40cetCf6tWYOqXV3CG+c1XOsHyw/cLzgGApN4GPTNIRjnXxy3eu/NZiU42e+A9upo2kLjstX9EKTy44bqUg88Rpy4YtQxil338yfgg39mb0q7jjLppdQiwVNApwfo7dCYzewUzNoEb5cpHQkTMhJ2SR3wUd8adVCjgrRflj5Gf/cXRbsEa9B2qA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>sora [横屏|竖屏] &#x3C;提示词></span></span>
<span class="line"><span>生成视频 [横屏|竖屏] &#x3C;提示词></span></span>
<span class="line"><span>视频生成 [横屏|竖屏] &#x3C;提示词></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>必填</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>横屏|竖屏</td>
<td>文本</td>
<td>否</td>
<td>视频方向，可选&quot;横屏&quot;或&quot;竖屏&quot;</td>
<td>横屏</td>
</tr>
<tr>
<td>提示词</td>
<td>文本</td>
<td>是</td>
<td>视频生成的描述文本</td>
<td>一只小猫在草地上玩耍</td>
</tr>
</tbody>
</table>
<h3 id="其他命令" tabindex="-1"><a class="header-anchor" href="#其他命令"><span>其他命令</span></a></h3>
<table>
<thead>
<tr>
<th>命令</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>sora查询 &lt;task_id&gt;</td>
<td>查询视频生成状态或重放已生成的视频</td>
<td>sora查询 task_123</td>
</tr>
<tr>
<td>sora强制查询 &lt;task_id&gt;</td>
<td>强制从官方接口重新查询任务状态</td>
<td>sora强制查询 task_123</td>
</tr>
<tr>
<td>sora鉴权检测</td>
<td>检测所有Token的有效性（仅管理员）</td>
<td>sora鉴权检测</td>
</tr>
<tr>
<td>sora自动token状态</td>
<td>查看自动获取的Token状态</td>
<td>sora自动token状态</td>
</tr>
<tr>
<td>sora自动token刷新</td>
<td>手动刷新自动获取的Token列表</td>
<td>sora自动token刷新</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本视频生成" tabindex="-1"><a class="header-anchor" href="#基本视频生成"><span>基本视频生成</span></a></h3>
<h4 id="生成竖屏视频" tabindex="-1"><a class="header-anchor" href="#生成竖屏视频"><span>生成竖屏视频</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">/sora 一只可爱的小猫在草地上追逐蝴蝶</chat-message>
<chat-message nickname="bot" type="bot">
<p>正在生成视频，请稍候~<br>
ID: task_abc123</p>
</chat-message>
<chat-message nickname="bot" type="bot">
<p><video src="https://cdn.tangbot.xyz/AstrBot/sora2.mp4" controls width="25%"></video></p>
</chat-message>
</chat-panel>
<h4 id="生成横屏视频" tabindex="-1"><a class="header-anchor" href="#生成横屏视频"><span>生成横屏视频</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">/sora 横屏 壮丽的日落时分，金色的阳光洒在海面上，海浪轻轻拍打着沙滩</chat-message>
<chat-message nickname="bot" type="bot">
<p>正在生成视频，请稍候~<br>
ID: task_def456</p>
</chat-message>
<chat-message nickname="bot" type="bot">
<video src="https://cdn.tangbot.xyz/AstrBot/sora.mp4" controls width="45%"></video>
</chat-message>
</chat-panel>
<h3 id="查询视频状态" tabindex="-1"><a class="header-anchor" href="#查询视频状态"><span>查询视频状态</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">sora查询 task_abc123</chat-message>
<chat-message nickname="bot" type="bot">
<p>任务还在队列中，请稍后再看~<br>
状态：queued 进度: 0.00%</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的token获取方式" tabindex="-1"><a class="header-anchor" href="#支持的token获取方式"><span>支持的Token获取方式</span></a></h3>
<ul>
<li><strong>手动填写</strong>: 传统方式，手动获取并填写AccessToken</li>
<li><strong>自动获取</strong>: 通过Tampermonkey脚本自动获取并上报Token到本地HTTP服务器</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>Token轮询</strong>: 支持多个Token轮询使用，避免单个Token并发限制</li>
<li><strong>并发控制</strong>: 每个账号有独立的并发限制，默认3个任务</li>
<li><strong>任务状态跟踪</strong>: 所有任务状态同步更新到Sqlite3数据库</li>
<li><strong>错误重试</strong>: 支持查询和重试未完成的任务</li>
<li><strong>图片处理</strong>: 自动处理GIF图片，转换为PNG格式</li>
</ul>
<h3 id="网络支持" tabindex="-1"><a class="header-anchor" href="#网络支持"><span>网络支持</span></a></h3>
<ul>
<li><strong>正向代理</strong>: 支持HTTP正向代理访问Sora API</li>
<li><strong>反向代理</strong>: 支持反向代理绕过地域限制</li>
<li><strong>代理类型</strong>: 支持拼接和替换两种反向代理方式</li>
</ul>
<h3 id="视频处理" tabindex="-1"><a class="header-anchor" href="#视频处理"><span>视频处理</span></a></h3>
<ul>
<li><strong>水印控制</strong>: 可选择是否在生成的视频中添加Sora2水印</li>
<li><strong>视频保存</strong>: 可选择是否持久化保存下载的视频文件</li>
<li><strong>方向检测</strong>: 自动检测图片方向，确定视频横屏或竖屏</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>账号权限</strong>: 需要有效的ChatGPT账号且有Sora模型的使用权限</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接访问OpenAI Sora API</li>
<li><strong>Token安全</strong>: Token存在封号风险，请谨慎使用</li>
<li><strong>并发限制</strong>: 每个账号有并发任务限制，超出限制会提示</li>
<li><strong>视频生成时间</strong>: 视频生成需要一定时间，复杂提示可能需要更长时间</li>
<li><strong>文件大小</strong>: 生成的视频文件可能较大，注意存储空间</li>
<li><strong>反向代理</strong>: 使用反向代理时请确保代理来源可信</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>插件支持以下配置选项：</p>
<table>
<thead>
<tr>
<th>配置项</th>
<th>类型</th>
<th>默认值</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>token_source</td>
<td>string</td>
<td>手动填写</td>
<td>Token获取方式：手动填写或自动获取</td>
</tr>
<tr>
<td>authorization_list</td>
<td>list</td>
<td>[]</td>
<td>手动填写的authorization列表，仅在token_source为&quot;手动填写&quot;时生效</td>
</tr>
<tr>
<td>websocket_enabled</td>
<td>bool</td>
<td>false</td>
<td>是否启用HTTP服务器接收自动上报的Token，仅在token_source为&quot;自动获取&quot;时生效</td>
</tr>
<tr>
<td>websocket_port</td>
<td>int</td>
<td>5103</td>
<td>HTTP服务器监听的端口号</td>
</tr>
<tr>
<td>auto_token_list</td>
<td>list</td>
<td>[]</td>
<td>自动获取的Token列表，只读</td>
</tr>
<tr>
<td>task_limit</td>
<td>int</td>
<td>3</td>
<td>每个账号的并发限制</td>
</tr>
<tr>
<td>model_config</td>
<td>object</td>
<td>{}</td>
<td>模型配置参数</td>
</tr>
<tr>
<td>model_config.model</td>
<td>string</td>
<td>sy_8</td>
<td>模型代码，目前已知可用的只有sy_8</td>
</tr>
<tr>
<td>model_config.size</td>
<td>string</td>
<td>small</td>
<td>清晰度，目前只有small可用</td>
</tr>
<tr>
<td>model_config.n_frames</td>
<td>int</td>
<td>450</td>
<td>视频的总帧数，视频时长为帧数/30秒</td>
</tr>
<tr>
<td>default_prompt</td>
<td>string</td>
<td>生成一个多镜头视频</td>
<td>默认提示词</td>
</tr>
<tr>
<td>watermark_enabled</td>
<td>bool</td>
<td>false</td>
<td>是否在生成的视频中添加Sora2水印</td>
</tr>
<tr>
<td>screen_mode</td>
<td>string</td>
<td>自动</td>
<td>默认视频方向：自动、竖屏、横屏</td>
</tr>
<tr>
<td>sora_base_url</td>
<td>string</td>
<td><a href="https://sora.chatgpt.com" target="_blank" rel="noopener noreferrer">https://sora.chatgpt.com</a></td>
<td>用于发起任务请求的Sora API地址</td>
</tr>
<tr>
<td>chatgpt_base_url</td>
<td>string</td>
<td><a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">https://chatgpt.com</a></td>
<td>用于获取Sentinel token的ChatGPT API地址</td>
</tr>
<tr>
<td>speed_down_url_type</td>
<td>string</td>
<td>拼接</td>
<td>下载视频的反代类型：拼接或替换</td>
</tr>
<tr>
<td>speed_down_url</td>
<td>string</td>
<td>&quot;&quot;</td>
<td>下载视频的反向代理地址</td>
</tr>
<tr>
<td>save_video_enabled</td>
<td>bool</td>
<td>false</td>
<td>是否持久化保存下载的视频文件</td>
</tr>
<tr>
<td>group_whitelist_enabled</td>
<td>bool</td>
<td>false</td>
<td>是否启用群组白名单</td>
</tr>
<tr>
<td>group_whitelist</td>
<td>list</td>
<td>[]</td>
<td>白名单群组sid列表</td>
</tr>
<tr>
<td>proxy</td>
<td>string</td>
<td>&quot;&quot;</td>
<td>HTTP正向代理地址</td>
</tr>
<tr>
<td>token_expiry_notification_enabled</td>
<td>bool</td>
<td>false</td>
<td>是否启用Token过期通知</td>
</tr>
<tr>
<td>token_expiry_notification_interval</td>
<td>int</td>
<td>30</td>
<td>Token过期检查间隔（分钟）</td>
</tr>
</tbody>
</table>
<h3 id="配置示例" tabindex="-1"><a class="header-anchor" href="#配置示例"><span>配置示例</span></a></h3>
<div class="language-yaml line-numbers-mode" data-highlighter="shiki" data-ext="yaml" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-yaml"><span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">astrbot_plugin_video_sora2</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  token_source</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"自动获取"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  websocket_enabled</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">true</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  websocket_port</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">5103</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  task_limit</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">3</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  model_config</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    model</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"sy_8"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    size</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"small"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    n_frames</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">450</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  default_prompt</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"生成一个多镜头视频"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  watermark_enabled</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">false</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  screen_mode</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"自动"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  sora_base_url</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://sora.chatgpt.com"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  chatgpt_base_url</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://chatgpt.com"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  speed_down_url_type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"拼接"</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  save_video_enabled</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">false</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  group_whitelist_enabled</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">false</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  proxy</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">""</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Sora视频生成插件基于OpenAI Sora API实现，能够生成高质量的视频内容。插件支持两种Token获取方式，可根据需要选择手动填写或自动获取。自动获取方式通过Tampermonkey脚本和本地HTTP服务器实现，解决了CSP限制问题，使用更加便捷。</p>
</div>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>本插件基于逆向工程技术调用官方接口，存在封号风险，请谨慎使用。如果使用反向代理，请确保反向代理的来源可信，以保证账号安全。</p>
</div>
</div></template>


