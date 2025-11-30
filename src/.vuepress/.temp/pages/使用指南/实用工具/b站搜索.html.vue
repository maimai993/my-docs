<template><div><h1 id="b站搜索" tabindex="-1"><a class="header-anchor" href="#b站搜索"><span>b站搜索</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: b站搜索</p>
<p><strong>功能描述</strong>: 在Bilibili平台进行多类型内容搜索，支持视频、用户、专栏等多种搜索类型</p>
<p><strong>插件名称</strong>: bilisearch</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9k0tv2kAQx+98ilHutMq9imS3l4oI7CBOVg8GtsVValvGtD02fURRKxQaOPSBaHi0SZsW0igiEeTxXSJ77XyLLLuLycYkc7B3Z377n9XM7NNV61WhpDsuLK8kgFhOCxq7eOPoCd3RT7mSf+bodgmWDbPymroEtwSaqvr9DjkV7A3YwampKonNXMgsJuICaauInpdBm/zvkcVKxXSNF0hUimiZgLpd0F3crPof2yI1sTSPixEhtSD4ELSUZZRLBm6v49YwLpji8XhEymh6Ubdd5CQtE+WtGzknJme1vLFqlJHuFErxsKJodsW2kYuQE7/w3XV7BJpMpCfyICmPxeMy8UThB3lnCdeawWFH4KYpIvkcJJNLpGl0o6pkBwsXn7cBDzfw2uC+N/rkjYcLFEpTJs2RNmRMJFsuvFxc9KubYb/PqNRsjFIc7QADwp0ubtUYJmUoImU40wWWyjvZvnyzdV1qqtKDcP8dGdVZbfHmVnQ5OUthOcvpnxAOjvD/t9fLxUmyYixZcPoXhOcN/3uLVSwY13GrOV93B7zTc3KLqIX4+AD/qDNYUSisKBzencpS5i7Z35wMxl/Z5M2rwB/wjr+RB+D33ge19fl13AO/XvVHDX9/Lex+mKfy95bGsfYKPf7HxdgwMOzmqPQBfzkLeqN46XKJK+74eZg="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>b站搜索 &#x3C;内容> [类型] [排序]</span></span></code></pre>
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
<td>要搜索的关键词</td>
<td>麦麦</td>
</tr>
<tr>
<td>类型</td>
<td>文本</td>
<td>否</td>
<td>搜索内容类型，默认为综合</td>
<td>用户</td>
</tr>
<tr>
<td>排序</td>
<td>文本</td>
<td>否</td>
<td>搜索结果排序方式</td>
<td>粉丝由高到低</td>
</tr>
</tbody>
</table>
<h3 id="搜索类型说明" tabindex="-1"><a class="header-anchor" href="#搜索类型说明"><span>搜索类型说明</span></a></h3>
<table>
<thead>
<tr>
<th>类型</th>
<th>说明</th>
<th>支持的排序选项</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>综合</strong></td>
<td>跨类型综合搜索</td>
<td>最多播放、最多点击、最多评论、最多弹幕、最多收藏、最新发布</td>
</tr>
<tr>
<td><strong>视频</strong></td>
<td>搜索视频内容</td>
<td>最多播放、最新发布、最多弹幕、最多收藏</td>
</tr>
<tr>
<td><strong>番剧</strong></td>
<td>搜索番剧内容</td>
<td>默认排序</td>
</tr>
<tr>
<td><strong>影视</strong></td>
<td>搜索影视内容</td>
<td>默认排序</td>
</tr>
<tr>
<td><strong>直播</strong></td>
<td>搜索直播内容</td>
<td>最新开播、主播、直播间、直播间最新开播</td>
</tr>
<tr>
<td><strong>专栏</strong></td>
<td>搜索专栏文章</td>
<td>最新发布、最多点击、最多喜欢、最多评论</td>
</tr>
<tr>
<td><strong>用户</strong></td>
<td>搜索用户账号</td>
<td>粉丝由高到低、粉丝由低到高、等级由高到低、等级由低到高</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本搜索" tabindex="-1"><a class="header-anchor" href="#基本搜索"><span>基本搜索</span></a></h3>
<h4 id="搜索-麦麦-相关内容" tabindex="-1"><a class="header-anchor" href="#搜索-麦麦-相关内容"><span>搜索 <code v-pre>麦麦</code> 相关内容</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦</chat-message>
<chat-message nickname="bot" type="bot">
[图片：麦麦综合搜索结果]
</chat-message>
</chat-panel>
<h3 id="指定类型搜索" tabindex="-1"><a class="header-anchor" href="#指定类型搜索"><span>指定类型搜索</span></a></h3>
<h4 id="搜索-麦麦-用户" tabindex="-1"><a class="header-anchor" href="#搜索-麦麦-用户"><span>搜索 <code v-pre>麦麦</code> 用户</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 用户</chat-message>
<chat-message nickname="bot" type="bot">
[图片：麦麦用户搜索结果]
</chat-message>
</chat-panel>
<h3 id="指定排序方式" tabindex="-1"><a class="header-anchor" href="#指定排序方式"><span>指定排序方式</span></a></h3>
<h4 id="搜索-麦麦-用户并按粉丝数排序" tabindex="-1"><a class="header-anchor" href="#搜索-麦麦-用户并按粉丝数排序"><span>搜索 <code v-pre>麦麦</code> 用户并按粉丝数排序</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 用户 粉丝由高到低</chat-message>
<chat-message nickname="bot" type="bot">
[图片：麦麦用户按粉丝数排序结果]
</chat-message>
</chat-panel>
<h4 id="搜索-麦麦-视频并按播放量排序" tabindex="-1"><a class="header-anchor" href="#搜索-麦麦-视频并按播放量排序"><span>搜索 <code v-pre>麦麦</code> 视频并按播放量排序</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站搜索 麦麦 视频 最多播放</chat-message>
<chat-message nickname="bot" type="bot">
[图片：麦麦视频按播放量排序结果]
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的搜索类型" tabindex="-1"><a class="header-anchor" href="#支持的搜索类型"><span>支持的搜索类型</span></a></h3>
<ul>
<li><strong>综合搜索</strong>: 跨类型综合结果</li>
<li><strong>视频搜索</strong>: 视频内容搜索</li>
<li><strong>用户搜索</strong>: UP主和用户搜索</li>
<li><strong>专栏搜索</strong>: 文章内容搜索</li>
<li><strong>直播搜索</strong>: 直播内容搜索</li>
<li><strong>番剧搜索</strong>: 番剧内容搜索</li>
<li><strong>影视搜索</strong>: 影视内容搜索</li>
</ul>
<h3 id="搜索特性" tabindex="-1"><a class="header-anchor" href="#搜索特性"><span>搜索特性</span></a></h3>
<ul>
<li><strong>实时搜索</strong>: 基于Bilibili官方API，结果实时更新</li>
<li><strong>多维度排序</strong>: 支持按播放量、粉丝数、发布时间等多种排序方式</li>
<li><strong>结果可视化</strong>: 搜索结果以图片形式呈现，便于查看</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>关键词为空</strong>: 当用户未输入搜索关键词时提示</li>
<li><strong>网络错误</strong>: 当API请求失败时提示</li>
<li><strong>无结果</strong>: 当搜索无结果时返回友好提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问Bilibili API</li>
<li><strong>结果时效性</strong>: 搜索结果基于Bilibili平台实时数据</li>
<li><strong>图片大小</strong>: 搜索结果图片会自动优化以适应消息大小限制</li>
<li><strong>API限制</strong>: 受Bilibili API调用频率限制</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>b站搜索功能基于Bilibili官方API实现，能够准确获取最新的搜索结果，支持多种内容类型和排序方式。</p>
</div>
</div></template>


