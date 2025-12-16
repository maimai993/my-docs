<template><div><h1 id="b站真实评分计算" tabindex="-1"><a class="header-anchor" href="#b站真实评分计算"><span>B站真实评分计算</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-bilibili-real-rating" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-bilibili-real-rating" alt="npm" loading="lazy"></a><br>
<strong>指令名称</strong>: bili.rating</p>
<p><strong>功能描述</strong>: 获取B站番剧评论并计算真实评分</p>
<p><strong>插件名称</strong>: bilibili-real-rating</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9kt1O4kAUx+95ihPvuxtfYBO6lxhISbhq9qJIV7phW1LK7l6u8SOoQfADNYagBRQ/CxcGDRp9F9OZqW/htDNWC+pJ2vk4v/nPmXPOz4LxdzavmBbMpGNALSOT7RNcuf4RrIJfqZydM5ViHmY0vfwv2Ipsx0GWJOS06Sly3mcHX0ySqO91S9VzsUmBpJFTf5VA9scvdJIu65b2W40qhbRIQaU4q1i4WUWrdpTyLcn9UU/k6ojgd5AThlbKa9hexq3hpGCC+yc98ZSs5JSipZqCoatZY+xO38S0nNUKmv8JpqoUBFOxNH1uMrjxeRhwBgThG81ksJAkuoKpx41DwMMKnu9/dUdr7u1wKoCSAZPkiA0pXRUNC/5MT6NqzXMcRiVea5vgaBsY4PU6uFVnWDwVIPEUZzrArnLvDp/+b76VelHpgjdY8PunthmGJLK+EtOcOQJcb5KrNmmcoZWe+2DTN7zVCsFj8NavUW2HHFx6/UXcGOBqJP4Q7HHwqfHwOXgCnmMTZ5c0D5DToiyqLL/3jFNwb/Zpa6HuIqlzYjwZZ4C2qmi0jQbzXmfpPZXzD7LPahQp1AUXYxVl2Hi9LwHv3ZPuiIVNbrdwq8nITOwZ/dNMAw=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>bili.rating &#x3C;name:text></span></span>
<span class="line"><span>打分 &#x3C;name:text></span></span>
<span class="line"><span>b站评分 &#x3C;name:text></span></span></code></pre>
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
<td>name</td>
<td>文本</td>
<td>是</td>
<td>要查询的B站番剧名称或ID</td>
<td>咒术回战</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本查询" tabindex="-1"><a class="header-anchor" href="#基本查询"><span>基本查询</span></a></h3>
<h4 id="查询-咒术回战-评分" tabindex="-1"><a class="header-anchor" href="#查询-咒术回战-评分"><span>查询 <code v-pre>咒术回战</code> 评分</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">bili.rating 咒术回战</chat-message>
<chat-message nickname="bot" type="bot">
正在搜索番剧信息，本次最大时间限制为 240 秒
</chat-message>
<chat-message nickname="bot" type="bot">
<p>======= 详细统计结果 =======<br>
当前时间：11/16/2025, 7:44:39 PM<br>
番剧名称：咒术回战 第二季<br>
----------------------------<br>
短评统计：<br>
• 平均分：8.4<br>
• 已收集样本：780 条<br>
• 官方标称总数：3429 条<br>
----------------------------<br>
长评统计：<br>
• 平均分：8.3<br>
• 已收集样本：80 条<br>
• 官方标称总数：82 条<br>
----------------------------<br>
综合统计：<br>
• 总平均分：8.4<br>
• 总已收集样本：860 条<br>
----------------------------<br>
官方数据：<br>
• 官方评分：9.4<br>
• 官方样本：5601 条<br>
==============================</p>
</chat-message>
</chat-panel>
<h3 id="使用自定义指令" tabindex="-1"><a class="header-anchor" href="#使用自定义指令"><span>使用自定义指令</span></a></h3>
<h4 id="使用-打分-指令" tabindex="-1"><a class="header-anchor" href="#使用-打分-指令"><span>使用 <code v-pre>打分</code> 指令</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">打分 有兽焉</chat-message>
<chat-message nickname="bot" type="bot">
正在搜索番剧信息，本次最大时间限制为 240 秒
</chat-message>
<chat-message nickname="bot" type="bot">
<p>======= 详细统计结果 =======<br>
当前时间：11/16/2025, 7:54:25 PM<br>
番剧名称：有兽焉<br>
----------------------------<br>
短评统计：<br>
• 平均分：9.9<br>
• 已收集样本：800 条<br>
• 官方标称总数：2477 条<br>
----------------------------<br>
长评统计：<br>
• 平均分：9.1<br>
• 已收集样本：37 条<br>
• 官方标称总数：37 条<br>
----------------------------<br>
综合统计：<br>
• 总平均分：9.9<br>
• 总已收集样本：837 条<br>
----------------------------<br>
官方数据：<br>
• 官方评分：9.6<br>
• 官方样本：3651 条<br>
==============================</p>
</chat-message>
</chat-panel>
<h4 id="使用-b站评分-指令" tabindex="-1"><a class="header-anchor" href="#使用-b站评分-指令"><span>使用 <code v-pre>b站评分</code> 指令</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">b站评分 奇诺之旅</chat-message>
<chat-message nickname="bot" type="bot">
<p>======= 详细统计结果 =======<br>
当前时间：11/16/2025, 7:52:15 PM<br>
番剧名称：奇诺之旅（2017）<br>
----------------------------<br>
短评统计：<br>
• 平均分：9.8<br>
• 已收集样本：820 条<br>
• 官方标称总数：2814 条<br>
----------------------------<br>
长评统计：<br>
• 平均分：9.6<br>
• 已收集样本：59 条<br>
• 官方标称总数：59 条<br>
----------------------------<br>
综合统计：<br>
• 总平均分：9.8<br>
• 总已收集样本：879 条<br>
----------------------------<br>
官方数据：<br>
• 官方评分：9.8<br>
• 官方样本：8425 条<br>
==============================</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>B站API接口</strong>: 通过B站官方API获取番剧信息和评论数据</li>
<li><strong>评论类型</strong>: 同时收集短评和长评，确保数据全面性</li>
<li><strong>数据验证</strong>: 对收集的数据进行有效性验证和去重处理</li>
</ul>
<h3 id="查询逻辑" tabindex="-1"><a class="header-anchor" href="#查询逻辑"><span>查询逻辑</span></a></h3>
<ol>
<li><strong>番剧搜索</strong>: 根据用户输入的番剧名称搜索对应的B站番剧</li>
<li><strong>ID获取</strong>: 获取番剧的唯一标识符用于后续数据收集</li>
<li><strong>评论收集</strong>: 并行收集短评和长评数据</li>
<li><strong>评分计算</strong>: 基于收集的评论数据计算加权平均分</li>
</ol>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>搜索失败</strong>: 当番剧名称无法匹配时提供友好的错误提示</li>
<li><strong>网络超时</strong>: 内置重试机制处理网络请求失败</li>
<li><strong>数据异常</strong>: 对异常数据进行过滤和清理</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问B站API</li>
<li><strong>时间限制</strong>: 单次查询最大时间限制为240秒</li>
<li><strong>数据限制</strong>: 可能无法获取全部评论数据，结果仅供参考</li>
<li><strong>API限制</strong>: 受B站API限制，频繁查询可能触发风控</li>
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
<td>shortLimit</td>
<td>number</td>
<td>1000</td>
<td>短评获取数量限制，达到此数量后停止获取</td>
</tr>
<tr>
<td>shortPercentage</td>
<td>number</td>
<td>100</td>
<td>短评获取百分比限制，达到总数的此百分比后停止获取</td>
</tr>
<tr>
<td>longLimit</td>
<td>number</td>
<td>1000</td>
<td>长评获取数量限制，达到此数量后停止获取</td>
</tr>
<tr>
<td>longPercentage</td>
<td>number</td>
<td>100</td>
<td>长评获取百分比限制，达到总数的此百分比后停止获取</td>
</tr>
<tr>
<td>timeLimit</td>
<td>number</td>
<td>240</td>
<td>总评分获取时间限制（秒），超过此时间后停止获取</td>
</tr>
<tr>
<td>shortTimeLimit</td>
<td>number</td>
<td>120</td>
<td>短评获取时间限制（秒），超过此时间后停止获取短评</td>
</tr>
<tr>
<td>longTimeLimit</td>
<td>number</td>
<td>120</td>
<td>长评获取时间限制（秒），超过此时间后停止获取长评</td>
</tr>
<tr>
<td>retryLimit</td>
<td>number</td>
<td>5</td>
<td>API请求失败重试次数</td>
</tr>
<tr>
<td>banWaitTime</td>
<td>number</td>
<td>6000</td>
<td>触发风控后等待时间（毫秒）</td>
</tr>
<tr>
<td>requestDelay</td>
<td>number</td>
<td>1000</td>
<td>请求间隔时间（毫秒）</td>
</tr>
<tr>
<td>customCommands</td>
<td>string[]</td>
<td>[&quot;打分&quot;, &quot;b站评分&quot;]</td>
<td>自定义触发指令</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>B站真实评分计算功能基于B站官方API实现，能够获取番剧的短评和长评数据，通过统计分析计算真实评分。由于API限制，可能无法获取全部评论数据，结果仅供参考。</p>
</div>
</div></template>


