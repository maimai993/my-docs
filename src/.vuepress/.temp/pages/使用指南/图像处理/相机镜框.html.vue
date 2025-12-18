<template><div><h1 id="相机镜框" tabindex="-1"><a class="header-anchor" href="#相机镜框"><span>相机镜框</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-patina" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-patina" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/patina" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 相机镜框</p>
<p><strong>功能描述</strong>: 为图片添加相机取景器镜框效果</p>
<p><strong>插件名称</strong>: patina</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6ACbrEQGvSVeOiyig12jZQ1KXGG2oIXlh4C5GLgmKAjWhQ4F1MZ1rfwmmnXAr1LNqZOd/85zZrm+rOalxK6LC4FABqgmjmqiT9sezsnE8ytbKekLQ4LMpKatc58hyHQOR5XC/SW2atwS72jeepb3iElFhgUiCixtBGEkT7P00XSylFl7eQV2lAz1NQ0lYlnTxk8FnBS9kWcf1ejye0R3ABxLAqJ+MyKRyTfGtSMOz6Jz2hqCjFJE1HiaCqoBV1LKZtHCdqki4rko9LELWUpiEdocRksuPrQQECBINztLPOhufpDqZ+Lh+BtNJkvzFjtM+Nr9aUA0UcJuIiBYgqaF7VYXt2FmeyVr3OqPBw1mEXLQIDrEqJ5C8YFoo6SCjqMiVgoYzvx9+9q1GpvkoZrOaB/Z6yV4OUOM5BOM5lnsDo9Cgz6ISLCQyzi7WxZyDvWauSxrdVcp0xOg/+ahWwejl8n8flQ/PiGN93zdMTv8yqYHze0dfDOP/6XgBfZ3A7h5v7VunIT+X1n4aytnt6X3PF2JAYNj7CNyA3XbPcHk1bCPwBkoIxrA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>相机镜框 [图片]</span></span></code></pre>
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
<td>要添加相机镜框的图片</td>
<td>[图片]</td>
</tr>
</tbody>
</table>
<h3 id="选项说明" tabindex="-1"><a class="header-anchor" href="#选项说明"><span>选项说明</span></a></h3>
<p>此功能目前没有可配置的指令参数，但可以通过插件配置调整图片对齐方式和压缩质量。</p>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="为图片添加相机镜框" tabindex="-1"><a class="header-anchor" href="#为图片添加相机镜框"><span>为图片添加相机镜框</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">相机镜框 [图片]</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用qq头像添加相机镜框" tabindex="-1"><a class="header-anchor" href="#使用qq头像添加相机镜框"><span>使用QQ头像添加相机镜框</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">相机镜框 123456789</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用-用户头像添加相机镜框" tabindex="-1"><a class="header-anchor" href="#使用-用户头像添加相机镜框"><span>使用@用户头像添加相机镜框</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">相机镜框 @用户</chat-message>
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
<h3 id="图片处理逻辑" tabindex="-1"><a class="header-anchor" href="#图片处理逻辑"><span>图片处理逻辑</span></a></h3>
<ul>
<li><strong>居中填充</strong>: 图片居中显示，保持比例，超出部分裁剪</li>
<li><strong>拉伸</strong>: 图片拉伸填满整个镜框区域</li>
<li><strong>适应</strong>: 图片适应镜框区域，保持比例，可能有留白</li>
</ul>
<h3 id="输出规格" tabindex="-1"><a class="header-anchor" href="#输出规格"><span>输出规格</span></a></h3>
<ul>
<li><strong>分辨率</strong>: 1080x2400像素</li>
<li><strong>格式</strong>: JPEG</li>
<li><strong>质量</strong>: 可配置压缩质量（0-100%）</li>
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
<td>enablecommand3</td>
<td>boolean</td>
<td>true</td>
<td>是否启用相机镜框功能</td>
</tr>
<tr>
<td>enablecommand3Name</td>
<td>string</td>
<td>'相机镜框'</td>
<td>指令名称</td>
</tr>
<tr>
<td>cameraAlignmentLogic</td>
<td>string</td>
<td>'居中填充'</td>
<td>输入图片的对齐逻辑（居中填充/拉伸/适应）</td>
</tr>
<tr>
<td>camerascreenshotquality</td>
<td>number</td>
<td>50</td>
<td>设置图片压缩质量（0-100%）</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>相机镜框功能基于puppeteer实现，能够准确处理各种尺寸的图片，并自动适配相机取景器镜框效果。镜框效果模拟真实的相机取景器界面，为用户图片增添专业感。</p>
</div>
</div></template>


