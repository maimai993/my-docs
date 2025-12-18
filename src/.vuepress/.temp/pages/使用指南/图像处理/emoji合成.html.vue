<template><div><h1 id="emoji合成" tabindex="-1"><a class="header-anchor" href="#emoji合成"><span>Emoji合成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-emojimixer" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-emojimixer" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: emix</p>
<p><strong>功能描述</strong>: 混合两个emoji表情，生成合成图片</p>
<p><strong>插件名称</strong>: emojimixer</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl/ABA0nBFITTo2HKlVqpCVQ1KNERNQQEDkYMXwjKAY4oQGD72LYbX0Lt7sFLMU5bHdnfvuf6cweHCun+yEhqsL2jgOIBXit0Mbp9116okssvncYFSIh2Jbk+Bl1Wdwu4DkOdWvkltbpsYtT4zgSm7tEOeiwC/iUoHgUA974rpLNTlxWpbBoVZrRmwQUIvuCip8y6KZqpQzzmXFrxJLaIrgFvEeRYiEJV1O4NLALesy4PeLy80JQiKhi1KnI4p6ykNMwt5cXw8qRFJbOxKi9pMX9rMwAOJ0bpH/0wHHkBCvfdxXAgzRO9NYmw9vJaLBCIR9lfCZSBb8sbioqnKyvo0xW73YZ5ZlP1GOiNWCA3qrjUo5hLj9FXH6TqQNLNfms/Jzn/0pNVRqg9y+MV5PNz0pyeyni9ppME3D9HJebtBXaKIly6eXgM2iFMk7nCGCsxbF2fbWcbIH+VUDFkp20lteGyccjeSiokdRyqeU/+QLoPoOGBdRP6PXLZSqv/3SV9d4ygI4pxibFsMU5vgF+GGuNISuedoWBAccvXsExMQ=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>emix &#x3C;emoji1>&#x3C;emoji2></span></span></code></pre>
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
<td>emoji1</td>
<td>emoji</td>
<td>是</td>
<td>第一个emoji表情</td>
<td>😊</td>
</tr>
<tr>
<td>emoji2</td>
<td>emoji</td>
<td>是</td>
<td>第二个emoji表情</td>
<td>😢</td>
</tr>
</tbody>
</table>
<h3 id="配置选项" tabindex="-1"><a class="header-anchor" href="#配置选项"><span>配置选项</span></a></h3>
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
<td>no_command</td>
<td>boolean</td>
<td>false</td>
<td>启用无指令模式，直接发送两个emoji即可合成</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本合成" tabindex="-1"><a class="header-anchor" href="#基本合成"><span>基本合成</span></a></h3>
<h4 id="合成笑脸和哭脸" tabindex="-1"><a class="header-anchor" href="#合成笑脸和哭脸"><span>合成笑脸和哭脸</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">emix 😊😢</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/emoji合成.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="无指令模式-需配置" tabindex="-1"><a class="header-anchor" href="#无指令模式-需配置"><span>无指令模式（需配置）</span></a></h3>
<p>当启用 <code v-pre>no_command: true</code> 配置时，可以直接发送两个emoji进行合成：</p>
<chat-panel>
<chat-message nickname="用户" type="user">😊😢</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/emoji合成.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="合成原理" tabindex="-1"><a class="header-anchor" href="#合成原理"><span>合成原理</span></a></h3>
<ul>
<li>基于Google的Emoji Kitchen API</li>
<li>自动将emoji转换为Unicode编码</li>
<li>检查emoji组合是否支持合成</li>
<li>生成合成图片并返回</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>参数过多</strong>: 当输入超过2个emoji时提示&quot;太多了&quot;</li>
<li><strong>参数过少</strong>: 当输入少于2个emoji时提示&quot;太少了&quot;</li>
<li><strong>无法合成</strong>: 当emoji组合不支持合成时提示&quot;无法合成emoji1+emoji2&quot;</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要网络连接访问Google Emoji Kitchen服务</li>
<li><strong>兼容性</strong>: 某些emoji可能不支持合成，会返回错误提示</li>
<li><strong>图片大小</strong>: 合成图片为标准emoji尺寸，适合在聊天中使用</li>
</ol>
<h2 id="配置示例" tabindex="-1"><a class="header-anchor" href="#配置示例"><span>配置示例</span></a></h2>
<div class="language-yaml line-numbers-mode" data-highlighter="shiki" data-ext="yaml" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-yaml"><span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">plugins</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  emojimixer</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    no_command</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">false</span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">  # 是否启用无指令模式</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Emoji合成功能基于Google Emoji Kitchen实现，能够将两个不同的emoji表情混合成一个有趣的合成图片，为聊天增添更多趣味性。</p>
</div>
</div></template>


