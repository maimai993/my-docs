<template><div><h1 id="搜图来源" tabindex="-1"><a class="header-anchor" href="#搜图来源"><span>搜图来源</span></a></h1>
<div class="hint-container warning">
<p class="hint-container-title">功能说明</p>
<p>搜索结果可能不准确，仅供参考。</p>
</div>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: 搜图</p>
<p><strong>功能描述</strong>: 搜图来源</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcR7NbyASfFY0qYETo2HAtXWaEvaoh4lKiEaAgIHo6ThS0FNgBMaMPoupt3Wt7BffJTiHNqdmd/+Z3Z2D46lswzPyirEExGwLcWYjQEqve+7nvtR8ulDmc3xEBfE/LkbCoRxYGjaGHbsXebbyNs4N5q2c8sQJ2YjYQFSynJHCjDOf9teJPKiKpxwQaUFHbNBNpdhVdQsGzftIOUY6eeDmUDpgOAeMIQkKLyA2kWkTcKChJ8PZ3CKYbNsTuVkTBK5tLRW0zEqyfCcLGEKx8oZPtzT+nrRZwowbNceoOvQtO3B1s9dC9CkhAqjHX16q88mWy5EugzpI22gRC4mqXAajRrlijUcehSxvFLCRzvgAVa/i7Sqh+GUi+CUz3TBK6V/tn4vaqtSc5UeWONL59lUaouWqKSLUEmfeQLru2E8auasjrTmJpVn0D8e7As1eldmtbi5lz4Y9bIxbRjjgtW93qQy+Ofw3ogCc3rxxbyBetj6uF8B3X+Zvelq26nIH09sCfA="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>搜图 [图片]</span></span></code></pre>
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
<td>图片</td>
<td>图片</td>
<td>是</td>
<td>搜索内容</td>
<td><a href="./%E6%90%9C%E5%9B%BE%E6%9D%A5%E6%BA%90_%E7%A4%BA%E8%8C%83.jpg">图片</a></td>
</tr>
</tbody>
</table>
<h3 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h3>
<h4 id="搜图来源-1" tabindex="-1"><a class="header-anchor" href="#搜图来源-1"><span>搜图来源</span></a></h4>
<chat-panel>
<chat-message nickname="用户" type="user">
<SimpleImageMessage text="搜图" image-src="./搜图来源_示范.jpg" max-width="200" max-height="150" />
</chat-message>
<chat-message nickname="bot" type="bot">
<MergeForward :messages="[
{ nickname: 'bot', type: 'bot', content: '[图片] 链接：https://e621.net/post/show/5609746 \n 作者：未知 \n 网站：e621 \n 相似度：88.5% \n 索引：29' }
]" />
</chat-message>
</chat-panel>
</div></template>


