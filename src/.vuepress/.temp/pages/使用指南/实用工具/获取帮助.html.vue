<template><div><h1 id="获取帮助" tabindex="-1"><a class="header-anchor" href="#获取帮助"><span>获取帮助</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: <code v-pre>帮助</code>  <code v-pre>help</code></p>
<p><strong>功能描述</strong>: 以图片形式展示帮助信息，包括指令列表和具体指令的详细用法</p>
<p><strong>插件名称</strong>: help-image</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9ksFu2kAQhu88xSh3WuUFKpFeQFCwo3KyenDCNrhKbAtM22OjNtRNhaCBQ9pUJARaSNKYqFIppVH6LhW7dt4iy+4GsHEyB3t359t/Zmfm+abxaj2vFixIrUaAWlZxGz1i/37GduxTLK1tFFQzDylNL71mR77jGCiyjJ1jess96/OLtybL1Dc7QnousiiQNnLoRRGUyf8BXayWdEvbQn6lKb1CQdVcVy3ytYJ3W35qYmnh93t8oX2Cj0FJGloxr5FWmTQHi4JJ4V/0xDKKmlNNCxWiho7WjEDMicUTSh5tmlFtS90IPGlikqSYJdNEFkKFxYSD6+kjshCNPqLVZRtZpjtY+v/pCMjAJtv9h+PRx/HfwRKD0oxJC6QFGR2tGBa8XF7GlarnOJxKzvqdFOgxcMDrtkmzxrFYhiGxjGDawEONL4+u3+zNS92qdMC7eEtnalYEUt2bJhdPMDieEPQ3cBuHxK7Fnz5J4fIOdv6Ec9+F6rR2ZPiTHNY5LEkMliQBd4H8qnpdG3/u3Yf1wPvXwAdNYp/ig6vwuCfgXtbx+T7uvHNr5XDmVOhQEffD+7CanMF4+IXO7rxKsLI/ANcreNTAF9teeydM5fyOVvKG+7ruCDE+HhwLDk8fyP6V2xnhoYN3T+aTz0ZuAP7WZtE="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>帮助 [指令]</span></span></code></pre>
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
<td>指令</td>
<td>文本</td>
<td>否</td>
<td>获取指令的具体用法</td>
<td>帮助</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="获取指令列表" tabindex="-1"><a class="header-anchor" href="#获取指令列表"><span>获取指令列表</span></a></h4>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>部分指令不会出现在该列表中，具体参考<a href="/features">功能列表</a>为准</p>
</div>
<chat-panel>
<chat-message nickname="用户" type="user">帮助</chat-message>
<chat-message nickname="bot" type="bot">
<span style="color: #575c63ff;">图片过长已隐藏</span>
</chat-message>
</chat-panel>
<h4 id="获取指定指令-帮助-信息" tabindex="-1"><a class="header-anchor" href="#获取指定指令-帮助-信息"><span>获取指定指令 <code v-pre>帮助</code> 信息</span></a></h4>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>部分指令不支持获取帮助，具体的使用方法请查看文档</p>
</div>
<chat-panel>
<chat-message nickname="用户" type="user">帮助 帮助</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/获取帮助_帮助的帮助图.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<div class="hint-container info">
<p class="hint-container-title">相关信息</p>
<p>您还可以使用 -h 参数获取该指令的帮助</p>
</div>
<h4 id="使用参数-h-获取指定指令-帮助-信息" tabindex="-1"><a class="header-anchor" href="#使用参数-h-获取指定指令-帮助-信息"><span>使用参数 <code v-pre>-h</code> 获取指定指令 <code v-pre>帮助</code> 信息</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">帮助 -h</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/获取帮助_帮助的帮助图.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="智能缓存机制" tabindex="-1"><a class="header-anchor" href="#智能缓存机制"><span>智能缓存机制</span></a></h3>
<ul>
<li><strong>文件缓存</strong>: 生成的帮助图片会缓存在 <code v-pre>data/help-image/cache/</code> 目录中</li>
<li><strong>内容比对</strong>: 通过比较HTML内容判断是否需要重新生成图片</li>
<li><strong>后台更新</strong>: 缓存命中时，会在后台异步更新缓存文件</li>
<li><strong>调试日志</strong>: 支持通过配置项开启缓存操作的调试日志</li>
</ul>
<h3 id="html渲染引擎" tabindex="-1"><a class="header-anchor" href="#html渲染引擎"><span>HTML渲染引擎</span></a></h3>
<ul>
<li><strong>毛玻璃效果</strong>: 使用CSS backdrop-filter实现现代化毛玻璃背景</li>
<li><strong>响应式设计</strong>: 自适应不同屏幕尺寸和设备</li>
<li><strong>中文字体</strong>: 集成Noto Sans SC字体，确保中文显示效果</li>
<li><strong>代码高亮</strong>: 专门的代码块样式，提高可读性</li>
</ul>
<h3 id="权限系统集成" tabindex="-1"><a class="header-anchor" href="#权限系统集成"><span>权限系统集成</span></a></h3>
<ul>
<li><strong>权限过滤</strong>: 自动过滤用户无权访问的指令</li>
<li><strong>权限提示</strong>: 在帮助信息中显示指令的最低权限等级</li>
<li><strong>动态内容</strong>: 根据用户权限动态生成帮助内容</li>
</ul>
<h2 id="配置选项" tabindex="-1"><a class="header-anchor" href="#配置选项"><span>配置选项</span></a></h2>
<p>help-image插件支持以下配置参数：</p>
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
<td><code v-pre>shortcut</code></td>
<td>boolean</td>
<td><code v-pre>true</code></td>
<td>是否启用快捷调用（直接输入&quot;帮助&quot;）</td>
</tr>
<tr>
<td><code v-pre>options</code></td>
<td>boolean</td>
<td><code v-pre>true</code></td>
<td>是否为每个指令添加 <code v-pre>-h, --help</code> 选项</td>
</tr>
<tr>
<td><code v-pre>debug</code></td>
<td>boolean</td>
<td><code v-pre>false</code></td>
<td>是否在控制台输出调试日志（缓存命中情况）</td>
</tr>
<tr>
<td><code v-pre>style.width</code></td>
<td>number</td>
<td><code v-pre>600</code></td>
<td>图片宽度（像素）</td>
</tr>
<tr>
<td><code v-pre>style.cardColor</code></td>
<td>string</td>
<td><code v-pre>#ffffff</code></td>
<td>卡片背景颜色（毛玻璃底色）</td>
</tr>
<tr>
<td><code v-pre>style.primaryColor</code></td>
<td>string</td>
<td><code v-pre>#007bff</code></td>
<td>主标题和重点部分颜色</td>
</tr>
<tr>
<td><code v-pre>style.textColor</code></td>
<td>string</td>
<td><code v-pre>#333333</code></td>
<td>主要文字颜色</td>
</tr>
<tr>
<td><code v-pre>style.codeColor</code></td>
<td>string</td>
<td><code v-pre>#e83e8c</code></td>
<td>代码块颜色</td>
</tr>
<tr>
<td><code v-pre>style.customCSS</code></td>
<td>string</td>
<td><code v-pre>&quot;&quot;</code></td>
<td>自定义CSS样式</td>
</tr>
</tbody>
</table>
<h2 id="高级用法" tabindex="-1"><a class="header-anchor" href="#高级用法"><span>高级用法</span></a></h2>
<h3 id="显示隐藏选项" tabindex="-1"><a class="header-anchor" href="#显示隐藏选项"><span>显示隐藏选项</span></a></h3>
<p>使用 <code v-pre>-H</code> 参数可以显示被隐藏的选项和指令：</p>
<chat-panel>
<chat-message nickname="用户" type="user">帮助 -H</chat-message>
<chat-message nickname="bot" type="bot">
<span style="color: #575c63ff;">图片过长已隐藏</span>
</chat-message>
</chat-panel>
<h2 id="故障排除" tabindex="-1"><a class="header-anchor" href="#故障排除"><span>故障排除</span></a></h2>
<h3 id="常见问题" tabindex="-1"><a class="header-anchor" href="#常见问题"><span>常见问题</span></a></h3>
<ol>
<li>
<p><strong>帮助图片显示异常</strong></p>
<ul>
<li>检查puppeteer插件是否正确安装</li>
<li>确认系统有足够的可用内存</li>
<li>查看控制台错误日志</li>
</ul>
</li>
<li>
<p><strong>缓存问题</strong></p>
<ul>
<li>删除 <code v-pre>data/help-image/cache/</code> 目录强制重新生成</li>
<li>启用debug模式查看缓存操作日志</li>
</ul>
</li>
<li>
<p><strong>权限问题</strong></p>
<ul>
<li>确认用户有访问相应指令的权限</li>
<li>检查权限配置是否正确</li>
</ul>
</li>
</ol>
<h3 id="性能优化" tabindex="-1"><a class="header-anchor" href="#性能优化"><span>性能优化</span></a></h3>
<ul>
<li><strong>缓存策略</strong>: 首次生成后，后续请求会直接使用缓存图片</li>
<li><strong>异步更新</strong>: 缓存命中时在后台异步更新，不阻塞用户响应</li>
<li><strong>内存管理</strong>: 及时关闭浏览器页面，避免内存泄漏</li>
</ul>
</div></template>


