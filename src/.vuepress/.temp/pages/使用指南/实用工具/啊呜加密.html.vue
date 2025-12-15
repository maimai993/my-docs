<template><div><h1 id="啊呜加密" tabindex="-1"><a class="header-anchor" href="#啊呜加密"><span>啊呜加密</span></a></h1>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-furry-encode-decode" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-furry-encode-decode" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/furry-encode-decode" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a></p>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: <code v-pre>furry-encode</code> <code v-pre>furry-decode</code></p>
<p><strong>功能描述</strong>: 兽音加密/解密文本，基于兽音译者的JS实现</p>
<p><strong>插件名称</strong>: furry-encode-decode</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kslOwkAYx+88xRfv1fgCJmjggoFU4NR4qFAFoy0pxeWmcYnREDcObkERVFwCJiZoQOVdTGda38LpzLCU4neY7fvNf75l5pe01URK1g2YnvEBsbhkFap4732W7uiQzc0t6HImBdNpNbdGj1zHfpBEEdVuyS3ruc4udkwUia93pKhJn1cgrCWVxSxIzjxKFjM51UgvK26lLj1JQDmTkA18lUf7JTflWJj73R7X0y7BKZBCWjqbSuPSLi42vIIh7vd6/BFJTsoZQ9EFTVXmtIE3HQsGpPmcrq8Lipog+QlJxZm8XDQmoZ2v3+s3q92y68fovOqNf3DdzSkOgjBBik03okh2MPJzfAO4sYc362Nm88BsNUYoFKZMmCMliKjKpGbAyvg4yh/atRqjQr32hzh6CwywH8q4eMQwf4Qi/ghnysCeMj9vfjdO+qU6KhWwX7ecL3Z40g0pGKBIMMCZOzC/2oQZqAeDozEKR2Mcvge7XUCXRVTZto52rdYpLl4Nl33gpNU6Z/0cFl8VzI8L8q2Y3PAsHwGd5lGzgF437fLOMJWnf8rKiu/qwDMXY61i2GAjXwCffVuVZn92cd8fH71DLw=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>furry-encode &#x3C;text></span></span>
<span class="line"><span>furry-decode &#x3C;text></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="别名" tabindex="-1"><a class="header-anchor" href="#别名"><span>别名</span></a></h3>
<ul>
<li><strong>加密</strong>: <code v-pre>兽音译者</code> <code v-pre>兽音加密</code></li>
<li><strong>解密</strong>: <code v-pre>兽音解密</code></li>
</ul>
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
<td>text</td>
<td>文本</td>
<td>是</td>
<td>要加密或解密的文本内容</td>
<td>你好世界</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="文本加密" tabindex="-1"><a class="header-anchor" href="#文本加密"><span>文本加密</span></a></h3>
<h4 id="加密普通文本" tabindex="-1"><a class="header-anchor" href="#加密普通文本"><span>加密普通文本</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">furry-encode 你好世界</chat-message>
<chat-message nickname="bot" type="bot">加密成功！
<p>呜嗷呜嗷嗷嗷啊嗷嗷~啊呜~啊~呜呜嗷~嗷呜~啊~嗷呜嗷~嗷啊嗷啊啊~啊</p>
</chat-message>
</chat-panel>
<h3 id="文本解密" tabindex="-1"><a class="header-anchor" href="#文本解密"><span>文本解密</span></a></h3>
<h4 id="解密兽音文本" tabindex="-1"><a class="header-anchor" href="#解密兽音文本"><span>解密兽音文本</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">furry-decode 呜嗷呜嗷嗷嗷啊嗷嗷~啊呜~啊~呜呜嗷~嗷呜~啊~嗷呜嗷~嗷啊嗷啊啊~啊</chat-message>
<chat-message nickname="bot" type="bot">
解密成功！
<p>你好世界</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="加密算法" tabindex="-1"><a class="header-anchor" href="#加密算法"><span>加密算法</span></a></h3>
<ul>
<li><strong>兽音编码</strong>: 基于兽音译者的JS实现</li>
<li><strong>字符映射</strong>: 将普通文本转换为兽音字符序列</li>
<li><strong>可逆加密</strong>: 支持双向转换，可加密也可解密</li>
</ul>
<h3 id="处理逻辑" tabindex="-1"><a class="header-anchor" href="#处理逻辑"><span>处理逻辑</span></a></h3>
<ul>
<li><strong>文本验证</strong>: 检查输入文本是否为空</li>
<li><strong>编码转换</strong>: 使用兽音翻译器进行编码/解码</li>
<li><strong>结果返回</strong>: 返回处理后的文本结果</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>空输入</strong>: 当用户未输入任何内容时提示</li>
<li><strong>处理失败</strong>: 当加密/解密过程中出现错误时提示</li>
<li><strong>网络错误</strong>: 当处理过程中出现异常时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>不可套娃</strong>: 不支持对已加密的文本再次加密</li>
<li><strong>文本长度</strong>: 长文本加密后会产生大量兽音字符</li>
<li><strong>字符限制</strong>: 仅支持可打印字符的加密</li>
<li><strong>兼容性</strong>: 加密结果可能在某些平台显示异常</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>插件为无配置插件，使用默认设置。</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>兽音加密功能基于兽音译者的JS实现，能够将普通文本转换为有趣的兽音加密文本，适合用于娱乐和简单的信息隐藏。</p>
</div>
</div></template>


