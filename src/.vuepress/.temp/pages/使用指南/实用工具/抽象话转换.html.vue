<template><div><h1 id="抽象话转换" tabindex="-1"><a class="header-anchor" href="#抽象话转换"><span>抽象话转换</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-chouxianghua" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-chouxianghua" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/chouxianghua" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: <code v-pre>抽象话</code> <code v-pre>还原抽象话</code></p>
<p><strong>功能描述</strong>: 将中文转换为emoji抽象话，或将抽象话还原为拼音</p>
<p><strong>插件名称</strong>: chouxianghua</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx9kl1vEkEUhu/5FSe9R9N704Rir2ih24SEZuPFAmt3G7tDYFfrnU0/bGw21BabRgnypUVLYBOTaqDqfzHM7PZfOMwMlAH0XOzuzHnmnXfPOU+foRcZQ8vbsLoRAhpJ1S+1yPH3J2zFHgUnvZXXcgasmpazy7ak7QioioI7dXrKv+7yg6NQFJq739KtbGhWII6y+nYB1OH7Af3YcCzb3NFlpTG9TEEtl9FsUnbxm5pMDSMu8nJGuloSjIIaQ2bBMEntiFRuZgVjIj+biSRULavlbD0fRpaeRlN3DiOaUjMGcnZNzdoyHG3W1P9r8xhUUm7jskfeecTtkIvXg/6UxfVNNWdaL02L1g5Zj9L5JXJye/fxG7msYu9AZlfWVH0HbZtjNKi1yP7hNDryNfaUhHB4iXaTLRSFrmDhz9sqkJtjstd9OOidUFsLDIozJi6QGiQsfRnZ8HxxEbvFoNPhVOx+vmICrQMHgqsGqZxyLJJgSCQhmAbwqwa31btXZ5NSI5UmBN4+neHJopPi2dheNMXwaErwnyDo9nHxQtSMVZmT65sy+VmQomQT5MqaTF5B8LuEP1SCn23i1v3+OamU53ltweDHezrDuHngnx7N/+MvgM9d3Cthby9oHM5T+fqPEvNGSN24FmK8bRybbmobyOUvv9mbtJ0M/QWrF2/1"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>抽象话 &#x3C;text:text></span></span>
<span class="line"><span>还原抽象话 &#x3C;text:text></span></span></code></pre>
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
<td>text</td>
<td>文本</td>
<td>是</td>
<td>要转换或还原的内容</td>
<td>需要被抽象的话语</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="转换为抽象话" tabindex="-1"><a class="header-anchor" href="#转换为抽象话"><span>转换为抽象话</span></a></h3>
<h4 id="将普通文本转换为抽象话" tabindex="-1"><a class="header-anchor" href="#将普通文本转换为抽象话"><span>将普通文本转换为抽象话</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">抽象话 需要被抽象的话语</chat-message>
<chat-message nickname="bot" type="bot">
‍⏭💊被🤡🐘💦🌸语
</chat-message>
</chat-panel>
<h4 id="将中文句子转换为抽象话" tabindex="-1"><a class="header-anchor" href="#将中文句子转换为抽象话"><span>将中文句子转换为抽象话</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">抽象话 真的太抽象啦</chat-message>
<chat-message nickname="bot" type="bot">
💉💦太🤡🐘🌶！
</chat-message>
</chat-panel>
<h3 id="还原抽象话" tabindex="-1"><a class="header-anchor" href="#还原抽象话"><span>还原抽象话</span></a></h3>
<h4 id="将抽象话还原为拼音" tabindex="-1"><a class="header-anchor" href="#将抽象话还原为拼音"><span>将抽象话还原为拼音</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">还原抽象话 ‍⏭💊被🤡🐘💦🌸语</chat-message>
<chat-message nickname="bot" type="bot">
‍-⏭-yao-被-chou-xiang-di/shui-hua-语
</chat-message>
</chat-panel>
<h4 id="将复杂抽象话还原为拼音" tabindex="-1"><a class="header-anchor" href="#将复杂抽象话还原为拼音"><span>将复杂抽象话还原为拼音</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">还原抽象话 💉💦太🤡🐘🌶！</chat-message>
<chat-message nickname="bot" type="bot">
zhen-di/shui-太-chou-xiang-na/la-！
</chat-message>
</chat-panel>
<h3 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h3>
<h4 id="空输入处理" tabindex="-1"><a class="header-anchor" href="#空输入处理"><span>空输入处理</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">抽象话</chat-message>
<chat-message nickname="bot" type="bot">
请输入需要转换的内容。
</chat-message>
</chat-panel>
<h4 id="还原空输入处理" tabindex="-1"><a class="header-anchor" href="#还原空输入处理"><span>还原空输入处理</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">还原抽象话</chat-message>
<chat-message nickname="bot" type="bot">
请输入需要还原的抽象话。
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="转换逻辑" tabindex="-1"><a class="header-anchor" href="#转换逻辑"><span>转换逻辑</span></a></h3>
<ul>
<li><strong>拼音映射</strong>: 基于pinyin.json文件将中文字符转换为拼音</li>
<li><strong>表情映射</strong>: 基于emoji.json文件将拼音转换为对应的emoji表情</li>
<li><strong>字符保留</strong>: 无法映射的字符保持原样输出</li>
</ul>
<h3 id="还原逻辑" tabindex="-1"><a class="header-anchor" href="#还原逻辑"><span>还原逻辑</span></a></h3>
<ul>
<li><strong>表情识别</strong>: 识别emoji表情对应的拼音</li>
<li><strong>多音字处理</strong>: 支持一个emoji对应多个拼音的情况</li>
<li><strong>拼音分隔</strong>: 使用连字符分隔各个拼音</li>
</ul>
<h3 id="数据源" tabindex="-1"><a class="header-anchor" href="#数据源"><span>数据源</span></a></h3>
<ul>
<li><strong>拼音数据</strong>: 包含中文字符到拼音的映射关系</li>
<li><strong>表情数据</strong>: 包含拼音到emoji表情的映射关系</li>
</ul>
<h3 id="错误处理-1" tabindex="-1"><a class="header-anchor" href="#错误处理-1"><span>错误处理</span></a></h3>
<ul>
<li><strong>空输入检测</strong>: 检测用户是否输入了内容</li>
<li><strong>字符保留</strong>: 无法处理的字符保持原样</li>
<li><strong>多音字支持</strong>: 支持一个emoji对应多个拼音的情况</li>
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
<td>commandname</td>
<td>string</td>
<td>抽象话</td>
<td>抽象话转换命令名称</td>
</tr>
<tr>
<td>commandname2</td>
<td>string</td>
<td>还原抽象话</td>
<td>还原抽象话命令名称</td>
</tr>
<tr>
<td>loggerinfo</td>
<td>boolean</td>
<td>true</td>
<td>日志调试模式</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>字符覆盖</strong>: 插件主要支持常用中文字符的转换，特殊字符可能无法正确转换</li>
<li><strong>表情识别</strong>: 还原功能依赖于emoji表情的识别，某些复杂表情可能无法正确还原</li>
<li><strong>多音字</strong>: 中文多音字可能无法准确还原为原始拼音</li>
<li><strong>数据更新</strong>: 拼音和表情映射数据固定，不支持动态更新</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>抽象话转换功能基于本地拼音和表情映射数据实现，能够将中文转换为有趣的emoji抽象话，或将抽象话还原为拼音形式，适合娱乐和趣味交流使用。</p>
</div>
</div></template>


