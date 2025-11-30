<template><div><h1 id="磁力链接截图" tabindex="-1"><a class="header-anchor" href="#磁力链接截图"><span>磁力链接截图</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: magnet</p>
<p><strong>功能描述</strong>: 获取磁力链接的预览截图，显示种子文件的基本信息</p>
<p><strong>插件名称</strong>: magnet-preview</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstu2kAUhvc8xVH2pMoLVCJdEsCOxMrqwoEpuE1sC+y2y6JcSlNR0oDUCxXllkBuThTlSiLyLhEzNm+R8YxJYnDOwp6Z881/5lzeLWufUlk5Z8DCYgioJSW72iPFy7dsxz55cymTk/UsLCiq+Zkd+Y4jIIkitlr0ln1wzC+OTRSp7+kIqenQtEBcS6P3eZDc/yxdLJqqoawgv9IjPU9BWU/JBvlXwptNP+Va3PP7Pb7QPsE3IEU1JZ9VSHOD1C+mBaOef9oTSUhyWtYNlAtrKlrSJmK6FhOkmJxRkUGr90FYNjOKOg0JgqSbuo4MhHKkvD28mXiF+/jJ9WNCSQiHX9NKs40o0h3M3P9sALkoksLxq2H/O9WbYVCcMXEPaUJCRfOaAR/n5nCp7FgWp6JPvY96aAs44HTbpL7FsUiCIZGEx7SBhxreNkZftp9LjVU64JysuvPFUuRETGBITPCYHeAx7HYBb9ZGlQH5sRNM7oJj3Y1+WSusvLO6kspzUOCgMAa7QM7LTreI//TI1Sn5XwnGekCK+7g2wNY1JfH6qn3WCI68B85dFdfqo9aaK1sb2N++BuW7D8Orv3RGcWfN3toIrtoB4EoJ96v4pOC014NUDl9oE2+mr6NHnhhvPccmB8MC8ntgd/rPC8wT4Xwy9AAWtmf4"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>magnet &#x3C;磁力链接></span></span></code></pre>
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
<td>磁力链接</td>
<td>文本</td>
<td>是</td>
<td>标准的磁力链接</td>
<td>magnet:?xt=urn:btih:xxxxxxxxxxxx</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="获取磁力链接预览" tabindex="-1"><a class="header-anchor" href="#获取磁力链接预览"><span>获取磁力链接预览</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">magnet magnet:?xt=urn:btih:xxxxxxxxxxxx</chat-message>
<chat-message nickname="bot" type="bot">
正在获取截图...
</chat-message>
<chat-message nickname="bot" type="bot">
[图片：磁力链接预览截图]
</chat-message>
</chat-panel>
<h4 id="交互式输入" tabindex="-1"><a class="header-anchor" href="#交互式输入"><span>交互式输入</span></a></h4>
<p>如果直接输入 <code v-pre>magnet</code> 指令而不带参数，机器人会提示输入磁力链接：</p>
<chat-panel>
<chat-message nickname="用户" type="user">magnet</chat-message>
<chat-message nickname="bot" type="bot">请输入磁力链接！</chat-message>
<chat-message nickname="用户" type="user">magnet:?xt=urn:btih:xxxxxxxxxxxx</chat-message>
<chat-message nickname="bot" type="bot">
正在获取截图...
</chat-message>
<chat-message nickname="bot" type="bot">
[图片：磁力链接预览截图]
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="磁力链接解析" tabindex="-1"><a class="header-anchor" href="#磁力链接解析"><span>磁力链接解析</span></a></h3>
<ul>
<li><strong>哈希提取</strong>: 自动从磁力链接中提取BTIH哈希值</li>
<li><strong>格式验证</strong>: 使用正则表达式验证磁力链接格式</li>
<li><strong>错误处理</strong>: 对无效格式的链接提供友好的错误提示</li>
</ul>
<h3 id="网页截图机制" tabindex="-1"><a class="header-anchor" href="#网页截图机制"><span>网页截图机制</span></a></h3>
<ul>
<li><strong>目标网站</strong>: 使用 <code v-pre>https://beta.magnet.pics/m/{hash}</code> 获取预览信息</li>
<li><strong>自定义UA</strong>: 设置Chrome浏览器用户代理避免被拦截</li>
<li><strong>元素定位</strong>: 精确截图 <code v-pre>.thumb-container</code> 容器元素</li>
<li><strong>透明背景</strong>: 使用 <code v-pre>omitBackground: true</code> 生成透明背景图片</li>
</ul>
<h3 id="用户体验优化" tabindex="-1"><a class="header-anchor" href="#用户体验优化"><span>用户体验优化</span></a></h3>
<ul>
<li><strong>进度提示</strong>: 显示&quot;正在获取截图...&quot;状态信息</li>
<li><strong>自动清理</strong>: 截图完成后自动删除进度提示消息</li>
<li><strong>错误反馈</strong>: 对无法获取信息的情况提供明确提示</li>
</ul>
<h2 id="支持的磁力链接格式" tabindex="-1"><a class="header-anchor" href="#支持的磁力链接格式"><span>支持的磁力链接格式</span></a></h2>
<p>插件支持标准的磁力链接格式：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>magnet:?xt=urn:btih:[哈希值]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><p>其中 <code v-pre>[哈希值]</code> 可以是：</p>
<ul>
<li>40字符的SHA1哈希（十六进制）</li>
<li>32字符的Base32编码哈希</li>
</ul>
<h2 id="故障排除" tabindex="-1"><a class="header-anchor" href="#故障排除"><span>故障排除</span></a></h2>
<h3 id="常见问题" tabindex="-1"><a class="header-anchor" href="#常见问题"><span>常见问题</span></a></h3>
<ol>
<li>
<p><strong>&quot;无效的磁力链接格式！&quot;</strong></p>
<ul>
<li>检查链接是否以 <code v-pre>magnet:?xt=urn:btih:</code> 开头</li>
<li>确认链接格式正确，没有多余的空格或字符</li>
</ul>
</li>
<li>
<p><strong>&quot;无法获取链接信息或未找到截图！&quot;</strong></p>
<ul>
<li>目标网站可能暂时不可用</li>
<li>该磁力链接在magnet.pics网站中没有对应的预览信息</li>
<li>网络连接问题导致无法访问目标网站</li>
</ul>
</li>
<li>
<p><strong>截图显示空白</strong></p>
<ul>
<li>目标网站的预览容器元素可能已更新</li>
<li>网站可能有反爬虫机制</li>
</ul>
</li>
</ol>
<h3 id="性能优化" tabindex="-1"><a class="header-anchor" href="#性能优化"><span>性能优化</span></a></h3>
<ul>
<li><strong>页面管理</strong>: 及时关闭浏览器页面避免内存泄漏</li>
<li><strong>网络优化</strong>: 设置合适的等待时间确保页面完全加载</li>
<li><strong>资源清理</strong>: 正确处理图片缓冲区避免内存占用</li>
</ul>
<h2 id="技术实现细节" tabindex="-1"><a class="header-anchor" href="#技术实现细节"><span>技术实现细节</span></a></h2>
<h3 id="核心算法" tabindex="-1"><a class="header-anchor" href="#核心算法"><span>核心算法</span></a></h3>
<div class="language-javascript line-numbers-mode" data-highlighter="shiki" data-ext="javascript" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-javascript"><span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 从磁力链接提取哈希值</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">const</span><span style="--shiki-light:#986801;--shiki-dark:#E5C07B"> hash</span><span style="--shiki-light:#0184BC;--shiki-dark:#56B6C2"> =</span><span style="--shiki-light:#383A42;--shiki-dark:#E5C07B"> magnetLink</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">.</span><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF">split</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">(</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">':'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">)[</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">3</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">].</span><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF">split</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">(</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'&#x26;'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">)[</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">0</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">];</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 构建预览URL</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">const</span><span style="--shiki-light:#986801;--shiki-dark:#E5C07B"> url</span><span style="--shiki-light:#0184BC;--shiki-dark:#56B6C2"> =</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> `https://beta.magnet.pics/m/</span><span style="--shiki-light:#CA1243;--shiki-dark:#C678DD">${</span><span style="--shiki-light:#383A42;--shiki-dark:#E06C75">hash</span><span style="--shiki-light:#CA1243;--shiki-dark:#C678DD">}</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">`</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">;</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 截图特定容器元素</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">const</span><span style="--shiki-light:#986801;--shiki-dark:#E5C07B"> thumbContainer</span><span style="--shiki-light:#0184BC;--shiki-dark:#56B6C2"> =</span><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD"> await</span><span style="--shiki-light:#383A42;--shiki-dark:#E5C07B"> page</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">.</span><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF">$</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">(</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'.thumb-container'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">);</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">const</span><span style="--shiki-light:#986801;--shiki-dark:#E5C07B"> imageBuffer</span><span style="--shiki-light:#0184BC;--shiki-dark:#56B6C2"> =</span><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD"> await</span><span style="--shiki-light:#383A42;--shiki-dark:#E5C07B"> thumbContainer</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">.</span><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF">screenshot</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">({ </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">omitBackground</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> true</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> });</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="依赖要求" tabindex="-1"><a class="header-anchor" href="#依赖要求"><span>依赖要求</span></a></h3>
<ul>
<li><strong>Koishi框架</strong>: ^4.12.2</li>
<li><strong>Puppeteer插件</strong>: ^3.8.3</li>
<li><strong>Node.js</strong>: 支持现代JavaScript特性</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>磁力链接预览功能基于magnet.pics网站提供的信息，能够显示种子的基本信息、文件列表、文件大小等关键信息，帮助用户快速了解种子内容。</p>
</div>
</div></template>


