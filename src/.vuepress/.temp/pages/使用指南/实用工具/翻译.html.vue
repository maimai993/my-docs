<template><div><h1 id="翻译" tabindex="-1"><a class="header-anchor" href="#翻译"><span>翻译</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 翻译</p>
<p><strong>功能描述</strong>: 多语言翻译功能，支持110种语言双向翻译</p>
<p><strong>插件名称</strong>: smmcat-translate</p>
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
<h4 id="翻译长文本" tabindex="-1"><a class="header-anchor" href="#翻译长文本"><span>翻译长文本</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 Artificial intelligence is transforming the way we live and work, bringing unprecedented opportunities and challenges to our society.</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>人工智能正在改变我们的生活和工作方式，给我们的社会带来了前所未有的机遇和挑战。</p>
<p>[英语] =&gt; [中文]</p>
</chat-message>
</chat-panel>
<h4 id="翻译日语文本" tabindex="-1"><a class="header-anchor" href="#翻译日语文本"><span>翻译日语文本</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 こんにちは、世界</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>你好，世界</p>
<p>[日语] =&gt; [中文]</p>
</chat-message>
</chat-panel>
<h4 id="翻译文言文" tabindex="-1"><a class="header-anchor" href="#翻译文言文"><span>翻译文言文</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">翻译 学而时习之，不亦说乎</chat-message>
<chat-message nickname="bot" type="bot">
翻译的结果：
<p>Learn and practice from time to time, isn't it pleasant?</p>
<p>[文言文] =&gt; [英语]</p>
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
<h2 id="配置说明" tabindex="-1"><a class="header-anchor" href="#配置说明"><span>配置说明</span></a></h2>
<h3 id="插件配置" tabindex="-1"><a class="header-anchor" href="#插件配置"><span>插件配置</span></a></h3>
<p>在使用翻译功能前，需要在Koishi配置文件中添加百度翻译API的配置：</p>
<div class="language-typescript line-numbers-mode" data-highlighter="shiki" data-ext="typescript" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-typescript"><span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// koishi.config.ts</span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">export</span><span style="--shiki-light:#E45649;--shiki-dark:#C678DD"> default</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  plugins</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">    'smmcat-translate'</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">      appId</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> 'your-baidu-app-id'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">,      </span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 百度翻译API App ID</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">      secretKey</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> 'your-baidu-secret'</span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">   // 百度翻译API密钥</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">}</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="获取api密钥" tabindex="-1"><a class="header-anchor" href="#获取api密钥"><span>获取API密钥</span></a></h3>
<ol>
<li>访问<a href="https://api.fanyi.baidu.com/" target="_blank" rel="noopener noreferrer">百度翻译开放平台</a></li>
<li>注册账号并创建应用</li>
<li>获取App ID和Secret Key</li>
<li>在插件配置中填写相应信息</li>
</ol>
<h2 id="使用限制" tabindex="-1"><a class="header-anchor" href="#使用限制"><span>使用限制</span></a></h2>
<h3 id="频率限制" tabindex="-1"><a class="header-anchor" href="#频率限制"><span>频率限制</span></a></h3>
<ul>
<li>免费版：每月200万字符翻译额度</li>
<li>标准版：每月1000万字符翻译额度</li>
<li>高级版：每月1亿字符翻译额度</li>
</ul>
<h3 id="字符限制" tabindex="-1"><a class="header-anchor" href="#字符限制"><span>字符限制</span></a></h3>
<ul>
<li>单次请求最大长度：6000字节</li>
<li>建议单次翻译文本不超过5000字符</li>
</ul>
<h3 id="语言支持" tabindex="-1"><a class="header-anchor" href="#语言支持"><span>语言支持</span></a></h3>
<ul>
<li>支持110种语言双向翻译</li>
<li>包括主流语言、方言和文言文</li>
<li>支持自动语言检测</li>
</ul>
<h2 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h2>
<h3 id="常见错误信息" tabindex="-1"><a class="header-anchor" href="#常见错误信息"><span>常见错误信息</span></a></h3>
<table>
<thead>
<tr>
<th>错误代码</th>
<th>说明</th>
<th>解决方法</th>
</tr>
</thead>
<tbody>
<tr>
<td>52001</td>
<td>请求超时</td>
<td>检查网络连接，稍后重试</td>
</tr>
<tr>
<td>52002</td>
<td>系统错误</td>
<td>服务端问题，稍后重试</td>
</tr>
<tr>
<td>52003</td>
<td>未授权用户</td>
<td>检查API密钥配置是否正确</td>
</tr>
<tr>
<td>54000</td>
<td>必填参数为空</td>
<td>检查翻译文本是否为空</td>
</tr>
<tr>
<td>54001</td>
<td>签名错误</td>
<td>检查API密钥和签名算法</td>
</tr>
<tr>
<td>54003</td>
<td>访问频率受限</td>
<td>降低请求频率</td>
</tr>
<tr>
<td>54004</td>
<td>账户余额不足</td>
<td>充值或等待下月重置</td>
</tr>
<tr>
<td>54005</td>
<td>长query请求频繁</td>
<td>减少长文本翻译频率</td>
</tr>
<tr>
<td>58000</td>
<td>客户端IP非法</td>
<td>检查IP白名单设置</td>
</tr>
<tr>
<td>58001</td>
<td>译文语言方向不支持</td>
<td>检查语言对是否支持</td>
</tr>
</tbody>
</table>
<h3 id="使用建议" tabindex="-1"><a class="header-anchor" href="#使用建议"><span>使用建议</span></a></h3>
<ol>
<li><strong>批量翻译</strong>：对于长文本，建议分段翻译</li>
<li><strong>语言检测</strong>：插件会自动检测源语言，无需手动指定</li>
<li><strong>缓存机制</strong>：相同文本的翻译结果会被缓存，提高响应速度</li>
<li><strong>错误重试</strong>：遇到网络错误时，插件会自动重试</li>
</ol>
<h2 id="高级功能" tabindex="-1"><a class="header-anchor" href="#高级功能"><span>高级功能</span></a></h2>
<h3 id="自定义翻译方向" tabindex="-1"><a class="header-anchor" href="#自定义翻译方向"><span>自定义翻译方向</span></a></h3>
<p>虽然插件支持自动语言检测，但也可以通过特定格式强制指定翻译方向：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>翻译 &#x3C;源语言>-&#x3C;目标语言> &#x3C;文本></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><p>示例：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>翻译 中-英 你好世界</span></span>
<span class="line"><span>翻译 英-日 hello world</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="多语言混合翻译" tabindex="-1"><a class="header-anchor" href="#多语言混合翻译"><span>多语言混合翻译</span></a></h3>
<p>插件支持在单次请求中翻译包含多种语言的混合文本，自动识别并分别翻译。</p>
<h2 id="性能优化" tabindex="-1"><a class="header-anchor" href="#性能优化"><span>性能优化</span></a></h2>
<ul>
<li><strong>响应时间</strong>：通常在1-3秒内完成翻译</li>
<li><strong>并发处理</strong>：支持多用户同时使用</li>
<li><strong>内存管理</strong>：自动清理缓存，避免内存泄漏</li>
</ul>
<h2 id="实际应用场景" tabindex="-1"><a class="header-anchor" href="#实际应用场景"><span>实际应用场景</span></a></h2>
<h3 id="学习交流" tabindex="-1"><a class="header-anchor" href="#学习交流"><span>学习交流</span></a></h3>
<ul>
<li><strong>语言学习</strong>：快速查询单词和短语的翻译</li>
<li><strong>文档阅读</strong>：翻译外文技术文档和论文</li>
<li><strong>跨文化交流</strong>：在群聊中帮助不同语言用户沟通</li>
</ul>
<h3 id="工作场景" tabindex="-1"><a class="header-anchor" href="#工作场景"><span>工作场景</span></a></h3>
<ul>
<li><strong>代码注释</strong>：翻译代码中的英文注释</li>
<li><strong>技术文档</strong>：翻译API文档和开发手册</li>
<li><strong>邮件沟通</strong>：翻译商务邮件内容</li>
</ul>
<h3 id="日常使用" tabindex="-1"><a class="header-anchor" href="#日常使用"><span>日常使用</span></a></h3>
<ul>
<li><strong>旅游准备</strong>：翻译目的地语言的关键短语</li>
<li><strong>购物海淘</strong>：翻译商品描述和用户评价</li>
<li><strong>新闻阅读</strong>：翻译外文新闻和资讯</li>
</ul>
<h2 id="常见问题解答" tabindex="-1"><a class="header-anchor" href="#常见问题解答"><span>常见问题解答</span></a></h2>
<h3 id="q-翻译结果不准确怎么办" tabindex="-1"><a class="header-anchor" href="#q-翻译结果不准确怎么办"><span>Q: 翻译结果不准确怎么办？</span></a></h3>
<p>A: 翻译质量受多种因素影响，包括：</p>
<ul>
<li>文本的复杂程度和语境</li>
<li>语言对的专业性</li>
<li>翻译模型的训练数据</li>
</ul>
<p>建议：</p>
<ul>
<li>简化句子结构</li>
<li>避免使用过于专业的术语</li>
<li>分段翻译长文本</li>
</ul>
<h3 id="q-如何提高翻译速度" tabindex="-1"><a class="header-anchor" href="#q-如何提高翻译速度"><span>Q: 如何提高翻译速度？</span></a></h3>
<p>A:</p>
<ul>
<li>确保网络连接稳定</li>
<li>避免在高峰期大量使用</li>
<li>使用缓存功能（相同文本会缓存结果）</li>
</ul>
<h3 id="q-支持哪些特殊语言" tabindex="-1"><a class="header-anchor" href="#q-支持哪些特殊语言"><span>Q: 支持哪些特殊语言？</span></a></h3>
<p>A: 除了主流语言外，还支持：</p>
<ul>
<li>文言文（古汉语）</li>
<li>粤语</li>
<li>繁体中文</li>
<li>多种方言和少数民族语言</li>
</ul>
<h3 id="q-翻译服务是否收费" tabindex="-1"><a class="header-anchor" href="#q-翻译服务是否收费"><span>Q: 翻译服务是否收费？</span></a></h3>
<p>A: 百度翻译API提供免费额度，超出后需要付费。具体费用请参考百度翻译开放平台的定价策略。</p>
<h3 id="q-如何检查翻译插件是否正常工作" tabindex="-1"><a class="header-anchor" href="#q-如何检查翻译插件是否正常工作"><span>Q: 如何检查翻译插件是否正常工作？</span></a></h3>
<p>A: 可以尝试翻译简单的测试文本，如&quot;hello&quot;或&quot;你好&quot;，如果返回正确结果说明插件运行正常。</p>
<h2 id="最佳实践" tabindex="-1"><a class="header-anchor" href="#最佳实践"><span>最佳实践</span></a></h2>
<ol>
<li><strong>分段翻译</strong>：对于长文档，分段翻译可以获得更好的结果</li>
<li><strong>上下文保持</strong>：尽量保持原文的上下文信息</li>
<li><strong>术语统一</strong>：对于专业术语，建议建立术语表</li>
<li><strong>质量检查</strong>：重要翻译建议人工校对</li>
<li><strong>合理使用</strong>：遵守API使用限制，避免滥用</li>
</ol>
<div class="hint-container warning">
<p class="hint-container-title">注意事项</p>
<ul>
<li>请勿使用翻译功能进行违法或不当内容的翻译</li>
<li>重要文档建议进行人工校对</li>
<li>遵守百度翻译API的使用条款和限制</li>
</ul>
</div>
</div></template>


