<template><div><h1 id="渲染typst" tabindex="-1"><a class="header-anchor" href="#渲染typst"><span>渲染Typst</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: typst</p>
<p><strong>功能描述</strong>: 使用本地Typst CLI渲染Typst标记、脚本和数学公式为图片</p>
<p><strong>插件名称</strong>: typbot-render</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6ACbowBlIsloVpXFSpgtG2KcXLTuINNUQUFkYNguBd0bhAA0bfxXSm9S2cdka0UM+inZnzzT/nNrugLs8kJd2ASCwAxOKiVbrGuZcpd+d+0pnpOV3SkhBJKZkV98hzHAKR51HjnNyy7h7pxR/jeeL7PZKVRKBXgFMT8nwaROffTxaxjGKkFmWvUoceJqCkzUgGPs2j3aqXcoxjfq/H87RHcATEsJpKJ1O4uoXLzV7BMPP3ekJRUUpImiHrQVWRp9WuNx0TYqKxqhFXUCchyLoPMTk+IYjCqpY2YCQy1ht297qTShyCwSFSY3fD82QHfZ8HFcDNHM4+DpitPbPd7HMhzmU4hlQhqsjDqgFLg4Mov283GpQK/3Y9zNBzoIB9VcPlAsVCURcJRRlTA/qU+Vb5Wjv8K/WjUgf7ad2ZrP3DTkgCnTghxpgLsEpnOFdwK2G2a1Yl6w9eMrFOyRjm1JGSzorBV4Bfn/FZcZwbRSfv1s62v+Y12B8ldFL+y3hTuAHz9ZgMHKpvWIUt/0LcAirmUauEnrJ2bdNP5e6fytP+eJp0z8RoNynW3esHwEfvVr1Fc7TaRVw+pWQ88A25SkWA"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>typst.markup &#x3C;Typst代码></span></span>
<span class="line"><span>typst.script &#x3C;Typst代码></span></span>
<span class="line"><span>typst.math &#x3C;数学公式></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="命令别名" tabindex="-1"><a class="header-anchor" href="#命令别名"><span>命令别名</span></a></h3>
<table>
<thead>
<tr>
<th>命令</th>
<th>别名</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>typst.markup</td>
<td>typ</td>
<td>渲染Typst标记模式代码</td>
</tr>
<tr>
<td>typst.script</td>
<td>typc</td>
<td>渲染Typst脚本模式代码</td>
</tr>
<tr>
<td>typst.math</td>
<td>teq</td>
<td>渲染数学公式</td>
</tr>
</tbody>
</table>
<h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>Typst代码</td>
<td>文本</td>
<td>是</td>
<td>Typst标记或脚本代码</td>
<td>#text(&quot;Hello World!&quot;)</td>
</tr>
<tr>
<td>数学公式</td>
<td>文本</td>
<td>是</td>
<td>数学公式内容</td>
<td 2a="">x = \frac{-b \pm \sqrt{b^2 - 4ac}}</td>
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
<td>fg</td>
<td>-f</td>
<td>string</td>
<td>设置文字颜色</td>
<td>#000000</td>
</tr>
<tr>
<td>size</td>
<td>-s</td>
<td>number</td>
<td>设置字体大小（pt）</td>
<td>16</td>
</tr>
<tr>
<td>width</td>
<td>-w</td>
<td>string</td>
<td>设置宽度（auto或数字）</td>
<td>auto</td>
</tr>
<tr>
<td>height</td>
<td>--height</td>
<td>string</td>
<td>设置高度（auto或数字）</td>
<td>auto</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="渲染typst标记" tabindex="-1"><a class="header-anchor" href="#渲染typst标记"><span>渲染Typst标记</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">typ #text("Hello World!")</chat-message>
<chat-message nickname="bot" type="bot">
[图片：Hello World! 渲染结果]
</chat-message>
</chat-panel>
<h3 id="渲染数学公式" tabindex="-1"><a class="header-anchor" href="#渲染数学公式"><span>渲染数学公式</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">teq "x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"</chat-message>
<chat-message nickname="bot" type="bot">
[图片：二次方程公式渲染结果]
</chat-message>
</chat-panel>
<h3 id="使用自定义样式" tabindex="-1"><a class="header-anchor" href="#使用自定义样式"><span>使用自定义样式</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">typ #text("彩色文字") -f red -s 24</chat-message>
<chat-message nickname="bot" type="bot">
[图片：红色24pt文字渲染结果]
</chat-message>
</chat-panel>
<h3 id="渲染复杂数学公式" tabindex="-1"><a class="header-anchor" href="#渲染复杂数学公式"><span>渲染复杂数学公式</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">teq "\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}"</chat-message>
<chat-message nickname="bot" type="bot">
[图片：高斯积分公式渲染结果]
</chat-message>
</chat-panel>
<h2 id="渲染模式" tabindex="-1"><a class="header-anchor" href="#渲染模式"><span>渲染模式</span></a></h2>
<h3 id="标记模式-typst-markup" tabindex="-1"><a class="header-anchor" href="#标记模式-typst-markup"><span>标记模式 (typst.markup)</span></a></h3>
<p>用于渲染Typst标记语言，支持完整的Typst语法：</p>
<ul>
<li>文本格式化</li>
<li>段落和标题</li>
<li>列表和表格</li>
<li>图片和链接</li>
</ul>
<h3 id="脚本模式-typst-script" tabindex="-1"><a class="header-anchor" href="#脚本模式-typst-script"><span>脚本模式 (typst.script)</span></a></h3>
<p>用于渲染Typst脚本代码，支持变量和函数：</p>
<ul>
<li>变量定义</li>
<li>函数调用</li>
<li>条件语句</li>
<li>循环结构</li>
</ul>
<h3 id="数学模式-typst-math" tabindex="-1"><a class="header-anchor" href="#数学模式-typst-math"><span>数学模式 (typst.math)</span></a></h3>
<p>专门用于渲染数学公式：</p>
<ul>
<li>代数表达式</li>
<li>微积分符号</li>
<li>矩阵和向量</li>
<li>特殊数学符号</li>
</ul>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="字体支持" tabindex="-1"><a class="header-anchor" href="#字体支持"><span>字体支持</span></a></h3>
<ul>
<li><strong>中文字体</strong>: Source Han Sans SC, Noto Sans CJK SC, Microsoft YaHei, WenQuanYi Micro Hei, SimHei, SimSun</li>
<li><strong>英文字体</strong>: Liberation Sans, Helvetica, Arial, New Computer Modern Sans</li>
<li><strong>数学字体</strong>: 内置数学符号支持</li>
</ul>
<h3 id="颜色支持" tabindex="-1"><a class="header-anchor" href="#颜色支持"><span>颜色支持</span></a></h3>
<ul>
<li><strong>十六进制</strong>: #ffffff, #000000</li>
<li><strong>命名颜色</strong>: red, blue, green, black, white等</li>
<li><strong>RGB格式</strong>: rgb(255, 255, 255)</li>
<li><strong>RGBA格式</strong>: rgba(255, 255, 255, 0.5)</li>
</ul>
<h3 id="渲染配置" tabindex="-1"><a class="header-anchor" href="#渲染配置"><span>渲染配置</span></a></h3>
<ul>
<li><strong>DPI</strong>: 300（高分辨率输出）</li>
<li><strong>超时</strong>: 10秒渲染超时</li>
<li><strong>临时文件</strong>: 自动管理临时文件</li>
</ul>
<h2 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h2>
<h3 id="输入错误" tabindex="-1"><a class="header-anchor" href="#输入错误"><span>输入错误</span></a></h3>
<ul>
<li><strong>缺少参数</strong>: 当未提供Typst代码时提示</li>
<li><strong>语法错误</strong>: 当Typst代码有语法错误时提示</li>
<li><strong>渲染失败</strong>: 当Typst CLI渲染失败时提示</li>
</ul>
<h3 id="系统错误" tabindex="-1"><a class="header-anchor" href="#系统错误"><span>系统错误</span></a></h3>
<ul>
<li><strong>Typst CLI未安装</strong>: 当系统未安装Typst时提示</li>
<li><strong>权限问题</strong>: 当无法创建临时文件时提示</li>
<li><strong>超时错误</strong>: 当渲染超时时提示</li>
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
<td>tempPath</td>
<td>string</td>
<td>temp/typst</td>
<td>临时文件保存路径</td>
</tr>
<tr>
<td>debug</td>
<td>boolean</td>
<td>false</td>
<td>是否开启调试模式</td>
</tr>
<tr>
<td>timeout</td>
<td>number</td>
<td>10000</td>
<td>渲染超时时间（毫秒）</td>
</tr>
<tr>
<td>color</td>
<td>string</td>
<td>#000000</td>
<td>渲染图片的文字颜色</td>
</tr>
<tr>
<td>fontSize</td>
<td>number</td>
<td>16</td>
<td>渲染图片的字体大小（pt）</td>
</tr>
<tr>
<td>width</td>
<td>string/number</td>
<td>auto</td>
<td>渲染图片的宽度</td>
</tr>
<tr>
<td>height</td>
<td>string/number</td>
<td>auto</td>
<td>渲染图片的高度</td>
</tr>
<tr>
<td>dpi</td>
<td>number</td>
<td>300</td>
<td>渲染图片的DPI</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>Typst CLI要求</strong>: 需要在系统中安装Typst CLI才能使用此功能</li>
<li><strong>代码转义</strong>: 数学公式中的反斜杠需要转义（使用双反斜杠）</li>
<li><strong>字体依赖</strong>: 确保系统中安装了支持的中文字体</li>
<li><strong>性能考虑</strong>: 复杂公式可能需要较长时间渲染</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Typst是一种现代化的排版系统，专门为学术论文和技术文档设计。它结合了LaTeX的强大排版能力和Markdown的简洁语法，特别适合渲染数学公式和科学文档。</p>
</div>
</div></template>


