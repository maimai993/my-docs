<template><div><h1 id="合并转发功能" tabindex="-1"><a class="header-anchor" href="#合并转发功能"><span>合并转发功能</span></a></h1>
<p>合并转发功能允许您将多条消息合并为一个转发卡片，点击后可以查看完整的消息对话。</p>
<h2 id="功能特点" tabindex="-1"><a class="header-anchor" href="#功能特点"><span>功能特点</span></a></h2>
<ul>
<li>📨 <strong>合并显示</strong> - 将多条消息合并为一个转发卡片</li>
<li>👆 <strong>点击查看</strong> - 点击转发卡片弹出完整对话界面</li>
<li>� <strong>复制内容</strong> - 支持一键复制所有消息内容</li>
<li>📱 <strong>响应式设计</strong> - 适配桌面和移动设备</li>
</ul>
<h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本用法" tabindex="-1"><a class="header-anchor" href="#基本用法"><span>基本用法</span></a></h3>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"用户名"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"user"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;MergeForward :messages="[</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { nickname: '用户A', type: 'user', content: '你好，今天天气不错' },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { nickname: '用户B', type: 'user', content: '是的，适合出去走走' },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { nickname: '用户C', type: 'user', content: '大家有什么计划吗？' }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">]" /></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="完整示例" tabindex="-1"><a class="header-anchor" href="#完整示例"><span>完整示例</span></a></h3>
<ChatPanel>
<ChatMessage nickname="用户A" type="user">
今天讨论一下项目进度
</ChatMessage>
<ChatMessage nickname="用户B" type="user">
我这边前端部分已经完成了
</ChatMessage>
<ChatMessage nickname="用户C" type="user">
后端API也开发完毕，可以联调了
</ChatMessage>
<ChatMessage nickname="用户D" type="user">
测试环境已经部署好了
</ChatMessage>
</ChatPanel>
<h3 id="带不同类型消息的示例" tabindex="-1"><a class="header-anchor" href="#带不同类型消息的示例"><span>带不同类型消息的示例</span></a></h3>
<ChatPanel>
<ChatMessage nickname="系统提示" type="system">
以下是群聊中的重要讨论
</ChatMessage>
<ChatMessage nickname="小助手" type="bot">
大家好，我是群聊助手
</ChatMessage>
<ChatMessage nickname="张三" type="user">
今天会议的主要内容是什么？
</ChatMessage>
<ChatMessage nickname="李四" type="user">
讨论项目进度和下周计划
</ChatMessage>
<MergeForward :messages="[
  { nickname: '小助手', type: 'bot', content: '大家好，我是群聊助手' },
  { nickname: '张三', type: 'user', content: '今天会议的主要内容是什么？' },
  { nickname: '李四', type: 'user', content: '讨论项目进度和下周计划' },
  { nickname: '王五', type: 'user', content: '我建议每周五下午开进度会' },
  { nickname: '赵六', type: 'user', content: '同意，这样能及时同步进度' }
]" />
</ChatPanel>
<h2 id="参数说明" tabindex="-1"><a class="header-anchor" href="#参数说明"><span>参数说明</span></a></h2>
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>默认值</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>messages</td>
<td>Array</td>
<td>[]</td>
<td>消息数组，包含nickname、type、content</td>
</tr>
<tr>
<td>maxPreview</td>
<td>Number</td>
<td>3</td>
<td>预览显示的最大消息数量</td>
</tr>
</tbody>
</table>
<h2 id="消息格式" tabindex="-1"><a class="header-anchor" href="#消息格式"><span>消息格式</span></a></h2>
<p>每条消息应该包含以下字段：</p>
<div class="language-javascript line-numbers-mode" data-highlighter="shiki" data-ext="javascript" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-javascript"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">{</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#E06C75">  nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'用户名'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">,  </span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 必需，显示的用户名</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#E06C75">  type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'user'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">,       </span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">// 必需，消息类型：'user'、'bot'、'system'</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#E06C75">  content</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'消息内容'</span><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">  // 必需，消息文本内容</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">}</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="交互功能" tabindex="-1"><a class="header-anchor" href="#交互功能"><span>交互功能</span></a></h2>
<ol>
<li><strong>点击转发卡片</strong> - 弹出完整的消息对话界面</li>
<li><strong>复制内容</strong> - 点击&quot;复制内容&quot;按钮将所有消息文本复制到剪贴板</li>
<li><strong>关闭对话框</strong> - 点击&quot;关闭&quot;按钮或点击对话框外部关闭</li>
</ol>
<h2 id="使用场景" tabindex="-1"><a class="header-anchor" href="#使用场景"><span>使用场景</span></a></h2>
<ul>
<li>群聊重要讨论的汇总</li>
<li>项目进度的阶段性总结</li>
<li>重要通知的转发</li>
<li>会议记录的整理</li>
</ul>
<p>这个功能特别适合在文档中展示群聊对话的精华部分，让读者能够快速了解讨论内容，同时保持页面的整洁性。</p>
</div></template>


