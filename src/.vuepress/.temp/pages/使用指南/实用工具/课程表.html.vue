<template><div><h1 id="课程表" tabindex="-1"><a class="header-anchor" href="#课程表"><span>课程表</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-curriculum-table" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-curriculum-table" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/curriculum-table" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 群友课表</p>
<p><strong>功能描述</strong>: 管理群组课程表，支持手动添加课程、WakeUp课程表导入、课程表图片渲染和定时推送功能</p>
<p><strong>插件名称</strong>: curriculum-table</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstO6kAYx/c8xRf3nBNf4CSAOwxYQ1fNWRSYc+gJtk1pjy41XmI0jRcwMWpQBBUvAeICDd7exXSm9S1sO7U6LX6Ldma+3/znu/2pKvOliqjpMD2bANd4wW50yfrdb3/nf2pG8a8mqhWYlmRjwT9ijlMgcBzunbq37Os+vfhhHOf6Po+QXE7EBXJKGf2rgeD9f7iLWUPWpTnEKoV02gVFtSTq5MjEGy2W8iwX+FkP8zQjmAEhq0i1ikRaa6Q5jAtmA3/ck8oLYllUdaQlFRkVlcibnmUKQsnQNKlkVI25pC4Wq5HEPJtKC2RvQMweHtXj3hleUA1VRTpCWjyp6DpMlIdk8pfbAX/Dce4OJl53ToAM18lS/6c12rQehhM+lPOZXIC0IC+jtKLD/8lJbG45vR6lsp8zkQ3QU6CAc9EmzW2KpfI+ksoHTBvoU9bjydvi7lepD5UOOINlb+62dsOQMgUfyRQC5gzCCpG6aT0dUWwqzWLn4PSf7e6m0+qS+1tyXKfYDM9iF+C8NPBhM4THhdUF6/7AHTHcWbG318Yndwm4buJRAw+WnPbqOJWrb6pJa84U/joQox2iWLR/N0D2n+3OKBI5n3gHYExCtw=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>群友课表.操作 [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="指令说明" tabindex="-1"><a class="header-anchor" href="#指令说明"><span>指令说明</span></a></h3>
<table>
<thead>
<tr>
<th>指令</th>
<th>功能</th>
<th>语法</th>
<th>参数说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>添加课程</td>
<td>手动添加课程</td>
<td><code v-pre>群友课表.添加 &lt;星期几&gt; &lt;课程名称&gt; &lt;上课时间-下课时间&gt;</code></td>
<td>星期几：支持&quot;周一&quot;、&quot;周二&quot;...&quot;周日&quot;，也支持&quot;周一周三&quot;格式<br>课程名称：课程的名称<br>上课时间-下课时间：24小时制，如&quot;8:00-9:30&quot;</td>
</tr>
<tr>
<td>WakeUp导入</td>
<td>从WakeUp课程表导入</td>
<td><code v-pre>群友课表.wakeup &lt;WakeUp分享文本&gt;</code></td>
<td>WakeUp分享文本：从WakeUp课程表应用中复制的分享文本（包含分享口令）</td>
</tr>
<tr>
<td>查看课程表</td>
<td>查看当前课程表</td>
<td><code v-pre>群友课表.看看 [日期]</code></td>
<td>日期：可选，支持数字（0=今天，1=明天，-1=昨天）或&quot;今天&quot;、&quot;明天&quot;、&quot;昨天&quot;等</td>
</tr>
<tr>
<td>移除课程</td>
<td>移除已添加课程</td>
<td><code v-pre>群友课表.移除</code></td>
<td>无参数，会列出课程供选择移除</td>
</tr>
<tr>
<td>课程去重</td>
<td>自动移除重复课程</td>
<td><code v-pre>群友课表.去重</code></td>
<td>无参数，自动检测并移除重复课程</td>
</tr>
</tbody>
</table>
<h3 id="可选参数" tabindex="-1"><a class="header-anchor" href="#可选参数"><span>可选参数</span></a></h3>
<table>
<thead>
<tr>
<th>参数</th>
<th>简写</th>
<th>说明</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td>userid</td>
<td>-i</td>
<td>指定用户ID (QQ号)</td>
<td><code v-pre>-i 114514</code></td>
</tr>
<tr>
<td>username</td>
<td>-n</td>
<td>指定用户的名称</td>
<td><code v-pre>-n 上学大人</code></td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="手动添加课程" tabindex="-1"><a class="header-anchor" href="#手动添加课程"><span>手动添加课程</span></a></h3>
<h4 id="添加单节课程" tabindex="-1"><a class="header-anchor" href="#添加单节课程"><span>添加单节课程</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.添加 周一周三 高等数学 8:00-9:30</chat-message>
<chat-message nickname="bot" type="bot">
已为 用户 添加课程：高等数学 周一,周三 8:00-9:30
</chat-message>
</chat-panel>
<h4 id="添加多节课程-指定用户" tabindex="-1"><a class="header-anchor" href="#添加多节课程-指定用户"><span>添加多节课程（指定用户）</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.添加 周四周五 9:55-12:15 大学英语 -i 114514 -n 上学大人</chat-message>
<chat-message nickname="bot" type="bot">
已为 上学大人 添加课程：大学英语 周四,周五 9:55-12:15
</chat-message>
</chat-panel>
<h3 id="wakeup课程表导入" tabindex="-1"><a class="header-anchor" href="#wakeup课程表导入"><span>WakeUp课程表导入</span></a></h3>
<h4 id="导入wakeup课程表" tabindex="-1"><a class="header-anchor" href="#导入wakeup课程表"><span>导入WakeUp课程表</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.wakeup 这是来自「WakeUp课程表」的课表分享......分享口令为「PaJ_8Kj_zeelspJs2HBL1」</chat-message>
<chat-message nickname="bot" type="bot">
已成功导入来自WakeUp的课程表，共导入 8 门课程：
课程名称：高等数学， 周一， 8:00-9:30
课程名称：大学英语， 周二， 10:00-11:30
...
</chat-message>
</chat-panel>
<h3 id="查看课程表" tabindex="-1"><a class="header-anchor" href="#查看课程表"><span>查看课程表</span></a></h3>
<h4 id="查看今日课程表" tabindex="-1"><a class="header-anchor" href="#查看今日课程表"><span>查看今日课程表</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.看看</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/课程表.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查看明日课程表" tabindex="-1"><a class="header-anchor" href="#查看明日课程表"><span>查看明日课程表</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.看看 1</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/课程表.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h4 id="查看昨天课程表" tabindex="-1"><a class="header-anchor" href="#查看昨天课程表"><span>查看昨天课程表</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.看看 -1</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/实用工具/课程表.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="课程移除" tabindex="-1"><a class="header-anchor" href="#课程移除"><span>课程移除</span></a></h3>
<h4 id="移除指定课程" tabindex="-1"><a class="header-anchor" href="#移除指定课程"><span>移除指定课程</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.移除</chat-message>
<chat-message nickname="bot" type="bot">
<p>你目前在本群的课程有：</p>
<ol>
<li>高等数学 周一,周三 8:00-9:30<br>
请选择要移除的课程序号 (输入数字):</li>
</ol>
</chat-message>
<chat-message nickname="用户" type="user">1</chat-message>
<chat-message nickname="bot" type="bot">
已删除课程：高等数学 周一,周三 8:00-9:30
</chat-message>
</chat-panel>
<h3 id="课程去重" tabindex="-1"><a class="header-anchor" href="#课程去重"><span>课程去重</span></a></h3>
<h4 id="自动移除重复课程" tabindex="-1"><a class="header-anchor" href="#自动移除重复课程"><span>自动移除重复课程</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">群友课表.去重</chat-message>
<chat-message nickname="bot" type="bot">
已成功移除 2 门重复的课程。
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="课程管理功能" tabindex="-1"><a class="header-anchor" href="#课程管理功能"><span>课程管理功能</span></a></h3>
<ul>
<li><strong>手动添加</strong>: 支持手动输入课程信息，智能参数识别</li>
<li><strong>WakeUp导入</strong>: 支持从WakeUp课程表平台导入，自动解析分享口令</li>
<li><strong>课程去重</strong>: 自动检测并避免重复课程</li>
<li><strong>课程移除</strong>: 交互式选择移除课程</li>
<li><strong>多用户支持</strong>: 支持为不同用户添加课程</li>
</ul>
<h3 id="课程表渲染" tabindex="-1"><a class="header-anchor" href="#课程表渲染"><span>课程表渲染</span></a></h3>
<ul>
<li><strong>图片生成</strong>: 使用Puppeteer生成美观的课程表图片</li>
<li><strong>HTML模板</strong>: 基于HTML模板渲染课程表，支持自定义字体</li>
<li><strong>状态显示</strong>: 实时显示课程状态（进行中、下一节、无课程）</li>
<li><strong>时间计算</strong>: 自动计算距离上课/下课时间</li>
</ul>
<h3 id="定时推送" tabindex="-1"><a class="header-anchor" href="#定时推送"><span>定时推送</span></a></h3>
<ul>
<li><strong>配置驱动</strong>: 通过插件配置设置定时推送</li>
<li><strong>多群组支持</strong>: 支持为不同群组设置不同的推送时间</li>
<li><strong>智能过滤</strong>: 只推送当前日期有效的课程</li>
</ul>
<h3 id="数据存储" tabindex="-1"><a class="header-anchor" href="#数据存储"><span>数据存储</span></a></h3>
<ul>
<li><strong>数据库持久化</strong>: 使用Koishi数据库存储课程数据</li>
<li><strong>用户隔离</strong>: 每个用户的课程表数据独立存储</li>
<li><strong>课程有效期</strong>: 支持设置课程的开始和结束日期</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>WakeUp导入</strong>: 需要有效的WakeUp课程表分享文本（包含分享口令）</li>
<li><strong>时间格式</strong>: 手动添加课程时使用24小时制时间格式（如&quot;8:00-9:30&quot;）</li>
<li><strong>星期格式</strong>: 支持&quot;周一&quot;、&quot;周二&quot;...&quot;周日&quot;，也支持&quot;周一周三&quot;格式</li>
<li><strong>定时推送</strong>: 需要开启cron服务并正确配置推送设置</li>
<li><strong>字体支持</strong>: 需要安装方正像素12字体或配置自定义字体路径</li>
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
<td>command</td>
<td>string</td>
<td>&quot;群友课表&quot;</td>
<td>父级指令名称</td>
</tr>
<tr>
<td>command11</td>
<td>string</td>
<td>&quot;添加&quot;</td>
<td>添加课程的指令名称</td>
</tr>
<tr>
<td>command12</td>
<td>string</td>
<td>&quot;移除&quot;</td>
<td>移除课程的指令名称</td>
</tr>
<tr>
<td>command13</td>
<td>string</td>
<td>&quot;wakeup&quot;</td>
<td>WakeUp导入的指令名称</td>
</tr>
<tr>
<td>command14</td>
<td>string</td>
<td>&quot;去重&quot;</td>
<td>课程去重的指令名称</td>
</tr>
<tr>
<td>command21</td>
<td>string</td>
<td>&quot;看看&quot;</td>
<td>查看课程表的指令名称</td>
</tr>
<tr>
<td>waittimeout</td>
<td>number</td>
<td>30</td>
<td>等待用户交互的超时时间（秒）</td>
</tr>
<tr>
<td>autocommand14</td>
<td>boolean</td>
<td>true</td>
<td>添加课程时自动执行课程去重</td>
</tr>
<tr>
<td>cronPush</td>
<td>boolean</td>
<td>false</td>
<td>是否开启自动推送功能（需要cron服务）</td>
</tr>
<tr>
<td>screenshotquality</td>
<td>number</td>
<td>60</td>
<td>图片压缩质量（0-100%）</td>
</tr>
<tr>
<td>backgroundcolor</td>
<td>string</td>
<td>&quot;rgba(234, 228, 225, 1)&quot;</td>
<td>课表背景颜色</td>
</tr>
<tr>
<td>customFontPath</td>
<td>string</td>
<td>字体路径</td>
<td>自定义字体文件路径</td>
</tr>
<tr>
<td>footertext</td>
<td>string</td>
<td>&quot;输入 群友课程表 以查看指令帮助...&quot;</td>
<td>页脚描述文字</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>课程表插件提供了完整的课程管理解决方案，支持多种课程添加方式和灵活的定时推送功能，能够满足学生用户的日常课程管理需求。</p>
</div>
</div></template>


