<template><div><h1 id="大学查询" tabindex="-1"><a class="header-anchor" href="#大学查询"><span>大学查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 学校查询</p>
<p><strong>功能描述</strong>: 查询大学基本信息，包括成立时间、占地面积、学校地址和简介</p>
<p><strong>插件名称</strong>: smmcat-daxue</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9kktPwkAQx+98iol3NN6NSZULwQA1ISFpPBSpgpGWQFGPvmM0xBcxvkJEUFAU8AIGjHwX092Wb+HSXR6F6hza3Znf/md2ZlfWlc3liJhQYWHRAcQCgp4p4aPGkrkzP8lUaDUhxiOwEJVTW6bL4uZA4HlUeSSn9HKVHuwZz5PYwCXJYce4gFcJS2tJELr/SbJYTMlqNCZZlfr0HAHF+LKo4vs0Os5Zqa55WdwasaS2CM6D4FGiyUgU5w5xtj4u6GHx8QjnE8SwGFelhFORpZAykrNrrqCQjMVIOc6wuJUauVS3qP974wIBFa46eyXO77a7MHEToIjen7V2Du9UZ0KJWRu0l6ifJABO5ywZj7nhebKDiZ/zB8D1I6IypTVPtFZ9woS8JuNlSA58sjSnqLAxPY3Sp0alQinP4MF4GPoIFDCKeZw9oxjnMxHOx5g80FTa10Nn+2JYqqdSAKO2Rx7lcBfx6UW/PFfQxF1Bxj+BUW3gj91+21hiv5tm9rsZ+AxGO4PussPts5csMlJv3dCXYFdnCbTPW9J0VNjXzw7tb/sC6DKNmhlU2zHyB3Yqr3+0lw7BMokyE6Mjo9joQN8AX3/rhabeusTZe8oEHL89UlUf"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>学校查询 &#x3C;query></span></span></code></pre>
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
<td>query</td>
<td>文本</td>
<td>是</td>
<td>要查询的大学名称</td>
<td>清华大学</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本查询" tabindex="-1"><a class="header-anchor" href="#基本查询"><span>基本查询</span></a></h3>
<h4 id="查询-清华大学-信息" tabindex="-1"><a class="header-anchor" href="#查询-清华大学-信息"><span>查询 <code v-pre>清华大学</code> 信息</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">学校查询 清华大学</chat-message>
<chat-message nickname="bot" type="bot">
<p>找到如下学校信息：<br>
【清华大学】<br>
[成立时间] 1911年<br>
[占地面积] 6632亩<br>
[学校地址] 北京市海淀区清华园1号<br>
[学校信息] 清华大学建校时间为1911年，占地面积6632亩，隶属于教育部，地址为北京市海淀区清华园1号，学校有44个国家重点学科，13个重点实验室，60个博士学科，65个硕士专业学科，属于985,211,双一流,强基计划学校。</p>
</chat-message>
</chat-panel>
<h4 id="查询-北京大学-信息" tabindex="-1"><a class="header-anchor" href="#查询-北京大学-信息"><span>查询 <code v-pre>北京大学</code> 信息</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">学校查询 北京大学</chat-message>
<chat-message nickname="bot" type="bot">
<p>找到如下学校信息：<br>
【北京大学】<br>
[成立时间] 1898年<br>
[占地面积] 7000亩<br>
[学校地址] 北京市海淀区颐和园路5号<br>
[学校信息] 北京大学建校时间为1898年，占地面积7000亩，隶属于教育部，地址为北京市海淀区颐和园路5号，学校有54个国家重点学科，47个重点实验室，49个博士学科，50个硕士专业学科，属于985,211,双一流,强基计划学校。</p>
</chat-message>
</chat-panel>
<h3 id="查询不存在的大学" tabindex="-1"><a class="header-anchor" href="#查询不存在的大学"><span>查询不存在的大学</span></a></h3>
<h4 id="查询不存在的大学-1" tabindex="-1"><a class="header-anchor" href="#查询不存在的大学-1"><span>查询不存在的大学</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">学校查询 魔法学院</chat-message>
<chat-message nickname="bot" type="bot">
没有找到对应的大学信息
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>API服务</strong>: 基于第三方大学信息API</li>
<li><strong>数据范围</strong>: 覆盖中国主要高等院校</li>
<li><strong>信息类型</strong>: 基本信息、历史沿革、地理位置</li>
</ul>
<h3 id="查询逻辑" tabindex="-1"><a class="header-anchor" href="#查询逻辑"><span>查询逻辑</span></a></h3>
<ul>
<li><strong>精确匹配</strong>: 基于大学名称进行精确查询</li>
<li><strong>中文支持</strong>: 支持中文大学名称查询</li>
<li><strong>错误处理</strong>: 当查询无结果时返回友好提示</li>
</ul>
<h3 id="返回信息" tabindex="-1"><a class="header-anchor" href="#返回信息"><span>返回信息</span></a></h3>
<ul>
<li><strong>成立时间</strong>: 学校的创办年份</li>
<li><strong>占地面积</strong>: 校园总面积</li>
<li><strong>学校地址</strong>: 详细地理位置</li>
<li><strong>学校信息</strong>: 学校简介和特色</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>空输入</strong>: 当用户未输入任何内容时提示</li>
<li><strong>无结果</strong>: 当查询无结果时返回友好提示</li>
<li><strong>网络错误</strong>: 当API请求失败时提示</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>数据准确性</strong>: 结果来源于第三方API，可能存在信息更新不及时的情况</li>
<li><strong>网络依赖</strong>: 需要稳定的网络连接来访问API服务</li>
<li><strong>查询范围</strong>: 主要支持中国大陆地区的高等院校</li>
<li><strong>信息完整性</strong>: 不同学校的信息完整度可能有所差异</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>大学查询功能基于第三方API实现，能够查询中国主要高等院校的基本信息，帮助用户了解学校概况。</p>
</div>
</div></template>


