<template><div><h1 id="原图坦克" tabindex="-1"><a class="header-anchor" href="#原图坦克"><span>原图坦克</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-patina" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-patina" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/patina" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 原图坦克</p>
<p><strong>功能描述</strong>: 将两张图片合成为两帧GIF图片，实现图片切换效果</p>
<p><strong>插件名称</strong>: patina</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOIkEUhvc8xYl7ZuILTIIkvcEAbYBNZxYlNNKTsbsDjTPLMY7EaAheWBg1RC6KV3SFBm/vYrqq27ewqCqRovEsuqvqfPWfOpf8b+tPtoCKDswvhIBaWvPqZ2Tj7ifbsU+pvLhURHYB5g2z/JcdSccR0FQV91r0lnd5wy9+mKpS3+eRbuZCQYG4ldN/lUAb/r/RxULZdIxlXVYa0XMURHYWOeSoijebMjW0uPDLHim0JBgFLWYZpYJBmhXS6AcFY8If9EQSGsoh29GLYcvUF62JmENLpjQbOYaJgi5F0fL5ZVtfCrqiGS2LzBVUCiYxuR4lloZw+AetONuoKt3BzOvOMZD+Blm9+e4OttyH/gyD4oyJC6QJCVOfsxxYmZ3F1Zrf63Eq9jkDMYG2gAN+t00a2xyLJBgSSQimDTyU+3j89m93XOpDpQP+7dpwzmq7oyclUwxJpgRzAu7TC2V4hTijKDJzKhheKs5EM4xRFMF0we9W3lo7uPPf265IsaIZwZwBPnzGa7UpzCjWOfgvdXzY4Iz3sEcaR9NyuwD3/oDO5bjWZIUuAe9V8aCOb1f99vo0lasvWsIbJ3XvWojxNnNscgh6QPafvc5g/Nnp0DsEw00M"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>原图坦克 [图片1] [图片2]</span></span></code></pre>
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
<td>图片1</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>第一帧图片（表图）</td>
<td>[图片] / 123456 / @用户</td>
</tr>
<tr>
<td>图片2</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>第二帧图片（里图）</td>
<td>[图片] / 123456 / @用户</td>
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
<td>width</td>
<td>-w</td>
<td>number</td>
<td>设置输出宽度</td>
<td>400</td>
</tr>
<tr>
<td>height</td>
<td>-h</td>
<td>number</td>
<td>设置输出高度</td>
<td>400</td>
</tr>
<tr>
<td>delay</td>
<td>-d</td>
<td>number</td>
<td>设置帧延迟（毫秒）</td>
<td>1000</td>
</tr>
<tr>
<td>quality</td>
<td>-q</td>
<td>number</td>
<td>设置图片质量（1-100）</td>
<td>90</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本使用" tabindex="-1"><a class="header-anchor" href="#基本使用"><span>基本使用</span></a></h3>
<h4 id="交互式输入图片" tabindex="-1"><a class="header-anchor" href="#交互式输入图片"><span>交互式输入图片</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克</chat-message>
<chat-message nickname="bot" type="bot">
请发送第一张图片（表图）
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
请发送第二张图片（里图）
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
<FileMessage
  fileName="output.JPG"
  :fileSize="9014454"
  downloadUrl="./output.JPG"
  fileType="image"
/>
</chat-message>
</chat-panel>
<h4 id="直接上传两张图片" tabindex="-1"><a class="header-anchor" href="#直接上传两张图片"><span>直接上传两张图片</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 [图片] [图片]</chat-message>
<chat-message nickname="bot" type="bot">
<FileMessage
  fileName="output.JPG"
  :fileSize="9014454"
  downloadUrl="./output.JPG"
  fileType="image"
/>
</chat-message>
</chat-panel>
<h3 id="使用qq头像" tabindex="-1"><a class="header-anchor" href="#使用qq头像"><span>使用QQ头像</span></a></h3>
<h4 id="使用qq号" tabindex="-1"><a class="header-anchor" href="#使用qq号"><span>使用QQ号</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 123456 654321</chat-message>
<chat-message nickname="bot" type="bot">
[使用两个QQ号头像生成的GIF图片]
</chat-message>
</chat-panel>
<h4 id="使用-用户" tabindex="-1"><a class="header-anchor" href="#使用-用户"><span>使用@用户</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 @用户1 @用户2</chat-message>
<chat-message nickname="bot" type="bot">
[使用两个用户头像生成的GIF图片]
</chat-message>
</chat-panel>
<h3 id="使用选项参数" tabindex="-1"><a class="header-anchor" href="#使用选项参数"><span>使用选项参数</span></a></h3>
<h4 id="自定义尺寸" tabindex="-1"><a class="header-anchor" href="#自定义尺寸"><span>自定义尺寸</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 [图片] [图片] -w 500 -h 500</chat-message>
<chat-message nickname="bot" type="bot">
[500x500尺寸的GIF图片]
</chat-message>
</chat-panel>
<h4 id="调整延迟时间" tabindex="-1"><a class="header-anchor" href="#调整延迟时间"><span>调整延迟时间</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 [图片] [图片] -d 2000</chat-message>
<chat-message nickname="bot" type="bot">
[2秒延迟的GIF图片]
</chat-message>
</chat-panel>
<h4 id="调整图片质量" tabindex="-1"><a class="header-anchor" href="#调整图片质量"><span>调整图片质量</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 [图片] [图片] -q 95</chat-message>
<chat-message nickname="bot" type="bot">
[高质量95的GIF图片]
</chat-message>
</chat-panel>
<h4 id="完整参数示例" tabindex="-1"><a class="header-anchor" href="#完整参数示例"><span>完整参数示例</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">原图坦克 [图片] [图片] -w 600 -h 600 -d 1500 -q 85</chat-message>
<chat-message nickname="bot" type="bot">
[600x600尺寸、1.5秒延迟、质量85的GIF图片]
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的图片格式" tabindex="-1"><a class="header-anchor" href="#支持的图片格式"><span>支持的图片格式</span></a></h3>
<ul>
<li>JPEG</li>
<li>PNG</li>
<li>GIF</li>
<li>WebP</li>
<li>BMP</li>
<li>TIFF</li>
<li>SVG</li>
</ul>
<h3 id="图片来源" tabindex="-1"><a class="header-anchor" href="#图片来源"><span>图片来源</span></a></h3>
<ul>
<li><strong>直接上传</strong>: 通过消息发送图片</li>
<li><strong>QQ头像</strong>: 使用QQ号或@用户获取头像</li>
<li><strong>网络图片</strong>: 支持图片URL</li>
</ul>
<h3 id="处理流程" tabindex="-1"><a class="header-anchor" href="#处理流程"><span>处理流程</span></a></h3>
<ol>
<li><strong>图片获取</strong>: 从用户输入或交互中获取两张图片</li>
<li><strong>尺寸分析</strong>: 使用canvas分析图片尺寸</li>
<li><strong>尺寸统一</strong>: 自动调整两张图片到相同尺寸</li>
<li><strong>GIF合成</strong>: 使用ffmpeg合成两帧GIF</li>
<li><strong>结果返回</strong>: 返回生成的GIF图片</li>
</ol>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>平台限制</strong>: 仅支持onebot平台使用此功能</li>
<li><strong>显示效果</strong>: GIF不会自动连续播放，需要手动切换</li>
<li><strong>文件发送</strong>: 建议以群文件形式发送以获得最佳效果</li>
<li><strong>服务依赖</strong>: 需要ffmpeg和canvas服务支持</li>
<li><strong>处理时间</strong>: 大尺寸图片可能需要较长时间处理</li>
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
<td>sendAsFile</td>
<td>boolean</td>
<td>true</td>
<td>是否以群文件形式发送GIF</td>
</tr>
<tr>
<td>loopCount</td>
<td>number</td>
<td>1</td>
<td>GIF循环次数</td>
</tr>
<tr>
<td>finalDelay</td>
<td>number</td>
<td>50000</td>
<td>最后一帧延迟（毫秒）</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>原图坦克功能基于ffmpeg和canvas实现，能够处理各种图片格式并生成高质量的两帧GIF图片。建议在手机QQ中查看效果以获得最佳体验。</p>
</div>
</div></template>


