<template><div><h1 id="二维码生成" tabindex="-1"><a class="header-anchor" href="#二维码生成"><span>二维码生成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: qrcode</p>
<p><strong>功能描述</strong>: 生成并发送二维码图片</p>
<p><strong>插件名称</strong>: QRCode</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6ACXaJgUwTVo2LClUw2iIUdSnxhhciKgujBkHwboCFQVMU3sV0pvUtHDoDWKizaGfm/+afM+ecxRVtIxqXUzrMiT6gIyJZxUeSe593Vs4nnVlYSsnJOMwl1Myms+XaDoCEEK7f0lPWS4Md7A+EqDbcUtSYb9wgpMWU5TRIvf8knYgZVU+sKm6nAT1LQTkZlXVynceHFTfVGyGuuxXX1S5DAaSglkjHE6SyR0qtccMg18eVQFiSY3JSV1J+TVUWtJE7nQyIEhIF+jIPSZDWUtExqRfp6HwQfQT8/hmaVmeBEF3BxPdpGUgrR7KNKdM4MtutCQcKOUyIIxUIq8qspsP69DTOn9j1OqOCw0IHOXoLDLAfqqRUYFgg7CCBMGeqwK4yP8s/W2d/rfouNbCb271mOjkbhIRYkyGRM3dgfnUpw9KAjXOOCQwTOHYPVvGG5AqmcWy136xy1tvtAexuEV+V8FXHOtj3iukRzI9L2jS4tmMV9rxf9gT4PI+NIm5m7equl8vzP6lkCXdl/YWbsfLwsEeK9wrkomPVjJHXRXy/Yocu4g=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>qrcode &#x3C;text></span></span></code></pre>
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
<td>text</td>
<td>文本</td>
<td>是</td>
<td>要编码为二维码的文本内容</td>
<td>Hello World</td>
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
<td>margin</td>
<td>-m</td>
<td>number</td>
<td>二维码边界尺寸</td>
<td>4</td>
</tr>
<tr>
<td>scale</td>
<td>-s</td>
<td>number</td>
<td>二维码缩放比例</td>
<td>4</td>
</tr>
<tr>
<td>width</td>
<td>-w</td>
<td>number</td>
<td>二维码图片大小</td>
<td>-</td>
</tr>
<tr>
<td>dark</td>
<td>-d</td>
<td>color</td>
<td>暗部颜色（二维码点颜色）</td>
<td>-</td>
</tr>
<tr>
<td>light</td>
<td>-l</td>
<td>color</td>
<td>亮部颜色（背景颜色）</td>
<td>-</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本二维码生成" tabindex="-1"><a class="header-anchor" href="#基本二维码生成"><span>基本二维码生成</span></a></h3>
<h4 id="生成文本二维码" tabindex="-1"><a class="header-anchor" href="#生成文本二维码"><span>生成文本二维码</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">qrcode Hello World</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/二维码生成.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="使用选项" tabindex="-1"><a class="header-anchor" href="#使用选项"><span>使用选项</span></a></h3>
<h4 id="自定义边界和缩放" tabindex="-1"><a class="header-anchor" href="#自定义边界和缩放"><span>自定义边界和缩放</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">qrcode -m 8 -s 6 https://tangbot.xyz</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/二维码生成2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="自定义颜色" tabindex="-1"><a class="header-anchor" href="#自定义颜色"><span>自定义颜色</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">qrcode -d #FF0000 -l #FFFF00 联系方式</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/二维码生成3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="指定图片大小" tabindex="-1"><a class="header-anchor" href="#指定图片大小"><span>指定图片大小</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">qrcode -w 300 重要信息</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/二维码生成4.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="wifi信息" tabindex="-1"><a class="header-anchor" href="#wifi信息"><span>WiFi信息</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">qrcode WIFI:S:iQOO Neo11;T:WPA2;P:114514;H:false;;</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/二维码生成5.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的编码内容" tabindex="-1"><a class="header-anchor" href="#支持的编码内容"><span>支持的编码内容</span></a></h3>
<ul>
<li><strong>纯文本</strong>: 任意文本内容</li>
<li><strong>URL链接</strong>: 网页地址</li>
<li><strong>联系方式</strong>: 电话号码、邮箱地址</li>
<li><strong>WiFi信息</strong>: SSID和密码</li>
<li><strong>地理位置</strong>: 坐标信息</li>
<li><strong>事件信息</strong>: 日历事件</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>格式验证</strong>: 自动验证输入文本的有效性</li>
<li><strong>大小优化</strong>: 根据内容自动调整二维码复杂度</li>
<li><strong>颜色处理</strong>: 支持自定义颜色配置</li>
<li><strong>图片格式</strong>: 生成PNG格式的二维码图片</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>空文本</strong>: 当未提供文本内容时提示</li>
<li><strong>无效内容</strong>: 当输入包含特殊格式时提示</li>
<li><strong>生成失败</strong>: 当二维码生成过程中出现错误时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>内容长度</strong>: 二维码可容纳的数据量有限，过长的文本可能导致二维码过于复杂</li>
<li><strong>扫描兼容性</strong>: 确保生成的二维码能被常见扫码工具识别</li>
<li><strong>颜色对比</strong>: 自定义颜色时确保暗部和亮部颜色有足够的对比度</li>
<li><strong>图片大小</strong>: 大尺寸二维码可能影响消息发送速度</li>
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
<td>margin</td>
<td>number</td>
<td>4</td>
<td>二维码边界尺寸</td>
</tr>
<tr>
<td>scale</td>
<td>number</td>
<td>4</td>
<td>二维码缩放比例</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>二维码生成功能基于qrcode库实现，支持生成标准QR码，能够被大多数扫码工具识别。可以用于分享链接、联系方式、文本信息等多种场景。</p>
</div>
</div></template>


