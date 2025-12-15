<template><div><h1 id="拼音缩写查询" tabindex="-1"><a class="header-anchor" href="#拼音缩写查询"><span>拼音缩写查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-abbreviation" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-abbreviation" alt="" loading="lazy"></a>  <a href="https://github.com/koishijs/koishi-plugin-abbreviation" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: abbr</p>
<p><strong>功能描述</strong>: 中文缩写词搜索，基于「能不能好好说话？」API</p>
<p><strong>插件名称</strong>: abbreviation</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9ks1O20AQx+95ihH3tOJeIdntJQpKYqScrB5s4jauWjtyHNpjaFqE2lpQiKp+0EC+SlqqGCQUUMLHu4B3vZx4BTbeTYiJYWWtd2d++5/dmXnx2ny7mFcsG+YXYkBHVvarHbx69DzYBVOxpL60lEIe5nWj9C4whcwCyJKEug16yt9z2cHRkCTquzVpRi42LZAyc9qrIsjD/yO6WCgZtv5GCyuNaZGCSmFRsfGWgz7Vw9RwpLg/7AmFDgk+BTlp6sW8jusruNabFkxy/7RHSMtKTinYmhU3DU0178QMEFFWVNXSlnTF1k1j+lIP5+YZyKj17arSETKJqAdTs3xZ/kIqp96xQ2fUHn7EPSTu7+uT7cuy80S15iIOj0KPw2YhHp+jBQs2kkR3MHPxdQdwbxUvu4+9/mdv0JsJoFTApDhSh7ShiaYNS7OzyFkj3S6jkrctlORoAxhAdpu4ts4wIR0gQpozTWChvJOdq/LGpNRIpQVkv0LbdDKveG1jfD1BZIoi59tA3CN88H6cSI5lEozLJDj4B8h5Ff2q4e02cRv+YBPXtqIldznpD36w3oi6Zwe845806aj1wV9fiX7tX0CbDupX0f4yaX6MUvl3T3pZEUKV2ONirGQMu1vQ/4C/n/mt/uTrsrEbBRRh3w=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>abbr &#x3C;text></span></span></code></pre>
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
<td>text</td>
<td>文本</td>
<td>是</td>
<td>要查询的拼音缩写</td>
<td>myt</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本查询" tabindex="-1"><a class="header-anchor" href="#基本查询"><span>基本查询</span></a></h3>
<h4 id="查询-myt-拼音缩写" tabindex="-1"><a class="header-anchor" href="#查询-myt-拼音缩写"><span>查询 <code v-pre>myt</code> 拼音缩写</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">abbr myt</chat-message>
<chat-message nickname="bot" type="bot">
myt：没有头, 麦芽糖, 米羽糖
</chat-message>
</chat-panel>
<h4 id="查询-yyds-拼音缩写" tabindex="-1"><a class="header-anchor" href="#查询-yyds-拼音缩写"><span>查询 <code v-pre>yyds</code> 拼音缩写</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">abbr yyds</chat-message>
<chat-message nickname="bot" type="bot">
yyds：永远滴神, 永远的神, 永远单身
</chat-message>
</chat-panel>
<h4 id="查询-xswl-拼音缩写" tabindex="-1"><a class="header-anchor" href="#查询-xswl-拼音缩写"><span>查询 <code v-pre>xswl</code> 拼音缩写</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">abbr xswl</chat-message>
<chat-message nickname="bot" type="bot">
xswl：笑死我了, 想死我了, 想死我了
</chat-message>
</chat-panel>
<h3 id="查询不存在的缩写" tabindex="-1"><a class="header-anchor" href="#查询不存在的缩写"><span>查询不存在的缩写</span></a></h3>
<h4 id="查询不存在的缩写-1" tabindex="-1"><a class="header-anchor" href="#查询不存在的缩写-1"><span>查询不存在的缩写</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">abbr abcdefg</chat-message>
<chat-message nickname="bot" type="bot">
未找到对应的缩写。
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>API服务</strong>: 基于「能不能好好说话？」(nbnhhsh) API</li>
<li><strong>数据更新</strong>: 实时查询，数据源持续更新</li>
</ul>
<h3 id="查询逻辑" tabindex="-1"><a class="header-anchor" href="#查询逻辑"><span>查询逻辑</span></a></h3>
<ul>
<li><strong>精确匹配</strong>: 优先返回已确认的翻译结果</li>
<li><strong>输入建议</strong>: 如果没有确认翻译，返回用户输入建议</li>
<li><strong>多结果支持</strong>: 支持返回多个可能的含义</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>空输入</strong>: 当用户未输入任何内容时提示</li>
<li><strong>无结果</strong>: 当查询无结果时返回友好提示</li>
<li><strong>网络错误</strong>: 当API请求失败时提示</li>
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
<td>endpoint</td>
<td>string</td>
<td><a href="https://lab.magiconch.com/api/nbnhhsh/guess" target="_blank" rel="noopener noreferrer">https://lab.magiconch.com/api/nbnhhsh/guess</a></td>
<td>API服务地址</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>数据准确性</strong>: 结果来源于用户提交的数据，可能存在不准确的情况</li>
<li><strong>网络依赖</strong>: 需要稳定的网络连接来访问API服务</li>
<li><strong>实时性</strong>: 查询结果为实时数据，可能包含最新的网络用语</li>
<li><strong>多义性</strong>: 同一缩写可能有多个不同的含义</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>拼音缩写查询功能基于「能不能好好说话？」API实现，能够查询最新的网络用语和流行缩写词。</p>
</div>
</div></template>


