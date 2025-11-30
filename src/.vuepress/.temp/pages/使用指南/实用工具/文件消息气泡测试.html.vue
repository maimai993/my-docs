<template><div><h1 id="文件消息气泡测试" tabindex="-1"><a class="header-anchor" href="#文件消息气泡测试"><span>文件消息气泡测试</span></a></h1>
<p>这个页面用于测试文件消息气泡组件的基本功能。</p>
<h2 id="简单测试" tabindex="-1"><a class="header-anchor" href="#简单测试"><span>简单测试</span></a></h2>
<h3 id="图片文件测试" tabindex="-1"><a class="header-anchor" href="#图片文件测试"><span>图片文件测试</span></a></h3>
<FileMessage
  fileName="测试图片.jpg"
  :fileSize="1024000"
  downloadUrl="https://picsum.photos/300/200"
  fileType="image"
/>
<h3 id="文档文件测试" tabindex="-1"><a class="header-anchor" href="#文档文件测试"><span>文档文件测试</span></a></h3>
<FileMessage
  fileName="测试文档.pdf"
  :fileSize="512000"
  downloadUrl="https://example.com/test.pdf"
  fileType="document"
/>
<h3 id="音频文件测试" tabindex="-1"><a class="header-anchor" href="#音频文件测试"><span>音频文件测试</span></a></h3>
<FileMessage
  fileName="测试音频.mp3"
  :fileSize="2048000"
  downloadUrl="https://example.com/test.mp3"
  fileType="audio"
/>
<h3 id="视频文件测试" tabindex="-1"><a class="header-anchor" href="#视频文件测试"><span>视频文件测试</span></a></h3>
<FileMessage
  fileName="测试视频.mp4"
  :fileSize="5242880"
  downloadUrl="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
  fileType="video"
/>
<h3 id="压缩文件测试" tabindex="-1"><a class="header-anchor" href="#压缩文件测试"><span>压缩文件测试</span></a></h3>
<FileMessage
  fileName="测试压缩包.zip"
  :fileSize="1048576"
  downloadUrl="https://example.com/test.zip"
  fileType="archive"
/>
<h3 id="未知文件测试" tabindex="-1"><a class="header-anchor" href="#未知文件测试"><span>未知文件测试</span></a></h3>
<FileMessage
  fileName="未知文件.xyz"
  :fileSize="102400"
  downloadUrl="https://example.com/unknown.xyz"
  fileType="unknown"
/>
<h2 id="测试说明" tabindex="-1"><a class="header-anchor" href="#测试说明"><span>测试说明</span></a></h2>
<p>如果组件正常工作，你应该看到：</p>
<ul>
<li>图片和视频文件显示预览内容</li>
<li>所有文件显示文件名称和大小</li>
<li>右下角有下载按钮</li>
<li>支持预览的文件：名称和大小在同一行显示在下方</li>
<li>不支持预览的文件：名称在上方，大小在下方</li>
</ul>
<p>如果组件不显示，请检查：</p>
<ol>
<li>组件是否正确注册</li>
<li>CSS样式是否加载</li>
<li>文件路径是否正确</li>
</ol>
</div></template>


