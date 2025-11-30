<template><div><h1 id="b站搜索" tabindex="-1"><a class="header-anchor" href="#b站搜索"><span>b站搜索</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: b站搜索</p>
<p><strong>功能描述</strong>: b站搜索</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJyNku9v0kAYx9/zV1z2Hs3emyWsviBhoe0CrxpfFDhtzdY2pagvt6gLEXFzYOIPgmOgQ5mF+AIXWPR/MfSu/hcedzfg1mr2vGh793zu+1yf53t/x35cNHTXA1vbCUAir+FmH1V/3KMr+ihXCg9c3THAlmlVntAtYTsFNFUN/FNyCg+G7OBVqCrJLbegVUpEBbJ2CT4sA23+vkU+tiuWZ+5CUWlBbxJQd4q6h1r14EVHpOaR5XkxI5QWBCWgZWyzbJioc4Da46hghuejmZSs6SXd8aCbtC1YsK/VnIec0wrmjlmGuls0omlF0ZyK40APQjd64f/37S7QcO0cD2qS4dq7MK4fUlpjyTsFdwNdfEcfG8HlG9R4Jc5EqJEHyeQGmRxdqCpZgbXfr08AGlfR/vD2bFKbTcdrFMpSJsuRDpAtuGl74NH6elA/DH2fUZmllzIcPQUMCM+6qH3EsJRMkZTMmS5gpWaXJ3/2jlelrlR6IBw9JX5dNhgdHi8uJ+coLOc4/QmEv5rBhzaevmPzjJP8zCUXQ1lVVBTKKgqHz4hiC/dr7AhjpDRlpDRn+rwqaz6eNlC7Fa/25Sb3+7qA5kIEXf57/F8PAGrt4Wk16D3DRweB/xJVeb9F4XMwu3hP/MO4+Il8A0GjHkyawWg/7D6PU/H/YQFmFMEtQy7GbMWw66YbAfT2J+5NVtuWT/wFphuelA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>b站搜索 [内容] &#x3C;类型> &#x3C;排序></span></span></code></pre>
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
<td>内容</td>
<td>文本</td>
<td>是</td>
<td>要搜索的内容</td>
<td>麦麦</td>
</tr>
<tr>
<td>类型</td>
<td>文本</td>
<td>否</td>
<td>要搜索的类型</td>
<td>用户</td>
</tr>
<tr>
<td>排序</td>
<td>文本</td>
<td>否</td>
<td>排序方法</td>
<td>粉丝量由高到低</td>
</tr>
</tbody>
</table>
<h3 id="各类型的排序方法" tabindex="-1"><a class="header-anchor" href="#各类型的排序方法"><span>各类型的排序方法</span></a></h3>
<table>
<thead>
<tr>
<th>类型</th>
<th>排序选项</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>综合</strong></td>
<td>最多播放、最多点击、最多评论、最多弹幕、最多收藏、最新发布</td>
</tr>
<tr>
<td><strong>视频</strong></td>
<td>最多播放、最新发布、最多弹幕、最多收藏</td>
</tr>
<tr>
<td><strong>番剧</strong></td>
<td></td>
</tr>
<tr>
<td><strong>影视</strong></td>
<td></td>
</tr>
<tr>
<td><strong>直播</strong></td>
<td>最新开播、主播、直播间、直播间最新开播</td>
</tr>
<tr>
<td><strong>专栏</strong></td>
<td>最新发布、最多点击、最多喜欢、最多评论</td>
</tr>
<tr>
<td><strong>用户</strong></td>
<td>粉丝由高到低、粉丝由低到高、等级由高到低、等级由低到高</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="b站搜索-麦麦" tabindex="-1"><a class="header-anchor" href="#b站搜索-麦麦"><span>b站搜索 <code v-pre>麦麦</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/b站搜索_麦麦.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="b站搜索-用户-麦麦" tabindex="-1"><a class="header-anchor" href="#b站搜索-用户-麦麦"><span>b站搜索 <code v-pre>用户</code> <code v-pre>麦麦</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 用户</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/b站搜索_2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="b站搜索-用户-麦麦-排序方法-粉丝由高到低" tabindex="-1"><a class="header-anchor" href="#b站搜索-用户-麦麦-排序方法-粉丝由高到低"><span>b站搜索 <code v-pre>用户</code> <code v-pre>麦麦</code> 排序方法 <code v-pre>粉丝由高到低</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 用户 粉丝由高到低</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/b站搜索_3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="b站搜索-麦麦-视频-排序方法-最多播放" tabindex="-1"><a class="header-anchor" href="#b站搜索-麦麦-视频-排序方法-最多播放"><span>b站搜索 <code v-pre>麦麦</code> <code v-pre>视频</code> 排序方法 <code v-pre>最多播放</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 视频 最多播放</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/b站搜索_4.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
</div></template>


