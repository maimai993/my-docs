<template><div><h1 id="cs2工具" tabindex="-1"><a class="header-anchor" href="#cs2工具"><span>CS2工具</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-cs2-tools" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-cs2-tools" alt="" loading="lazy"></a> <a href="https://github.com/SparkUiX/koishi-plugin-cs2-tools" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: cs2</p>
<p><strong>功能描述</strong>: 提供Counter-Strike 2游戏相关的实用工具，包括饰品查询、价格监控、游戏数据统计等功能</p>
<p><strong>插件名称</strong>: cs2-tools</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gn0AE/RkMGA1nBoPFapgsCW0qEcJSoiGgIDGKEE+BcUAJzRg9F0Muy1v4dJdPkpxDvs1v/3P7MweBuUzr18Iq7C9awNiHl7LNXDiY9/YGYMSOTgKCyE/bAekyLlxZDp2AM9xqFUmt7Rmm14cG8cR3/RIlHw2q4BL9onHCvCjeZksdiOSGjgRzUoTeoOAQsgrqDifRNclMzUyF/ObPabQJsFN4J1yQPEHcCmOC12roJP5rR6Hmxd8QkgVw3ZZEg/kuZgj29xb473Kml2V5aCyQGFni0fV+2GsQVbWjOfXk1d4wG5fJ+U1NhxHdrD0e1sE3E3gaHtl0LsZ9LtLBuQyGBdDSuCWxA1ZhdPVVZRM6a0WpZzThjsZWgYK6PUKLqQp5nAbiMPNmArQUIOv4vAiMys1VqmC3omNPlUqM0mJFMVgyMyoGuDnmt4uD2sdlI3iuw5OssRIXWjInS3GvoD+k0NPhVnKqlgHVL3U0vFZypxZAwafj+QLUW7x+14BZZOol0OdqF65WqTy9k9BadlNtW8yMdokis238B3ww7dW7Wn9LC7kKeOx/QHw3TOR"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>cs2 &#x3C;功能> [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="功能列表" tabindex="-1"><a class="header-anchor" href="#功能列表"><span>功能列表</span></a></h3>
<table>
<thead>
<tr>
<th>功能</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>price</td>
<td>查询饰品价格</td>
<td>cs2 price 咆哮</td>
</tr>
<tr>
<td>search</td>
<td>搜索饰品</td>
<td>cs2 search 刀</td>
</tr>
<tr>
<td>stats</td>
<td>查询游戏数据</td>
<td>cs2 stats 玩家ID</td>
</tr>
<tr>
<td>inspect</td>
<td>检视链接解析</td>
<td>cs2 inspect &lt;链接&gt;</td>
</tr>
<tr>
<td>float</td>
<td>查询磨损值</td>
<td>cs2 float &lt;链接&gt;</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="查询饰品价格" tabindex="-1"><a class="header-anchor" href="#查询饰品价格"><span>查询饰品价格</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">cs2 price 咆哮</chat-message>
<chat-message nickname="bot" type="bot">
🔫 咆哮 (纪念品) - Howl
💰 价格范围: ¥15,000 - ¥25,000
📊 最近成交: ¥18,500
🔄 24小时交易量: 12件
📈 价格趋势: ↗️ 上涨 3.2%
</chat-message>
</chat-panel>
<h3 id="搜索饰品" tabindex="-1"><a class="header-anchor" href="#搜索饰品"><span>搜索饰品</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">cs2 search 蝴蝶刀</chat-message>
<chat-message nickname="bot" type="bot">
🔪 蝴蝶刀搜索结果：
1. 蝴蝶刀 | 多普勒 (Phase 2) - ¥8,500
2. 蝴蝶刀 | 大理石渐变 - ¥12,000
3. 蝴蝶刀 | 表面淬火 - ¥6,800
4. 蝴蝶刀 | 自动化 - ¥4,200
5. 蝴蝶刀 | 森林 DDPAT - ¥3,500
</chat-message>
</chat-panel>
<h3 id="查询游戏数据" tabindex="-1"><a class="header-anchor" href="#查询游戏数据"><span>查询游戏数据</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">cs2 stats 76561198326378547</chat-message>
<chat-message nickname="bot" type="bot">
🎮 玩家数据 - [CS2]
🏆 段位: 全球精英
🎯 K/D: 1.45
🎪 胜率: 58.3%
🎲 总场次: 1,247
🔥 最近战绩: 5连胜
</chat-message>
</chat-panel>
<h3 id="检视链接解析" tabindex="-1"><a class="header-anchor" href="#检视链接解析"><span>检视链接解析</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">cs2 inspect steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198326378547A32894765432D16987654321</chat-message>
<chat-message nickname="bot" type="bot">
🔍 检视结果：
🔫 AK-47 | 火蛇 (StatTrak™)
🎨 皮肤: Fire Serpent
⭐ 品质: 隐秘
🎯 磨损值: 0.0345 (久经沙场)
🎨 贴纸: 4x Katowice 2014 Holo
💰 估价: ¥25,000 - ¥35,000
</chat-message>
</chat-panel>
<h2 id="饰品品质等级" tabindex="-1"><a class="header-anchor" href="#饰品品质等级"><span>饰品品质等级</span></a></h2>
<table>
<thead>
<tr>
<th>品质</th>
<th>颜色</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>消费级</td>
<td>白色</td>
<td>最常见的品质</td>
</tr>
<tr>
<td>工业级</td>
<td>浅蓝</td>
<td>较为常见的品质</td>
</tr>
<tr>
<td>军规级</td>
<td>深蓝</td>
<td>中等稀有度</td>
</tr>
<tr>
<td>受限</td>
<td>紫色</td>
<td>较为稀有</td>
</tr>
<tr>
<td>保密</td>
<td>粉色</td>
<td>稀有</td>
</tr>
<tr>
<td>隐秘</td>
<td>红色</td>
<td>非常稀有</td>
</tr>
<tr>
<td>违禁</td>
<td>金色</td>
<td>极其稀有</td>
</tr>
</tbody>
</table>
<h2 id="磨损等级" tabindex="-1"><a class="header-anchor" href="#磨损等级"><span>磨损等级</span></a></h2>
<table>
<thead>
<tr>
<th>磨损范围</th>
<th>等级</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.00 - 0.07</td>
<td>崭新出厂</td>
<td>几乎无磨损</td>
</tr>
<tr>
<td>0.07 - 0.15</td>
<td>略有磨损</td>
<td>轻微磨损痕迹</td>
</tr>
<tr>
<td>0.15 - 0.38</td>
<td>久经沙场</td>
<td>明显磨损</td>
</tr>
<tr>
<td>0.38 - 0.45</td>
<td>破损不堪</td>
<td>严重磨损</td>
</tr>
<tr>
<td>0.45 - 1.00</td>
<td>战痕累累</td>
<td>极度磨损</td>
</tr>
</tbody>
</table>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>价格数据</strong>: 实时获取各大交易平台价格</li>
<li><strong>游戏数据</strong>: 通过Steam API获取玩家数据</li>
<li><strong>饰品信息</strong>: 完整的CS2饰品数据库</li>
</ul>
<h3 id="缓存机制" tabindex="-1"><a class="header-anchor" href="#缓存机制"><span>缓存机制</span></a></h3>
<ul>
<li><strong>价格缓存</strong>: 5分钟更新一次价格数据</li>
<li><strong>玩家数据缓存</strong>: 30分钟更新一次</li>
<li><strong>搜索缓存</strong>: 10分钟有效期</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>网络错误</strong>: 当无法连接API时提示</li>
<li><strong>数据错误</strong>: 当数据格式异常时提示</li>
<li><strong>玩家不存在</strong>: 当玩家ID无效时提示</li>
<li><strong>饰品未找到</strong>: 当搜索无结果时提示</li>
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
<td>api_key</td>
<td>string</td>
<td>-</td>
<td>Steam API密钥</td>
</tr>
<tr>
<td>cache_time</td>
<td>number</td>
<td>300</td>
<td>缓存时间（秒）</td>
</tr>
<tr>
<td>max_results</td>
<td>number</td>
<td>10</td>
<td>最大搜索结果数</td>
</tr>
<tr>
<td>price_source</td>
<td>string</td>
<td>buff</td>
<td>价格数据源</td>
</tr>
<tr>
<td>enable_stats</td>
<td>boolean</td>
<td>true</td>
<td>启用游戏数据查询</td>
</tr>
<tr>
<td>enable_inspect</td>
<td>boolean</td>
<td>true</td>
<td>启用检视链接解析</td>
</tr>
<tr>
<td>enable_float</td>
<td>boolean</td>
<td>true</td>
<td>启用磨损值查询</td>
</tr>
<tr>
<td>language</td>
<td>string</td>
<td>zh-CN</td>
<td>显示语言</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>API限制</strong>: Steam API有请求频率限制，请合理使用</li>
<li><strong>数据延迟</strong>: 价格数据可能存在5-10分钟的延迟</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问外部API</li>
<li><strong>玩家隐私</strong>: 只能查询公开游戏数据的玩家</li>
<li><strong>饰品价格</strong>: 价格仅供参考，实际交易价格可能有所不同</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>CS2工具集成了多种实用功能，可以帮助玩家快速查询饰品信息、监控价格变化、查看游戏数据等，是CS2玩家的好帮手。</p>
</div>
</div></template>


