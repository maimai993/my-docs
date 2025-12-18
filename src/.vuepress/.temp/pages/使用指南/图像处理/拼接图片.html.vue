<template><div><h1 id="拼接图片" tabindex="-1"><a class="header-anchor" href="#拼接图片"><span>拼接图片</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-pic-splice-lizard" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-pic-splice-lizard" alt="" loading="lazy"></a> <a href="https://github.com/lizard0126/pic-splice-lizard" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 拼图</p>
<p><strong>功能描述</strong>: 将多张图片拼接成一张长图，支持横向或纵向拼接</p>
<p><strong>插件名称</strong>: pic-splice-lizard</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kktPwkAQx+98ion3avwCJugRA62EU+Ohwio12DalqPGk8RGiQXxw8BUUQcFH0JiIBl/fxXSX+i1cugtYqHNod2d++5/ZmZ1N6UvxpGJaMDkVAGoxuVWokezLtLtzP+nMzJypGEmYVLXMsuvyuIMgSxKuX9JTrbsHdrBjkkRjPRfSEoFBgbCeQPNpkNv/YbqYymiWuoC8Sl16nIKKEVcscpbD2yUv1bYwj3sjntQewQmQQ7qaTqqktEWKjUHBEI8PRoIRWUkohoVMQdfQjN6Xs21iVDbUuJA2UmocCSl1RTETPpQoGxnDQBZC5mDd/evuXWIgCGO0ye5GkugOhr73L4A0smTtYcRu7thvjSEXCrtMmCMliGhoXLdgcXQU5/JOvc6oUG/sIY5eAgOcapkU9xgWjLhIMMKZMrBU9vvFz+rBX6mOSgWcx/X208ofdEsSoy4iRjlzBfbHF2W6neCYyDCRY9dAnvNONYuPa+T1iZwf+qtVwfkq4NMi2Xknu1f49NOvrBrYryf0FeHKRmtvy/9yN4APc7hZwI9rTnnTT+X2n26ynnsaf8fF2IQY1j+/eyBHn61Ks6/yWOAX7tw2hA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>拼图 [方向]</span></span></code></pre>
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
<td>方向</td>
<td>文本</td>
<td>否</td>
<td>拼接方向：横向/纵向，默认纵向</td>
<td>横向</td>
</tr>
</tbody>
</table>
<h3 id="操作流程" tabindex="-1"><a class="header-anchor" href="#操作流程"><span>操作流程</span></a></h3>
<ol>
<li>输入 <code v-pre>拼图 [方向]</code> 开始拼接任务</li>
<li>发送多张图片（支持一次性发送多张）</li>
<li>输入 <code v-pre>完成</code> 或等待10秒自动开始拼接</li>
</ol>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="横向拼接图片" tabindex="-1"><a class="header-anchor" href="#横向拼接图片"><span>横向拼接图片</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">拼图 横向</chat-message>
<chat-message nickname="bot" type="bot">请发送图片，输入 "完成" 开始拼接。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/1-1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 1 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/1-2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 2 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/1-3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 3 张图片。</chat-message>
<chat-message nickname="用户" type="user">完成</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="用户" type="user">拼图 横向</chat-message><chat-message nickname="bot" type="bot">请发送图片，输入 "完成" 开始拼接。</chat-message><chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/2-1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 1 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/2-2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 2 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/2-3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 3 张图片。</chat-message>
<chat-message nickname="用户" type="user">完成</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="用户" type="user">拼图 横向</chat-message><chat-message nickname="bot" type="bot">请发送图片，输入 "完成" 开始拼接。</chat-message><chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/3-1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 1 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/3-2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 2 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/3-3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 3 张图片。</chat-message>
<chat-message nickname="用户" type="user">完成</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="纵向拼接图片" tabindex="-1"><a class="header-anchor" href="#纵向拼接图片"><span>纵向拼接图片</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">拼图 纵向</chat-message>
<chat-message nickname="bot" type="bot">请发送图片，输入 "完成" 开始拼接。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/result1.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 1 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/result2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 2 张图片。</chat-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/result3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">已获取 3 张图片。</chat-message>
<chat-message nickname="用户" type="user">完成</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/result.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的图片格式" tabindex="-1"><a class="header-anchor" href="#支持的图片格式"><span>支持的图片格式</span></a></h3>
<ul>
<li>所有浏览器支持的图片格式（JPG、PNG、GIF、WebP等）</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>方向选择</strong>: 支持横向和纵向两种拼接方式</li>
<li><strong>自动超时</strong>: 10秒无操作自动开始拼接</li>
<li><strong>图片收集</strong>: 支持一次性发送多张图片</li>
<li><strong>智能布局</strong>: 根据方向自动调整图片排列方式</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>图片数量不足</strong>: 当图片少于2张时提示</li>
<li><strong>拼接失败</strong>: 当拼接过程中出现错误时提示</li>
<li><strong>方向错误</strong>: 当方向参数不正确时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>图片数量</strong>: 至少需要2张图片才能进行拼接</li>
<li><strong>图片大小</strong>: 建议不要超过10张图片，以免拼接时间过长</li>
<li><strong>操作超时</strong>: 发送图片后10秒内未输入&quot;完成&quot;将自动开始拼接</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接来处理图片</li>
<li><strong>内存使用</strong>: 处理大量图片时可能需要较多内存</li>
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
<td>超时时间</td>
<td>number</td>
<td>10秒</td>
<td>自动拼接的超时时间</td>
</tr>
<tr>
<td>最大图片数</td>
<td>number</td>
<td>10张</td>
<td>单次拼接的最大图片数量</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>拼接图片功能基于puppeteer实现，能够准确渲染图片并生成高质量的拼接图，支持各种尺寸和比例的图片。</p>
</div>
</div></template>


