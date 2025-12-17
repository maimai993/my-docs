<template><div><h1 id="steam挂刀行情" tabindex="-1"><a class="header-anchor" href="#steam挂刀行情"><span>Steam挂刀行情</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-steam-trading" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-steam-trading" alt="" loading="lazy"></a> <a href="https://github.com/initialencounter/mykoishi" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: trad</p>
<p><strong>功能描述</strong>: 查询Steam挂刀行情，获取不同交易平台的最优交易比例和价格信息</p>
<p><strong>插件名称</strong>: steam-trading</p>
<p><strong>数据来源</strong>: <a href="https://www.iflow.work" target="_blank" rel="noopener noreferrer">iflow.work</a></p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kltP4kAUx9/5FCe+48YvsAnuIwZagadmH6rMSnfXtill3UeNlxCV4IXEa4gVFLxVX0SDF76L6Qz1WzidqdVSPA/tzJzf/M+Zc86vv9rcdEE2TJiYjAG1nNSvtUn57ifbsU+xNDVjyHoBJhS19J8dhY4TIIkito/prf7FNb/4bqJIfR9HSM3HogIpLY9+F0Hy/qN0MVlSTWUWhZUCepyCsj4tm+SwgletMOVZyveHPaHQIcEfICU1pVhQiLVC6p2oYNL3Rz2JtCTnZd1ERlxT0ZQ2ENOzTFYqmkiejZuGnFfUmSghCJJe0nVkImREcx5cB+/IQTz+nRaYbUSR7mDkZfMISKdMFq6/Od0156EzwqAUY1I+YkFaReOaCf/GxnCl6to2p5IfLU/66DFwwG01SH2DY4k0QxJpn2kAD+U8Hr3Ob32Weldpgnuz6I1VdStIKZNlSCbrMyfg2r3XHVvxJnJ0TjP+DOdOwXnqUa2gYqR8jg+eOSwIDBYEH24Bua26rTLea5PtivN0OFyzDW6vhg/qrrVOFpc/C4bfcQbO/T4dOdxc6m+sDK/GOeDtCu7W8M2C21gepnLxRfl5k0KduvTFeEs5NtjwKyC7z/1mlyfv9KyAzMXeADHvS24="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>trad &#x3C;平台></span></span>
<span class="line"><span>trad.行情分析 [url]</span></span></code></pre>
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
<td>平台</td>
<td>文本</td>
<td>是</td>
<td>交易平台名称</td>
<td>buff, igxe, c5, uuyp</td>
</tr>
<tr>
<td>url</td>
<td>文本</td>
<td>否</td>
<td>自定义分析页面URL</td>
<td><a href="https://www.iflow.work/analysis" target="_blank" rel="noopener noreferrer">https://www.iflow.work/analysis</a></td>
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
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>game</td>
<td>-g</td>
<td>string</td>
<td>游戏筛选</td>
<td>dota2, csgo, dota2-csgo, csgo-dota2</td>
</tr>
<tr>
<td>order</td>
<td>-o</td>
<td>string</td>
<td>排序依据</td>
<td>buy, safe_buy, sell</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="查询buff平台行情" tabindex="-1"><a class="header-anchor" href="#查询buff平台行情"><span>查询Buff平台行情</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">trad buff</chat-message>
<chat-message nickname="bot" type="bot">
正在加载中，请稍等片刻~
[图片：Buff平台挂刀行情截图]
</chat-message>
</chat-panel>
<h3 id="查询igxe平台csgo行情" tabindex="-1"><a class="header-anchor" href="#查询igxe平台csgo行情"><span>查询IGXE平台CSGO行情</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">trad igxe -g csgo</chat-message>
<chat-message nickname="bot" type="bot">
正在加载中，请稍等片刻~
[图片：IGXE平台CSGO挂刀行情截图]
</chat-message>
</chat-panel>
<h3 id="查询最优求购比例" tabindex="-1"><a class="header-anchor" href="#查询最优求购比例"><span>查询最优求购比例</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">trad buff -o buy</chat-message>
<chat-message nickname="bot" type="bot">
正在加载中，请稍等片刻~
[图片：Buff平台最优求购比例截图]
</chat-message>
</chat-panel>
<h3 id="自定义行情分析" tabindex="-1"><a class="header-anchor" href="#自定义行情分析"><span>自定义行情分析</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">trad.行情分析 https://www.iflow.work/analysis</chat-message>
<chat-message nickname="bot" type="bot">
正在加载中，请稍等片刻~
[图片：自定义分析页面截图]
</chat-message>
</chat-panel>
<h2 id="平台说明" tabindex="-1"><a class="header-anchor" href="#平台说明"><span>平台说明</span></a></h2>
<table>
<thead>
<tr>
<th>平台</th>
<th>名称</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>buff</td>
<td>Buff交易平台</td>
<td>国内最大的Steam饰品交易平台</td>
</tr>
<tr>
<td>igxe</td>
<td>IGXE交易平台</td>
<td>老牌Steam饰品交易平台</td>
</tr>
<tr>
<td>c5</td>
<td>C5Game交易平台</td>
<td>综合性游戏交易平台</td>
</tr>
<tr>
<td>uuyp</td>
<td>UUYP交易平台</td>
<td>新兴游戏交易平台</td>
</tr>
</tbody>
</table>
<h2 id="排序依据" tabindex="-1"><a class="header-anchor" href="#排序依据"><span>排序依据</span></a></h2>
<table>
<thead>
<tr>
<th>排序方式</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>buy</td>
<td>最优求购比例 - 显示当前最优的求购价格</td>
</tr>
<tr>
<td>safe_buy</td>
<td>稳定求购比例 - 显示相对稳定的求购价格</td>
</tr>
<tr>
<td>sell</td>
<td>最优寄售比例 - 显示当前最优的寄售价格</td>
</tr>
</tbody>
</table>
<h2 id="游戏筛选" tabindex="-1"><a class="header-anchor" href="#游戏筛选"><span>游戏筛选</span></a></h2>
<table>
<thead>
<tr>
<th>游戏类型</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>dota2</td>
<td>仅显示Dota2相关饰品</td>
</tr>
<tr>
<td>csgo</td>
<td>仅显示CSGO相关饰品</td>
</tr>
<tr>
<td>dota2-csgo</td>
<td>显示Dota2和CSGO所有饰品</td>
</tr>
<tr>
<td>csgo-dota2</td>
<td>显示CSGO和Dota2所有饰品</td>
</tr>
</tbody>
</table>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="网页截图" tabindex="-1"><a class="header-anchor" href="#网页截图"><span>网页截图</span></a></h3>
<ul>
<li><strong>完整页面截图</strong>: 自动截取整个行情页面</li>
<li><strong>智能裁剪</strong>: 自动裁剪图片，只保留关键信息区域</li>
<li><strong>图片优化</strong>: 自动处理图片格式和大小</li>
</ul>
<h3 id="加载处理" tabindex="-1"><a class="header-anchor" href="#加载处理"><span>加载处理</span></a></h3>
<ul>
<li><strong>超时控制</strong>:
<ul>
<li>加载超时: 10秒</li>
<li>空闲超时: 30秒</li>
</ul>
</li>
<li><strong>状态提示</strong>: 加载过程中实时反馈状态</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>无法打开页面</strong>: 当页面无法加载时提示</li>
<li><strong>截图失败</strong>: 当截图过程中出现错误时提示</li>
<li><strong>平台无效</strong>: 当指定平台不存在时使用默认平台</li>
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
<td>text_len</td>
<td>number</td>
<td>15</td>
<td>显示条目数量</td>
</tr>
<tr>
<td>buff</td>
<td>boolean</td>
<td>true</td>
<td>启用Buff平台</td>
</tr>
<tr>
<td>igxe</td>
<td>boolean</td>
<td>true</td>
<td>启用IGXE平台</td>
</tr>
<tr>
<td>c5</td>
<td>boolean</td>
<td>false</td>
<td>启用C5Game平台</td>
</tr>
<tr>
<td>uuyp</td>
<td>boolean</td>
<td>false</td>
<td>启用UUYP平台</td>
</tr>
<tr>
<td>game</td>
<td>string</td>
<td>csgo-dota2</td>
<td>游戏筛选</td>
</tr>
<tr>
<td>order</td>
<td>string</td>
<td>safe_buy</td>
<td>排序依据</td>
</tr>
<tr>
<td>min_price</td>
<td>number</td>
<td>1.0</td>
<td>最低价格</td>
</tr>
<tr>
<td>max_price</td>
<td>number</td>
<td>5000.0</td>
<td>最高价格</td>
</tr>
<tr>
<td>min_volume</td>
<td>number</td>
<td>2</td>
<td>最低成交量</td>
</tr>
<tr>
<td>buy</td>
<td>boolean</td>
<td>false</td>
<td>最优求购比例</td>
</tr>
<tr>
<td>safe_buy</td>
<td>boolean</td>
<td>true</td>
<td>稳定求购比例</td>
</tr>
<tr>
<td>sell</td>
<td>boolean</td>
<td>true</td>
<td>寄售比例</td>
</tr>
<tr>
<td>loadTimeout</td>
<td>number</td>
<td>10秒</td>
<td>页面加载超时时间</td>
</tr>
<tr>
<td>idleTimeout</td>
<td>number</td>
<td>30秒</td>
<td>页面空闲超时时间</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问iflow.work网站</li>
<li><strong>平台可用性</strong>: 部分平台可能因地区或网络问题无法访问</li>
<li><strong>数据延迟</strong>: 行情数据可能存在一定的延迟，仅供参考</li>
<li><strong>免责声明</strong>: 对于部署者行为及所产生的任何纠纷，Koishi及steam-trading插件概不负责</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>&quot;挂刀&quot;是Steam社区中的术语，指通过第三方交易平台进行Steam饰品交易以获取更优惠的汇率。此功能可以帮助用户快速了解各平台的实时交易行情。</p>
</div>
</div></template>


