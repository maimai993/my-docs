<template><div><h1 id="股票" tabindex="-1"><a class="header-anchor" href="#股票"><span>股票</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://github.com/Genshin-bots/gsuid_core" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-GsCore-af9183?style=flat" alt="" loading="lazy"></a> <a href="https://www.python.org" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="" loading="lazy"></a> <a href="https://github.com/KimigaiiWuyi/SayuStock" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a></p>
<p><strong>功能描述</strong>: 基于GsCore的全功能股票/A股机器人插件，支持大盘云图、个股查询、自选管理、新闻订阅等功能</p>
<p><strong>插件名称</strong>: SayuStock</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kslOAkEQhu88RYU7MbyACRDigS0j4TTxMMAouDAEBpcbRETUEBA5GDHsCIoBTmjA4LsYumd8C4fuARyWOnS6qr7+u7qq94+FM1+Ai4hg39WBYh5WKrRx+mOPeGSJxrwHES4cAHswFDsnIU3YBCzDoG5NOSV1evTgzBhGyS1CfMiv0+TnImZgnVzYx4n4OYNuq1qVqTnVvDazWdACrE0IRgNBXE3h0mBV0MbuRC1ChF/NmFws5+fCIh8xCCHeKyzdOTWrg3VzFzG3KPiOVita3s+r9IDBsK00hTgMo3ig/7mvAB6kcaK3NRneTUYDPYGchHGqSBVcId4siHBqNKJMVu52KWVbjMmmojWggNyq41KOYiYXQUwulakDvWryVfmN5/9LzVQaIPcvp18hm5+XZHUQxOpQmSbgehyXm/yJcBiURkmUS68HX0AqlHE6pwDTtTiWbq7Xky2QvwuoWFolteW1YfL5pPwT1EhKudT6R74CesigYQH1E3L9ap3K24au0t5rBtBRxeikKLY8x3fAj2OpMaTFk65Q0KP7AxygIyQ="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>大盘概览</span></span>
<span class="line"><span>大盘云图 [类型]</span></span>
<span class="line"><span>行业云图 [行业名称]</span></span>
<span class="line"><span>概念云图 [概念名称]</span></span>
<span class="line"><span>个股 &#x3C;股票代码/名称> [K线类型]</span></span>
<span class="line"><span>我的个股</span></span>
<span class="line"><span>我的自选</span></span>
<span class="line"><span>全天候</span></span>
<span class="line"><span>对比个股 &#x3C;股票代码1> &#x3C;股票代码2> ...</span></span>
<span class="line"><span>添加自选 &#x3C;股票代码/名称></span></span>
<span class="line"><span>删除自选 &#x3C;股票代码/名称></span></span>
<span class="line"><span>基金持仓 &#x3C;基金代码></span></span>
<span class="line"><span>市盈率对比 &#x3C;股票代码></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="主要指令说明" tabindex="-1"><a class="header-anchor" href="#主要指令说明"><span>主要指令说明</span></a></h3>
<table>
<thead>
<tr>
<th>指令</th>
<th>参数</th>
<th>必填</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>大盘概览</td>
<td>无</td>
<td>是</td>
<td>显示大盘概览信息</td>
<td>大盘概览</td>
</tr>
<tr>
<td>大盘云图</td>
<td>类型</td>
<td>否</td>
<td>显示大盘云图，可选：港股、美股</td>
<td>大盘云图 港股</td>
</tr>
<tr>
<td>行业云图</td>
<td>行业名称</td>
<td>是</td>
<td>显示指定行业的云图</td>
<td>行业云图 半导体</td>
</tr>
<tr>
<td>概念云图</td>
<td>概念名称</td>
<td>是</td>
<td>显示指定概念的云图</td>
<td>概念云图 白酒</td>
</tr>
<tr>
<td>个股</td>
<td>股票代码</td>
<td>是</td>
<td>查询个股信息</td>
<td>个股 沪深300</td>
</tr>
<tr>
<td>我的个股</td>
<td>无</td>
<td>是</td>
<td>显示用户自选的个股信息</td>
<td>我的个股</td>
</tr>
<tr>
<td>我的自选</td>
<td>无</td>
<td>是</td>
<td>显示用户的自选列表</td>
<td>我的自选</td>
</tr>
<tr>
<td>全天候</td>
<td>无</td>
<td>是</td>
<td>显示全天候板块信息</td>
<td>全天候</td>
</tr>
<tr>
<td>对比个股</td>
<td>股票代码列表</td>
<td>是</td>
<td>对比多个股票走势</td>
<td>对比个股 A500 沪深300</td>
</tr>
<tr>
<td>添加自选</td>
<td>股票代码</td>
<td>是</td>
<td>添加股票到自选</td>
<td>添加自选 中证白酒</td>
</tr>
<tr>
<td>删除自选</td>
<td>股票代码</td>
<td>是</td>
<td>从自选删除股票</td>
<td>删除自选 中证白酒</td>
</tr>
<tr>
<td>基金持仓</td>
<td>基金代码</td>
<td>是</td>
<td>显示基金持仓分布</td>
<td>基金持仓 510300</td>
</tr>
<tr>
<td>市盈率对比</td>
<td>股票代码</td>
<td>是</td>
<td>显示市盈率对比图</td>
<td>市盈率对比 贵州茅台</td>
</tr>
</tbody>
</table>
<h3 id="k线类型选项" tabindex="-1"><a class="header-anchor" href="#k线类型选项"><span>K线类型选项</span></a></h3>
<table>
<thead>
<tr>
<th>选项</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>5k</td>
<td>5分钟K线</td>
<td>个股 沪深300 5k</td>
</tr>
<tr>
<td>15k</td>
<td>15分钟K线</td>
<td>个股 沪深300 15k</td>
</tr>
<tr>
<td>30k</td>
<td>30分钟K线</td>
<td>个股 沪深300 30k</td>
</tr>
<tr>
<td>60k</td>
<td>60分钟K线</td>
<td>个股 沪深300 60k</td>
</tr>
<tr>
<td>日k</td>
<td>日K线</td>
<td>个股 沪深300 日k</td>
</tr>
<tr>
<td>周k</td>
<td>周K线</td>
<td>个股 沪深300 周k</td>
</tr>
<tr>
<td>月k</td>
<td>月K线</td>
<td>个股 沪深300 月k</td>
</tr>
<tr>
<td>年k</td>
<td>年K线</td>
<td>个股 沪深300 年k</td>
</tr>
</tbody>
</table>
<h3 id="时间范围选项-对比个股" tabindex="-1"><a class="header-anchor" href="#时间范围选项-对比个股"><span>时间范围选项（对比个股）</span></a></h3>
<table>
<thead>
<tr>
<th>选项</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>年初至今</td>
<td>从今年年初开始对比</td>
<td>对比个股 年初至今 中证白酒 中证2000</td>
</tr>
<tr>
<td>最近一年</td>
<td>最近一年数据对比</td>
<td>对比个股 最近一年 中证白酒 中证2000</td>
</tr>
<tr>
<td>最近一月</td>
<td>最近一月数据对比</td>
<td>对比个股 最近一月 中证白酒 中证2000</td>
</tr>
<tr>
<td>自定义日期</td>
<td>指定日期范围</td>
<td>对比个股 2024.01.01-2024.12.31 中证白酒</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本查询" tabindex="-1"><a class="header-anchor" href="#基本查询"><span>基本查询</span></a></h3>
<h4 id="查询大盘概览" tabindex="-1"><a class="header-anchor" href="#查询大盘概览"><span>查询大盘概览</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">大盘概览</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/01/22/GCip3KMlLjASnsV.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查询个股信息" tabindex="-1"><a class="header-anchor" href="#查询个股信息"><span>查询个股信息</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">个股 沪深300</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/08/04/AQPOKB9T2WwU5sf.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="云图功能" tabindex="-1"><a class="header-anchor" href="#云图功能"><span>云图功能</span></a></h3>
<h4 id="查看大盘云图" tabindex="-1"><a class="header-anchor" href="#查看大盘云图"><span>查看大盘云图</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">大盘云图</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2024/11/26/qvMG1ers7pITSUZ.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查看行业云图" tabindex="-1"><a class="header-anchor" href="#查看行业云图"><span>查看行业云图</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">行业云图 半导体</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/01/22/vsUthKeZk3TEfxR.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="自选管理" tabindex="-1"><a class="header-anchor" href="#自选管理"><span>自选管理</span></a></h3>
<h4 id="添加自选" tabindex="-1"><a class="header-anchor" href="#添加自选"><span>添加自选</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">添加自选 中证白酒</chat-message>
<chat-message nickname="bot" type="bot">
是否确认将下列股票添加自选?
中证白酒(512690)
请输入是或否。
</chat-message>
<chat-message nickname="用户" type="user">是</chat-message>
<chat-message nickname="bot" type="bot">
✅[SayuStock] 添加自选成功!
可发送[我的自选]查看或发送[删除自选]清除！
</chat-message>
</chat-panel>
<h4 id="查看我的自选" tabindex="-1"><a class="header-anchor" href="#查看我的自选"><span>查看我的自选</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">我的自选</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/02/23/k1AOeTfxtPZHluo.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="高级功能" tabindex="-1"><a class="header-anchor" href="#高级功能"><span>高级功能</span></a></h3>
<h4 id="对比个股" tabindex="-1"><a class="header-anchor" href="#对比个股"><span>对比个股</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">对比个股 A500 沪深300 上证指数 中证白酒</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/06/02/a41cqb2rGzTvSWy.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查看k线图" tabindex="-1"><a class="header-anchor" href="#查看k线图"><span>查看K线图</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">个股 东方财富 日k</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="https://s2.loli.net/2025/05/16/Mlz5qEyKBe16SdR.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的数据类型" tabindex="-1"><a class="header-anchor" href="#支持的数据类型"><span>支持的数据类型</span></a></h3>
<ul>
<li><strong>A股</strong>: 沪深主板、创业板、科创板</li>
<li><strong>指数</strong>: 上证指数、深证成指、创业板指等</li>
<li><strong>ETF</strong>: 各类交易型开放式指数基金</li>
<li><strong>基金</strong>: 公募基金持仓信息</li>
<li><strong>港股</strong>: 香港交易所股票</li>
<li><strong>美股</strong>: 美国交易所股票（通过VIX）</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>数据更新</strong>: 实时获取最新股票数据</li>
<li><strong>图片生成</strong>: 自动生成美观的数据可视化图表</li>
<li><strong>缓存管理</strong>: 智能缓存减少API调用</li>
<li><strong>错误重试</strong>: 网络异常时自动重试</li>
</ul>
<h3 id="数据源" tabindex="-1"><a class="header-anchor" href="#数据源"><span>数据源</span></a></h3>
<ul>
<li><strong>东方财富</strong>: 主要数据源，提供实时行情</li>
<li><strong>新浪财经</strong>: 市盈率等基本面数据</li>
<li><strong>雪球</strong>: 新闻和热点信息</li>
<li><strong>自有API</strong>: 插件内置的数据处理服务</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>数据延迟</strong>: 股票数据有15分钟左右的延迟，非实时数据</li>
<li><strong>API限制</strong>: 频繁请求可能触发API限制，请合理使用</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接来获取数据</li>
<li><strong>图片大小</strong>: 生成的图片可能较大，部分平台可能压缩</li>
<li><strong>自选限制</strong>: 单个用户自选股票数量有限制</li>
<li><strong>管理员功能</strong>: 新闻订阅功能仅限管理员使用</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>插件支持以下配置选项（通过GsCore配置）：</p>
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
<td>cache_timeout</td>
<td>number</td>
<td>300秒</td>
<td>数据缓存时间</td>
</tr>
<tr>
<td>max_favorites</td>
<td>number</td>
<td>20</td>
<td>最大自选股票数量</td>
</tr>
<tr>
<td>image_quality</td>
<td>string</td>
<td>high</td>
<td>图片质量（high/medium/low）</td>
</tr>
<tr>
<td>auto_clean_cache</td>
<td>boolean</td>
<td>true</td>
<td>是否自动清理缓存</td>
</tr>
<tr>
<td>news_check_interval</td>
<td>number</td>
<td>5分钟</td>
<td>新闻检查间隔</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>SayuStock插件基于GsCore框架开发，能够无缝集成到多种机器人平台。插件使用playwright进行网页渲染，plotly进行数据可视化，pandas进行数据处理，确保功能的稳定性和美观性。</p>
</div>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>本插件仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。</p>
</div>
</div></template>


