<template><div><h1 id="火烧云预报" tabindex="-1"><a class="header-anchor" href="#火烧云预报"><span>火烧云预报</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: hsy</p>
<p><strong>功能描述</strong>: 查询和订阅城市朝霞(日出)和晚霞(日落)预报</p>
<p><strong>插件名称</strong>: sunsetbot</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl7ApHgsaVMCp8ZDgSo12hLaqkeJSoiGgMDBKGn4UlAT4IQGjL6Labf1LWy75aMU59Duzv+3/5nO9uBYOktnubwCsXgI7EiyZmOASu/77s59yGrqMM/lshATRPXcTfnSBLAMYww79inzbYQPzoNhbG2Z4sVMKGhASRn+SAbWeW/bi7gqKsIJ73da0FEb5HJpTkHNsnHT9lNOUJ7uV3ylfYZ7wJKSIGcF1C4ibRI0JD09qBA0y2W4nMLnw5LIp6S1mk7QCVZWRZlXAqrT0fp60WUSwuFde3zuhmHsHWz93LUATUqoMNrRp7f6bLLlQpTLUB7SBlrko5ICp5GIUa5YwyGmyOWFkh7aAQxY/S7SqhgjaBchaI/pAi6lf7Z+L2qrVnOXHljjS+enqdQWLdEJF6ETHvME1nfDeNTMWR1pzU0uz6B/PNjXafSuzGpxcy99MOplY9owxgWre73JZfDPx+MR+eb04pnhgWJsfdyvgO6/zN50te1k6A/FHgmG"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>hsy.query [城市名]  # 查询指定城市的火烧云预报，不指定城市则使用默认城市</span></span>
<span class="line"><span>hsy.sub &#x3C;城市名>   # 订阅指定城市的自动预报</span></span>
<span class="line"><span>hsy.unsub &#x3C;城市名> # 取消订阅指定城市的自动预报</span></span>
<span class="line"><span>hsy.list          # 查看已订阅的城市列表</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>城市名</td>
<td>文本</td>
<td>否</td>
<td>要查询/订阅的城市名称</td>
<td>重庆</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="查询火烧云预报" tabindex="-1"><a class="header-anchor" href="#查询火烧云预报"><span>查询火烧云预报</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hsy.query 重庆</chat-message>
<chat-message nickname="bot" type="bot">
<p>🌄 火烧云预报 - 重庆 🌅<br>
═════════════════<br>
今日朝霞<br>
• GFS: 0.0（不烧）<br>
• EC: 0.0（不烧）</p>
<p>今日晚霞<br>
• GFS: 0.0（不烧）<br>
• EC: 0.0（不烧）</p>
<p>明日朝霞<br>
• GFS: 0.0（不烧）<br>
• EC: 0.0（不烧）</p>
<p>明日晚霞<br>
• GFS: 0.007（微烧）<br>
• EC: 0.0（不烧）</p>
<p>═════════════════</p>
</chat-message>
</chat-panel>
<h3 id="订阅城市预报" tabindex="-1"><a class="header-anchor" href="#订阅城市预报"><span>订阅城市预报</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hsy.sub 重庆</chat-message>
<chat-message nickname="bot" type="bot">已订阅重庆的自动预报，将在当前频道推送。</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<ul>
<li><strong>预报模型</strong>: 使用GFS和EC两种气象模型</li>
<li><strong>预报内容</strong>: 提供朝霞(rise)和晚霞(set)预报</li>
<li><strong>预报时段</strong>: 当日和次日预报</li>
<li><strong>自动推送</strong>: 每3小时自动推送订阅城市的最新预报</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>城市名称</strong>: 只支持中文、字母、数字和空格</li>
<li><strong>预报准确性</strong>: 预报结果仅供参考，实际天气可能有所不同</li>
<li><strong>订阅限制</strong>: 每个用户在每个频道最多可订阅5个城市</li>
<li><strong>推送时间</strong>: 每日6:00、9:00、12:00、15:00、18:00、21:00自动推送</li>
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
<td>apiUrl</td>
<td>string</td>
<td><a href="https://sunsetbot.top/" target="_blank" rel="noopener noreferrer">https://sunsetbot.top/</a></td>
<td>API地址</td>
</tr>
<tr>
<td>defaultCity</td>
<td>string</td>
<td>重庆</td>
<td>默认查询城市</td>
</tr>
</tbody>
</table>
</div></template>


