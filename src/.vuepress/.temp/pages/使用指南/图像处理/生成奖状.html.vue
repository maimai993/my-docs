<template><div><h1 id="生成奖状" tabindex="-1"><a class="header-anchor" href="#生成奖状"><span>生成奖状</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-certificate-achievement" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-certificate-achievement" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/certificate-achievement" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 生成奖状</p>
<p><strong>功能描述</strong>: 生成一张自定义的奖状图片，可指定获奖者、奖项名称和授权单位</p>
<p><strong>插件名称</strong>: certificate-achievement</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kktPwkAQx+98iol3NH4Bk8oRA60Jp8ZDhVVqtG1KUY8aX6gh+CDGV1AEBR9BYyIafH0X093Wb+GyW8FCnUO7O/Pb/8zO7NSsvpBMK6YFY+MhoJaQnWKd5J4n2I59MtnJaVMx0jCmatlF5vK5BZAlCTcu6Cnn9p4f/DVJorGuC2mpUL9ATE+hmQzI7f8gXYxnNUudQ36lDj1KQcVIKhY5zeOtsp9qW8yL+yO+1D7BCMhRXc2kVVJeJ6Vmv2DUi/dHhLispBTDQmZY19Ck3pOzbRFBTiLTUqdUWhIKK8m0iubRHNICWFGUjaxhIAshs7/63nXnRgkIh0doq9lGkugOBr52z4E0c2T5fshubduvzQEGxRgT85AyxDU0qlswPzyM8wW30eBUtDv8qIdeAAfcWoWUdjgmxBkixD2mAjyV/Xb+vbT3V+pXpQruw0r7gRX2OiVFBIZEBI+5BPv9kzKdTnBMFBkmih52BeSp4NZy+KhOXh7J2X6wWg3czyI+KeHLA2eriU8+nM2NoMrqYL8c0+eEq6vOznrw/a4B7+dxq4gflt3KWpDKzT8N5W339f7WE+ND4ljvCO+AHH441RYvnjOJ0A8YSThB"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>生成奖状 &#x3C;姓名> &#x3C;奖项> [单位]</span></span></code></pre>
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
<td>姓名</td>
<td>文本</td>
<td>是</td>
<td>获奖者姓名</td>
<td>张三</td>
</tr>
<tr>
<td>奖项</td>
<td>文本</td>
<td>是</td>
<td>奖项名称</td>
<td>galgame糕手</td>
</tr>
<tr>
<td>单位</td>
<td>文本</td>
<td>否</td>
<td>授权单位，如不指定则使用默认值</td>
<td>本群授奖处</td>
</tr>
</tbody>
</table>
<h3 id="配置选项" tabindex="-1"><a class="header-anchor" href="#配置选项"><span>配置选项</span></a></h3>
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
<td>commandname</td>
<td>string</td>
<td>'生成奖状'</td>
<td>指令名称</td>
</tr>
<tr>
<td>customText</td>
<td>string</td>
<td>'在本学年第一学期中表现优秀，被本群决定\n评为'</td>
<td>奖状中间的自定义文字</td>
</tr>
<tr>
<td>defaultClassname</td>
<td>string</td>
<td>'本群指定授奖处'</td>
<td>默认的授奖单位</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本奖状生成" tabindex="-1"><a class="header-anchor" href="#基本奖状生成"><span>基本奖状生成</span></a></h3>
<h4 id="生成简单奖状" tabindex="-1"><a class="header-anchor" href="#生成简单奖状"><span>生成简单奖状</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">生成奖状 张三 galgame糕手</chat-message>
<chat-message nickname="bot" type="bot">
[奖状图片]
</chat-message>
</chat-panel>
<h4 id="指定授奖单位" tabindex="-1"><a class="header-anchor" href="#指定授奖单位"><span>指定授奖单位</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">生成奖状 李四 游戏苦手 本群授奖处</chat-message>
<chat-message nickname="bot" type="bot">
[奖状图片]
</chat-message>
</chat-panel>
<h3 id="高级用法" tabindex="-1"><a class="header-anchor" href="#高级用法"><span>高级用法</span></a></h3>
<h4 id="自定义奖状文字" tabindex="-1"><a class="header-anchor" href="#自定义奖状文字"><span>自定义奖状文字</span></a></h4>
<p>通过插件配置可以修改奖状中间的自定义文字，例如：</p>
<ul>
<li>&quot;在本次活动中表现突出，荣获&quot;</li>
<li>&quot;因在技术分享中贡献卓越，特授予&quot;</li>
</ul>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="渲染技术" tabindex="-1"><a class="header-anchor" href="#渲染技术"><span>渲染技术</span></a></h3>
<ul>
<li><strong>基于Puppeteer</strong>: 使用无头浏览器进行HTML渲染</li>
<li><strong>本地渲染</strong>: 所有处理在本地完成，无需外部服务</li>
<li><strong>高质量输出</strong>: 生成PNG格式的高质量图片</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>模板加载</strong>: 自动加载预设的奖状模板图片</li>
<li><strong>文字定位</strong>: 智能定位姓名、奖项和单位的位置</li>
<li><strong>格式保持</strong>: 保持奖状原有的美观格式</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>参数验证</strong>: 当缺少必要参数时提示用户</li>
<li><strong>渲染失败</strong>: 当图片生成过程中出现错误时提示</li>
<li><strong>超时处理</strong>: 设置合理的渲染超时时间</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>姓名长度</strong>: 建议使用2~3个汉字或适当长度的英文，过长可能影响显示效果</li>
<li><strong>依赖要求</strong>: 需要安装puppeteer服务才能正常使用</li>
<li><strong>渲染时间</strong>: 首次使用可能需要较长时间加载浏览器实例</li>
<li><strong>图片大小</strong>: 生成的奖状图片尺寸为1214x902像素</li>
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
<td>commandname</td>
<td>string</td>
<td>'生成奖状'</td>
<td>指令名称，可自定义</td>
</tr>
<tr>
<td>customText</td>
<td>string</td>
<td>'在本学年第一学期中表现优秀，被本群决定\n评为'</td>
<td>奖状中间的自定义文字，支持换行</td>
</tr>
<tr>
<td>defaultClassname</td>
<td>string</td>
<td>'本群指定授奖处'</td>
<td>默认的授奖单位名称</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>奖状生成功能基于puppeteer实现，能够准确渲染自定义文字到奖状模板上，生成美观的奖状图片。支持自定义奖状文字内容和授奖单位，满足不同场景的使用需求。</p>
</div>
</div></template>


