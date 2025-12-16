<template><div><h1 id="网页截图" tabindex="-1"><a class="header-anchor" href="#网页截图"><span>网页截图</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-screenshot" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-screenshot" alt="" loading="lazy"></a>  <a href="https://github.com/koishijs/koishi-plugin-puppeteer" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: shot</p>
<p><strong>功能描述</strong>: 截取网页内容并返回图片</p>
<p><strong>插件名称</strong>: screenshot</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kktPwkAQx+98iol3NH4BE/SIgdaGU+OhwioYbZu2qEeNjxANwQcHXyEiKPgIchENCnwX013qt3DZLY9CnUO7O/Pb/8zO7OqGth1PKoYFi0sBoBaTu/kqyXwssx37mOmVNUPRk7CYUtM7zOVxh0AWRVy7p6e6L2/8YN9EkcaGLqQmApMCES2B1k2Qe/9pulhKq1ZqE3mVBvQ8BRU9rljkNouPi16qZxE37o14UnsEF0AOaykzmSLFI1JoTAqG3fhkJBSVlYSiW8gIaipa0cZy9kySZDNuIKSaSb+wIMh6WteRhZAxWfD4enCJGASDc7S7bCOKdAdTP2d3QBoZsvc2YzdP7K/GFIMijIm4SBGiKprXLNiancXZnFOrcSo8nHfYRe+BA06lRAqnHAtFGRKKukwJeCr7++5393xUqq9SBqe+33tTufNBSZLEEElymQewWx3KDDrBMUFgmCC42COQ95xTyeCrKrnI2q1bf7UKOJ08vimQzDO+afvVVAX785q+HVw+6J4e+d/sCfBFFjfzuL7nlA79VJ7/aSVvuKfrL64YHw/Hxof3CuSy3S03R8uOBf4AtIEvtA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>shot &#x3C;url> [selector]</span></span>
<span class="line"><span>screenshot &#x3C;url> [selector]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>url</td>
<td>文本</td>
<td>是</td>
<td>要截图的网页地址</td>
<td><a href="https://www.baidu.com" target="_blank" rel="noopener noreferrer">https://www.baidu.com</a></td>
</tr>
<tr>
<td>selector</td>
<td>文本</td>
<td>否</td>
<td>CSS选择器，指定要截图的特定元素</td>
<td>.main-content</td>
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
<td>full</td>
<td>-f</td>
<td>无</td>
<td>对整个可滚动区域截图</td>
</tr>
<tr>
<td>viewport</td>
<td>-v</td>
<td>string</td>
<td>指定视口大小，格式：宽度x高度</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本截图" tabindex="-1"><a class="header-anchor" href="#基本截图"><span>基本截图</span></a></h3>
<h4 id="截图-百度-首页" tabindex="-1"><a class="header-anchor" href="#截图-百度-首页"><span>截图 <a href="https://www.baidu.com" target="_blank" rel="noopener noreferrer"><code v-pre>百度</code></a> 首页</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">shot https://www.baidu.com</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/网页截图.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用选项" tabindex="-1"><a class="header-anchor" href="#使用选项"><span>使用选项</span></a></h3>
<h4 id="全页面截图" tabindex="-1"><a class="header-anchor" href="#全页面截图"><span>全页面截图</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">shot https://www.bilibili.com -f</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/网页截图3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="指定视口大小" tabindex="-1"><a class="header-anchor" href="#指定视口大小"><span>指定视口大小</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">shot https://www.taobao.com -v 1280x720</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/网页截图4.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的协议" tabindex="-1"><a class="header-anchor" href="#支持的协议"><span>支持的协议</span></a></h3>
<ul>
<li>HTTP</li>
<li>HTTPS</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>协议补全</strong>: 如果URL没有协议前缀，自动添加<code v-pre>http://</code></li>
<li><strong>超时处理</strong>:
<ul>
<li>加载超时: 5秒</li>
<li>空闲超时: 30秒</li>
</ul>
</li>
<li><strong>图片优化</strong>: 自动压缩超过1MB的图片</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>无法打开页面</strong>: 当页面无法加载时提示</li>
<li><strong>元素未找到</strong>: 当指定选择器对应的元素不存在时提示</li>
<li><strong>截图失败</strong>: 当截图过程中出现错误时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问目标网站</li>
<li><strong>网站限制</strong>: 某些网站可能有反爬虫机制，可能无法正常截图</li>
<li><strong>加载时间</strong>: 复杂页面可能需要较长时间加载</li>
<li><strong>图片大小</strong>: 大尺寸截图会自动压缩以符合消息大小限制</li>
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
<td>protocols</td>
<td>string[]</td>
<td>['http', 'https']</td>
<td>允许的协议列表</td>
</tr>
<tr>
<td>maxSize</td>
<td>number</td>
<td>1MB</td>
<td>单张图片最大尺寸</td>
</tr>
<tr>
<td>loadTimeout</td>
<td>number</td>
<td>5秒</td>
<td>页面加载超时时间</td>
</tr>
<tr>
<td>idleTimeout</td>
<td>number</td>
<td>30秒</td>
<td>页面空闲超时时间</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>网页截图功能基于puppeteer-core实现，能够准确渲染现代网页内容，包括JavaScript动态生成的内容。</p>
</div>
</div></template>


