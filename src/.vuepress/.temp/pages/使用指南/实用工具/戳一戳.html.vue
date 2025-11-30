<template><div><h1 id="戳一戳" tabindex="-1"><a class="header-anchor" href="#戳一戳"><span>戳一戳</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: poke</p>
<p><strong>功能描述</strong>: 戳一戳</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xYR7NbyASfFY0qYETo2HAlVqsCVQ1KNEJURDQOBglDR8KagJcEIDRt/FtNv6Frbd8lGKc2h35//b/0xne5iRz5JpPqdAJBoAK+Kc0Ryi8vuBs3Me+ULiKMdn0xARpcK5k/KkSeBYVh91rVPG2xgfXATLWtoqJUipgN+AllPCcR44+71jLaIFSRFPBK/Tkg5bIJ9N8gpqVfSbjpeyg3Z1r+Ip7THcB46SxXxaRJ0SUqd+Q8rV/QrJcHyKzypCjpAlISFv1LSDiXFYIhRZzvh72lwv+4wDQexZA3Q2LGvtIPhz1wY0LaPieFeb3WrzadCBaIehXaQDjCSEZQVOQyG9UjVHI0xRqyulXLQLGDAHPaTWMEYyDkIyLtMDXEr7bP9e1NetFi59MCeX9m9TrS9bYmIOwsRc5gnM76b+qBrzBlJb21yeQft4sC5U718ZtdL2XgagNyr6rKlPimbvepvL8J+PxyPyzOnFNcMDxdjmuF8B3X8Z/dl62/HAH4rXChE="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>poke &#x3C;次数> &#x3C;用户></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>次数</td>
<td>文本</td>
<td>否</td>
<td>戳一戳的次数</td>
<td>1</td>
</tr>
<tr>
<td>用户</td>
<td>@</td>
<td>否</td>
<td>用户id</td>
<td>@马化腾</td>
</tr>
<tr>
<td>用户</td>
<td>ID</td>
<td>否</td>
<td>用户id</td>
<td>10001</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="基本用法" tabindex="-1"><a class="header-anchor" href="#基本用法"><span>基本用法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">poke</chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
<h4 id="基本用法-次数-5" tabindex="-1"><a class="header-anchor" href="#基本用法-次数-5"><span>基本用法 <code v-pre>次数 5</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">poke 5</chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">用户</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
<h4 id="指定用户" tabindex="-1"><a class="header-anchor" href="#指定用户"><span>指定用户 <code v-pre>@</code></span></a></h4>
<chat-panel>
<chat-message nickname="马化腾" type="user">大家好，我是马化腾</chat-message>
<chat-message nickname="用户" type="user">poke 1 <span style="color: #3175de;">@马化腾</span></chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
<h4 id="指定用户-id" tabindex="-1"><a class="header-anchor" href="#指定用户-id"><span>指定用户 <code v-pre>ID</code></span></a></h4>
<chat-panel>
<chat-message nickname="马化腾" type="user">大家好，我是马化腾</chat-message>
<chat-message nickname="用户" type="user">poke 1 <span style="color: #3175de;">10001</span></chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
<h4 id="指定用户-次数-5" tabindex="-1"><a class="header-anchor" href="#指定用户-次数-5"><span>指定用户 <code v-pre>@</code> <code v-pre>次数 5</code></span></a></h4>
<chat-panel>
<chat-message nickname="马化腾" type="user">大家好，我是马化腾</chat-message>
<chat-message nickname="用户" type="user">poke 5 <span style="color: #3175de;">@马化腾</span></chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
<h4 id="指定用户-id-次数-5" tabindex="-1"><a class="header-anchor" href="#指定用户-id-次数-5"><span>指定用户 <code v-pre>ID</code> <code v-pre>次数 5</code></span></a></h4>
<chat-panel>
<chat-message nickname="马化腾" type="user">大家好，我是马化腾</chat-message>
<chat-message nickname="用户" type="user">poke 5 <span style="color: #3175de;">10001</span></chat-message>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; width: 100%; margin: 2px 0;">
<ChatMessage nickname="系统" type="system"><span style="color: #3175de;">bot</span>戳了戳<span style="color: #3175de;">马化腾</span></ChatMessage>
</div>
<chat-message nickname="bot" type="bot">success！</chat-message>
</chat-panel>
</div></template>


