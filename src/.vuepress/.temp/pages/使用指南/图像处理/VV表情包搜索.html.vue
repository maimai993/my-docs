<template><div><h1 id="vv表情包搜索" tabindex="-1"><a class="header-anchor" href="#vv表情包搜索"><span>VV表情包搜索</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-vv-bot" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-vv-bot" alt="" loading="lazy"></a> <a href="https://github.com/738NGX/vv-bot" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: vv</p>
<p><strong>功能描述</strong>: 搜索并返回VV表情包图片</p>
<p><strong>插件名称</strong>: vv-bot</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl/ApPVkMGBNqIfGQ5EqGG0JFPSoUfwmoKIxaoh8KPgFHAwSJPguht3Wt3DbLWChzKHdnfntf2ZndnVD2VoJiVEV5hddQMwvaNkKPvpcNnfmJxYPrEXFSAjmw3J823TZ3AwIHIeqBXJKe63Rgz3jOBIbuCQ56BoV8CpBaT0GgvGfJIvFuKyGNyW7Up9mCShGVkQV36fQSd5OGea14vaILbVNcBYEjxKOhcI4f4BzjVFBjxUfjTA+QQyKEVWKuhVZCihDOQ3jWSGRcI+EjHKG1/0S/eB2z5DemRuOIzuY+Dl/ANw4wru1qW7rtPvVmDAhr8l4LSQPPlliFRUS09MoldarVUp5BtP0WGgBKKCXiziXoRjjMxHGZzFFoKm67YffnYv/Uj2VEuj1PePFpC/6JfGsifCsxTxaDM8DszCHM/faR8GZfAJaDQFQ+wpfH47VLANOZ1D6ekkKLKBm2RmqgP6dRXc5PV/Be0l0lkR3He340Okez9Bt3pLXhEr7WubAuRsvgC5TqJVF9V29mHRSeR3Tfjok26TeLDE6UooND/wd8E1HK7X69VPM7/oDcGM/ow=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>vv &#x3C;搜索关键词> [数量]</span></span></code></pre>
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
<td>搜索关键词</td>
<td>文本</td>
<td>是</td>
<td>要搜索的表情包关键词</td>
<td>开心</td>
</tr>
<tr>
<td>数量</td>
<td>数字</td>
<td>否</td>
<td>返回的表情包数量，默认1，最大5</td>
<td>3</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="搜索单个表情包" tabindex="-1"><a class="header-anchor" href="#搜索单个表情包"><span>搜索单个表情包</span></a></h3>
<h4 id="搜索-开心-表情包" tabindex="-1"><a class="header-anchor" href="#搜索-开心-表情包"><span>搜索&quot;开心&quot;表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">vv 开心</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/vvkx.webp" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="搜索多个表情包" tabindex="-1"><a class="header-anchor" href="#搜索多个表情包"><span>搜索多个表情包</span></a></h3>
<h4 id="搜索3个-惊讶-表情包" tabindex="-1"><a class="header-anchor" href="#搜索3个-惊讶-表情包"><span>搜索3个&quot;惊讶&quot;表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">vv 惊讶 3</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/vvjy1.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvjy2.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvjy3.webp" alt="" loading="lazy"></p>
</chat-message>
</chat-panel>
<h4 id="搜索5个-生气-表情包" tabindex="-1"><a class="header-anchor" href="#搜索5个-生气-表情包"><span>搜索5个&quot;生气&quot;表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">vv 生气 5</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/vvsq1.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvsq2.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvsq3.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvsq4.webp" alt="" loading="lazy"><br>
<img src="@source/使用指南/图像处理/vvsq5.webp" alt="" loading="lazy"></p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="搜索原理" tabindex="-1"><a class="header-anchor" href="#搜索原理"><span>搜索原理</span></a></h3>
<ul>
<li><strong>API调用</strong>: 调用VV表情包搜索API获取匹配结果</li>
<li><strong>索引解析</strong>: 解析二进制索引文件定位表情包位置</li>
<li><strong>帧提取</strong>: 从WebP图片中提取特定帧</li>
<li><strong>格式转换</strong>: 将WebP帧转换为Base64数据URL</li>
</ul>
<h3 id="搜索参数" tabindex="-1"><a class="header-anchor" href="#搜索参数"><span>搜索参数</span></a></h3>
<ul>
<li><strong>最小相似度</strong>: 50%</li>
<li><strong>最小比例</strong>: 0.5</li>
<li><strong>最大结果数</strong>: 可配置，默认1，最大5</li>
</ul>
<h3 id="数据处理流程" tabindex="-1"><a class="header-anchor" href="#数据处理流程"><span>数据处理流程</span></a></h3>
<ol>
<li>
<p><strong>搜索阶段</strong>:</p>
<ul>
<li>调用VV API搜索表情包</li>
<li>解析API返回的JSON数据</li>
<li>提取文件夹ID和时间戳信息</li>
</ul>
</li>
<li>
<p><strong>索引解析阶段</strong>:</p>
<ul>
<li>根据文件夹ID计算组索引</li>
<li>下载对应的索引文件(.index)</li>
<li>使用二分查找定位表情包帧位置</li>
</ul>
</li>
<li>
<p><strong>图片提取阶段</strong>:</p>
<ul>
<li>使用Range请求下载WebP图片片段</li>
<li>将二进制数据转换为Blob对象</li>
<li>转换为Base64数据URL格式</li>
</ul>
</li>
<li>
<p><strong>返回阶段</strong>:</p>
<ul>
<li>将数据URL封装为图片消息</li>
<li>返回给用户</li>
</ul>
</li>
</ol>
<h3 id="支持的格式" tabindex="-1"><a class="header-anchor" href="#支持的格式"><span>支持的格式</span></a></h3>
<ul>
<li><strong>输入格式</strong>: 任意文本关键词</li>
<li><strong>输出格式</strong>: WebP图片数据URL</li>
<li><strong>索引格式</strong>: 自定义二进制索引文件</li>
<li><strong>图片格式</strong>: WebP动画帧</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接访问VV API和图片服务器</li>
<li><strong>搜索限制</strong>: 每次最多返回5个表情包</li>
<li><strong>相似度阈值</strong>: 搜索结果需要满足50%相似度和0.5比例要求</li>
<li><strong>处理时间</strong>: 复杂搜索可能需要较长时间处理</li>
<li><strong>服务器状态</strong>: 依赖VV API和图片服务器的可用性</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>本插件为轻量级工具，无需额外配置参数。</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>VV表情包搜索功能基于VV表情包数据库实现，能够快速搜索和提取匹配的表情包图片。该功能适合日常聊天和表情包分享需求。</p>
</div>
</div></template>


