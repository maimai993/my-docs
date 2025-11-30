<template><div><h1 id="bmi查询" tabindex="-1"><a class="header-anchor" href="#bmi查询"><span>BMI查询</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><strong>指令名称</strong>: bmi-calculator</p>
<p><strong>功能描述</strong>: 根据身高和体重计算BMI指数，评估体重对健康的影响，并提供相应的健康建议</p>
<p><strong>插件名称</strong>: bmi-calculator</p>
<h2 id="架构图" tabindex="-1"><a class="header-anchor" href="#架构图"><span>架构图</span></a></h2>
<Mermaid code="eJx1ks1OwkAQx+88xcQ7Gl7ABDwZEFISTo2HAlVqoCVQ1KNEJERDQCDRGEL4FJSkcAIDxIcx3W19C7fdApaPOXR3Z377n+nMXsSlm0iMS8ngCzqAWIjVagNcmJ6bJ/OTzoQvU1wyBj5BzNyaLpvbDSzDIKVNbmnDEb24NIYhsbWLF6OObQG/FOWv0sAa6yHZBDOiLCR4u9KK9hCQS0Y4GdeL6LFlpwzzW3F7xJbaJngCrFcS0jEBt/K4MdkW9Frx7Yg7wHJRLinzKack8mFpI6dhnrNTNpwQnBEuHsnEOVlKbde1uV/VGgKn85g00TwwDDnBwc9zE/CkgLOjI3X2pM4nBybkNxm/hbQgIPIeSYZrlwsVS7qiUMq7HqvXQttAAb3fwY0yxdwBE3EHLKYDNJW6aP7eVf5LLVW6oI/vjadTqqxKIr9uMmS1qJ6x15WWprzsQ94BZXtoNtVHOXUx3pWqD+rXG5k86ua0cn53wQNA1SKa1dA4q3cedql87OkQ7aOtmZ+WGO06xTZnMgT8+q11Z9q8iht1yoQcfy7TF1Q="></Mermaid><h2 id="使用方法" tabindex="-1"><a class="header-anchor" href="#使用方法"><span>使用方法</span></a></h2>
<h3 id="基本语法" tabindex="-1"><a class="header-anchor" href="#基本语法"><span>基本语法</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>bmi-calculator &#x3C;身高> &#x3C;体重></span></span></code></pre>
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
<td>身高</td>
<td>数字</td>
<td>是</td>
<td>身高（厘米）</td>
<td>175</td>
</tr>
<tr>
<td>体重</td>
<td>数字</td>
<td>是</td>
<td>体重（斤）</td>
<td>145</td>
</tr>
</tbody>
</table>
<h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="正常体重计算" tabindex="-1"><a class="header-anchor" href="#正常体重计算"><span>正常体重计算</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">bmi-calculator 175 130</chat-message>
<chat-message nickname="bot" type="bot">
<p>您的BMI指数为21.2。<br>
正常体重是身体健康的一项标志，继续保持良好的生活习惯。</p>
</chat-message>
</chat-panel>
<h3 id="超重计算" tabindex="-1"><a class="header-anchor" href="#超重计算"><span>超重计算</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">bmi-calculator 170 160</chat-message>
<chat-message nickname="bot" type="bot">
<p>您的BMI指数为27.7。<br>
注意啦，您的体重是健康的，但身体已经不苗条了唔，适当锻炼很重要哦~</p>
</chat-message>
</chat-panel>
<h3 id="低体重计算" tabindex="-1"><a class="header-anchor" href="#低体重计算"><span>低体重计算</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">bmi-calculator 180 120</chat-message>
<chat-message nickname="bot" type="bot">
<p>您的BMI指数为18.5。<br>
您的体重稍轻，请适度增加营养摄入。</p>
</chat-message>
</chat-panel>
<h2 id="bmi标准范围" tabindex="-1"><a class="header-anchor" href="#bmi标准范围"><span>BMI标准范围</span></a></h2>
<table>
<thead>
<tr>
<th>BMI范围</th>
<th>分类</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt; 18.5</td>
<td>低体重</td>
<td>体重过轻，需要适当增加营养</td>
</tr>
<tr>
<td>18.5 - 24.9</td>
<td>正常体重</td>
<td>理想体重范围，继续保持</td>
</tr>
<tr>
<td>25 - 29.9</td>
<td>超重</td>
<td>体重偏重，建议适当控制</td>
</tr>
<tr>
<td>30 - 34.9</td>
<td>肥胖（一级）</td>
<td>需要调整饮食和锻炼计划</td>
</tr>
<tr>
<td>35 - 39.9</td>
<td>肥胖（二级）</td>
<td>建议咨询医生制定减重计划</td>
</tr>
<tr>
<td>≥ 40</td>
<td>肥胖（三级）</td>
<td>强烈建议寻求专业医疗帮助</td>
</tr>
</tbody>
</table>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<h3 id="计算算法" tabindex="-1"><a class="header-anchor" href="#计算算法"><span>计算算法</span></a></h3>
<ul>
<li><strong>BMI公式</strong>: BMI = 体重(kg) / 身高(m)²</li>
<li><strong>单位转换</strong>: 自动将体重从斤转换为千克，身高从厘米转换为米</li>
<li><strong>精度控制</strong>: BMI结果保留1位小数</li>
</ul>
<h3 id="输入验证" tabindex="-1"><a class="header-anchor" href="#输入验证"><span>输入验证</span></a></h3>
<ul>
<li><strong>数字检查</strong>: 确保身高和体重都是有效数字</li>
<li><strong>范围检查</strong>:
<ul>
<li>身高范围: 1-300厘米</li>
<li>体重范围: 1-1200斤</li>
</ul>
</li>
<li><strong>零值检查</strong>: 防止除零错误</li>
<li><strong>异常值检查</strong>: 过滤不合理的BMI计算结果</li>
</ul>
<h3 id="随机建议" tabindex="-1"><a class="header-anchor" href="#随机建议"><span>随机建议</span></a></h3>
<ul>
<li><strong>多样化提示</strong>: 每个BMI分类都有多个随机提示语</li>
<li><strong>个性化反馈</strong>: 根据BMI值提供针对性的健康建议</li>
</ul>
<h2 id="错误处理" tabindex="-1"><a class="header-anchor" href="#错误处理"><span>错误处理</span></a></h2>
<h3 id="输入错误" tabindex="-1"><a class="header-anchor" href="#输入错误"><span>输入错误</span></a></h3>
<ul>
<li><strong>缺少参数</strong>: 当未提供身高或体重时提示</li>
<li><strong>非数字输入</strong>: 当输入包含非数字字符时提示</li>
<li><strong>零值输入</strong>: 当身高或体重为0时提示</li>
<li><strong>超出范围</strong>: 当输入值超出合理范围时提示</li>
</ul>
<h3 id="计算错误" tabindex="-1"><a class="header-anchor" href="#计算错误"><span>计算错误</span></a></h3>
<ul>
<li><strong>异常结果</strong>: 当BMI计算结果异常时提示重新输入</li>
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
<td>underweight</td>
<td>string[]</td>
<td>多条提示语</td>
<td>低体重的健康建议</td>
</tr>
<tr>
<td>normal</td>
<td>string[]</td>
<td>多条提示语</td>
<td>正常体重的健康建议</td>
</tr>
<tr>
<td>overweight</td>
<td>string[]</td>
<td>多条提示语</td>
<td>超重的健康建议</td>
</tr>
<tr>
<td>moderately_obese</td>
<td>string[]</td>
<td>多条提示语</td>
<td>肥胖（一级）的健康建议</td>
</tr>
<tr>
<td>severely_obese</td>
<td>string[]</td>
<td>多条提示语</td>
<td>肥胖（二级）的健康建议</td>
</tr>
<tr>
<td>very_severely_obese</td>
<td>string[]</td>
<td>多条提示语</td>
<td>肥胖（三级）的健康建议</td>
</tr>
</tbody>
</table>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li><strong>单位说明</strong>: 体重单位为斤（1斤=0.5千克），身高单位为厘米</li>
<li><strong>适用范围</strong>: 主要适用于成年人BMI评估</li>
<li><strong>个体差异</strong>: BMI仅为参考指标，实际健康状况需结合其他因素</li>
<li><strong>专业建议</strong>: 对于极端BMI值，建议咨询专业医生</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>BMI（Body Mass Index）是国际上常用的衡量人体胖瘦程度以及是否健康的一个标准。通过简单的身高体重计算，可以快速了解自己的体重状况。</p>
</div>
</div></template>


