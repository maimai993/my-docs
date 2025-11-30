<template><div><h1 id="天气查询" tabindex="-1"><a class="header-anchor" href="#天气查询"><span>天气查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 天气</p>
<p><strong>功能描述</strong>: 天气查询</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xYQ7Gl7ABDxCaErg1HgoUKV+tNAW0ZtEJURDQOBglDR8KagJcEIDRt/FtNv6Fm4/+CjFObQ7M7/9z+zs7h/z+WSaFiQIRz2ALU5pjQEqve+ZnvkRc4kDgc6kIcxyuTMz5AgHgCJJddjBu7S3kbVxbiSJc8sQw6U8boEIn2IORaCM/xZeRHOcxJ4wTqUFHcQgnUnSEmqW1Zu2kzIsYuedGUdph+AuUCGeFdMsaheRPHELhuy8OxMgKDpFZyRG8PEck+DXahpGxKg8Q0tpjGSzPoFmuQSfF4/O3d2trxcdx8Hn28GjNB2SxB54f+5agCYlVBhtK9NbZTbxmlDEZCI20gaCY4K8BKd+v1qu6MOhRYWWlxuy0Q5YgN7vIrlqYQHCRAKEzXTBKqV8tn4vaqtSc5Ue6ONL4wFVaouWiJiJEDGbeQL9u6E+ytqsjuTmJpVnUD4e8NWqvSutWtzcSx/UelmdNtRxQe9eb1IZ/HN4a0SOOb3YYtZALWx93K+A7r+03nS17bjnD9HBDhQ="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>abbr [地区] &#x3C;天></span></span></code></pre>
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
<td>地区</td>
<td>文本</td>
<td>是</td>
<td>要查询天气的地区</td>
<td>myt</td>
</tr>
<tr>
<td>天</td>
<td>文本</td>
<td>是</td>
<td>要查询最近？天</td>
<td>1</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="查询-北京-天气" tabindex="-1"><a class="header-anchor" href="#查询-北京-天气"><span>查询 <code v-pre>北京</code> 天气</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京</chat-message>
<chat-message nickname="bot" type="bot">
2025-10-21（今天）
    天气：晴 转 多云
    温度：2 - 13 ℃
    湿度：33 %
    北风2级
<p>2025-10-22<br>
天气：多云 转 小雨<br>
温度：2 - 10 ℃<br>
湿度：42 %<br>
北风2级</p>
<p>2025-10-23<br>
天气：多云<br>
温度：3 - 12 ℃<br>
湿度：55 %<br>
北风1级</p>
</chat-message>
</chat-panel>
<h4 id="查询-北京-最近1天-天气" tabindex="-1"><a class="header-anchor" href="#查询-北京-最近1天-天气"><span>查询 <code v-pre>北京</code> <code v-pre>最近1天</code> 天气</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京 1</chat-message>
<chat-message nickname="bot" type="bot">
<p>2025-10-21（今天）<br>
天气：晴 转 多云<br>
温度：2 - 13 ℃<br>
湿度：33 %<br>
北风2级</p>
</chat-message>
</chat-panel>
</div></template>


