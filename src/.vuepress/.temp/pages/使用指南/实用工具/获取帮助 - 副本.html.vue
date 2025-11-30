<template><div><h1 id="获取帮助" tabindex="-1"><a class="header-anchor" href="#获取帮助"><span>获取帮助</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 帮助</p>
<p><strong>功能描述</strong>: 获取帮助</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJyNks9vEkEUx+/8FZPe0fRumlA8kNCwuw2cNh6WMnbXlN3NsqjHNmpDRGwtmPiDYCloUepCPGADjf4vhp1Z/wtnZ6bAwNr0HWBn3me+b+a978M968mOrjku2NqOARI5FTd6qPLzAV3Rn1I5v+totg62DLP8lG4J2wmgKorvnZFTuD9gB69DUUhuvgXNQmxVIGMV4KMSUMP/O+Rju2y6RhGKSjN6k4CavaO5qFnzX7ZFKowMz4sZobQgmARq2jJKuoHah6g1WhVM8/xqJiGpWkGzXejELRPmraWaYUhZVYd7dtwoartLTwpDllW7bNvQhdBZvfDNfbsPVFy9wP1qUnesIozqRzKlsuS9vLOBLn+gT3X/6i2qvxZnItTIgXh8g0yOLhSFrMDanzenAI0q6GBwdzquTiejNQplKJPhSBtIJty0XPB4fd2vHQWex6j03Etpjp4BBgTnHdQ6ZlhCokhC4kwHsFLTq9O/+yeLUtcqXRAMnxG/zhuMjk5ml5OyFJaynP4Mgt8N/2MLT96zeUZJfuGSs6EsKsoyZWWZw+dEsYl7VXaEMckUZZIpzvR4VdZ8PKmjVjNa7ett7vdtBoVCBJ2/PfrVfYCa+3hS8bvP8fGh771CFd5vUfgCTC8/EP8wLnoi34Ffr/njhj88CDovolS8/1iAGUVwy4CLMVsxbNl0Q4De/cLd8WLbcrF/L3md3Q=="></Mermaid><div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>由于某些环境下流程图可能无法正常渲染<br>
我们提供了图片版本作为备选显示方式</p>
</div>
<figure><img src="@source/使用指南/实用工具/获取帮助_架构图.png" alt="架构图" tabindex="0" loading="lazy"><figcaption>架构图</figcaption></figure>
<h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
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
<span style="color: #7d8faaff;">
    <a href="./获取帮助_帮助图.png" target="_blank">[图片]</a>
</span>
</chat-message>
</chat-panel>
<h4 id="获取指定指令帮助信息-帮助" tabindex="-1"><a class="header-anchor" href="#获取指定指令帮助信息-帮助"><span>获取指定指令帮助信息 <code v-pre>帮助</code></span></a></h4>
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
<h4 id="获取指定指令帮助信息-帮助-h" tabindex="-1"><a class="header-anchor" href="#获取指定指令帮助信息-帮助-h"><span>获取指定指令帮助信息 <code v-pre>帮助</code> <code v-pre>-h</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">帮助 -h</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/获取帮助_帮助的帮助图.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel></div></template>


