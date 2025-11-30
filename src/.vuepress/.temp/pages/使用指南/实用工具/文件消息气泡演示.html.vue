<template><div><h1 id="文件消息气泡演示" tabindex="-1"><a class="header-anchor" href="#文件消息气泡演示"><span>文件消息气泡演示</span></a></h1>
<p>这个页面展示了文件消息气泡组件的各种使用场景和效果。</p>
<h2 id="演示示例" tabindex="-1"><a class="header-anchor" href="#演示示例"><span>演示示例</span></a></h2>
<h3 id="图片文件预览" tabindex="-1"><a class="header-anchor" href="#图片文件预览"><span>图片文件预览</span></a></h3>
<FileMessage
  fileName="风景照片.jpg"
  :fileSize="2457600"
  downloadUrl="https://picsum.photos/800/600"
  fileType="image"
/>
<ChatMessage nickname="用户B" type="bot">
<FileMessage
  fileName="产品截图.png"
  :fileSize="1536000"
  downloadUrl="https://picsum.photos/600/400"
  previewUrl="https://picsum.photos/300/200"
  fileType="image"
/>
</ChatMessage>
<h3 id="视频文件预览" tabindex="-1"><a class="header-anchor" href="#视频文件预览"><span>视频文件预览</span></a></h3>
<ChatMessage nickname="用户C" type="user">
<FileMessage
  fileName="产品演示.mp4"
  :fileSize="15728640"
  downloadUrl="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
  fileType="video"
/>
</ChatMessage>
<h3 id="不支持预览的文件类型" tabindex="-1"><a class="header-anchor" href="#不支持预览的文件类型"><span>不支持预览的文件类型</span></a></h3>
<ChatMessage nickname="用户D" type="user">
<FileMessage
  fileName="项目文档.pdf"
  :fileSize="1048576"
  downloadUrl="https://example.com/document.pdf"
  fileType="document"
/>
</ChatMessage>
<ChatMessage nickname="用户E" type="bot">
<FileMessage
  fileName="背景音乐.mp3"
  :fileSize="5242880"
  downloadUrl="https://example.com/music.mp3"
  fileType="audio"
/>
</ChatMessage>
<ChatMessage nickname="用户F" type="user">
<FileMessage
  fileName="源代码.zip"
  :fileSize="20971520"
  downloadUrl="https://example.com/source.zip"
  fileType="archive"
/>
</ChatMessage>
<ChatMessage nickname="用户G" type="bot">
<FileMessage
  fileName="未知文件.xyz"
  :fileSize="102400"
  downloadUrl="https://example.com/unknown.xyz"
  fileType="unknown"
/>
</ChatMessage>
<h3 id="不同大小的文件" tabindex="-1"><a class="header-anchor" href="#不同大小的文件"><span>不同大小的文件</span></a></h3>
<ChatMessage nickname="用户H" type="user">
<FileMessage
  fileName="小文件.txt"
  :fileSize="1024"
  downloadUrl="https://example.com/small.txt"
  fileType="document"
/>
</ChatMessage>
<ChatMessage nickname="用户I" type="bot">
<FileMessage
  fileName="大文件.iso"
  :fileSize="2147483648"
  downloadUrl="https://example.com/large.iso"
  fileType="archive"
/>
</ChatMessage>
<h2 id="组件特点总结" tabindex="-1"><a class="header-anchor" href="#组件特点总结"><span>组件特点总结</span></a></h2>
<h3 id="布局差异" tabindex="-1"><a class="header-anchor" href="#布局差异"><span>布局差异</span></a></h3>
<p><strong>支持预览的文件（图片、视频）：</strong></p>
<ul>
<li>预览内容显示在上方</li>
<li>文件名称和大小在同一行显示在下方</li>
<li>右下角固定下载按钮</li>
</ul>
<p><strong>不支持预览的文件：</strong></p>
<ul>
<li>文件图标显示在左侧</li>
<li>文件名称在上方</li>
<li>文件大小在下方</li>
<li>右下角固定下载按钮</li>
</ul>
<h3 id="交互效果" tabindex="-1"><a class="header-anchor" href="#交互效果"><span>交互效果</span></a></h3>
<ul>
<li>鼠标悬停时卡片有轻微上浮效果</li>
<li>下载按钮悬停时有颜色变化</li>
<li>滚动进入视口时有淡入动画</li>
<li>加载状态显示加载动画</li>
<li>错误状态显示错误提示</li>
</ul>
<h3 id="响应式设计" tabindex="-1"><a class="header-anchor" href="#响应式设计"><span>响应式设计</span></a></h3>
<ul>
<li>桌面端：最大宽度 320px</li>
<li>移动端：最大宽度 280px</li>
<li>图片/视频预览最大高度自动调整</li>
</ul>
<h2 id="使用建议" tabindex="-1"><a class="header-anchor" href="#使用建议"><span>使用建议</span></a></h2>
<ol>
<li><strong>图片文件</strong>：建议提供独立的预览链接，使用较低分辨率的图片作为预览，提高加载速度</li>
<li><strong>视频文件</strong>：确保视频格式兼容主流浏览器（MP4、WebM）</li>
<li><strong>文件大小</strong>：组件会自动格式化为合适的单位（B、KB、MB、GB）</li>
<li><strong>文件类型</strong>：正确设置文件类型以获得最佳图标和布局</li>
</ol>
<h2 id="代码示例" tabindex="-1"><a class="header-anchor" href="#代码示例"><span>代码示例</span></a></h2>
<div class="language-vue line-numbers-mode" data-highlighter="shiki" data-ext="vue" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-vue"><span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">template</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">div</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">    &#x3C;!-- 图片文件 --></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"示例图片.jpg"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">      :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">2048576</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/file.jpg"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      previewUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/preview.jpg"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"image"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    /></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    </span></span>
<span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">    &#x3C;!-- 视频文件 --></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"演示视频.mp4"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">      :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">15728640</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/video.mp4"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"video"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    /></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    </span></span>
<span class="line"><span style="--shiki-light:#A0A1A7;--shiki-light-font-style:italic;--shiki-dark:#7F848E;--shiki-dark-font-style:italic">    &#x3C;!-- 文档文件 --></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    &#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">FileMessage</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileName</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"项目文档.pdf"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">      :</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">fileSize</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66">1048576</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      downloadUrl</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"https://example.com/document.pdf"</span></span>
<span class="line"><span style="--shiki-light:#986801;--shiki-dark:#D19A66">      fileType</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">=</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">"document"</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    /></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  &#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">div</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">template</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">script</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">import</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75"> FileMessage</span><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD"> from</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379"> '../components/FileMessage.vue'</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#A626A4;--shiki-dark:#C678DD">export</span><span style="--shiki-light:#E45649;--shiki-dark:#C678DD"> default</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  components</span><span style="--shiki-light:#0184BC;--shiki-dark:#ABB2BF">:</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF"> {</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">    FileMessage</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">  }</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">}</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">&#x3C;/</span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">script</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><p>这个组件可以很好地集成到聊天界面中，提供一致的用户体验。</p>
</div></template>


