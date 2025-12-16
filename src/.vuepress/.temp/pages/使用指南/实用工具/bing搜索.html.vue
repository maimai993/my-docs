<template><div><h1 id="bing搜索" tabindex="-1"><a class="header-anchor" href="#bing搜索"><span>bing搜索</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-bing" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-bing" alt="npm" loading="lazy"></a><br>
<strong>指令名称</strong>: bing</p>
<p><strong>功能描述</strong>: 使用Bing搜索引擎进行网页搜索，返回前10个搜索结果</p>
<p><strong>插件名称</strong>: bing</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9kltP4kAUx9/5FCe+sxvfNyZ0N2EJbEnN8tTsQ5GudLO2BIr66D1Gg6Kg8UKIXFS8gSYGDRj9LoaZ1m/htDOoI9Xz0M7M+c1/Zs7//P1vTI0llbQJkVEfkIjJVrGBl2/+uDP3k8nGx9NKKgkRTc9Ou0vccgBkSULNKtllnbXoxn5IEsm9Lql6wjcoIBoJ9V8GZOf/hQxGs7qpTai80gstEFBJjSkmLuXQSoWnnBBZns9wR3OC30EOG1omqeHKEi63BwXDLD+YCURlJaGkTDXtN3Q1brw70wkhJMc1fXzwMp/X5AfIqL79NN/weqUQEoOyQFS/xdMjOF+yrqvobgsX1vhKc+ox8PtHiB/uRJLIDIYeNw4At5fxbOtrr7Pa67aHXEh0GZEhFYjqqmCYMDk8jHLrdrNJqfBrh4QZWgUK2Mc1XM5TLBB1kUCUMTWgR/XuDp5mNt9K9VXqYF/Oky50yobXN1+uJYRcTAgx7hDs1g2+mnMKQYvQ58QgI8UgY4/Afiii/TLlrG4Bl0veqsdAb//z96/IZ1yDKVrdXdodXk85gd7tHrEP1Res/JJ3QU4BFXKoU0SXs3Zt0Uvl7AMHqE+cWedMjLpKsfeeXwDeubfqnbevi/meAZFPWss="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>bing &#x3C;keyword:text></span></span></code></pre>
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
<td>keyword</td>
<td>文本</td>
<td>是</td>
<td>要搜索的关键词</td>
<td>麦芽糖</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本搜索" tabindex="-1"><a class="header-anchor" href="#基本搜索"><span>基本搜索</span></a></h3>
<h4 id="搜索-麦芽糖" tabindex="-1"><a class="header-anchor" href="#搜索-麦芽糖"><span>搜索 <code v-pre>麦芽糖</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">bing 麦芽糖</chat-message>
<chat-message nickname="bot" type="bot">
<ol>
<li>麦芽糖有什么优点和缺点？吃多了会怎样？ - 知乎<br>
<a href="https://www.zhihu.com/question/38210812" target="_blank" rel="noopener noreferrer">https://www.zhihu.com/question/38210812</a></li>
<li>怎么判断二糖的糖苷键是α型还是β型，还有怎么判断二糖本身 ...<br>
<a href="https://www.zhihu.com/question/381854212" target="_blank" rel="noopener noreferrer">https://www.zhihu.com/question/381854212</a></li>
<li>麦芽糖有醛基因此有还原性，为什么在麦芽糖结构式中找不到 ...<br>
<a href="https://www.zhihu.com/question/436654663" target="_blank" rel="noopener noreferrer">https://www.zhihu.com/question/436654663</a></li>
<li>葡萄糖，果糖，蔗糖相比较哪个会使血糖升高？ - 知乎<br>
<a href="https://www.zhihu.com/question/427483316" target="_blank" rel="noopener noreferrer">https://www.zhihu.com/question/427483316</a></li>
<li>麦芽糖是二糖还是单糖？是还原糖么？_百度知道<br>
<a href="https://zhidao.baidu.com/question/403694961.html" target="_blank" rel="noopener noreferrer">https://zhidao.baidu.com/question/403694961.html</a></li>
<li>周杰伦《麦芽糖》这首歌的歌词._百度知道<br>
<a href="https://zhidao.baidu.com/question/280507155.html" target="_blank" rel="noopener noreferrer">https://zhidao.baidu.com/question/280507155.html</a></li>
<li>葡萄糖，麦芽糖，果糖和蔗糖还原性的高低排行是怎么样的？<br>
<a href="https://www.zhihu.com/question/10313603503" target="_blank" rel="noopener noreferrer">https://www.zhihu.com/question/10313603503</a></li>
<li>单糖怎么脱水缩合成多糖，就拿葡萄糖举例，最好画个图。<br>
<a href="https://zhidao.baidu.com/question/2269737442427711628.html" target="_blank" rel="noopener noreferrer">https://zhidao.baidu.com/question/2269737442427711628.html</a></li>
<li>麦芽糖是单糖还是二糖_百度知道<br>
<a href="https://zhidao.baidu.com/question/635674000813349404.html" target="_blank" rel="noopener noreferrer">https://zhidao.baidu.com/question/635674000813349404.html</a></li>
<li>麦芽糖的正确吃法大全-百度经验<br>
<a href="https://jingyan.baidu.com/article/86f4a73e44b80d76d65269f8.html" target="_blank" rel="noopener noreferrer">https://jingyan.baidu.com/article/86f4a73e44b80d76d65269f8.html</a></li>
</ol>
</chat-message>
</chat-panel>
<h4 id="搜索-人工智能" tabindex="-1"><a class="header-anchor" href="#搜索-人工智能"><span>搜索 <code v-pre>人工智能</code></span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">bing 人工智能</chat-message>
<chat-message nickname="bot" type="bot">
<ol>
<li>人工智能（智能科学与技术专业术语）_百度百科<br>
<a href="https://baike.baidu.com/item/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/9180" target="_blank" rel="noopener noreferrer">https://baike.baidu.com/item/人工智能/9180</a></li>
<li>国务院关于深入实施“人工智能+”行动的意见_科技_中国政府网<br>
<a href="https://www.gov.cn/zhengce/content/202508/content_7037861.htm" target="_blank" rel="noopener noreferrer">https://www.gov.cn/zhengce/content/202508/content_7037861.htm</a></li>
<li>国家定调“人工智能+”：中国AI十年三步走，战略解读来了<br>
<a href="https://news.qq.com/rain/a/20250827A04XTV00" target="_blank" rel="noopener noreferrer">https://news.qq.com/rain/a/20250827A04XTV00</a></li>
<li>第一节：人工智能的定义和基本概念 - 知乎<br>
<a href="https://zhuanlan.zhihu.com/p/698162111" target="_blank" rel="noopener noreferrer">https://zhuanlan.zhihu.com/p/698162111</a></li>
<li>人工智能是什么？全面解析AI的定义、技术与应用<br>
<a href="https://www.sohu.com/a/860368477_121956424" target="_blank" rel="noopener noreferrer">https://www.sohu.com/a/860368477_121956424</a></li>
<li>【我国正式全面启动“人工智能+”新时代】-国家发展和改革委员会<br>
<a href="https://www.ndrc.gov.cn/wsdwhfz/202509/t20250901_1400201.html" target="_blank" rel="noopener noreferrer">https://www.ndrc.gov.cn/wsdwhfz/202509/t20250901_1400201.html</a></li>
<li>从实验室到千行百业：我国“人工智能+”六大行动全景图出炉 ...<br>
<a href="https://news.cctv.com/2025/08/27/ARTIj8A653Df44jjD41hdRqP250827.shtml" target="_blank" rel="noopener noreferrer">https://news.cctv.com/2025/08/27/ARTIj8A653Df44jjD41hdRqP250827.shtml</a></li>
<li>人工智能实验室AiLab-人工智能网-中国人工智能领域的专业 ...<br>
<a href="https://www.ailab.cn/" target="_blank" rel="noopener noreferrer">https://www.ailab.cn/</a></li>
<li>人工智能，从深度学习到全面赋能_人民日报<br>
<a href="https://www.peopleapp.com/column/30048352431-500006111786" target="_blank" rel="noopener noreferrer">https://www.peopleapp.com/column/30048352431-500006111786</a></li>
<li>工业和信息化部办公厅关于开展2025年人工智能产业及赋能 ...<br>
<a href="https://www.miit.gov.cn/jgsj/kjs/wjfb/art/2025/art_a8465500de45444dbea19e8064d97ffc.html" target="_blank" rel="noopener noreferrer">https://www.miit.gov.cn/jgsj/kjs/wjfb/art/2025/art_a8465500de45444dbea19e8064d97ffc.html</a></li>
</ol>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="搜索功能" tabindex="-1"><a class="header-anchor" href="#搜索功能"><span>搜索功能</span></a></h3>
<ul>
<li><strong>搜索引擎</strong>: 使用Bing搜索引擎</li>
<li><strong>结果数量</strong>: 返回前10个搜索结果</li>
<li><strong>格式</strong>: 包含标题和URL链接</li>
</ul>
<h3 id="技术实现" tabindex="-1"><a class="header-anchor" href="#技术实现"><span>技术实现</span></a></h3>
<ul>
<li><strong>HTML解析</strong>: 使用cheerio库解析Bing搜索结果页面</li>
<li><strong>请求头</strong>: 模拟真实浏览器请求头，避免被反爬虫机制拦截</li>
<li><strong>编码处理</strong>: 自动处理URL编码和中文关键词</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>网络错误</strong>: 当无法访问Bing时提示</li>
<li><strong>解析错误</strong>: 当搜索结果解析失败时提示</li>
<li><strong>空结果</strong>: 当搜索无结果时返回友好提示</li>
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
<td>isCN</td>
<td>boolean</td>
<td>true</td>
<td>是否使用中国特供Bing</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络依赖</strong>: 需要稳定的网络连接来访问Bing搜索引擎</li>
<li><strong>结果时效性</strong>: 搜索结果基于Bing的实时索引</li>
<li><strong>内容限制</strong>: 某些地区可能无法访问特定内容</li>
<li><strong>格式限制</strong>: 返回结果为纯文本格式，不包含图片或富媒体内容</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>Bing搜索功能基于真实的Bing搜索引擎，能够提供准确和最新的网页搜索结果。插件会自动处理中文编码和搜索结果解析。</p>
</div>
</div></template>


