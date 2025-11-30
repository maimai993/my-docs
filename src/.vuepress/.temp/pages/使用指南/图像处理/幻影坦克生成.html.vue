<template><div><h1 id="幻影坦克生成" tabindex="-1"><a class="header-anchor" href="#幻影坦克生成"><span>幻影坦克生成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 幻影、幻影坦克</p>
<p><strong>功能描述</strong>: 制作幻影坦克图片，通过两张图片的混合实现在不同亮度下显示不同图片的效果</p>
<p><strong>插件名称</strong>: patina</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl/ABD1ioDVwajxUWaVG2waKetT4EaIhqHDwK4QvBcUAF9GAyLuY7ra+hUt3+SjgHNrdmd/+Z3Zmt3a1g82oHDNgdc0D1MKSla2S5Me6s3M+8cTGdkzWo7CqqIlDx+Vy+0ASRVwv0lNWrcEODkwUaWzkQmrEMy0Q0CJoJw5S/z9PF2sJ1VD2kFtpSC9TUNY3ZYM8pvBFwU31LcDj7ogrtUtwBSS/psSjCimck1xrWtDP49MRX1CSI7JuoJhXU9GGNpGzb0JI0mVDUeUZIUHSE7qODIRi08VOrocXCIPXu0Q762xEke5g7uc6D6SVJMeNBbN9aXZacw4UcJgARwoQVNGyZsD+4iJOpe16nVH+0az9HC0CA+xKieSuGOYLOogvyJkSsFTmV/736GZcaqBSBrt50n9P6ZthSULIQYQQZ57A7PYoM+wExwSGCRx7BvKetitJfFclmZTZfZytVgG7l8UPOVw+ta7OrU6G5DjprqwK5uc9fT2Mm32/F8CZFG5ncfPYLp3NUnn9p6Gs7a7e17gYGxLDJkf4BuT22yq3x8sOe/4AsEIx8Q=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>幻影 [图片1] [图片2]</span></span>
<span class="line"><span>幻影坦克 [图片1] [图片2]</span></span></code></pre>
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
<td>图片1</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>表图（正常显示）</td>
<td>[图片] / 123456 / @用户</td>
</tr>
<tr>
<td>图片2</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>里图（暗处显示）</td>
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
<td>fullColor</td>
<td>-f</td>
<td>无</td>
<td>开启全彩输出，关闭则为黑白图</td>
<td>false</td>
</tr>
<tr>
<td>size</td>
<td>-s</td>
<td>number</td>
<td>指定输出图像尺寸（长宽中的较大值）</td>
<td>1200</td>
</tr>
<tr>
<td>weight</td>
<td>-w</td>
<td>number</td>
<td>设置里图混合权重，范围为0到1</td>
<td>0.7</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本使用" tabindex="-1"><a class="header-anchor" href="#基本使用"><span>基本使用</span></a></h3>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>效果在网页文档显示可能较差，请在QQ中查看效果更佳<br>
在QQ发送时请勾选原图<br>
不支持动图生成</p>
</div>
<h4 id="交互式输入图片" tabindex="-1"><a class="header-anchor" href="#交互式输入图片"><span>交互式输入图片</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片作为【表图】：
</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif5.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片作为【里图】：
</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif10.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/幻影坦克.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="直接上传两张图片" tabindex="-1"><a class="header-anchor" href="#直接上传两张图片"><span>直接上传两张图片</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 
<p><img src="@source/使用指南/图像处理/gif5.gif" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/gif10.gif" alt="" loading="lazy"></p>
</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/幻影坦克.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用qq头像" tabindex="-1"><a class="header-anchor" href="#使用qq头像"><span>使用QQ头像</span></a></h3>
<h4 id="使用qq号" tabindex="-1"><a class="header-anchor" href="#使用qq号"><span>使用QQ号</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 123456 654321</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/幻影坦克2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="使用-用户" tabindex="-1"><a class="header-anchor" href="#使用-用户"><span>使用@用户</span></a></h4>
<chat-panel>
<chat-message nickname="马化腾" type="user">大家好，我是马化腾</chat-message>
<chat-message nickname="腾讯视频" type="user">大家好，我是腾讯视频</chat-message>
<chat-message nickname="用户" type="user">幻影 <span style="color: #3175de;">@腾讯视频 @马化腾</span></chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/幻影坦克2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用选项参数" tabindex="-1"><a class="header-anchor" href="#使用选项参数"><span>使用选项参数</span></a></h3>
<h4 id="全彩输出" tabindex="-1"><a class="header-anchor" href="#全彩输出"><span>全彩输出</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 -f
<p><img src="@source/使用指南/图像处理/gif5.gif" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/gif10.gif" alt="" loading="lazy"></p>
</chat-message>
<chat-message nickname="bot" type="bot">
![](./幻影坦克3.png)
</chat-message>
</chat-panel>
<h4 id="自定义尺寸和权重" tabindex="-1"><a class="header-anchor" href="#自定义尺寸和权重"><span>自定义尺寸和权重</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 [图片] [图片] -s 800 -w 0.5</chat-message>
<chat-message nickname="bot" type="bot">
[尺寸800、权重0.5的幻影坦克图片]
</chat-message>
</chat-panel>
<h4 id="完整参数示例" tabindex="-1"><a class="header-anchor" href="#完整参数示例"><span>完整参数示例</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影坦克 [图片] [图片] -f -s 1000 -w 0.8</chat-message>
<chat-message nickname="bot" type="bot">
[全彩输出、尺寸1000、权重0.8的幻影坦克图片]
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
<li><strong>参数配置</strong>: 应用用户指定的选项参数</li>
<li><strong>图像处理</strong>: 使用puppeteer在浏览器中处理图片</li>
<li><strong>结果返回</strong>: 返回处理后的幻影坦克图片</li>
</ol>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来处理图片</li>
<li><strong>处理时间</strong>: 复杂图片可能需要较长时间处理</li>
<li><strong>图片大小</strong>: 大尺寸图片会自动调整以适应处理需求</li>
<li><strong>效果预览</strong>: 建议先在网页版工具中预览效果：<a href="https://uyanide.github.io/Mirage_Colored/" target="_blank" rel="noopener noreferrer">https://uyanide.github.io/Mirage_Colored/</a></li>
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
<td>Full_color_output</td>
<td>boolean</td>
<td>false</td>
<td>全彩输出，关闭后变成黑白图</td>
</tr>
<tr>
<td>Output_Size</td>
<td>number</td>
<td>1200</td>
<td>输出尺寸（长宽中的较大值）</td>
</tr>
<tr>
<td>Mixed_Weight</td>
<td>number</td>
<td>0.7</td>
<td>里图混合权重，数值越大里图越隐约可见</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>幻影坦克功能基于puppeteer实现，能够准确处理各种图片格式，生成高质量的隐写图片。</p>
</div>
</div></template>


