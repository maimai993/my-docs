<template><div><h1 id="啤酒烧烤表情包生成" tabindex="-1"><a class="header-anchor" href="#啤酒烧烤表情包生成"><span>啤酒烧烤表情包生成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-pjsk-pptr" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-pjsk-pptr" alt="" loading="lazy"></a> <a href="https://github.com/araea/koishi-plugin-pjsk-pptr" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: pjsk</p>
<p><strong>功能描述</strong>: 基于初音未来Project Sekai角色的表情包生成器，支持自定义文字和多种调整选项</p>
<p><strong>插件名称</strong>: pjsk-pptr</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6ACbqzBqiGVeOiyih4aSdQ1KXGS4hK8MLCW1AEBS9BYyIavPAupjPUt3DaGcAWOIt2Zv5v/jlzzswt6auzMTVhwMSkD1hElGauQtNv087M+SRTM/MJFcdgIq6l1pwl13IAFFkm1Wu2q/nwxDe2QpaZ1llCWtTXbRDUo2ghCYr9H2SDyZRmxJeR26lNjzJQxbOqQS8yZLfgpuwICt2tuI52GY6BIunxZCxOCzs0X+s2lITerQRCihpVsYESfl1DM7rnTDvC41OSgheSi36MjUQPPazgFMbIQMij2hl7x+1bRMDvH2HldSayzGYw8HN4BbSWphtPQ2Z9z/yoDThQ0GGCAilASEOjugErw8Mkk7WqVU5JnYZLAr0GDljlIs0fcCwQcpBASDBF4EeZn1e/60f/rVouJbCeN+1HlT1qp2QXxYHsgeBuwPxqMK5dDYGGORgW2C3Q16xVTpPTCn1/oZfH/R3LYDVy5DxvFSp0c5vsb/dKrwLm+xl7R6S01TzY6X3JOyDHGVLPkecNq9jT5b5PVXntXQ14EGa8Uxzz9vER6Ml3s1T3ZB7x/QG5IzWe"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.绘制 [文本内容]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="高级选项" tabindex="-1"><a class="header-anchor" href="#高级选项"><span>高级选项</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.绘制 [文本内容] -n [表情包ID] -x [水平位置] -y [垂直位置] -r [旋转角度] -s [字体大小] -c [启用文本曲线] -l [行间距]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
<table>
<thead>
<tr>
<th>参数</th>
<th>简写</th>
<th>类型</th>
<th>必填</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>文本内容</td>
<td>-</td>
<td>文本</td>
<td>是</td>
<td>要添加到表情包中的文本，使用 / 可以换行</td>
<td>你好/世界</td>
</tr>
<tr>
<td>表情包ID</td>
<td>-n</td>
<td>数字</td>
<td>否</td>
<td>指定表情包ID，范围0-358</td>
<td>-n 6</td>
</tr>
<tr>
<td>水平位置</td>
<td>-x</td>
<td>数字</td>
<td>否</td>
<td>文本的水平位置，范围0-296</td>
<td>-x 50</td>
</tr>
<tr>
<td>垂直位置</td>
<td>-y</td>
<td>数字</td>
<td>否</td>
<td>文本的垂直位置，范围0-256</td>
<td>-y 100</td>
</tr>
<tr>
<td>旋转角度</td>
<td>-r</td>
<td>数字</td>
<td>否</td>
<td>文本的旋转角度，范围-10到10</td>
<td>-r 2</td>
</tr>
<tr>
<td>字体大小</td>
<td>-s</td>
<td>数字</td>
<td>否</td>
<td>文本字体大小，范围10-100</td>
<td>-s 30</td>
</tr>
<tr>
<td>文本曲线</td>
<td>-c</td>
<td>布尔</td>
<td>否</td>
<td>启用文本曲线效果</td>
<td>-c</td>
</tr>
<tr>
<td>行间距</td>
<td>-l</td>
<td>数字</td>
<td>否</td>
<td>文本上下行间距，范围18-100</td>
<td>-l 25</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本绘制" tabindex="-1"><a class="header-anchor" href="#基本绘制"><span>基本绘制</span></a></h3>
<h4 id="随机表情包绘制" tabindex="-1"><a class="header-anchor" href="#随机表情包绘制"><span>随机表情包绘制</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.绘制 你好世界</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
🎉 表情包绘制完成！</p>
<p>🔍 输入&quot;pjsk.调整&quot;获取调整指令<br>
或直接输入&quot;pjsk.列表.角色分类&quot;开始新的绘制</p>
<p>✨ 期待您的下一个创作！</p>
</chat-message>
</chat-panel>
<h4 id="指定表情包绘制" tabindex="-1"><a class="header-anchor" href="#指定表情包绘制"><span>指定表情包绘制</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.绘制 -n 10 今天天气真好</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
🎉 表情包绘制完成！</p>
<p>🔍 输入&quot;pjsk.调整&quot;获取调整指令<br>
或直接输入&quot;pjsk.列表.角色分类&quot;开始新的绘制</p>
<p>✨ 期待您的下一个创作！</p>
</chat-message>
</chat-panel>
<h3 id="多行文本绘制" tabindex="-1"><a class="header-anchor" href="#多行文本绘制"><span>多行文本绘制</span></a></h3>
<h4 id="使用换行符" tabindex="-1"><a class="header-anchor" href="#使用换行符"><span>使用换行符</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.绘制 第一行/第二行/第三行</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
🎉 表情包绘制完成！</p>
<p>🔍 输入&quot;pjsk.调整&quot;获取调整指令<br>
或直接输入&quot;pjsk.列表.角色分类&quot;开始新的绘制</p>
<p>✨ 期待您的下一个创作！</p>
</chat-message>
</chat-panel>
<h3 id="高级效果绘制" tabindex="-1"><a class="header-anchor" href="#高级效果绘制"><span>高级效果绘制</span></a></h3>
<h4 id="启用文本曲线" tabindex="-1"><a class="header-anchor" href="#启用文本曲线"><span>启用文本曲线</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.绘制 -c 弧形文字效果</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk4.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
🎉 表情包绘制完成！</p>
<p>🔍 输入&quot;pjsk.调整&quot;获取调整指令<br>
或直接输入&quot;pjsk.列表.角色分类&quot;开始新的绘制</p>
<p>✨ 期待您的下一个创作！</p>
</chat-message>
</chat-panel>
<h4 id="自定义位置和大小" tabindex="-1"><a class="header-anchor" href="#自定义位置和大小"><span>自定义位置和大小</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.绘制 -x 100 -y 150 -s 25 -r 1 自定义位置</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk5.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
🎉 表情包绘制完成！</p>
<p>🔍 输入&quot;pjsk.调整&quot;获取调整指令<br>
或直接输入&quot;pjsk.列表.角色分类&quot;开始新的绘制</p>
<p>✨ 期待您的下一个创作！</p>
</chat-message>
</chat-panel>
<h2 id="角色列表管理" tabindex="-1"><a class="header-anchor" href="#角色列表管理"><span>角色列表管理</span></a></h2>
<h3 id="查看全部表情包列表" tabindex="-1"><a class="header-anchor" href="#查看全部表情包列表"><span>查看全部表情包列表</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.列表.全部</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="查看角色分类列表" tabindex="-1"><a class="header-anchor" href="#查看角色分类列表"><span>查看角色分类列表</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.列表.角色分类</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="查看指定角色列表" tabindex="-1"><a class="header-anchor" href="#查看指定角色列表"><span>查看指定角色列表</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.列表.展开指定角色 [角色序号或角色名]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="角色列表示例" tabindex="-1"><a class="header-anchor" href="#角色列表示例"><span>角色列表示例</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">pjsk.列表.角色分类</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/pjsk6.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p>~<br>
查看指定角色的表情，请输入：</p>
<blockquote>
<p>角色序号，例如：10<br>
角色名，例如：Emu</p>
</blockquote>
</chat-message>
</chat-panel>
<h2 id="表情包调整功能" tabindex="-1"><a class="header-anchor" href="#表情包调整功能"><span>表情包调整功能</span></a></h2>
<h3 id="文本内容调整" tabindex="-1"><a class="header-anchor" href="#文本内容调整"><span>文本内容调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.文本 [新文本内容]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="字体大小调整" tabindex="-1"><a class="header-anchor" href="#字体大小调整"><span>字体大小调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.字体.大</span></span>
<span class="line"><span>pjsk.调整.字体.小</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="行间距调整" tabindex="-1"><a class="header-anchor" href="#行间距调整"><span>行间距调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.行间距.大</span></span>
<span class="line"><span>pjsk.调整.行间距.小</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="文本曲线调整" tabindex="-1"><a class="header-anchor" href="#文本曲线调整"><span>文本曲线调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.文本曲线.开启</span></span>
<span class="line"><span>pjsk.调整.文本曲线.关闭</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="文本位置调整" tabindex="-1"><a class="header-anchor" href="#文本位置调整"><span>文本位置调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.位置.上</span></span>
<span class="line"><span>pjsk.调整.位置.下</span></span>
<span class="line"><span>pjsk.调整.位置.左</span></span>
<span class="line"><span>pjsk.调整.位置.右</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="角色调整" tabindex="-1"><a class="header-anchor" href="#角色调整"><span>角色调整</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>pjsk.调整.角色 [角色ID]</span></span>
<span class="line"><span>pjsk.调整.角色 -r  # 随机角色</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="渲染引擎" tabindex="-1"><a class="header-anchor" href="#渲染引擎"><span>渲染引擎</span></a></h3>
<ul>
<li><strong>基于Puppeteer</strong>: 使用Headless Chrome进行高质量渲染</li>
<li><strong>Canvas绘制</strong>: 基于HTML5 Canvas实现精确的文本渲染</li>
<li><strong>字体支持</strong>: 支持YurukaStd和SSFangTangTi字体</li>
</ul>
<h3 id="自适应功能" tabindex="-1"><a class="header-anchor" href="#自适应功能"><span>自适应功能</span></a></h3>
<ul>
<li><strong>文本大小自适应</strong>: 根据文本长度自动调整字体大小</li>
<li><strong>位置自适应</strong>: 智能调整文本位置以适应不同表情包</li>
<li><strong>多语言支持</strong>: 支持中英文混合文本处理</li>
</ul>
<h3 id="图像处理" tabindex="-1"><a class="header-anchor" href="#图像处理"><span>图像处理</span></a></h3>
<ul>
<li><strong>高质量输出</strong>: 296x256像素标准尺寸</li>
<li><strong>透明背景</strong>: 支持透明PNG格式输出</li>
<li><strong>颜色管理</strong>: 支持自定义文本颜色</li>
</ul>
<h2 id="支持的字符" tabindex="-1"><a class="header-anchor" href="#支持的字符"><span>支持的字符</span></a></h2>
<h3 id="角色列表" tabindex="-1"><a class="header-anchor" href="#角色列表"><span>角色列表</span></a></h3>
<ul>
<li>Airi, Akito, An, Emu, Ena, Haruka, Honami, Ichika</li>
<li>KAITO, Kanade, Kohane, Len, Luka, Mafuyu, Meiko</li>
<li>Miku, Minori, Mizuki, Nene, Rin, Rui, Saki</li>
<li>Shiho, Shizuku, Touya, Tsukasa</li>
</ul>
<h3 id="文本特性" tabindex="-1"><a class="header-anchor" href="#文本特性"><span>文本特性</span></a></h3>
<ul>
<li><strong>中文字符</strong>: 完整支持简体中文</li>
<li><strong>英文字符</strong>: 支持大小写英文字母</li>
<li><strong>特殊符号</strong>: 支持常用标点符号</li>
<li><strong>换行支持</strong>: 使用 <code v-pre>/</code> 或 <code v-pre>\n</code> 进行换行</li>
</ul>
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
<td>isTextSizeAdaptationEnabled</td>
<td>boolean</td>
<td>true</td>
<td>是否启用文本大小自适应</td>
</tr>
<tr>
<td>shouldSendDrawingGuideText</td>
<td>boolean</td>
<td>true</td>
<td>是否发送绘制引导文本</td>
</tr>
<tr>
<td>shouldSendSuccessMessageAfterDrawingEmoji</td>
<td>boolean</td>
<td>true</td>
<td>是否发送绘制成功提示</td>
</tr>
<tr>
<td>shouldMentionUserInMessage</td>
<td>boolean</td>
<td>false</td>
<td>是否在消息中@用户</td>
</tr>
<tr>
<td>retractDelay</td>
<td>number</td>
<td>0</td>
<td>自动撤回等待时间（秒）</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>表情包ID范围</strong>: 有效表情包ID范围为0-358</li>
<li><strong>文本长度限制</strong>: 单行建议不超过15个字符</li>
<li><strong>换行限制</strong>: 建议不超过3行文本</li>
<li><strong>性能考虑</strong>: 复杂渲染可能需要较长时间</li>
<li><strong>字体兼容性</strong>: 确保字体文件正确安装</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>啤酒烧烤表情包生成功能基于初音未来Project Sekai角色库，提供高质量的表情包生成体验。该功能支持丰富的自定义选项，适合制作个性化的社交表情包。</p>
</div>
</div></template>


