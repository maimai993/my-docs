<template><div><h1 id="随机表情包" tabindex="-1"><a class="header-anchor" href="#随机表情包"><span>随机表情包</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-emojihub-bili" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-emojihub-bili" alt="" loading="lazy"></a> <a href="https://github.com/koishi-shangxue-plugins/koishi-shangxue-apps/tree/main/plugins/emojihub-bili" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 随机表情包、再来一张、表情包列表</p>
<p><strong>功能描述</strong>: 从43套表情包中随机选择并发送表情图片</p>
<p><strong>插件名称</strong>: emojihub-bili</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kttOwkAQhu95ion3aHwBEzQQEgykEq4aL4pUqdGWQFEvNZ4PBA9ojBqUg4JigMQEDRh8F8Nu61u47C5gC85Fuzvz7T+zM7u4oq0vRKW4DrNzDiAWEo1MGR+8z9Md/SSS4aW4FIvCrKImN6jL4naBKAiomienjEqNHeyZIJDYwCWrEcewgF+LyMsJELv/cbKYS6q6sipblfr0NAGl2IKk47sUOspZqa75edwasaS2CM6A6NOURFTBuT2cbQwL+nh8OOIKiFJEiuly3Kmpcliz5eya2yvKq9qyEk2GnWFlZYSIJyjiq/1Oq2G8tYzW/XDZ9nX/KiFwOqdIj+lGEMgOxr7PHgA3DvBWbaLTPCaqYxTyU8bPkRwEVHla02FtchKl0ma1yijfYOo+juaBAWapgLOnDHMFKOIKcKYALFXn8+Fn8/yvVE+lCGZ9u/uy0uf9ktxeiri9nHkEs9ZC6SszV8bbu+hkl2GeIMU8QY49gfmVQbdZdNs2DvfxZR2nePV2wRInbYLWysrQ+bgh7wgVd4zTvdH3ewZ0kULNDKpvmYWRKi//NJS13dL7ChdjQ2KYfYSvgK/bRrFpqzzk+AXchjza"></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>随机表情包</span></span>
<span class="line"><span>再来一张</span></span>
<span class="line"><span>表情包列表</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="随机表情包-1" tabindex="-1"><a class="header-anchor" href="#随机表情包-1"><span>随机表情包</span></a></h3>
<h4 id="获取随机表情包" tabindex="-1"><a class="header-anchor" href="#获取随机表情包"><span>获取随机表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">随机表情包</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/表情包1.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="再来一张" tabindex="-1"><a class="header-anchor" href="#再来一张"><span>再来一张</span></a></h3>
<h4 id="继续获取同类型表情包" tabindex="-1"><a class="header-anchor" href="#继续获取同类型表情包"><span>继续获取同类型表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">再来一张</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/表情包2.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="表情包列表" tabindex="-1"><a class="header-anchor" href="#表情包列表"><span>表情包列表</span></a></h3>
<h4 id="查看可用表情包" tabindex="-1"><a class="header-anchor" href="#查看可用表情包"><span>查看可用表情包</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">表情包</chat-message>
<chat-message nickname="bot" type="bot">
<p>可用的表情包指令：<br>
随机emojihub表情包<br>
acomu414表情包<br>
ba表情包<br>
capoo表情包<br>
chiikawa表情包<br>
downvote表情包<br>
doro表情包<br>
eveonecat表情包<br>
fufu表情包<br>
girlsbandcry<br>
kemomimi表情包<br>
koishi-meme表情包<br>
mygo表情包<br>
seseren表情包<br>
阿夸表情包<br>
阿尼亚表情包<br>
白圣女表情包<br>
白圣女漫画表情包<br>
败犬女主表情包<br>
柴郡表情包<br>
初音Q版表情包<br>
甘城猫猫表情包<br>
孤独摇滚表情包<br>
狗妈表情包<br>
滑稽表情包<br>
疾旋鼬表情包<br>
卡拉彼丘表情包<br>
流萤表情包<br>
龙图表情包<br>
鹿乃子表情包<br>
玛丽猫表情包<br>
小c表情包<br>
男娘武器库表情包<br>
千恋万花表情包<br>
赛马娘表情包<br>
瑟莉亚表情包<br>
藤田琴音表情包<br>
小黑子表情包<br>
心海表情包<br>
绪山真寻表情包<br>
亚托莉表情包<br>
永雏小菲表情包<br>
宇佐紀表情包</p>
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的图片源" tabindex="-1"><a class="header-anchor" href="#支持的图片源"><span>支持的图片源</span></a></h3>
<ul>
<li><strong>本地文件夹</strong>: 从本地文件系统读取表情包图片</li>
<li><strong>TXT文件</strong>: 通过TXT文件配置表情包路径</li>
<li><strong>网络URL</strong>: 支持从网络URL获取表情包图片</li>
</ul>
<h3 id="自动触发机制" tabindex="-1"><a class="header-anchor" href="#自动触发机制"><span>自动触发机制</span></a></h3>
<ul>
<li><strong>定量消息发送</strong>: 当群聊消息达到一定数量时自动发送表情包</li>
<li><strong>定时发送</strong>: 支持定时自动发送表情包功能</li>
</ul>
<h3 id="显示模式" tabindex="-1"><a class="header-anchor" href="#显示模式"><span>显示模式</span></a></h3>
<ul>
<li><strong>Markdown模式</strong>: 使用Markdown格式显示表情包</li>
<li><strong>按钮模式</strong>: 提供交互式按钮界面</li>
</ul>
<h2 id="表情包管理" tabindex="-1"><a class="header-anchor" href="#表情包管理"><span>表情包管理</span></a></h2>
<h3 id="表情包配置" tabindex="-1"><a class="header-anchor" href="#表情包配置"><span>表情包配置</span></a></h3>
<p>插件支持多种表情包配置方式：</p>
<ol>
<li><strong>本地文件夹</strong>: 将表情包图片放置在指定文件夹中</li>
<li><strong>TXT文件</strong>: 在TXT文件中列出表情包图片路径</li>
<li><strong>网络URL</strong>: 配置网络图片URL作为表情包源</li>
</ol>
<h3 id="图片缓存" tabindex="-1"><a class="header-anchor" href="#图片缓存"><span>图片缓存</span></a></h3>
<ul>
<li><strong>本地缓存</strong>: 自动缓存网络表情包到本地</li>
<li><strong>下载机制</strong>: 支持自动下载网络表情包</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>图片格式</strong>: 支持常见图片格式（JPG、PNG、GIF等）</li>
<li><strong>文件大小</strong>: 表情包图片大小应符合消息传输限制</li>
<li><strong>网络连接</strong>: 使用网络URL时需要稳定的网络连接</li>
<li><strong>存储空间</strong>: 本地表情包需要足够的存储空间</li>
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
<td>emojiPaths</td>
<td>string[]</td>
<td>[]</td>
<td>表情包路径列表</td>
</tr>
<tr>
<td>autoSendCount</td>
<td>number</td>
<td>50</td>
<td>自动发送的消息数量阈值</td>
</tr>
<tr>
<td>autoSendInterval</td>
<td>number</td>
<td>3600</td>
<td>自动发送的时间间隔（秒）</td>
</tr>
<tr>
<td>enableMarkdown</td>
<td>boolean</td>
<td>true</td>
<td>是否启用Markdown模式</td>
</tr>
<tr>
<td>enableButtons</td>
<td>boolean</td>
<td>true</td>
<td>是否启用按钮模式</td>
</tr>
</tbody>
</table>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>随机表情包功能基于emojihub-bili插件实现，提供43套丰富的表情包资源，支持多种触发方式和显示模式，为群聊增添趣味性。</p>
</div>
</div></template>


