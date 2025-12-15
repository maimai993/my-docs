<template><div><h1 id="火星文转换" tabindex="-1"><a class="header-anchor" href="#火星文转换"><span>火星文转换</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-martian-translator" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-martian-translator" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/martian-translator" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: <code v-pre>火星文</code> <code v-pre>反火星文</code></p>
<p><strong>功能描述</strong>: 将简体中文和火星文互相转换</p>
<p><strong>插件名称</strong>: martian-translator</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl/ABD0ikBo4NR5WqVKjLSlFPUpEQjQEBBKJEsKXgILACQ348S6G3da3cOkWsBTn0O7M/PY/k5k9OJbP9kNIUWF7xwHUAryWb5Hk667hGZ9IdO9QQeEQbItS9NwIWcIu4DkOd6v0ltbusYtT4ziam4cEKeiwC3jloHAUAX7yX6WHnaikiieCVWlGb1IQhfeRSoopfF2xUhPzmnlrxlLaIrgFvFsWIyGRVBKkNLALus28PePy8SiIwqqgOGVJ2JMXak7M4+dP6HxFJDlVBUmRY6TKir21xfOs3QA4nRt0jobDcdSDle/bMpBBksR6a+PhzXg0WDEgr8F4TaQCPknYlFU4XV/HqbTe7TLKPd+s20SrwAC9WSOlDMNcPgNx+UymBqzU+L38c5H9KzVVqYPev5y8nnR21pLHbyAev8k8An650zoNUijjflz/6JBUdTnZAP0rjx9KjNFGOVIqLqvahPHbPX0HuB7XMonlvbcA51J4mMf9mF67Wqby9M+w2Egtc302xdgCGLa4njaQwqdWH9qbDzh+ASCVKIc="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>火星文 &#x3C;文本></span></span>
<span class="line"><span>反火星文 &#x3C;文本></span></span></code></pre>
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
<td>文本</td>
<td>文本</td>
<td>是</td>
<td>要转换的文本内容</td>
<td>你好啊</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="简体中文转火星文" tabindex="-1"><a class="header-anchor" href="#简体中文转火星文"><span>简体中文转火星文</span></a></h3>
<h4 id="转换-你好啊-为火星文" tabindex="-1"><a class="header-anchor" href="#转换-你好啊-为火星文"><span>转换&quot;你好啊&quot;为火星文</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">火星文 你好啊</chat-message>
<chat-message nickname="bot" type="bot">
沵恏娿
</chat-message>
</chat-panel>
<h4 id="转换-今天天气不错-为火星文" tabindex="-1"><a class="header-anchor" href="#转换-今天天气不错-为火星文"><span>转换&quot;今天天气不错&quot;为火星文</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">火星文 今天天气不错</chat-message>
<chat-message nickname="bot" type="bot">
妗兲兲気芣諎
</chat-message>
</chat-panel>
<h3 id="火星文转简体中文" tabindex="-1"><a class="header-anchor" href="#火星文转简体中文"><span>火星文转简体中文</span></a></h3>
<h4 id="转换-沵恏娿-为简体中文" tabindex="-1"><a class="header-anchor" href="#转换-沵恏娿-为简体中文"><span>转换&quot;沵恏娿&quot;为简体中文</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">反火星文 沵恏娿</chat-message>
<chat-message nickname="bot" type="bot">
你好啊
</chat-message>
</chat-panel>
<h4 id="转换-妗兲兲気芣諎-为简体中文" tabindex="-1"><a class="header-anchor" href="#转换-妗兲兲気芣諎-为简体中文"><span>转换&quot;妗兲兲気芣諎&quot;为简体中文</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">反火星文 妗兲兲気芣諎</chat-message>
<chat-message nickname="bot" type="bot">
今天天气不错
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="转换原理" tabindex="-1"><a class="header-anchor" href="#转换原理"><span>转换原理</span></a></h3>
<ul>
<li><strong>字符映射</strong>: 基于预定义的字符映射表进行转换</li>
<li><strong>双向转换</strong>: 支持简体中文到火星文的转换，也支持火星文到简体中文的反向转换</li>
<li><strong>容错处理</strong>: 对于无法识别的字符保持原样输出</li>
</ul>
<h3 id="支持的字符范围" tabindex="-1"><a class="header-anchor" href="#支持的字符范围"><span>支持的字符范围</span></a></h3>
<ul>
<li><strong>简体中文</strong>: 支持常用汉字字符转换</li>
<li><strong>火星文</strong>: 支持常见的火星文字符变体</li>
<li><strong>特殊字符</strong>: 标点符号、数字、英文字母等保持原样</li>
</ul>
<h3 id="转换算法" tabindex="-1"><a class="header-anchor" href="#转换算法"><span>转换算法</span></a></h3>
<ol>
<li>
<p><strong>正向转换</strong>: 简体中文 → 火星文</p>
<ul>
<li>遍历输入文本的每个字符</li>
<li>在简体中文字符表中查找对应位置</li>
<li>返回火星文字符表中对应位置的字符</li>
<li>如果找不到对应字符，保持原样</li>
</ul>
</li>
<li>
<p><strong>反向转换</strong>: 火星文 → 简体中文</p>
<ul>
<li>遍历输入文本的每个字符</li>
<li>在火星文字符表中查找对应位置</li>
<li>返回简体中文字符表中对应位置的字符</li>
<li>如果找不到对应字符，保持原样</li>
</ul>
</li>
</ol>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>字符覆盖</strong>: 转换表覆盖常用汉字，但可能不包含所有生僻字</li>
<li><strong>转换精度</strong>: 对于复杂的火星文变体，转换可能不完全准确</li>
<li><strong>性能考虑</strong>: 转换过程为线性时间复杂度，适合处理常规长度的文本</li>
<li><strong>字符保持</strong>: 非汉字字符（数字、字母、标点）在转换过程中保持不变</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>本插件为轻量级工具，无需额外配置参数。</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>火星文转换功能基于字符映射表实现，能够快速准确地进行简体中文和火星文之间的双向转换。该功能简单实用，适合日常娱乐和文字转换需求。</p>
</div>
</div></template>


