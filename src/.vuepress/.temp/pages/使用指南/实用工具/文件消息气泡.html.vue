<template><div><h1 id="文件消息气泡组件" tabindex="-1"><a class="header-anchor" href="#文件消息气泡组件"><span>文件消息气泡组件</span></a></h1>
<p>文件消息气泡组件用于在聊天界面中显示文件消息，支持多种文件类型的预览和下载功能。</p>
<h2 id="功能特性" tabindex="-1"><a class="header-anchor" href="#功能特性"><span>功能特性</span></a></h2>
<ul>
<li>✅ 支持图片和视频文件预览</li>
<li>✅ 自定义预览链接（可独立于下载链接）</li>
<li>✅ 文件大小智能格式化显示</li>
<li>✅ 多种文件类型图标支持</li>
<li>✅ 右下角固定下载按钮</li>
<li>✅ 响应式设计，适配移动端</li>
<li>✅ 加载状态和错误处理</li>
<li>✅ 滚动动画效果</li>
</ul>
<h2 id="组件参数" tabindex="-1"><a class="header-anchor" href="#组件参数"><span>组件参数</span></a></h2>
<table>
<thead>
<tr>
<th>参数名</th>
<th>类型</th>
<th>必填</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code v-pre>fileName</code></td>
<td>String</td>
<td>✅</td>
<td>-</td>
<td>文件名称</td>
</tr>
<tr>
<td><code v-pre>fileSize</code></td>
<td>String/Number</td>
<td>❌</td>
<td>0</td>
<td>文件大小（字节）</td>
</tr>
<tr>
<td><code v-pre>downloadUrl</code></td>
<td>String</td>
<td>✅</td>
<td>-</td>
<td>文件下载链接</td>
</tr>
<tr>
<td><code v-pre>previewUrl</code></td>
<td>String</td>
<td>❌</td>
<td>''</td>
<td>文件预览链接（可选，不填则使用下载链接）</td>
</tr>
<tr>
<td><code v-pre>fileType</code></td>
<td>String</td>
<td>❌</td>
<td>'unknown'</td>
<td>文件类型：'image', 'video', 'audio', 'document', 'archive', 'unknown'</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本用法" tabindex="-1"><a class="header-anchor" href="#基本用法"><span>基本用法</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">template</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"用户"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"user"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"示例图片.jpg"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">      :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">2048576</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/file.jpg"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"image"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    /></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">template</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">script</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">import</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75"> FileMessage</span><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD"> from</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '../components/FileMessage.vue'</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">import</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75"> ChatMessage</span><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD"> from</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '../components/ChatMessage.vue'</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">export</span><span style="--shiki-light:#E45649;--shiki-dark:#C678DD"> default</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  components</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    FileMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">,</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    ChatMessage</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">}</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">script</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="带独立预览链接的图片文件" tabindex="-1"><a class="header-anchor" href="#带独立预览链接的图片文件"><span>带独立预览链接的图片文件</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"高清图片.png"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">5123456</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/download/high-quality.png"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  previewUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/preview/low-quality.png"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"image"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">/></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="视频文件预览" tabindex="-1"><a class="header-anchor" href="#视频文件预览"><span>视频文件预览</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"演示视频.mp4"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">15728640</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/video.mp4"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"video"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">/></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="不支持预览的文件类型" tabindex="-1"><a class="header-anchor" href="#不支持预览的文件类型"><span>不支持预览的文件类型</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"项目文档.pdf"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">1048576</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/document.pdf"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"document"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">/></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="压缩包文件" tabindex="-1"><a class="header-anchor" href="#压缩包文件"><span>压缩包文件</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"项目源码.zip"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">5242880</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/source-code.zip"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"archive"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">/></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="文件类型支持" tabindex="-1"><a class="header-anchor" href="#文件类型支持"><span>文件类型支持</span></a></h2>
<h3 id="支持预览的文件类型" tabindex="-1"><a class="header-anchor" href="#支持预览的文件类型"><span>支持预览的文件类型</span></a></h3>
<ul>
<li><strong>image</strong>: 图片文件（JPG、PNG、GIF等）</li>
<li><strong>video</strong>: 视频文件（MP4、WebM等）</li>
</ul>
<h3 id="不支持预览的文件类型-1" tabindex="-1"><a class="header-anchor" href="#不支持预览的文件类型-1"><span>不支持预览的文件类型</span></a></h3>
<ul>
<li><strong>audio</strong>: 音频文件（MP3、WAV等）</li>
<li><strong>document</strong>: 文档文件（PDF、DOC、TXT等）</li>
<li><strong>archive</strong>: 压缩文件（ZIP、RAR等）</li>
<li><strong>unknown</strong>: 未知文件类型</li>
</ul>
<h2 id="样式特点" tabindex="-1"><a class="header-anchor" href="#样式特点"><span>样式特点</span></a></h2>
<h3 id="支持预览的文件布局" tabindex="-1"><a class="header-anchor" href="#支持预览的文件布局"><span>支持预览的文件布局</span></a></h3>
<ul>
<li>预览内容在上方</li>
<li>文件名称和大小在同一行显示在下方</li>
<li>右下角固定下载按钮</li>
</ul>
<h3 id="不支持预览的文件布局" tabindex="-1"><a class="header-anchor" href="#不支持预览的文件布局"><span>不支持预览的文件布局</span></a></h3>
<ul>
<li>文件图标在左侧</li>
<li>文件名称在上方</li>
<li>文件大小在下方</li>
<li>右下角固定下载按钮</li>
</ul>
<h2 id="响应式设计" tabindex="-1"><a class="header-anchor" href="#响应式设计"><span>响应式设计</span></a></h2>
<p>组件会自动适配不同屏幕尺寸：</p>
<ul>
<li>桌面端：最大宽度 320px</li>
<li>移动端：最大宽度 280px</li>
<li>图片/视频预览最大高度自动调整</li>
</ul>
<h2 id="交互效果" tabindex="-1"><a class="header-anchor" href="#交互效果"><span>交互效果</span></a></h2>
<ul>
<li>悬停时卡片有轻微上浮效果</li>
<li>下载按钮悬停时有颜色变化和阴影</li>
<li>滚动进入视口时有淡入动画</li>
<li>加载状态显示加载动画</li>
<li>错误状态显示错误提示</li>
</ul>
<h2 id="自定义样式" tabindex="-1"><a class="header-anchor" href="#自定义样式"><span>自定义样式</span></a></h2>
<p>组件使用 CSS 变量，可以轻松自定义：</p>
<ul>
<li><code v-pre>--vp-c-bg</code>: 背景色</li>
<li><code v-pre>--vp-c-border</code>: 边框色</li>
<li><code v-pre>--vp-c-brand</code>: 品牌色（下载按钮）</li>
<li><code v-pre>--vp-c-text-1</code>: 主要文字色</li>
<li><code v-pre>--vp-c-text-2</code>: 次要文字色</li>
</ul>
<h2 id="浏览器兼容性" tabindex="-1"><a class="header-anchor" href="#浏览器兼容性"><span>浏览器兼容性</span></a></h2>
<ul>
<li>现代浏览器（Chrome、Firefox、Safari、Edge）</li>
<li>支持 Intersection Observer API</li>
<li>支持 CSS Grid 和 Flexbox</li>
<li>支持 CSS 自定义属性（CSS Variables）</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li>预览链接和下载链接可以是相同的，也可以是不同的</li>
<li>文件大小会自动格式化为合适的单位（B、KB、MB、GB）</li>
<li>组件会自动处理加载状态和错误状态</li>
<li>下载按钮始终显示在右下角，便于用户操作</li>
<li>组件设计符合现代聊天应用的用户体验标准</li>
</ol>
</div></template>


