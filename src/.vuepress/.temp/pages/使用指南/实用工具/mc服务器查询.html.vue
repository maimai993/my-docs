<template><div><h1 id="mc服务器查询" tabindex="-1"><a class="header-anchor" href="#mc服务器查询"><span>MC服务器查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: MBS/MJS</p>
<p><strong>功能描述</strong>: 查询Minecraft Java版和基岩版服务器信息</p>
<p><strong>插件名称</strong>: mcmotd-customserver-canvas</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl/ABD1iITXh1HgopQpGWkILepSoiBoCAgcVwjeCYoATGjD4Lobd1rew7ZaPQp1DuzPz2/9MZ3p0Kp5xQTYqw/6BAzTzMUqhg1Mfh4ZnPKSY/zjKRoKwHxJi50bIEnYBQ9OoV9duKd0+uTgzmtZyixAvBBzrAh4xwJ9IwOjvTe1wEBPkUJi3Ks3pXQ1kIxwr41Ia3dWslG4eM2/NWEpbBPeAcYshKRjCtSQuD9cF3WZ+PePyMmyAjch81CkKvF9cqakbRTFhLizKAScXk2QxLPHRuIZzrBBnpfUWV8/ztn3gdO5o8zQcmtY82Ph5qAIepnCivzUd3U/Hww0D8hiMx0Rq4BX4XVGG+PY2SmfUXo9Q7sWG3SZaBwKo7QYuZwnm8hqIy2syDSClpl/V34vcstRMpQnq4FL/izK5eUsUZSAUZTItwJWW2q+THaKnjj32AkqhglNZVJwotzf2TBvU7wIqlpVxHpdLdg11YPr5rJdpXinZpP1nvQLKp9GogAYJtXFtp/L2zxzJtC0j75piZDcEW93cO+DHidIcLbftc/wBW1suag=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>MBS &#x3C;地址(可带端口)> [端口(选填)]</span></span>
<span class="line"><span>MJS &#x3C;地址(可带端口)> [端口(选填)]</span></span>
<span class="line"><span>motdbe &#x3C;地址(可带端口)> [端口(选填)]</span></span>
<span class="line"><span>motdje &#x3C;地址(可带端口)> [端口(选填)]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h3>
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
<td>地址</td>
<td>文本</td>
<td>是</td>
<td>要查询的服务器地址</td>
<td>localhost</td>
</tr>
<tr>
<td>端口</td>
<td>数字</td>
<td>否</td>
<td>服务器端口号</td>
<td>25565</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="查询基岩版服务器" tabindex="-1"><a class="header-anchor" href="#查询基岩版服务器"><span>查询基岩版服务器</span></a></h3>
<h4 id="查询-基岩版-服务器" tabindex="-1"><a class="header-anchor" href="#查询-基岩版-服务器"><span>查询 <code v-pre>基岩版</code> 服务器</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">MBS </chat-message>
<chat-message nickname="bot" type="bot">
</chat-message>
</chat-panel>
<h4 id="查询-指定端口-的-基岩版-服务器" tabindex="-1"><a class="header-anchor" href="#查询-指定端口-的-基岩版-服务器"><span>查询 <code v-pre>指定端口</code> 的 <code v-pre>基岩版</code> 服务器</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">MBS  19132</chat-message>
<chat-message nickname="bot" type="bot">
</chat-message>
</chat-panel>
<h3 id="查询-java版-服务器" tabindex="-1"><a class="header-anchor" href="#查询-java版-服务器"><span>查询 <code v-pre>Java版</code> 服务器</span></a></h3>
<h4 id="查询-java版-服务器-1" tabindex="-1"><a class="header-anchor" href="#查询-java版-服务器-1"><span>查询 <code v-pre>Java版</code> 服务器</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">MJS mc233.cn</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/mc服务器查询3.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查询-指定端口-的-java-版服务器" tabindex="-1"><a class="header-anchor" href="#查询-指定端口-的-java-版服务器"><span>查询 <code v-pre>指定端口</code> 的 <code v-pre>Java</code> 版服务器</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">MJS play.simpfun.cn 36877</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/mc服务器查询4.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的版本" tabindex="-1"><a class="header-anchor" href="#支持的版本"><span>支持的版本</span></a></h3>
<ul>
<li><strong>Java Edition</strong>: Java版</li>
<li><strong>Bedrock Edition</strong>: 基岩版</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>地址解析</strong>: 自动解析带有端口的地址</li>
<li><strong>默认端口</strong>:
<ul>
<li>Java版默认端口: 25565</li>
<li>基岩版默认端口: 19132</li>
</ul>
</li>
<li><strong>超时处理</strong>: 可配置的查询超时时间</li>
<li><strong>图片生成</strong>: 自动生成美观的服务器信息图片</li>
</ul>
<h3 id="展示信息" tabindex="-1"><a class="header-anchor" href="#展示信息"><span>展示信息</span></a></h3>
<ul>
<li>服务器favicon图标</li>
<li>服务器版本信息</li>
<li>在线玩家数量</li>
<li>服务器描述信息</li>
<li>延迟(Ping)信息</li>
<li>玩家列表(Java版)</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>权限要求</strong>: 需要权限等级1以上才能使用查询命令</li>
<li><strong>插件依赖</strong>: 需要canvas和database插件支持</li>
<li><strong>配置要求</strong>: 需要在配置中启用对应功能开关</li>
<li><strong>字体设置</strong>: 首次使用需配置默认字体</li>
<li><strong>网络连接</strong>: 需要能访问目标服务器的网络环境</li>
</ol>
<h2 id="配置参数" tabindex="-1"><a class="header-anchor" href="#配置参数"><span>配置参数</span></a></h2>
<p>插件支持丰富的配置选项：</p>
<h3 id="基础配置" tabindex="-1"><a class="header-anchor" href="#基础配置"><span>基础配置</span></a></h3>
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
<td>defaultFont</td>
<td>string</td>
<td>-</td>
<td>默认字体</td>
</tr>
<tr>
<td>enableWhiteList</td>
<td>boolean</td>
<td>false</td>
<td>是否启用白名单功能</td>
</tr>
</tbody>
</table>
<h3 id="java版查询配置" tabindex="-1"><a class="header-anchor" href="#java版查询配置"><span>Java版查询配置</span></a></h3>
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
<td>enabledMotdJe</td>
<td>boolean</td>
<td>false</td>
<td>是否启用MJS指令</td>
</tr>
<tr>
<td>initJeDomainOrIp</td>
<td>string</td>
<td>-</td>
<td>Java版初始地址</td>
</tr>
<tr>
<td>initJePort</td>
<td>number</td>
<td>25565</td>
<td>Java版初始端口</td>
</tr>
<tr>
<td>initJeTimeOut</td>
<td>number</td>
<td>750</td>
<td>Java版查询超时时间(ms)</td>
</tr>
<tr>
<td>isShowJeVersion</td>
<td>boolean</td>
<td>true</td>
<td>是否显示版本信息</td>
</tr>
<tr>
<td>isShowPlayerList</td>
<td>boolean</td>
<td>false</td>
<td>是否显示玩家列表</td>
</tr>
<tr>
<td>isGenuineServer</td>
<td>boolean</td>
<td>false</td>
<td>是否验证正版服务器</td>
</tr>
</tbody>
</table>
<h3 id="基岩版查询配置" tabindex="-1"><a class="header-anchor" href="#基岩版查询配置"><span>基岩版查询配置</span></a></h3>
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
<td>enabledMotdBe</td>
<td>boolean</td>
<td>false</td>
<td>是否启用MBS指令</td>
</tr>
<tr>
<td>initBeDomainOrIp</td>
<td>string</td>
<td>-</td>
<td>基岩版初始地址</td>
</tr>
<tr>
<td>initBePort</td>
<td>number</td>
<td>19132</td>
<td>基岩版初始端口</td>
</tr>
<tr>
<td>initBeTimeOut</td>
<td>number</td>
<td>750</td>
<td>基岩版查询超时时间(ms)</td>
</tr>
<tr>
<td>isShowBeVersion</td>
<td>boolean</td>
<td>true</td>
<td>是否显示版本信息</td>
</tr>
</tbody>
</table>
<h3 id="服务器轮询配置" tabindex="-1"><a class="header-anchor" href="#服务器轮询配置"><span>服务器轮询配置</span></a></h3>
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
<td>enabledMotdServerPolling</td>
<td>boolean</td>
<td>false</td>
<td>是否启用服务器轮询查询</td>
</tr>
<tr>
<td>initServerPollingTime</td>
<td>number</td>
<td>60</td>
<td>服务器轮询时间(s)</td>
</tr>
<tr>
<td>enabledMotdHeartBeat</td>
<td>boolean</td>
<td>false</td>
<td>是否启用机器人保活</td>
</tr>
<tr>
<td>initHeartBeatTime</td>
<td>number</td>
<td>5</td>
<td>保活消息间隔次数</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>MC服务器查询插件可以同时支持Java版和基岩版Minecraft服务器查询，并提供美观的信息展示图片。</p>
</div>
</div></template>


