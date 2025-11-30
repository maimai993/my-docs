<template><div><h1 id="获取热搜" tabindex="-1"><a class="header-anchor" href="#获取热搜"><span>获取热搜</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: hotof.[平台]</p>
<p><strong>功能描述</strong>: 获取各平台热搜，支持自定义显示数量</p>
<p><strong>插件名称</strong>: hot-search</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwlAQhvc8xcQ9Gl7ApLjBQMBCWDUuClSL0ZZAUZciSoiGgICJUUK4KSgKuAEDRt/FtKf1LeyNSy/Ooj1n5jv/zJk5e4fsSZQmkxz4gg6QLUyI1R7KT3bVnfpJpSP7STJBgy/OpE9Vl8GNAYHjwqAlnxL7Q+3g3HBcji1dFBNzWAX8bIw6SAGh/NflRTDNcPEjyqi0oN0ySCaiJIdqBeGqaaQU8+txY8SQ2iC4BYSXjafoOGrmUH1sFfTqcWsECxBkjExwVNLJMlSENeVUzBMiaJZzpigyGaWtJZnXizLD4HRuyv1TNzgu72Dt56YBaJxHmeEGP73mZ+M1FfKrjF9HmhBgKDfLwbHLJRSK0mCgUd7lRL062gINkLptVC9pGBZQESygM23QUvGfjd+z8qrUXKUD0iirvJpieVGSJ6QinpDOPAK2sy0NJ+j93B54AnQ7QoWB0LkQSzl7pgvSd1V4qIuzCqrX7ErpAf9xLz+KVRXzhZ5BqBSEaVUYZaT2pZ3Kyz8d1PpsaHZfF9OmomHmmb0CuvsSO1Mx+4ZKetlhxx/VYiJJ"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>hotof.[平台] [-n &#x3C;数量>]</span></span></code></pre>
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
<td>平台</td>
<td>文本</td>
<td>是</td>
<td>要获取热搜的平台</td>
<td>bili</td>
</tr>
<tr>
<td>-n</td>
<td>数字</td>
<td>否</td>
<td>显示的热搜数量，默认10条</td>
<td>-n 5</td>
</tr>
</tbody>
</table>
<h3 id="支持平台" tabindex="-1"><a class="header-anchor" href="#支持平台"><span>支持平台</span></a></h3>
<table>
<thead>
<tr>
<th>平台</th>
<th>指令名称</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>bilibili</strong></td>
<td>hotof.bili</td>
<td>B站热搜榜</td>
</tr>
<tr>
<td><strong>抖音</strong></td>
<td>hotof.douyin</td>
<td>抖音热点榜和实时上升热点</td>
</tr>
<tr>
<td><strong>知乎</strong></td>
<td>hotof.zhihu</td>
<td>知乎热搜榜</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="获取-b站-热搜" tabindex="-1"><a class="header-anchor" href="#获取-b站-热搜"><span>获取 <code v-pre>b站</code> 热搜</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hotof.bili</chat-message>
<chat-message nickname="bot" type="bot">
<p>=1= [热]拆解TES外战背后的问题<br>
=2= [新]海贼王伊姆与戴维一族的约定<br>
=3= [无]黄金还有投资机会吗<br>
=4= [新]AI还原福建舰电磁弹射全过程<br>
=5= [热]解读冯小刚电影芳华<br>
=6= [无]TES发文告别S赛<br>
=7= [无]马思纯 重获新生<br>
=8= [新]2025年金摇杆大奖投票开启<br>
=9= [无]片仔癀业绩爆雷意味着什么<br>
=10= [无]第三人称逃离鸭科夫</p>
</chat-message>
</chat-panel>
<h3 id="获取-抖音-热搜" tabindex="-1"><a class="header-anchor" href="#获取-抖音-热搜"><span>获取 <code v-pre>抖音</code> 热搜</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hotof.douyin</chat-message>
<chat-message nickname="bot" type="bot">
<p>■热点榜■<br>
=1= 金永南逝世(1205.10w, 视频3)<br>
=2= 馆长帮赖清德寻根(1157.78w, 视频3)<br>
=3= APEC中国年即将开启(1146.51w, 视频5)<br>
=4= 中国空间站可以吃烧烤了(1141.55w, 视频6)<br>
=5= 队友炸鱼全红婵表情亮了(1064.20w, 视频3)<br>
=6= 鬼灭之刃无限城篇定档(1036.27w, 视频3)<br>
=7= 把装修的坑全踩了一遍(908.49w, 视频2)<br>
=8= 月亮月亮你别笑我(898.53w, 视频10)<br>
=9= 儿时的公益广告照进现实(897.14w, 视频1)<br>
=10= 沉浸式感受永子制作过程(878.68w, 视频1)<br>
■实时上升热点■</p>
<ul>
<li>长春亚泰降级后致歉(视频1)</li>
<li>山河枕这一幕梦回杨门女将(视频3)</li>
<li>关晓彤玫瑰礼花变装(视频1)</li>
<li>刘芮麟新手奶爸的一天(视频1)</li>
<li>LPL的S15结束了(视频5)</li>
</ul>
</chat-message>
</chat-panel>
<h3 id="获取-知乎-热搜" tabindex="-1"><a class="header-anchor" href="#获取-知乎-热搜"><span>获取 <code v-pre>知乎</code> 热搜</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hotof.zhihu</chat-message>
<chat-message nickname="bot" type="bot">
<p>知乎热搜🔥</p>
<ul>
<li>湖人vs热火</li>
<li>哪句话让你突然沉默了很久</li>
<li>TES对战T1</li>
<li>有哪些非常冷门且令人意外的知识</li>
<li>常年独居的人靠什么抵抗孤独</li>
<li>灰熊vs湖人</li>
<li>有什么尴尬到爆的经历</li>
<li>不鸡娃的结果是什么</li>
<li>你心目中排名第一的饮料是什么</li>
<li>钱可以成为一个人的底气吗</li>
</ul>
</chat-message>
</chat-panel>
<h3 id="自定义显示数量" tabindex="-1"><a class="header-anchor" href="#自定义显示数量"><span>自定义显示数量</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">hotof.bili -n 5</chat-message>
<chat-message nickname="bot" type="bot">
<p>=1= [热]拆解TES外战背后的问题<br>
=2= [新]海贼王伊姆与戴维一族的约定<br>
=3= [无]黄金还有投资机会吗<br>
=4= [新]AI还原福建舰电磁弹射全过程<br>
=5= [热]解读冯小刚电影芳华</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>B站</strong>: 官方API接口，获取实时热搜榜</li>
<li><strong>抖音</strong>: 官方API接口，获取热点榜和实时上升热点</li>
<li><strong>知乎</strong>: 官方API接口，获取热搜话题</li>
</ul>
<h3 id="功能特点" tabindex="-1"><a class="header-anchor" href="#功能特点"><span>功能特点</span></a></h3>
<ul>
<li><strong>实时更新</strong>: 直接从平台API获取最新热搜数据</li>
<li><strong>自定义数量</strong>: 支持通过-n参数指定显示的热搜数量</li>
<li><strong>图片支持</strong>: 抖音热搜支持显示相关图片</li>
<li><strong>分类显示</strong>: 抖音热搜分为热点榜和实时上升热点</li>
</ul>
<h3 id="数据格式" tabindex="-1"><a class="header-anchor" href="#数据格式"><span>数据格式</span></a></h3>
<ul>
<li><strong>B站</strong>: 显示排名、热度标签和关键词</li>
<li><strong>抖音</strong>: 显示排名、热度值、视频数量和图片</li>
<li><strong>知乎</strong>: 显示热搜话题列表</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问各平台API</li>
<li><strong>API限制</strong>: 各平台API可能有访问频率限制</li>
<li><strong>数据时效</strong>: 热搜数据实时变化，结果可能随时间变化</li>
<li><strong>图片加载</strong>: 抖音热搜图片需要网络加载，可能影响响应速度</li>
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
<td>command</td>
<td>string</td>
<td>&quot;hotof&quot;</td>
<td>指令前缀字段</td>
</tr>
<tr>
<td>endpoints</td>
<td>object</td>
<td>各平台API地址</td>
<td>平台获取热搜的API地址</td>
</tr>
<tr>
<td>isUseImage</td>
<td>boolean</td>
<td>true</td>
<td>是否使用图片消息</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>获取热搜功能基于各平台官方API实现，能够准确获取实时热搜数据。支持B站、抖音、知乎三大主流平台的热搜查询，满足日常娱乐和信息获取需求。</p>
</div>
</div></template>


