<template><div><h1 id="宝可梦集换式卡片查询" tabindex="-1"><a class="header-anchor" href="#宝可梦集换式卡片查询"><span>宝可梦集换式卡片查询</span></a></h1>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-ptcg-research" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-ptcg-research" alt="" loading="lazy"></a> <a href="https://github.com/AsakuraHitomi/ptcg-research" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a></p>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: ptcg</p>
<p><strong>功能描述</strong>: 查询宝可梦集换式卡片游戏(PTCG)的卡片信息，包括宝可梦卡、训练师卡和能量卡</p>
<p><strong>插件名称</strong>: ptcg-research</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kttO8kAQx+95ion3fF98ARPUxBAMUCNXjRcVVsFoS0pRLzWeDw0e0Bg1SAHPBrhCg0TfxXS39S3cdle0UOeind357X9mZ3ZmXllKpiVVg/GJAFBLiFbxjmw/T7kr95PLT8+qUjYN4xk5v+xuebZDIAoCrlfoKeuxwQ5+myDQ2M8WklOBfoGokkJzORCd/z/qTORlLbOAvEpdepiCUjYpaeRSx7uGl3IsyuPeiCe1R3AExIiSyaUzxNgkpVa/YITH+yOhmCilpKyG1KAio2mlJ6dj8cmRMTGrJWeDKsohSU2mfWTiYZFio2jZcfvr7vW7d0lAMDhEm+wuBIGuYODjsAyktU1WG//N9p752hpwoajLRDliQExGw4oGi4ODWC/Y9TqjIj9jj3C0Agywb6ukdMCwUMxFQjHOVIGlMjvlz5Wj31LfKjWwm2vO0yocdUtyWuNCjsO5ayBX13ajgnXD2tni2eJhli4e5tQN2O9FfFEiJ02i89L91G6BlDu4U8D7p9brMSld+pV2B+bLOX1JuLZuHWz6X/Ae8LGO20XcXLWrG34qD390lPXd0/xHLsamxLDeGT4BOXuzam3WB/Pd6JKJwBcXLDdL"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>ptcg [-s 系列] [-l 语言] &#x3C;名称或ID></span></span></code></pre>
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
<td>名称或ID</td>
<td>文本</td>
<td>是</td>
<td>卡片名称或ID</td>
<td>大尾立 / swsh3-136</td>
</tr>
<tr>
<td>系列</td>
<td>文本</td>
<td>否</td>
<td>指定卡片系列</td>
<td>swsh3</td>
</tr>
<tr>
<td>语言</td>
<td>文本</td>
<td>否</td>
<td>查询语言</td>
<td>zh-tw / zh-cn / en / ja</td>
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
<td>serie</td>
<td>-s</td>
<td>string</td>
<td>指定卡片系列</td>
<td>swsh3</td>
</tr>
<tr>
<td>lang</td>
<td>-l</td>
<td>string</td>
<td>指定查询语言</td>
<td>zh-tw</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="名称查询" tabindex="-1"><a class="header-anchor" href="#名称查询"><span>名称查询</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">ptcg 大尾立</chat-message>
<chat-message nickname="bot" type="bot">
<p>查询到大尾立的全部结果：</p>
<ol>
<li>大尾立 [SV9-077]</li>
<li>大尾立 [SC2b-105]</li>
<li>大尾立 [SC2D-118]<br>
第 1 页 / 共 1 页<br>
请at并发送数字选择卡片, 或at并发送&quot;跳页 页码&quot;切换页面</li>
</ol>
</chat-message>
<chat-message nickname="用户" type="user">1</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/实用工具/宝可梦.webp" alt="" loading="lazy"><br>
大尾立<br>
HP：120  屬性：[無]<br>
階段：Stage1<br>
•抓  [無]<br>
40<br>
•噴射頭擊  [無][無]<br>
70<br>
弱點：[鬥] ×2   撤退：1<br>
卡標: I  稀有度: Common<br>
所屬系列: 對戰搭檔 (SV9)<br>
ID: SV9-077</p>
</chat-message>
</chat-panel>
<h3 id="id精确查询" tabindex="-1"><a class="header-anchor" href="#id精确查询"><span>ID精确查询</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">ptcg SV9-077</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/实用工具/宝可梦.webp" alt="" loading="lazy"><br>
大尾立<br>
HP：120  屬性：[無]<br>
階段：Stage1<br>
•抓  [無]<br>
40<br>
•噴射頭擊  [無][無]<br>
70<br>
弱點：[鬥] ×2   撤退：1<br>
卡標: I  稀有度: Common<br>
所屬系列: 對戰搭檔 (SV9)<br>
ID: SV9-077</p>
</chat-message>
</chat-panel>
<h3 id="指定系列查询" tabindex="-1"><a class="header-anchor" href="#指定系列查询"><span>指定系列查询</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">ptcg -s SV9 大尾立</chat-message>
<chat-message nickname="bot" type="bot">
<p><img src="@source/使用指南/实用工具/宝可梦.webp" alt="" loading="lazy"><br>
大尾立<br>
HP：120  屬性：[無]<br>
階段：Stage1<br>
•抓  [無]<br>
40<br>
•噴射頭擊  [無][無]<br>
70<br>
弱點：[鬥] ×2   撤退：1<br>
卡標: I  稀有度: Common<br>
所屬系列: 對戰搭檔 (SV9)<br>
ID: SV9-077</p>
</chat-message>
</chat-panel>
<h3 id="多结果分页查询" tabindex="-1"><a class="header-anchor" href="#多结果分页查询"><span>多结果分页查询</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">ptcg 皮卡丘</chat-message>
<chat-message nickname="bot" type="bot">
<p>查询到皮卡丘的全部结果：</p>
<ol>
<li>皮卡丘V [SN-001]</li>
<li>皮卡丘 [SV-P-001]</li>
<li>皮卡丘V [SDP-001]</li>
<li>皮卡丘 [S8a-001]</li>
<li>皮卡丘ex [SVC-001]</li>
<li>皮卡丘 [S10a-014]</li>
<li>皮卡丘 [SV2D-017]</li>
<li>皮卡丘V [SH-019]</li>
<li>皮卡丘V [S8a-020]</li>
<li>衝浪皮卡丘V [S8a-021]<br>
第 1 页 / 共 5 页<br>
请at并发送数字选择卡片, 或at并发送&quot;跳页 页码&quot;切换页面</li>
</ol>
</chat-message>
</chat-panel>
<h2 id="卡片类型说明" tabindex="-1"><a class="header-anchor" href="#卡片类型说明"><span>卡片类型说明</span></a></h2>
<h3 id="宝可梦卡" tabindex="-1"><a class="header-anchor" href="#宝可梦卡"><span>宝可梦卡</span></a></h3>
<ul>
<li><strong>HP</strong>: 生命值</li>
<li><strong>属性</strong>: 卡片属性（无、草、水、火、斗、超、恶、钢、妖、电、龙）</li>
<li><strong>阶段</strong>: 进化阶段（基础、1、2）</li>
<li><strong>特性</strong>: 宝可梦的特殊能力</li>
<li><strong>招式</strong>: 攻击招式的名称、属性和效果</li>
<li><strong>弱点</strong>: 受到特定属性攻击时的伤害倍率</li>
<li><strong>抵抗力</strong>: 对特定属性攻击的伤害减免</li>
<li><strong>撤退</strong>: 撤退所需的能量数量</li>
</ul>
<h3 id="训练师卡" tabindex="-1"><a class="header-anchor" href="#训练师卡"><span>训练师卡</span></a></h3>
<ul>
<li><strong>类型</strong>: 训练师卡的类型（物品、支援者、竞技场等）</li>
<li><strong>效果</strong>: 卡片的效果描述</li>
</ul>
<h3 id="能量卡" tabindex="-1"><a class="header-anchor" href="#能量卡"><span>能量卡</span></a></h3>
<ul>
<li><strong>类型</strong>: 能量类型</li>
<li><strong>效果</strong>: 特殊能量卡的效果</li>
</ul>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="查询功能" tabindex="-1"><a class="header-anchor" href="#查询功能"><span>查询功能</span></a></h3>
<ul>
<li><strong>模糊查询</strong>: 支持卡片名称的模糊匹配</li>
<li><strong>精确查询</strong>: 支持卡片ID的精确查询</li>
<li><strong>系列筛选</strong>: 支持按卡片系列筛选结果</li>
<li><strong>多语言支持</strong>: 支持中文繁体、中文简体、英文、日文</li>
</ul>
<h3 id="名称映射" tabindex="-1"><a class="header-anchor" href="#名称映射"><span>名称映射</span></a></h3>
<ul>
<li><strong>简繁转换</strong>: 自动处理简体中文和繁体中文的转换</li>
<li><strong>自定义映射</strong>: 支持自定义名称映射规则</li>
<li><strong>智能回退</strong>: 当查询失败时自动尝试其他语言版本</li>
</ul>
<h3 id="分页系统" tabindex="-1"><a class="header-anchor" href="#分页系统"><span>分页系统</span></a></h3>
<ul>
<li><strong>结果分页</strong>: 当查询结果过多时自动分页显示</li>
<li><strong>交互选择</strong>: 支持通过数字选择具体卡片</li>
<li><strong>页面跳转</strong>: 支持跳转到指定页面</li>
</ul>
<h2 id="名称映射管理" tabindex="-1"><a class="header-anchor" href="#名称映射管理"><span>名称映射管理</span></a></h2>
<h3 id="管理指令" tabindex="-1"><a class="header-anchor" href="#管理指令"><span>管理指令</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>rptfg &#x3C;操作> [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="操作说明" tabindex="-1"><a class="header-anchor" href="#操作说明"><span>操作说明</span></a></h3>
<table>
<thead>
<tr>
<th>操作</th>
<th>参数</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>add</td>
<td>源名称:目标名称</td>
<td>添加名称映射</td>
<td>rptfg add 乌栗:烏栗</td>
</tr>
<tr>
<td>delete</td>
<td>源名称:目标名称</td>
<td>删除名称映射</td>
<td>rptfg delete 乌栗:烏栗</td>
</tr>
<tr>
<td>reload</td>
<td>无</td>
<td>重新加载映射配置</td>
<td>rptfg reload</td>
</tr>
<tr>
<td>list</td>
<td>无</td>
<td>列出所有映射规则</td>
<td>rptfg list</td>
</tr>
</tbody>
</table>
<h2 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h2>
<h3 id="查询错误" tabindex="-1"><a class="header-anchor" href="#查询错误"><span>查询错误</span></a></h3>
<ul>
<li><strong>未找到卡片</strong>: 当没有匹配的卡片时提示</li>
<li><strong>网络错误</strong>: 当API请求失败时提示重试</li>
<li><strong>超时错误</strong>: 当查询超时时提示稍后重试</li>
</ul>
<h3 id="输入错误" tabindex="-1"><a class="header-anchor" href="#输入错误"><span>输入错误</span></a></h3>
<ul>
<li><strong>缺少参数</strong>: 当未提供查询内容时显示帮助信息</li>
<li><strong>无效操作</strong>: 当名称映射操作无效时提示</li>
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
<td>itemsPerPage</td>
<td>number</td>
<td>10</td>
<td>每页显示的结果数量</td>
</tr>
<tr>
<td>dataPath</td>
<td>string</td>
<td>&quot;./ptcg-data&quot;</td>
<td>数据存储路径</td>
</tr>
<tr>
<td>requestConcurrency</td>
<td>number</td>
<td>3</td>
<td>最大并发请求数</td>
</tr>
<tr>
<td>retryCount</td>
<td>number</td>
<td>2</td>
<td>请求重试次数</td>
</tr>
<tr>
<td>sessionTimeout</td>
<td>number</td>
<td>60000</td>
<td>会话超时时间（毫秒）</td>
</tr>
<tr>
<td>enableReplace</td>
<td>boolean</td>
<td>true</td>
<td>是否启用名称映射功能</td>
</tr>
<tr>
<td>replaceConfigPath</td>
<td>string</td>
<td>&quot;./ptcg.json&quot;</td>
<td>名称映射配置文件路径</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>数据来源</strong>: 卡片数据来源于TCGDex API，可能存在更新延迟</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问API服务</li>
<li><strong>图片加载</strong>: 卡片图片可能因网络问题无法正常显示</li>
<li><strong>语言支持</strong>: 不同语言的卡片数据完整度可能不同</li>
<li><strong>名称差异</strong>: 不同语言版本的卡片名称可能存在差异</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>宝可梦集换式卡片游戏(PTCG)是一款基于宝可梦系列的集换式卡牌游戏，玩家通过收集和组合不同的卡片来构建卡组，与其他玩家进行对战。</p>
</div>
</div></template>


