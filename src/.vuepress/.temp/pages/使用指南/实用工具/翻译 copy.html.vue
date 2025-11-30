<template><div><h1 id="翻译" tabindex="-1"><a class="header-anchor" href="#翻译"><span>翻译</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 翻译</p>
<p><strong>功能描述</strong>: 中英互译</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl7ABDyWtCmBU+OhQJUaaElb1KNEJURDQOBglDR8KagJcEIDRt/FtNv6Fm4/+GjBObQ7M7/9z+zsHmXFs1SGlRSIxgKALcEYzSEqvx/anv2RC8ljic1nIMoLhXM75AmHgaFpfdTFu4y3sbNxYTSNc6sQJ6QDmwKkmOZOZGCs/y5exAqCwuc4r9KSjmCQzadYBbUq+k3HS1lGunlvxlPaI3gADCHycoZHnRJSp5uChJvfzIQphk2zeYWTgqLAJUVfTcuoOCPncridoCKxgpxlFd/BrMb862WzCQgG9/EUbYemsQc7P3dtQNMyKo73tNmtNp/u2BBpM6SLdIASuIiowGkopFeq5mjkUMTqXgkX7YIDmIMeUmsOFqZsJEy5TA+cUtpn+/eivi61UOmDObm03k61vmyJitsIFXeZJzC/m/qjaswbSG1tU3kG7eMB36revzJqpe29DEBvVPRZU58Uzd71NpXhP4d3RuSZ04sr5gzUwfzjfgV0/2X0Z+ttJwJ/QH8MHw=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>翻译 &#x3C;文本></span></span></code></pre>
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
<td>文本</td>
<td>文本</td>
<td>否</td>
<td>要翻译的文本</td>
<td>麦芽糖</td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="翻译-麦芽糖" tabindex="-1"><a class="header-anchor" href="#翻译-麦芽糖"><span>翻译 <code v-pre>麦芽糖</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[中文] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="翻译-maltose" tabindex="-1"><a class="header-anchor" href="#翻译-maltose"><span>翻译 <code v-pre>maltose</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[英语] =&gt; [中文]</p>
</chat-message>
</chat-panel>
<h3 id="翻译方向对照表" tabindex="-1"><a class="header-anchor" href="#翻译方向对照表"><span>翻译方向对照表</span></a></h3>
<table>
<thead>
<tr>
<th style="text-align:left">源语言</th>
<th style="text-align:left">目标语言</th>
<th style="text-align:left">源语言</th>
<th style="text-align:left">目标语言</th>
<th style="text-align:left">源语言</th>
<th style="text-align:left">目标语言</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">德</td>
<td style="text-align:left">法</td>
<td style="text-align:left">德</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">法</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">法</td>
<td style="text-align:left">法</td>
<td style="text-align:left">俄</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">法</td>
<td style="text-align:left">繁</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">法</td>
<td style="text-align:left">韩</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">法</td>
<td style="text-align:left">葡</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">日</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">日</td>
<td style="text-align:left">法</td>
<td style="text-align:left">日</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">法</td>
<td style="text-align:left">泰</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">言</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">言</td>
<td style="text-align:left">法</td>
<td style="text-align:left">言</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">英</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">英</td>
<td style="text-align:left">法</td>
<td style="text-align:left">英</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">法</td>
<td style="text-align:left">粤</td>
</tr>
<tr>
<td style="text-align:left">德</td>
<td style="text-align:left">中</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">中</td>
<td style="text-align:left">法</td>
<td style="text-align:left">中</td>
</tr>
<tr>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">德</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">德</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">德</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">俄</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">法</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">法</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">法</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">繁</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">韩</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">日</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">日</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">日</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">泰</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">言</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">言</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">言</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">英</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">英</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">英</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">粤</td>
</tr>
<tr>
<td style="text-align:left">繁</td>
<td style="text-align:left">中</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">中</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">中</td>
</tr>
<tr>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">德</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">德</td>
<td style="text-align:left">言</td>
<td style="text-align:left">德</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">言</td>
<td style="text-align:left">俄</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">法</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">法</td>
<td style="text-align:left">言</td>
<td style="text-align:left">法</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">言</td>
<td style="text-align:left">繁</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">言</td>
<td style="text-align:left">韩</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">言</td>
<td style="text-align:left">葡</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">日</td>
<td style="text-align:left">言</td>
<td style="text-align:left">日</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">言</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">言</td>
<td style="text-align:left">言</td>
<td style="text-align:left">泰</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">英</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">英</td>
<td style="text-align:left">言</td>
<td style="text-align:left">英</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">言</td>
<td style="text-align:left">粤</td>
</tr>
<tr>
<td style="text-align:left">日</td>
<td style="text-align:left">中</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">中</td>
<td style="text-align:left">言</td>
<td style="text-align:left">中</td>
</tr>
<tr>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
<td style="text-align:left"><strong>源语言</strong></td>
<td style="text-align:left"><strong>目标语言</strong></td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">德</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">德</td>
<td style="text-align:left">中</td>
<td style="text-align:left">德</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">俄</td>
<td style="text-align:left">中</td>
<td style="text-align:left">俄</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">法</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">法</td>
<td style="text-align:left">中</td>
<td style="text-align:left">法</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">繁</td>
<td style="text-align:left">中</td>
<td style="text-align:left">繁</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">韩</td>
<td style="text-align:left">中</td>
<td style="text-align:left">韩</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">葡</td>
<td style="text-align:left">中</td>
<td style="text-align:left">葡</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">日</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">日</td>
<td style="text-align:left">中</td>
<td style="text-align:left">日</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">泰</td>
<td style="text-align:left">中</td>
<td style="text-align:left">泰</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">言</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">言</td>
<td style="text-align:left">中</td>
<td style="text-align:left">言</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">英</td>
<td style="text-align:left">中</td>
<td style="text-align:left">英</td>
</tr>
<tr>
<td style="text-align:left">英</td>
<td style="text-align:left">中</td>
<td style="text-align:left">粤</td>
<td style="text-align:left">中</td>
<td style="text-align:left">中</td>
<td style="text-align:left">粤</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<ul>
<li>&quot;繁&quot; 指繁体中文</li>
<li>&quot;言&quot; 指文言文</li>
<li>表格展示了所有110种双向翻译组合</li>
</ul>
</div>
<h4 id="德译俄" tabindex="-1"><a class="header-anchor" href="#德译俄"><span>德译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[德语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="德译法" tabindex="-1"><a class="header-anchor" href="#德译法"><span>德译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[德语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="德译繁" tabindex="-1"><a class="header-anchor" href="#德译繁"><span>德译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[德语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="德译韩" tabindex="-1"><a class="header-anchor" href="#德译韩"><span>德译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[德语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="德译葡" tabindex="-1"><a class="header-anchor" href="#德译葡"><span>德译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[德语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="德译日" tabindex="-1"><a class="header-anchor" href="#德译日"><span>德译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[德语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="德译泰" tabindex="-1"><a class="header-anchor" href="#德译泰"><span>德译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[德语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="德译言" tabindex="-1"><a class="header-anchor" href="#德译言"><span>德译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[德语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="德译英" tabindex="-1"><a class="header-anchor" href="#德译英"><span>德译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[德语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="德译粤" tabindex="-1"><a class="header-anchor" href="#德译粤"><span>德译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[德语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="德译中" tabindex="-1"><a class="header-anchor" href="#德译中"><span>德译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[德语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="俄译德" tabindex="-1"><a class="header-anchor" href="#俄译德"><span>俄译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[俄语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译法" tabindex="-1"><a class="header-anchor" href="#俄译法"><span>俄译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[俄语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译繁" tabindex="-1"><a class="header-anchor" href="#俄译繁"><span>俄译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[俄语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="俄译韩" tabindex="-1"><a class="header-anchor" href="#俄译韩"><span>俄译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[俄语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译葡" tabindex="-1"><a class="header-anchor" href="#俄译葡"><span>俄译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[俄语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译日" tabindex="-1"><a class="header-anchor" href="#俄译日"><span>俄译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[俄语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译泰" tabindex="-1"><a class="header-anchor" href="#俄译泰"><span>俄译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[俄语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译言" tabindex="-1"><a class="header-anchor" href="#俄译言"><span>俄译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[俄语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="俄译英" tabindex="-1"><a class="header-anchor" href="#俄译英"><span>俄译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[俄语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译粤" tabindex="-1"><a class="header-anchor" href="#俄译粤"><span>俄译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[俄语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="俄译中" tabindex="-1"><a class="header-anchor" href="#俄译中"><span>俄译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Мальтоза</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[俄语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="法译德" tabindex="-1"><a class="header-anchor" href="#法译德"><span>法译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[法语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="法译俄" tabindex="-1"><a class="header-anchor" href="#法译俄"><span>法译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[法语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="法译繁" tabindex="-1"><a class="header-anchor" href="#法译繁"><span>法译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[法语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="法译韩" tabindex="-1"><a class="header-anchor" href="#法译韩"><span>法译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[法语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="法译葡" tabindex="-1"><a class="header-anchor" href="#法译葡"><span>法译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[法语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="法译日" tabindex="-1"><a class="header-anchor" href="#法译日"><span>法译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[法语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="法译泰" tabindex="-1"><a class="header-anchor" href="#法译泰"><span>法译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[法语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="法译言" tabindex="-1"><a class="header-anchor" href="#法译言"><span>法译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[法语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="法译英" tabindex="-1"><a class="header-anchor" href="#法译英"><span>法译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[法语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="法译粤" tabindex="-1"><a class="header-anchor" href="#法译粤"><span>法译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[法语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="法译中" tabindex="-1"><a class="header-anchor" href="#法译中"><span>法译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[法语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="繁译德" tabindex="-1"><a class="header-anchor" href="#繁译德"><span>繁译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[繁体中文] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译俄" tabindex="-1"><a class="header-anchor" href="#繁译俄"><span>繁译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[繁体中文] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译法" tabindex="-1"><a class="header-anchor" href="#繁译法"><span>繁译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[繁体中文] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译韩" tabindex="-1"><a class="header-anchor" href="#繁译韩"><span>繁译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[繁体中文] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译葡" tabindex="-1"><a class="header-anchor" href="#繁译葡"><span>繁译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[繁体中文] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译日" tabindex="-1"><a class="header-anchor" href="#繁译日"><span>繁译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[繁体中文] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译泰" tabindex="-1"><a class="header-anchor" href="#繁译泰"><span>繁译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[繁体中文] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译言" tabindex="-1"><a class="header-anchor" href="#繁译言"><span>繁译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[繁体中文] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="繁译英" tabindex="-1"><a class="header-anchor" href="#繁译英"><span>繁译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[繁体中文] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译粤" tabindex="-1"><a class="header-anchor" href="#繁译粤"><span>繁译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[繁体中文] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="繁译中" tabindex="-1"><a class="header-anchor" href="#繁译中"><span>繁译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[繁体中文] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="韩译德" tabindex="-1"><a class="header-anchor" href="#韩译德"><span>韩译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[韩语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译俄" tabindex="-1"><a class="header-anchor" href="#韩译俄"><span>韩译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[韩语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译法" tabindex="-1"><a class="header-anchor" href="#韩译法"><span>韩译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[韩语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译繁" tabindex="-1"><a class="header-anchor" href="#韩译繁"><span>韩译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[韩语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="韩译葡" tabindex="-1"><a class="header-anchor" href="#韩译葡"><span>韩译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[韩语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译日" tabindex="-1"><a class="header-anchor" href="#韩译日"><span>韩译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[韩语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译泰" tabindex="-1"><a class="header-anchor" href="#韩译泰"><span>韩译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[韩语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译言" tabindex="-1"><a class="header-anchor" href="#韩译言"><span>韩译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[韩语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="韩译英" tabindex="-1"><a class="header-anchor" href="#韩译英"><span>韩译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[韩语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译粤" tabindex="-1"><a class="header-anchor" href="#韩译粤"><span>韩译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[韩语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="韩译中" tabindex="-1"><a class="header-anchor" href="#韩译中"><span>韩译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 말토스</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[韩语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="葡译德" tabindex="-1"><a class="header-anchor" href="#葡译德"><span>葡译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[葡萄牙语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译俄" tabindex="-1"><a class="header-anchor" href="#葡译俄"><span>葡译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[葡萄牙语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译法" tabindex="-1"><a class="header-anchor" href="#葡译法"><span>葡译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[葡萄牙语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译繁" tabindex="-1"><a class="header-anchor" href="#葡译繁"><span>葡译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[葡萄牙语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="葡译韩" tabindex="-1"><a class="header-anchor" href="#葡译韩"><span>葡译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[葡萄牙语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译日" tabindex="-1"><a class="header-anchor" href="#葡译日"><span>葡译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[葡萄牙语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译泰" tabindex="-1"><a class="header-anchor" href="#葡译泰"><span>葡译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[葡萄牙语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译言" tabindex="-1"><a class="header-anchor" href="#葡译言"><span>葡译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[葡萄牙语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="葡译英" tabindex="-1"><a class="header-anchor" href="#葡译英"><span>葡译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[葡萄牙语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译粤" tabindex="-1"><a class="header-anchor" href="#葡译粤"><span>葡译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[葡萄牙语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="葡译中" tabindex="-1"><a class="header-anchor" href="#葡译中"><span>葡译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[葡萄牙语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="日译德" tabindex="-1"><a class="header-anchor" href="#日译德"><span>日译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[日语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="日译俄" tabindex="-1"><a class="header-anchor" href="#日译俄"><span>日译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[日语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="日译法" tabindex="-1"><a class="header-anchor" href="#日译法"><span>日译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[日语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="日译繁" tabindex="-1"><a class="header-anchor" href="#日译繁"><span>日译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[日语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="日译韩" tabindex="-1"><a class="header-anchor" href="#日译韩"><span>日译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[日语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="日译葡" tabindex="-1"><a class="header-anchor" href="#日译葡"><span>日译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[日语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="日译泰" tabindex="-1"><a class="header-anchor" href="#日译泰"><span>日译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[日语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="日译言" tabindex="-1"><a class="header-anchor" href="#日译言"><span>日译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[日语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="日译英" tabindex="-1"><a class="header-anchor" href="#日译英"><span>日译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[日语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="日译粤" tabindex="-1"><a class="header-anchor" href="#日译粤"><span>日译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[日语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="日译中" tabindex="-1"><a class="header-anchor" href="#日译中"><span>日译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 マルトース</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[日语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="泰译德" tabindex="-1"><a class="header-anchor" href="#泰译德"><span>泰译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[泰语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译俄" tabindex="-1"><a class="header-anchor" href="#泰译俄"><span>泰译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[泰语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译法" tabindex="-1"><a class="header-anchor" href="#泰译法"><span>泰译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[泰语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译繁" tabindex="-1"><a class="header-anchor" href="#泰译繁"><span>泰译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[泰语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="泰译韩" tabindex="-1"><a class="header-anchor" href="#泰译韩"><span>泰译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[泰语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译葡" tabindex="-1"><a class="header-anchor" href="#泰译葡"><span>泰译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[泰语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译日" tabindex="-1"><a class="header-anchor" href="#泰译日"><span>泰译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[泰语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译言" tabindex="-1"><a class="header-anchor" href="#泰译言"><span>泰译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[泰语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="泰译英" tabindex="-1"><a class="header-anchor" href="#泰译英"><span>泰译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[泰语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译粤" tabindex="-1"><a class="header-anchor" href="#泰译粤"><span>泰译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[泰语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="泰译中" tabindex="-1"><a class="header-anchor" href="#泰译中"><span>泰译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 มอลโทส</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[泰语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="言译德" tabindex="-1"><a class="header-anchor" href="#言译德"><span>言译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[文言文] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="言译俄" tabindex="-1"><a class="header-anchor" href="#言译俄"><span>言译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[文言文] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="言译法" tabindex="-1"><a class="header-anchor" href="#言译法"><span>言译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[文言文] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="言译繁" tabindex="-1"><a class="header-anchor" href="#言译繁"><span>言译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[文言文] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="言译韩" tabindex="-1"><a class="header-anchor" href="#言译韩"><span>言译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[文言文] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="言译葡" tabindex="-1"><a class="header-anchor" href="#言译葡"><span>言译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[文言文] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="言译日" tabindex="-1"><a class="header-anchor" href="#言译日"><span>言译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[文言文] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="言译泰" tabindex="-1"><a class="header-anchor" href="#言译泰"><span>言译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[文言文] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="言译英" tabindex="-1"><a class="header-anchor" href="#言译英"><span>言译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[文言文] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="言译粤" tabindex="-1"><a class="header-anchor" href="#言译粤"><span>言译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[文言文] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="言译中" tabindex="-1"><a class="header-anchor" href="#言译中"><span>言译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 睡觉</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[文言文] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="英译德" tabindex="-1"><a class="header-anchor" href="#英译德"><span>英译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[英语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="英译俄" tabindex="-1"><a class="header-anchor" href="#英译俄"><span>英译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[英语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="英译法" tabindex="-1"><a class="header-anchor" href="#英译法"><span>英译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[英语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="英译繁" tabindex="-1"><a class="header-anchor" href="#英译繁"><span>英译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[英语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="英译韩" tabindex="-1"><a class="header-anchor" href="#英译韩"><span>英译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[英语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="英译葡" tabindex="-1"><a class="header-anchor" href="#英译葡"><span>英译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[英语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="英译日" tabindex="-1"><a class="header-anchor" href="#英译日"><span>英译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[英语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="英译泰" tabindex="-1"><a class="header-anchor" href="#英译泰"><span>英译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[英语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="英译言" tabindex="-1"><a class="header-anchor" href="#英译言"><span>英译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[英语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="英译粤" tabindex="-1"><a class="header-anchor" href="#英译粤"><span>英译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[英语] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
<h4 id="英译中" tabindex="-1"><a class="header-anchor" href="#英译中"><span>英译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 maltose</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[英语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="粤译德" tabindex="-1"><a class="header-anchor" href="#粤译德"><span>粤译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[粤语] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译俄" tabindex="-1"><a class="header-anchor" href="#粤译俄"><span>粤译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[粤语] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译法" tabindex="-1"><a class="header-anchor" href="#粤译法"><span>粤译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[粤语] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译繁" tabindex="-1"><a class="header-anchor" href="#粤译繁"><span>粤译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[粤语] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="粤译韩" tabindex="-1"><a class="header-anchor" href="#粤译韩"><span>粤译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[粤语] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译葡" tabindex="-1"><a class="header-anchor" href="#粤译葡"><span>粤译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[粤语] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译日" tabindex="-1"><a class="header-anchor" href="#粤译日"><span>粤译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[粤语] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译泰" tabindex="-1"><a class="header-anchor" href="#粤译泰"><span>粤译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[粤语] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译言" tabindex="-1"><a class="header-anchor" href="#粤译言"><span>粤译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[粤语] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="粤译英" tabindex="-1"><a class="header-anchor" href="#粤译英"><span>粤译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[粤语] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="粤译中" tabindex="-1"><a class="header-anchor" href="#粤译中"><span>粤译中</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麥芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麦芽糖</p>
<p>[粤语] =&gt; [简体中文]</p>
</chat-message>
</chat-panel>
<h4 id="中译德" tabindex="-1"><a class="header-anchor" href="#中译德"><span>中译德</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Maltose</p>
<p>[简体中文] =&gt; [德语]</p>
</chat-message>
</chat-panel>
<h4 id="中译俄" tabindex="-1"><a class="header-anchor" href="#中译俄"><span>中译俄</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Мальтоза</p>
<p>[简体中文] =&gt; [俄语]</p>
</chat-message>
</chat-panel>
<h4 id="中译法" tabindex="-1"><a class="header-anchor" href="#中译法"><span>中译法</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[简体中文] =&gt; [法语]</p>
</chat-message>
</chat-panel>
<h4 id="中译繁" tabindex="-1"><a class="header-anchor" href="#中译繁"><span>中译繁</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[简体中文] =&gt; [繁体中文]</p>
</chat-message>
</chat-panel>
<h4 id="中译韩" tabindex="-1"><a class="header-anchor" href="#中译韩"><span>中译韩</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>말토스</p>
<p>[简体中文] =&gt; [韩语]</p>
</chat-message>
</chat-panel>
<h4 id="中译葡" tabindex="-1"><a class="header-anchor" href="#中译葡"><span>中译葡</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[简体中文] =&gt; [葡萄牙语]</p>
</chat-message>
</chat-panel>
<h4 id="中译日" tabindex="-1"><a class="header-anchor" href="#中译日"><span>中译日</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>マルトース</p>
<p>[简体中文] =&gt; [日语]</p>
</chat-message>
</chat-panel>
<h4 id="中译泰" tabindex="-1"><a class="header-anchor" href="#中译泰"><span>中译泰</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>มอลโทส</p>
<p>[简体中文] =&gt; [泰语]</p>
</chat-message>
</chat-panel>
<h4 id="中译言" tabindex="-1"><a class="header-anchor" href="#中译言"><span>中译言</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>寝。</p>
<p>[简体中文] =&gt; [文言文]</p>
</chat-message>
</chat-panel>
<h4 id="中译英" tabindex="-1"><a class="header-anchor" href="#中译英"><span>中译英</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>maltose</p>
<p>[简体中文] =&gt; [英语]</p>
</chat-message>
</chat-panel>
<h4 id="中译粤" tabindex="-1"><a class="header-anchor" href="#中译粤"><span>中译粤</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>麥芽糖</p>
<p>[简体中文] =&gt; [粤语]</p>
</chat-message>
</chat-panel>
</div></template>


