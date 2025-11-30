<template><div><h1 id="搜图" tabindex="-1"><a class="header-anchor" href="#搜图"><span>搜图</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: [平台]搜图</p>
<p><strong>功能描述</strong>: 根据文字搜索一张图片，支持多个搜索平台</p>
<p><strong>插件名称</strong>: baidu-image-search</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9kktP20AQx+/5FCPubsW9QrLbSxSUxEQ5WT1sEpe4KnbkOG2PpbQ8FREgQjyiiDyA8FACEgooQfBdUHZtvgUb7yZgbJiDvTvzm//szuy3H8avdBaZFkzPhIBaUrHLLbJ8/dXduZ98ITVrolwWpjW98Nt1edwiKLKM23WaZZ91WOLIZJnGnl2qngn5BaJGRv2eB2X4/0AXMwXd0uZUr9KYliiIcmlkkUoRr9a81NCiPO6NeEp7BD+DEjG0fFYjtUVS7foFIzzuj4gxBWVQzlJNwdDVlPGq5tCkhJJCWqYgaHNoVhXyKjLTWf/R3u/QF1Bwc/txoSXGw0HXpm4F79/ZK0ukVLGv6p9S5lQAOio0LpIEQZiiQ3I3skx3MPGwcQCku0zmOx8HvbVBvzvhQlGXiXKkBjFdlQwLfk5O4uK6024zKvL8bCIcrQMDnOMGqZYYJsZcRIxxpgGs1OD24PHP5kupkUoTnIsF+jT9vSTrm+NDSgk3SUrwrENwOtfk8u+4ebx8PMzqx8McPALnvoz3q6yJdn+LVCvBksectPu77FUEnbYFg5s92nrc/GeXFoPvfAJ4q4h7ZXwx7zT+B6mcvtFkNgrPPM64GBscw16P9RzIzp3d7LE7MiYZegK2OViE"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>[平台]搜图 &#x3C;keyword></span></span></code></pre>
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
<td>keyword</td>
<td>文本</td>
<td>是</td>
<td>要搜索的关键词</td>
<td>麦芽糖</td>
</tr>
</tbody>
</table>
<h3 id="支持平台" tabindex="-1"><a class="header-anchor" href="#支持平台"><span>支持平台</span></a></h3>
<table>
<thead>
<tr>
<th>类型</th>
<th>指令名称</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>百度</strong></td>
<td>百度搜图</td>
<td>使用百度图片搜索</td>
</tr>
<tr>
<td><strong>搜狗</strong></td>
<td>搜狗搜图</td>
<td>使用搜狗图片搜索</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="百度搜图" tabindex="-1"><a class="header-anchor" href="#百度搜图"><span>百度搜图</span></a></h3>
<h4 id="百度搜图-麦芽糖" tabindex="-1"><a class="header-anchor" href="#百度搜图-麦芽糖"><span>百度搜图 <code v-pre>麦芽糖</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">百度搜图 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/搜图_百度麦芽糖.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="搜狗搜图" tabindex="-1"><a class="header-anchor" href="#搜狗搜图"><span>搜狗搜图</span></a></h3>
<h4 id="搜狗搜图-麦芽糖" tabindex="-1"><a class="header-anchor" href="#搜狗搜图-麦芽糖"><span>搜狗搜图 <code v-pre>麦芽糖</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">搜狗搜图 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/搜图_搜狗麦芽糖.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="搜索能力" tabindex="-1"><a class="header-anchor" href="#搜索能力"><span>搜索能力</span></a></h3>
<ul>
<li><strong>多平台支持</strong>: 支持百度、搜狗搜索平台</li>
<li><strong>自动切换</strong>: 具备自动切换至备用搜索接口的能力，确保在主要接口不可用时的稳定性</li>
<li><strong>快速响应</strong>: 提供快速的图片搜索体验</li>
</ul>
<h3 id="图片处理" tabindex="-1"><a class="header-anchor" href="#图片处理"><span>图片处理</span></a></h3>
<ul>
<li><strong>单张返回</strong>: 每次搜索返回一张相关图片</li>
<li><strong>质量保证</strong>: 返回高质量的搜索结果图片</li>
<li><strong>格式支持</strong>: 支持常见的图片格式</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>网络异常</strong>: 当API请求失败时提示</li>
<li><strong>无结果</strong>: 当搜索无结果时返回友好提示</li>
<li><strong>参数缺失</strong>: 当用户未输入关键词时提示</li>
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
<td>API端点</td>
<td>string</td>
<td>自动选择</td>
<td>图片搜索API端点</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络依赖</strong>: 需要稳定的网络连接来访问图片搜索API</li>
<li><strong>结果随机</strong>: 每次搜索返回的图片可能不同</li>
<li><strong>内容限制</strong>: 搜索结果受各平台内容政策限制</li>
<li><strong>图片质量</strong>: 返回的图片质量可能因搜索平台而异</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>搜图功能基于多个图片搜索API实现，能够快速找到与关键词相关的图片，满足日常图片搜索需求。</p>
</div>
</div></template>


