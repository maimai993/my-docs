<template><div><h1 id="hypixel封禁统计" tabindex="-1"><a class="header-anchor" href="#hypixel封禁统计"><span>Hypixel封禁统计</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-hypixel-ban-tracker" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-hypixel-ban-tracker" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: hypixel</p>
<p><strong>别名</strong>: hpbans</p>
<p><strong>功能描述</strong>: 查询Hypixel服务器的封禁统计数据，包括Watchdog反作弊系统和客服封禁的统计信息</p>
<p><strong>插件名称</strong>: hypixel-ban-tracker</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9klFv0lAUx9/5FCd7Z2ZfwKQ1JhAWaJeRkDQ+XKBKFVtSiuKbOF2Ihgw3NEYXtg7c0GnBF2bAuO9i2tvuW3jbe9ethe08tPfc87v/c84992FVe16qIN2A9Y0EEMtLbm+E22cPAi/41BvFRzqqVWBdURvNYCuyzYEkio51RE65p2N68NJEkcSutmS1nFgUyGpl+XEdJP+/ShYbDdVQnspRpZDmCYhqJWTg/Y7z1oxSvmVZPBqJpI4I3gMpoyn1ioLNbdyfLgpmWHwxwuUkVEY1Q9aTmioXtVhO31K8VHlRU5pyNVlEatLQUemJrC+RKkioqWj1xarj67CTsIP7TVKBiqogOcOPF1uj+M1wQloSqkglmVcVzXdpLFTKQzJ5lwwrcESReLDy7/0h4Gkbt8Z37Nk7ez5dCaBswGQZYkJOlXnNgGdra05nx7MsSmWunk+GoUdAAe9kgPtdinG5AOFyjBkATWX/Obx4uXtd6lJlCN5ky3+iO7thSSk+QFI8Y76CNz7Dv16RPvGHCe6wmrgCTVZg2DGkNjcFijJCSFNESDPmBLzznvOl70xa7nHrNrUR0KgzfO12t5cX9g3c3gFud935gWeZ9rlJLndZk9/B/v2ZTPC6VvyqTsHZ6zizHqnMG7xZpvLjhtnQCUbG+JOJ0XlTLP4aLMCf/rrDGS3ene/h/j4l84n/oeBwFg=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>hypixel</span></span>
<span class="line"><span>hpbans</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
<p>该指令无需额外参数，直接调用即可获取最新的封禁统计数据。</p>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="查询封禁统计" tabindex="-1"><a class="header-anchor" href="#查询封禁统计"><span>查询封禁统计</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hypixel</chat-message>
<chat-message nickname="bot" type="bot">
<p>🕒 更新时间: 2025-11-16 23:35:15<br>
🛡️ Watchdog封禁统计:<br>
▸ 最近1分钟: 0次<br>
▸ 最近24小时: 0次<br>
▸ 总计: 10040701次<br>
👮 客服封禁统计:<br>
▸ 最近1分钟: 0次<br>
▸ 最近24小时: 0次<br>
▸ 总计: 5272330次<br>
📜 最近封禁记录:<br>
[🐕] 23:35:15 封禁 10040701 名玩家<br>
[👮] 23:35:15 封禁 5272330 名玩家</p>
</chat-message>
</chat-panel>
<h3 id="使用别名查询" tabindex="-1"><a class="header-anchor" href="#使用别名查询"><span>使用别名查询</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hpbans</chat-message>
<chat-message nickname="bot" type="bot">
<p>🕒 更新时间: 2025-11-16 23:35:15<br>
🛡️ Watchdog封禁统计:<br>
▸ 最近1分钟: 0次<br>
▸ 最近24小时: 0次<br>
▸ 总计: 10040701次<br>
👮 客服封禁统计:<br>
▸ 最近1分钟: 0次<br>
▸ 最近24小时: 0次<br>
▸ 总计: 5272330次<br>
📜 最近封禁记录:<br>
[🐕] 23:35:15 封禁 10040701 名玩家<br>
[👮] 23:35:15 封禁 5272330 名玩家</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>API接口</strong>: 使用Plancke.io提供的Hypixel封禁统计API</li>
<li><strong>数据更新</strong>: 实时获取最新的封禁数据</li>
<li><strong>缓存机制</strong>: 内置数据缓存，避免频繁请求API</li>
</ul>
<h3 id="统计维度" tabindex="-1"><a class="header-anchor" href="#统计维度"><span>统计维度</span></a></h3>
<ul>
<li><strong>Watchdog封禁</strong>: Hypixel反作弊系统的自动封禁</li>
<li><strong>客服封禁</strong>: 人工客服处理的封禁</li>
<li><strong>时间范围</strong>:
<ul>
<li>最近1分钟</li>
<li>最近24小时</li>
<li>总计封禁数量</li>
</ul>
</li>
</ul>
<h3 id="数据展示" tabindex="-1"><a class="header-anchor" href="#数据展示"><span>数据展示</span></a></h3>
<ul>
<li><strong>实时更新</strong>: 显示数据更新时间</li>
<li><strong>历史记录</strong>: 保存最近的封禁记录</li>
<li><strong>图标标识</strong>: 使用🐕和👮图标区分封禁类型</li>
</ul>
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
<td>apiUrl</td>
<td>string</td>
<td><a href="https://api.plancke.io/hypixel/v1/punishmentStats" target="_blank" rel="noopener noreferrer">https://api.plancke.io/hypixel/v1/punishmentStats</a></td>
<td>Hypixel封禁统计API地址</td>
</tr>
<tr>
<td>cacheDuration</td>
<td>number</td>
<td>30000</td>
<td>数据缓存时间(毫秒)</td>
</tr>
<tr>
<td>maxRecords</td>
<td>number</td>
<td>100</td>
<td>最大记录保存数量</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>数据延迟</strong>: API数据可能存在一定的延迟，不是完全实时的</li>
<li><strong>网络要求</strong>: <a href="http://xn--Plancke-vf2m5670a31rquf3s9aw5c.io" target="_blank" rel="noopener noreferrer">需要能够访问Plancke.io</a> API的网络环境</li>
<li><strong>缓存机制</strong>: 为避免频繁请求API，数据会缓存一段时间</li>
<li><strong>数据估算</strong>: 24小时数据在跨天时会进行估算处理</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Hypixel是全球最大的Minecraft服务器之一，Watchdog是其反作弊系统，能够自动检测和封禁使用作弊软件的玩家。该插件可以帮助玩家了解服务器的安全状况。</p>
</div>
</div></template>


