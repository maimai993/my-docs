<template><div><h1 id="成语查询" tabindex="-1"><a class="header-anchor" href="#成语查询"><span>成语查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 成语查询</p>
<p><strong>功能描述</strong>: 查询成语含义、出处、用法和示例，支持精确查询和模糊匹配</p>
<p><strong>插件名称</strong>: idiom-dictionary</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJyNkstu2kAUhvc8xSh7WmVfRSJ0gUSE7QhWVhcGu8VVsS1jetklahuhUpo0UKkXREOgDS2pQV3QCKL2XSpmxn2LDjMTwmAnyixsz5zv/Gd8zn//kf2kUNRcD2xtxwBZORU3+6j66x7d0Ue5kn/gak4RbJlW5Sk9Eo4TQFUU6B+TLDwYssSLpSgkdnlkWHosLJCxdeNhGajz9y3ysV2xPLNkiEoLepOAmlPQPNSqw1cdkZqvDI+LEaG0IJgEato2y0UTdfZQexwWTPN4OJKQVE3XHM9w47Zl5O2VmvMlZVVTN+1SXDcLnmlbmvssDMmy6lQcx/AMww1f+/ru3QUqrp3iQS1ZdO2SEdWVZEplwTt5dwOd/USfG/D8HWq8EScj1MiBeHyDzI9uFIXswNrft0cAjatod3h7NqnNpuM1CmUok+FIB0iWsWl74PH6OqzvB77PqPSlo9IcPQYMCE66qH3AsIREkYTEmS5gpWbnR/92DpelLlR6IBg9J65dbTPaP1xcUcrSFCnLc76A4E8Tfmrj6Qc22yjhr1x4MZplRVmmrCxz+IQotnC/xlIYk0xRJpniTJ9XZSPA0wZqt6LVvt3kft8X0FyIoKsdiP73AUCtHTytwt4LfLAH/deoynsvyp+C2dlH4iXGRU/nB4CNOpw04Wg36L6MUvGvsAMzjeCcIRdjFmPYqgFHAL3/jXuT5eblYv8BmqSlsQ=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>成语查询 &#x3C;成语></span></span>
<span class="line"><span>近义词查询 &#x3C;词语></span></span>
<span class="line"><span>反义词查询 &#x3C;词语></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>成语</td>
<td>文本</td>
<td>是</td>
<td>要查询的成语，支持使用?进行模糊匹配</td>
<td>一帆风顺</td>
</tr>
<tr>
<td>词语</td>
<td>文本</td>
<td>是</td>
<td>要查询近义词或反义词的词语</td>
<td>美丽</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="成语精确查询" tabindex="-1"><a class="header-anchor" href="#成语精确查询"><span>成语精确查询</span></a></h3>
<h4 id="查询成语-一帆风顺" tabindex="-1"><a class="header-anchor" href="#查询成语-一帆风顺"><span>查询成语 <code v-pre>一帆风顺</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">成语查询 一帆风顺</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/成语查询_一帆风顺.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="成语模糊查询" tabindex="-1"><a class="header-anchor" href="#成语模糊查询"><span>成语模糊查询</span></a></h3>
<h4 id="模糊查询-帆" tabindex="-1"><a class="header-anchor" href="#模糊查询-帆"><span>模糊查询 <code v-pre>?帆??</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">成语查询 ?帆??</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/成语查询_帆.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="近义词查询" tabindex="-1"><a class="header-anchor" href="#近义词查询"><span>近义词查询</span></a></h3>
<h4 id="查询词语-美丽-的近义词" tabindex="-1"><a class="header-anchor" href="#查询词语-美丽-的近义词"><span>查询词语 <code v-pre>美丽</code> 的近义词</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">近义词查询 美丽</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/成语查询_美丽.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="反义词查询" tabindex="-1"><a class="header-anchor" href="#反义词查询"><span>反义词查询</span></a></h3>
<h4 id="查询词语-美丽-的反义词" tabindex="-1"><a class="header-anchor" href="#查询词语-美丽-的反义词"><span>查询词语 <code v-pre>美丽</code> 的反义词</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">反义词查询 美丽</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/成语查询_美丽2.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的查询类型" tabindex="-1"><a class="header-anchor" href="#支持的查询类型"><span>支持的查询类型</span></a></h3>
<ul>
<li><strong>精确查询</strong>: 直接查询完整成语的详细释义</li>
<li><strong>模糊查询</strong>: 使用?作为通配符进行位置匹配查询</li>
<li><strong>近义词查询</strong>: 查询词语的近义词及解释</li>
<li><strong>反义词查询</strong>: 查询词语的反义词及解释</li>
</ul>
<h3 id="输出模式" tabindex="-1"><a class="header-anchor" href="#输出模式"><span>输出模式</span></a></h3>
<ul>
<li><strong>文本模式</strong>: 默认输出纯文本结果</li>
<li><strong>图片模式</strong>: 启用puppeteer服务后可输出渲染图片</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>问号处理</strong>: 自动将?和？统一处理为通配符</li>
<li><strong>长度验证</strong>: 自动验证成语是否为四字成语</li>
<li><strong>结果限制</strong>: 可配置最大返回结果数量</li>
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
<td>Maximumidiom</td>
<td>number</td>
<td>10</td>
<td>返回成语的最大数量限制</td>
</tr>
<tr>
<td>MaximumnearSynonyms</td>
<td>number</td>
<td>5</td>
<td>返回近义词/反义词的最大数量限制</td>
</tr>
<tr>
<td>imagifyoutput</td>
<td>boolean</td>
<td>false</td>
<td>图片输出模式（需要puppeteer服务）</td>
</tr>
<tr>
<td>consoleinfo</td>
<td>boolean</td>
<td>false</td>
<td>日志调试模式</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>成语长度</strong>: 成语查询仅支持四字成语，未知字可用?代替</li>
<li><strong>模糊查询</strong>: 近义词和反义词查询不支持模糊查询</li>
<li><strong>网络要求</strong>: 需要网络连接访问汉语国学网</li>
<li><strong>图片模式</strong>: 图片输出需要安装并配置puppeteer服务</li>
<li><strong>查询限制</strong>: 模糊查询结果数量受Maximumidiom配置限制</li>
</ol>
<h2 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h2>
<ul>
<li><strong>输入不完整</strong>: 当输入为空或包含问号时提示</li>
<li><strong>未找到结果</strong>: 当查询无匹配结果时提示</li>
<li><strong>查询失败</strong>: 当网络或服务异常时提示</li>
<li><strong>长度错误</strong>: 当输入不是四字成语时提示</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>成语查询插件基于<a href="https://www.hanyuguoxue.com" target="_blank" rel="noopener noreferrer">汉语国学网</a>的权威数据，提供准确的成语释义、出处和用法说明。支持模糊查询功能，可以帮助用户在不记得完整成语时进行查找。</p>
</div>
</div></template>


