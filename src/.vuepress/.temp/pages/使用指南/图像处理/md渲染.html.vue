<template><div><h1 id="markdown渲染" tabindex="-1"><a class="header-anchor" href="#markdown渲染"><span>Markdown渲染</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://github.com/KarinJS/Karin" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-Karin-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/@karinjs/plugin-markdown" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/@karinjs/plugin-markdown" alt="" loading="lazy"></a>  <a href="https://github.com/KarinJS/plugin-markdown" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: md, markdown</p>
<p><strong>功能描述</strong>: 将Markdown文本渲染为图片并发送</p>
<p><strong>插件名称</strong>: @karinjs/plugin-markdown</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks9T2kAUx+/8FW+8U8d/oFMsB2YgkDjllOkhmrSgkmRCqD3q2FraDgMVDrVaEMFCawtOZ0od/PW/ONlN/C9Mdhc0JL5Dsrvvs9/39r33al3bWMlJhgmppQi4lhXtRh+X/78kO/IplpZfG5Keg1ReLb0lR77jGIiCgAZH7i37ZEgvTkwQXN/9kaLKkaBAWpOV1SKI3v+Ju1gqqWa+oPiVpvSiC0r6imTigwr61PZTnqWZ3+/xhfYJPgcxKRl5Fbd3cHMU1EtSd9ARy4iSLOmmYkQ1VVnWZiJ6xsXFgmSsydpGyH0uIT5b86RXi/MFOZozC+tBiOdFvaTriqkoRvBFs+vpK7MQjT51y082guDuYO7myyHgURlvDeet8WfrfDRHoDRh0gxpQ0ZVFjUT3iwsoErVGQwolbwfiCRDj4ACTq+DmzWKxTIEiWUY0wEayro4vN3cfSg1UemCc7rtDV11d5oSFycIF2fMMeDv27d7NdzZxK3jcOYH0Dw4Vm9GJSiVYFQP7EYLl2uJF1wqXKcP1uW1m8+06vjsL27VKczzBOZ5Bv8E/K/q9Mpor4/rFevyIFzzFzjXDbTfRPtX9scPYVU4AevsmzvOqPvOru2E1/I3oHoFjRvodMvpvA9T+fNI82iLfX0eMDE6EBSbHZch4K9Xdnc8KenD9LORO/KnZHI="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>#md &#x3C;markdown文本></span></span>
<span class="line"><span>#markdown &#x3C;markdown文本></span></span>
<span class="line"><span>md &#x3C;markdown文本></span></span>
<span class="line"><span>markdown &#x3C;markdown文本></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>markdown文本</td>
<td>文本</td>
<td>是</td>
<td>要渲染的Markdown内容或文件路径/URL</td>
<td><code v-pre># 标题\n这是一段**粗体**文字</code></td>
</tr>
<tr>
<td>文件路径</td>
<td>文本</td>
<td>否</td>
<td>本地Markdown文件路径</td>
<td><code v-pre>./README.md</code></td>
</tr>
<tr>
<td>URL</td>
<td>文本</td>
<td>否</td>
<td>网络Markdown文件URL</td>
<td><code v-pre>https://raw.githubusercontent.com/markedjs/marked/master/README.md</code></td>
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
</tr>
</thead>
<tbody>
<tr>
<td>前缀</td>
<td>-</td>
<td>无</td>
<td>使用<code v-pre>#md</code>或<code v-pre>#markdown</code>作为命令前缀</td>
</tr>
<tr>
<td>无前缀</td>
<td>-</td>
<td>无</td>
<td>使用<code v-pre>md</code>或<code v-pre>markdown</code>作为命令（需配置）</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本渲染" tabindex="-1"><a class="header-anchor" href="#基本渲染"><span>基本渲染</span></a></h3>
<h4 id="渲染简单markdown文本" tabindex="-1"><a class="header-anchor" href="#渲染简单markdown文本"><span>渲染简单Markdown文本</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">#md # 标题
这是一段**粗体**文字，这是*斜体*文字。
<ul>
<li>列表项1</li>
<li>列表项2</li>
</ul>
<blockquote>
<p>这是一段引用</chat-message></p>
</blockquote>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="数学公式渲染" tabindex="-1"><a class="header-anchor" href="#数学公式渲染"><span>数学公式渲染</span></a></h3>
<h4 id="渲染katex数学公式" tabindex="-1"><a class="header-anchor" href="#渲染katex数学公式"><span>渲染KaTeX数学公式</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">#md # 数学公式示例
<p>行内公式：$E = mc^2$</p>
<p>块级公式：<br>
$$<br>
\int_{-\infty}^{\infty} e<sup>{-x</sup>2} dx = \sqrt{\pi}<br>
$$</chat-message></p>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="文件渲染" tabindex="-1"><a class="header-anchor" href="#文件渲染"><span>文件渲染</span></a></h3>
<h4 id="渲染网络markdown文件" tabindex="-1"><a class="header-anchor" href="#渲染网络markdown文件"><span>渲染网络Markdown文件</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">#md https://raw.githubusercontent.com/markedjs/marked/master/README.md</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="渲染本地markdown文件" tabindex="-1"><a class="header-anchor" href="#渲染本地markdown文件"><span>渲染本地Markdown文件</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">#md ./README.md</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的markdown语法" tabindex="-1"><a class="header-anchor" href="#支持的markdown语法"><span>支持的Markdown语法</span></a></h3>
<ul>
<li><strong>标题</strong>: 1-6级标题</li>
<li><strong>文本样式</strong>: 粗体、斜体、删除线、下划线</li>
<li><strong>列表</strong>: 有序列表、无序列表</li>
<li><strong>引用</strong>: 块级引用</li>
<li><strong>代码</strong>: 行内代码、代码块（支持语法高亮）</li>
<li><strong>表格</strong>: Markdown表格</li>
<li><strong>链接</strong>: 内联链接、引用链接</li>
<li><strong>图片</strong>: 图片嵌入</li>
<li><strong>分割线</strong>: 水平分割线</li>
<li><strong>数学公式</strong>: KaTeX数学公式支持</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>文件检测</strong>: 自动识别URL和本地文件路径</li>
<li><strong>权限验证</strong>: 根据配置检查用户权限</li>
<li><strong>HTML转换</strong>: 使用@karinjs/md-html库将Markdown转换为HTML</li>
<li><strong>图片渲染</strong>: 使用puppeteer将HTML渲染为图片</li>
<li><strong>缓存优化</strong>: 相同内容缓存处理</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>权限不足</strong>: 当用户没有相应权限时提示</li>
<li><strong>文件不存在</strong>: 当本地文件不存在时提示</li>
<li><strong>网络错误</strong>: 当网络文件无法访问时提示</li>
<li><strong>渲染失败</strong>: 当Markdown渲染过程中出现错误时提示</li>
<li><strong>语法错误</strong>: 当Markdown语法错误时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>权限要求</strong>: 根据配置可能需要特定权限才能使用</li>
<li><strong>文件大小</strong>: 大文件可能需要较长时间渲染</li>
<li><strong>网络依赖</strong>: 渲染网络文件需要稳定的网络连接</li>
<li><strong>数学公式</strong>: 需要正确安装KaTeX依赖</li>
<li><strong>本地文件</strong>: 需要正确配置文件路径权限</li>
<li><strong>性能考虑</strong>: 复杂Markdown文档可能需要更多渲染时间</li>
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
<td>prefix</td>
<td>boolean</td>
<td>true</td>
<td>是否使用<code v-pre>#</code>前缀</td>
</tr>
<tr>
<td>render.local</td>
<td>boolean</td>
<td>true</td>
<td>是否允许渲染本地文件</td>
</tr>
<tr>
<td>render.network</td>
<td>boolean</td>
<td>true</td>
<td>是否允许渲染网络文件</td>
</tr>
<tr>
<td>render.localPermission</td>
<td>boolean</td>
<td>true</td>
<td>本地文件渲染是否需要权限检查</td>
</tr>
<tr>
<td>render.networkPermission</td>
<td>boolean</td>
<td>true</td>
<td>网络文件渲染是否需要权限检查</td>
</tr>
<tr>
<td>permission</td>
<td>Permission</td>
<td>'all'</td>
<td>权限控制模式：'all'、'master'、'admin'、'group.owner'、'whitelist'、'blacklist'</td>
</tr>
<tr>
<td>deviceScaleFactor</td>
<td>number</td>
<td>2</td>
<td>设备像素比，影响图片清晰度</td>
</tr>
<tr>
<td>waitUntil</td>
<td>string</td>
<td>'networkidle0'</td>
<td>页面加载等待条件：'load'、'domcontentloaded'、'networkidle0'、'networkidle2'</td>
</tr>
<tr>
<td>markedKatex.output</td>
<td>string</td>
<td>'htmlAndMathml'</td>
<td>KaTeX输出格式：'html'、'mathml'、'htmlAndMathml'</td>
</tr>
<tr>
<td>markedKatex.throwOnError</td>
<td>boolean</td>
<td>false</td>
<td>KaTeX错误时是否抛出异常</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Markdown渲染功能基于@karinjs/md-html和puppeteer实现，能够准确渲染现代Markdown内容，包括KaTeX数学公式和代码语法高亮。</p>
<p>插件支持热重载配置，修改配置后无需重启即可生效。</p>
</div>
</div></template>


