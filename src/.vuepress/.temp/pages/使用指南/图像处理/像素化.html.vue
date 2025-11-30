<template><div><h1 id="像素化" tabindex="-1"><a class="header-anchor" href="#像素化"><span>像素化</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 像素化</p>
<p><strong>功能描述</strong>: 将图片转换为像素化艺术效果</p>
<p><strong>插件名称</strong>: patina</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kslOwkAYx+88xRfvaHwBE/SIgdakp8ZDlVFqtG2gqEeNGy4EF2LcQkBQcAl6UDQo8C6mM61v4bRTlkL9Du3MfL/5f9ssLKtr83EpocP0TACoCaKZq5L0x6yzcz7J1NxiQtLiMC0rqXXnyHMcApHnce2W3jKfXtjFjvE89fWOkBILDAtE1BhaSoJo/0fpYial6PIK8ip16UkKStq8pJObDD4oeinbIq7f6/GE9ghOgRhW5WRcJsVdkq8PC4Zd/7AnFBWlmKTpKBFUFTSnDsS0jeNETdJlRfJxCaKW0jSkI5QYTnZw3S1AgGBwgnbW2fA83cHIz0kBSD1NNl/GjMah8VUfcaCIw0RcpAhRBU2qOqyOj+NM1qrVGBXuzTrsorfAAKtSIvljhoWiDhKKukwJWCjju/C7cdov1VEpg/W6Zb+n7Gk3JY5zEI5zmTswmm3KdDvhYgLD7GJt7B7Ie9aqpPFllZxljOaNv1oFrHYOX+fxVtZ8K+Cjc3zdMvf3/JKrgvF5RR8QLm+bx7v+JT4APsvgRg6/blqlHT+Vx396yjrvaf+TK8bmxLDBKT4DuWiZ5UZ/2kLgD/xRM9s="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>像素化 [图片] [-p &#x3C;百分比>]</span></span></code></pre>
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
<td>图片</td>
<td>图片/QQ号/@用户</td>
<td>是</td>
<td>要像素化的图片</td>
<td>[图片]</td>
</tr>
</tbody>
</table>
<h3 id="选项说明" tabindex="-1"><a class="header-anchor" href="#选项说明"><span>选项说明</span></a></h3>
<table>
<thead>
<tr>
<th>选项</th>
<th>简写</th>
<th>参数</th>
<th>说明</th>
<th>默认值</th>
</tr>
</thead>
<tbody>
<tr>
<td>pixelate</td>
<td>-p</td>
<td>number</td>
<td>像素化百分比，值越高像素化效果越强</td>
<td>80</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本像素化" tabindex="-1"><a class="header-anchor" href="#基本像素化"><span>基本像素化</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 [图片]</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="指定像素化百分比" tabindex="-1"><a class="header-anchor" href="#指定像素化百分比"><span>指定像素化百分比</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 [图片] -p 50</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用qq头像像素化" tabindex="-1"><a class="header-anchor" href="#使用qq头像像素化"><span>使用QQ头像像素化</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 123456789</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用-用户头像像素化" tabindex="-1"><a class="header-anchor" href="#使用-用户头像像素化"><span>使用@用户头像像素化</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 @用户</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的输入格式" tabindex="-1"><a class="header-anchor" href="#支持的输入格式"><span>支持的输入格式</span></a></h3>
<ul>
<li><strong>图片文件</strong>: 支持常见图片格式</li>
<li><strong>QQ号</strong>: 使用指定QQ号的头像</li>
<li><strong>@用户</strong>: 使用被@用户的头像</li>
</ul>
<h3 id="像素化算法" tabindex="-1"><a class="header-anchor" href="#像素化算法"><span>像素化算法</span></a></h3>
<ul>
<li><strong>基于Pixelate.js</strong>: 使用先进的像素化算法</li>
<li><strong>实时预览</strong>: 支持实时调整像素化程度</li>
<li><strong>高质量输出</strong>: 保持图像质量的同时实现像素化效果</li>
</ul>
<h3 id="像素化效果" tabindex="-1"><a class="header-anchor" href="#像素化效果"><span>像素化效果</span></a></h3>
<ul>
<li><strong>百分比控制</strong>: 0-100%可调像素化程度</li>
<li><strong>智能处理</strong>: 自动适应不同尺寸的图片</li>
<li><strong>艺术效果</strong>: 产生类似8位像素艺术的视觉效果</li>
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
<td>enablecommand2</td>
<td>boolean</td>
<td>true</td>
<td>是否启用像素化功能</td>
</tr>
<tr>
<td>enablecommand2Name</td>
<td>string</td>
<td>'像素化'</td>
<td>指令名称</td>
</tr>
<tr>
<td>pixelate</td>
<td>number</td>
<td>80</td>
<td>默认像素化百分比（0-100）</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>像素化功能基于Pixelate.js算法实现，能够将普通图片转换为具有艺术感的像素化效果。该算法通过降低图像分辨率并重新采样来创建像素艺术风格，适合制作复古游戏风格的头像或艺术创作。</p>
<p><strong>原项目地址</strong>: <a href="https://lab.miguelmota.com/pixelate/example/" target="_blank" rel="noopener noreferrer">https://lab.miguelmota.com/pixelate/example/</a></p>
</div>
</div></template>


