<template><div><h1 id="fish-audio" tabindex="-1"><a class="header-anchor" href="#fish-audio"><span>fish-audio</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-fish-audio" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-fish-audio" alt="" loading="lazy"></a>  <a href="https://github.com/idranme/koishi-plugin-fish-audio" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: 根据配置的角色名称</p>
<p><strong>功能描述</strong>: 通过 Fish Audio API 进行文本转语音，支持多种语音模型</p>
<p><strong>插件名称</strong>: fish-audio</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1kstOwkAUhvc8xYl7NL6AyWhCNBiwRlaNiypVarQlUNSl9xgNchE3xiBXQZGLMQGDxocxdChv4XRmAAt4Fu3MnG/+Oeef2drVDjYDUkiH5VUHkPCJ3VQZX7bW6Yx+wpGN7ZAUDMCyokYO6ZJtGYEoCEYtR3Z1K3W2sR+CQHLDJVn1O8YFPJpf3gmDaP2nyWA1ourKnmxXGtDzBJSCm5KOH6LGVdZOWeHheXvGdrRNcAFEt6aEAwrOXuB0c1zQzfPjGeQVJb8U1OWQU1PlDW3kTCtcSNwim51SxK9o4+nFtbUVMaDrwUndWDWPjgd9+MDpnCMG04kgkBlM/SQygJuX+Lg+02lfdz6bUxTyUMbDkSx4VXle02F/dtaIxsxajVHu4ZW7OZoDBpilPE7HGYa8FEFezuSBHdX5yvSOkn+l+ioFMBun1rOKJQcluRBFXIgzRc6glSUGWMZQxBpw6AnMegu/nbiIoYAsQ2HAjwqWAN8UcarZe3zv5RL4roGjtj77xZWh83FPnDcKZ934xeQWn8G4jRrtlNE4NvPnk1Re/vGUOW+zv8LF2D0xbPQWXwEnqzj1bdarpH7G+By/oSsx+Q=="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>tts &#x3C;角色名称> &#x3C;文本内容></span></span></code></pre>
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
<td>角色名称</td>
<td>文本</td>
<td>是</td>
<td>配置中定义的角色名称</td>
<td>流萤</td>
</tr>
<tr>
<td>文本内容</td>
<td>文本</td>
<td>是</td>
<td>要转换为语音的文本</td>
<td>你好，我是流萤</td>
</tr>
</tbody>
</table>
<h3 id="可用角色" tabindex="-1"><a class="header-anchor" href="#可用角色"><span>可用角色</span></a></h3>
<p>根据配置文件，当前支持以下角色：</p>
<table>
<thead>
<tr>
<th>角色名称</th>
<th>参考ID</th>
</tr>
</thead>
<tbody>
<tr>
<td>流萤</td>
<td>bcbb6d60721c44a489bc33dd59ce7cfc</td>
</tr>
<tr>
<td>银狼</td>
<td>5f75344c4bfa47318d7252496bd1d308</td>
</tr>
<tr>
<td>雷军</td>
<td>738d0cc1a3e9430a9de2b544a466a7fc</td>
</tr>
<tr>
<td>丁真</td>
<td>54a5170264694bfc8e9ad98df7bd89c3</td>
</tr>
<tr>
<td>奶龙</td>
<td>3d1cb00d75184099992ddbaf0fdd7387</td>
</tr>
<tr>
<td>诗歌剧</td>
<td>0eb38bc974e1459facca38b359e13511</td>
</tr>
<tr>
<td>东雪莲</td>
<td>7af4d620be1c4c6686132f21940d51c5</td>
</tr>
<tr>
<td>永雏塔菲</td>
<td>e1cfccf59a1c4492b5f51c7c62a8abd2</td>
</tr>
<tr>
<td>孙笑川</td>
<td>e80ea225770f42f79d50aa98be3cedfc</td>
</tr>
<tr>
<td>七海娜娜米</td>
<td>a7725771e0974eb5a9b044ba357f6e13</td>
</tr>
<tr>
<td>刘伟</td>
<td>5b191ce8add743f0a62a55364e2866b0</td>
</tr>
<tr>
<td>蔡徐坤</td>
<td>e4642e5edccd4d9ab61a69e82d4f8a14</td>
</tr>
<tr>
<td>黑手</td>
<td>f7561ff309bd4040a59f1e600f4f4338</td>
</tr>
<tr>
<td>郭德纲</td>
<td>7c66db6e457c4d53b1fe428a8c547953</td>
</tr>
<tr>
<td>多托雷</td>
<td>1ff4ea5624884731a65a0dcd58cbcb61</td>
</tr>
<tr>
<td>潘塔罗涅</td>
<td>98dd87194f3c4cd096881cd61336ab62</td>
</tr>
<tr>
<td>王同志</td>
<td>753a35fa4b7b407dafa1277f22f99697</td>
</tr>
<tr>
<td>林德</td>
<td>28ec5b92ac984d058ae07d716b56240c</td>
</tr>
<tr>
<td>沙威马</td>
<td>54a2b55df13e42c0a09bf18b0a5e04d1</td>
</tr>
<tr>
<td>贝利亚</td>
<td>356623728b844a1a95c1a5125e340467</td>
</tr>
<tr>
<td>少羽</td>
<td>1218287072ff42e6b2e1373958742529</td>
</tr>
<tr>
<td>孙悟空</td>
<td>2f7857f695f141e0b88c865e12d231b3</td>
</tr>
<tr>
<td>女法式中</td>
<td>3a0d20c9223a438bbeae1e46fb08794a</td>
</tr>
<tr>
<td>夯大力</td>
<td>84ed22e0ec8746969adf08bef0407494</td>
</tr>
<tr>
<td>银枝</td>
<td>ae4d87fc4b0944beaa06b16bb7458552</td>
</tr>
<tr>
<td>胖猫</td>
<td>665e031efe27435780ebfa56cc7e0e0d</td>
</tr>
<tr>
<td>科比</td>
<td>0bb80f15ff69492ea36f67174250cdb1</td>
</tr>
<tr>
<td>明前奶绿</td>
<td>e0cefc0c31674611862242d79f1075cc</td>
</tr>
<tr>
<td>小老师</td>
<td>434bb3a59f8b459e8d4fd2326cecd800</td>
</tr>
<tr>
<td>麦麦</td>
<td>53a749722edb4b7fb514054b3d31cd89</td>
</tr>
<tr>
<td>风堇</td>
<td>5eb6a4de76c649049dd136dd9f53b0d2</td>
</tr>
<tr>
<td>威龙</td>
<td>4d09c6726bac4464bb17b3a9aa148ee4</td>
</tr>
<tr>
<td>德穆兰</td>
<td>96c8c5d15f1240688abbada7394d6537</td>
</tr>
<tr>
<td>烧麦</td>
<td>d32ac201055f4567ab8435e1943e1830</td>
</tr>
<tr>
<td>快麦</td>
<td>300d2c22405f421f93551ae109</td>
</tr>
<tr>
<td>慢麦</td>
<td>296978aabdea4d0db46dd432424ff7c0</td>
</tr>
<tr>
<td>月樱</td>
<td>f68a6692376345988756428a6fc3b04f</td>
</tr>
<tr>
<td>今汐</td>
<td>1fa6a46da8484d72a4c4809dbb944943</td>
</tr>
<tr>
<td>菲比</td>
<td>3c4ca0e69c65482f9fbb01cec7bc0678</td>
</tr>
<tr>
<td>珂莱塔</td>
<td>1b968f22bd244f199a21c5ae1b759932</td>
</tr>
<tr>
<td>东海帝王</td>
<td>ec263983ed464bbca97017eab40fa767</td>
</tr>
<tr>
<td>波旁</td>
<td>47f0b282985d4d958daed73509e75e12</td>
</tr>
<tr>
<td>米浴</td>
<td>f820798ba9b74510bd5e46cb73b361d8</td>
</tr>
<tr>
<td>福来</td>
<td>e2abe323ffb3492e850f0a9f7e3d2132</td>
</tr>
<tr>
<td>电棍</td>
<td>703b0f7a5b7848f3bdfb7698ddb1899b</td>
</tr>
<tr>
<td>酵母</td>
<td>0bd063af3d6e43418808d50febeac5de</td>
</tr>
<tr>
<td>迪拉熊</td>
<td>b8cdad77ddd64783b4ee26ab9a2b053e</td>
</tr>
<tr>
<td>高松灯</td>
<td>a24ad94ea73449558c3c8fe9e0f0a41f</td>
</tr>
<tr>
<td>油库里</td>
<td>1f25aac343ff4613bb62015d964125e7</td>
</tr>
<tr>
<td>户晨风</td>
<td>be8c4e50b41f4eb0b1badce141c2b0a8</td>
</tr>
<tr>
<td>拉伸</td>
<td>84e138ec381947de8420fb96a750f68a</td>
</tr>
<tr>
<td>079</td>
<td>1ac0f409f4264f1ba86b4bc88d474ed1</td>
</tr>
<tr>
<td>SL广播</td>
<td>f95e2cdf975642618b9dc3f380375c1f</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="使用流萤生成语音" tabindex="-1"><a class="header-anchor" href="#使用流萤生成语音"><span>使用流萤生成语音</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">tts 流萤 夜色渐深，我的光芒为迷途者指引方向。如同群星闪烁，每个生命都有属于自己的光辉时刻。让我们一同穿越黑暗，寻找黎明的希望。这便是我存在的意义。</chat-message>
<chat-message nickname="bot" type="bot">
  <voice-message 
    :duration="13" 
    :is-listened="true"
    audio-url="./流萤.mp3"
  />
</chat-message>
</chat-panel>
<h3 id="使用银狼生成语音" tabindex="-1"><a class="header-anchor" href="#使用银狼生成语音"><span>使用银狼生成语音</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">tts 银狼 防火墙漏洞已经找到了，给我三分钟就能突破。这种老旧系统的加密方式太好玩了，简直就是在给我送礼物。不过还是要小心行事，毕竟我可不想打草惊蛇。</chat-message>
<chat-message nickname="bot" type="bot">
  <voice-message 
    :duration="13" 
    :is-listened="true"
    audio-url="./银狼.mp3"
  />
</chat-message>
</chat-panel>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="支持的api" tabindex="-1"><a class="header-anchor" href="#支持的api"><span>支持的API</span></a></h3>
<ul>
<li><strong>Fish Audio API</strong>: 使用官方API进行文本转语音</li>
<li><strong>VITS服务</strong>: 支持VITS服务接口，可与其他插件集成</li>
</ul>
<h3 id="自动处理" tabindex="-1"><a class="header-anchor" href="#自动处理"><span>自动处理</span></a></h3>
<ul>
<li><strong>文本验证</strong>: 自动检测输入是否为纯文本，拒绝包含HTML标签的内容</li>
<li><strong>错误处理</strong>: 当API调用失败时提供友好的错误提示</li>
<li><strong>音频格式</strong>: 生成WAV格式的音频文件，兼容性良好</li>
</ul>
<h3 id="配置灵活" tabindex="-1"><a class="header-anchor" href="#配置灵活"><span>配置灵活</span></a></h3>
<ul>
<li><strong>多角色支持</strong>: 可配置多个语音角色，每个角色有独立的指令</li>
<li><strong>代理支持</strong>: 支持通过代理访问Fish Audio API</li>
<li><strong>自定义API地址</strong>: 可配置自定义API地址</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>API密钥</strong>: 需要有效的Fish Audio API密钥，可从<a href="https://fish.audio/zh-CN/go-api/" target="_blank" rel="noopener noreferrer">Fish Audio官网</a>获取</li>
<li><strong>网络要求</strong>: 需要稳定的网络连接来访问Fish Audio API</li>
<li><strong>文本限制</strong>: 输入文本应为纯文本，不支持HTML或其他标记语言</li>
<li><strong>语音质量</strong>: 语音质量取决于Fish Audio API的模型质量</li>
<li><strong>响应时间</strong>: 语音生成需要调用外部API，响应时间受网络影响</li>
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
<td>api_key</td>
<td>string</td>
<td>无</td>
<td>Fish Audio API密钥，必填项</td>
</tr>
<tr>
<td>api_url</td>
<td>string</td>
<td><a href="https://api.fish.audio/v1/tts" target="_blank" rel="noopener noreferrer">https://api.fish.audio/v1/tts</a></td>
<td>Fish Audio API地址</td>
</tr>
<tr>
<td>command_name</td>
<td>string</td>
<td>空</td>
<td>指令前缀名称，如果设置则指令格式为<code v-pre>&lt;前缀&gt;.&lt;角色&gt;</code></td>
</tr>
<tr>
<td>command</td>
<td>array</td>
<td>见默认配置</td>
<td>指令列表，包含角色名称、描述和参考ID</td>
</tr>
<tr>
<td>vits_service_speaker</td>
<td>string</td>
<td>bcbb6d60721c44a489bc33dd59ce7cfc</td>
<td>用于VITS服务的默认语音角色</td>
</tr>
<tr>
<td>proxy_agent</td>
<td>string</td>
<td>无</td>
<td>用于访问API的代理设置</td>
</tr>
</tbody>
</table>
<h3 id="默认配置示例" tabindex="-1"><a class="header-anchor" href="#默认配置示例"><span>默认配置示例</span></a></h3>
<div class="language-yaml line-numbers-mode" data-highlighter="shiki" data-ext="yaml" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-yaml"><span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">fish-audio</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  api_key</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">'your-api-key-here'</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">  command</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">:</span></span>
<span class="line"><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">    - </span><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">name</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">流萤</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">      description</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">语音生成（流萤）</span></span>
<span class="line"><span style="--shiki-light:#E45649;--shiki-dark:#E06C75">      reference_id</span><span style="--shiki-light:#383A42;--shiki-dark:#ABB2BF">: </span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379">bcbb6d60721c44a489bc33dd59ce7cfc</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>fish-audio插件基于Fish Audio API实现，能够生成高质量的语音内容。支持多种语音模型，可根据需要配置不同的角色。插件还实现了VITS服务接口，可与其他需要语音合成的插件集成使用。</p>
</div>
</div></template>


