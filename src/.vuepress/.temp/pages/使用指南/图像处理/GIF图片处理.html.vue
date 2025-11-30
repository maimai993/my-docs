<template><div><h1 id="gif图片处理" tabindex="-1"><a class="header-anchor" href="#gif图片处理"><span>GIF图片处理</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: gif-reverse</p>
<p><strong>功能描述</strong>: 提供多种GIF图片处理功能，包括倒放、回弹、滑动、旋转、转向等效果</p>
<p><strong>插件名称</strong>: gif-reverse</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6ACZqUGAykJLhpXFQYoEZb0hZ0qfGuQVFZGDVELgpKAqzQgMF3Mcy0voVtp1za4lm0M3O++c9lTnJb2o2neVmFtagPDItxWrFBzj42rJ31UbKbKZnPpGFNELN71pHjOAAcy+JWxbilNdv04shY1vBNjpCY8HkFwlICbSnAmf95YxHNiqqwg5xKY3rZAPlMnFfJUx5flJ2UaWHb7/Q4QjsEV4ALSYKSFkj5hJS6XsGQ7fd6AhGOT/AZFcl+SUSbkiumacEolxKSfhnlkKy4ajKNYbhkcieDUl7XyjoX58Ucr3grca/H1cXA718y2m5tWNbYwdzPzTOQ7hk5aC8Me5fDfnfOgsIWE7aRMkREtCypkFtcxPlrvdWiVGgyCCEbrQAF9HqVlAoUC0QsJBCxmSrQUMOv59/922mpkUoN9M6hOWzXt+OUgnQIg1GbeQH8ONDOT3HtSCucUIZhLIZhbOYV9O8ifixRRuvfkdLTbLU6DD8fjJGZVnPn3QB8l8e9Iu4c6NXjWXm//dMo2k5HT99tMdp8irmfpgnkfqDVejQpXLjSHo6CqwyFY74/JgYsiA=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>gif-reverse [选项] [图片]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="选项说明" tabindex="-1"><a class="header-anchor" href="#选项说明"><span>选项说明</span></a></h3>
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
<td><code v-pre>--rebound</code></td>
<td><code v-pre>-b</code></td>
<td>无</td>
<td>回弹效果（正放+倒放）</td>
</tr>
<tr>
<td><code v-pre>--reverse</code></td>
<td><code v-pre>-r</code></td>
<td>无</td>
<td>倒放 GIF</td>
</tr>
<tr>
<td><code v-pre>--frame</code></td>
<td><code v-pre>-f</code></td>
<td>number</td>
<td>指定处理gif的帧间隔</td>
</tr>
<tr>
<td><code v-pre>--slide</code></td>
<td><code v-pre>-l</code></td>
<td>string</td>
<td>滑动方向 (上/下/左/右)</td>
</tr>
<tr>
<td><code v-pre>--rotate</code></td>
<td><code v-pre>-o</code></td>
<td>string</td>
<td>旋转方向 (顺/逆)</td>
</tr>
<tr>
<td><code v-pre>--turn</code></td>
<td><code v-pre>-t</code></td>
<td>string</td>
<td>转向角度 (上/下/左/右/左上/左下/右上/右下/0-360)</td>
</tr>
<tr>
<td><code v-pre>--shake</code></td>
<td><code v-pre>-s</code></td>
<td>无</td>
<td>上下震动效果</td>
</tr>
<tr>
<td><code v-pre>--information</code></td>
<td><code v-pre>-i</code></td>
<td>无</td>
<td>显示 GIF 信息</td>
</tr>
</tbody>
</table>
<h2 id="支持的图片格式" tabindex="-1"><a class="header-anchor" href="#支持的图片格式"><span>支持的图片格式</span></a></h2>
<ul>
<li><strong>GIF 图片</strong>: 支持所有效果</li>
<li><strong>静态图片</strong>: 支持滑动、旋转、转向效果，可将静态图转换为动态GIF
<ul>
<li>支持格式：JPEG、PNG、WebP</li>
<li>不支持：倒放、回弹效果</li>
</ul>
</li>
</ul>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="回弹效果" tabindex="-1"><a class="header-anchor" href="#回弹效果"><span>回弹效果</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -b</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/gif2.gif" alt="" loading="lazy"><br>
图片信息：<br>
文件大小：4636.02 KB<br>
图片尺寸：400x679<br>
帧数：58<br>
帧间隔：66.72 毫秒<br>
帧率：14.99 FPS<br>
总时长：3.87 秒</p>
</chat-message>
</chat-panel>
<h3 id="倒放gif" tabindex="-1"><a class="header-anchor" href="#倒放gif"><span>倒放GIF</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -r</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif3.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/gif4.gif" alt="" loading="lazy"><br>
图片信息：<br>
文件大小：1892.95 KB<br>
图片尺寸：240x240<br>
帧数：200<br>
帧间隔：30.00 毫秒<br>
帧率：33.33 FPS<br>
总时长：6.00 秒</p>
</chat-message>
</chat-panel>
<h3 id="右滑效果" tabindex="-1"><a class="header-anchor" href="#右滑效果"><span>右滑效果</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -l 右</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif5.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/gif6.gif" alt="" loading="lazy"><br>
图片信息：<br>
文件大小：1732.19 KB<br>
图片尺寸：400x400<br>
帧数：17<br>
帧间隔：50.00 毫秒<br>
帧率：20.00 FPS<br>
总时长：0.85 秒</p>
</chat-message>
</chat-panel>
<h3 id="顺时针旋转" tabindex="-1"><a class="header-anchor" href="#顺时针旋转"><span>顺时针旋转</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -o 顺</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif5.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/图像处理/gif7.gif" alt="" loading="lazy"><br>
图片信息：<br>
文件大小：1667.81 KB<br>
图片尺寸：400x400<br>
帧数：17<br>
帧间隔：50.00 毫秒<br>
帧率：20.00 FPS<br>
总时长：0.85 秒</p>
</chat-message>
</chat-panel>
<h3 id="转向30度" tabindex="-1"><a class="header-anchor" href="#转向30度"><span>转向30度</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -t 30</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif5.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/gif8.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="加速gif" tabindex="-1"><a class="header-anchor" href="#加速gif"><span>加速gif</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">gif-reverse -f 20</chat-message>
<recall-message nickname="bot" type="bot">在 50 秒内发送想要处理的图片</recall-message>
<chat-message nickname="用户" type="user">
<figure><img src="@source/使用指南/图像处理/gif5.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/gif9.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="处理原理" tabindex="-1"><a class="header-anchor" href="#处理原理"><span>处理原理</span></a></h3>
<ul>
<li><strong>FFmpeg处理</strong>: 使用FFmpeg进行GIF处理</li>
<li><strong>Canvas支持</strong>: 使用Canvas进行图片解析和操作</li>
<li><strong>动态效果</strong>: 支持将静态图片转为动态GIF</li>
</ul>
<h3 id="性能优化" tabindex="-1"><a class="header-anchor" href="#性能优化"><span>性能优化</span></a></h3>
<ul>
<li><strong>帧率限制</strong>: 限制输出GIF的最大帧率(默认50FPS)</li>
<li><strong>图片压缩</strong>: 自动优化处理后的GIF大小</li>
<li><strong>内存管理</strong>: 使用临时文件处理大文件</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li>
<p><strong>依赖要求</strong>:</p>
<ul>
<li>需要安装ffmpeg服务</li>
<li>需要安装canvas服务</li>
<li>需要http和logger服务</li>
</ul>
</li>
<li>
<p><strong>处理限制</strong>:</p>
<ul>
<li>静态图片不支持倒放和回弹效果</li>
<li>大尺寸GIF处理可能需要更长时间</li>
<li>复杂效果组合可能影响处理性能</li>
</ul>
</li>
<li>
<p><strong>输入要求</strong>:</p>
<ul>
<li>需要在指令后直接发送图片或引用包含图片的消息</li>
<li>支持GIF、JPEG、PNG和WebP格式</li>
</ul>
</li>
</ol>
</div></template>


