<template><div><h1 id="使用指南" tabindex="-1"><a class="header-anchor" href="#使用指南"><span>使用指南</span></a></h1>
<p>了解如何充分利用麦芽糖bot的各项功能。</p>
<h2 id="基本操作" tabindex="-1"><a class="header-anchor" href="#基本操作"><span>基本操作</span></a></h2>
<h3 id="_1-唤醒机器人" tabindex="-1"><a class="header-anchor" href="#_1-唤醒机器人"><span>1. 唤醒机器人</span></a></h3>
<p>在群聊中使用以下方式唤醒机器人：</p>
<ul>
<li><strong>@机器人</strong>: <code v-pre>@麦芽糖bot</code></li>
<li><strong>直接称呼</strong>: <code v-pre>麦芽糖</code>、<code v-pre>bot</code>、<code v-pre>机器人</code></li>
</ul>
<h3 id="_2-命令格式" tabindex="-1"><a class="header-anchor" href="#_2-命令格式"><span>2. 命令格式</span></a></h3>
<p>大多数命令支持以下格式：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot [命令] [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><p>例如：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 天气 北京</span></span>
<span class="line"><span>@麦芽糖bot 翻译 hello world</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="功能详解" tabindex="-1"><a class="header-anchor" href="#功能详解"><span>功能详解</span></a></h2>
<h3 id="娱乐功能使用" tabindex="-1"><a class="header-anchor" href="#娱乐功能使用"><span>娱乐功能使用</span></a></h3>
<h4 id="抽签系统" tabindex="-1"><a class="header-anchor" href="#抽签系统"><span>抽签系统</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 抽签        # 每日运势抽签</span></span>
<span class="line"><span>@麦芽糖bot 随机抽签    # 随时抽签</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h4 id="游戏功能" tabindex="-1"><a class="header-anchor" href="#游戏功能"><span>游戏功能</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 猜数字      # 开始猜数字游戏</span></span>
<span class="line"><span>@麦芽糖bot 成语接龙    # 开始成语接龙</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h4 id="趣味互动" tabindex="-1"><a class="header-anchor" href="#趣味互动"><span>趣味互动</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 讲个笑话    # 随机笑话</span></span>
<span class="line"><span>@麦芽糖bot 心灵鸡汤    # 正能量语录</span></span>
<span class="line"><span>@麦芽糖bot 星座运势 白羊座  # 查询星座运势</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="实用工具使用" tabindex="-1"><a class="header-anchor" href="#实用工具使用"><span>实用工具使用</span></a></h3>
<h4 id="信息查询" tabindex="-1"><a class="header-anchor" href="#信息查询"><span>信息查询</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 天气 上海    # 查询天气</span></span>
<span class="line"><span>@麦芽糖bot 汇率 USD     # 查询美元汇率</span></span>
<span class="line"><span>@麦芽糖bot 时间 纽约    # 查询纽约时间</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h4 id="文本处理" tabindex="-1"><a class="header-anchor" href="#文本处理"><span>文本处理</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 翻译 你好 world  # 中英翻译</span></span>
<span class="line"><span>@麦芽糖bot 计算 2+3*4     # 数学计算</span></span>
<span class="line"><span>@麦芽糖bot 单位换算 1米=英尺  # 单位换算</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h4 id="生活助手" tabindex="-1"><a class="header-anchor" href="#生活助手"><span>生活助手</span></a></h4>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 倒数日 2024-12-25  # 设置倒数日</span></span>
<span class="line"><span>@麦芽糖bot 随机决定 吃饭,睡觉,打游戏  # 随机选择</span></span>
<span class="line"><span>@麦芽糖bot 二维码 hello      # 生成二维码</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="群管功能使用" tabindex="-1"><a class="header-anchor" href="#群管功能使用"><span>群管功能使用</span></a></h3>
<p>群管功能通常自动运行，无需手动命令：</p>
<ul>
<li><strong>欢迎新人</strong>: 新成员加入时自动发送欢迎消息</li>
<li><strong>关键词提醒</strong>: 检测到特定关键词时自动提醒</li>
<li><strong>防刷屏</strong>: 自动检测并限制刷屏行为</li>
</ul>
<h2 id="高级功能" tabindex="-1"><a class="header-anchor" href="#高级功能"><span>高级功能</span></a></h2>
<h3 id="个性化设置" tabindex="-1"><a class="header-anchor" href="#个性化设置"><span>个性化设置</span></a></h3>
<p>部分功能支持个性化设置：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 设置语言 中文</span></span>
<span class="line"><span>@麦芽糖bot 设置时区 +8</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="批量操作" tabindex="-1"><a class="header-anchor" href="#批量操作"><span>批量操作</span></a></h3>
<p>某些功能支持批量操作：</p>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>@麦芽糖bot 批量翻译 你好,hello,こんにちは</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h2 id="常见问题" tabindex="-1"><a class="header-anchor" href="#常见问题"><span>常见问题</span></a></h2>
<h3 id="q-机器人没有响应怎么办" tabindex="-1"><a class="header-anchor" href="#q-机器人没有响应怎么办"><span>Q: 机器人没有响应怎么办？</span></a></h3>
<p>A: 请检查：</p>
<ol>
<li>机器人是否在线</li>
<li>命令格式是否正确</li>
<li>网络连接是否正常</li>
</ol>
<h3 id="q-如何获取帮助" tabindex="-1"><a class="header-anchor" href="#q-如何获取帮助"><span>Q: 如何获取帮助？</span></a></h3>
<p>A: 使用 <code v-pre>@麦芽糖bot 帮助</code> 命令查看所有可用功能。</p>
<h3 id="q-功能无法使用怎么办" tabindex="-1"><a class="header-anchor" href="#q-功能无法使用怎么办"><span>Q: 功能无法使用怎么办？</span></a></h3>
<p>A: 可能是该功能正在维护或暂时关闭，请稍后重试。</p>
<h2 id="联系支持" tabindex="-1"><a class="header-anchor" href="#联系支持"><span>联系支持</span></a></h2>
<p>如果遇到问题，可以通过以下方式联系：</p>
<ul>
<li><strong>官方QQ群</strong>: 1030501081</li>
<li><strong>机器人QQ</strong>: 3929982192</li>
</ul>
<p>我们会在第一时间为您解决问题！</p>
</div></template>


