<template><div><h1 id="vuepress-组件示例展示" tabindex="-1"><a class="header-anchor" href="#vuepress-组件示例展示"><span>VuePress 组件示例展示</span></a></h1>
<p>本页面展示了项目中所有 Vue 组件的使用示例。</p>
<h2 id="组件列表" tabindex="-1"><a class="header-anchor" href="#组件列表"><span>组件列表</span></a></h2>
<h3 id="_1-chatmessage-聊天消息组件" tabindex="-1"><a class="header-anchor" href="#_1-chatmessage-聊天消息组件"><span>1. ChatMessage - 聊天消息组件</span></a></h3>
<p>用于显示聊天消息，支持用户、机器人和系统三种类型。</p>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"用户"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"user"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  这是一条用户消息</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"机器人"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"bot"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  这是一条机器人回复</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"系统"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"system"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  这是一条系统提示消息</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>实际效果：</strong></p>
<ChatMessage nickname="用户" type="user">
  你好，这是一个用户消息示例！
</ChatMessage>
<ChatMessage nickname="机器人" type="bot">
  你好！我是机器人，很高兴为您服务。
</ChatMessage>
<ChatMessage nickname="系统" type="system">
  系统提示：消息已发送成功
</ChatMessage>
<h3 id="_2-recallmessage-消息撤回组件" tabindex="-1"><a class="header-anchor" href="#_2-recallmessage-消息撤回组件"><span>2. RecallMessage - 消息撤回组件</span></a></h3>
<p>模拟消息撤回效果，3秒后显示撤回样式。</p>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">RecallMessage</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> nickname</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"用户"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66"> type</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"user"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  这条消息将在3秒后显示撤回效果</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">RecallMessage</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>实际效果：</strong></p>
<RecallMessage nickname="用户" type="user">
  这条消息将在3秒后显示撤回效果
</RecallMessage>
<h3 id="_3-simpleimagemessage-简单图片消息组件" tabindex="-1"><a class="header-anchor" href="#_3-simpleimagemessage-简单图片消息组件"><span>3. SimpleImageMessage - 简单图片消息组件</span></a></h3>
<p>用于显示图片消息，支持加载状态和错误处理。</p>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">SimpleImageMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  imageSrc</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"/logotxt.png"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  imageAlt</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"示例图片"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  text</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"这是一张示例图片"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">  caption</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"图片说明文字"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">/></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>实际效果：</strong></p>
<SimpleImageMessage
  imageSrc="/logo.png"
  imageAlt="示例图片"
  text="这是一张示例图片"
  caption="图片说明文字"
/>
<h3 id="_4-mergeforward-合并转发组件" tabindex="-1"><a class="header-anchor" href="#_4-mergeforward-合并转发组件"><span>4. MergeForward - 合并转发组件</span></a></h3>
<p>模拟聊天记录合并转发效果，点击可查看完整转发内容。</p>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">MergeForward</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">messages</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">[</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">nickname</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '用户A'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">, </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">content</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '第一条消息内容'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">nickname</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '用户B'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">, </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">content</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '第二条消息内容，这是一条比较长的消息，用于测试显示效果'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">nickname</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '用户C'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">, </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">content</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '第三条消息'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">nickname</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '用户D'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">, </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">content</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '第四条消息'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> },</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  { </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">nickname</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '用户E'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">, </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">content</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '第五条消息'</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">]</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> /></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>实际效果：</strong></p>
<MergeForward :messages="[
  { nickname: '用户A', content: '第一条消息内容' },
  { nickname: '用户B', content: '第二条消息内容，这是一条比较长的消息，用于测试显示效果' },
  { nickname: '用户C', content: '第三条消息' },
  { nickname: '用户D', content: '第四条消息' },
  { nickname: '用户E', content: '第五条消息' }
]" />
<h3 id="_5-chatpanel-聊天面板组件" tabindex="-1"><a class="header-anchor" href="#_5-chatpanel-聊天面板组件"><span>5. ChatPanel - 聊天面板组件</span></a></h3>
<p>用于创建类似聊天窗口的面板容器。</p>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatPanel</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;!-- 面板内容 --></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;ChatMessage nickname="用户" type="user"></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    面板内的用户消息</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;/ChatMessage></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;ChatMessage nickname="机器人" type="bot"></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    面板内的机器人回复</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;/ChatMessage></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">ChatPanel</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p><strong>实际效果：</strong></p>
<ChatPanel>
  <ChatMessage nickname="用户" type="user">
    这是一个在面板内的用户消息
  </ChatMessage>
  <ChatMessage nickname="机器人" type="bot">
    这是一个在面板内的机器人回复，面板提供了更好的视觉容器效果
  </ChatMessage>
</ChatPanel>
<h2 id="组件组合使用示例" tabindex="-1"><a class="header-anchor" href="#组件组合使用示例"><span>组件组合使用示例</span></a></h2>
<h3 id="完整的聊天场景" tabindex="-1"><a class="header-anchor" href="#完整的聊天场景"><span>完整的聊天场景</span></a></h3>
<ChatPanel>
  <ChatMessage nickname="小明" type="user">
    大家好，今天天气不错！
  </ChatMessage>
  <ChatMessage nickname="小红" type="user">
    是啊，适合出去走走
  </ChatMessage>
  <ChatMessage nickname="系统" type="system">
    小明撤回了一条消息
  </ChatMessage>
  <RecallMessage nickname="小明" type="user">
    刚才发错消息了
  </RecallMessage>
  <SimpleImageMessage
    imageSrc="https://via.placeholder.com/250x150"
    imageAlt="风景图片"
    text="分享一张风景图片"
    caption="美丽的风景"
  />
  <ChatMessage nickname="机器人" type="bot">
    检测到图片分享，图片已保存到相册
  </ChatMessage>
</ChatPanel>
<h3 id="转发聊天记录" tabindex="-1"><a class="header-anchor" href="#转发聊天记录"><span>转发聊天记录</span></a></h3>
<MergeForward :messages="[
  { nickname: '小明', content: '今天有什么安排？' },
  { nickname: '小红', content: '打算去公园散步' },
  { nickname: '小刚', content: '我也想去，一起吧！' },
  { nickname: '小美', content: '好的，下午2点公园门口见' },
  { nickname: '小明', content: '收到，准时到' }
]" />
<h2 id="组件属性说明" tabindex="-1"><a class="header-anchor" href="#组件属性说明"><span>组件属性说明</span></a></h2>
<h3 id="chatmessage" tabindex="-1"><a class="header-anchor" href="#chatmessage"><span>ChatMessage</span></a></h3>
<ul>
<li><code v-pre>nickname</code> (必需): 显示的用户昵称</li>
<li><code v-pre>type</code>: 消息类型，可选值: 'user' | 'bot' | 'system'</li>
</ul>
<h3 id="recallmessage" tabindex="-1"><a class="header-anchor" href="#recallmessage"><span>RecallMessage</span></a></h3>
<ul>
<li><code v-pre>nickname</code> (必需): 显示的用户昵称</li>
<li><code v-pre>type</code>: 消息类型，可选值: 'user' | 'bot' | 'system'</li>
</ul>
<h3 id="simpleimagemessage" tabindex="-1"><a class="header-anchor" href="#simpleimagemessage"><span>SimpleImageMessage</span></a></h3>
<ul>
<li><code v-pre>imageSrc</code> (必需): 图片URL</li>
<li><code v-pre>imageAlt</code>: 图片替代文本</li>
<li><code v-pre>text</code>: 图片上方的文本内容</li>
<li><code v-pre>caption</code>: 图片下方的说明文字</li>
<li><code v-pre>maxWidth</code>: 图片最大宽度</li>
<li><code v-pre>maxHeight</code>: 图片最大高度</li>
<li><code v-pre>borderRadius</code>: 图片圆角</li>
</ul>
<h3 id="mergeforward" tabindex="-1"><a class="header-anchor" href="#mergeforward"><span>MergeForward</span></a></h3>
<ul>
<li><code v-pre>messages</code> (必需): 转发消息数组</li>
<li><code v-pre>maxPreview</code>: 预览显示的最大消息数量</li>
</ul>
<h3 id="chatpanel" tabindex="-1"><a class="header-anchor" href="#chatpanel"><span>ChatPanel</span></a></h3>
<ul>
<li>无特定属性，用作内容容器</li>
</ul>
<h2 id="使用提示" tabindex="-1"><a class="header-anchor" href="#使用提示"><span>使用提示</span></a></h2>
<ol>
<li>所有组件都支持响应式设计，在不同屏幕尺寸下都能良好显示</li>
<li>组件样式会自动适配 VuePress 主题颜色</li>
<li>图片组件会自动处理加载状态和错误情况</li>
<li>聊天消息组件支持滚动进入视口时的动画效果</li>
</ol>
<hr>
<p><em>本页面展示了项目中所有 Vue 组件的完整使用示例</em></p>
</div></template>


