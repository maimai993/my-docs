<template><div><h1 id="图片处理工具" tabindex="-1"><a class="header-anchor" href="#图片处理工具"><span>图片处理工具</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>插件名称</strong>: patina</p>
<p><strong>功能描述</strong>: 提供多种图片处理功能，包括幻影坦克、光棱坦克、原图坦克、像素化和相机镜框滤镜</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1k8tu2kAUhvc8xVH2tMoLVCJI3hCBHQEbq4sJDMFVY1tg0i4bpUWoFSIJLNomQuHSQpsW2JRG5PYukWfsvEWMZ+IwmMzC9sz/zX/OnDkuvDXe5YqoZMHmVgS8kVGd1pDW/r/2Z/6jXNneKSGzCJuaXnnvLwnLMVAVhYy63i7nfMw2Pg5F8bSnJaznI2GDpJHHb8qgzt8vvI+tim5pu1h0CugND0RmDln0tE4+d0RqPpJcFxUhtGAYBzVhaOWiRjtV2p6GDRNcDyuxlIryyLRwKWroeNtYijkfclo1kaXpaIUkq2bFNLGFcSmsSpJaKOyaeCcsxbNqDul7qBw+4vJ3cOwMRKOvvPvwJ4rizWDt7ugM6LRG98cv7dkX+3K65kNJn0lypAMpHW8YFuytr5N6wx2NGJV46pAER7vAAHfQo+1DhsVSPhJLcaYHLJR9dXb/4XjR6tGlD+7kYN6FjeMgJTntI3KaMz/Avr71mKB+HJNF7CfHWCEZI0kiM+AMqyhj4lnGyJwZAv3XcAc18m1Im3X7+lTISpI49gvcQfW+e0T6H53DqsDEs5z5DeTkhhw0VjBBSufg3rbISZsxzmWTtnlEsVJ/wL747v0Di17L9f4LpFknsxaZ7Lu9T6tcRs9cMGsDoRfG3Iw1DcOWW2oC9OuN058tpp2JPACa/HLc"></Mermaid><h2 id="幻影坦克" tabindex="-1"><a class="header-anchor" href="#幻影坦克"><span>幻影坦克</span></a></h2>
<h3 id="概述-1" tabindex="-1"><a class="header-anchor" href="#概述-1"><span>概述</span></a></h3>
<p>幻影坦克是一种特殊的图片隐写技术，通过两张图片的混合，实现在不同亮度下显示不同图片的效果。</p>
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
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="基本使用" tabindex="-1"><a class="header-anchor" href="#基本使用"><span>基本使用</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片作为【表图】：
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片作为【里图】：
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
[处理后的幻影坦克图片]
</chat-message>
</chat-panel>
<h4 id="使用qq头像" tabindex="-1"><a class="header-anchor" href="#使用qq头像"><span>使用QQ头像</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 123456 654321</chat-message>
<chat-message nickname="bot" type="bot">
[使用两个QQ号头像生成的幻影坦克图片]
</chat-message>
</chat-panel>
<h4 id="使用选项参数" tabindex="-1"><a class="header-anchor" href="#使用选项参数"><span>使用选项参数</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">幻影 [图片] [图片] -f -s 800 -w 0.5</chat-message>
<chat-message nickname="bot" type="bot">
[全彩输出、尺寸800、权重0.5的幻影坦克图片]
</chat-message>
</chat-panel>
<h2 id="像素化" tabindex="-1"><a class="header-anchor" href="#像素化"><span>像素化</span></a></h2>
<h3 id="概述-2" tabindex="-1"><a class="header-anchor" href="#概述-2"><span>概述</span></a></h3>
<p>将图片进行像素化处理，可以调整像素化程度来获得不同的艺术效果。</p>
<h3 id="基本语法-1" tabindex="-1"><a class="header-anchor" href="#基本语法-1"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>像素化 [图片]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="参数说明-1" tabindex="-1"><a class="header-anchor" href="#参数说明-1"><span>参数说明</span></a></h3>
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
<td>图片</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>要像素化的图片</td>
<td>[图片] / 123456 / @用户</td>
</tr>
</tbody>
</table>
<h3 id="选项说明-1" tabindex="-1"><a class="header-anchor" href="#选项说明-1"><span>选项说明</span></a></h3>
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
<td>pixelate</td>
<td>-p</td>
<td>number</td>
<td>像素化百分比，越高越抽象</td>
<td>80</td>
</tr>
</tbody>
</table>
<h3 id="使用示例-1" tabindex="-1"><a class="header-anchor" href="#使用示例-1"><span>使用示例</span></a></h3>
<h4 id="基本使用-1" tabindex="-1"><a class="header-anchor" href="#基本使用-1"><span>基本使用</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">像素化</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片：
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
[像素化后的图片]
</chat-message>
</chat-panel>
<h4 id="使用qq头像-1" tabindex="-1"><a class="header-anchor" href="#使用qq头像-1"><span>使用QQ头像</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 123456</chat-message>
<chat-message nickname="bot" type="bot">
[像素化后的QQ头像]
</chat-message>
</chat-panel>
<h4 id="调整像素化程度" tabindex="-1"><a class="header-anchor" href="#调整像素化程度"><span>调整像素化程度</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">像素化 [图片] -p 50</chat-message>
<chat-message nickname="bot" type="bot">
[50%像素化程度的图片]
</chat-message>
</chat-panel>
<h2 id="相机镜框滤镜" tabindex="-1"><a class="header-anchor" href="#相机镜框滤镜"><span>相机镜框滤镜</span></a></h2>
<h3 id="概述-3" tabindex="-1"><a class="header-anchor" href="#概述-3"><span>概述</span></a></h3>
<p>为图片添加相机镜框效果，模拟相机取景器的外观。</p>
<h3 id="基本语法-2" tabindex="-1"><a class="header-anchor" href="#基本语法-2"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>相机镜框 [图片]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="参数说明-2" tabindex="-1"><a class="header-anchor" href="#参数说明-2"><span>参数说明</span></a></h3>
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
<td>图片</td>
<td>图片/QQ号/@用户</td>
<td>否</td>
<td>要添加镜框的图片</td>
<td>[图片] / 123456 / @用户</td>
</tr>
</tbody>
</table>
<h3 id="使用示例-2" tabindex="-1"><a class="header-anchor" href="#使用示例-2"><span>使用示例</span></a></h3>
<h4 id="基本使用-2" tabindex="-1"><a class="header-anchor" href="#基本使用-2"><span>基本使用</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">相机镜框</chat-message>
<chat-message nickname="bot" type="bot">
请发送一张图片：
</chat-message>
<chat-message nickname="用户" type="user">[图片]</chat-message>
<chat-message nickname="bot" type="bot">
[添加相机镜框后的图片]
</chat-message>
</chat-panel>
<h4 id="使用qq头像-2" tabindex="-1"><a class="header-anchor" href="#使用qq头像-2"><span>使用QQ头像</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">相机镜框 @用户</chat-message>
<chat-message nickname="bot" type="bot">
[添加相机镜框的用户头像]
</chat-message>
</div></template>


