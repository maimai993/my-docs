<template><div><h1 id="天气查询" tabindex="-1"><a class="header-anchor" href="#天气查询"><span>天气查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 天气</p>
<p><strong>功能描述</strong>: 获取今日或最近天气，基于心知天气API</p>
<p><strong>插件名称</strong>: hello-rainbow</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9ks1OwkAQx+88xcQ7Gu/GpOoBggFKwqnxUKRKDbakFPWoosZoiF9o/AqKVMWPAF7QgNF3Mey2voVLd0EK1TlAd+a3/5mdmbmkujybEDUdpiMeIBYVzHwZb7/O2Cf7J52JzWtiKgHTspJZsV0ONwcCz6PKDbllPlXpxY7xPIn9uiQl7hkUCKpxaSENQvt/mHxEMoouL0pOpS49QUAxNSvq+DKHdopOqm1BFndGHKkdgpMgBFQ5nZBxcQsX6oOCARYfjHAhQYyLKV3SvKoixdS+nG3zRYSElEyqXk2UlZi6PFjV/82ZAgEZJ9/ZMhf2u72YuAX0mTWvbpHxgGv5sZg27oJ2EnWTRMHrHSfzsQ88T04w9HVwDbi+jdeqI63GbqtZH7KhoM0EGVKEkCJNqDosjY6i3J5VqVAq8LsxAYbeAAWs+xIu7FOMC9kIF2JMCWiq1vv19+phr1RHxQCrliVb6Wgj3jvs1uejq+uLsAu3YFVf8ct6b1tIS1j+sJ8WEPYz/A6szzy6KFAQH9dwjj2pX/iekWbzjG6EW7llaL2dk94jY8Pc33J/9AOgoxxq5FFtzSptuqk8/tFlOgvHQJ6YGJ0cxfrn+gz49MM0GmbzCBcuKRP1/AA2rlo2"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>天气 &#x3C;city> [day]</span></span>
<span class="line"><span>weather &#x3C;city> [day]</span></span></code></pre>
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
<td>city</td>
<td>文本</td>
<td>是</td>
<td>要查询天气的城市名称</td>
<td>北京</td>
</tr>
<tr>
<td>day</td>
<td>数字</td>
<td>否</td>
<td>要查询最近多少天的天气，默认3天</td>
<td>5</td>
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
</tr>
</thead>
<tbody>
<tr>
<td>-h</td>
<td>-h</td>
<td>无</td>
<td>显示帮助信息</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="基本查询" tabindex="-1"><a class="header-anchor" href="#基本查询"><span>基本查询</span></a></h3>
<h4 id="查询-北京-天气-默认最近3天" tabindex="-1"><a class="header-anchor" href="#查询-北京-天气-默认最近3天"><span>查询 <code v-pre>北京</code> 天气（默认最近3天）</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京</chat-message>
<chat-message nickname="bot" type="bot">
2025-10-21（今天）
    天气：晴 转 多云
    温度：2 - 13 ℃
    湿度：33 %
    北风2级
<p>2025-10-22<br>
天气：多云 转 小雨<br>
温度：2 - 10 ℃<br>
湿度：42 %<br>
北风2级</p>
<p>2025-10-23<br>
天气：多云<br>
温度：3 - 12 ℃<br>
湿度：55 %<br>
北风1级</p>
</chat-message>
</chat-panel>
<h4 id="查询-北京-最近5天-天气" tabindex="-1"><a class="header-anchor" href="#查询-北京-最近5天-天气"><span>查询 <code v-pre>北京</code> <code v-pre>最近5天</code> 天气</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京 5</chat-message>
<chat-message nickname="bot" type="bot">
2025-10-21（今天）
    天气：晴 转 多云
    温度：2 - 13 ℃
    湿度：33 %
    北风2级
<p>2025-10-22<br>
天气：多云 转 小雨<br>
温度：2 - 10 ℃<br>
湿度：42 %<br>
北风2级</p>
<p>2025-10-23<br>
天气：多云<br>
温度：3 - 12 ℃<br>
湿度：55 %<br>
北风1级</p>
<p>2025-10-24<br>
天气：晴<br>
温度：4 - 15 ℃<br>
湿度：40 %<br>
南风1级</p>
<p>2025-10-25<br>
天气：多云<br>
温度：5 - 16 ℃<br>
湿度：45 %<br>
南风2级</p>
</chat-message>
</chat-panel>
<h3 id="查询区级天气" tabindex="-1"><a class="header-anchor" href="#查询区级天气"><span>查询区级天气</span></a></h3>
<h4 id="查询-北京-朝阳-天气" tabindex="-1"><a class="header-anchor" href="#查询-北京-朝阳-天气"><span>查询 <code v-pre>北京/朝阳</code> 天气</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京/朝阳</chat-message>
<chat-message nickname="bot" type="bot">
2025-10-21（今天）
    天气：晴 转 多云
    温度：3 - 14 ℃
    湿度：35 %
    北风2级
<p>2025-10-22<br>
天气：多云 转 小雨<br>
温度：3 - 11 ℃<br>
湿度：44 %<br>
北风2级</p>
<p>2025-10-23<br>
天气：多云<br>
温度：4 - 13 ℃<br>
湿度：58 %<br>
北风1级</p>
</chat-message>
</chat-panel>
<h3 id="错误处理示例" tabindex="-1"><a class="header-anchor" href="#错误处理示例"><span>错误处理示例</span></a></h3>
<h4 id="查询不存在的城市" tabindex="-1"><a class="header-anchor" href="#查询不存在的城市"><span>查询不存在的城市</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 不存在的城市</chat-message>
<chat-message nickname="bot" type="bot">
未找到城市：不存在的城市 区级请用 北京/朝阳 写法
</chat-message>
</chat-panel>
<h4 id="查询非法天数" tabindex="-1"><a class="header-anchor" href="#查询非法天数"><span>查询非法天数</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">天气 北京 0</chat-message>
<chat-message nickname="bot" type="bot">
0 并非合法天数
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="数据来源" tabindex="-1"><a class="header-anchor" href="#数据来源"><span>数据来源</span></a></h3>
<ul>
<li><strong>API服务</strong>: 基于心知天气API</li>
<li><strong>数据更新</strong>: 实时天气数据，每日更新</li>
</ul>
<h3 id="查询逻辑" tabindex="-1"><a class="header-anchor" href="#查询逻辑"><span>查询逻辑</span></a></h3>
<ul>
<li><strong>城市匹配</strong>: 支持城市名称和区级查询（使用/分隔）</li>
<li><strong>天数控制</strong>: 支持查询1-31天的天气数据</li>
<li><strong>智能处理</strong>: 自动处理城市名称中的&quot;市&quot;、&quot;区&quot;等后缀</li>
</ul>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<ul>
<li><strong>城市未找到</strong>: 当查询的城市不存在时提示</li>
<li><strong>非法天数</strong>: 当天数不是正整数时提示</li>
<li><strong>API错误</strong>: 当API请求失败时返回相应错误信息</li>
<li><strong>付费限制</strong>: 免费用户只能获取最近3天的信息</li>
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
<td>baseurl</td>
<td>string</td>
<td><a href="https://api.seniverse.com/v3" target="_blank" rel="noopener noreferrer">https://api.seniverse.com/v3</a></td>
<td>API基础路径</td>
</tr>
<tr>
<td>privateKey</td>
<td>string</td>
<td>空</td>
<td>API私钥（必须配置）</td>
</tr>
<tr>
<td>publicKey</td>
<td>string</td>
<td>空</td>
<td>API公钥（公钥加密时需要）</td>
</tr>
<tr>
<td>encodeType</td>
<td>string</td>
<td>私钥</td>
<td>加密类型：公钥/私钥</td>
</tr>
<tr>
<td>defaultDay</td>
<td>number</td>
<td>3</td>
<td>默认获取最近多少天的天气</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>API密钥</strong>: 使用前需要注册心知天气API并配置密钥</li>
<li><strong>免费限制</strong>: 免费用户只能获取最近3天的天气信息</li>
<li><strong>城市格式</strong>: 区级查询使用&quot;城市/区&quot;格式，如&quot;北京/朝阳&quot;</li>
<li><strong>网络依赖</strong>: 需要稳定的网络连接来访问API服务</li>
<li><strong>数据准确性</strong>: 天气数据来源于心知天气，可能存在延迟</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>天气查询功能基于心知天气API实现，能够提供准确的天气预报和实时天气信息。建议使用公钥加密方式以获得更好的安全性。</p>
</div>
</div></template>


