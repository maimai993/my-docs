<template><div><!DOCTYPE html>
<!-- saved from url=(0101)http://127.0.0.1/%E6%8F%92%E4%BB%B6%E5%B8%82%E5%9C%BA%20_%20Koishi%20%E6%8E%A7%E5%88%B6%E5%8F%B0.html -->
<html lang="zh" theme="default-dark" class="dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<pre><code>&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
&lt;script&gt;KOISHI_CONFIG = {&quot;devMode&quot;:false,&quot;uiPath&quot;:&quot;&quot;,&quot;heartbeat&quot;:{&quot;interval&quot;:30000,&quot;timeout&quot;:60000},&quot;endpoint&quot;:&quot;/status&quot;}&lt;/script&gt;&lt;title&gt;插件市场 | Koishi 控制台&lt;/title&gt;
&lt;link rel=&quot;icon&quot; href=&quot;http://110.42.70.166:5140/logo.png&quot;&gt;
&lt;script type=&quot;module&quot; crossorigin=&quot;&quot; src=&quot;./安装onebot_files/index.js.下载&quot;&gt;&lt;/script&gt;
&lt;link rel=&quot;stylesheet&quot; crossorigin=&quot;&quot; href=&quot;./安装onebot_files/style.css&quot;&gt;
</code></pre>
  <style type="text/css">x-vue-echarts,.echarts-inner{display:block;width:100%;height:100%;min-width:0}
</style><link rel="stylesheet" href="./安装onebot_files/style(1).css"><link rel="stylesheet" href="./安装onebot_files/style(2).css"><link rel="stylesheet" href="./安装onebot_files/style(3).css"><link rel="stylesheet" href="./安装onebot_files/style(4).css"><link rel="stylesheet" href="./安装onebot_files/style(5).css"><link rel="stylesheet" href="./安装onebot_files/style(6).css"><link rel="stylesheet" href="./安装onebot_files/style(7).css"><link rel="stylesheet" href="./安装onebot_files/style(8).css"><link rel="stylesheet" href="./安装onebot_files/style(9).css"><link rel="stylesheet" href="./安装onebot_files/style(10).css"><link rel="stylesheet" href="./安装onebot_files/style(11).css"><link rel="stylesheet" href="./安装onebot_files/style(12).css"><link rel="stylesheet" href="./安装onebot_files/style(13).css"><link rel="stylesheet" href="./安装onebot_files/style(14).css"><link rel="stylesheet" href="./安装onebot_files/style(15).css"><link rel="stylesheet" href="./安装onebot_files/style(16).css"><link rel="stylesheet" href="./安装onebot_files/style(17).css"><link rel="stylesheet" href="./安装onebot_files/style(18).css"><link rel="stylesheet" href="./安装onebot_files/style(19).css"><style data-id="immersive-translate-input-injected-css">.immersive-translate-input {
<p>position: absolute;<br>
top: 0;<br>
right: 0;<br>
left: 0;<br>
bottom: 0;<br>
z-index: 2147483647;<br>
display: flex;<br>
justify-content: center;<br>
align-items: center;<br>
}<br>
.immersive-translate-attach-loading::after {<br>
content: &quot; &quot;;</p>
<p>--loading-color: #f78fb6;<br>
width: 6px;<br>
height: 6px;<br>
border-radius: 50%;<br>
display: block;<br>
margin: 12px auto;<br>
position: relative;<br>
color: white;<br>
left: -100px;<br>
box-sizing: border-box;<br>
animation: immersiveTranslateShadowRolling 1.5s linear infinite;</p>
<p>position: absolute;<br>
top: 50%;<br>
left: 50%;<br>
transform: translate(-2000%, -50%);<br>
z-index: 100;<br>
}</p>
<p>.immersive-translate-loading-spinner {<br>
vertical-align: middle !important;<br>
width: 10px !important;<br>
height: 10px !important;<br>
display: inline-block !important;<br>
margin: 0 4px !important;<br>
border: 2px rgba(221, 244, 255, 0.6) solid !important;<br>
border-top: 2px rgba(0, 0, 0, 0.375) solid !important;<br>
border-left: 2px rgba(0, 0, 0, 0.375) solid !important;<br>
border-radius: 50% !important;<br>
padding: 0 !important;<br>
-webkit-animation: immersive-translate-loading-animation 0.6s infinite linear !important;<br>
animation: immersive-translate-loading-animation 0.6s infinite linear !important;<br>
}</p>
<p>@-webkit-keyframes immersive-translate-loading-animation {<br>
from {<br>
-webkit-transform: rotate(0deg);<br>
}</p>
<p>to {<br>
-webkit-transform: rotate(359deg);<br>
}<br>
}</p>
<p>@keyframes immersive-translate-loading-animation {<br>
from {<br>
transform: rotate(0deg);<br>
}</p>
<p>to {<br>
transform: rotate(359deg);<br>
}<br>
}</p>
<p>.immersive-translate-input-loading {<br>
--loading-color: #f78fb6;<br>
width: 6px;<br>
height: 6px;<br>
border-radius: 50%;<br>
display: block;<br>
margin: 12px auto;<br>
position: relative;<br>
color: white;<br>
left: -100px;<br>
box-sizing: border-box;<br>
animation: immersiveTranslateShadowRolling 1.5s linear infinite;<br>
}</p>
<p>@keyframes immersiveTranslateShadowRolling {<br>
0% {<br>
box-shadow: 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0),<br>
0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);<br>
}</p>
<p>12% {<br>
box-shadow: 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0),<br>
0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);<br>
}</p>
<p>25% {<br>
box-shadow: 110px 0 var(--loading-color), 100px 0 var(--loading-color),<br>
0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);<br>
}</p>
<p>36% {<br>
box-shadow: 120px 0 var(--loading-color), 110px 0 var(--loading-color),<br>
100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0);<br>
}</p>
<p>50% {<br>
box-shadow: 130px 0 var(--loading-color), 120px 0 var(--loading-color),<br>
110px 0 var(--loading-color), 100px 0 var(--loading-color);<br>
}</p>
<p>62% {<br>
box-shadow: 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color),<br>
120px 0 var(--loading-color), 110px 0 var(--loading-color);<br>
}</p>
<p>75% {<br>
box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),<br>
130px 0 var(--loading-color), 120px 0 var(--loading-color);<br>
}</p>
<p>87% {<br>
box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),<br>
200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color);<br>
}</p>
<p>100% {<br>
box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),<br>
200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0);<br>
}<br>
}</p>
<p>.immersive-translate-toast {<br>
display: flex;<br>
position: fixed;<br>
z-index: 2147483647;<br>
left: 0;<br>
right: 0;<br>
top: 1%;<br>
width: fit-content;<br>
padding: 12px 20px;<br>
margin: auto;<br>
overflow: auto;<br>
background: #fef6f9;<br>
box-shadow: 0px 4px 10px 0px rgba(0, 10, 30, 0.06);<br>
font-size: 15px;<br>
border-radius: 8px;<br>
color: #333;<br>
}</p>
<p>.immersive-translate-toast-content {<br>
display: flex;<br>
flex-direction: row;<br>
align-items: center;<br>
}</p>
<p>.immersive-translate-toast-hidden {<br>
margin: 0 20px 0 72px;<br>
text-decoration: underline;<br>
cursor: pointer;<br>
}</p>
<p>.immersive-translate-toast-close {<br>
color: #666666;<br>
font-size: 20px;<br>
font-weight: bold;<br>
padding: 0 10px;<br>
cursor: pointer;<br>
}</p>
<p>@media screen and (max-width: 768px) {<br>
.immersive-translate-toast {<br>
top: 0;<br>
padding: 12px 0px 0 10px;<br>
}<br>
.immersive-translate-toast-content {<br>
flex-direction: column;<br>
text-align: center;<br>
}<br>
.immersive-translate-toast-hidden {<br>
margin: 10px auto;<br>
}<br>
}</p>
<p>.immersive-translate-dialog {<br>
position: fixed;<br>
z-index: 2147483647;<br>
left: 0;<br>
top: 0;<br>
display: flex;<br>
width: 300px;<br>
flex-direction: column;<br>
align-items: center;<br>
font-size: 15px;<br>
left: 0;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
margin: auto;<br>
height: fit-content;<br>
border-radius: 20px;<br>
background-color: #fff;<br>
}</p>
<p>.immersive-translate-modal {<br>
display: none;<br>
position: fixed;<br>
z-index: 2147483647;<br>
left: 0;<br>
top: 0;<br>
width: 100%;<br>
height: 100%;<br>
overflow: auto;<br>
background-color: rgb(0, 0, 0);<br>
background-color: rgba(0, 0, 0, 0.4);<br>
font-size: 15px;<br>
}</p>
<p>.immersive-translate-modal-content {<br>
background-color: #fefefe;<br>
margin: 10% auto;<br>
padding: 40px 24px 24px;<br>
border-radius: 12px;<br>
width: 350px;<br>
font-family: system-ui, -apple-system, &quot;Segoe UI&quot;, &quot;Roboto&quot;, &quot;Ubuntu&quot;,<br>
&quot;Cantarell&quot;, &quot;Noto Sans&quot;, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;,<br>
&quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;;<br>
position: relative;<br>
}</p>
<p>@media screen and (max-width: 768px) {<br>
.immersive-translate-modal-content {<br>
margin: 25% auto !important;<br>
}<br>
}</p>
<p>@media screen and (max-width: 480px) {<br>
.immersive-translate-modal-content {<br>
width: 80vw !important;<br>
margin: 20vh auto !important;<br>
padding: 20px 12px 12px !important;<br>
}</p>
<p>.immersive-translate-modal-title {<br>
font-size: 14px !important;<br>
}</p>
<p>.immersive-translate-modal-body {<br>
font-size: 13px !important;<br>
max-height: 60vh !important;<br>
}</p>
<p>.immersive-translate-btn {<br>
font-size: 13px !important;<br>
padding: 8px 16px !important;<br>
margin: 0 4px !important;<br>
}</p>
<p>.immersive-translate-modal-footer {<br>
gap: 6px !important;<br>
margin-top: 16px !important;<br>
}<br>
}</p>
<p>.immersive-translate-modal .immersive-translate-modal-content-in-input {<br>
max-width: 500px;<br>
}<br>
.immersive-translate-modal-content-in-input .immersive-translate-modal-body {<br>
text-align: left;<br>
max-height: unset;<br>
}</p>
<p>.immersive-translate-modal-title {<br>
text-align: center;<br>
font-size: 16px;<br>
font-weight: 700;<br>
color: #333333;<br>
}</p>
<p>.immersive-translate-modal-body {<br>
text-align: center;<br>
font-size: 14px;<br>
font-weight: 400;<br>
color: #333333;<br>
margin-top: 24px;<br>
word-break: break-all;<br>
}</p>
<p>@media screen and (max-width: 768px) {<br>
.immersive-translate-modal-body {<br>
max-height: 250px;<br>
overflow-y: auto;<br>
}<br>
}</p>
<p>.immersive-translate-close {<br>
color: #666666;<br>
position: absolute;<br>
right: 16px;<br>
top: 16px;<br>
font-size: 20px;<br>
font-weight: bold;<br>
}</p>
<p>.immersive-translate-close:hover,<br>
.immersive-translate-close:focus {<br>
text-decoration: none;<br>
cursor: pointer;<br>
}</p>
<p>.immersive-translate-modal-footer {<br>
display: flex;<br>
justify-content: center;<br>
flex-wrap: wrap;<br>
margin-top: 24px;<br>
}</p>
<p>.immersive-translate-btn {<br>
width: fit-content;<br>
color: #fff;<br>
background-color: #ea4c89;<br>
border: none;<br>
font-size: 14px;<br>
margin: 0 8px;<br>
padding: 9px 30px;<br>
border-radius: 5px;<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
cursor: pointer;<br>
transition: background-color 0.3s ease;<br>
}</p>
<p>.immersive-translate-btn-container {<br>
display: flex;<br>
flex-direction: column;<br>
align-items: center;<br>
justify-content: center;<br>
gap: 8px;<br>
}</p>
<p>.immersive-translate-btn:hover {<br>
background-color: #f082ac;<br>
}<br>
.immersive-translate-btn:disabled {<br>
opacity: 0.6;<br>
cursor: not-allowed;<br>
}<br>
.immersive-translate-btn:disabled:hover {<br>
background-color: #ea4c89;<br>
}</p>
<p>.immersive-translate-link-btn {<br>
background-color: transparent;<br>
color: #ea4c89;<br>
border: none;<br>
cursor: pointer;<br>
height: 30px;<br>
line-height: 30px;<br>
}</p>
<p>.immersive-translate-cancel-btn {<br>
/* gray color */<br>
background-color: rgb(89, 107, 120);<br>
}</p>
<p>.immersive-translate-cancel-btn:hover {<br>
background-color: hsl(205, 20%, 32%);<br>
}</p>
<p>.immersive-translate-action-btn {<br>
background-color: transparent;<br>
color: #ea4c89;<br>
border: 1px solid #ea4c89;<br>
}</p>
<p>.immersive-translate-btn svg {<br>
margin-right: 5px;<br>
}</p>
<p>.immersive-translate-link {<br>
cursor: pointer;<br>
user-select: none;<br>
-webkit-user-drag: none;<br>
text-decoration: none;<br>
color: #ea4c89;<br>
-webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);<br>
}</p>
<p>.immersive-translate-primary-link {<br>
cursor: pointer;<br>
user-select: none;<br>
-webkit-user-drag: none;<br>
text-decoration: none;<br>
color: #ea4c89;<br>
-webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);<br>
}</p>
<p>.immersive-translate-modal input[type=&quot;radio&quot;] {<br>
margin: 0 6px;<br>
cursor: pointer;<br>
}</p>
<p>.immersive-translate-modal label {<br>
cursor: pointer;<br>
}</p>
<p>.immersive-translate-close-action {<br>
position: absolute;<br>
top: 2px;<br>
right: 0px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-image-status {<br>
background-color: rgba(0, 0, 0, 0.5) !important;<br>
display: flex !important;<br>
flex-direction: column !important;<br>
align-items: center !important;<br>
justify-content: center !important;<br>
border-radius: 16px !important;<br>
}<br>
.imt-image-status img,<br>
.imt-image-status svg,<br>
.imt-img-loading {<br>
width: 28px !important;<br>
height: 28px !important;<br>
margin: 0 0 8px 0 !important;<br>
min-height: 28px !important;<br>
min-width: 28px !important;<br>
position: relative !important;<br>
}<br>
.imt-img-loading {<br>
background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAMAAACfWMssAAAAtFBMVEUAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////oK74hAAAAPHRSTlMABBMIDyQXHwyBfFdDMSw+OjXCb+5RG51IvV/k0rOqlGRM6KKMhdvNyZBz9MaupmxpWyj437iYd/yJVNZeuUC7AAACt0lEQVRIx53T2XKiUBCA4QYOiyCbiAsuuGBcYtxiYtT3f6/pbqoYHVFO5r+iivpo6DpAWYpqeoFfr9f90DsYAuRSWkFnPO50OgR9PwiCUFcl2GEcx+N/YBh6pvKaefHlUgZd1zVe0NbYcQjGBfzrPE8Xz8aF+71D8gG6DHFPpc4a7xFiCDuhaWgKgGIJQ3d5IMGDrpS4S5KgpIm+en9f6PlAhKby4JwEIxlYJV9h5k5nee9GoxHJ2IDSNB0dwdad1NAxDJ/uXDHYmebdk4PdbkS58CIVHdYSUHTYYRWOJblWSyu2lmy3KNFVJNBhxcuGW4YBVCbYGRZwIooipHsNqjM4FbgOQqQqSKQQU9V8xmi1QlgHqQQ6DDBvRUVCDirs+EzGDGOQTCATgtYTnbCVLgsVgRE0T1QE0qHCFAht2z6dLvJQs3Lo2FQoDxWNUiBhaP4eRgwNkI+dAjVOA/kUrIDwf3CG8NfNOE0eiFotSuo+rBiq8tD9oY4Qzc6YJw99hl1wzpQvD7ef2M8QgnOGJfJw+EltQc+oX2yn907QB22WZcvlUpd143dqQu+8pCJZuGE4xCuPXJqqcs5sNpsI93Rmzym1k4Npk+oD1SH3/a3LOK/JpUBpWfqNySxWzCfNCUITuDG5dtuphrUJ1myeIE9bIsPiKrfqTai5WZxbhtNphYx6GEIHihyGFTI69lje/rxajdh0s0msZ0zYxyPLhYCb1CyHm9Qsd2H37Y3lugVwL9kNh8Ot8cha6fUNQ8nuXi5z9/ExsAO4zQrb/ev1yrCB7lGyQzgYDGuxq1toDN/JGvN+HyWNHKB7zEoK+PX11e12G431erGYzwmytAWU56fkMHY5JJnDRR2eZji3AwtIcrEV8Cojat/BdQ7XOwGV1e1hDjGGjXbdArm8uJZtCH5MbcctVX8A1WpqumJHwckAAAAASUVORK5CYII=&quot;);<br>
background-size: 28px 28px;<br>
animation: image-loading-rotate 1s linear infinite !important;<br>
}</p>
<p>.imt-image-status span {<br>
color: var(--bg-2, #fff) !important;<br>
font-size: 14px !important;<br>
line-height: 14px !important;<br>
font-weight: 500 !important;<br>
font-family: &quot;PingFang SC&quot;, Arial, sans-serif !important;<br>
}</p>
<p>.imt-primary-button {<br>
display: flex;<br>
padding: 12px 80px;<br>
justify-content: center;<br>
align-items: center;<br>
gap: 8px;<br>
border-radius: 8px;<br>
background: #ea4c89;<br>
color: #fff;<br>
font-size: 16px;<br>
font-style: normal;<br>
font-weight: 700;<br>
line-height: 24px;<br>
border: none;<br>
cursor: pointer;<br>
}</p>
<p>.imt-retry-text {<br>
color: #999;<br>
text-align: center;<br>
font-size: 14px;<br>
font-style: normal;<br>
font-weight: 400;<br>
line-height: 21px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-action-container {<br>
display: flex;<br>
flex-direction: column;<br>
gap: 12px;<br>
}</p>
<p>.imt-modal-content-text {<br>
text-align: left;<br>
color: #333;<br>
font-size: 16px;<br>
font-weight: 400;<br>
line-height: 24px;<br>
}</p>
<p>@keyframes image-loading-rotate {<br>
from {<br>
transform: rotate(360deg);<br>
}<br>
to {<br>
transform: rotate(0deg);<br>
}<br>
}</p>
<p>.imt-linear-gradient-text {<br>
background: linear-gradient(90deg, #00a6ff 0%, #c369ff 52.4%, #ff4590 100%);<br>
background-clip: text;<br>
-webkit-background-clip: text;<br>
-webkit-text-fill-color: transparent;<br>
}</p>
<p>.imt-flex-center {<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
}</p>
<p>.imt-linear-black-btn {<br>
border-radius: 50px;<br>
background: linear-gradient(66deg, #222 19%, #696969 94.25%);<br>
height: 48px;<br>
width: 100%;<br>
color: #fff;<br>
font-size: 16px;<br>
font-weight: 700;<br>
display: flex;<br>
align-items: center;<br>
cursor: pointer;<br>
justify-content: center;<br>
}</p>
</style></head>
  <body class="">
    <div id="app" data-v-app=""><nav data-v-a101f417="" class="layout-activity flex flex-col justify-evenly"><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" viewBox="-64 0 1152 1024" xmlns="http://www.w3.org/2000/svg"><!-- make it a little wider --><path d="M512,64c60.51,0,119.17,11.84,174.36,35.18,53.34,22.56,101.26,54.87,142.42,96.04,41.16,41.16,73.48,89.08,96.04,142.42,23.34,55.19,35.18,113.85,35.18,174.36s-11.84,119.17-35.18,174.36c-22.56,53.34-54.87,101.26-96.04,142.42-41.16,41.16-89.08,73.48-142.42,96.04-55.19,23.34-113.85,35.18-174.36,35.18s-119.17-11.84-174.36-35.18c-53.34-22.56-101.26-54.87-142.42-96.04-41.16-41.16-73.48-89.08-96.04-142.42-23.34-55.19-35.18-113.85-35.18-174.36s11.84-119.17,35.18-174.36c22.56-53.34,54.87-101.26,96.04-142.42s89.08-73.48,142.42-96.04c55.19-23.34,113.85-35.18,174.36-35.18m0-64C229.23,0,0,229.23,0,512s229.23,512,512,512,512-229.23,512-512S794.77,0,512,0h0Z" style="fill:currentColor;"></path><line x1="678.29" y1="676.29" x2="742.29" y2="740.29" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:64px;"></line><line x1="816" y1="416" x2="872" y2="416" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px;"></line><path d="M816,304c0,283-229,512-512,512" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:64px;"></path><line x1="416" y1="872" x2="416" y2="816" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px;"></line><line x1="760" y1="552" x2="840" y2="585.14" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:56px;"></line><line x1="552" y1="760" x2="585.14" y2="840" style="fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:56px;"></line></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/plugins/0fok7g" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M168 255.1C168 207.4 207.4 167.1 256 167.1C304.6 167.1 344 207.4 344 255.1C344 304.6 304.6 344 256 344C207.4 344 168 304.6 168 255.1zM256 199.1C225.1 199.1 200 225.1 200 255.1C200 286.9 225.1 311.1 256 311.1C286.9 311.1 312 286.9 312 255.1C312 225.1 286.9 199.1 256 199.1zM65.67 230.6L25.34 193.8C14.22 183.7 11.66 167.2 19.18 154.2L49.42 101.8C56.94 88.78 72.51 82.75 86.84 87.32L138.8 103.9C152.2 93.56 167 84.96 182.8 78.43L194.5 25.16C197.7 10.47 210.7 0 225.8 0H286.2C301.3 0 314.3 10.47 317.5 25.16L329.2 78.43C344.1 84.96 359.8 93.56 373.2 103.9L425.2 87.32C439.5 82.75 455.1 88.78 462.6 101.8L492.8 154.2C500.3 167.2 497.8 183.7 486.7 193.8L446.3 230.6C447.4 238.9 448 247.4 448 255.1C448 264.6 447.4 273.1 446.3 281.4L486.7 318.2C497.8 328.3 500.3 344.8 492.8 357.8L462.6 410.2C455.1 423.2 439.5 429.2 425.2 424.7L373.2 408.1C359.8 418.4 344.1 427 329.2 433.6L317.5 486.8C314.3 501.5 301.3 512 286.2 512H225.8C210.7 512 197.7 501.5 194.5 486.8L182.8 433.6C167 427 152.2 418.4 138.8 408.1L86.84 424.7C72.51 429.2 56.94 423.2 49.42 410.2L19.18 357.8C11.66 344.8 14.22 328.3 25.34 318.2L65.67 281.4C64.57 273.1 64 264.6 64 255.1C64 247.4 64.57 238.9 65.67 230.6V230.6zM158.4 129.2L145.1 139.5L77.13 117.8L46.89 170.2L99.58 218.2L97.39 234.8C96.47 241.7 96 248.8 96 255.1C96 263.2 96.47 270.3 97.39 277.2L99.58 293.8L46.89 341.8L77.13 394.2L145.1 372.5L158.4 382.8C169.5 391.4 181.9 398.6 195 403.1L210.5 410.4L225.8 480H286.2L301.5 410.4L316.1 403.1C330.1 398.6 342.5 391.4 353.6 382.8L366.9 372.5L434.9 394.2L465.1 341.8L412.4 293.8L414.6 277.2C415.5 270.3 416 263.2 416 256C416 248.8 415.5 241.7 414.6 234.8L412.4 218.2L465.1 170.2L434.9 117.8L366.9 139.5L353.6 129.2C342.5 120.6 330.1 113.4 316.1 108L301.5 101.6L286.2 32H225.8L210.5 101.6L195 108C181.9 113.4 169.5 120.6 158.4 129.2H158.4z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item active"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/market?keyword=adapter-onebot" class="active router-link-exact-active activity-button el-tooltip__trigger" draggable="true" aria-current="page"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M448 208c-18.53 0-36.09 10-48.16 27.42C398.9 236.8 396.3 240 392.4 240C387.8 240 384 236.3 384 231.6V176C384 149.5 362.5 128 336 128l-55.64 0C275.8 127.1 272 124.3 272 119.6c0-3.906 3.188-6.531 4.547-7.484C293.1 100.1 304 82.55 304 64c0-35.3-35.89-64-80-64S144 28.7 144 64c0 18.55 9.1 36.09 27.42 48.14C172.8 113.1 176 115.7 176 119.6c0 4.609-3.75 8.359-8.359 8.359L48 128C21.53 128 0 149.5 0 176v55.64C0 253.9 18.11 272 40.36 272c13.2 0 25.84-6.859 33.8-18.36C77.69 248.5 85.2 240 96 240c17.34 0 32 21.98 32 48s-14.66 48-32 48c-10.8 0-18.31-8.547-21.86-13.67C66.19 310.9 53.55 304 40.36 304C18.11 304 0 322.1 0 344.4V464C0 490.5 21.53 512 48 512h119.6C189.9 512 208 493.9 208 471.6c0-13.19-6.859-25.83-18.36-33.8C184.5 434.3 176 426.8 176 416c0-17.34 21.98-32 48-32s48 14.66 48 32c0 10.8-8.547 18.31-13.66 21.84C246.9 445.8 240 458.4 240 471.6C240 493.9 258.1 512 280.4 512H336c26.47 0 48-21.53 48-48v-119.6c0-4.609 3.75-8.358 8.359-8.358c3.906 0 6.547 3.203 7.484 4.547C411.9 358 429.5 368 448 368c35.3 0 64-35.89 64-80S483.3 208 448 208zM448 336c-10.8 0-18.31-8.547-21.86-13.67C418.2 310.9 405.5 304 392.4 304C370.1 304 352 322.1 352 344.4V464c0 8.828-7.172 16-16 16h-55.64C275.8 480 272 476.3 272 471.6c0-3.906 3.188-6.531 4.547-7.484C293.1 452.1 304 434.5 304 416c0-35.3-35.89-64-80-64s-80 28.7-80 64c0 18.55 9.1 36.09 27.42 48.14C172.8 465.1 176 467.7 176 471.6C176 476.3 172.3 480 167.6 480H48C39.17 480 32 472.8 32 464v-119.6C32 339.8 35.75 336 40.36 336c3.906 0 6.547 3.203 7.484 4.547C59.91 358 77.45 368 96 368c35.3 0 64-35.89 64-80S131.3 208 96 208c-18.53 0-36.09 10-48.16 27.42C46.89 236.8 44.25 240 40.36 240C35.75 240 32 236.3 32 231.6V176C32 167.2 39.17 160 48 160h119.6C189.9 160 208 141.9 208 119.6c0-13.19-6.859-25.83-18.36-33.8C184.5 82.31 176 74.8 176 64c0-17.34 21.98-32 48-32s48 14.66 48 32c0 10.8-8.547 18.31-13.66 21.84C246.9 93.8 240 106.4 240 119.6C240 141.9 258.1 160 280.4 160H336C344.8 160 352 167.2 352 176v55.64C352 253.9 370.1 272 392.4 272c13.2 0 25.84-6.859 33.8-18.36C429.7 248.5 437.2 240 448 240c17.34 0 32 21.98 32 48S465.3 336 448 336z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/dependencies" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M320 77.23L559.6 49.48C573.7 47.85 587.2 55.65 592.7 68.66L624.7 143.3C634.6 166.2 621.3 192.4 596.1 198L437.8 234.8C418.8 239.1 399.2 231.7 387.9 215.9L320 120.9L252.1 215.9C240.8 231.7 221.2 239.1 202.3 234.8L43.04 198C18.75 192.4 5.449 166.2 15.27 143.3L47.26 68.66C52.84 55.65 66.3 47.85 80.36 49.48L320 77.23zM44.68 155.9C42.72 160.5 45.38 165.7 50.24 166.9L209.4 203.6C215.7 205.1 222.3 202.6 226.1 197.3L291.2 106.1L76.68 81.27L44.68 155.9zM413.9 197.3C417.7 202.6 424.3 205.1 430.6 203.6L589.8 166.9C594.6 165.7 597.3 160.5 595.3 155.9L563.3 81.27L348.8 106.1L413.9 197.3zM544 236.7L576 227.6V378.5C576 400.5 561 419.7 539.6 425.1L331.6 477.1C324 479 316 479 308.4 477.1L100.4 425.1C78.99 419.7 64 400.5 64 378.5V227.6L96 236.7V378.5C96 385.9 100.1 392.3 108.1 394L304 443V207.1C304 199.2 311.2 191.1 320 191.1C328.8 191.1 336 199.2 336 207.1V443L531.9 394C539 392.3 544 385.9 544 378.5L544 236.7z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/files/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M336 480H96c-35.35 0-64-28.65-64-64V112C32 103.2 24.84 96 16 96S0 103.2 0 112V416c0 53.02 42.98 96 96 96h240c8.836 0 16-7.164 16-16S344.8 480 336 480zM429.3 113.3l-94.51-94.51C322.7 6.742 306.5 0 289.5 0H160C124.7 0 96 28.65 96 64l.0098 288c0 35.35 28.65 64 64 64h224C419.4 416 448 387.3 448 352V158.5C448 141.5 441.3 125.3 429.3 113.3zM320 49.25L398.8 128H336C327.2 128 320 120.8 320 112V49.25zM416 352c0 17.64-14.36 32-32 32H160c-17.64 0-32-14.36-32-32V64c0-17.64 14.36-32 32-32h128v80C288 138.5 309.5 160 336 160H416V352z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/graph" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M160 64C160 28.65 188.7 0 224 0C259.3 0 288 28.65 288 64C288 83.36 279.4 100.7 265.8 112.5L304.3 196.5C314.4 193.6 325 192 336 192C367.7 192 396.2 205.1 416.6 226.2L517.4 153.7C513.9 145.8 512 137.1 512 128C512 92.65 540.7 64 576 64C611.3 64 640 92.65 640 128C640 163.3 611.3 192 576 192C561.4 192 547.9 187.1 537.2 178.9L435.3 252.2C443.4 267.7 448 285.3 448 304C448 319.4 444.9 334 439.3 347.3L531.1 402.4C542.6 391 558.5 384 576 384C611.3 384 640 412.7 640 448C640 483.3 611.3 512 576 512C540.7 512 512 483.3 512 448C512 441.7 512.9 435.6 514.6 429.8L422.8 374.8C402.3 399.9 371 416 336 416C279.6 416 232.9 374.3 225.1 320H125.1C118.9 347.6 93.82 368 64 368C28.65 368 0 339.3 0 304C0 268.7 28.65 240 64 240C93.82 240 118.9 260.4 125.1 288H225.1C229.8 255.3 248.7 227.1 275.3 209.9L237.1 126.7C232.9 127.5 228.5 128 224 128C188.7 128 160 99.35 160 64V64zM224 96C241.7 96 256 81.67 256 64C256 46.33 241.7 32 224 32C206.3 32 192 46.33 192 64C192 81.67 206.3 96 224 96zM576 160C593.7 160 608 145.7 608 128C608 110.3 593.7 96 576 96C558.3 96 544 110.3 544 128C544 145.7 558.3 160 576 160zM576 416C558.3 416 544 430.3 544 448C544 465.7 558.3 480 576 480C593.7 480 608 465.7 608 448C608 430.3 593.7 416 576 416zM64 336C81.67 336 96 321.7 96 304C96 286.3 81.67 272 64 272C46.33 272 32 286.3 32 304C32 321.7 46.33 336 64 336zM336 384C380.2 384 416 348.2 416 304C416 259.8 380.2 224 336 224C291.8 224 256 259.8 256 304C256 348.2 291.8 384 336 384z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/locales/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M386.7 22.63C411.7-2.365 452.3-2.365 477.3 22.63L489.4 34.74C514.4 59.74 514.4 100.3 489.4 125.3L269 345.6C260.6 354.1 249.9 359.1 238.2 362.7L147.6 383.6C142.2 384.8 136.6 383.2 132.7 379.3C128.8 375.4 127.2 369.8 128.4 364.4L149.3 273.8C152 262.1 157.9 251.4 166.4 242.1L386.7 22.63zM454.6 45.26C442.1 32.76 421.9 32.76 409.4 45.26L382.6 72L440 129.4L466.7 102.6C479.2 90.13 479.2 69.87 466.7 57.37L454.6 45.26zM180.5 281L165.3 346.7L230.1 331.5C236.8 330.2 242.2 327.2 246.4 322.1L417.4 152L360 94.63L189 265.6C184.8 269.8 181.8 275.2 180.5 281V281zM208 64C216.8 64 224 71.16 224 80C224 88.84 216.8 96 208 96H80C53.49 96 32 117.5 32 144V432C32 458.5 53.49 480 80 480H368C394.5 480 416 458.5 416 432V304C416 295.2 423.2 288 432 288C440.8 288 448 295.2 448 304V432C448 476.2 412.2 512 368 512H80C35.82 512 0 476.2 0 432V144C0 99.82 35.82 64 80 64H208z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/commands/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M368 320H320V192h48C412.2 192 448 156.2 448 112C448 67.82 412.2 32 368 32S288 67.82 288 112V160H160V112C160 67.82 124.2 32 80 32S0 67.82 0 112C0 156.2 35.82 192 80 192H128v128H80C35.82 320 0 355.8 0 400C0 444.2 35.82 480 80 480S160 444.2 160 400V352h128v48c0 44.18 35.82 80 80 80s80-35.82 80-80C448 355.8 412.2 320 368 320zM320 112C320 85.53 341.5 64 368 64S416 85.53 416 112S394.5 160 368 160H320V112zM128 400C128 426.5 106.5 448 80 448S32 426.5 32 400S53.53 352 80 352H128V400zM128 160H80C53.53 160 32 138.5 32 112S53.53 64 80 64S128 85.53 128 112V160zM288 320H160V192h128V320zM368 448c-26.47 0-48-21.53-48-48V352h48c26.47 0 48 21.53 48 48S394.5 448 368 448z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/database/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M224 512C100.3 512 0 476.2 0 432V80C0 35.82 100.3 0 224 0C347.7 0 448 35.82 448 80V432C448 476.2 347.7 512 224 512zM416 80.45C415.7 79.69 414.4 77.27 409.8 73.31C402.4 67.11 389.9 60.09 371.6 53.57C335.4 40.62 283.2 32 224 32C164.8 32 112.6 40.62 76.37 53.57C58.1 60.09 45.59 67.11 38.25 73.31C33.55 77.27 32.29 79.69 32 80.45V182.1C46.47 192.7 69.9 202.8 100.9 210.4C135.5 218.9 177.1 224 224 224C270 224 312.5 218.9 347.1 210.4C378.1 202.8 401.5 192.7 416 182.1V80.45zM416 219.5C398.8 228.4 377.9 235.8 354.8 241.5C317.3 250.7 272.2 256 224 256C175.8 256 130.7 250.7 93.22 241.5C70.11 235.8 49.18 228.4 32 219.5V310.1C46.47 320.7 69.9 330.8 100.9 338.4C135.5 346.9 177.1 352 224 352C270 352 312.5 346.9 347.1 338.4C378.1 330.8 401.5 320.7 416 310.1V219.5zM38.25 438.7C45.59 444.9 58.1 451.9 76.37 458.4C112.6 471.4 164.8 480 224 480C283.2 480 335.4 471.4 371.6 458.4C389.9 451.9 402.4 444.9 409.8 438.7C414.4 434.7 415.7 432.3 416 431.6V347.5C398.8 356.4 377.9 363.8 354.8 369.5C317.3 378.7 272.2 384 224 384C175.8 384 130.7 378.7 93.22 369.5C70.11 363.8 49.18 356.4 32 347.5V431.6C32.29 432.3 33.55 434.7 38.25 438.7zM416 431.4C416.1 431.3 416.1 431.3 416.1 431.3L416 431.4zM31.96 431.4C31.94 431.3 31.93 431.3 31.92 431.3L31.96 431.4zM31.96 80.56C31.93 80.65 31.92 80.7 31.92 80.7L31.96 80.56zM416.1 80.7C416.1 80.7 416.1 80.65 416 80.56z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/admin/" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="currentColor" d="M274.7 304H173.3c-95.73 0-173.3 77.6-173.3 173.3C0 496.5 15.52 512 34.66 512H413.3C432.5 512 448 496.5 448 477.3C448 381.6 370.4 304 274.7 304zM413.3 480H34.66C33.2 480 32 478.8 32 477.3C32 399.4 95.4 336 173.3 336H274.7C352.6 336 416 399.4 416 477.3C416 478.8 414.8 480 413.3 480zM224 256c70.7 0 128-57.31 128-128S294.7 0 224 0C153.3 0 96 57.31 96 128S153.3 256 224 256zM224 32c52.94 0 96 43.06 96 96c0 52.93-43.06 96-96 96S128 180.9 128 128C128 75.06 171.1 32 224 32zM375.1 241C392.9 250.8 412.3 256 432 256C493.8 256 544 205.8 544 144S493.8 32 432 32c-12.83 0-25.39 2.156-37.34 6.391c-8.328 2.953-12.69 12.09-9.734 20.42c2.953 8.344 12.12 12.66 20.42 9.734C413.9 65.53 422.8 64 432 64C476.1 64 512 99.89 512 144S476.1 224 432 224c-14.08 0-27.91-3.703-39.98-10.69c-7.656-4.453-17.44-1.828-21.86 5.828C365.7 226.8 368.3 236.6 375.1 241zM490.7 320H448c-8.844 0-16 7.156-16 16S439.2 352 448 352h42.67C555.4 352 608 404.6 608 469.3C608 475.2 603.2 480 597.3 480H496c-8.844 0-16 7.156-16 16s7.156 16 16 16h101.3C620.9 512 640 492.9 640 469.3C640 386.1 573 320 490.7 320z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/sandbox" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M437.2 403.5L319.1 215l.0001-135C319.1 71.16 312.8 64 303.1 64S288 71.16 288 79.1L287.1 215c0 5.973 1.672 11.83 4.826 16.9L347.6 320H100.4l54.79-88.1C158.3 226.8 160 220.1 160 215L160 79.1C160 71.16 152.8 64 144 64S128 71.16 128 79.1L128 215l-117.2 188.5C-18.48 450.6 15.27 512 70.89 512h306.2C432.7 512 466.5 450.5 437.2 403.5zM410.9 460C407.6 466 397.6 480 377.1 480H70.89c-20.51 0-30.48-13.95-33.82-19.95c-7.025-12.63-6.691-27.46 .873-39.65L80.48 352h287l42.55 68.41C417.6 432.6 417.1 447.4 410.9 460zM112 32h224C344.8 32 352 24.84 352 16S344.8 0 336 0h-224C103.2 0 96 7.156 96 16S103.2 32 112 32z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><span data-v-b2f2e6e3="" class="activity-button is-group el-tooltip__trigger el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M352 256C352 238.3 366.3 224 384 224C401.7 224 416 238.3 416 256C416 273.7 401.7 288 384 288C366.3 288 352 273.7 352 256zM192 256C192 238.3 206.3 224 224 224C241.7 224 256 238.3 256 256C256 273.7 241.7 288 224 288C206.3 288 192 273.7 192 256zM96 256C96 273.7 81.67 288 64 288C46.33 288 32 273.7 32 256C32 238.3 46.33 224 64 224C81.67 224 96 238.3 96 256z"></path></svg></span></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div><div data-v-a101f417="" class="activity-item"><a data-v-b2f2e6e3="" href="http://110.42.70.166:5140/profile" class="activity-button el-tooltip__trigger" draggable="true"><svg data-v-b2f2e6e3="" class="k-icon activity-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M256 0C114.6 0 0 114.6 0 256s114.6 256 256 256s256-114.6 256-256S397.4 0 256 0zM256 480c-47.24 0-91.04-14.78-127.2-39.84C132.9 390.9 173.8 352 224 352h64c50.25 0 91.14 38.94 95.21 88.16C347 465.2 303.2 480 256 480zM411.7 416.7C397.6 361.3 347.7 320 288 320H224c-59.73 0-109.6 41.3-123.7 96.72C58.27 375.1 32 319 32 256c0-123.5 100.5-224 224-224s224 100.5 224 224C480 319 453.7 375.1 411.7 416.7zM256 128C211.8 128 176 163.8 176 208C176 252.2 211.8 288 256 288s80-35.82 80-80C336 163.8 300.2 128 256 128zM256 256C229.5 256 208 234.5 208 208S229.5 160 256 160s48 21.53 48 48S282.5 256 256 256z"></path></svg></a></div><div data-v-529cafc9="" data-v-a101f417="" class="separator"></div></nav><div class="layout-container has-left-aside page-market"><aside class="layout-aside layout-left"><div class="el-scrollbar"><div class="el-scrollbar__wrap el-scrollbar__wrap--hidden-default"><div class="el-scrollbar__view" style=""><div data-v-75c8400c="" class="market-filter-group"><div data-v-75c8400c="" class="market-filter-title"><h2 data-v-75c8400c="" class="text">排序</h2></div><div data-v-75c8400c="" class="market-filter-item active"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M489.1 363.3l-24.03 41.59c-6.635 11.48-21.33 15.41-32.82 8.78l-129.1-74.56V488c0 13.25-10.75 24-24.02 24H231.1c-13.27 0-24.02-10.75-24.02-24v-148.9L78.87 413.7c-11.49 6.629-26.19 2.698-32.82-8.78l-24.03-41.59c-6.635-11.48-2.718-26.14 8.774-32.77L159.9 256L30.8 181.5C19.3 174.8 15.39 160.2 22.02 148.7l24.03-41.59c6.635-11.48 21.33-15.41 32.82-8.781l129.1 74.56L207.1 24c0-13.25 10.75-24 24.02-24h48.04c13.27 0 24.02 10.75 24.02 24l.0005 148.9l129.1-74.56c11.49-6.629 26.19-2.698 32.82 8.78l24.02 41.59c6.637 11.48 2.718 26.14-8.774 32.77L352.1 256l129.1 74.53C492.7 337.2 496.6 351.8 489.1 363.3z"></path></svg></span><span data-v-75c8400c="" class="text">综合</span><span data-v-75c8400c="" class="spacer"></span><span data-v-75c8400c="" class="order"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M416 288h-95.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H416c17.67 0 32-14.33 32-32S433.7 288 416 288zM352 416h-32c-17.67 0-32 14.33-32 32s14.33 32 32 32h32c17.67 0 31.1-14.33 31.1-32S369.7 416 352 416zM480 160h-159.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H480c17.67 0 32-14.33 32-32S497.7 160 480 160zM544 32h-223.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H544c17.67 0 32-14.33 32-32S561.7 32 544 32zM151.6 41.95c-12.12-13.26-35.06-13.26-47.19 0l-87.1 96.09C4.475 151.1 5.35 171.4 18.38 183.3c6.141 5.629 13.89 8.414 21.61 8.414c8.672 0 17.3-3.504 23.61-10.39L96 145.9v302C96 465.7 110.3 480 128 480s32-14.33 32-32.03V145.9L192.4 181.3C204.4 194.3 224.6 195.3 237.6 183.3c13.03-11.95 13.9-32.22 1.969-45.27L151.6 41.95z"></path></svg></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg></span><span data-v-75c8400c="" class="text">按评分</span><span data-v-75c8400c="" class="spacer"></span><span data-v-75c8400c="" class="order"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M416 288h-95.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H416c17.67 0 32-14.33 32-32S433.7 288 416 288zM352 416h-32c-17.67 0-32 14.33-32 32s14.33 32 32 32h32c17.67 0 31.1-14.33 31.1-32S369.7 416 352 416zM480 160h-159.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H480c17.67 0 32-14.33 32-32S497.7 160 480 160zM544 32h-223.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H544c17.67 0 32-14.33 32-32S561.7 32 544 32zM151.6 41.95c-12.12-13.26-35.06-13.26-47.19 0l-87.1 96.09C4.475 151.1 5.35 171.4 18.38 183.3c6.141 5.629 13.89 8.414 21.61 8.414c8.672 0 17.3-3.504 23.61-10.39L96 145.9v302C96 465.7 110.3 480 128 480s32-14.33 32-32.03V145.9L192.4 181.3C204.4 194.3 224.6 195.3 237.6 183.3c13.03-11.95 13.9-32.22 1.969-45.27L151.6 41.95z"></path></svg></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M480 352h-133.5l-45.25 45.25C289.2 409.3 273.1 416 256 416s-33.16-6.656-45.25-18.75L165.5 352H32c-17.67 0-32 14.33-32 32v96c0 17.67 14.33 32 32 32h448c17.67 0 32-14.33 32-32v-96C512 366.3 497.7 352 480 352zM432 456c-13.2 0-24-10.8-24-24c0-13.2 10.8-24 24-24s24 10.8 24 24C456 445.2 445.2 456 432 456zM233.4 374.6C239.6 380.9 247.8 384 256 384s16.38-3.125 22.62-9.375l128-128c12.49-12.5 12.49-32.75 0-45.25c-12.5-12.5-32.76-12.5-45.25 0L288 274.8V32c0-17.67-14.33-32-32-32C238.3 0 224 14.33 224 32v242.8L150.6 201.4c-12.49-12.5-32.75-12.5-45.25 0c-12.49 12.5-12.49 32.75 0 45.25L233.4 374.6z"></path></svg></span><span data-v-75c8400c="" class="text">按下载量</span><span data-v-75c8400c="" class="spacer"></span><span data-v-75c8400c="" class="order"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M416 288h-95.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H416c17.67 0 32-14.33 32-32S433.7 288 416 288zM352 416h-32c-17.67 0-32 14.33-32 32s14.33 32 32 32h32c17.67 0 31.1-14.33 31.1-32S369.7 416 352 416zM480 160h-159.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H480c17.67 0 32-14.33 32-32S497.7 160 480 160zM544 32h-223.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H544c17.67 0 32-14.33 32-32S561.7 32 544 32zM151.6 41.95c-12.12-13.26-35.06-13.26-47.19 0l-87.1 96.09C4.475 151.1 5.35 171.4 18.38 183.3c6.141 5.629 13.89 8.414 21.61 8.414c8.672 0 17.3-3.504 23.61-10.39L96 145.9v302C96 465.7 110.3 480 128 480s32-14.33 32-32.03V145.9L192.4 181.3C204.4 194.3 224.6 195.3 237.6 183.3c13.03-11.95 13.9-32.22 1.969-45.27L151.6 41.95z"></path></svg></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M352.4 243.8l-49.83 99.5c-6.009 12-23.41 11.62-28.92-.625L216.7 216.3l-30.05 71.75L88.55 288l176.4 182.2c12.66 13.07 33.36 13.07 46.03 0l176.4-182.2l-112.1 .0052L352.4 243.8zM495.2 62.86c-54.36-46.98-137.5-38.5-187.5 13.06L288 96.25L268.3 75.92C218.3 24.36 135.2 15.88 80.81 62.86C23.37 112.5 16.84 197.6 60.18 256h105l35.93-86.25c5.508-12.88 23.66-13.12 29.54-.375l58.21 129.4l49.07-98c5.884-11.75 22.78-11.75 28.67 0l27.67 55.25h121.5C559.2 197.6 552.6 112.5 495.2 62.86z"></path></svg></span><span data-v-75c8400c="" class="text">按创建时间</span><span data-v-75c8400c="" class="spacer"></span><span data-v-75c8400c="" class="order"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M416 288h-95.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H416c17.67 0 32-14.33 32-32S433.7 288 416 288zM352 416h-32c-17.67 0-32 14.33-32 32s14.33 32 32 32h32c17.67 0 31.1-14.33 31.1-32S369.7 416 352 416zM480 160h-159.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H480c17.67 0 32-14.33 32-32S497.7 160 480 160zM544 32h-223.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H544c17.67 0 32-14.33 32-32S561.7 32 544 32zM151.6 41.95c-12.12-13.26-35.06-13.26-47.19 0l-87.1 96.09C4.475 151.1 5.35 171.4 18.38 183.3c6.141 5.629 13.89 8.414 21.61 8.414c8.672 0 17.3-3.504 23.61-10.39L96 145.9v302C96 465.7 110.3 480 128 480s32-14.33 32-32.03V145.9L192.4 181.3C204.4 194.3 224.6 195.3 237.6 183.3c13.03-11.95 13.9-32.22 1.969-45.27L151.6 41.95z"></path></svg></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M0 252.118V48C0 21.49 21.49 0 48 0h204.118a48 48 0 0 1 33.941 14.059l211.882 211.882c18.745 18.745 18.745 49.137 0 67.882L293.823 497.941c-18.745 18.745-49.137 18.745-67.882 0L14.059 286.059A48 48 0 0 1 0 252.118zM112 64c-26.51 0-48 21.49-48 48s21.49 48 48 48 48-21.49 48-48-21.49-48-48-48z"></path></svg></span><span data-v-75c8400c="" class="text">按更新时间</span><span data-v-75c8400c="" class="spacer"></span><span data-v-75c8400c="" class="order"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M416 288h-95.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H416c17.67 0 32-14.33 32-32S433.7 288 416 288zM352 416h-32c-17.67 0-32 14.33-32 32s14.33 32 32 32h32c17.67 0 31.1-14.33 31.1-32S369.7 416 352 416zM480 160h-159.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H480c17.67 0 32-14.33 32-32S497.7 160 480 160zM544 32h-223.1c-17.67 0-32 14.33-32 32s14.33 32 32 32H544c17.67 0 32-14.33 32-32S561.7 32 544 32zM151.6 41.95c-12.12-13.26-35.06-13.26-47.19 0l-87.1 96.09C4.475 151.1 5.35 171.4 18.38 183.3c6.141 5.629 13.89 8.414 21.61 8.414c8.672 0 17.3-3.504 23.61-10.39L96 145.9v302C96 465.7 110.3 480 128 480s32-14.33 32-32.03V145.9L192.4 181.3C204.4 194.3 224.6 195.3 237.6 183.3c13.03-11.95 13.9-32.22 1.969-45.27L151.6 41.95z"></path></svg></span></div></div><div data-v-75c8400c="" class="market-filter-group"><div data-v-75c8400c="" class="market-filter-title"><h2 data-v-75c8400c="" class="text">筛选</h2></div><div data-v-75c8400c="" class="market-filter-item installed"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="market-icon"><path fill="currentColor" d="M433.1 129.1l-83.9-83.9C342.3 38.32 327.1 32 316.1 32H64C28.65 32 0 60.65 0 96v320c0 35.35 28.65 64 64 64h320c35.35 0 64-28.65 64-64V163.9C448 152.9 441.7 137.7 433.1 129.1zM224 416c-35.34 0-64-28.66-64-64s28.66-64 64-64s64 28.66 64 64S259.3 416 224 416zM320 208C320 216.8 312.8 224 304 224h-224C71.16 224 64 216.8 64 208v-96C64 103.2 71.16 96 80 96h224C312.8 96 320 103.2 320 112V208z"></path></svg></span><span data-v-75c8400c="" class="text">已下载</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item verified"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M256 0C292.8 0 324.8 20.7 340.9 51.1C373.8 40.1 410.1 48.96 437 74.98C463 101 470.1 138.2 460.9 171.1C491.3 187.2 512 219.2 512 256C512 292.8 491.3 324.8 460.9 340.9C471 373.8 463 410.1 437 437C410.1 463 373.8 470.1 340.9 460.9C324.8 491.3 292.8 512 256 512C219.2 512 187.2 491.3 171.1 460.9C138.2 471 101 463 74.98 437C48.96 410.1 41 373.8 51.1 340.9C20.7 324.8 0 292.8 0 256C0 219.2 20.7 187.2 51.1 171.1C40.1 138.2 48.96 101 74.98 74.98C101 48.96 138.2 41 171.1 51.1C187.2 20.7 219.2 0 256 0V0zM352.1 224.1C362.3 215.6 362.3 200.4 352.1 191C343.6 181.7 328.4 181.7 319 191L224 286.1L184.1 247C175.6 237.7 160.4 237.7 151 247C141.7 256.4 141.7 271.6 151 280.1L207 336.1C216.4 346.3 231.6 346.3 240.1 336.1L352.1 224.1z"></path></svg></span><span data-v-75c8400c="" class="text">官方认证</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item insecure"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M466.5 83.69l-192-80.01C269.6 1.656 261.3 0 256.1 0C250.8 0 242.5 1.656 237.6 3.688l-192 80.01C27.69 91.08 16 108.6 16 127.1C16 385.2 205.2 512 255.1 512C307.1 512 496 383.8 496 127.1C496 108.6 484.3 91.08 466.5 83.69zM232 152C232 138.8 242.8 128 256 128s24 10.75 24 24v112C280 277.3 269.3 288 256 288S232 277.3 232 264V152zM256 384c-17.67 0-32-14.33-32-32s14.33-32 32-32s32 14.33 32 32S273.7 384 256 384z"></path></svg></span><span data-v-75c8400c="" class="text">不安全</span></div><div data-v-75c8400c="" class="market-filter-item preview"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M507.6 122.8c-2.904-12.09-18.25-16.13-27.04-7.338l-76.55 76.56l-83.1-.0002l0-83.1l76.55-76.56c8.791-8.789 4.75-24.14-7.336-27.04c-23.69-5.693-49.34-6.111-75.92 .2484c-61.45 14.7-109.4 66.9-119.2 129.3C189.8 160.8 192.3 186.7 200.1 210.1l-178.1 178.1c-28.12 28.12-28.12 73.69 0 101.8C35.16 504.1 53.56 512 71.1 512s36.84-7.031 50.91-21.09l178.1-178.1c23.46 7.736 49.31 10.24 76.17 6.004c62.41-9.84 114.6-57.8 129.3-119.2C513.7 172.1 513.3 146.5 507.6 122.8zM80 456c-13.25 0-24-10.75-24-24c0-13.26 10.75-24 24-24s24 10.74 24 24C104 445.3 93.25 456 80 456z"></path></svg></span><span data-v-75c8400c="" class="text">开发中</span><span data-v-75c8400c="" class="spacer"></span></div><!--v-if--><div data-v-75c8400c="" class="market-filter-item newborn"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M64 95.1H0c0 123.8 100.3 224 224 224v128C224 465.6 238.4 480 255.1 480S288 465.6 288 448V320C288 196.3 187.7 95.1 64 95.1zM448 32c-84.25 0-157.4 46.5-195.8 115.3c27.75 30.12 48.25 66.88 59 107.5C424 243.1 512 147.9 512 32H448z"></path></svg></span><span data-v-75c8400c="" class="text">近期新增</span><span data-v-75c8400c="" class="spacer"></span></div></div><div data-v-75c8400c="" class="market-filter-group"><div data-v-75c8400c="" class="market-filter-title"><h2 data-v-75c8400c="" class="text">分类</h2></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" class="market-icon"><path fill="currentColor" d="M400 0C426.5 0 448 21.49 448 48V144C448 170.5 426.5 192 400 192H352V224H608C625.7 224 640 238.3 640 256C640 273.7 625.7 288 608 288H512V320H560C586.5 320 608 341.5 608 368V464C608 490.5 586.5 512 560 512H400C373.5 512 352 490.5 352 464V368C352 341.5 373.5 320 400 320H448V288H192V320H240C266.5 320 288 341.5 288 368V464C288 490.5 266.5 512 240 512H80C53.49 512 32 490.5 32 464V368C32 341.5 53.49 320 80 320H128V288H32C14.33 288 0 273.7 0 256C0 238.3 14.33 224 32 224H288V192H240C213.5 192 192 170.5 192 144V48C192 21.49 213.5 0 240 0H400zM256 64V128H384V64H256zM224 448V384H96V448H224zM416 384V448H544V384H416z"></path></svg></span><span data-v-75c8400c="" class="text">适配器</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="market-icon"><path fill="currentColor" d="M448 80V128C448 172.2 347.7 208 224 208C100.3 208 0 172.2 0 128V80C0 35.82 100.3 0 224 0C347.7 0 448 35.82 448 80zM393.2 214.7C413.1 207.3 433.1 197.8 448 186.1V288C448 332.2 347.7 368 224 368C100.3 368 0 332.2 0 288V186.1C14.93 197.8 34.02 207.3 54.85 214.7C99.66 230.7 159.5 240 224 240C288.5 240 348.3 230.7 393.2 214.7V214.7zM54.85 374.7C99.66 390.7 159.5 400 224 400C288.5 400 348.3 390.7 393.2 374.7C413.1 367.3 433.1 357.8 448 346.1V432C448 476.2 347.7 512 224 512C100.3 512 0 476.2 0 432V346.1C14.93 357.8 34.02 367.3 54.85 374.7z"></path></svg></span><span data-v-75c8400c="" class="text">通用服务</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M512 288c0 35.35-21.49 64-48 64c-32.43 0-31.72-32-55.64-32C394.9 320 384 330.9 384 344.4V480c0 17.67-14.33 32-32 32h-71.64C266.9 512 256 501.1 256 487.6C256 463.1 288 464.4 288 432c0-26.51-28.65-48-64-48s-64 21.49-64 48c0 32.43 32 31.72 32 55.64C192 501.1 181.1 512 167.6 512H32c-17.67 0-32-14.33-32-32v-135.6C0 330.9 10.91 320 24.36 320C48.05 320 47.6 352 80 352C106.5 352 128 323.3 128 288S106.5 223.1 80 223.1c-32.43 0-31.72 32-55.64 32C10.91 255.1 0 245.1 0 231.6v-71.64c0-17.67 14.33-31.1 32-31.1h135.6C181.1 127.1 192 117.1 192 103.6c0-23.69-32-23.24-32-55.64c0-26.51 28.65-47.1 64-47.1s64 21.49 64 47.1c0 32.43-32 31.72-32 55.64c0 13.45 10.91 24.36 24.36 24.36H352c17.67 0 32 14.33 32 31.1v71.64c0 13.45 10.91 24.36 24.36 24.36c23.69 0 23.24-32 55.64-32C490.5 223.1 512 252.7 512 288z"></path></svg></span><span data-v-75c8400c="" class="text">扩展功能</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M0 96C0 60.65 28.65 32 64 32H448C483.3 32 512 60.65 512 96V416C512 451.3 483.3 480 448 480H64C28.65 480 0 451.3 0 416V96zM224 416H448V96H224V416zM88 96C74.75 96 64 106.7 64 120C64 133.3 74.75 144 88 144H136C149.3 144 160 133.3 160 120C160 106.7 149.3 96 136 96H88zM88 240H136C149.3 240 160 229.3 160 216C160 202.7 149.3 192 136 192H88C74.75 192 64 202.7 64 216C64 229.3 74.75 240 88 240zM88 288C74.75 288 64 298.7 64 312C64 325.3 74.75 336 88 336H136C149.3 336 160 325.3 160 312C160 298.7 149.3 288 136 288H88z"></path></svg></span><span data-v-75c8400c="" class="text">控制台</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M502.6 182.6l-45.25-45.25C451.4 131.4 443.3 128 434.8 128H384V80C384 53.5 362.5 32 336 32h-160C149.5 32 128 53.5 128 80V128H77.25c-8.5 0-16.62 3.375-22.62 9.375L9.375 182.6C3.375 188.6 0 196.8 0 205.3V304h128v-32C128 263.1 135.1 256 144 256h32C184.9 256 192 263.1 192 272v32h128v-32C320 263.1 327.1 256 336 256h32C376.9 256 384 263.1 384 272v32h128V205.3C512 196.8 508.6 188.6 502.6 182.6zM336 128h-160V80h160V128zM384 368c0 8.875-7.125 16-16 16h-32c-8.875 0-16-7.125-16-16v-32H192v32C192 376.9 184.9 384 176 384h-32C135.1 384 128 376.9 128 368v-32H0V448c0 17.62 14.38 32 32 32h448c17.62 0 32-14.38 32-32v-112h-128V368z"></path></svg></span><span data-v-75c8400c="" class="text">管理工具</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M495.9 166.6C499.2 175.2 496.4 184.9 489.6 191.2L446.3 230.6C447.4 238.9 448 247.4 448 256C448 264.6 447.4 273.1 446.3 281.4L489.6 320.8C496.4 327.1 499.2 336.8 495.9 345.4C491.5 357.3 486.2 368.8 480.2 379.7L475.5 387.8C468.9 398.8 461.5 409.2 453.4 419.1C447.4 426.2 437.7 428.7 428.9 425.9L373.2 408.1C359.8 418.4 344.1 427 329.2 433.6L316.7 490.7C314.7 499.7 307.7 506.1 298.5 508.5C284.7 510.8 270.5 512 255.1 512C241.5 512 227.3 510.8 213.5 508.5C204.3 506.1 197.3 499.7 195.3 490.7L182.8 433.6C167 427 152.2 418.4 138.8 408.1L83.14 425.9C74.3 428.7 64.55 426.2 58.63 419.1C50.52 409.2 43.12 398.8 36.52 387.8L31.84 379.7C25.77 368.8 20.49 357.3 16.06 345.4C12.82 336.8 15.55 327.1 22.41 320.8L65.67 281.4C64.57 273.1 64 264.6 64 256C64 247.4 64.57 238.9 65.67 230.6L22.41 191.2C15.55 184.9 12.82 175.3 16.06 166.6C20.49 154.7 25.78 143.2 31.84 132.3L36.51 124.2C43.12 113.2 50.52 102.8 58.63 92.95C64.55 85.8 74.3 83.32 83.14 86.14L138.8 103.9C152.2 93.56 167 84.96 182.8 78.43L195.3 21.33C197.3 12.25 204.3 5.04 213.5 3.51C227.3 1.201 241.5 0 256 0C270.5 0 284.7 1.201 298.5 3.51C307.7 5.04 314.7 12.25 316.7 21.33L329.2 78.43C344.1 84.96 359.8 93.56 373.2 103.9L428.9 86.14C437.7 83.32 447.4 85.8 453.4 92.95C461.5 102.8 468.9 113.2 475.5 124.2L480.2 132.3C486.2 143.2 491.5 154.7 495.9 166.6V166.6zM256 336C300.2 336 336 300.2 336 255.1C336 211.8 300.2 175.1 256 175.1C211.8 175.1 176 211.8 176 255.1C176 300.2 211.8 336 256 336z"></path></svg></span><span data-v-75c8400c="" class="text">行为预设</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M447.1 32h-384C28.64 32-.0091 60.65-.0091 96v320c0 35.35 28.65 64 63.1 64h384c35.35 0 64-28.65 64-64V96C511.1 60.65 483.3 32 447.1 32zM111.1 96c26.51 0 48 21.49 48 48S138.5 192 111.1 192s-48-21.49-48-48S85.48 96 111.1 96zM446.1 407.6C443.3 412.8 437.9 416 432 416H82.01c-6.021 0-11.53-3.379-14.26-8.75c-2.73-5.367-2.215-11.81 1.334-16.68l70-96C142.1 290.4 146.9 288 152 288s9.916 2.441 12.93 6.574l32.46 44.51l93.3-139.1C293.7 194.7 298.7 192 304 192s10.35 2.672 13.31 7.125l128 192C448.6 396 448.9 402.3 446.1 407.6z"></path></svg></span><span data-v-75c8400c="" class="text">图片服务</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M447.1 128L218.5 128l276.2-80.97c12.72-3.734 19.1-17.06 16.28-29.78c-3.719-12.7-16.1-19.1-29.78-16.28L51.75 126.9c-29.07 8.512-49.55 34.8-51.39 64.78L.0007 192v255.1c0 35.31 28.69 63.1 63.1 63.1h383.1c35.31 0 63.1-28.69 63.1-63.1V192C511.1 156.7 483.3 128 447.1 128zM80 248c0-4.406 3.594-7.1 7.1-7.1h111.1c4.406 0 7.1 3.594 7.1 7.1V263.1c0 4.406-3.594 7.1-7.1 7.1h-111.1c-4.406 0-7.1-3.594-7.1-7.1V248zM208 391.1c0 4.406-3.594 7.1-7.1 7.1h-111.1c-4.406 0-7.1-3.594-7.1-7.1v-15.1c0-4.406 3.594-7.1 7.1-7.1h111.1c4.406 0 7.1 3.594 7.1 7.1V391.1zM224 327.1c0 4.406-3.594 7.1-7.1 7.1H72c-4.406 0-7.1-3.594-7.1-7.1V311.1c0-4.406 3.594-7.1 7.1-7.1h143.1c4.406 0 7.1 3.594 7.1 7.1V327.1zM367.1 399.1c-44.16 0-80-35.84-80-79.1s35.84-80 80-80s79.1 35.85 79.1 80S412.2 399.1 367.1 399.1z"></path></svg></span><span data-v-75c8400c="" class="text">资讯服务</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M331.8 224.1c28.29 0 54.88 10.99 74.86 30.97l19.59 19.59c40.01-17.74 71.25-53.3 81.62-96.65c5.725-23.92 5.34-47.08 .2148-68.4c-2.613-10.88-16.43-14.51-24.34-6.604l-68.9 68.9h-75.6V97.2l68.9-68.9c7.912-7.912 4.275-21.73-6.604-24.34c-21.32-5.125-44.48-5.51-68.4 .2148c-55.3 13.23-98.39 60.22-107.2 116.4C224.5 128.9 224.2 137 224.3 145l82.78 82.86C315.2 225.1 323.5 224.1 331.8 224.1zM384 278.6c-23.16-23.16-57.57-27.57-85.39-13.9L191.1 158L191.1 95.99l-127.1-95.99L0 63.1l96 127.1l62.04 .0077l106.7 106.6c-13.67 27.82-9.251 62.23 13.91 85.39l117 117.1c14.62 14.5 38.21 14.5 52.71-.0016l52.75-52.75c14.5-14.5 14.5-38.08-.0016-52.71L384 278.6zM227.9 307L168.7 247.9l-148.9 148.9c-26.37 26.37-26.37 69.08 0 95.45C32.96 505.4 50.21 512 67.5 512s34.54-6.592 47.72-19.78l119.1-119.1C225.5 352.3 222.6 329.4 227.9 307zM64 472c-13.25 0-24-10.75-24-24c0-13.26 10.75-24 24-24S88 434.7 88 448C88 461.3 77.25 472 64 472z"></path></svg></span><span data-v-75c8400c="" class="text">实用工具</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" class="market-icon"><path fill="currentColor" d="M96 208c0-61.86 50.14-111.1 111.1-111.1c52.65 0 96.5 36.45 108.5 85.42C334.7 173.1 354.7 168 375.1 168c4.607 0 9.152 .3809 13.68 .8203l24.13-34.76c5.145-7.414 .8965-17.67-7.984-19.27L317.2 98.78L301.2 10.21C299.6 1.325 289.4-2.919 281.9 2.226L208 53.54L134.1 2.225C126.6-2.92 116.4 1.326 114.8 10.21L98.78 98.78L10.21 114.8C1.326 116.4-2.922 126.7 2.223 134.1l51.3 73.94L2.224 281.9c-5.145 7.414-.8975 17.67 7.983 19.27L98.78 317.2l16.01 88.58c1.604 8.881 11.86 13.13 19.27 7.982l10.71-7.432c2.725-35.15 19.85-66.51 45.83-88.1C137.1 309.8 96 263.9 96 208zM128 208c0 44.18 35.82 80 80 80c9.729 0 18.93-1.996 27.56-5.176c7.002-33.65 25.53-62.85 51.57-83.44C282.8 159.3 249.2 128 208 128C163.8 128 128 163.8 128 208zM575.2 325.6c.125-2 .7453-3.744 .7453-5.619c0-35.38-28.75-64-63.1-64c-12.62 0-24.25 3.749-34.13 9.999c-17.62-38.88-56.5-65.1-101.9-65.1c-61.75 0-112 50.12-112 111.1c0 3 .7522 5.743 .8772 8.618c-49.63 3.75-88.88 44.74-88.88 95.37C175.1 469 218.1 512 271.1 512h272c53 0 96-42.99 96-95.99C639.1 373.9 612.7 338.6 575.2 325.6z"></path></svg></span><span data-v-75c8400c="" class="text">生活指南</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M160 352h192V160H160V352zM448 176h48C504.8 176 512 168.8 512 160s-7.162-16-16-16H448V128c0-35.35-28.65-64-64-64h-16V16C368 7.164 360.8 0 352 0c-8.836 0-16 7.164-16 16V64h-64V16C272 7.164 264.8 0 256 0C247.2 0 240 7.164 240 16V64h-64V16C176 7.164 168.8 0 160 0C151.2 0 144 7.164 144 16V64H128C92.65 64 64 92.65 64 128v16H16C7.164 144 0 151.2 0 160s7.164 16 16 16H64v64H16C7.164 240 0 247.2 0 256s7.164 16 16 16H64v64H16C7.164 336 0 343.2 0 352s7.164 16 16 16H64V384c0 35.35 28.65 64 64 64h16v48C144 504.8 151.2 512 160 512c8.838 0 16-7.164 16-16V448h64v48c0 8.836 7.164 16 16 16c8.838 0 16-7.164 16-16V448h64v48c0 8.836 7.164 16 16 16c8.838 0 16-7.164 16-16V448H384c35.35 0 64-28.65 64-64v-16h48c8.838 0 16-7.164 16-16s-7.162-16-16-16H448v-64h48C504.8 272 512 264.8 512 256s-7.162-16-16-16H448V176zM384 368c0 8.836-7.162 16-16 16h-224C135.2 384 128 376.8 128 368v-224C128 135.2 135.2 128 144 128h224C376.8 128 384 135.2 384 144V368z"></path></svg></span><span data-v-75c8400c="" class="text">人工智能</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon"><path fill="currentColor" d="M327.5 85.19L384 64L405.2 7.491C406.9 2.985 411.2 0 416 0C420.8 0 425.1 2.985 426.8 7.491L448 64L504.5 85.19C509 86.88 512 91.19 512 96C512 100.8 509 105.1 504.5 106.8L448 128L426.8 184.5C425.1 189 420.8 192 416 192C411.2 192 406.9 189 405.2 184.5L384 128L327.5 106.8C322.1 105.1 320 100.8 320 96C320 91.19 322.1 86.88 327.5 85.19V85.19zM257.8 187.3L371.8 240C377.5 242.6 381.1 248.3 381.1 254.6C381.1 260.8 377.5 266.5 371.8 269.1L257.8 321.8L205.1 435.8C202.5 441.5 196.8 445.1 190.6 445.1C184.3 445.1 178.6 441.5 176 435.8L123.3 321.8L9.292 269.1C3.627 266.5 0 260.8 0 254.6C0 248.3 3.627 242.6 9.292 240L123.3 187.3L176 73.29C178.6 67.63 184.3 64 190.6 64C196.8 64 202.5 67.63 205.1 73.29L257.8 187.3zM405.2 327.5C406.9 322.1 411.2 320 416 320C420.8 320 425.1 322.1 426.8 327.5L448 384L504.5 405.2C509 406.9 512 411.2 512 416C512 420.8 509 425.1 504.5 426.8L448 448L426.8 504.5C425.1 509 420.8 512 416 512C411.2 512 406.9 509 405.2 504.5L384 448L327.5 426.8C322.1 425.1 320 420.8 320 416C320 411.2 322.1 406.9 327.5 405.2L384 384L405.2 327.5z"></path></svg></span><span data-v-75c8400c="" class="text">趣味交互</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="market-icon"><path fill="currentColor" d="M384 32H64C28.62 32 0 60.62 0 96v320c0 35.38 28.62 64 64 64h320c35.38 0 64-28.62 64-64V96C448 60.62 419.4 32 384 32zM128 384c-17.62 0-32-14.38-32-32s14.38-32 32-32s32 14.38 32 32S145.6 384 128 384zM128 192C110.4 192 96 177.6 96 160s14.38-32 32-32s32 14.38 32 32S145.6 192 128 192zM224 288C206.4 288 192 273.6 192 256s14.38-32 32-32s32 14.38 32 32S241.6 288 224 288zM320 384c-17.62 0-32-14.38-32-32s14.38-32 32-32s32 14.38 32 32S337.6 384 320 384zM320 192c-17.62 0-32-14.38-32-32s14.38-32 32-32s32 14.38 32 32S337.6 192 320 192z"></path></svg></span><span data-v-75c8400c="" class="text">娱乐玩法</span><span data-v-75c8400c="" class="spacer"></span></div><div data-v-75c8400c="" class="market-filter-item"><span data-v-75c8400c="" class="icon"><svg data-v-75c8400c="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" class="market-icon"><path fill="currentColor" d="M640 384.2c0-5.257-.4576-10.6-1.406-15.98l-33.38-211.6C591.4 77.96 522 32 319.1 32C119 32 48.71 77.46 34.78 156.6l-33.38 211.6c-.9487 5.383-1.406 10.72-1.406 15.98c0 51.89 44.58 95.81 101.5 95.81c49.69 0 93.78-30.06 109.5-74.64l7.5-21.36h203l7.5 21.36c15.72 44.58 59.81 74.64 109.5 74.64C595.4 479.1 640 436.1 640 384.2zM247.1 248l-31.96-.0098L215.1 280c0 13.2-10.78 24-23.98 24c-13.2 0-24.02-10.8-24.02-24l.0367-32.01L135.1 248c-13.2 0-23.98-10.8-23.98-24c0-13.2 10.77-24 23.98-24l32.04-.011L167.1 168c0-13.2 10.82-24 24.02-24c13.2 0 23.98 10.8 23.98 24l.0368 31.99L247.1 200c13.2 0 24.02 10.8 24.02 24C271.1 237.2 261.2 248 247.1 248zM432 311.1c-22.09 0-40-17.92-40-40c0-22.08 17.91-40 40-40s40 17.92 40 40C472 294.1 454.1 311.1 432 311.1zM496 215.1c-22.09 0-40-17.92-40-40c0-22.08 17.91-40 40-40s40 17.92 40 40C536 198.1 518.1 215.1 496 215.1z"></path></svg></span><span data-v-75c8400c="" class="text">游戏辅助</span><span data-v-75c8400c="" class="spacer"></span></div></div></div></div><div class="el-scrollbar__bar is-horizontal" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div></div><div class="el-scrollbar__bar is-vertical el-scrollbar-fade-enter-to" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateY(0%); height: 625.558px;"></div></div></div></aside><div class="main-container"><div class="aside-mask"></div><div class="layout-header has-menu"><div class="toggle-sidebar-button" role="button" tabindex="0"><div class="icon"><span></span><span></span><span></span></div></div><div class="left">插件市场</div><div class="right"><span class="menu-item disabled el-tooltip__trigger el-tooltip__trigger"><svg class="k-icon check menu-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M438.6 105.4C451.1 117.9 451.1 138.1 438.6 150.6L182.6 406.6C170.1 419.1 149.9 419.1 137.4 406.6L9.372 278.6C-3.124 266.1-3.124 245.9 9.372 233.4C21.87 220.9 42.13 220.9 54.63 233.4L159.1 338.7L393.4 105.4C405.9 92.88 426.1 92.88 438.6 105.4H438.6z"></path></svg></span><span class="menu-item el-tooltip__trigger el-tooltip__trigger"><svg class="k-icon refresh menu-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M496 40v160C496 213.3 485.3 224 472 224h-160C298.8 224 288 213.3 288 200s10.75-24 24-24h100.5C382.8 118.3 322.5 80 256 80C158.1 80 80 158.1 80 256s78.97 176 176 176c41.09 0 81.09-14.47 112.6-40.75c10.16-8.5 25.31-7.156 33.81 3.062c8.5 10.19 7.125 25.31-3.062 33.81c-40.16 33.44-91.17 51.77-143.5 51.77C132.4 479.9 32 379.5 32 256s100.4-223.9 223.9-223.9c79.85 0 152.4 43.46 192.1 109.1V40c0-13.25 10.75-24 24-24S496 26.75 496 40z"></path></svg></span></div><div class="toggle-menu-button" role="button" tabindex="1"><svg class="k-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M352 256C352 238.3 366.3 224 384 224C401.7 224 416 238.3 416 256C416 273.7 401.7 288 384 288C366.3 288 352 273.7 352 256zM192 256C192 238.3 206.3 224 224 224C241.7 224 256 238.3 256 256C256 273.7 241.7 288 224 288C206.3 288 192 273.7 192 256zM96 256C96 273.7 81.67 288 64 288C46.33 288 32 273.7 32 256C32 238.3 46.33 224 64 224C81.67 224 96 238.3 96 256z"></path></svg></div></div><main class="layout-main darker"><div class="el-scrollbar"><div class="el-scrollbar__wrap el-scrollbar__wrap--hidden-default"><div class="el-scrollbar__view" style=""><div data-v-8ee9e6d5="" class="search-box"><div data-v-8ee9e6d5="" class="search-container"><span data-v-8ee9e6d5="" class="search-word">adapter-onebot</span><input data-v-8ee9e6d5="" placeholder="输入想要查询的插件名"></div><div data-v-8ee9e6d5="" class="search-action"><svg data-v-8ee9e6d5="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="market-icon search"><path fill="currentColor" d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"></path></svg><svg data-v-8ee9e6d5="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="market-icon close"><path fill="currentColor" d="M310.6 361.4c12.5 12.5 12.5 32.75 0 45.25C304.4 412.9 296.2 416 288 416s-16.38-3.125-22.62-9.375L160 301.3L54.63 406.6C48.38 412.9 40.19 416 32 416S15.63 412.9 9.375 406.6c-12.5-12.5-12.5-32.75 0-45.25l105.4-105.4L9.375 150.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 210.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-105.4 105.4L310.6 361.4z"></path></svg></div></div><div class="market-hint text-center"> 共搜索到 1 / 114514 个插件。 </div><div data-v-07418c20="" class="el-pagination is-background pagination"><button type="button" class="btn-prev is-first" disabled="" aria-label="Go to previous page" aria-disabled="true"><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M609.408 149.376 277.76 489.6a32 32 0 0 0 0 44.672l331.648 340.352a29.12 29.12 0 0 0 41.728 0 30.592 30.592 0 0 0 0-42.752L339.264 511.936l311.872-319.872a30.592 30.592 0 0 0 0-42.688 29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button><ul class="el-pager"><li class="is-active number" aria-current="true" aria-label="page 1" tabindex="0"> 1 </li><!--v-if--><!--v-if--><!--v-if--></ul><button type="button" class="btn-next is-last" aria-label="Go to next page" aria-disabled="true" disabled=""><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button></div><div data-v-07418c20="" class="package-list"><a data-v-78c515d7="" data-v-07418c20="" class="market-package flex flex-col gap-3 k-card" target="_blank"><div data-v-78c515d7="" class="header flex flex-row gap-4"><div data-v-78c515d7="" class="left shrink-0 flex flex-row justify-center items-center"><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" class="market-icon"><path fill="currentColor" d="M336 240H624C632.8 240 640 247.2 640 256C640 264.8 632.8 272 624 272H496V320H560C586.5 320 608 341.5 608 368V464C608 490.5 586.5 512 560 512H400C373.5 512 352 490.5 352 464V368C352 341.5 373.5 320 400 320H464V272H176V320H240C266.5 320 288 341.5 288 368V464C288 490.5 266.5 512 240 512H80C53.49 512 32 490.5 32 464V368C32 341.5 53.49 320 80 320H144V272H16C7.164 272 0 264.8 0 256C0 247.2 7.164 240 16 240H304V192H240C213.5 192 192 170.5 192 144V48C192 21.49 213.5 0 240 0H400C426.5 0 448 21.49 448 48V144C448 170.5 426.5 192 400 192H336V240zM400 32H240C231.2 32 224 39.16 224 48V144C224 152.8 231.2 160 240 160H400C408.8 160 416 152.8 416 144V48C416 39.16 408.8 32 400 32zM400 352C391.2 352 384 359.2 384 368V464C384 472.8 391.2 480 400 480H560C568.8 480 576 472.8 576 464V368C576 359.2 568.8 352 560 352H400zM80 352C71.16 352 64 359.2 64 368V464C64 472.8 71.16 480 80 480H240C248.8 480 256 472.8 256 464V368C256 359.2 248.8 352 240 352H80z"></path></svg></div><div data-v-78c515d7="" class="main flex flex-col justify-around overflow-hidden"><h2 data-v-78c515d7="" class="top"><span data-v-78c515d7="" class="title truncate" title="adapter-onebot">adapter-onebot</span><!--v-if--></h2><div data-v-78c515d7="" class="bottom"><div data-v-78c515d7="" class="rating el-tooltip__trigger el-tooltip__trigger"><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg><svg data-v-78c515d7="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="market-icon"><path fill="currentColor" d="M381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3z"></path></svg></div></div></div><div data-v-78c515d7="" class="text-right grow-1 shrink-0"><button aria-disabled="false" type="button" class="el-button el-button--success" solid=""><!--v-if--><span class="">修改</span></button></div></div><span data-v-78c515d7="" class="markdown desc">OneBot 适配器</span></a><div data-v-78c515d7="" class="footer"></div></div><div data-v-07418c20="" class="el-pagination is-background pagination"><button type="button" class="btn-prev is-first" disabled="" aria-label="Go to previous page" aria-disabled="true"><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M609.408 149.376 277.76 489.6a32 32 0 0 0 0 44.672l331.648 340.352a29.12 29.12 0 0 0 41.728 0 30.592 30.592 0 0 0 0-42.752L339.264 511.936l311.872-319.872a30.592 30.592 0 0 0 0-42.688 29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button><ul class="el-pager"><li class="is-active number" aria-current="true" aria-label="page 1" tabindex="0"> 1 </li><!--v-if--><!--v-if--><!--v-if--></ul><button type="button" class="btn-next is-last" aria-label="Go to next page" aria-disabled="true" disabled=""><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button></div></div></div><div class="el-scrollbar__bar is-horizontal" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div></div><div class="el-scrollbar__bar is-vertical" style=""><div class="el-scrollbar__thumb" style="transform: translateY(3.15657%); height: 677.997px;"></div></div></div></main></div><!--v-if--></div><footer class="layout-status"><div><div data-v-ed732ada="" class="k-status version el-tooltip__trigger el-tooltip__trigger"> Koishi </div></div><div><!--v-if--><!--v-if--><!--v-if--><div data-v-ed732ada="" class="k-status el-tooltip__trigger el-tooltip__trigger"><span data-v-5269806f="" data-v-a3e59fe7="" class="status-light online"></span><svg data-v-a3e59fe7="" class="k-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M6.625 215.5l168-176C179.2 34.7 185.4 32.02 192 32.02s12.84 2.688 17.38 7.438l168 176c9.125 9.594 8.781 24.78-.8125 33.94c-9.5 9.156-24.75 8.812-33.94-.8125L216 115.9V456c0 13.25-10.75 23.1-23.1 23.1S168 469.3 168 456V115.9l-126.6 132.7C32.22 258.2 16.97 258.5 7.438 249.4C-2.156 240.2-2.5 225 6.625 215.5z"></path></svg><span data-v-a3e59fe7="">0/min</span><svg data-v-a3e59fe7="" class="k-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M377.4 296.6l-168 176C204.8 477.3 198.6 480 192 480s-12.84-2.688-17.38-7.438l-168-176C-2.5 286.1-2.156 271.8 7.438 262.6c9.5-9.156 24.75-8.812 33.94 .8125L168 396.1V56.02c0-13.25 10.75-24.01 23.1-24.01S216 42.77 216 56.02v340.1l126.6-132.7c9.156-9.625 24.41-9.969 33.94-.8125C386.2 271.8 386.5 286.1 377.4 296.6z"></path></svg><span data-v-a3e59fe7="">0/min</span></div><div data-v-ed732ada="" class="k-status el-tooltip__trigger el-tooltip__trigger"> CPU: 0% 内存: 114514%</div></div></footer><!--v-if--><div class="el-overlay" style="z-index: 2134; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-548" aria-describedby="el-id-9459-549" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2078; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-312" aria-describedby="el-id-9459-313" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2079; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-314" aria-describedby="el-id-9459-315" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2080; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-323" aria-describedby="el-id-9459-324" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2081; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-325" aria-describedby="el-id-9459-326" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2142; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-328" aria-describedby="el-id-9459-329" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2083; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-330" aria-describedby="el-id-9459-331" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2135; display: none;"><div role="dialog" aria-modal="true" aria-labelledby="el-id-9459-550" aria-describedby="el-id-9459-551" class="el-overlay-dialog"></div></div></div>
<div id="el-popper-container-9459"><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><div class="el-popper is-dark" tabindex="-1" aria-hidden="true" role="tooltip" id="el-id-9459-1336" style="z-index: 2236; position: absolute; inset: 0px auto auto 0px; display: none; transform: translate3d(0px, 12.4444px, 0px);" data-popper-reference-hidden="true" data-popper-escaped="true" data-popper-placement="bottom"><span>1</span><span class="el-popper__arrow" data-popper-arrow="" style="position: absolute; left: 0px; transform: translate3d(0px, 0px, 0px);"></span></div><!--v-if--><!--v-if--><div class="el-popper is-pure is-light el-select__popper" tabindex="-1" aria-hidden="true" role="tooltip" id="el-id-9459-1342" style="z-index: 2240; position: absolute; inset: 12.4444px auto auto 0px; display: none;" data-popper-reference-hidden="true" data-popper-escaped="true" data-popper-placement="bottom-start"><div class="el-select-dropdown" style="min-width: 0px;"><!--v-if--><!--v-if--><div class="el-scrollbar is-empty" style="display: none;"><div class="el-select-dropdown__wrap el-scrollbar__wrap el-scrollbar__wrap--hidden-default"><ul id="el-id-9459-1343" class="el-scrollbar__view el-select-dropdown__list" role="listbox" aria-orientation="vertical" style=""><!--v-if--></ul></div><div class="el-scrollbar__bar is-horizontal" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div></div><div class="el-scrollbar__bar is-vertical" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateY(0%);"></div></div></div><div class="el-select-dropdown__empty"><span>No data</span></div><!--v-if--><!--v-if--></div><span class="el-popper__arrow" data-popper-arrow="" style="position: absolute; left: 0px;"></span></div><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><div class="el-popper is-dark" tabindex="-1" aria-hidden="true" role="tooltip" id="el-id-9459-1397" style="z-index: 2276; position: absolute; inset: 0px auto auto 0px; display: none; transform: translate3d(0px, 12.4444px, 0px);" data-popper-reference-hidden="true" data-popper-escaped="true" data-popper-placement="bottom"><span>1</span><span class="el-popper__arrow" data-popper-arrow="" style="position: absolute; left: 0px; transform: translate3d(0px, 0px, 0px);"></span></div><!--v-if--><!--v-if--><div class="el-popper is-pure is-light el-select__popper" tabindex="-1" aria-hidden="true" role="tooltip" id="el-id-9459-1403" style="z-index: 2280; position: absolute; inset: 12.4444px auto auto 0px; display: none;" data-popper-reference-hidden="true" data-popper-escaped="true" data-popper-placement="bottom-start"><div class="el-select-dropdown" style="min-width: 0px;"><!--v-if--><!--v-if--><div class="el-scrollbar is-empty" style="display: none;"><div class="el-select-dropdown__wrap el-scrollbar__wrap el-scrollbar__wrap--hidden-default"><ul id="el-id-9459-1404" class="el-scrollbar__view el-select-dropdown__list" role="listbox" aria-orientation="vertical" style=""><!--v-if--></ul></div><div class="el-scrollbar__bar is-horizontal" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div></div><div class="el-scrollbar__bar is-vertical" style="display: none;"><div class="el-scrollbar__thumb" style="transform: translateY(0%);"></div></div></div><div class="el-select-dropdown__empty"><span>No data</span></div><!--v-if--><!--v-if--></div><span class="el-popper__arrow" data-popper-arrow="" style="position: absolute; left: 0px;"></span></div><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--><!--v-if--></div><div class="el-overlay" style="z-index: 2085; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-340" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2086; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-342" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2087; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-343" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2088; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-345" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2089; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-347" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2090; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-348" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2226; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1321" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2227; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1323" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2228; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1324" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2229; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1326" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2230; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1328" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2231; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1329" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2232; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1331" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2233; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1332" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2234; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1334" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2235; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1335" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2237; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1338" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2238; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1339" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2239; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1341" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2241; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1345" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2242; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1346" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2243; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1347" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2244; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1348" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2245; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1350" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2246; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1352" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2247; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1354" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2248; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1356" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2249; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1358" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2250; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1359" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2251; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1360" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2252; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1362" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2253; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1364" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2254; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1366" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2255; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1367" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2256; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1368" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2257; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1370" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2258; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1372" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2259; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1373" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2260; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1374" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2261; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1375" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2262; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1376" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2263; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1377" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2264; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1378" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2265; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1379" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2266; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1382" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2267; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1384" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2268; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1385" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2269; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1387" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2270; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1389" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2271; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1390" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2272; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1392" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2273; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1393" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2274; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1395" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2275; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1396" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2277; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1399" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2278; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1400" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2279; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1402" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2281; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1406" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2282; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1407" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2283; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1408" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2284; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1409" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2285; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1411" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2286; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1413" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2287; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1415" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2288; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1417" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2289; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1419" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2290; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1420" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2291; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1421" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2292; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1423" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2293; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1425" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2294; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1427" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2295; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1428" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2296; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1429" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2297; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1431" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2298; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1433" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2299; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1434" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2300; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1435" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2301; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1436" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2302; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1437" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2303; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1438" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2304; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1439" class="el-overlay-dialog"></div></div><div class="el-overlay" style="z-index: 2305; display: none;"><div role="dialog" aria-modal="true" aria-label="编辑 JSON" aria-describedby="el-id-9459-1440" class="el-overlay-dialog"></div></div><div id="immersive-translate-browser-popup" style="all: initial"><template shadowrootmode="open"><style>@charset "UTF-8";
/*!
 * Pico.css v1.5.6 (https://picocss.com)
 * Copyright 2019-2022 - Licensed under MIT
 */
/**
 * Theme: default
 */
#mount {
  --font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --line-height: 1.5;
  --font-weight: 400;
  --font-size: 16px;
  --border-radius: 0.25rem;
  --border-width: 1px;
  --outline-width: 3px;
  --spacing: 1rem;
  --typography-spacing-vertical: 1.5rem;
  --block-spacing-vertical: calc(var(--spacing) * 2);
  --block-spacing-horizontal: var(--spacing);
  --grid-spacing-vertical: 0;
  --grid-spacing-horizontal: var(--spacing);
  --form-element-spacing-vertical: 0.75rem;
  --form-element-spacing-horizontal: 1rem;
  --nav-element-spacing-vertical: 1rem;
  --nav-element-spacing-horizontal: 0.5rem;
  --nav-link-spacing-vertical: 0.5rem;
  --nav-link-spacing-horizontal: 0.5rem;
  --form-label-font-weight: var(--font-weight);
  --transition: 0.2s ease-in-out;
  --modal-overlay-backdrop-filter: blur(0.25rem);
}
@media (min-width: 576px) {
  #mount {
    --font-size: 17px;
  }
}
@media (min-width: 768px) {
  #mount {
    --font-size: 18px;
  }
}
@media (min-width: 992px) {
  #mount {
    --font-size: 19px;
  }
}
@media (min-width: 1200px) {
  #mount {
    --font-size: 20px;
  }
}
<p>@media (min-width: 576px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 2.5);<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 3);<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 3.5);<br>
}<br>
}</p>
<p>@media (min-width: 576px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.25);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.5);<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.75);<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 2);<br>
}<br>
}</p>
<p>dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
--block-spacing-horizontal: var(--spacing);<br>
}<br>
@media (min-width: 576px) {<br>
dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 2.5);<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.25);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 3);<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.5);<br>
}<br>
}</p>
<p>a {<br>
--text-decoration: none;<br>
}<br>
a.secondary,<br>
a.contrast {<br>
--text-decoration: underline;<br>
}</p>
<p>small {<br>
--font-size: 0.875em;<br>
}</p>
<p>h1,<br>
h2,<br>
h3,<br>
h4,<br>
h5,<br>
h6 {<br>
--font-weight: 700;<br>
}</p>
<p>h1 {<br>
--font-size: 2rem;<br>
--typography-spacing-vertical: 3rem;<br>
}</p>
<p>h2 {<br>
--font-size: 1.75rem;<br>
--typography-spacing-vertical: 2.625rem;<br>
}</p>
<p>h3 {<br>
--font-size: 1.5rem;<br>
--typography-spacing-vertical: 2.25rem;<br>
}</p>
<p>h4 {<br>
--font-size: 1.25rem;<br>
--typography-spacing-vertical: 1.874rem;<br>
}</p>
<p>h5 {<br>
--font-size: 1.125rem;<br>
--typography-spacing-vertical: 1.6875rem;<br>
}</p>
<p>[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
--border-width: 2px;<br>
}</p>
<p>[type=&quot;checkbox&quot;][role=&quot;switch&quot;] {<br>
--border-width: 2px;<br>
}</p>
<p>thead th,<br>
thead td,<br>
tfoot th,<br>
tfoot td {<br>
--border-width: 3px;<br>
}</p>
<p>:not(thead, tfoot) &gt; * &gt; td {<br>
--font-size: 0.875em;<br>
}</p>
<p>pre,<br>
code,<br>
kbd,<br>
samp {<br>
--font-family: &quot;Menlo&quot;, &quot;Consolas&quot;, &quot;Roboto Mono&quot;, &quot;Ubuntu Monospace&quot;,<br>
&quot;Noto Mono&quot;, &quot;Oxygen Mono&quot;, &quot;Liberation Mono&quot;, monospace,<br>
&quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;;<br>
}</p>
<p>kbd {<br>
--font-weight: bolder;<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--background-color: #fff;<br>
--background-light-green: #f5f7f9;<br>
--color: hsl(205deg, 20%, 32%);<br>
--h1-color: hsl(205deg, 30%, 15%);<br>
--h2-color: #24333e;<br>
--h3-color: hsl(205deg, 25%, 23%);<br>
--h4-color: #374956;<br>
--h5-color: hsl(205deg, 20%, 32%);<br>
--h6-color: #4d606d;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: hsl(205deg, 20%, 94%);<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 90%, 32%);<br>
--primary-focus: rgba(16, 149, 193, 0.125);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 20%, 32%);<br>
--secondary-focus: rgba(89, 107, 120, 0.125);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 30%, 15%);<br>
--contrast-hover: #000;<br>
--contrast-focus: rgba(89, 107, 120, 0.125);<br>
--contrast-inverse: #fff;<br>
--mark-background-color: #fff2ca;<br>
--mark-color: #543a26;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: transparent;<br>
--form-element-border-color: hsl(205deg, 14%, 68%);<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: transparent;<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 18%, 86%);<br>
--form-element-disabled-border-color: hsl(205deg, 14%, 68%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #c62828;<br>
--form-element-invalid-active-border-color: #d32f2f;<br>
--form-element-invalid-focus-color: rgba(211, 47, 47, 0.125);<br>
--form-element-valid-border-color: #388e3c;<br>
--form-element-valid-active-border-color: #43a047;<br>
--form-element-valid-focus-color: rgba(67, 160, 71, 0.125);<br>
--switch-background-color: hsl(205deg, 16%, 77%);<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: hsl(205deg, 18%, 86%);<br>
--range-active-border-color: hsl(205deg, 16%, 77%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: #f6f8f9;<br>
--code-background-color: hsl(205deg, 20%, 94%);<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 40%, 50%);<br>
--code-property-color: hsl(185deg, 40%, 40%);<br>
--code-value-color: hsl(40deg, 20%, 50%);<br>
--code-comment-color: hsl(205deg, 14%, 68%);<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: var(--background-color);<br>
--card-border-color: var(--muted-border-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(27, 40, 50, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(27, 40, 50, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(27, 40, 50, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(27, 40, 50, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(27, 40, 50, 0.04302),<br>
0.5rem 1rem 6rem rgba(27, 40, 50, 0.06),<br>
0 0 0 0.0625rem rgba(27, 40, 50, 0.015);<br>
--card-sectionning-background-color: #fbfbfc;<br>
--dropdown-background-color: #fbfbfc;<br>
--dropdown-border-color: #e1e6eb;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: hsl(205deg, 20%, 94%);<br>
--modal-overlay-background-color: rgba(213, 220, 226, 0.7);<br>
--progress-background-color: hsl(205deg, 18%, 86%);<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(198, 40, 40)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(56, 142, 60)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjQnIGhlaWdodD0nMjQnIHZpZXdCb3g9JzAgMCAyNCAyNCcgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTguOTM0OCA4LjY0ODQ0QzIwLjg5NDEgOC42NDg0NCAyMi40ODU1IDcuMDU0NjkgMjIuNDg1NSA1LjA5NzY2QzIyLjQ4NTUgMy4xNDA2MiAyMC44OTE4IDEuNTQ2ODggMTguOTM0OCAxLjU0Njg4QzE2Ljk3NTQgMS41NDY4OCAxNS4zODQgMy4xNDA2MiAxNS4zODQgNS4wOTc2NkMxNS4zODQgNS4yOTkyMiAxNS40MDA0IDUuNDkzNzUgMTUuNDMzMiA1LjY4NTk0TDcuMzIzODMgOS4zNTM5MUM2LjcwOTc3IDguODQ1MzEgNS45MjIyNyA4LjU0MDYyIDUuMDY0NDUgOC41NDA2MkMzLjEwNTA4IDguNTQwNjIgMS41MTM2NyAxMC4xMzQ0IDEuNTEzNjcgMTIuMDkxNEMxLjUxMzY3IDE0LjA0ODQgMy4xMDc0MiAxNS42NDIyIDUuMDY0NDUgMTUuNjQyMkM1LjgzMzIgMTUuNjQyMiA2LjU0NTcgMTUuMzk2MSA3LjEyNjk1IDE0Ljk4MTNMMTIuNDk0MSAxNy45OTUzQzEyLjQxNjggMTguMjg1OSAxMi4zNzcgMTguNTg4MyAxMi4zNzcgMTguOTAyM0MxMi4zNzcgMjAuODYxNyAxMy45NzA3IDIyLjQ1MzEgMTUuOTI3NyAyMi40NTMxQzE3Ljg4NzEgMjIuNDUzMSAxOS40Nzg1IDIwLjg1OTQgMTkuNDc4NSAxOC45MDIzQzE5LjQ3ODUgMTYuOTQzIDE3Ljg4NDggMTUuMzUxNiAxNS45Mjc3IDE1LjM1MTZDMTQuOTU3NCAxNS4zNTE2IDE0LjA3ODUgMTUuNzQzIDEzLjQzNjMgMTYuMzczNEw4LjMyMjI3IDEzLjUwNDdDOC41MDk3NyAxMy4wNzExIDguNjE1MjMgMTIuNTk1MyA4LjYxNTIzIDEyLjA5MzhDOC42MTUyMyAxMS42ODEyIDguNTQ0OTIgMTEuMjg3NSA4LjQxNjAyIDEwLjkxOTVMMTYuMjIzIDcuMzg3NUMxNi44NzQ2IDguMTU2MjUgMTcuODQ5NiA4LjY0ODQ0IDE4LjkzNDggOC42NDg0NFpNNS4wNjQ0NSAxMy43Njk1QzQuMTQxMDIgMTMuNzY5NSAzLjM4ODY3IDEzLjAxNzIgMy4zODg2NyAxMi4wOTM4QzMuMzg4NjcgMTEuMTcwMyA0LjE0MTAyIDEwLjQxOCA1LjA2NDQ1IDEwLjQxOEM1Ljk4Nzg5IDEwLjQxOCA2Ljc0MDIzIDExLjE3MDMgNi43NDAyMyAxMi4wOTM4QzYuNzQwMjMgMTMuMDE3MiA1Ljk4Nzg5IDEzLjc2OTUgNS4wNjQ0NSAxMy43Njk1Wk0xNS45Mjc3IDE3LjIyNjZDMTYuODUxMiAxNy4yMjY2IDE3LjYwMzUgMTcuOTc4OSAxNy42MDM1IDE4LjkwMjNDMTcuNjAzNSAxOS44MjU4IDE2Ljg1MTIgMjAuNTc4MSAxNS45Mjc3IDIwLjU3ODFDMTUuMDA0MyAyMC41NzgxIDE0LjI1MiAxOS44MjU4IDE0LjI1MiAxOC45MDIzQzE0LjI1MiAxNy45Nzg5IDE1LjAwMiAxNy4yMjY2IDE1LjkyNzcgMTcuMjI2NlpNMTguOTM0OCAzLjQxOTUzQzE5Ljg1ODIgMy40MTk1MyAyMC42MTA1IDQuMTcxODcgMjAuNjEwNSA1LjA5NTMxQzIwLjYxMDUgNi4wMTg3NSAxOS44NTgyIDYuNzcxMDkgMTguOTM0OCA2Ljc3MTA5QzE4LjAxMTMgNi43NzEwOSAxNy4yNTkgNi4wMTg3NSAxNy4yNTkgNS4wOTUzMUMxNy4yNTkgNC4xNzE4NyAxOC4wMTEzIDMuNDE5NTMgMTguOTM0OCAzLjQxOTUzWicgZmlsbD0nIzgzODM4MycvPjwvc3ZnPiA=&quot;);<br>
--float-ball-more-button-border-color: #f6f6f6;<br>
--float-ball-more-button-background-color: #ffffff;<br>
--float-ball-more-button-svg-color: #6c6f73;<br>
color-scheme: light;<br>
--service-bg-hover: #f7faff;<br>
--service-bg: #fafbfb;<br>
}</p>
<p>@media only screen and (prefers-color-scheme: dark) {<br>
#mount:not([data-theme=&quot;light&quot;]) {<br>
--background-color: #11191f;<br>
--float-ball-more-button-background-color: #ffffff;<br>
--background-light-green: #141e26;<br>
--color: hsl(205deg, 16%, 77%);<br>
--h1-color: hsl(205deg, 20%, 94%);<br>
--h2-color: #e1e6eb;<br>
--h3-color: hsl(205deg, 18%, 86%);<br>
--h4-color: #c8d1d8;<br>
--h5-color: hsl(205deg, 16%, 77%);<br>
--h6-color: #afbbc4;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: #1f2d38;<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 80%, 50%);<br>
--primary-focus: rgba(16, 149, 193, 0.25);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 10%, 50%);<br>
--secondary-focus: rgba(115, 130, 140, 0.25);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 20%, 94%);<br>
--contrast-hover: #fff;<br>
--contrast-focus: rgba(115, 130, 140, 0.25);<br>
--contrast-inverse: #000;<br>
--mark-background-color: #d1c284;<br>
--mark-color: #11191f;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: #11191f;<br>
--form-element-border-color: #374956;<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: var(<br>
--form-element-background-color<br>
);<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 25%, 23%);<br>
--form-element-disabled-border-color: hsl(205deg, 20%, 32%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #b71c1c;<br>
--form-element-invalid-active-border-color: #c62828;<br>
--form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);<br>
--form-element-valid-border-color: #2e7d32;<br>
--form-element-valid-active-border-color: #388e3c;<br>
--form-element-valid-focus-color: rgba(56, 142, 60, 0.25);<br>
--switch-background-color: #374956;<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: #24333e;<br>
--range-active-border-color: hsl(205deg, 25%, 23%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: rgba(115, 130, 140, 0.05);<br>
--code-background-color: #18232c;<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 30%, 50%);<br>
--code-property-color: hsl(185deg, 30%, 50%);<br>
--code-value-color: hsl(40deg, 10%, 50%);<br>
--code-comment-color: #4d606d;<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-active-summary-color: var(--primary);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: #141e26;<br>
--card-border-color: var(--card-background-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),<br>
0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);<br>
--card-sectionning-background-color: #18232c;<br>
--dropdown-background-color: hsl(205deg, 30%, 15%);<br>
--dropdown-border-color: #24333e;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: rgba(36, 51, 62, 0.75);<br>
--modal-overlay-background-color: rgba(36, 51, 62, 0.8);<br>
--progress-background-color: #24333e;<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=&quot;);<br>
color-scheme: dark;<br>
--service-bg-hover: #22292f;<br>
--service-bg: rgba(0, 0, 0, 0.1);<br>
}<br>
}<br>
[data-theme=&quot;dark&quot;] {<br>
--background-color: #11191f;<br>
--float-ball-more-button-background-color: #191919;<br>
--background-light-green: #141e26;<br>
--color: hsl(205deg, 16%, 77%);<br>
--h1-color: hsl(205deg, 20%, 94%);<br>
--h2-color: #e1e6eb;<br>
--h3-color: hsl(205deg, 18%, 86%);<br>
--h4-color: #c8d1d8;<br>
--h5-color: hsl(205deg, 16%, 77%);<br>
--h6-color: #afbbc4;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: #1f2d38;<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 80%, 50%);<br>
--primary-focus: rgba(16, 149, 193, 0.25);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 10%, 50%);<br>
--secondary-focus: rgba(115, 130, 140, 0.25);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 20%, 94%);<br>
--contrast-hover: #fff;<br>
--contrast-focus: rgba(115, 130, 140, 0.25);<br>
--contrast-inverse: #000;<br>
--mark-background-color: #d1c284;<br>
--mark-color: #11191f;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: #11191f;<br>
--form-element-border-color: #374956;<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: var(--form-element-background-color);<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 25%, 23%);<br>
--form-element-disabled-border-color: hsl(205deg, 20%, 32%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #b71c1c;<br>
--form-element-invalid-active-border-color: #c62828;<br>
--form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);<br>
--form-element-valid-border-color: #2e7d32;<br>
--form-element-valid-active-border-color: #388e3c;<br>
--form-element-valid-focus-color: rgba(56, 142, 60, 0.25);<br>
--switch-background-color: #374956;<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: #24333e;<br>
--range-active-border-color: hsl(205deg, 25%, 23%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: rgba(115, 130, 140, 0.05);<br>
--code-background-color: #18232c;<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 30%, 50%);<br>
--code-property-color: hsl(185deg, 30%, 50%);<br>
--code-value-color: hsl(40deg, 10%, 50%);<br>
--code-comment-color: #4d606d;<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-active-summary-color: var(--primary);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: #141e26;<br>
--card-border-color: var(--card-background-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),<br>
0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);<br>
--card-sectionning-background-color: #18232c;<br>
--dropdown-background-color: hsl(205deg, 30%, 15%);<br>
--dropdown-border-color: #24333e;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: rgba(36, 51, 62, 0.75);<br>
--modal-overlay-background-color: rgba(36, 51, 62, 0.8);<br>
--progress-background-color: #24333e;<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=&quot;);<br>
color-scheme: dark;<br>
--service-bg: rgba(0, 0, 0, 0.1);<br>
}</p>
<p>progress,<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;] {<br>
accent-color: var(--primary);<br>
}</p>
<p>/**</p>
<ul>
<li>Document</li>
<li>Content-box &amp; Responsive typography<br>
*/<br>
*,<br>
*<VPIcon icon="before,
*" />after {<br>
box-sizing: border-box;<br>
background-repeat: no-repeat;<br>
}</li>
</ul>
<p><VPIcon icon="before," />after {<br>
text-decoration: inherit;<br>
vertical-align: inherit;<br>
}</p>
<p>:where(#mount) {<br>
-webkit-tap-highlight-color: transparent;<br>
-webkit-text-size-adjust: 100%;<br>
-moz-text-size-adjust: 100%;<br>
text-size-adjust: 100%;<br>
background-color: var(--background-color);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
line-height: var(--line-height);<br>
font-family: var(--font-family);<br>
text-rendering: optimizeLegibility;<br>
overflow-wrap: break-word;<br>
cursor: default;<br>
-moz-tab-size: 4;<br>
-o-tab-size: 4;<br>
tab-size: 4;<br>
}</p>
<p>/**</p>
<ul>
<li>Sectioning</li>
<li>Container and responsive spacings for header, main, footer<br>
*/<br>
main {<br>
display: block;<br>
}</li>
</ul>
<p>#mount {<br>
width: 100%;<br>
margin: 0;<br>
}<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
width: 100%;<br>
margin-right: auto;<br>
margin-left: auto;<br>
padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);<br>
}<br>
@media (min-width: 576px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 2px !important;<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 0 12px !important;<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 0 24px !important;<br>
}<br>
}</p>
<p>/**</p>
<ul>
<li>Container<br>
<em>/<br>
.container,<br>
.container-fluid {<br>
width: 100%;<br>
margin-right: auto;<br>
margin-left: auto;<br>
padding-right: var(--spacing);<br>
padding-left: var(--spacing);<br>
}<br>
/</em><br>
@media (min-width: 576px) {<br>
.container {<br>
max-width: 510px;<br>
padding-right: 0;<br>
padding-left: 0;<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
.container {<br>
max-width: 700px;<br>
}<br>
} */<br>
@media (min-width: 992px) {<br>
.container {<br>
max-width: 920px;<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
.container {<br>
max-width: 1130px;<br>
}<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Section</li>
<li>Responsive spacings for section<br>
*/<br>
section {<br>
margin-bottom: var(--block-spacing-vertical);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Grid</li>
<li>Minimal grid system with auto-layout columns<br>
*/<br>
.grid {<br>
grid-column-gap: var(--grid-spacing-horizontal);<br>
grid-row-gap: var(--grid-spacing-vertical);<br>
display: grid;<br>
grid-template-columns: 1fr;<br>
margin: 0;<br>
}<br>
@media (min-width: 1280px) {<br>
.grid {<br>
grid-template-columns: repeat(auto-fit, minmax(0%, 1fr));<br>
}<br>
}<br>
.grid &gt; * {<br>
min-width: 0;<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Horizontal scroller (<figure>)<br>
*/<br>
figure {<br>
display: block;<br>
margin: 0;<br>
padding: 0;<br>
overflow-x: auto;<br>
}<br>
figure figcaption {<br>
padding: calc(var(--spacing) * 0.5) 0;<br>
color: var(--muted-color);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Typography<br>
*/<br>
b,<br>
strong {<br>
font-weight: bolder;<br>
}</li>
</ul>
<p>sub,<br>
sup {<br>
position: relative;<br>
font-size: 0.75em;<br>
line-height: 0;<br>
vertical-align: baseline;<br>
}</p>
<p>sub {<br>
bottom: -0.25em;<br>
}</p>
<p>sup {<br>
top: -0.5em;<br>
}</p>
<p>address,<br>
blockquote,<br>
dl,<br>
figure,<br>
form,<br>
ol,<br>
p,<br>
pre,<br>
table,<br>
ul {<br>
margin-top: 0;<br>
margin-bottom: var(--typography-spacing-vertical);<br>
color: var(--color);<br>
font-style: normal;<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
}</p>
<p>a,<br>
[role=&quot;link&quot;] {<br>
--color: var(--primary);<br>
--background-color: transparent;<br>
outline: none;<br>
background-color: var(--background-color);<br>
color: var(--color);<br>
-webkit-text-decoration: var(--text-decoration);<br>
text-decoration: var(--text-decoration);<br>
transition: background-color var(--transition), color var(--transition),<br>
box-shadow var(--transition), -webkit-text-decoration var(--transition);<br>
transition: background-color var(--transition), color var(--transition),<br>
text-decoration var(--transition), box-shadow var(--transition);<br>
transition: background-color var(--transition), color var(--transition),<br>
text-decoration var(--transition), box-shadow var(--transition),<br>
-webkit-text-decoration var(--transition);<br>
}<br>
a:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--primary-hover);<br>
--text-decoration: underline;<br>
}<br>
a:focus,<br>
[role=&quot;link&quot;]:focus {<br>
--background-color: var(--primary-focus);<br>
}<br>
a.secondary,<br>
[role=&quot;link&quot;].secondary {<br>
--color: var(--secondary);<br>
}<br>
a.secondary:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;].secondary:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--secondary-hover);<br>
}<br>
a.secondary:focus,<br>
[role=&quot;link&quot;].secondary:focus {<br>
--background-color: var(--secondary-focus);<br>
}<br>
a.contrast,<br>
[role=&quot;link&quot;].contrast {<br>
--color: var(--contrast);<br>
}<br>
a.contrast:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;].contrast:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--contrast-hover);<br>
}<br>
a.contrast:focus,<br>
[role=&quot;link&quot;].contrast:focus {<br>
--background-color: var(--contrast-focus);<br>
}</p>
<p>h1,<br>
h2,<br>
h3,<br>
h4,<br>
h5,<br>
h6 {<br>
margin-top: 0;<br>
margin-bottom: var(--typography-spacing-vertical);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
font-family: var(--font-family);<br>
}</p>
<p>h1 {<br>
--color: var(--h1-color);<br>
}</p>
<p>h2 {<br>
--color: var(--h2-color);<br>
}</p>
<p>h3 {<br>
--color: var(--h3-color);<br>
}</p>
<p>h4 {<br>
--color: var(--h4-color);<br>
}</p>
<p>h5 {<br>
--color: var(--h5-color);<br>
}</p>
<p>h6 {<br>
--color: var(--h6-color);<br>
}</p>
<p>:where(address, blockquote, dl, figure, form, ol, p, pre, table, ul)<br>
~ :is(h1, h2, h3, h4, h5, h6) {<br>
margin-top: var(--typography-spacing-vertical);<br>
}</p>
<p>hgroup,<br>
.headings {<br>
margin-bottom: var(--typography-spacing-vertical);<br>
}<br>
hgroup &gt; *,<br>
.headings &gt; * {<br>
margin-bottom: 0;<br>
}<br>
hgroup &gt; *:last-child,<br>
.headings &gt; *:last-child {<br>
--color: var(--muted-color);<br>
--font-weight: unset;<br>
font-size: 1rem;<br>
font-family: unset;<br>
}</p>
<p>p {<br>
margin-bottom: var(--typography-spacing-vertical);<br>
}</p>
<p>small {<br>
font-size: var(--font-size);<br>
}</p>
<p>:where(dl, ol, ul) {<br>
padding-right: 0;<br>
padding-left: var(--spacing);<br>
-webkit-padding-start: var(--spacing);<br>
padding-inline-start: var(--spacing);<br>
-webkit-padding-end: 0;<br>
padding-inline-end: 0;<br>
}<br>
:where(dl, ol, ul) li {<br>
margin-bottom: calc(var(--typography-spacing-vertical) * 0.25);<br>
}</p>
<p>:where(dl, ol, ul) :is(dl, ol, ul) {<br>
margin: 0;<br>
margin-top: calc(var(--typography-spacing-vertical) * 0.25);<br>
}</p>
<p>ul li {<br>
list-style: square;<br>
}</p>
<p>mark {<br>
padding: 0.125rem 0.25rem;<br>
background-color: var(--mark-background-color);<br>
color: var(--mark-color);<br>
vertical-align: baseline;<br>
}</p>
<p>blockquote {<br>
display: block;<br>
margin: var(--typography-spacing-vertical) 0;<br>
padding: var(--spacing);<br>
border-right: none;<br>
border-left: 0.25rem solid var(--blockquote-border-color);<br>
-webkit-border-start: 0.25rem solid var(--blockquote-border-color);<br>
border-inline-start: 0.25rem solid var(--blockquote-border-color);<br>
-webkit-border-end: none;<br>
border-inline-end: none;<br>
}<br>
blockquote footer {<br>
margin-top: calc(var(--typography-spacing-vertical) * 0.5);<br>
color: var(--blockquote-footer-color);<br>
}</p>
<p>abbr[title] {<br>
border-bottom: 1px dotted;<br>
text-decoration: none;<br>
cursor: help;<br>
}</p>
<p>ins {<br>
color: var(--ins-color);<br>
text-decoration: none;<br>
}</p>
<p>del {<br>
color: var(--del-color);<br>
}</p>
<p>::-moz-selection {<br>
background-color: var(--primary-focus);<br>
}</p>
<p>::selection {<br>
background-color: var(--primary-focus);<br>
}</p>
<p>/**</p>
<ul>
<li>Embedded content<br>
*/<br>
:where(audio, canvas, iframe, img, svg, video) {<br>
vertical-align: middle;<br>
}</li>
</ul>
<p>audio,<br>
video {<br>
display: inline-block;<br>
}</p>
<p>audio:not([controls]) {<br>
display: none;<br>
height: 0;<br>
}</p>
<p>:where(iframe) {<br>
border-style: none;<br>
}</p>
<p>img {<br>
max-width: 100%;<br>
height: auto;<br>
border-style: none;<br>
}</p>
<p>:where(svg:not([fill])) {<br>
fill: currentColor;<br>
}</p>
<p>svg:not(#mount) {<br>
overflow: hidden;<br>
}</p>
<p>/**</p>
<ul>
<li>Button<br>
*/<br>
button {<br>
margin: 0;<br>
overflow: visible;<br>
font-family: inherit;<br>
text-transform: none;<br>
}</li>
</ul>
<p>button,<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;submit&quot;] {<br>
-webkit-appearance: button;<br>
}</p>
<p>button {<br>
display: block;<br>
width: 100%;<br>
margin-bottom: var(--spacing);<br>
}</p>
<p>[role=&quot;button&quot;] {<br>
display: inline-block;<br>
text-decoration: none;<br>
}</p>
<p>button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
input[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;] {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
--color: var(--primary-inverse);<br>
--box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: 1rem;<br>
line-height: var(--line-height);<br>
text-align: center;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}<br>
button:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;submit&quot;]:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;button&quot;]:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;]:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;button&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--primary-hover);<br>
--border-color: var(--primary-hover);<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
--color: var(--primary-inverse);<br>
}<br>
button:focus,<br>
input[type=&quot;submit&quot;]:focus,<br>
input[type=&quot;button&quot;]:focus,<br>
input[type=&quot;reset&quot;]:focus,<br>
[role=&quot;button&quot;]:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--primary-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary,<br>
input[type=&quot;reset&quot;] {<br>
--background-color: var(--secondary);<br>
--border-color: var(--secondary);<br>
--color: var(--secondary-inverse);<br>
cursor: pointer;<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
--color: var(--secondary-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary:focus,<br>
input[type=&quot;reset&quot;]:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--secondary-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast {<br>
--background-color: var(--contrast);<br>
--border-color: var(--contrast);<br>
--color: var(--contrast-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--contrast-hover);<br>
--border-color: var(--contrast-hover);<br>
--color: var(--contrast-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--contrast-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline,<br>
input[type=&quot;reset&quot;].outline {<br>
--background-color: transparent;<br>
--color: var(--primary);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;].outline:is([aria-current], :hover, :active, :focus) {<br>
--background-color: transparent;<br>
--color: var(--primary-hover);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.secondary,<br>
input[type=&quot;reset&quot;].outline {<br>
--color: var(--secondary);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.secondary:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;].outline:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--secondary-hover);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.contrast {<br>
--color: var(--contrast);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.contrast:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--contrast-hover);<br>
}</p>
<p>:where(<br>
button,<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;]<br>
)[disabled],<br>
:where(fieldset[disabled])<br>
:is(<br>
button,<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;]<br>
),<br>
a[role=&quot;button&quot;]:not([href]) {<br>
opacity: 0.5;<br>
pointer-events: none;<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements<br>
*/<br>
input,<br>
optgroup,<br>
select,<br>
textarea {<br>
margin: 0;<br>
font-size: 1rem;<br>
line-height: var(--line-height);<br>
font-family: inherit;<br>
letter-spacing: inherit;<br>
}</li>
</ul>
<p>input {<br>
overflow: visible;<br>
}</p>
<p>select {<br>
text-transform: none;<br>
}</p>
<p>legend {<br>
max-width: 100%;<br>
padding: 0;<br>
color: inherit;<br>
white-space: normal;<br>
}</p>
<p>textarea {<br>
overflow: auto;<br>
}</p>
<p>[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
padding: 0;<br>
}</p>
<p><VPIcon icon="-webkit-inner-spin-button," />-webkit-outer-spin-button {<br>
height: auto;<br>
}</p>
<p>[type=&quot;search&quot;] {<br>
-webkit-appearance: textfield;<br>
outline-offset: -2px;<br>
}</p>
<p>[type=&quot;search&quot;]::-webkit-search-decoration {<br>
-webkit-appearance: none;<br>
}</p>
<p>::-webkit-file-upload-button {<br>
-webkit-appearance: button;<br>
font: inherit;<br>
}</p>
<p>::-moz-focus-inner {<br>
padding: 0;<br>
border-style: none;<br>
}</p>
<p>:-moz-focusring {<br>
outline: none;<br>
}</p>
<p>:-moz-ui-invalid {<br>
box-shadow: none;<br>
}</p>
<p>::-ms-expand {<br>
display: none;<br>
}</p>
<p>[type=&quot;file&quot;],<br>
[type=&quot;range&quot;] {<br>
padding: 0;<br>
border-width: 0;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;]) {<br>
height: calc(<br>
1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +<br>
var(--border-width) * 2<br>
);<br>
}</p>
<p>fieldset {<br>
margin: 0;<br>
margin-bottom: var(--spacing);<br>
padding: 0;<br>
border: 0;<br>
}</p>
<p>label,<br>
fieldset legend {<br>
display: block;<br>
margin-bottom: calc(var(--spacing) * 0.25);<br>
font-weight: var(--form-label-font-weight, var(--font-weight));<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]),<br>
select,<br>
textarea {<br>
width: 100%;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;], [type=&quot;file&quot;]),<br>
select,<br>
textarea {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
}</p>
<p>input,<br>
select,<br>
textarea {<br>
--background-color: var(--form-element-background-color);<br>
--border-color: var(--form-element-border-color);<br>
--color: var(--form-element-color);<br>
--box-shadow: none;<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[readonly]<br>
):is(:active, :focus),<br>
:where(select, textarea):is(:active, :focus) {<br>
--background-color: var(--form-element-active-background-color);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;switch&quot;],<br>
[readonly]<br>
):is(:active, :focus),<br>
:where(select, textarea):is(:active, :focus) {<br>
--border-color: var(--form-element-active-border-color);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;],<br>
[readonly]<br>
):focus,<br>
select:focus,<br>
textarea:focus {<br>
--box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);<br>
}</p>
<p>input:not([type=&quot;submit&quot;], [type=&quot;button&quot;], [type=&quot;reset&quot;])[disabled],<br>
select[disabled],<br>
textarea[disabled],<br>
:where(fieldset[disabled])<br>
:is(<br>
input:not([type=&quot;submit&quot;], [type=&quot;button&quot;], [type=&quot;reset&quot;]),<br>
select,<br>
textarea<br>
) {<br>
--background-color: var(--form-element-disabled-background-color);<br>
--border-color: var(--form-element-disabled-border-color);<br>
opacity: var(--form-element-disabled-opacity);<br>
pointer-events: none;<br>
}</p>
<p>:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid] {<br>
padding-right: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
padding-left: var(--form-element-spacing-horizontal);<br>
-webkit-padding-start: var(--form-element-spacing-horizontal) !important;<br>
padding-inline-start: var(--form-element-spacing-horizontal) !important;<br>
-webkit-padding-end: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
padding-inline-end: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
background-position: center right 0.75rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}<br>
:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid=&quot;false&quot;] {<br>
background-image: var(--icon-valid);<br>
}<br>
:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid=&quot;true&quot;] {<br>
background-image: var(--icon-invalid);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;false&quot;] {<br>
--border-color: var(--form-element-valid-border-color);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;false&quot;]:is(:active, :focus) {<br>
--border-color: var(--form-element-valid-active-border-color) !important;<br>
--box-shadow: 0 0 0 var(--outline-width) var(--form-element-valid-focus-color) !important;<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;true&quot;] {<br>
--border-color: var(--form-element-invalid-border-color);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;true&quot;]:is(:active, :focus) {<br>
--border-color: var(--form-element-invalid-active-border-color) !important;<br>
--box-shadow: 0 0 0 var(--outline-width)<br>
var(--form-element-invalid-focus-color) !important;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:where(input, select, textarea):not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]):is(<br>
[aria-invalid],<br>
[aria-invalid=&quot;true&quot;],<br>
[aria-invalid=&quot;false&quot;]<br>
) {<br>
background-position: center left 0.75rem;<br>
}</p>
<p>input<VPIcon icon="placeholder,
input" />-webkit-input-placeholder,<br>
textarea<VPIcon icon="placeholder,
textarea" />-webkit-input-placeholder,<br>
select:invalid {<br>
color: var(--form-element-placeholder-color);<br>
opacity: 1;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]),<br>
select,<br>
textarea {<br>
margin-bottom: var(--spacing);<br>
}</p>
<p>select::-ms-expand {<br>
border: 0;<br>
background-color: transparent;<br>
}<br>
select:not([multiple], [size]) {<br>
padding-right: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
padding-left: var(--form-element-spacing-horizontal);<br>
-webkit-padding-start: var(--form-element-spacing-horizontal);<br>
padding-inline-start: var(--form-element-spacing-horizontal);<br>
-webkit-padding-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
padding-inline-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
background-image: var(--icon-chevron);<br>
background-position: center right 0.75rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}</p>
<p>[dir=&quot;rtl&quot;] select:not([multiple], [size]) {<br>
background-position: center left 0.75rem;<br>
}</p>
<p>:where(input, select, textarea) + small {<br>
display: block;<br>
width: 100%;<br>
margin-top: calc(var(--spacing) * -0.75);<br>
margin-bottom: var(--spacing);<br>
color: var(--muted-color);<br>
}</p>
<p>label &gt; :where(input, select, textarea) {<br>
margin-top: calc(var(--spacing) * 0.25);<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements</li>
<li>Checkboxes &amp; Radios<br>
*/<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
width: 1.25em;<br>
height: 1.25em;<br>
margin-top: -0.125em;<br>
margin-right: 0.375em;<br>
margin-left: 0;<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
-webkit-margin-end: 0.375em;<br>
margin-inline-end: 0.375em;<br>
border-width: var(--border-width);<br>
font-size: inherit;<br>
vertical-align: middle;<br>
cursor: pointer;<br>
}<br>
[type=&quot;checkbox&quot;]<VPIcon icon="-ms-check,
[" type="&quot;radio&quot;]" />-ms-check {<br>
display: none;<br>
}<br>
[type=&quot;checkbox&quot;]:checked,<br>
[type=&quot;checkbox&quot;]:checked:active,<br>
[type=&quot;checkbox&quot;]:checked:focus,<br>
[type=&quot;radio&quot;]:checked,<br>
[type=&quot;radio&quot;]:checked:active,<br>
[type=&quot;radio&quot;]:checked:focus {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
background-image: var(--icon-checkbox);<br>
background-position: center;<br>
background-size: 0.75em auto;<br>
background-repeat: no-repeat;<br>
}<br>
[type=&quot;checkbox&quot;] ~ label,<br>
[type=&quot;radio&quot;] ~ label {<br>
display: inline-block;<br>
margin-right: 0.375em;<br>
margin-bottom: 0;<br>
cursor: pointer;<br>
}</li>
</ul>
<p>[type=&quot;checkbox&quot;]:indeterminate {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
background-image: var(--icon-minus);<br>
background-position: center;<br>
background-size: 0.75em auto;<br>
background-repeat: no-repeat;<br>
}</p>
<p>[type=&quot;radio&quot;] {<br>
border-radius: 50%;<br>
}<br>
[type=&quot;radio&quot;]:checked,<br>
[type=&quot;radio&quot;]:checked:active,<br>
[type=&quot;radio&quot;]:checked:focus {<br>
--background-color: var(--primary-inverse);<br>
border-width: 0.35em;<br>
background-image: none;<br>
}</p>
<p>[type=&quot;checkbox&quot;][role=&quot;switch&quot;] {<br>
--background-color: var(--switch-background-color);<br>
--border-color: var(--switch-background-color);<br>
--color: var(--switch-color);<br>
width: 2.25em;<br>
height: 1.25em;<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: 1.25em;<br>
background-color: var(--background-color);<br>
line-height: 1.25em;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:focus {<br>
--background-color: var(--switch-background-color);<br>
--border-color: var(--switch-background-color);<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked {<br>
--background-color: var(--switch-checked-background-color);<br>
--border-color: var(--switch-checked-background-color);<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:before {<br>
display: block;<br>
width: calc(1.25em - (var(--border-width) * 2));<br>
height: 100%;<br>
border-radius: 50%;<br>
background-color: var(--color);<br>
content: &quot;&quot;;<br>
transition: margin 0.1s ease-in-out;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked {<br>
background-image: none;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked::before {<br>
margin-left: calc(1.125em - var(--border-width));<br>
-webkit-margin-start: calc(1.125em - var(--border-width));<br>
margin-inline-start: calc(1.125em - var(--border-width));<br>
}</p>
<p>[type=&quot;checkbox&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;]:checked[aria-invalid=&quot;false&quot;],<br>
[type=&quot;radio&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;radio&quot;]:checked[aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked[aria-invalid=&quot;false&quot;] {<br>
--border-color: var(--form-element-valid-border-color);<br>
}<br>
[type=&quot;checkbox&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;]:checked[aria-invalid=&quot;true&quot;],<br>
[type=&quot;radio&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;radio&quot;]:checked[aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked[aria-invalid=&quot;true&quot;] {<br>
--border-color: var(--form-element-invalid-border-color);<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements</li>
<li>Alternatives input types (Not Checkboxes &amp; Radios)<br>
*/<br>
[type=&quot;color&quot;]<VPIcon icon="-webkit-color-swatch-wrapper {
padding: 0;
}
[" type="&quot;color&quot;]" />-moz-focus-inner {<br>
padding: 0;<br>
}<br>
[type=&quot;color&quot;]<VPIcon icon="-webkit-color-swatch {
border: 0;
border-radius: calc(var(--border-radius) * 0.5);
}
[" type="&quot;color&quot;]" />-moz-color-swatch {<br>
border: 0;<br>
border-radius: calc(var(--border-radius) * 0.5);<br>
}</li>
</ul>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;], [type=&quot;file&quot;]):is(<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
) {<br>
--icon-position: 0.75rem;<br>
--icon-width: 1rem;<br>
padding-right: calc(var(--icon-width) + var(--icon-position));<br>
background-image: var(--icon-date);<br>
background-position: center right var(--icon-position);<br>
background-size: var(--icon-width) auto;<br>
background-repeat: no-repeat;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a> {<br>
background-image: var(--icon-time);<br>
}</p>
<p>[type=&quot;week&quot;]::-webkit-calendar-picker-indicator {<br>
width: var(--icon-width);<br>
margin-right: calc(var(--icon-width) * -1);<br>
margin-left: var(--icon-position);<br>
opacity: 0;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:is(<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
) {<br>
text-align: right;<br>
}</p>
<p>[type=&quot;file&quot;] {<br>
--color: var(--muted-color);<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5) 0;<br>
border: 0;<br>
border-radius: 0;<br>
background: none;<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="file-selector-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />file-selector-button:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="-webkit-file-upload-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -webkit-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />-webkit-file-upload-button:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="-ms-browse {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  margin-inline-start: 0;
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -ms-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />-ms-browse:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}</p>
<p>[type=&quot;range&quot;] {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
width: 100%;<br>
height: 1.25rem;<br>
background: none;<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-webkit-slider-runnable-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -webkit-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[" type="&quot;range&quot;]" />-moz-range-track {<br>
width: 100%;<br>
height: 0.25rem;<br>
border-radius: var(--border-radius);<br>
background-color: var(--range-border-color);<br>
-moz-transition: background-color var(--transition),<br>
box-shadow var(--transition);<br>
transition: background-color var(--transition), box-shadow var(--transition);<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-ms-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -ms-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[" type="&quot;range&quot;]" />-webkit-slider-thumb {<br>
-webkit-appearance: none;<br>
width: 1.25rem;<br>
height: 1.25rem;<br>
margin-top: -0.5rem;<br>
border: 2px solid var(--range-thumb-border-color);<br>
border-radius: 50%;<br>
background-color: var(--range-thumb-color);<br>
cursor: pointer;<br>
-webkit-transition: background-color var(--transition),<br>
transform var(--transition);<br>
transition: background-color var(--transition), transform var(--transition);<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-moz-range-thumb {
  -webkit-appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: -0.5rem;
  border: 2px solid var(--range-thumb-border-color);
  border-radius: 50%;
  background-color: var(--range-thumb-color);
  cursor: pointer;
  -moz-transition: background-color var(--transition),
    transform var(--transition);
  transition: background-color var(--transition), transform var(--transition);
}
[" type="&quot;range&quot;]" />-ms-thumb {<br>
-webkit-appearance: none;<br>
width: 1.25rem;<br>
height: 1.25rem;<br>
margin-top: -0.5rem;<br>
border: 2px solid var(--range-thumb-border-color);<br>
border-radius: 50%;<br>
background-color: var(--range-thumb-color);<br>
cursor: pointer;<br>
-ms-transition: background-color var(--transition),<br>
transform var(--transition);<br>
transition: background-color var(--transition), transform var(--transition);<br>
}<br>
[type=&quot;range&quot;]:hover,<br>
[type=&quot;range&quot;]:focus {<br>
--range-border-color: var(--range-active-border-color);<br>
--range-thumb-color: var(--range-thumb-hover-color);<br>
}<br>
[type=&quot;range&quot;]:active {<br>
--range-thumb-color: var(--range-thumb-active-color);<br>
}<br>
[type=&quot;range&quot;]:active<VPIcon icon="-webkit-slider-thumb {
  transform: scale(1.25);
}
[" type="&quot;range&quot;]:active" />-moz-range-thumb {<br>
transform: scale(1.25);<br>
}<br>
[type=&quot;range&quot;]:active::-ms-thumb {<br>
transform: scale(1.25);<br>
}</p>
<p>input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;] {<br>
-webkit-padding-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);<br>
padding-inline-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);<br>
border-radius: 5rem;<br>
background-image: var(--icon-search);<br>
background-position: center left 1.125rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid] {<br>
-webkit-padding-start: calc(<br>
var(--form-element-spacing-horizontal) + 1.75rem<br>
) !important;<br>
padding-inline-start: calc(<br>
var(--form-element-spacing-horizontal) + 1.75rem<br>
) !important;<br>
background-position: center left 1.125rem, center right 0.75rem;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid=&quot;false&quot;] {<br>
background-image: var(--icon-search), var(--icon-valid);<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid=&quot;true&quot;] {<br>
background-image: var(--icon-search), var(--icon-invalid);<br>
}</p>
<p>[type=&quot;search&quot;]::-webkit-search-cancel-button {<br>
-webkit-appearance: none;<br>
display: none;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:where(input):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;] {<br>
background-position: center right 1.125rem;<br>
}<br>
[dir=&quot;rtl&quot;]<br>
:where(input):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid] {<br>
background-position: center right 1.125rem, center left 0.75rem;<br>
}</p>
<p>/**</p>
<ul>
<li>Table<br>
*/<br>
:where(table) {<br>
width: 100%;<br>
border-collapse: collapse;<br>
border-spacing: 0;<br>
text-indent: 0;<br>
}</li>
</ul>
<p>th,<br>
td {<br>
padding: calc(var(--spacing) / 2) var(--spacing);<br>
border-bottom: var(--border-width) solid var(--table-border-color);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
text-align: left;<br>
text-align: start;<br>
}</p>
<p>tfoot th,<br>
tfoot td {<br>
border-top: var(--border-width) solid var(--table-border-color);<br>
border-bottom: 0;<br>
}</p>
<p>table[role=&quot;grid&quot;] tbody tr:nth-child(odd) {<br>
background-color: var(--table-row-stripped-background-color);<br>
}</p>
<p>/**</p>
<ul>
<li>Code<br>
*/<br>
pre,<br>
code,<br>
kbd,<br>
samp {<br>
font-size: 0.875em;<br>
font-family: var(--font-family);<br>
}</li>
</ul>
<p>pre {<br>
-ms-overflow-style: scrollbar;<br>
overflow: auto;<br>
}</p>
<p>pre,<br>
code,<br>
kbd {<br>
border-radius: var(--border-radius);<br>
background: var(--code-background-color);<br>
color: var(--code-color);<br>
font-weight: var(--font-weight);<br>
line-height: initial;<br>
}</p>
<p>code,<br>
kbd {<br>
display: inline-block;<br>
padding: 0.375rem 0.5rem;<br>
}</p>
<p>pre {<br>
display: block;<br>
margin-bottom: var(--spacing);<br>
overflow-x: auto;<br>
}<br>
pre &gt; code {<br>
display: block;<br>
padding: var(--spacing);<br>
background: none;<br>
font-size: 14px;<br>
line-height: var(--line-height);<br>
}</p>
<p>code b {<br>
color: var(--code-tag-color);<br>
font-weight: var(--font-weight);<br>
}<br>
code i {<br>
color: var(--code-property-color);<br>
font-style: normal;<br>
}<br>
code u {<br>
color: var(--code-value-color);<br>
text-decoration: none;<br>
}<br>
code em {<br>
color: var(--code-comment-color);<br>
font-style: normal;<br>
}</p>
<p>kbd {<br>
background-color: var(--code-kbd-background-color);<br>
color: var(--code-kbd-color);<br>
vertical-align: baseline;<br>
}</p>
<p>/**</p>
<ul>
<li>Miscs<br>
*/<br>
hr {<br>
height: 0;<br>
border: 0;<br>
border-top: 1px solid var(--muted-border-color);<br>
color: inherit;<br>
}</li>
</ul>
<p>[hidden],<br>
template {<br>
display: none !important;<br>
}</p>
<p>canvas {<br>
display: inline-block;<br>
}</p>
<p>/**</p>
<ul>
<li>Accordion (<details>)<br>
*/<br>
details {<br>
display: block;<br>
margin-bottom: var(--spacing);<br>
padding-bottom: var(--spacing);<br>
border-bottom: var(--border-width) solid var(--accordion-border-color);<br>
}<br>
details summary {<br>
line-height: 1rem;<br>
list-style-type: none;<br>
cursor: pointer;<br>
transition: color var(--transition);<br>
}<br>
details summary:not([role]) {<br>
color: var(--accordion-close-summary-color);<br>
}<br>
details summary<VPIcon icon="-webkit-details-marker {
display: none;
}
details summary" />marker {<br>
display: none;<br>
}<br>
details summary<VPIcon icon="-moz-list-bullet {
list-style-type: none;
}
details summary" />after {<br>
display: block;<br>
width: 1rem;<br>
height: 1rem;<br>
-webkit-margin-start: calc(var(--spacing, 1rem) * 0.5);<br>
margin-inline-start: calc(var(--spacing, 1rem) * 0.5);<br>
float: right;<br>
transform: rotate(-90deg);<br>
background-image: var(--icon-chevron);<br>
background-position: right center;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
content: &quot;&quot;;<br>
transition: transform var(--transition);<br>
}<br>
details summary:focus {<br>
outline: none;<br>
}<br>
details summary:focus:not([role=&quot;button&quot;]) {<br>
color: var(--accordion-active-summary-color);<br>
}<br>
details summary[role=&quot;button&quot;] {<br>
width: 100%;<br>
text-align: left;<br>
}<br>
details summary[role=&quot;button&quot;]<VPIcon icon="after {
height: calc(1rem * var(--line-height, 1.5));
background-image: var(--icon-chevron-button);
}
details summary" [role="&quot;button&quot;]:not(.outline).contrast" />after {<br>
background-image: var(--icon-chevron-button-inverse);<br>
}<br>
details[open] &gt; summary {<br>
margin-bottom: calc(var(--spacing));<br>
}<br>
details[open] &gt; summary:not([role]):not(:focus) {<br>
color: var(--accordion-open-summary-color);<br>
}<br>
details[open] &gt; summary::after {<br>
transform: rotate(0);<br>
}</li>
</ul>
<p>[dir=&quot;rtl&quot;] details summary {<br>
text-align: right;<br>
}<br>
[dir=&quot;rtl&quot;] details summary::after {<br>
float: left;<br>
background-position: left center;<br>
}</p>
<p>/**</p>
<ul>
<li>Card (<article>)<br>
*/<br>
article {<br>
margin: var(--block-spacing-vertical) 0;<br>
padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);<br>
border-radius: var(--border-radius);<br>
background: var(--card-background-color);<br>
box-shadow: var(--card-box-shadow);<br>
}<br>
article &gt; header,<br>
article &gt; footer {<br>
margin-right: calc(var(--block-spacing-horizontal) * -1);<br>
margin-left: calc(var(--block-spacing-horizontal) * -1);<br>
padding: calc(var(--block-spacing-vertical) * 0.66)<br>
var(--block-spacing-horizontal);<br>
background-color: var(--card-sectionning-background-color);<br>
}<br>
article &gt; header {<br>
margin-top: calc(var(--block-spacing-vertical) * -1);<br>
margin-bottom: var(--block-spacing-vertical);<br>
border-bottom: var(--border-width) solid var(--card-border-color);<br>
border-top-right-radius: var(--border-radius);<br>
border-top-left-radius: var(--border-radius);<br>
}<br>
article &gt; footer {<br>
margin-top: var(--block-spacing-vertical);<br>
margin-bottom: calc(var(--block-spacing-vertical) * -1);<br>
border-top: var(--border-width) solid var(--card-border-color);<br>
border-bottom-right-radius: var(--border-radius);<br>
border-bottom-left-radius: var(--border-radius);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Modal (<dialog>)<br>
*/<br>
#mount {<br>
--scrollbar-width: 0px;<br>
}</li>
</ul>
<p>dialog {<br>
display: flex;<br>
z-index: 999;<br>
position: fixed;<br>
top: 0;<br>
right: 0;<br>
bottom: 0;<br>
left: 0;<br>
align-items: center;<br>
justify-content: center;<br>
width: inherit;<br>
min-width: 100%;<br>
height: inherit;<br>
min-height: 100%;<br>
padding: var(--spacing);<br>
border: 0;<br>
-webkit-backdrop-filter: var(--modal-overlay-backdrop-filter);<br>
backdrop-filter: var(--modal-overlay-backdrop-filter);<br>
background-color: var(--modal-overlay-background-color);<br>
color: var(--color);<br>
}<br>
dialog article {<br>
max-height: calc(100vh - var(--spacing) * 2);<br>
overflow: auto;<br>
}<br>
@media (min-width: 576px) {<br>
dialog article {<br>
max-width: 510px;<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
dialog article {<br>
max-width: 700px;<br>
}<br>
}<br>
dialog article &gt; header,<br>
dialog article &gt; footer {<br>
padding: calc(var(--block-spacing-vertical) * 0.5)<br>
var(--block-spacing-horizontal);<br>
}<br>
dialog article &gt; header .close {<br>
margin: 0;<br>
margin-left: var(--spacing);<br>
float: right;<br>
}<br>
dialog article &gt; footer {<br>
text-align: right;<br>
}<br>
dialog article &gt; footer [role=&quot;button&quot;] {<br>
margin-bottom: 0;<br>
}<br>
dialog article &gt; footer [role=&quot;button&quot;]:not(:first-of-type) {<br>
margin-left: calc(var(--spacing) * 0.5);<br>
}<br>
dialog article p:last-of-type {<br>
margin: 0;<br>
}<br>
dialog article .close {<br>
display: block;<br>
width: 1rem;<br>
height: 1rem;<br>
margin-top: calc(var(--block-spacing-vertical) * -0.5);<br>
margin-bottom: var(--typography-spacing-vertical);<br>
margin-left: auto;<br>
background-image: var(--icon-close);<br>
background-position: center;<br>
background-size: auto 1rem;<br>
background-repeat: no-repeat;<br>
opacity: 0.5;<br>
transition: opacity var(--transition);<br>
}<br>
dialog article .close:is([aria-current], :hover, :active, :focus) {<br>
opacity: 1;<br>
}<br>
dialog:not([open]),<br>
dialog[open=&quot;false&quot;] {<br>
display: none;<br>
}</p>
<p>.modal-is-open {<br>
padding-right: var(--scrollbar-width, 0px);<br>
overflow: hidden;<br>
pointer-events: none;<br>
}<br>
.modal-is-open dialog {<br>
pointer-events: auto;<br>
}</p>
<p>:where(.modal-is-opening, .modal-is-closing) dialog,<br>
:where(.modal-is-opening, .modal-is-closing) dialog &gt; article {<br>
animation-duration: 0.2s;<br>
animation-timing-function: ease-in-out;<br>
animation-fill-mode: both;<br>
}<br>
:where(.modal-is-opening, .modal-is-closing) dialog {<br>
animation-duration: 0.8s;<br>
animation-name: modal-overlay;<br>
}<br>
:where(.modal-is-opening, .modal-is-closing) dialog &gt; article {<br>
animation-delay: 0.2s;<br>
animation-name: modal;<br>
}</p>
<p>.modal-is-closing dialog,<br>
.modal-is-closing dialog &gt; article {<br>
animation-delay: 0s;<br>
animation-direction: reverse;<br>
}</p>
<p>@keyframes modal-overlay {<br>
from {<br>
-webkit-backdrop-filter: none;<br>
backdrop-filter: none;<br>
background-color: transparent;<br>
}<br>
}<br>
@keyframes modal {<br>
from {<br>
transform: translateY(-100%);<br>
opacity: 0;<br>
}<br>
}<br>
/**</p>
<ul>
<li>Nav<br>
*/<br>
:where(nav li)::before {<br>
float: left;<br>
content: &quot;​&quot;;<br>
}</li>
</ul>
<p>nav,<br>
nav ul {<br>
display: flex;<br>
}</p>
<p>nav {<br>
justify-content: space-between;<br>
}<br>
nav ol,<br>
nav ul {<br>
align-items: center;<br>
margin-bottom: 0;<br>
padding: 0;<br>
list-style: none;<br>
}<br>
nav ol:first-of-type,<br>
nav ul:first-of-type {<br>
margin-left: calc(var(--nav-element-spacing-horizontal) * -1);<br>
}<br>
nav ol:last-of-type,<br>
nav ul:last-of-type {<br>
margin-right: calc(var(--nav-element-spacing-horizontal) * -1);<br>
}<br>
nav li {<br>
display: inline-block;<br>
margin: 0;<br>
padding: var(--nav-element-spacing-vertical)<br>
var(--nav-element-spacing-horizontal);<br>
}<br>
nav li &gt; * {<br>
--spacing: 0;<br>
}<br>
nav :where(a, [role=&quot;link&quot;]) {<br>
display: inline-block;<br>
margin: calc(var(--nav-link-spacing-vertical) * -1)<br>
calc(var(--nav-link-spacing-horizontal) * -1);<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
border-radius: var(--border-radius);<br>
text-decoration: none;<br>
}<br>
nav :where(a, [role=&quot;link&quot;]):is([aria-current], :hover, :active, :focus) {<br>
text-decoration: none;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] {<br>
align-items: center;<br>
justify-content: start;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:first-child) {<br>
-webkit-margin-start: var(--nav-link-spacing-horizontal);<br>
margin-inline-start: var(--nav-link-spacing-horizontal);<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:last-child) ::after {<br>
position: absolute;<br>
width: calc(var(--nav-link-spacing-horizontal) * 2);<br>
-webkit-margin-start: calc(var(--nav-link-spacing-horizontal) / 2);<br>
margin-inline-start: calc(var(--nav-link-spacing-horizontal) / 2);<br>
content: &quot;/&quot;;<br>
color: var(--muted-color);<br>
text-align: center;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] a[aria-current] {<br>
background-color: transparent;<br>
color: inherit;<br>
text-decoration: none;<br>
pointer-events: none;<br>
}<br>
nav [role=&quot;button&quot;] {<br>
margin-right: inherit;<br>
margin-left: inherit;<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
}</p>
<p>aside nav,<br>
aside ol,<br>
aside ul,<br>
aside li {<br>
display: block;<br>
}<br>
aside li {<br>
padding: calc(var(--nav-element-spacing-vertical) * 0.5)<br>
var(--nav-element-spacing-horizontal);<br>
}<br>
aside li a {<br>
display: block;<br>
}<br>
aside li [role=&quot;button&quot;] {<br>
margin: inherit;<br>
}</p>
<p>[dir=&quot;rtl&quot;] nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:last-child) ::after {<br>
content: &quot;\&quot;;<br>
}</p>
<p>/**</p>
<ul>
<li>Progress<br>
*/<br>
progress {<br>
display: inline-block;<br>
vertical-align: baseline;<br>
}</li>
</ul>
<p>progress {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
display: inline-block;<br>
appearance: none;<br>
width: 100%;<br>
height: 0.5rem;<br>
margin-bottom: calc(var(--spacing) * 0.5);<br>
overflow: hidden;<br>
border: 0;<br>
border-radius: var(--border-radius);<br>
background-color: var(--progress-background-color);<br>
color: var(--progress-color);<br>
}<br>
progress<VPIcon icon="-webkit-progress-bar {
  border-radius: var(--border-radius);
  background: none;
}
progress[value]" />-webkit-progress-value {<br>
background-color: var(--progress-color);<br>
}<br>
progress<VPIcon icon="-moz-progress-bar {
  background-color: var(--progress-color);
}
@media (prefers-reduced-motion: no-preference) {
  progress:indeterminate {
    background: var(--progress-background-color)
      linear-gradient(
        to right,
        var(--progress-color) 30%,
        var(--progress-background-color) 30%
      )
      top left/150% 150% no-repeat;
    animation: progress-indeterminate 1s linear infinite;
  }
  progress:indeterminate[value]" />-webkit-progress-value {<br>
background-color: transparent;<br>
}<br>
progress:indeterminate::-moz-progress-bar {<br>
background-color: transparent;<br>
}<br>
}</p>
<p>@media (prefers-reduced-motion: no-preference) {<br>
[dir=&quot;rtl&quot;] progress:indeterminate {<br>
animation-direction: reverse;<br>
}<br>
}</p>
<p>@keyframes progress-indeterminate {<br>
0% {<br>
background-position: 200% 0;<br>
}<br>
100% {<br>
background-position: -200% 0;<br>
}<br>
}<br>
/**</p>
<ul>
<li>Dropdown ([role=&quot;list&quot;])<br>
*/<br>
details[role=&quot;list&quot;],<br>
li[role=&quot;list&quot;] {<br>
position: relative;<br>
}</li>
</ul>
<p>details[role=&quot;list&quot;] summary + ul,<br>
li[role=&quot;list&quot;] &gt; ul {<br>
display: flex;<br>
z-index: 99;<br>
position: absolute;<br>
top: auto;<br>
right: 0;<br>
left: 0;<br>
flex-direction: column;<br>
margin: 0;<br>
padding: 0;<br>
border: var(--border-width) solid var(--dropdown-border-color);<br>
border-radius: var(--border-radius);<br>
border-top-right-radius: 0;<br>
border-top-left-radius: 0;<br>
background-color: var(--dropdown-background-color);<br>
box-shadow: var(--card-box-shadow);<br>
color: var(--dropdown-color);<br>
white-space: nowrap;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li,<br>
li[role=&quot;list&quot;] &gt; ul li {<br>
width: 100%;<br>
margin-bottom: 0;<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5)<br>
var(--form-element-spacing-horizontal);<br>
list-style: none;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li:first-of-type,<br>
li[role=&quot;list&quot;] &gt; ul li:first-of-type {<br>
margin-top: calc(var(--form-element-spacing-vertical) * 0.5);<br>
}<br>
details[role=&quot;list&quot;] summary + ul li:last-of-type,<br>
li[role=&quot;list&quot;] &gt; ul li:last-of-type {<br>
margin-bottom: calc(var(--form-element-spacing-vertical) * 0.5);<br>
}<br>
details[role=&quot;list&quot;] summary + ul li a,<br>
li[role=&quot;list&quot;] &gt; ul li a {<br>
display: block;<br>
margin: calc(var(--form-element-spacing-vertical) * -0.5)<br>
calc(var(--form-element-spacing-horizontal) * -1);<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5)<br>
var(--form-element-spacing-horizontal);<br>
overflow: hidden;<br>
color: var(--dropdown-color);<br>
text-decoration: none;<br>
text-overflow: ellipsis;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li a:hover,<br>
li[role=&quot;list&quot;] &gt; ul li a:hover {<br>
background-color: var(--dropdown-hover-background-color);<br>
}</p>
<p>details[role=&quot;list&quot;] summary<VPIcon icon="after,
li> a" [role="&quot;list&quot;]" />after {<br>
display: block;<br>
width: 1rem;<br>
height: calc(1rem * var(--line-height, 1.5));<br>
-webkit-margin-start: 0.5rem;<br>
margin-inline-start: 0.5rem;<br>
float: right;<br>
transform: rotate(0deg);<br>
background-position: right center;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
content: &quot;&quot;;<br>
}</p>
<p>details[role=&quot;list&quot;] {<br>
padding: 0;<br>
border-bottom: none;<br>
}<br>
details[role=&quot;list&quot;] summary {<br>
margin-bottom: 0;<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]) {<br>
height: calc(<br>
1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +<br>
var(--border-width) * 2<br>
);<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--form-element-border-color);<br>
border-radius: var(--border-radius);<br>
background-color: var(--form-element-background-color);<br>
color: var(--form-element-placeholder-color);<br>
line-height: inherit;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]):active,<br>
details[role=&quot;list&quot;] summary:not([role]):focus {<br>
border-color: var(--form-element-active-border-color);<br>
background-color: var(--form-element-active-background-color);<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]):focus {<br>
box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);<br>
}<br>
details[role=&quot;list&quot;][open] summary {<br>
border-bottom-right-radius: 0;<br>
border-bottom-left-radius: 0;<br>
}<br>
details[role=&quot;list&quot;][open] summary::before {<br>
display: block;<br>
z-index: 1;<br>
position: fixed;<br>
top: 0;<br>
right: 0;<br>
bottom: 0;<br>
left: 0;<br>
background: none;<br>
content: &quot;&quot;;<br>
cursor: default;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary,<br>
nav li[role=&quot;list&quot;] a {<br>
display: flex;<br>
direction: ltr;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary + ul,<br>
nav li[role=&quot;list&quot;] &gt; ul {<br>
min-width: -moz-fit-content;<br>
min-width: fit-content;<br>
border-radius: var(--border-radius);<br>
}<br>
nav details[role=&quot;list&quot;] summary + ul li a,<br>
nav li[role=&quot;list&quot;] &gt; ul li a {<br>
border-radius: 0;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary,<br>
nav details[role=&quot;list&quot;] summary:not([role]) {<br>
height: auto;<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
}<br>
nav details[role=&quot;list&quot;][open] summary {<br>
border-radius: var(--border-radius);<br>
}<br>
nav details[role=&quot;list&quot;] summary + ul {<br>
margin-top: var(--outline-width);<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
}<br>
nav details[role=&quot;list&quot;] summary[role=&quot;link&quot;] {<br>
margin-bottom: calc(var(--nav-link-spacing-vertical) * -1);<br>
line-height: var(--line-height);<br>
}<br>
nav details[role=&quot;list&quot;] summary[role=&quot;link&quot;] + ul {<br>
margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));<br>
-webkit-margin-start: calc(var(--nav-link-spacing-horizontal) * -1);<br>
margin-inline-start: calc(var(--nav-link-spacing-horizontal) * -1);<br>
}</p>
<p>li[role=&quot;list&quot;]:hover &gt; ul,<br>
li[role=&quot;list&quot;] a:active ~ ul,<br>
li[role=&quot;list&quot;] a:focus ~ ul {<br>
display: flex;<br>
}<br>
li[role=&quot;list&quot;] &gt; ul {<br>
display: none;<br>
margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));<br>
-webkit-margin-start: calc(<br>
var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)<br>
);<br>
margin-inline-start: calc(<br>
var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)<br>
);<br>
}<br>
li[role=&quot;list&quot;] &gt; a::after {<br>
background-image: var(--icon-chevron);<br>
}</p>
<p>/**</p>
<ul>
<li>Loading ([aria-busy=true])<br>
*/<br>
[aria-busy=&quot;true&quot;] {<br>
cursor: progress;<br>
}</li>
</ul>
<p>[aria-busy=&quot;true&quot;]:not(input, select, textarea)<VPIcon icon="before {
  display: inline-block;
  width: 1em;
  height: 1em;
  border: 0.1875em solid currentColor;
  border-radius: 1em;
  border-right-color: transparent;
  content: "";
  vertical-align: text-bottom;
  vertical-align: -0.125em;
  animation: spinner 0.75s linear infinite;
  opacity: var(--loading-spinner-opacity);
}
[select, textarea):not(:empty)" aria-busy="&quot;true&quot;]:not(input," />before {<br>
margin-right: calc(var(--spacing) * 0.5);<br>
margin-left: 0;<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
-webkit-margin-end: calc(var(--spacing) * 0.5);<br>
margin-inline-end: calc(var(--spacing) * 0.5);<br>
}<br>
[aria-busy=&quot;true&quot;]:not(input, select, textarea):empty {<br>
text-align: center;<br>
}</p>
<p>button[aria-busy=&quot;true&quot;],<br>
input[type=&quot;submit&quot;][aria-busy=&quot;true&quot;],<br>
input[type=&quot;button&quot;][aria-busy=&quot;true&quot;],<br>
input[type=&quot;reset&quot;][aria-busy=&quot;true&quot;],<br>
a[aria-busy=&quot;true&quot;] {<br>
pointer-events: none;<br>
}</p>
<p>@keyframes spinner {<br>
to {<br>
transform: rotate(360deg);<br>
}<br>
}<br>
/**</p>
<ul>
<li>Tooltip ([data-tooltip])<br>
*/<br>
[data-tooltip] {<br>
position: relative;<br>
}<br>
[data-tooltip]:not(a, button, input) {<br>
border-bottom: 1px dotted;<br>
text-decoration: none;<br>
cursor: help;<br>
}<br>
[data-tooltip][data-placement=&quot;top&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;top&quot;]" />after,<br>
[data-tooltip]<VPIcon icon="before,
[data-tooltip]" />after {<br>
display: block;<br>
z-index: 99;<br>
position: absolute;<br>
bottom: 100%;<br>
left: 50%;<br>
padding: 0.25rem 0.5rem;<br>
overflow: hidden;<br>
transform: translate(-50%, -0.25rem);<br>
border-radius: var(--border-radius);<br>
background: var(--tooltip-background-color);<br>
content: attr(data-tooltip);<br>
color: var(--tooltip-color);<br>
font-style: normal;<br>
font-weight: var(--font-weight);<br>
font-size: 0.875rem;<br>
text-decoration: none;<br>
text-overflow: ellipsis;<br>
white-space: nowrap;<br>
opacity: 0;<br>
pointer-events: none;<br>
}<br>
[data-tooltip][data-placement=&quot;top&quot;]<VPIcon icon="after,
[data-tooltip]" />after {<br>
padding: 0;<br>
transform: translate(-50%, 0rem);<br>
border-top: 0.3rem solid;<br>
border-right: 0.3rem solid transparent;<br>
border-left: 0.3rem solid transparent;<br>
border-radius: 0;<br>
background-color: transparent;<br>
content: &quot;&quot;;<br>
color: var(--tooltip-background-color);<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;bottom&quot;]" />after {<br>
top: 100%;<br>
bottom: auto;<br>
transform: translate(-50%, 0.25rem);<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:after {<br>
transform: translate(-50%, -0.3rem);<br>
border: 0.3rem solid transparent;<br>
border-bottom: 0.3rem solid;<br>
}<br>
[data-tooltip][data-placement=&quot;left&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;left&quot;]" />after {<br>
top: 50%;<br>
right: 100%;<br>
bottom: auto;<br>
left: auto;<br>
transform: translate(-0.25rem, -50%);<br>
}<br>
[data-tooltip][data-placement=&quot;left&quot;]:after {<br>
transform: translate(0.3rem, -50%);<br>
border: 0.3rem solid transparent;<br>
border-left: 0.3rem solid;<br>
}<br>
[data-tooltip][data-placement=&quot;right&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;right&quot;]" />after {<br>
top: 50%;<br>
right: auto;<br>
bottom: auto;<br>
left: 100%;<br>
transform: translate(0.25rem, -50%);<br>
}<br>
[data-tooltip][data-placement=&quot;right&quot;]:after {<br>
transform: translate(-0.3rem, -50%);<br>
border: 0.3rem solid transparent;<br>
border-right: 0.3rem solid;<br>
}<br>
[data-tooltip]:focus<VPIcon icon="before,
[data-tooltip]:focus" />after,<br>
[data-tooltip]:hover<VPIcon icon="before,
[data-tooltip]:hover" />after {<br>
opacity: 1;<br>
}<br>
@media (hover: hover) and (pointer: fine) {<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover [data-tooltip]:focus<VPIcon icon="before,
[data-tooltip][[data-tooltip]:focus" data-placement="&quot;bottom&quot;]:hover" />after,<br>
[data-tooltip]:hover<VPIcon icon="before,
[data-tooltip]:hover" />after {<br>
animation-duration: 0.2s;<br>
animation-name: tooltip-slide-top;<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="after,
[data-tooltip][[data-tooltip]:focus" data-placement="&quot;bottom&quot;]:hover" />after,<br>
[data-tooltip]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-top;
}
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;bottom&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-bottom;
}
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-bottom;
}
[data-tooltip][" data-placement="&quot;left&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;left&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;left&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;left&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-left;
}
[data-tooltip][" data-placement="&quot;left&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;left&quot;]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-left;
}
[data-tooltip][" data-placement="&quot;right&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;right&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;right&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;right&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-right;
}
[data-tooltip][" data-placement="&quot;right&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;right&quot;]:hover::after {<br>
animation-name: tooltip-caret-slide-right;<br>
}<br>
}<br>
@keyframes tooltip-slide-top {<br>
from {<br>
transform: translate(-50%, 0.75rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, -0.25rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-top {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-50%, -0.25rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, 0rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-bottom {<br>
from {<br>
transform: translate(-50%, -0.75rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, 0.25rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-bottom {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-50%, -0.5rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, -0.3rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-left {<br>
from {<br>
transform: translate(0.75rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-0.25rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-left {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(0.05rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(0.3rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-right {<br>
from {<br>
transform: translate(-0.75rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(0.25rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-right {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-0.05rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-0.3rem, -50%);<br>
opacity: 1;<br>
}<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Accessibility &amp; User interaction<br>
*/<br>
[aria-controls] {<br>
cursor: pointer;<br>
}</li>
</ul>
<p>[aria-disabled=&quot;true&quot;],<br>
[disabled] {<br>
cursor: not-allowed;<br>
}</p>
<p>[aria-hidden=&quot;false&quot;][hidden] {<br>
display: initial;<br>
}</p>
<p>[aria-hidden=&quot;false&quot;][hidden]:not(:focus) {<br>
clip: rect(0, 0, 0, 0);<br>
position: absolute;<br>
}</p>
<p>a,<br>
area,<br>
button,<br>
input,<br>
label,<br>
select,<br>
summary,<br>
textarea,<br>
[tabindex] {<br>
-ms-touch-action: manipulation;<br>
}</p>
<p>[dir=&quot;rtl&quot;] {<br>
direction: rtl;<br>
}</p>
<p>/**</p>
<ul>
<li>Reduce Motion Features<br>
*/<br>
@media (prefers-reduced-motion: reduce) {<br>
*:not([aria-busy=&quot;true&quot;]),<br>
:not([aria-busy=&quot;true&quot;])<VPIcon icon="before,
:not([" aria-busy="&quot;true&quot;])" />after {<br>
background-attachment: initial !important;<br>
animation-duration: 1ms !important;<br>
animation-delay: -1ms !important;<br>
animation-iteration-count: 1 !important;<br>
scroll-behavior: auto !important;<br>
transition-delay: 0s !important;<br>
transition-duration: 0s !important;<br>
}<br>
}</li>
</ul>
<p>#mount {<br>
/* --primary: rgb(227, 59, 126); */<br>
--primary: #ea4c89;<br>
--primary-hover: #f082ac;<br>
--icon-xia: url(&quot;data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgaWQ9IkZyYW1lIj4KPHBhdGggaWQ9IlZlY3RvciIgZD0iTTguMDAyOTEgOS42Nzk4M0wzLjgzMzM5IDUuNTEyMjFMMy4wMjUzOSA2LjMxOTgzTDguMDAzMjkgMTEuMjk1MUwxMi45NzYyIDYuMzE5ODNMMTIuMTY3OSA1LjUxMjIxTDguMDAyOTEgOS42Nzk4M1oiIGZpbGw9IiM4MzgzODMiLz4KPC9nPgo8L3N2Zz4K&quot;);<br>
--switch-checked-background-color: var(--primary);<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--primary: #e23c7c;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>[data-theme=&quot;dark&quot;] {<br>
--primary: #e23c7c;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>[data-theme=&quot;light&quot;] {<br>
--primary: #ea4c89;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>li.select-link.select-link:hover &gt; ul {<br>
display: none;<br>
}<br>
li.select-link.select-link &gt; ul {<br>
display: none;<br>
}<br>
li.select-link.select-link a:focus ~ ul {<br>
display: none;<br>
}</p>
<p>li.select-link.select-link a:active ~ ul {<br>
display: none;<br>
}<br>
li.select-link-active.select-link-active &gt; ul {<br>
display: flex;<br>
}<br>
li.select-link-active.select-link-active:hover &gt; ul {<br>
display: flex;<br>
}</p>
<p>li.select-link-active.select-link-active a:focus ~ ul {<br>
display: flex;<br>
}</p>
<p>li.select-link-active.select-link-active a:active ~ ul {<br>
display: flex;<br>
}<br>
ul.select-link-ul.select-link-ul {<br>
right: 0px;<br>
left: auto;<br>
}</p>
<p>a.select-link-selected {<br>
background-color: var(--primary-focus);<br>
}<br>
.immersive-translate-no-select {<br>
-webkit-touch-callout: none; /* iOS Safari <em>/<br>
-webkit-user-select: none; /</em> Safari <em>/<br>
-khtml-user-select: none; /</em> Konqueror HTML <em>/<br>
-moz-user-select: none; /</em> Old versions of Firefox <em>/<br>
-ms-user-select: none; /</em> Internet Explorer/Edge */<br>
user-select: none;<br>
}</p>
<p>/* li[role=&quot;list&quot;].no-arrow &gt; a<VPIcon icon="after { */
  background-image: none; */
/*   width: 0; */
/*   color: var(--color); */
/* } */
li{
  margin-left: 8px;
  padding-right: 0;
}
li> a" [role="&quot;list&quot;]" color="*" />after {<br>
-webkit-margin-start: 0.2rem;<br>
margin-inline-start: 0.2rem;<br>
}</p>
<p>li[role=&quot;list&quot;].no-arrow &gt; a,<br>
li[role=&quot;list&quot;].no-arrow &gt; a:link,<br>
li[role=&quot;list&quot;].no-arrow &gt; a:visited {<br>
color: var(--secondary);<br>
}</p>
<p>select.min-select {<br>
--form-element-spacing-horizontal: 0;<br>
margin-bottom: 4px;<br>
max-width: 128px;<br>
overflow: hidden;<br>
color: var(--primary);<br>
font-size: 13px;<br>
border: none;<br>
padding: 0;<br>
padding-right: 20px;<br>
padding-left: 8px;<br>
text-overflow: ellipsis;<br>
color: var(--color);<br>
}<br>
select.min-select-secondary {<br>
color: var(--color);<br>
}<br>
select.min-select:focus {<br>
outline: none;<br>
border: none;<br>
--box-shadow: none;<br>
}<br>
select.min-select-no-arrow {<br>
background-image: none;<br>
padding-right: 0;<br>
}</p>
<p>select.min-select-left {<br>
padding-right: 0px;<br>
/* padding-left: 24px; <em>/<br>
/</em> background-position: center left 0; */<br>
text-overflow: ellipsis;<br>
text-align: left;<br>
}</p>
<p>.muted {<br>
color: var(--muted-color);<br>
}</p>
<p>.select.button-select {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
--color: var(--secondary-inverse);<br>
cursor: pointer;<br>
--box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: 16px;<br>
line-height: var(--line-height);<br>
text-align: center;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
-webkit-appearance: button;<br>
margin: 0;<br>
margin-bottom: 0px;<br>
overflow: visible;<br>
font-family: inherit;<br>
text-transform: none;<br>
}</p>
<p>body {<br>
padding: 0;<br>
margin: 0 auto;<br>
min-width: 268px;<br>
border-radius: 10px;<br>
}</p>
<p>.popup-container {<br>
font-size: 16px;<br>
--font-size: 16px;<br>
color: #666;<br>
background-color: var(--popup-footer-background-color);<br>
width: 316px;<br>
min-width: 316px;<br>
}</p>
<p>.popup-content {<br>
background-color: var(--popup-content-background-color);<br>
border-radius: 0px 0px 12px 12px;<br>
padding: 16px 20px;<br>
}</p>
<p>.immersive-translate-popup-overlay {<br>
position: fixed;<br>
top: 0;<br>
left: 0;<br>
height: 100%;<br>
width: 100%;<br>
touch-action: none;<br>
}</p>
<p>.immersive-translate-popup-wrapper {<br>
background: var(--background-color);<br>
border-radius: 10px;<br>
border: 1px solid var(--muted-border-color);<br>
}</p>
<p>#mount {<br>
--font-family: system-ui, -apple-system, &quot;Segoe UI&quot;, &quot;Roboto&quot;, &quot;Ubuntu&quot;,<br>
&quot;Cantarell&quot;, &quot;Noto Sans&quot;, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;,<br>
&quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;;<br>
--line-height: 1.5;<br>
--font-weight: 400;<br>
--font-size: 16px;<br>
--border-radius: 4px;<br>
--border-width: 1px;<br>
--outline-width: 3px;<br>
--spacing: 16px;<br>
--typography-spacing-vertical: 24px;<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
--block-spacing-horizontal: var(--spacing);<br>
--grid-spacing-vertical: 0;<br>
--grid-spacing-horizontal: var(--spacing);<br>
--form-element-spacing-vertical: 12px;<br>
--form-element-spacing-horizontal: 16px;<br>
--nav-element-spacing-vertical: 16px;<br>
--nav-element-spacing-horizontal: 8px;<br>
--nav-link-spacing-vertical: 8px;<br>
--nav-link-spacing-horizontal: 8px;<br>
--form-label-font-weight: var(--font-weight);<br>
--transition: 0.2s ease-in-out;<br>
--modal-overlay-backdrop-filter: blur(4px);<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--popup-footer-background-color: #e8eaeb;<br>
--popup-content-background-color: #ffffff;<br>
--popup-item-background-color: #f3f5f6;<br>
--popup-item-hover-background-color: #eaeced;<br>
--popup-trial-pro-background-color: #f9fbfc;<br>
--text-black-2: #222222;<br>
--text-gray-2: #222222;<br>
--text-gray-6: #666666;<br>
--text-gray-9: #999999;<br>
--text-gray-c2: #c2c2c2;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(75, 76, 77, 0.2);<br>
--service-select-border-color: #fafafa;<br>
--service-select-selected-background-color: #f3f5f6;<br>
--download-app-background: #f3f5f6;<br>
}</p>
<p>@media only screen and (prefers-color-scheme: dark) {<br>
#mount:not([data-theme=&quot;light&quot;]) {<br>
--popup-footer-background-color: #0d0d0d;<br>
--popup-content-background-color: #191919;<br>
--popup-item-background-color: #272727;<br>
--popup-item-hover-background-color: #333333;<br>
--popup-trial-pro-background-color: #222222;<br>
--text-black-2: #ffffff;<br>
--text-gray-2: #dbdbdb;<br>
--text-gray-6: #b3b3b3;<br>
--text-gray-9: #777777;<br>
--text-gray-c2: #5b5b5b;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);<br>
--service-select-border-color: #2c2c2c;<br>
--service-select-selected-background-color: #333333;<br>
--download-app-background: #333;<br>
}<br>
}</p>
<p>[data-theme=&quot;dark&quot;] {<br>
--popup-footer-background-color: #0d0d0d;<br>
--popup-content-background-color: #191919;<br>
--popup-item-background-color: #272727;<br>
--popup-item-hover-background-color: #333333;<br>
--popup-trial-pro-background-color: #222222;<br>
--text-black-2: #ffffff;<br>
--text-gray-2: #dbdbdb;<br>
--text-gray-6: #b3b3b3;<br>
--text-gray-9: #777777;<br>
--text-gray-c2: #5b5b5b;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);<br>
--service-select-border-color: #2c2c2c;<br>
--service-select-selected-background-color: #333333;<br>
--download-app-background: #333;<br>
}</p>
<p>.text-balck {<br>
color: var(--text-black-2);<br>
}</p>
<p>.text-gray-2 {<br>
color: var(--text-gray-2);<br>
}</p>
<p>.text-gray-6 {<br>
color: var(--text-gray-6);<br>
}</p>
<p>.text-gray-9 {<br>
color: var(--text-gray-9);<br>
}</p>
<p>.text-gray-c2 {<br>
color: var(--text-gray-c2);<br>
}</p>
<p>#mount {<br>
min-width: 268px;<br>
}</p>
<p>.main-button {<br>
font-size: 15px;<br>
vertical-align: middle;<br>
border-radius: 12px;<br>
padding: unset;<br>
height: 44px;<br>
line-height: 44px;<br>
}</p>
<p>.pt-4 {<br>
padding-top: 16px;<br>
}</p>
<p>.p-2 {<br>
padding: 8px;<br>
}</p>
<p>.pl-5 {<br>
padding-left: 48px;<br>
}</p>
<p>.p-0 {<br>
padding: 0;<br>
}</p>
<p>.pl-2 {<br>
padding-left: 8px;<br>
}</p>
<p>.pl-4 {<br>
padding-left: 24px;<br>
}</p>
<p>.pt-2 {<br>
padding-top: 8px;<br>
}</p>
<p>.pb-2 {<br>
padding-bottom: 8px;<br>
}</p>
<p>.pb-4 {<br>
padding-bottom: 16px;<br>
}</p>
<p>.pb-5 {<br>
padding-bottom: 20px;<br>
}</p>
<p>.pr-5 {<br>
padding-right: 48px;<br>
}</p>
<p>.text-sm {<br>
font-size: 13px;<br>
}</p>
<p>.text-base {<br>
font-size: 16px;<br>
}</p>
<p>.w-full {<br>
width: 100%;<br>
}</p>
<p>.flex {<br>
display: flex;<br>
}</p>
<p>.flex-row {<br>
flex-direction: row;<br>
}</p>
<p>.flex-wrap {<br>
flex-wrap: wrap;<br>
}</p>
<p>.flex-end {<br>
justify-content: flex-end;<br>
}</p>
<p>.flex-grow {<br>
flex-grow: 1;<br>
}</p>
<p>.justify-between {<br>
justify-content: space-between;<br>
}</p>
<p>.mb-0 {<br>
margin-bottom: 0px;<br>
}</p>
<p>.mb-2 {<br>
margin-bottom: 8px;<br>
}</p>
<p>.mb-4 {<br>
margin-bottom: 16px;<br>
}</p>
<p>.mb-3 {<br>
margin-bottom: 12px;<br>
}</p>
<p>.inline-block {<br>
display: inline-block;<br>
}</p>
<p>.py-2 {<br>
padding-top: 8px;<br>
padding-bottom: 8px;<br>
}</p>
<p>.py-2-5 {<br>
padding-top: 6px;<br>
padding-bottom: 6px;<br>
}</p>
<p>.mt-0 {<br>
margin-top: 0;<br>
}</p>
<p>.mt-2 {<br>
margin-top: 8px;<br>
}</p>
<p>.mt-3 {<br>
margin-top: 12px;<br>
}</p>
<p>.mt-4 {<br>
margin-top: 16px;<br>
}</p>
<p>.mt-5 {<br>
margin-top: 20px;<br>
}</p>
<p>.mt-6 {<br>
margin-top: 24px;<br>
}</p>
<p>.mb-1 {<br>
margin-bottom: 4px;<br>
}</p>
<p>.ml-4 {<br>
margin-left: 24px;<br>
}</p>
<p>.ml-3 {<br>
margin-left: 16px;<br>
}</p>
<p>.ml-2 {<br>
margin-left: 8px;<br>
}</p>
<p>.ml-1 {<br>
margin-left: 4px;<br>
}</p>
<p>.mr-1 {<br>
margin-right: 4px;<br>
}</p>
<p>.mr-2 {<br>
margin-right: 8px;<br>
}</p>
<p>.mr-3 {<br>
margin-right: 16px;<br>
}</p>
<p>.mx-2 {<br>
margin-left: 8px;<br>
margin-right: 8px;<br>
}</p>
<p>.pl-3 {<br>
padding-left: 12px;<br>
}</p>
<p>.pr-3 {<br>
padding-right: 12px;<br>
}</p>
<p>.p-3 {<br>
padding: 12px;<br>
}</p>
<p>.px-1 {<br>
padding-left: 4px;<br>
padding-right: 4px;<br>
}</p>
<p>.px-3 {<br>
padding-left: 12px;<br>
padding-right: 12px;<br>
}</p>
<p>.pt-3 {<br>
padding-top: 12px;<br>
}</p>
<p>.px-6 {<br>
padding-left: 18px;<br>
padding-right: 18px;<br>
}</p>
<p>.px-4 {<br>
padding-left: 16px;<br>
padding-right: 16px;<br>
}</p>
<p>.pt-6 {<br>
padding-top: 20px;<br>
}</p>
<p>.py-3 {<br>
padding-top: 12px;<br>
padding-bottom: 12px;<br>
}</p>
<p>.py-0 {<br>
padding-top: 0;<br>
padding-bottom: 0;<br>
}</p>
<p>.left-auto {<br>
left: auto !important;<br>
}</p>
<p>.max-h-28 {<br>
max-height: 112px;<br>
}</p>
<p>.max-h-30 {<br>
max-height: 120px;<br>
}</p>
<p>.overflow-y-scroll {<br>
overflow-y: scroll;<br>
}</p>
<p>.text-xs {<br>
font-size: 12px;<br>
}</p>
<p>.flex-1 {<br>
flex: 1;<br>
}</p>
<p>.flex-3 {<br>
flex: 3;<br>
}</p>
<p>.flex-4 {<br>
flex: 4;<br>
}</p>
<p>.flex-2 {<br>
flex: 2;<br>
}</p>
<p>.items-center {<br>
align-items: center;<br>
}</p>
<p>.max-content {<br>
width: max-content;<br>
}</p>
<p>.justify-center {<br>
justify-content: center;<br>
}</p>
<p>.items-end {<br>
align-items: flex-end;<br>
}</p>
<p>.items-baseline {<br>
align-items: baseline;<br>
}</p>
<p>.my-5 {<br>
margin-top: 48px;<br>
margin-bottom: 48px;<br>
}</p>
<p>.my-4 {<br>
margin-top: 24px;<br>
margin-bottom: 24px;<br>
}</p>
<p>.my-3 {<br>
margin-top: 16px;<br>
margin-bottom: 16px;<br>
}</p>
<p>.pt-3 {<br>
padding-top: 12px;<br>
}</p>
<p>.px-3 {<br>
padding-left: 12px;<br>
padding-right: 12px;<br>
}</p>
<p>.pt-2 {<br>
padding-top: 8px;<br>
}</p>
<p>.px-2 {<br>
padding-left: 8px;<br>
padding-right: 8px;<br>
}</p>
<p>.pt-1 {<br>
padding-top: 4px;<br>
}</p>
<p>.px-1 {<br>
padding-left: 4px;<br>
padding-right: 4px;<br>
}</p>
<p>.pb-2 {<br>
padding-bottom: 8px;<br>
}</p>
<p>.justify-end {<br>
justify-content: flex-end;<br>
}</p>
<p>.w-auto {<br>
width: auto;<br>
}</p>
<p>.shrink-0 {<br>
flex-shrink: 0;<br>
}</p>
<p>select.language-select,<br>
select.translate-service,<br>
select.min-select {<br>
--form-element-spacing-horizontal: 0;<br>
margin-bottom: 0px;<br>
max-width: unset;<br>
flex: 1;<br>
overflow: hidden;<br>
font-size: 13px;<br>
border: none;<br>
border-radius: 8px;<br>
padding-right: 30px;<br>
padding-left: 0px;<br>
background-position: center right 12px;<br>
background-size: 16px auto;<br>
background-image: var(--icon-xia);<br>
text-overflow: ellipsis;<br>
color: var(--text-gray-2);<br>
background-color: transparent;<br>
box-shadow: unset !important;<br>
cursor: pointer;<br>
}</p>
<p>select.more {<br>
background-position: center right;<br>
padding-right: 20px;<br>
}</p>
<p>select.transform-padding-left {<br>
padding-left: 12px;<br>
transform: translateX(-12px);<br>
background-position: center right 0px;<br>
}</p>
<p>select.translate-service {<br>
color: var(--text-black-2);<br>
}</p>
<p>.min-select-container.disabled {<br>
opacity: 0.5;<br>
pointer-events: none;<br>
}</p>
<p>/* dark use black, for windows */<br>
@media (prefers-color-scheme: dark) {<br>
select.language-select option,<br>
select.translate-service option,<br>
select.min-select option {<br>
background-color: #666666;<br>
}<br>
}</p>
<p>.text-overflow-ellipsis {<br>
text-overflow: ellipsis;<br>
overflow: hidden;<br>
white-space: nowrap;<br>
}</p>
<p>.max-w-20 {<br>
max-width: 180px;<br>
white-space: nowrap;<br>
}</p>
<p>select.min-select-secondary {<br>
color: var(--color);<br>
}</p>
<p>select.min-select:focus {<br>
outline: none;<br>
border: none;<br>
--box-shadow: none;<br>
}</p>
<p>select.min-select-no-arrow {<br>
background-image: none;<br>
padding-right: 0;<br>
}</p>
<p>select.min-select-left {<br>
padding-right: 0px;<br>
/* padding-left: 24px; <em>/<br>
/</em> background-position: center left 0; */<br>
text-overflow: ellipsis;<br>
text-align: left;<br>
}</p>
<p>.popup-footer {<br>
background-color: var(--popup-footer-background-color);<br>
height: 40px;<br>
}</p>
<p>.text-right {<br>
text-align: right;<br>
}</p>
<p>.clickable {<br>
cursor: pointer;<br>
}</p>
<p>.close {<br>
cursor: pointer;<br>
width: 16px;<br>
height: 16px;<br>
background-image: var(--icon-close);<br>
background-position: center;<br>
background-size: auto 1rem;<br>
background-repeat: no-repeat;<br>
opacity: 0.5;<br>
transition: opacity var(--transition);<br>
}</p>
<p>.padding-two-column {<br>
padding-left: 40px;<br>
padding-right: 40px;<br>
}</p>
<p>.muted {<br>
color: #999;<br>
}</p>
<p>.text-label {<br>
color: #666;<br>
}</p>
<p>.display-none {<br>
display: none;<br>
}</p>
<p>/* dark use #18232c */<br>
@media (prefers-color-scheme: dark) {<br>
.text-label {<br>
color: #9ca3af;<br>
}<br>
}</p>
<p>.text-decoration-none {<br>
text-decoration: none;<br>
}</p>
<p>.text-decoration-none:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--text-decoration: none !important;<br>
background-color: transparent !important;<br>
}</p>
<p>.language-select-container {<br>
position: relative;<br>
width: 100%;<br>
background-color: var(--popup-item-background-color);<br>
height: 55px;<br>
border-radius: 12px;<br>
}</p>
<p>select.language-select {<br>
color: var(--text-black-2);<br>
font-size: 14px;<br>
padding: 8px 24px 24px 16px;<br>
position: absolute;<br>
border-radius: 12px;<br>
position: absolute;<br>
left: 0;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
}</p>
<p>select.text-gray-6 {<br>
color: var(--text-gray-6);<br>
}</p>
<p>.language-select-container label {<br>
position: absolute;<br>
bottom: 10px;<br>
left: 16px;<br>
font-size: 12px;<br>
color: var(--text-gray-9);<br>
line-height: 12px;<br>
margin: 0;<br>
}</p>
<p>.translation-service-container {<br>
background-color: var(--popup-item-background-color);<br>
border-radius: 12px;<br>
}</p>
<p>.min-select-container {<br>
display: flex;<br>
justify-content: space-between;<br>
align-items: center;<br>
height: 44px;<br>
background-color: var(--popup-item-background-color);<br>
padding-left: 16px;<br>
}</p>
<p>.min-select-container:first-child {<br>
border-top-left-radius: 10px;<br>
border-top-right-radius: 10px;<br>
}</p>
<p>.min-select-container:last-child {<br>
border-bottom-left-radius: 10px;<br>
border-bottom-right-radius: 10px;<br>
}</p>
<p>.min-select-container:only-child {<br>
border-radius: 10px;<br>
}</p>
<p>.translate-mode {<br>
width: 44px;<br>
height: 44px;<br>
border-radius: 22px;<br>
background-color: var(--popup-item-background-color);<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
flex-shrink: 0;<br>
cursor: pointer;<br>
}</p>
<p>.translate-mode svg {<br>
fill: var(--text-gray-2);<br>
}</p>
<p>.widgets-container {<br>
display: flex;<br>
align-items: stretch;<br>
justify-content: space-between;<br>
width: 100%;<br>
gap: 9px;<br>
}</p>
<p>/* 当只有两个小组件时的样式优化 */<br>
.widgets-container.widgets-two-items {<br>
gap: 16px;<br>
}</p>
<p>.widgets-container.widgets-two-items .widget-item {<br>
flex: 0 1 auto;<br>
min-width: 93px;<br>
max-width: 120px;<br>
}</p>
<p>.widget-item {<br>
display: flex;<br>
max-width: 93px;<br>
flex-direction: row;<br>
align-items: center;<br>
justify-content: center;<br>
background-color: var(--popup-item-background-color);<br>
font-size: 12px;<br>
min-height: 44px;<br>
height: 100%;<br>
border-radius: 8px;<br>
cursor: pointer;<br>
flex: 1;<br>
padding: 8px 4px;<br>
text-align: center;<br>
}</p>
<p>.widget-icon-text {<br>
white-space: nowrap;<br>
overflow: hidden;<br>
text-overflow: ellipsis;<br>
color: var(--text-gray-2);<br>
}</p>
<p>.widgets-container svg {<br>
fill: var(--text-gray-2);<br>
color: var(--text-gray-2);<br>
}</p>
<p>.share-button-container {<br>
display: flex;<br>
align-items: center;<br>
cursor: pointer;<br>
padding: 2px 3px 0 8px;<br>
}</p>
<p>.share-button-container svg {<br>
fill: var(--text-gray-9);<br>
}</p>
<p>.min-select-container:hover,<br>
.language-select-container:hover,<br>
.widget-item:hover,<br>
.translate-mode:hover {<br>
background-color: var(--popup-item-hover-background-color);<br>
}</p>
<p>.main-button:hover {<br>
background-color: #f5508f;<br>
}</p>
<p>.share-button-container:hover {<br>
background-color: var(--popup-item-background-color);<br>
border-radius: 6px;<br>
}</p>
<p>.error-boundary {<br>
background: #fff2f0;<br>
border: 1px solid #ffccc7;<br>
display: flex;<br>
padding: 12px;<br>
font-size: 14px;<br>
color: rgba(0, 0, 0, 0.88);<br>
word-break: break-all;<br>
margin: 12px;<br>
border-radius: 12px;<br>
flex-direction: column;<br>
}</p>
<p>.upgrade-pro {<br>
border-radius: 11px;<br>
background: linear-gradient(57deg, #272727 19.8%, #696969 82.2%);<br>
padding: 2px 8px;<br>
transform: scale(0.85);<br>
}</p>
<p>.upgrade-pro span {<br>
background: linear-gradient(180deg, #ffeab4 17.65%, #f8c235 85.29%);<br>
background-clip: text;<br>
-webkit-background-clip: text;<br>
-webkit-text-fill-color: transparent;<br>
font-size: 12px;<br>
margin-left: 4px;<br>
}</p>
<p>.upgrade-pro svg {<br>
margin-top: -2px;<br>
}</p>
<p>.upgrade-pro:hover {<br>
background: linear-gradient(57deg, #3d3d3d 19.8%, #949494 82.2%);<br>
}</p>
<p>.border-bottom-radius-0 {<br>
border-bottom-left-radius: 0 !important;<br>
border-bottom-right-radius: 0 !important;<br>
}</p>
<p>.trial-pro-container {<br>
border-radius: 0px 0px 12px 12px;<br>
background: var(--popup-trial-pro-background-color);<br>
display: flex;<br>
align-items: center;<br>
height: 44px;<br>
padding-left: 16px;<br>
padding-right: 12px;<br>
font-size: 12px;<br>
}</p>
<p>.trial-pro-container label {<br>
line-height: 13px;<br>
color: var(--text-black-2);<br>
}</p>
<p>.trial-pro-container img {<br>
margin-left: 5px;<br>
}</p>
<p>.cursor-pointer {<br>
cursor: pointer;<br>
}</p>
<p>.upgrade-pro-discount-act {<br>
height: 25px;<br>
display: flex;<br>
padding: 0 4px;<br>
align-items: center;<br>
border-radius: 15px;<br>
background: linear-gradient(<br>
90deg,<br>
#cefbfa 11.33%,<br>
#d7f56f 63.75%,<br>
#fccd5e 100%<br>
);<br>
transform: scale(0.9);<br>
box-shadow: 0px 1.8px 3.6px 0px rgba(0, 0, 0, 0.1);<br>
cursor: pointer;<br>
}</p>
<p>.upgrade-pro-discount-act span {<br>
font-size: 12px;<br>
font-weight: 700;<br>
margin-left: 4px;<br>
color: #222222;<br>
}</p>
<p>.upgrade-pro-discount-act:hover {<br>
text-decoration: unset;<br>
background: linear-gradient(<br>
90deg,<br>
#e2fffe 11.33%,<br>
#e6ff91 63.75%,<br>
#ffdf93 100%<br>
);<br>
}</p>
<p>.custom-select-container {<br>
width: 200px;<br>
position: relative;<br>
flex: 1;<br>
}</p>
<p>#translation-service-select {<br>
padding-right: 12px;<br>
padding-left: 6px;<br>
}</p>
<p>.custom-select-content {<br>
border-radius: 12px;<br>
background: var(--popup-content-background-color);<br>
box-shadow: var(--service-select-content-shadow);<br>
border: 1px solid var(--service-select-border-color);<br>
padding: 4px 5px;<br>
position: absolute;<br>
left: -10px;<br>
right: 0;<br>
z-index: 100;<br>
overflow-y: auto;<br>
}</p>
<p>.custom-select-item.default {<br>
width: 100%;<br>
padding: 0;<br>
}</p>
<p>.custom-select-item {<br>
font-size: 13px;<br>
padding: 5px 6px;<br>
border-radius: 8px;<br>
display: flex;<br>
align-items: center;<br>
cursor: pointer;<br>
color: var(--text-black-2);<br>
width: auto;<br>
overflow: hidden;<br>
height: 30px;<br>
line-height: 30px;<br>
}</p>
<p>.custom-select-item-img {<br>
width: 20px;<br>
height: 20px;<br>
margin-right: 4px;<br>
}</p>
<p>@media (prefers-color-scheme: dark) {<br>
.custom-select-item-img {<br>
margin-right: 6px;<br>
}<br>
}</p>
<p>.custom-select-content .custom-select-item.selected,<br>
.custom-select-content .custom-select-item:hover {<br>
background: var(--service-select-selected-background-color);<br>
}</p>
<p>.custom-select-item &gt; span {<br>
white-space: nowrap;<br>
overflow: hidden;<br>
text-overflow: ellipsis;<br>
}</p>
<p>.custom-select-item-pro {<br>
font-size: 12px;<br>
margin-left: 6px;<br>
display: flex;<br>
}</p>
<p>.custom-select-item-pro img {<br>
margin: 0 3px;<br>
width: 20px;<br>
flex-shrink: 0;<br>
}</p>
<p>.custom-select-group-header {<br>
font-size: 12px;<br>
font-weight: 500;<br>
color: var(--text-gray-9);<br>
padding: 6px 8px 4px;<br>
margin-top: 2px;<br>
text-transform: uppercase;<br>
letter-spacing: 0.5px;<br>
}</p>
<p>.more-container {<br>
position: relative;<br>
}</p>
<p>.new-menu-indicator {<br>
position: absolute;<br>
width: 8px;<br>
height: 8px;<br>
background-color: #ef3434;<br>
border-radius: 50%;<br>
right: 18px;<br>
top: 4px;<br>
}</p>
<p>.download-app {<br>
display: inline-flex;<br>
align-items: center;<br>
gap: 4px;<br>
border-radius: 8px;<br>
background: var(--download-app-background);<br>
padding: 4px 8px;<br>
color: var(--text-gray-6);<br>
font-size: 12px;<br>
cursor: pointer;<br>
transition: all 0.2s ease-in-out;<br>
}</p>
<p>/* Popup 动画效果 */<br>
@keyframes popup-fade-in {<br>
from {<br>
opacity: 0;<br>
transform: translateY(10px) scale(0.95);<br>
}<br>
to {<br>
opacity: 1;<br>
transform: translateY(0) scale(1);<br>
}<br>
}</p>
<p>@keyframes popup-fade-out {<br>
from {<br>
opacity: 1;<br>
transform: translateY(0) scale(1);<br>
}<br>
to {<br>
opacity: 0;<br>
transform: translateY(10px) scale(0.95);<br>
}<br>
}</p>
<p>.popup-generic-content {<br>
animation: popup-fade-in 0.2s ease-out;<br>
}</p>
<p>.popup-generic-content.hiding {<br>
animation: popup-fade-out 0.15s ease-in;<br>
}</p>
<p>html {<br>
font-size: 17px;<br>
}</p>
<p>@media print {<br>
.imt-fb-container {<br>
display: none !important;<br>
}<br>
}</p>
<p>#mount#mount {<br>
position: absolute;<br>
display: none;<br>
min-width: 250px;<br>
height: auto;<br>
--font-size: 17px;<br>
font-size: 17px;<br>
}</p>
<p>/* float-ball */<br>
.imt-fb-container {<br>
position: fixed;<br>
padding: 0;<br>
top: 335px;<br>
width: fit-content;<br>
display: flex;<br>
flex-direction: column;<br>
display: none;<br>
direction: ltr;<br>
}</p>
<p>.imt-fb-container.left {<br>
align-items: flex-start;<br>
left: 0;<br>
}</p>
<p>.imt-fb-container.right {<br>
align-items: flex-end;<br>
right: 0;<br>
}</p>
<p>.imt-fb-btn {<br>
cursor: pointer;<br>
background: var(--float-ball-more-button-background-color);<br>
height: 36px;<br>
width: 56px;<br>
box-shadow: 2px 6px 10px 0px #0e121629;<br>
}</p>
<p>.imt-fb-btn.left {<br>
border-top-right-radius: 36px;<br>
border-bottom-right-radius: 36px;<br>
}</p>
<p>.imt-fb-btn.right {<br>
border-top-left-radius: 36px;<br>
border-bottom-left-radius: 36px;<br>
}</p>
<p>.imt-fb-btn div {<br>
background: var(--float-ball-more-button-background-color);<br>
height: 36px;<br>
width: 54px;<br>
display: flex;<br>
align-items: center;<br>
}</p>
<p>.imt-fb-btn.left div {<br>
border-top-right-radius: 34px;<br>
border-bottom-right-radius: 34px;<br>
justify-content: flex-end;<br>
}</p>
<p>.imt-fb-btn.right div {<br>
border-top-left-radius: 34px;<br>
border-bottom-left-radius: 34px;<br>
}</p>
<p>.imt-fb-logo-img {<br>
width: 20px;<br>
height: 20px;<br>
margin: 0 10px;<br>
}</p>
<p>.imt-fb-logo-img-big-bg {<br>
width: 28px;<br>
height: 28px;<br>
margin: 0;<br>
padding: 4px;<br>
background-color: #ed6d8f;<br>
border-radius: 50%;<br>
margin: 0 5px;<br>
}</p>
<p>.imt-float-ball-translated {<br>
position: absolute;<br>
width: 11px;<br>
height: 11px;<br>
bottom: 4px;<br>
right: 20px;<br>
}</p>
<p>.btn-animate {<br>
-webkit-transform: translate3d(0, 0, 0);<br>
transform: translate3d(0, 0, 0);<br>
-webkit-transition: -webkit-transform ease-out 250ms;<br>
transition: -webkit-transform ease-out 250ms;<br>
transition: transform ease-out 250ms;<br>
transition: transform ease-out 250ms, -webkit-transform ease-out 250ms;<br>
}</p>
<p>.imt-fb-setting-btn {<br>
margin-right: 18px;<br>
width: 28px;<br>
height: 28px;<br>
}</p>
<p>.immersive-translate-popup-wrapper {<br>
background: var(--background-color);<br>
border-radius: 20px;<br>
box-shadow: 2px 10px 24px 0px #0e121614;<br>
border: none;<br>
}</p>
<p>.popup-container {<br>
border-radius: 20px;<br>
}</p>
<p>.popup-content {<br>
border-radius: 20px 20px 12px 12px;<br>
}<br>
.popup-footer {<br>
border-radius: 20px;<br>
}</p>
<p>.imt-fb-close-button {<br>
pointer-events: all;<br>
cursor: pointer;<br>
position: absolute;<br>
margin-top: -10px;<br>
}</p>
<p>.imt-fb-close-content {<br>
padding: 22px;<br>
width: 320px;<br>
pointer-events: all;<br>
}</p>
<p>.imt-fb-close-title {<br>
font-weight: 500;<br>
color: var(--h2-color);<br>
}</p>
<p>.imt-fb-close-radio-content {<br>
background-color: var(--background-light-green);<br>
padding: 8px 20px;<br>
}</p>
<p>.imt-fb-radio-sel,<br>
.imt-fb-radio-nor {<br>
width: 16px;<br>
height: 16px;<br>
border-radius: 8px;<br>
flex-shrink: 0;<br>
}</p>
<p>.imt-fb-radio-sel {<br>
border: 2px solid var(--primary);<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
}</p>
<p>.imt-fb-radio-sel div {<br>
width: 8px;<br>
height: 8px;<br>
border-radius: 4px;<br>
background-color: var(--primary);<br>
}</p>
<p>.imt-fb-radio-nor {<br>
border: 2px solid #d3d4d6;<br>
}</p>
<p>.imt-fb-primary-btn {<br>
background-color: var(--primary);<br>
width: 72px;<br>
height: 32px;<br>
color: white;<br>
border-radius: 8px;<br>
text-align: center;<br>
line-height: 32px;<br>
font-size: 16px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-default-btn {<br>
border: 1px solid var(--primary);<br>
width: 72px;<br>
height: 32px;<br>
border-radius: 8px;<br>
color: var(--primary);<br>
line-height: 32px;<br>
text-align: center;<br>
font-size: 16px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-guide-container {<br>
width: 312px;<br>
transform: translateY(-45%);<br>
}</p>
<p>.imt-fb-guide-bg {<br>
position: absolute;<br>
left: 30px;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
z-index: -1;<br>
height: 100%;<br>
width: 90%;<br>
}</p>
<p>.imt-fb-guide-bg.left {<br>
transform: scaleX(-1);<br>
}</p>
<p>.imt-fb-guide-content {<br>
margin: 16px -30px 80px 0px;<br>
display: flex;<br>
flex-direction: column;<br>
align-items: center;<br>
}</p>
<p>.imt-fb-guide-content.left {<br>
margin: 16px 21px 60px 32px;<br>
}</p>
<p>.imt-fb-guide-img {<br>
width: 220px;<br>
height: 112px;<br>
}</p>
<p>.imt-fb-guide-message {<br>
font-size: 14px;<br>
line-height: 28px;<br>
color: #333333;<br>
white-space: pre-wrap;<br>
text-align: center;<br>
font-weight: 700;<br>
margin-bottom: 20px;<br>
}</p>
<p>.imt-manga-guide-message {<br>
font-size: 16px;<br>
line-height: 24px;<br>
color: #333333;<br>
text-align: center;<br>
font-weight: 500;<br>
margin-bottom: 12px;<br>
}</p>
<p>.imt-fb-guide-button {<br>
margin-top: 16px;<br>
line-height: 40px;<br>
height: 40px;<br>
padding: 0 20px;<br>
width: unset;<br>
}</p>
<p>.imt-fb-more-buttons {<br>
box-shadow: 0px 2px 10px 0px #00000014;<br>
border: none;<br>
background: var(--float-ball-more-button-background-color);<br>
width: 36px;<br>
display: flex;<br>
flex-direction: column;<br>
border-radius: 18px;<br>
margin-top: 0px;<br>
padding: 7px 0 7px 0;<br>
}</p>
<p>.imt-fb-more-buttons &gt; div {<br>
margin: auto;<br>
}</p>
<p>.imt-fb-side,<br>
.imt-fb-reward {<br>
border-radius: 50%;<br>
cursor: pointer;<br>
pointer-events: all;<br>
position: relative;<br>
}</p>
<p>.imt-fb-side {<br>
margin: 10px 0;<br>
}</p>
<p>.imt-fb-new-badge {<br>
width: 26px;<br>
height: 14px;<br>
padding: 3px;<br>
background-color: #f53f3f;<br>
border-radius: 4px;<br>
position: absolute;<br>
top: -5px;<br>
right: 15px;<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
}</p>
<p>.imt-fb-side *,<br>
.imt-fb-reward * {<br>
pointer-events: all;<br>
}</p>
<p>.imt-fb-more-button {<br>
width: 36px;<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
cursor: pointer;<br>
}<br>
/* Sheet.css <em>/<br>
.immersive-translate-sheet {<br>
position: fixed;<br>
transform: translateY(100%);<br>
/</em> Start off screen <em>/<br>
left: 0;<br>
right: 0;<br>
background-color: white;<br>
transition: transform 0.3s ease-out;<br>
/</em> Smooth slide transition <em>/<br>
box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);<br>
/</em> Ensure it's above other content */<br>
bottom: 0;<br>
border-top-left-radius: 16px;<br>
border-top-right-radius: 16px;<br>
overflow: hidden;<br>
}</p>
<p>.immersive-translate-sheet.visible {<br>
transform: translateY(0);<br>
}</p>
<p>.immersive-translate-sheet-backdrop {<br>
position: fixed;<br>
top: 0;<br>
left: 0;<br>
right: 0;<br>
bottom: 0;<br>
background-color: rgba(0, 0, 0, 0.5);<br>
opacity: 0;<br>
transition: opacity 0.3s ease-out;<br>
}</p>
<p>.immersive-translate-sheet-backdrop.visible {<br>
opacity: 1;<br>
}</p>
<p>.popup-container-sheet {<br>
max-width: 100vw;<br>
width: 100vw;<br>
}</p>
<p>.imt-no-events svg * {<br>
pointer-events: none !important;<br>
}</p>
<p>.imt-manga-button {<br>
width: 36px;<br>
display: flex;<br>
flex-direction: column;<br>
position: relative;<br>
align-items: center;<br>
justify-content: center;<br>
cursor: pointer;<br>
pointer-events: all;<br>
margin: 0 0 10px 0;<br>
background-color: var(--float-ball-more-button-background-color);<br>
border-radius: 18px;<br>
filter: drop-shadow(0px 2px 10px rgba(0, 0, 0, 0.08));<br>
opacity: 0.5;<br>
right: 8px;<br>
padding: 10px 0 4px 0;<br>
}</p>
<p>.imt-manga-feedback {<br>
cursor: pointer;<br>
margin-bottom: 10px;<br>
}</p>
<p>.imt-fb-feedback {<br>
cursor: pointer;<br>
margin-top: 10px;<br>
}</p>
<p>.imt-fb-upgrade-button {<br>
cursor: pointer;<br>
margin-top: 10px;<br>
}</p>
<p>.imt-manga-button:hover {<br>
opacity: 1;<br>
}</p>
<p>.imt-manga-translated {<br>
position: absolute;<br>
left: 24px;<br>
top: 20px;<br>
}</p>
<p>.imt-float-ball-loading {<br>
animation: imt-loading-animation 0.6s infinite linear !important;<br>
}</p>
<p>.imt-manga-guide-bg {<br>
position: absolute;<br>
left: 0;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
z-index: -1;<br>
width: 372px;<br>
transform: translateY(-50%);<br>
}<br>
.imt-manga-guide-content {<br>
position: absolute;<br>
top: 15px;<br>
left: 0;<br>
right: 0;<br>
margin: 0 40px 0;<br>
}</p>
<p>.img-manga-guide-button {<br>
width: fit-content;<br>
margin: 0 auto;<br>
}</p>
<p>.img-manga-close {<br>
position: absolute;<br>
bottom: -200px;<br>
width: 32px;<br>
height: 32px;<br>
left: 0;<br>
right: 0;<br>
margin: auto;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-more-buttons,<br>
.imt-fb-container.dragging .imt-manga-button,<br>
.imt-fb-container.dragging .btn-animate:not(.imt-fb-btn) {<br>
display: none !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn {<br>
border-radius: 50% !important;<br>
width: 36px !important;<br>
height: 36px !important;<br>
display: flex !important;<br>
align-items: center !important;<br>
justify-content: center !important;<br>
cursor: move !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn div {<br>
border-radius: 50% !important;<br>
width: 36px !important;<br>
height: 36px !important;<br>
display: flex !important;<br>
align-items: center !important;<br>
justify-content: center !important;<br>
margin: 0 !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn.left,<br>
.imt-fb-container.dragging .imt-fb-btn.right {<br>
border-radius: 50% !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn.left div,<br>
.imt-fb-container.dragging .imt-fb-btn.right div {<br>
border-radius: 50% !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-logo-img {<br>
margin: 0 !important;<br>
padding: 4px !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-float-ball-translated {<br>
right: 2px !important;<br>
bottom: 2px !important;<br>
}</p>
<p>@-webkit-keyframes imt-loading-animation {<br>
from {<br>
-webkit-transform: rotate(0deg);<br>
}</p>
<p>to {<br>
-webkit-transform: rotate(359deg);<br>
}<br>
}</p>
<p>@keyframes imt-loading-animation {<br>
from {<br>
transform: rotate(0deg);<br>
}</p>
<p>to {<br>
transform: rotate(359deg);<br>
}<br>
}</p>
<p>.imt-fb-icon {<br>
color: #666666;<br>
}</p>
<p>[data-theme=&quot;dark&quot;] .imt-fb-icon {<br>
color: #B3B3B3;<br>
}</p>
<p>[data-theme=&quot;light&quot;] .imt-fb-icon {<br>
color: #666666;<br>
}</p>
</style><div id="mount" style="display: block;"><div hidden="" id="immersive-translate-popup-overlay" class="immersive-translate-popup-overlay" style="z-index: 2147483647; background-color: rgba(0, 0, 0, 0.5);"><div class="immersive-translate-popup-wrapper" style="position: fixed; top: 50%; left: 50%; transform: translateX(-50%) translateY(-50%);"></div></div></div></template></div></body><div id="immersive-translate-popup" style="all: initial"><template shadowrootmode="open"><style>@charset "UTF-8";
/*!
 * Pico.css v1.5.6 (https://picocss.com)
 * Copyright 2019-2022 - Licensed under MIT
 */
/**
 * Theme: default
 */
#mount {
  --font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --line-height: 1.5;
  --font-weight: 400;
  --font-size: 16px;
  --border-radius: 0.25rem;
  --border-width: 1px;
  --outline-width: 3px;
  --spacing: 1rem;
  --typography-spacing-vertical: 1.5rem;
  --block-spacing-vertical: calc(var(--spacing) * 2);
  --block-spacing-horizontal: var(--spacing);
  --grid-spacing-vertical: 0;
  --grid-spacing-horizontal: var(--spacing);
  --form-element-spacing-vertical: 0.75rem;
  --form-element-spacing-horizontal: 1rem;
  --nav-element-spacing-vertical: 1rem;
  --nav-element-spacing-horizontal: 0.5rem;
  --nav-link-spacing-vertical: 0.5rem;
  --nav-link-spacing-horizontal: 0.5rem;
  --form-label-font-weight: var(--font-weight);
  --transition: 0.2s ease-in-out;
  --modal-overlay-backdrop-filter: blur(0.25rem);
}
@media (min-width: 576px) {
  #mount {
    --font-size: 17px;
  }
}
@media (min-width: 768px) {
  #mount {
    --font-size: 18px;
  }
}
@media (min-width: 992px) {
  #mount {
    --font-size: 19px;
  }
}
@media (min-width: 1200px) {
  #mount {
    --font-size: 20px;
  }
}
<p>@media (min-width: 576px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 2.5);<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 3);<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer,<br>
section {<br>
--block-spacing-vertical: calc(var(--spacing) * 3.5);<br>
}<br>
}</p>
<p>@media (min-width: 576px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.25);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.5);<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.75);<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
article {<br>
--block-spacing-horizontal: calc(var(--spacing) * 2);<br>
}<br>
}</p>
<p>dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
--block-spacing-horizontal: var(--spacing);<br>
}<br>
@media (min-width: 576px) {<br>
dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 2.5);<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.25);<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
dialog &gt; article {<br>
--block-spacing-vertical: calc(var(--spacing) * 3);<br>
--block-spacing-horizontal: calc(var(--spacing) * 1.5);<br>
}<br>
}</p>
<p>a {<br>
--text-decoration: none;<br>
}<br>
a.secondary,<br>
a.contrast {<br>
--text-decoration: underline;<br>
}</p>
<p>small {<br>
--font-size: 0.875em;<br>
}</p>
<p>h1,<br>
h2,<br>
h3,<br>
h4,<br>
h5,<br>
h6 {<br>
--font-weight: 700;<br>
}</p>
<p>h1 {<br>
--font-size: 2rem;<br>
--typography-spacing-vertical: 3rem;<br>
}</p>
<p>h2 {<br>
--font-size: 1.75rem;<br>
--typography-spacing-vertical: 2.625rem;<br>
}</p>
<p>h3 {<br>
--font-size: 1.5rem;<br>
--typography-spacing-vertical: 2.25rem;<br>
}</p>
<p>h4 {<br>
--font-size: 1.25rem;<br>
--typography-spacing-vertical: 1.874rem;<br>
}</p>
<p>h5 {<br>
--font-size: 1.125rem;<br>
--typography-spacing-vertical: 1.6875rem;<br>
}</p>
<p>[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
--border-width: 2px;<br>
}</p>
<p>[type=&quot;checkbox&quot;][role=&quot;switch&quot;] {<br>
--border-width: 2px;<br>
}</p>
<p>thead th,<br>
thead td,<br>
tfoot th,<br>
tfoot td {<br>
--border-width: 3px;<br>
}</p>
<p>:not(thead, tfoot) &gt; * &gt; td {<br>
--font-size: 0.875em;<br>
}</p>
<p>pre,<br>
code,<br>
kbd,<br>
samp {<br>
--font-family: &quot;Menlo&quot;, &quot;Consolas&quot;, &quot;Roboto Mono&quot;, &quot;Ubuntu Monospace&quot;,<br>
&quot;Noto Mono&quot;, &quot;Oxygen Mono&quot;, &quot;Liberation Mono&quot;, monospace,<br>
&quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;;<br>
}</p>
<p>kbd {<br>
--font-weight: bolder;<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--background-color: #fff;<br>
--background-light-green: #f5f7f9;<br>
--color: hsl(205deg, 20%, 32%);<br>
--h1-color: hsl(205deg, 30%, 15%);<br>
--h2-color: #24333e;<br>
--h3-color: hsl(205deg, 25%, 23%);<br>
--h4-color: #374956;<br>
--h5-color: hsl(205deg, 20%, 32%);<br>
--h6-color: #4d606d;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: hsl(205deg, 20%, 94%);<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 90%, 32%);<br>
--primary-focus: rgba(16, 149, 193, 0.125);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 20%, 32%);<br>
--secondary-focus: rgba(89, 107, 120, 0.125);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 30%, 15%);<br>
--contrast-hover: #000;<br>
--contrast-focus: rgba(89, 107, 120, 0.125);<br>
--contrast-inverse: #fff;<br>
--mark-background-color: #fff2ca;<br>
--mark-color: #543a26;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: transparent;<br>
--form-element-border-color: hsl(205deg, 14%, 68%);<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: transparent;<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 18%, 86%);<br>
--form-element-disabled-border-color: hsl(205deg, 14%, 68%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #c62828;<br>
--form-element-invalid-active-border-color: #d32f2f;<br>
--form-element-invalid-focus-color: rgba(211, 47, 47, 0.125);<br>
--form-element-valid-border-color: #388e3c;<br>
--form-element-valid-active-border-color: #43a047;<br>
--form-element-valid-focus-color: rgba(67, 160, 71, 0.125);<br>
--switch-background-color: hsl(205deg, 16%, 77%);<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: hsl(205deg, 18%, 86%);<br>
--range-active-border-color: hsl(205deg, 16%, 77%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: #f6f8f9;<br>
--code-background-color: hsl(205deg, 20%, 94%);<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 40%, 50%);<br>
--code-property-color: hsl(185deg, 40%, 40%);<br>
--code-value-color: hsl(40deg, 20%, 50%);<br>
--code-comment-color: hsl(205deg, 14%, 68%);<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: var(--background-color);<br>
--card-border-color: var(--muted-border-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(27, 40, 50, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(27, 40, 50, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(27, 40, 50, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(27, 40, 50, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(27, 40, 50, 0.04302),<br>
0.5rem 1rem 6rem rgba(27, 40, 50, 0.06),<br>
0 0 0 0.0625rem rgba(27, 40, 50, 0.015);<br>
--card-sectionning-background-color: #fbfbfc;<br>
--dropdown-background-color: #fbfbfc;<br>
--dropdown-border-color: #e1e6eb;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: hsl(205deg, 20%, 94%);<br>
--modal-overlay-background-color: rgba(213, 220, 226, 0.7);<br>
--progress-background-color: hsl(205deg, 18%, 86%);<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(198, 40, 40)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(56, 142, 60)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjQnIGhlaWdodD0nMjQnIHZpZXdCb3g9JzAgMCAyNCAyNCcgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTguOTM0OCA4LjY0ODQ0QzIwLjg5NDEgOC42NDg0NCAyMi40ODU1IDcuMDU0NjkgMjIuNDg1NSA1LjA5NzY2QzIyLjQ4NTUgMy4xNDA2MiAyMC44OTE4IDEuNTQ2ODggMTguOTM0OCAxLjU0Njg4QzE2Ljk3NTQgMS41NDY4OCAxNS4zODQgMy4xNDA2MiAxNS4zODQgNS4wOTc2NkMxNS4zODQgNS4yOTkyMiAxNS40MDA0IDUuNDkzNzUgMTUuNDMzMiA1LjY4NTk0TDcuMzIzODMgOS4zNTM5MUM2LjcwOTc3IDguODQ1MzEgNS45MjIyNyA4LjU0MDYyIDUuMDY0NDUgOC41NDA2MkMzLjEwNTA4IDguNTQwNjIgMS41MTM2NyAxMC4xMzQ0IDEuNTEzNjcgMTIuMDkxNEMxLjUxMzY3IDE0LjA0ODQgMy4xMDc0MiAxNS42NDIyIDUuMDY0NDUgMTUuNjQyMkM1LjgzMzIgMTUuNjQyMiA2LjU0NTcgMTUuMzk2MSA3LjEyNjk1IDE0Ljk4MTNMMTIuNDk0MSAxNy45OTUzQzEyLjQxNjggMTguMjg1OSAxMi4zNzcgMTguNTg4MyAxMi4zNzcgMTguOTAyM0MxMi4zNzcgMjAuODYxNyAxMy45NzA3IDIyLjQ1MzEgMTUuOTI3NyAyMi40NTMxQzE3Ljg4NzEgMjIuNDUzMSAxOS40Nzg1IDIwLjg1OTQgMTkuNDc4NSAxOC45MDIzQzE5LjQ3ODUgMTYuOTQzIDE3Ljg4NDggMTUuMzUxNiAxNS45Mjc3IDE1LjM1MTZDMTQuOTU3NCAxNS4zNTE2IDE0LjA3ODUgMTUuNzQzIDEzLjQzNjMgMTYuMzczNEw4LjMyMjI3IDEzLjUwNDdDOC41MDk3NyAxMy4wNzExIDguNjE1MjMgMTIuNTk1MyA4LjYxNTIzIDEyLjA5MzhDOC42MTUyMyAxMS42ODEyIDguNTQ0OTIgMTEuMjg3NSA4LjQxNjAyIDEwLjkxOTVMMTYuMjIzIDcuMzg3NUMxNi44NzQ2IDguMTU2MjUgMTcuODQ5NiA4LjY0ODQ0IDE4LjkzNDggOC42NDg0NFpNNS4wNjQ0NSAxMy43Njk1QzQuMTQxMDIgMTMuNzY5NSAzLjM4ODY3IDEzLjAxNzIgMy4zODg2NyAxMi4wOTM4QzMuMzg4NjcgMTEuMTcwMyA0LjE0MTAyIDEwLjQxOCA1LjA2NDQ1IDEwLjQxOEM1Ljk4Nzg5IDEwLjQxOCA2Ljc0MDIzIDExLjE3MDMgNi43NDAyMyAxMi4wOTM4QzYuNzQwMjMgMTMuMDE3MiA1Ljk4Nzg5IDEzLjc2OTUgNS4wNjQ0NSAxMy43Njk1Wk0xNS45Mjc3IDE3LjIyNjZDMTYuODUxMiAxNy4yMjY2IDE3LjYwMzUgMTcuOTc4OSAxNy42MDM1IDE4LjkwMjNDMTcuNjAzNSAxOS44MjU4IDE2Ljg1MTIgMjAuNTc4MSAxNS45Mjc3IDIwLjU3ODFDMTUuMDA0MyAyMC41NzgxIDE0LjI1MiAxOS44MjU4IDE0LjI1MiAxOC45MDIzQzE0LjI1MiAxNy45Nzg5IDE1LjAwMiAxNy4yMjY2IDE1LjkyNzcgMTcuMjI2NlpNMTguOTM0OCAzLjQxOTUzQzE5Ljg1ODIgMy40MTk1MyAyMC42MTA1IDQuMTcxODcgMjAuNjEwNSA1LjA5NTMxQzIwLjYxMDUgNi4wMTg3NSAxOS44NTgyIDYuNzcxMDkgMTguOTM0OCA2Ljc3MTA5QzE4LjAxMTMgNi43NzEwOSAxNy4yNTkgNi4wMTg3NSAxNy4yNTkgNS4wOTUzMUMxNy4yNTkgNC4xNzE4NyAxOC4wMTEzIDMuNDE5NTMgMTguOTM0OCAzLjQxOTUzWicgZmlsbD0nIzgzODM4MycvPjwvc3ZnPiA=&quot;);<br>
--float-ball-more-button-border-color: #f6f6f6;<br>
--float-ball-more-button-background-color: #ffffff;<br>
--float-ball-more-button-svg-color: #6c6f73;<br>
color-scheme: light;<br>
--service-bg-hover: #f7faff;<br>
--service-bg: #fafbfb;<br>
}</p>
<p>@media only screen and (prefers-color-scheme: dark) {<br>
#mount:not([data-theme=&quot;light&quot;]) {<br>
--background-color: #11191f;<br>
--float-ball-more-button-background-color: #ffffff;<br>
--background-light-green: #141e26;<br>
--color: hsl(205deg, 16%, 77%);<br>
--h1-color: hsl(205deg, 20%, 94%);<br>
--h2-color: #e1e6eb;<br>
--h3-color: hsl(205deg, 18%, 86%);<br>
--h4-color: #c8d1d8;<br>
--h5-color: hsl(205deg, 16%, 77%);<br>
--h6-color: #afbbc4;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: #1f2d38;<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 80%, 50%);<br>
--primary-focus: rgba(16, 149, 193, 0.25);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 10%, 50%);<br>
--secondary-focus: rgba(115, 130, 140, 0.25);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 20%, 94%);<br>
--contrast-hover: #fff;<br>
--contrast-focus: rgba(115, 130, 140, 0.25);<br>
--contrast-inverse: #000;<br>
--mark-background-color: #d1c284;<br>
--mark-color: #11191f;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: #11191f;<br>
--form-element-border-color: #374956;<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: var(<br>
--form-element-background-color<br>
);<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 25%, 23%);<br>
--form-element-disabled-border-color: hsl(205deg, 20%, 32%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #b71c1c;<br>
--form-element-invalid-active-border-color: #c62828;<br>
--form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);<br>
--form-element-valid-border-color: #2e7d32;<br>
--form-element-valid-active-border-color: #388e3c;<br>
--form-element-valid-focus-color: rgba(56, 142, 60, 0.25);<br>
--switch-background-color: #374956;<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: #24333e;<br>
--range-active-border-color: hsl(205deg, 25%, 23%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: rgba(115, 130, 140, 0.05);<br>
--code-background-color: #18232c;<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 30%, 50%);<br>
--code-property-color: hsl(185deg, 30%, 50%);<br>
--code-value-color: hsl(40deg, 10%, 50%);<br>
--code-comment-color: #4d606d;<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-active-summary-color: var(--primary);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: #141e26;<br>
--card-border-color: var(--card-background-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),<br>
0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);<br>
--card-sectionning-background-color: #18232c;<br>
--dropdown-background-color: hsl(205deg, 30%, 15%);<br>
--dropdown-border-color: #24333e;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: rgba(36, 51, 62, 0.75);<br>
--modal-overlay-background-color: rgba(36, 51, 62, 0.8);<br>
--progress-background-color: #24333e;<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=&quot;);<br>
color-scheme: dark;<br>
--service-bg-hover: #22292f;<br>
--service-bg: rgba(0, 0, 0, 0.1);<br>
}<br>
}<br>
[data-theme=&quot;dark&quot;] {<br>
--background-color: #11191f;<br>
--float-ball-more-button-background-color: #191919;<br>
--background-light-green: #141e26;<br>
--color: hsl(205deg, 16%, 77%);<br>
--h1-color: hsl(205deg, 20%, 94%);<br>
--h2-color: #e1e6eb;<br>
--h3-color: hsl(205deg, 18%, 86%);<br>
--h4-color: #c8d1d8;<br>
--h5-color: hsl(205deg, 16%, 77%);<br>
--h6-color: #afbbc4;<br>
--muted-color: hsl(205deg, 10%, 50%);<br>
--muted-border-color: #1f2d38;<br>
--primary: hsl(195deg, 85%, 41%);<br>
--primary-hover: hsl(195deg, 80%, 50%);<br>
--primary-focus: rgba(16, 149, 193, 0.25);<br>
--primary-inverse: #fff;<br>
--secondary: hsl(205deg, 15%, 41%);<br>
--secondary-hover: hsl(205deg, 10%, 50%);<br>
--secondary-focus: rgba(115, 130, 140, 0.25);<br>
--secondary-inverse: #fff;<br>
--contrast: hsl(205deg, 20%, 94%);<br>
--contrast-hover: #fff;<br>
--contrast-focus: rgba(115, 130, 140, 0.25);<br>
--contrast-inverse: #000;<br>
--mark-background-color: #d1c284;<br>
--mark-color: #11191f;<br>
--ins-color: #388e3c;<br>
--del-color: #c62828;<br>
--blockquote-border-color: var(--muted-border-color);<br>
--blockquote-footer-color: var(--muted-color);<br>
--button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);<br>
--form-element-background-color: #11191f;<br>
--form-element-border-color: #374956;<br>
--form-element-color: var(--color);<br>
--form-element-placeholder-color: var(--muted-color);<br>
--form-element-active-background-color: var(--form-element-background-color);<br>
--form-element-active-border-color: var(--primary);<br>
--form-element-focus-color: var(--primary-focus);<br>
--form-element-disabled-background-color: hsl(205deg, 25%, 23%);<br>
--form-element-disabled-border-color: hsl(205deg, 20%, 32%);<br>
--form-element-disabled-opacity: 0.5;<br>
--form-element-invalid-border-color: #b71c1c;<br>
--form-element-invalid-active-border-color: #c62828;<br>
--form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);<br>
--form-element-valid-border-color: #2e7d32;<br>
--form-element-valid-active-border-color: #388e3c;<br>
--form-element-valid-focus-color: rgba(56, 142, 60, 0.25);<br>
--switch-background-color: #374956;<br>
--switch-color: var(--primary-inverse);<br>
--switch-checked-background-color: var(--primary);<br>
--range-border-color: #24333e;<br>
--range-active-border-color: hsl(205deg, 25%, 23%);<br>
--range-thumb-border-color: var(--background-color);<br>
--range-thumb-color: var(--secondary);<br>
--range-thumb-hover-color: var(--secondary-hover);<br>
--range-thumb-active-color: var(--primary);<br>
--table-border-color: var(--muted-border-color);<br>
--table-row-stripped-background-color: rgba(115, 130, 140, 0.05);<br>
--code-background-color: #18232c;<br>
--code-color: var(--muted-color);<br>
--code-kbd-background-color: var(--contrast);<br>
--code-kbd-color: var(--contrast-inverse);<br>
--code-tag-color: hsl(330deg, 30%, 50%);<br>
--code-property-color: hsl(185deg, 30%, 50%);<br>
--code-value-color: hsl(40deg, 10%, 50%);<br>
--code-comment-color: #4d606d;<br>
--accordion-border-color: var(--muted-border-color);<br>
--accordion-active-summary-color: var(--primary);<br>
--accordion-close-summary-color: var(--color);<br>
--accordion-open-summary-color: var(--muted-color);<br>
--card-background-color: #141e26;<br>
--card-border-color: var(--card-background-color);<br>
--card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),<br>
0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),<br>
0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),<br>
0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),<br>
0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),<br>
0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);<br>
--card-sectionning-background-color: #18232c;<br>
--dropdown-background-color: hsl(205deg, 30%, 15%);<br>
--dropdown-border-color: #24333e;<br>
--dropdown-box-shadow: var(--card-box-shadow);<br>
--dropdown-color: var(--color);<br>
--dropdown-hover-background-color: rgba(36, 51, 62, 0.75);<br>
--modal-overlay-background-color: rgba(36, 51, 62, 0.8);<br>
--progress-background-color: #24333e;<br>
--progress-color: var(--primary);<br>
--loading-spinner-opacity: 0.5;<br>
--tooltip-background-color: var(--contrast);<br>
--tooltip-color: var(--contrast-inverse);<br>
--icon-checkbox: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-chevron-button-inverse: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-close: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-date: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-invalid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-minus: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-search: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E&quot;);<br>
--icon-time: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-valid: url(&quot;data:image/svg+xml,%3Csvg xmlns='<a href="http://www.w3.org/2000/svg" target="_blank" rel="noopener noreferrer">http://www.w3.org/2000/svg</a>' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E&quot;);<br>
--icon-share: url(&quot;data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=&quot;);<br>
color-scheme: dark;<br>
--service-bg: rgba(0, 0, 0, 0.1);<br>
}</p>
<p>progress,<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;] {<br>
accent-color: var(--primary);<br>
}</p>
<p>/**</p>
<ul>
<li>Document</li>
<li>Content-box &amp; Responsive typography<br>
*/<br>
*,<br>
*<VPIcon icon="before,
*" />after {<br>
box-sizing: border-box;<br>
background-repeat: no-repeat;<br>
}</li>
</ul>
<p><VPIcon icon="before," />after {<br>
text-decoration: inherit;<br>
vertical-align: inherit;<br>
}</p>
<p>:where(#mount) {<br>
-webkit-tap-highlight-color: transparent;<br>
-webkit-text-size-adjust: 100%;<br>
-moz-text-size-adjust: 100%;<br>
text-size-adjust: 100%;<br>
background-color: var(--background-color);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
line-height: var(--line-height);<br>
font-family: var(--font-family);<br>
text-rendering: optimizeLegibility;<br>
overflow-wrap: break-word;<br>
cursor: default;<br>
-moz-tab-size: 4;<br>
-o-tab-size: 4;<br>
tab-size: 4;<br>
}</p>
<p>/**</p>
<ul>
<li>Sectioning</li>
<li>Container and responsive spacings for header, main, footer<br>
*/<br>
main {<br>
display: block;<br>
}</li>
</ul>
<p>#mount {<br>
width: 100%;<br>
margin: 0;<br>
}<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
width: 100%;<br>
margin-right: auto;<br>
margin-left: auto;<br>
padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);<br>
}<br>
@media (min-width: 576px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 2px !important;<br>
}<br>
}<br>
@media (min-width: 992px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 0 12px !important;<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
#mount &gt; header,<br>
#mount &gt; main,<br>
#mount &gt; footer {<br>
padding: 0 24px !important;<br>
}<br>
}</p>
<p>/**</p>
<ul>
<li>Container<br>
<em>/<br>
.container,<br>
.container-fluid {<br>
width: 100%;<br>
margin-right: auto;<br>
margin-left: auto;<br>
padding-right: var(--spacing);<br>
padding-left: var(--spacing);<br>
}<br>
/</em><br>
@media (min-width: 576px) {<br>
.container {<br>
max-width: 510px;<br>
padding-right: 0;<br>
padding-left: 0;<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
.container {<br>
max-width: 700px;<br>
}<br>
} */<br>
@media (min-width: 992px) {<br>
.container {<br>
max-width: 920px;<br>
}<br>
}<br>
@media (min-width: 1200px) {<br>
.container {<br>
max-width: 1130px;<br>
}<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Section</li>
<li>Responsive spacings for section<br>
*/<br>
section {<br>
margin-bottom: var(--block-spacing-vertical);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Grid</li>
<li>Minimal grid system with auto-layout columns<br>
*/<br>
.grid {<br>
grid-column-gap: var(--grid-spacing-horizontal);<br>
grid-row-gap: var(--grid-spacing-vertical);<br>
display: grid;<br>
grid-template-columns: 1fr;<br>
margin: 0;<br>
}<br>
@media (min-width: 1280px) {<br>
.grid {<br>
grid-template-columns: repeat(auto-fit, minmax(0%, 1fr));<br>
}<br>
}<br>
.grid &gt; * {<br>
min-width: 0;<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Horizontal scroller (<figure>)<br>
*/<br>
figure {<br>
display: block;<br>
margin: 0;<br>
padding: 0;<br>
overflow-x: auto;<br>
}<br>
figure figcaption {<br>
padding: calc(var(--spacing) * 0.5) 0;<br>
color: var(--muted-color);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Typography<br>
*/<br>
b,<br>
strong {<br>
font-weight: bolder;<br>
}</li>
</ul>
<p>sub,<br>
sup {<br>
position: relative;<br>
font-size: 0.75em;<br>
line-height: 0;<br>
vertical-align: baseline;<br>
}</p>
<p>sub {<br>
bottom: -0.25em;<br>
}</p>
<p>sup {<br>
top: -0.5em;<br>
}</p>
<p>address,<br>
blockquote,<br>
dl,<br>
figure,<br>
form,<br>
ol,<br>
p,<br>
pre,<br>
table,<br>
ul {<br>
margin-top: 0;<br>
margin-bottom: var(--typography-spacing-vertical);<br>
color: var(--color);<br>
font-style: normal;<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
}</p>
<p>a,<br>
[role=&quot;link&quot;] {<br>
--color: var(--primary);<br>
--background-color: transparent;<br>
outline: none;<br>
background-color: var(--background-color);<br>
color: var(--color);<br>
-webkit-text-decoration: var(--text-decoration);<br>
text-decoration: var(--text-decoration);<br>
transition: background-color var(--transition), color var(--transition),<br>
box-shadow var(--transition), -webkit-text-decoration var(--transition);<br>
transition: background-color var(--transition), color var(--transition),<br>
text-decoration var(--transition), box-shadow var(--transition);<br>
transition: background-color var(--transition), color var(--transition),<br>
text-decoration var(--transition), box-shadow var(--transition),<br>
-webkit-text-decoration var(--transition);<br>
}<br>
a:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--primary-hover);<br>
--text-decoration: underline;<br>
}<br>
a:focus,<br>
[role=&quot;link&quot;]:focus {<br>
--background-color: var(--primary-focus);<br>
}<br>
a.secondary,<br>
[role=&quot;link&quot;].secondary {<br>
--color: var(--secondary);<br>
}<br>
a.secondary:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;].secondary:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--secondary-hover);<br>
}<br>
a.secondary:focus,<br>
[role=&quot;link&quot;].secondary:focus {<br>
--background-color: var(--secondary-focus);<br>
}<br>
a.contrast,<br>
[role=&quot;link&quot;].contrast {<br>
--color: var(--contrast);<br>
}<br>
a.contrast:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;].contrast:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--contrast-hover);<br>
}<br>
a.contrast:focus,<br>
[role=&quot;link&quot;].contrast:focus {<br>
--background-color: var(--contrast-focus);<br>
}</p>
<p>h1,<br>
h2,<br>
h3,<br>
h4,<br>
h5,<br>
h6 {<br>
margin-top: 0;<br>
margin-bottom: var(--typography-spacing-vertical);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
font-family: var(--font-family);<br>
}</p>
<p>h1 {<br>
--color: var(--h1-color);<br>
}</p>
<p>h2 {<br>
--color: var(--h2-color);<br>
}</p>
<p>h3 {<br>
--color: var(--h3-color);<br>
}</p>
<p>h4 {<br>
--color: var(--h4-color);<br>
}</p>
<p>h5 {<br>
--color: var(--h5-color);<br>
}</p>
<p>h6 {<br>
--color: var(--h6-color);<br>
}</p>
<p>:where(address, blockquote, dl, figure, form, ol, p, pre, table, ul)<br>
~ :is(h1, h2, h3, h4, h5, h6) {<br>
margin-top: var(--typography-spacing-vertical);<br>
}</p>
<p>hgroup,<br>
.headings {<br>
margin-bottom: var(--typography-spacing-vertical);<br>
}<br>
hgroup &gt; *,<br>
.headings &gt; * {<br>
margin-bottom: 0;<br>
}<br>
hgroup &gt; *:last-child,<br>
.headings &gt; *:last-child {<br>
--color: var(--muted-color);<br>
--font-weight: unset;<br>
font-size: 1rem;<br>
font-family: unset;<br>
}</p>
<p>p {<br>
margin-bottom: var(--typography-spacing-vertical);<br>
}</p>
<p>small {<br>
font-size: var(--font-size);<br>
}</p>
<p>:where(dl, ol, ul) {<br>
padding-right: 0;<br>
padding-left: var(--spacing);<br>
-webkit-padding-start: var(--spacing);<br>
padding-inline-start: var(--spacing);<br>
-webkit-padding-end: 0;<br>
padding-inline-end: 0;<br>
}<br>
:where(dl, ol, ul) li {<br>
margin-bottom: calc(var(--typography-spacing-vertical) * 0.25);<br>
}</p>
<p>:where(dl, ol, ul) :is(dl, ol, ul) {<br>
margin: 0;<br>
margin-top: calc(var(--typography-spacing-vertical) * 0.25);<br>
}</p>
<p>ul li {<br>
list-style: square;<br>
}</p>
<p>mark {<br>
padding: 0.125rem 0.25rem;<br>
background-color: var(--mark-background-color);<br>
color: var(--mark-color);<br>
vertical-align: baseline;<br>
}</p>
<p>blockquote {<br>
display: block;<br>
margin: var(--typography-spacing-vertical) 0;<br>
padding: var(--spacing);<br>
border-right: none;<br>
border-left: 0.25rem solid var(--blockquote-border-color);<br>
-webkit-border-start: 0.25rem solid var(--blockquote-border-color);<br>
border-inline-start: 0.25rem solid var(--blockquote-border-color);<br>
-webkit-border-end: none;<br>
border-inline-end: none;<br>
}<br>
blockquote footer {<br>
margin-top: calc(var(--typography-spacing-vertical) * 0.5);<br>
color: var(--blockquote-footer-color);<br>
}</p>
<p>abbr[title] {<br>
border-bottom: 1px dotted;<br>
text-decoration: none;<br>
cursor: help;<br>
}</p>
<p>ins {<br>
color: var(--ins-color);<br>
text-decoration: none;<br>
}</p>
<p>del {<br>
color: var(--del-color);<br>
}</p>
<p>::-moz-selection {<br>
background-color: var(--primary-focus);<br>
}</p>
<p>::selection {<br>
background-color: var(--primary-focus);<br>
}</p>
<p>/**</p>
<ul>
<li>Embedded content<br>
*/<br>
:where(audio, canvas, iframe, img, svg, video) {<br>
vertical-align: middle;<br>
}</li>
</ul>
<p>audio,<br>
video {<br>
display: inline-block;<br>
}</p>
<p>audio:not([controls]) {<br>
display: none;<br>
height: 0;<br>
}</p>
<p>:where(iframe) {<br>
border-style: none;<br>
}</p>
<p>img {<br>
max-width: 100%;<br>
height: auto;<br>
border-style: none;<br>
}</p>
<p>:where(svg:not([fill])) {<br>
fill: currentColor;<br>
}</p>
<p>svg:not(#mount) {<br>
overflow: hidden;<br>
}</p>
<p>/**</p>
<ul>
<li>Button<br>
*/<br>
button {<br>
margin: 0;<br>
overflow: visible;<br>
font-family: inherit;<br>
text-transform: none;<br>
}</li>
</ul>
<p>button,<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;submit&quot;] {<br>
-webkit-appearance: button;<br>
}</p>
<p>button {<br>
display: block;<br>
width: 100%;<br>
margin-bottom: var(--spacing);<br>
}</p>
<p>[role=&quot;button&quot;] {<br>
display: inline-block;<br>
text-decoration: none;<br>
}</p>
<p>button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
input[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;] {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
--color: var(--primary-inverse);<br>
--box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: 1rem;<br>
line-height: var(--line-height);<br>
text-align: center;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}<br>
button:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;submit&quot;]:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;button&quot;]:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;]:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;button&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--primary-hover);<br>
--border-color: var(--primary-hover);<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
--color: var(--primary-inverse);<br>
}<br>
button:focus,<br>
input[type=&quot;submit&quot;]:focus,<br>
input[type=&quot;button&quot;]:focus,<br>
input[type=&quot;reset&quot;]:focus,<br>
[role=&quot;button&quot;]:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--primary-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary,<br>
input[type=&quot;reset&quot;] {<br>
--background-color: var(--secondary);<br>
--border-color: var(--secondary);<br>
--color: var(--secondary-inverse);<br>
cursor: pointer;<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
--color: var(--secondary-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).secondary:focus,<br>
input[type=&quot;reset&quot;]:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--secondary-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast {<br>
--background-color: var(--contrast);<br>
--border-color: var(--contrast);<br>
--color: var(--contrast-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast:is([aria-current], :hover, :active, :focus) {<br>
--background-color: var(--contrast-hover);<br>
--border-color: var(--contrast-hover);<br>
--color: var(--contrast-inverse);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).contrast:focus {<br>
--box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),<br>
0 0 0 var(--outline-width) var(--contrast-focus);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline,<br>
input[type=&quot;reset&quot;].outline {<br>
--background-color: transparent;<br>
--color: var(--primary);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;].outline:is([aria-current], :hover, :active, :focus) {<br>
--background-color: transparent;<br>
--color: var(--primary-hover);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.secondary,<br>
input[type=&quot;reset&quot;].outline {<br>
--color: var(--secondary);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.secondary:is([aria-current], :hover, :active, :focus),<br>
input[type=&quot;reset&quot;].outline:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--secondary-hover);<br>
}</p>
<p>:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.contrast {<br>
--color: var(--contrast);<br>
}<br>
:is(<br>
button,<br>
input[type=&quot;submit&quot;],<br>
input[type=&quot;button&quot;],<br>
[role=&quot;button&quot;]<br>
).outline.contrast:is([aria-current], :hover, :active, :focus) {<br>
--color: var(--contrast-hover);<br>
}</p>
<p>:where(<br>
button,<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;]<br>
)[disabled],<br>
:where(fieldset[disabled])<br>
:is(<br>
button,<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;button&quot;]<br>
),<br>
a[role=&quot;button&quot;]:not([href]) {<br>
opacity: 0.5;<br>
pointer-events: none;<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements<br>
*/<br>
input,<br>
optgroup,<br>
select,<br>
textarea {<br>
margin: 0;<br>
font-size: 1rem;<br>
line-height: var(--line-height);<br>
font-family: inherit;<br>
letter-spacing: inherit;<br>
}</li>
</ul>
<p>input {<br>
overflow: visible;<br>
}</p>
<p>select {<br>
text-transform: none;<br>
}</p>
<p>legend {<br>
max-width: 100%;<br>
padding: 0;<br>
color: inherit;<br>
white-space: normal;<br>
}</p>
<p>textarea {<br>
overflow: auto;<br>
}</p>
<p>[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
padding: 0;<br>
}</p>
<p><VPIcon icon="-webkit-inner-spin-button," />-webkit-outer-spin-button {<br>
height: auto;<br>
}</p>
<p>[type=&quot;search&quot;] {<br>
-webkit-appearance: textfield;<br>
outline-offset: -2px;<br>
}</p>
<p>[type=&quot;search&quot;]::-webkit-search-decoration {<br>
-webkit-appearance: none;<br>
}</p>
<p>::-webkit-file-upload-button {<br>
-webkit-appearance: button;<br>
font: inherit;<br>
}</p>
<p>::-moz-focus-inner {<br>
padding: 0;<br>
border-style: none;<br>
}</p>
<p>:-moz-focusring {<br>
outline: none;<br>
}</p>
<p>:-moz-ui-invalid {<br>
box-shadow: none;<br>
}</p>
<p>::-ms-expand {<br>
display: none;<br>
}</p>
<p>[type=&quot;file&quot;],<br>
[type=&quot;range&quot;] {<br>
padding: 0;<br>
border-width: 0;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;]) {<br>
height: calc(<br>
1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +<br>
var(--border-width) * 2<br>
);<br>
}</p>
<p>fieldset {<br>
margin: 0;<br>
margin-bottom: var(--spacing);<br>
padding: 0;<br>
border: 0;<br>
}</p>
<p>label,<br>
fieldset legend {<br>
display: block;<br>
margin-bottom: calc(var(--spacing) * 0.25);<br>
font-weight: var(--form-label-font-weight, var(--font-weight));<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]),<br>
select,<br>
textarea {<br>
width: 100%;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;], [type=&quot;file&quot;]),<br>
select,<br>
textarea {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
}</p>
<p>input,<br>
select,<br>
textarea {<br>
--background-color: var(--form-element-background-color);<br>
--border-color: var(--form-element-border-color);<br>
--color: var(--form-element-color);<br>
--box-shadow: none;<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[readonly]<br>
):is(:active, :focus),<br>
:where(select, textarea):is(:active, :focus) {<br>
--background-color: var(--form-element-active-background-color);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[role=&quot;switch&quot;],<br>
[readonly]<br>
):is(:active, :focus),<br>
:where(select, textarea):is(:active, :focus) {<br>
--border-color: var(--form-element-active-border-color);<br>
}</p>
<p>input:not(<br>
[type=&quot;submit&quot;],<br>
[type=&quot;button&quot;],<br>
[type=&quot;reset&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;],<br>
[readonly]<br>
):focus,<br>
select:focus,<br>
textarea:focus {<br>
--box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);<br>
}</p>
<p>input:not([type=&quot;submit&quot;], [type=&quot;button&quot;], [type=&quot;reset&quot;])[disabled],<br>
select[disabled],<br>
textarea[disabled],<br>
:where(fieldset[disabled])<br>
:is(<br>
input:not([type=&quot;submit&quot;], [type=&quot;button&quot;], [type=&quot;reset&quot;]),<br>
select,<br>
textarea<br>
) {<br>
--background-color: var(--form-element-disabled-background-color);<br>
--border-color: var(--form-element-disabled-border-color);<br>
opacity: var(--form-element-disabled-opacity);<br>
pointer-events: none;<br>
}</p>
<p>:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid] {<br>
padding-right: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
padding-left: var(--form-element-spacing-horizontal);<br>
-webkit-padding-start: var(--form-element-spacing-horizontal) !important;<br>
padding-inline-start: var(--form-element-spacing-horizontal) !important;<br>
-webkit-padding-end: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
padding-inline-end: calc(<br>
var(--form-element-spacing-horizontal) + 1.5rem<br>
) !important;<br>
background-position: center right 0.75rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}<br>
:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid=&quot;false&quot;] {<br>
background-image: var(--icon-valid);<br>
}<br>
:where(input, select, textarea):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
)[aria-invalid=&quot;true&quot;] {<br>
background-image: var(--icon-invalid);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;false&quot;] {<br>
--border-color: var(--form-element-valid-border-color);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;false&quot;]:is(:active, :focus) {<br>
--border-color: var(--form-element-valid-active-border-color) !important;<br>
--box-shadow: 0 0 0 var(--outline-width) var(--form-element-valid-focus-color) !important;<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;true&quot;] {<br>
--border-color: var(--form-element-invalid-border-color);<br>
}<br>
:where(input, select, textarea)[aria-invalid=&quot;true&quot;]:is(:active, :focus) {<br>
--border-color: var(--form-element-invalid-active-border-color) !important;<br>
--box-shadow: 0 0 0 var(--outline-width)<br>
var(--form-element-invalid-focus-color) !important;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:where(input, select, textarea):not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]):is(<br>
[aria-invalid],<br>
[aria-invalid=&quot;true&quot;],<br>
[aria-invalid=&quot;false&quot;]<br>
) {<br>
background-position: center left 0.75rem;<br>
}</p>
<p>input<VPIcon icon="placeholder,
input" />-webkit-input-placeholder,<br>
textarea<VPIcon icon="placeholder,
textarea" />-webkit-input-placeholder,<br>
select:invalid {<br>
color: var(--form-element-placeholder-color);<br>
opacity: 1;<br>
}</p>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;]),<br>
select,<br>
textarea {<br>
margin-bottom: var(--spacing);<br>
}</p>
<p>select::-ms-expand {<br>
border: 0;<br>
background-color: transparent;<br>
}<br>
select:not([multiple], [size]) {<br>
padding-right: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
padding-left: var(--form-element-spacing-horizontal);<br>
-webkit-padding-start: var(--form-element-spacing-horizontal);<br>
padding-inline-start: var(--form-element-spacing-horizontal);<br>
-webkit-padding-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
padding-inline-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);<br>
background-image: var(--icon-chevron);<br>
background-position: center right 0.75rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}</p>
<p>[dir=&quot;rtl&quot;] select:not([multiple], [size]) {<br>
background-position: center left 0.75rem;<br>
}</p>
<p>:where(input, select, textarea) + small {<br>
display: block;<br>
width: 100%;<br>
margin-top: calc(var(--spacing) * -0.75);<br>
margin-bottom: var(--spacing);<br>
color: var(--muted-color);<br>
}</p>
<p>label &gt; :where(input, select, textarea) {<br>
margin-top: calc(var(--spacing) * 0.25);<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements</li>
<li>Checkboxes &amp; Radios<br>
*/<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;] {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
width: 1.25em;<br>
height: 1.25em;<br>
margin-top: -0.125em;<br>
margin-right: 0.375em;<br>
margin-left: 0;<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
-webkit-margin-end: 0.375em;<br>
margin-inline-end: 0.375em;<br>
border-width: var(--border-width);<br>
font-size: inherit;<br>
vertical-align: middle;<br>
cursor: pointer;<br>
}<br>
[type=&quot;checkbox&quot;]<VPIcon icon="-ms-check,
[" type="&quot;radio&quot;]" />-ms-check {<br>
display: none;<br>
}<br>
[type=&quot;checkbox&quot;]:checked,<br>
[type=&quot;checkbox&quot;]:checked:active,<br>
[type=&quot;checkbox&quot;]:checked:focus,<br>
[type=&quot;radio&quot;]:checked,<br>
[type=&quot;radio&quot;]:checked:active,<br>
[type=&quot;radio&quot;]:checked:focus {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
background-image: var(--icon-checkbox);<br>
background-position: center;<br>
background-size: 0.75em auto;<br>
background-repeat: no-repeat;<br>
}<br>
[type=&quot;checkbox&quot;] ~ label,<br>
[type=&quot;radio&quot;] ~ label {<br>
display: inline-block;<br>
margin-right: 0.375em;<br>
margin-bottom: 0;<br>
cursor: pointer;<br>
}</li>
</ul>
<p>[type=&quot;checkbox&quot;]:indeterminate {<br>
--background-color: var(--primary);<br>
--border-color: var(--primary);<br>
background-image: var(--icon-minus);<br>
background-position: center;<br>
background-size: 0.75em auto;<br>
background-repeat: no-repeat;<br>
}</p>
<p>[type=&quot;radio&quot;] {<br>
border-radius: 50%;<br>
}<br>
[type=&quot;radio&quot;]:checked,<br>
[type=&quot;radio&quot;]:checked:active,<br>
[type=&quot;radio&quot;]:checked:focus {<br>
--background-color: var(--primary-inverse);<br>
border-width: 0.35em;<br>
background-image: none;<br>
}</p>
<p>[type=&quot;checkbox&quot;][role=&quot;switch&quot;] {<br>
--background-color: var(--switch-background-color);<br>
--border-color: var(--switch-background-color);<br>
--color: var(--switch-color);<br>
width: 2.25em;<br>
height: 1.25em;<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: 1.25em;<br>
background-color: var(--background-color);<br>
line-height: 1.25em;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:focus {<br>
--background-color: var(--switch-background-color);<br>
--border-color: var(--switch-background-color);<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked {<br>
--background-color: var(--switch-checked-background-color);<br>
--border-color: var(--switch-checked-background-color);<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:before {<br>
display: block;<br>
width: calc(1.25em - (var(--border-width) * 2));<br>
height: 100%;<br>
border-radius: 50%;<br>
background-color: var(--color);<br>
content: &quot;&quot;;<br>
transition: margin 0.1s ease-in-out;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked {<br>
background-image: none;<br>
}<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked::before {<br>
margin-left: calc(1.125em - var(--border-width));<br>
-webkit-margin-start: calc(1.125em - var(--border-width));<br>
margin-inline-start: calc(1.125em - var(--border-width));<br>
}</p>
<p>[type=&quot;checkbox&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;]:checked[aria-invalid=&quot;false&quot;],<br>
[type=&quot;radio&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;radio&quot;]:checked[aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;][aria-invalid=&quot;false&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked[aria-invalid=&quot;false&quot;] {<br>
--border-color: var(--form-element-valid-border-color);<br>
}<br>
[type=&quot;checkbox&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;]:checked[aria-invalid=&quot;true&quot;],<br>
[type=&quot;radio&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;radio&quot;]:checked[aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;][aria-invalid=&quot;true&quot;],<br>
[type=&quot;checkbox&quot;][role=&quot;switch&quot;]:checked[aria-invalid=&quot;true&quot;] {<br>
--border-color: var(--form-element-invalid-border-color);<br>
}</p>
<p>/**</p>
<ul>
<li>Form elements</li>
<li>Alternatives input types (Not Checkboxes &amp; Radios)<br>
*/<br>
[type=&quot;color&quot;]<VPIcon icon="-webkit-color-swatch-wrapper {
padding: 0;
}
[" type="&quot;color&quot;]" />-moz-focus-inner {<br>
padding: 0;<br>
}<br>
[type=&quot;color&quot;]<VPIcon icon="-webkit-color-swatch {
border: 0;
border-radius: calc(var(--border-radius) * 0.5);
}
[" type="&quot;color&quot;]" />-moz-color-swatch {<br>
border: 0;<br>
border-radius: calc(var(--border-radius) * 0.5);<br>
}</li>
</ul>
<p>input:not([type=&quot;checkbox&quot;], [type=&quot;radio&quot;], [type=&quot;range&quot;], [type=&quot;file&quot;]):is(<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
) {<br>
--icon-position: 0.75rem;<br>
--icon-width: 1rem;<br>
padding-right: calc(var(--icon-width) + var(--icon-position));<br>
background-image: var(--icon-date);<br>
background-position: center right var(--icon-position);<br>
background-size: var(--icon-width) auto;<br>
background-repeat: no-repeat;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a> {<br>
background-image: var(--icon-time);<br>
}</p>
<p>[type=&quot;week&quot;]::-webkit-calendar-picker-indicator {<br>
width: var(--icon-width);<br>
margin-right: calc(var(--icon-width) * -1);<br>
margin-left: var(--icon-position);<br>
opacity: 0;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:is(<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;date&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;datetime-local&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;month&quot;</a>,<br>
<a href=":-webkit-calendar-picker-indicator,">type=&quot;time&quot;</a>,<br>
[type=&quot;week&quot;]<br>
) {<br>
text-align: right;<br>
}</p>
<p>[type=&quot;file&quot;] {<br>
--color: var(--muted-color);<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5) 0;<br>
border: 0;<br>
border-radius: 0;<br>
background: none;<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="file-selector-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />file-selector-button:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="-webkit-file-upload-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -webkit-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />-webkit-file-upload-button:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}<br>
[type=&quot;file&quot;]<VPIcon icon="-ms-browse {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing)   margin-left: 0;
  margin-inline-start: 0;
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -ms-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[" type="&quot;file&quot;]" color=" 2);" />-ms-browse:is(:hover, :active, :focus) {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
}</p>
<p>[type=&quot;range&quot;] {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
appearance: none;<br>
width: 100%;<br>
height: 1.25rem;<br>
background: none;<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-webkit-slider-runnable-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -webkit-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[" type="&quot;range&quot;]" />-moz-range-track {<br>
width: 100%;<br>
height: 0.25rem;<br>
border-radius: var(--border-radius);<br>
background-color: var(--range-border-color);<br>
-moz-transition: background-color var(--transition),<br>
box-shadow var(--transition);<br>
transition: background-color var(--transition), box-shadow var(--transition);<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-ms-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -ms-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[" type="&quot;range&quot;]" />-webkit-slider-thumb {<br>
-webkit-appearance: none;<br>
width: 1.25rem;<br>
height: 1.25rem;<br>
margin-top: -0.5rem;<br>
border: 2px solid var(--range-thumb-border-color);<br>
border-radius: 50%;<br>
background-color: var(--range-thumb-color);<br>
cursor: pointer;<br>
-webkit-transition: background-color var(--transition),<br>
transform var(--transition);<br>
transition: background-color var(--transition), transform var(--transition);<br>
}<br>
[type=&quot;range&quot;]<VPIcon icon="-moz-range-thumb {
  -webkit-appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: -0.5rem;
  border: 2px solid var(--range-thumb-border-color);
  border-radius: 50%;
  background-color: var(--range-thumb-color);
  cursor: pointer;
  -moz-transition: background-color var(--transition),
    transform var(--transition);
  transition: background-color var(--transition), transform var(--transition);
}
[" type="&quot;range&quot;]" />-ms-thumb {<br>
-webkit-appearance: none;<br>
width: 1.25rem;<br>
height: 1.25rem;<br>
margin-top: -0.5rem;<br>
border: 2px solid var(--range-thumb-border-color);<br>
border-radius: 50%;<br>
background-color: var(--range-thumb-color);<br>
cursor: pointer;<br>
-ms-transition: background-color var(--transition),<br>
transform var(--transition);<br>
transition: background-color var(--transition), transform var(--transition);<br>
}<br>
[type=&quot;range&quot;]:hover,<br>
[type=&quot;range&quot;]:focus {<br>
--range-border-color: var(--range-active-border-color);<br>
--range-thumb-color: var(--range-thumb-hover-color);<br>
}<br>
[type=&quot;range&quot;]:active {<br>
--range-thumb-color: var(--range-thumb-active-color);<br>
}<br>
[type=&quot;range&quot;]:active<VPIcon icon="-webkit-slider-thumb {
  transform: scale(1.25);
}
[" type="&quot;range&quot;]:active" />-moz-range-thumb {<br>
transform: scale(1.25);<br>
}<br>
[type=&quot;range&quot;]:active::-ms-thumb {<br>
transform: scale(1.25);<br>
}</p>
<p>input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;] {<br>
-webkit-padding-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);<br>
padding-inline-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);<br>
border-radius: 5rem;<br>
background-image: var(--icon-search);<br>
background-position: center left 1.125rem;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid] {<br>
-webkit-padding-start: calc(<br>
var(--form-element-spacing-horizontal) + 1.75rem<br>
) !important;<br>
padding-inline-start: calc(<br>
var(--form-element-spacing-horizontal) + 1.75rem<br>
) !important;<br>
background-position: center left 1.125rem, center right 0.75rem;<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid=&quot;false&quot;] {<br>
background-image: var(--icon-search), var(--icon-valid);<br>
}<br>
input:not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid=&quot;true&quot;] {<br>
background-image: var(--icon-search), var(--icon-invalid);<br>
}</p>
<p>[type=&quot;search&quot;]::-webkit-search-cancel-button {<br>
-webkit-appearance: none;<br>
display: none;<br>
}</p>
<p>[dir=&quot;rtl&quot;]<br>
:where(input):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;] {<br>
background-position: center right 1.125rem;<br>
}<br>
[dir=&quot;rtl&quot;]<br>
:where(input):not(<br>
[type=&quot;checkbox&quot;],<br>
[type=&quot;radio&quot;],<br>
[type=&quot;range&quot;],<br>
[type=&quot;file&quot;]<br>
)[type=&quot;search&quot;][aria-invalid] {<br>
background-position: center right 1.125rem, center left 0.75rem;<br>
}</p>
<p>/**</p>
<ul>
<li>Table<br>
*/<br>
:where(table) {<br>
width: 100%;<br>
border-collapse: collapse;<br>
border-spacing: 0;<br>
text-indent: 0;<br>
}</li>
</ul>
<p>th,<br>
td {<br>
padding: calc(var(--spacing) / 2) var(--spacing);<br>
border-bottom: var(--border-width) solid var(--table-border-color);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: var(--font-size);<br>
text-align: left;<br>
text-align: start;<br>
}</p>
<p>tfoot th,<br>
tfoot td {<br>
border-top: var(--border-width) solid var(--table-border-color);<br>
border-bottom: 0;<br>
}</p>
<p>table[role=&quot;grid&quot;] tbody tr:nth-child(odd) {<br>
background-color: var(--table-row-stripped-background-color);<br>
}</p>
<p>/**</p>
<ul>
<li>Code<br>
*/<br>
pre,<br>
code,<br>
kbd,<br>
samp {<br>
font-size: 0.875em;<br>
font-family: var(--font-family);<br>
}</li>
</ul>
<p>pre {<br>
-ms-overflow-style: scrollbar;<br>
overflow: auto;<br>
}</p>
<p>pre,<br>
code,<br>
kbd {<br>
border-radius: var(--border-radius);<br>
background: var(--code-background-color);<br>
color: var(--code-color);<br>
font-weight: var(--font-weight);<br>
line-height: initial;<br>
}</p>
<p>code,<br>
kbd {<br>
display: inline-block;<br>
padding: 0.375rem 0.5rem;<br>
}</p>
<p>pre {<br>
display: block;<br>
margin-bottom: var(--spacing);<br>
overflow-x: auto;<br>
}<br>
pre &gt; code {<br>
display: block;<br>
padding: var(--spacing);<br>
background: none;<br>
font-size: 14px;<br>
line-height: var(--line-height);<br>
}</p>
<p>code b {<br>
color: var(--code-tag-color);<br>
font-weight: var(--font-weight);<br>
}<br>
code i {<br>
color: var(--code-property-color);<br>
font-style: normal;<br>
}<br>
code u {<br>
color: var(--code-value-color);<br>
text-decoration: none;<br>
}<br>
code em {<br>
color: var(--code-comment-color);<br>
font-style: normal;<br>
}</p>
<p>kbd {<br>
background-color: var(--code-kbd-background-color);<br>
color: var(--code-kbd-color);<br>
vertical-align: baseline;<br>
}</p>
<p>/**</p>
<ul>
<li>Miscs<br>
*/<br>
hr {<br>
height: 0;<br>
border: 0;<br>
border-top: 1px solid var(--muted-border-color);<br>
color: inherit;<br>
}</li>
</ul>
<p>[hidden],<br>
template {<br>
display: none !important;<br>
}</p>
<p>canvas {<br>
display: inline-block;<br>
}</p>
<p>/**</p>
<ul>
<li>Accordion (<details>)<br>
*/<br>
details {<br>
display: block;<br>
margin-bottom: var(--spacing);<br>
padding-bottom: var(--spacing);<br>
border-bottom: var(--border-width) solid var(--accordion-border-color);<br>
}<br>
details summary {<br>
line-height: 1rem;<br>
list-style-type: none;<br>
cursor: pointer;<br>
transition: color var(--transition);<br>
}<br>
details summary:not([role]) {<br>
color: var(--accordion-close-summary-color);<br>
}<br>
details summary<VPIcon icon="-webkit-details-marker {
display: none;
}
details summary" />marker {<br>
display: none;<br>
}<br>
details summary<VPIcon icon="-moz-list-bullet {
list-style-type: none;
}
details summary" />after {<br>
display: block;<br>
width: 1rem;<br>
height: 1rem;<br>
-webkit-margin-start: calc(var(--spacing, 1rem) * 0.5);<br>
margin-inline-start: calc(var(--spacing, 1rem) * 0.5);<br>
float: right;<br>
transform: rotate(-90deg);<br>
background-image: var(--icon-chevron);<br>
background-position: right center;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
content: &quot;&quot;;<br>
transition: transform var(--transition);<br>
}<br>
details summary:focus {<br>
outline: none;<br>
}<br>
details summary:focus:not([role=&quot;button&quot;]) {<br>
color: var(--accordion-active-summary-color);<br>
}<br>
details summary[role=&quot;button&quot;] {<br>
width: 100%;<br>
text-align: left;<br>
}<br>
details summary[role=&quot;button&quot;]<VPIcon icon="after {
height: calc(1rem * var(--line-height, 1.5));
background-image: var(--icon-chevron-button);
}
details summary" [role="&quot;button&quot;]:not(.outline).contrast" />after {<br>
background-image: var(--icon-chevron-button-inverse);<br>
}<br>
details[open] &gt; summary {<br>
margin-bottom: calc(var(--spacing));<br>
}<br>
details[open] &gt; summary:not([role]):not(:focus) {<br>
color: var(--accordion-open-summary-color);<br>
}<br>
details[open] &gt; summary::after {<br>
transform: rotate(0);<br>
}</li>
</ul>
<p>[dir=&quot;rtl&quot;] details summary {<br>
text-align: right;<br>
}<br>
[dir=&quot;rtl&quot;] details summary::after {<br>
float: left;<br>
background-position: left center;<br>
}</p>
<p>/**</p>
<ul>
<li>Card (<article>)<br>
*/<br>
article {<br>
margin: var(--block-spacing-vertical) 0;<br>
padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);<br>
border-radius: var(--border-radius);<br>
background: var(--card-background-color);<br>
box-shadow: var(--card-box-shadow);<br>
}<br>
article &gt; header,<br>
article &gt; footer {<br>
margin-right: calc(var(--block-spacing-horizontal) * -1);<br>
margin-left: calc(var(--block-spacing-horizontal) * -1);<br>
padding: calc(var(--block-spacing-vertical) * 0.66)<br>
var(--block-spacing-horizontal);<br>
background-color: var(--card-sectionning-background-color);<br>
}<br>
article &gt; header {<br>
margin-top: calc(var(--block-spacing-vertical) * -1);<br>
margin-bottom: var(--block-spacing-vertical);<br>
border-bottom: var(--border-width) solid var(--card-border-color);<br>
border-top-right-radius: var(--border-radius);<br>
border-top-left-radius: var(--border-radius);<br>
}<br>
article &gt; footer {<br>
margin-top: var(--block-spacing-vertical);<br>
margin-bottom: calc(var(--block-spacing-vertical) * -1);<br>
border-top: var(--border-width) solid var(--card-border-color);<br>
border-bottom-right-radius: var(--border-radius);<br>
border-bottom-left-radius: var(--border-radius);<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Modal (<dialog>)<br>
*/<br>
#mount {<br>
--scrollbar-width: 0px;<br>
}</li>
</ul>
<p>dialog {<br>
display: flex;<br>
z-index: 999;<br>
position: fixed;<br>
top: 0;<br>
right: 0;<br>
bottom: 0;<br>
left: 0;<br>
align-items: center;<br>
justify-content: center;<br>
width: inherit;<br>
min-width: 100%;<br>
height: inherit;<br>
min-height: 100%;<br>
padding: var(--spacing);<br>
border: 0;<br>
-webkit-backdrop-filter: var(--modal-overlay-backdrop-filter);<br>
backdrop-filter: var(--modal-overlay-backdrop-filter);<br>
background-color: var(--modal-overlay-background-color);<br>
color: var(--color);<br>
}<br>
dialog article {<br>
max-height: calc(100vh - var(--spacing) * 2);<br>
overflow: auto;<br>
}<br>
@media (min-width: 576px) {<br>
dialog article {<br>
max-width: 510px;<br>
}<br>
}<br>
@media (min-width: 768px) {<br>
dialog article {<br>
max-width: 700px;<br>
}<br>
}<br>
dialog article &gt; header,<br>
dialog article &gt; footer {<br>
padding: calc(var(--block-spacing-vertical) * 0.5)<br>
var(--block-spacing-horizontal);<br>
}<br>
dialog article &gt; header .close {<br>
margin: 0;<br>
margin-left: var(--spacing);<br>
float: right;<br>
}<br>
dialog article &gt; footer {<br>
text-align: right;<br>
}<br>
dialog article &gt; footer [role=&quot;button&quot;] {<br>
margin-bottom: 0;<br>
}<br>
dialog article &gt; footer [role=&quot;button&quot;]:not(:first-of-type) {<br>
margin-left: calc(var(--spacing) * 0.5);<br>
}<br>
dialog article p:last-of-type {<br>
margin: 0;<br>
}<br>
dialog article .close {<br>
display: block;<br>
width: 1rem;<br>
height: 1rem;<br>
margin-top: calc(var(--block-spacing-vertical) * -0.5);<br>
margin-bottom: var(--typography-spacing-vertical);<br>
margin-left: auto;<br>
background-image: var(--icon-close);<br>
background-position: center;<br>
background-size: auto 1rem;<br>
background-repeat: no-repeat;<br>
opacity: 0.5;<br>
transition: opacity var(--transition);<br>
}<br>
dialog article .close:is([aria-current], :hover, :active, :focus) {<br>
opacity: 1;<br>
}<br>
dialog:not([open]),<br>
dialog[open=&quot;false&quot;] {<br>
display: none;<br>
}</p>
<p>.modal-is-open {<br>
padding-right: var(--scrollbar-width, 0px);<br>
overflow: hidden;<br>
pointer-events: none;<br>
}<br>
.modal-is-open dialog {<br>
pointer-events: auto;<br>
}</p>
<p>:where(.modal-is-opening, .modal-is-closing) dialog,<br>
:where(.modal-is-opening, .modal-is-closing) dialog &gt; article {<br>
animation-duration: 0.2s;<br>
animation-timing-function: ease-in-out;<br>
animation-fill-mode: both;<br>
}<br>
:where(.modal-is-opening, .modal-is-closing) dialog {<br>
animation-duration: 0.8s;<br>
animation-name: modal-overlay;<br>
}<br>
:where(.modal-is-opening, .modal-is-closing) dialog &gt; article {<br>
animation-delay: 0.2s;<br>
animation-name: modal;<br>
}</p>
<p>.modal-is-closing dialog,<br>
.modal-is-closing dialog &gt; article {<br>
animation-delay: 0s;<br>
animation-direction: reverse;<br>
}</p>
<p>@keyframes modal-overlay {<br>
from {<br>
-webkit-backdrop-filter: none;<br>
backdrop-filter: none;<br>
background-color: transparent;<br>
}<br>
}<br>
@keyframes modal {<br>
from {<br>
transform: translateY(-100%);<br>
opacity: 0;<br>
}<br>
}<br>
/**</p>
<ul>
<li>Nav<br>
*/<br>
:where(nav li)::before {<br>
float: left;<br>
content: &quot;​&quot;;<br>
}</li>
</ul>
<p>nav,<br>
nav ul {<br>
display: flex;<br>
}</p>
<p>nav {<br>
justify-content: space-between;<br>
}<br>
nav ol,<br>
nav ul {<br>
align-items: center;<br>
margin-bottom: 0;<br>
padding: 0;<br>
list-style: none;<br>
}<br>
nav ol:first-of-type,<br>
nav ul:first-of-type {<br>
margin-left: calc(var(--nav-element-spacing-horizontal) * -1);<br>
}<br>
nav ol:last-of-type,<br>
nav ul:last-of-type {<br>
margin-right: calc(var(--nav-element-spacing-horizontal) * -1);<br>
}<br>
nav li {<br>
display: inline-block;<br>
margin: 0;<br>
padding: var(--nav-element-spacing-vertical)<br>
var(--nav-element-spacing-horizontal);<br>
}<br>
nav li &gt; * {<br>
--spacing: 0;<br>
}<br>
nav :where(a, [role=&quot;link&quot;]) {<br>
display: inline-block;<br>
margin: calc(var(--nav-link-spacing-vertical) * -1)<br>
calc(var(--nav-link-spacing-horizontal) * -1);<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
border-radius: var(--border-radius);<br>
text-decoration: none;<br>
}<br>
nav :where(a, [role=&quot;link&quot;]):is([aria-current], :hover, :active, :focus) {<br>
text-decoration: none;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] {<br>
align-items: center;<br>
justify-content: start;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:first-child) {<br>
-webkit-margin-start: var(--nav-link-spacing-horizontal);<br>
margin-inline-start: var(--nav-link-spacing-horizontal);<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:last-child) ::after {<br>
position: absolute;<br>
width: calc(var(--nav-link-spacing-horizontal) * 2);<br>
-webkit-margin-start: calc(var(--nav-link-spacing-horizontal) / 2);<br>
margin-inline-start: calc(var(--nav-link-spacing-horizontal) / 2);<br>
content: &quot;/&quot;;<br>
color: var(--muted-color);<br>
text-align: center;<br>
}<br>
nav[aria-label=&quot;breadcrumb&quot;] a[aria-current] {<br>
background-color: transparent;<br>
color: inherit;<br>
text-decoration: none;<br>
pointer-events: none;<br>
}<br>
nav [role=&quot;button&quot;] {<br>
margin-right: inherit;<br>
margin-left: inherit;<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
}</p>
<p>aside nav,<br>
aside ol,<br>
aside ul,<br>
aside li {<br>
display: block;<br>
}<br>
aside li {<br>
padding: calc(var(--nav-element-spacing-vertical) * 0.5)<br>
var(--nav-element-spacing-horizontal);<br>
}<br>
aside li a {<br>
display: block;<br>
}<br>
aside li [role=&quot;button&quot;] {<br>
margin: inherit;<br>
}</p>
<p>[dir=&quot;rtl&quot;] nav[aria-label=&quot;breadcrumb&quot;] ul li:not(:last-child) ::after {<br>
content: &quot;\&quot;;<br>
}</p>
<p>/**</p>
<ul>
<li>Progress<br>
*/<br>
progress {<br>
display: inline-block;<br>
vertical-align: baseline;<br>
}</li>
</ul>
<p>progress {<br>
-webkit-appearance: none;<br>
-moz-appearance: none;<br>
display: inline-block;<br>
appearance: none;<br>
width: 100%;<br>
height: 0.5rem;<br>
margin-bottom: calc(var(--spacing) * 0.5);<br>
overflow: hidden;<br>
border: 0;<br>
border-radius: var(--border-radius);<br>
background-color: var(--progress-background-color);<br>
color: var(--progress-color);<br>
}<br>
progress<VPIcon icon="-webkit-progress-bar {
  border-radius: var(--border-radius);
  background: none;
}
progress[value]" />-webkit-progress-value {<br>
background-color: var(--progress-color);<br>
}<br>
progress<VPIcon icon="-moz-progress-bar {
  background-color: var(--progress-color);
}
@media (prefers-reduced-motion: no-preference) {
  progress:indeterminate {
    background: var(--progress-background-color)
      linear-gradient(
        to right,
        var(--progress-color) 30%,
        var(--progress-background-color) 30%
      )
      top left/150% 150% no-repeat;
    animation: progress-indeterminate 1s linear infinite;
  }
  progress:indeterminate[value]" />-webkit-progress-value {<br>
background-color: transparent;<br>
}<br>
progress:indeterminate::-moz-progress-bar {<br>
background-color: transparent;<br>
}<br>
}</p>
<p>@media (prefers-reduced-motion: no-preference) {<br>
[dir=&quot;rtl&quot;] progress:indeterminate {<br>
animation-direction: reverse;<br>
}<br>
}</p>
<p>@keyframes progress-indeterminate {<br>
0% {<br>
background-position: 200% 0;<br>
}<br>
100% {<br>
background-position: -200% 0;<br>
}<br>
}<br>
/**</p>
<ul>
<li>Dropdown ([role=&quot;list&quot;])<br>
*/<br>
details[role=&quot;list&quot;],<br>
li[role=&quot;list&quot;] {<br>
position: relative;<br>
}</li>
</ul>
<p>details[role=&quot;list&quot;] summary + ul,<br>
li[role=&quot;list&quot;] &gt; ul {<br>
display: flex;<br>
z-index: 99;<br>
position: absolute;<br>
top: auto;<br>
right: 0;<br>
left: 0;<br>
flex-direction: column;<br>
margin: 0;<br>
padding: 0;<br>
border: var(--border-width) solid var(--dropdown-border-color);<br>
border-radius: var(--border-radius);<br>
border-top-right-radius: 0;<br>
border-top-left-radius: 0;<br>
background-color: var(--dropdown-background-color);<br>
box-shadow: var(--card-box-shadow);<br>
color: var(--dropdown-color);<br>
white-space: nowrap;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li,<br>
li[role=&quot;list&quot;] &gt; ul li {<br>
width: 100%;<br>
margin-bottom: 0;<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5)<br>
var(--form-element-spacing-horizontal);<br>
list-style: none;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li:first-of-type,<br>
li[role=&quot;list&quot;] &gt; ul li:first-of-type {<br>
margin-top: calc(var(--form-element-spacing-vertical) * 0.5);<br>
}<br>
details[role=&quot;list&quot;] summary + ul li:last-of-type,<br>
li[role=&quot;list&quot;] &gt; ul li:last-of-type {<br>
margin-bottom: calc(var(--form-element-spacing-vertical) * 0.5);<br>
}<br>
details[role=&quot;list&quot;] summary + ul li a,<br>
li[role=&quot;list&quot;] &gt; ul li a {<br>
display: block;<br>
margin: calc(var(--form-element-spacing-vertical) * -0.5)<br>
calc(var(--form-element-spacing-horizontal) * -1);<br>
padding: calc(var(--form-element-spacing-vertical) * 0.5)<br>
var(--form-element-spacing-horizontal);<br>
overflow: hidden;<br>
color: var(--dropdown-color);<br>
text-decoration: none;<br>
text-overflow: ellipsis;<br>
}<br>
details[role=&quot;list&quot;] summary + ul li a:hover,<br>
li[role=&quot;list&quot;] &gt; ul li a:hover {<br>
background-color: var(--dropdown-hover-background-color);<br>
}</p>
<p>details[role=&quot;list&quot;] summary<VPIcon icon="after,
li> a" [role="&quot;list&quot;]" />after {<br>
display: block;<br>
width: 1rem;<br>
height: calc(1rem * var(--line-height, 1.5));<br>
-webkit-margin-start: 0.5rem;<br>
margin-inline-start: 0.5rem;<br>
float: right;<br>
transform: rotate(0deg);<br>
background-position: right center;<br>
background-size: 1rem auto;<br>
background-repeat: no-repeat;<br>
content: &quot;&quot;;<br>
}</p>
<p>details[role=&quot;list&quot;] {<br>
padding: 0;<br>
border-bottom: none;<br>
}<br>
details[role=&quot;list&quot;] summary {<br>
margin-bottom: 0;<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]) {<br>
height: calc(<br>
1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +<br>
var(--border-width) * 2<br>
);<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--form-element-border-color);<br>
border-radius: var(--border-radius);<br>
background-color: var(--form-element-background-color);<br>
color: var(--form-element-placeholder-color);<br>
line-height: inherit;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]):active,<br>
details[role=&quot;list&quot;] summary:not([role]):focus {<br>
border-color: var(--form-element-active-border-color);<br>
background-color: var(--form-element-active-background-color);<br>
}<br>
details[role=&quot;list&quot;] summary:not([role]):focus {<br>
box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);<br>
}<br>
details[role=&quot;list&quot;][open] summary {<br>
border-bottom-right-radius: 0;<br>
border-bottom-left-radius: 0;<br>
}<br>
details[role=&quot;list&quot;][open] summary::before {<br>
display: block;<br>
z-index: 1;<br>
position: fixed;<br>
top: 0;<br>
right: 0;<br>
bottom: 0;<br>
left: 0;<br>
background: none;<br>
content: &quot;&quot;;<br>
cursor: default;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary,<br>
nav li[role=&quot;list&quot;] a {<br>
display: flex;<br>
direction: ltr;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary + ul,<br>
nav li[role=&quot;list&quot;] &gt; ul {<br>
min-width: -moz-fit-content;<br>
min-width: fit-content;<br>
border-radius: var(--border-radius);<br>
}<br>
nav details[role=&quot;list&quot;] summary + ul li a,<br>
nav li[role=&quot;list&quot;] &gt; ul li a {<br>
border-radius: 0;<br>
}</p>
<p>nav details[role=&quot;list&quot;] summary,<br>
nav details[role=&quot;list&quot;] summary:not([role]) {<br>
height: auto;<br>
padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);<br>
}<br>
nav details[role=&quot;list&quot;][open] summary {<br>
border-radius: var(--border-radius);<br>
}<br>
nav details[role=&quot;list&quot;] summary + ul {<br>
margin-top: var(--outline-width);<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
}<br>
nav details[role=&quot;list&quot;] summary[role=&quot;link&quot;] {<br>
margin-bottom: calc(var(--nav-link-spacing-vertical) * -1);<br>
line-height: var(--line-height);<br>
}<br>
nav details[role=&quot;list&quot;] summary[role=&quot;link&quot;] + ul {<br>
margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));<br>
-webkit-margin-start: calc(var(--nav-link-spacing-horizontal) * -1);<br>
margin-inline-start: calc(var(--nav-link-spacing-horizontal) * -1);<br>
}</p>
<p>li[role=&quot;list&quot;]:hover &gt; ul,<br>
li[role=&quot;list&quot;] a:active ~ ul,<br>
li[role=&quot;list&quot;] a:focus ~ ul {<br>
display: flex;<br>
}<br>
li[role=&quot;list&quot;] &gt; ul {<br>
display: none;<br>
margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));<br>
-webkit-margin-start: calc(<br>
var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)<br>
);<br>
margin-inline-start: calc(<br>
var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)<br>
);<br>
}<br>
li[role=&quot;list&quot;] &gt; a::after {<br>
background-image: var(--icon-chevron);<br>
}</p>
<p>/**</p>
<ul>
<li>Loading ([aria-busy=true])<br>
*/<br>
[aria-busy=&quot;true&quot;] {<br>
cursor: progress;<br>
}</li>
</ul>
<p>[aria-busy=&quot;true&quot;]:not(input, select, textarea)<VPIcon icon="before {
  display: inline-block;
  width: 1em;
  height: 1em;
  border: 0.1875em solid currentColor;
  border-radius: 1em;
  border-right-color: transparent;
  content: "";
  vertical-align: text-bottom;
  vertical-align: -0.125em;
  animation: spinner 0.75s linear infinite;
  opacity: var(--loading-spinner-opacity);
}
[select, textarea):not(:empty)" aria-busy="&quot;true&quot;]:not(input," />before {<br>
margin-right: calc(var(--spacing) * 0.5);<br>
margin-left: 0;<br>
-webkit-margin-start: 0;<br>
margin-inline-start: 0;<br>
-webkit-margin-end: calc(var(--spacing) * 0.5);<br>
margin-inline-end: calc(var(--spacing) * 0.5);<br>
}<br>
[aria-busy=&quot;true&quot;]:not(input, select, textarea):empty {<br>
text-align: center;<br>
}</p>
<p>button[aria-busy=&quot;true&quot;],<br>
input[type=&quot;submit&quot;][aria-busy=&quot;true&quot;],<br>
input[type=&quot;button&quot;][aria-busy=&quot;true&quot;],<br>
input[type=&quot;reset&quot;][aria-busy=&quot;true&quot;],<br>
a[aria-busy=&quot;true&quot;] {<br>
pointer-events: none;<br>
}</p>
<p>@keyframes spinner {<br>
to {<br>
transform: rotate(360deg);<br>
}<br>
}<br>
/**</p>
<ul>
<li>Tooltip ([data-tooltip])<br>
*/<br>
[data-tooltip] {<br>
position: relative;<br>
}<br>
[data-tooltip]:not(a, button, input) {<br>
border-bottom: 1px dotted;<br>
text-decoration: none;<br>
cursor: help;<br>
}<br>
[data-tooltip][data-placement=&quot;top&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;top&quot;]" />after,<br>
[data-tooltip]<VPIcon icon="before,
[data-tooltip]" />after {<br>
display: block;<br>
z-index: 99;<br>
position: absolute;<br>
bottom: 100%;<br>
left: 50%;<br>
padding: 0.25rem 0.5rem;<br>
overflow: hidden;<br>
transform: translate(-50%, -0.25rem);<br>
border-radius: var(--border-radius);<br>
background: var(--tooltip-background-color);<br>
content: attr(data-tooltip);<br>
color: var(--tooltip-color);<br>
font-style: normal;<br>
font-weight: var(--font-weight);<br>
font-size: 0.875rem;<br>
text-decoration: none;<br>
text-overflow: ellipsis;<br>
white-space: nowrap;<br>
opacity: 0;<br>
pointer-events: none;<br>
}<br>
[data-tooltip][data-placement=&quot;top&quot;]<VPIcon icon="after,
[data-tooltip]" />after {<br>
padding: 0;<br>
transform: translate(-50%, 0rem);<br>
border-top: 0.3rem solid;<br>
border-right: 0.3rem solid transparent;<br>
border-left: 0.3rem solid transparent;<br>
border-radius: 0;<br>
background-color: transparent;<br>
content: &quot;&quot;;<br>
color: var(--tooltip-background-color);<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;bottom&quot;]" />after {<br>
top: 100%;<br>
bottom: auto;<br>
transform: translate(-50%, 0.25rem);<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:after {<br>
transform: translate(-50%, -0.3rem);<br>
border: 0.3rem solid transparent;<br>
border-bottom: 0.3rem solid;<br>
}<br>
[data-tooltip][data-placement=&quot;left&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;left&quot;]" />after {<br>
top: 50%;<br>
right: 100%;<br>
bottom: auto;<br>
left: auto;<br>
transform: translate(-0.25rem, -50%);<br>
}<br>
[data-tooltip][data-placement=&quot;left&quot;]:after {<br>
transform: translate(0.3rem, -50%);<br>
border: 0.3rem solid transparent;<br>
border-left: 0.3rem solid;<br>
}<br>
[data-tooltip][data-placement=&quot;right&quot;]<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;right&quot;]" />after {<br>
top: 50%;<br>
right: auto;<br>
bottom: auto;<br>
left: 100%;<br>
transform: translate(0.25rem, -50%);<br>
}<br>
[data-tooltip][data-placement=&quot;right&quot;]:after {<br>
transform: translate(-0.3rem, -50%);<br>
border: 0.3rem solid transparent;<br>
border-right: 0.3rem solid;<br>
}<br>
[data-tooltip]:focus<VPIcon icon="before,
[data-tooltip]:focus" />after,<br>
[data-tooltip]:hover<VPIcon icon="before,
[data-tooltip]:hover" />after {<br>
opacity: 1;<br>
}<br>
@media (hover: hover) and (pointer: fine) {<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="before,
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover [data-tooltip]:focus<VPIcon icon="before,
[data-tooltip][[data-tooltip]:focus" data-placement="&quot;bottom&quot;]:hover" />after,<br>
[data-tooltip]:hover<VPIcon icon="before,
[data-tooltip]:hover" />after {<br>
animation-duration: 0.2s;<br>
animation-name: tooltip-slide-top;<br>
}<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="after,
[data-tooltip][[data-tooltip]:focus" data-placement="&quot;bottom&quot;]:hover" />after,<br>
[data-tooltip]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-top;
}
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;bottom&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-bottom;
}
[data-tooltip][" data-placement="&quot;bottom&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;bottom&quot;]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-bottom;
}
[data-tooltip][" data-placement="&quot;left&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;left&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;left&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;left&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-left;
}
[data-tooltip][" data-placement="&quot;left&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;left&quot;]:hover<VPIcon icon="after {
 animation-name: tooltip-caret-slide-left;
}
[data-tooltip][" data-placement="&quot;right&quot;]:focus" />before,<br>
[data-tooltip][data-placement=&quot;right&quot;]:focus<VPIcon icon="after,
[data-tooltip][" data-placement="&quot;right&quot;]:hover" />before,<br>
[data-tooltip][data-placement=&quot;right&quot;]:hover<VPIcon icon="after {
 animation-duration: 0.2s;
 animation-name: tooltip-slide-right;
}
[data-tooltip][" data-placement="&quot;right&quot;]:focus" />after,<br>
[data-tooltip][data-placement=&quot;right&quot;]:hover::after {<br>
animation-name: tooltip-caret-slide-right;<br>
}<br>
}<br>
@keyframes tooltip-slide-top {<br>
from {<br>
transform: translate(-50%, 0.75rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, -0.25rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-top {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-50%, -0.25rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, 0rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-bottom {<br>
from {<br>
transform: translate(-50%, -0.75rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, 0.25rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-bottom {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-50%, -0.5rem);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-50%, -0.3rem);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-left {<br>
from {<br>
transform: translate(0.75rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-0.25rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-left {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(0.05rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(0.3rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-slide-right {<br>
from {<br>
transform: translate(-0.75rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(0.25rem, -50%);<br>
opacity: 1;<br>
}<br>
}<br>
@keyframes tooltip-caret-slide-right {<br>
from {<br>
opacity: 0;<br>
}<br>
50% {<br>
transform: translate(-0.05rem, -50%);<br>
opacity: 0;<br>
}<br>
to {<br>
transform: translate(-0.3rem, -50%);<br>
opacity: 1;<br>
}<br>
}</li>
</ul>
<p>/**</p>
<ul>
<li>Accessibility &amp; User interaction<br>
*/<br>
[aria-controls] {<br>
cursor: pointer;<br>
}</li>
</ul>
<p>[aria-disabled=&quot;true&quot;],<br>
[disabled] {<br>
cursor: not-allowed;<br>
}</p>
<p>[aria-hidden=&quot;false&quot;][hidden] {<br>
display: initial;<br>
}</p>
<p>[aria-hidden=&quot;false&quot;][hidden]:not(:focus) {<br>
clip: rect(0, 0, 0, 0);<br>
position: absolute;<br>
}</p>
<p>a,<br>
area,<br>
button,<br>
input,<br>
label,<br>
select,<br>
summary,<br>
textarea,<br>
[tabindex] {<br>
-ms-touch-action: manipulation;<br>
}</p>
<p>[dir=&quot;rtl&quot;] {<br>
direction: rtl;<br>
}</p>
<p>/**</p>
<ul>
<li>Reduce Motion Features<br>
*/<br>
@media (prefers-reduced-motion: reduce) {<br>
*:not([aria-busy=&quot;true&quot;]),<br>
:not([aria-busy=&quot;true&quot;])<VPIcon icon="before,
:not([" aria-busy="&quot;true&quot;])" />after {<br>
background-attachment: initial !important;<br>
animation-duration: 1ms !important;<br>
animation-delay: -1ms !important;<br>
animation-iteration-count: 1 !important;<br>
scroll-behavior: auto !important;<br>
transition-delay: 0s !important;<br>
transition-duration: 0s !important;<br>
}<br>
}</li>
</ul>
<p>#mount {<br>
/* --primary: rgb(227, 59, 126); */<br>
--primary: #ea4c89;<br>
--primary-hover: #f082ac;<br>
--icon-xia: url(&quot;data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgaWQ9IkZyYW1lIj4KPHBhdGggaWQ9IlZlY3RvciIgZD0iTTguMDAyOTEgOS42Nzk4M0wzLjgzMzM5IDUuNTEyMjFMMy4wMjUzOSA2LjMxOTgzTDguMDAzMjkgMTEuMjk1MUwxMi45NzYyIDYuMzE5ODNMMTIuMTY3OSA1LjUxMjIxTDguMDAyOTEgOS42Nzk4M1oiIGZpbGw9IiM4MzgzODMiLz4KPC9nPgo8L3N2Zz4K&quot;);<br>
--switch-checked-background-color: var(--primary);<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--primary: #e23c7c;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>[data-theme=&quot;dark&quot;] {<br>
--primary: #e23c7c;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>[data-theme=&quot;light&quot;] {<br>
--primary: #ea4c89;<br>
--primary-hover: #f082ac;<br>
}</p>
<p>li.select-link.select-link:hover &gt; ul {<br>
display: none;<br>
}<br>
li.select-link.select-link &gt; ul {<br>
display: none;<br>
}<br>
li.select-link.select-link a:focus ~ ul {<br>
display: none;<br>
}</p>
<p>li.select-link.select-link a:active ~ ul {<br>
display: none;<br>
}<br>
li.select-link-active.select-link-active &gt; ul {<br>
display: flex;<br>
}<br>
li.select-link-active.select-link-active:hover &gt; ul {<br>
display: flex;<br>
}</p>
<p>li.select-link-active.select-link-active a:focus ~ ul {<br>
display: flex;<br>
}</p>
<p>li.select-link-active.select-link-active a:active ~ ul {<br>
display: flex;<br>
}<br>
ul.select-link-ul.select-link-ul {<br>
right: 0px;<br>
left: auto;<br>
}</p>
<p>a.select-link-selected {<br>
background-color: var(--primary-focus);<br>
}<br>
.immersive-translate-no-select {<br>
-webkit-touch-callout: none; /* iOS Safari <em>/<br>
-webkit-user-select: none; /</em> Safari <em>/<br>
-khtml-user-select: none; /</em> Konqueror HTML <em>/<br>
-moz-user-select: none; /</em> Old versions of Firefox <em>/<br>
-ms-user-select: none; /</em> Internet Explorer/Edge */<br>
user-select: none;<br>
}</p>
<p>/* li[role=&quot;list&quot;].no-arrow &gt; a<VPIcon icon="after { */
  background-image: none; */
/*   width: 0; */
/*   color: var(--color); */
/* } */
li{
  margin-left: 8px;
  padding-right: 0;
}
li> a" [role="&quot;list&quot;]" color="*" />after {<br>
-webkit-margin-start: 0.2rem;<br>
margin-inline-start: 0.2rem;<br>
}</p>
<p>li[role=&quot;list&quot;].no-arrow &gt; a,<br>
li[role=&quot;list&quot;].no-arrow &gt; a:link,<br>
li[role=&quot;list&quot;].no-arrow &gt; a:visited {<br>
color: var(--secondary);<br>
}</p>
<p>select.min-select {<br>
--form-element-spacing-horizontal: 0;<br>
margin-bottom: 4px;<br>
max-width: 128px;<br>
overflow: hidden;<br>
color: var(--primary);<br>
font-size: 13px;<br>
border: none;<br>
padding: 0;<br>
padding-right: 20px;<br>
padding-left: 8px;<br>
text-overflow: ellipsis;<br>
color: var(--color);<br>
}<br>
select.min-select-secondary {<br>
color: var(--color);<br>
}<br>
select.min-select:focus {<br>
outline: none;<br>
border: none;<br>
--box-shadow: none;<br>
}<br>
select.min-select-no-arrow {<br>
background-image: none;<br>
padding-right: 0;<br>
}</p>
<p>select.min-select-left {<br>
padding-right: 0px;<br>
/* padding-left: 24px; <em>/<br>
/</em> background-position: center left 0; */<br>
text-overflow: ellipsis;<br>
text-align: left;<br>
}</p>
<p>.muted {<br>
color: var(--muted-color);<br>
}</p>
<p>.select.button-select {<br>
--background-color: var(--secondary-hover);<br>
--border-color: var(--secondary-hover);<br>
--color: var(--secondary-inverse);<br>
cursor: pointer;<br>
--box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));<br>
padding: var(--form-element-spacing-vertical)<br>
var(--form-element-spacing-horizontal);<br>
border: var(--border-width) solid var(--border-color);<br>
border-radius: var(--border-radius);<br>
outline: none;<br>
background-color: var(--background-color);<br>
box-shadow: var(--box-shadow);<br>
color: var(--color);<br>
font-weight: var(--font-weight);<br>
font-size: 16px;<br>
line-height: var(--line-height);<br>
text-align: center;<br>
cursor: pointer;<br>
transition: background-color var(--transition), border-color var(--transition),<br>
color var(--transition), box-shadow var(--transition);<br>
-webkit-appearance: button;<br>
margin: 0;<br>
margin-bottom: 0px;<br>
overflow: visible;<br>
font-family: inherit;<br>
text-transform: none;<br>
}</p>
<p>body {<br>
padding: 0;<br>
margin: 0 auto;<br>
min-width: 268px;<br>
border-radius: 10px;<br>
}</p>
<p>.popup-container {<br>
font-size: 16px;<br>
--font-size: 16px;<br>
color: #666;<br>
background-color: var(--popup-footer-background-color);<br>
width: 316px;<br>
min-width: 316px;<br>
}</p>
<p>.popup-content {<br>
background-color: var(--popup-content-background-color);<br>
border-radius: 0px 0px 12px 12px;<br>
padding: 16px 20px;<br>
}</p>
<p>.immersive-translate-popup-overlay {<br>
position: fixed;<br>
top: 0;<br>
left: 0;<br>
height: 100%;<br>
width: 100%;<br>
touch-action: none;<br>
}</p>
<p>.immersive-translate-popup-wrapper {<br>
background: var(--background-color);<br>
border-radius: 10px;<br>
border: 1px solid var(--muted-border-color);<br>
}</p>
<p>#mount {<br>
--font-family: system-ui, -apple-system, &quot;Segoe UI&quot;, &quot;Roboto&quot;, &quot;Ubuntu&quot;,<br>
&quot;Cantarell&quot;, &quot;Noto Sans&quot;, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;,<br>
&quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;;<br>
--line-height: 1.5;<br>
--font-weight: 400;<br>
--font-size: 16px;<br>
--border-radius: 4px;<br>
--border-width: 1px;<br>
--outline-width: 3px;<br>
--spacing: 16px;<br>
--typography-spacing-vertical: 24px;<br>
--block-spacing-vertical: calc(var(--spacing) * 2);<br>
--block-spacing-horizontal: var(--spacing);<br>
--grid-spacing-vertical: 0;<br>
--grid-spacing-horizontal: var(--spacing);<br>
--form-element-spacing-vertical: 12px;<br>
--form-element-spacing-horizontal: 16px;<br>
--nav-element-spacing-vertical: 16px;<br>
--nav-element-spacing-horizontal: 8px;<br>
--nav-link-spacing-vertical: 8px;<br>
--nav-link-spacing-horizontal: 8px;<br>
--form-label-font-weight: var(--font-weight);<br>
--transition: 0.2s ease-in-out;<br>
--modal-overlay-backdrop-filter: blur(4px);<br>
}</p>
<p>[data-theme=&quot;light&quot;],<br>
#mount:not([data-theme=&quot;dark&quot;]) {<br>
--popup-footer-background-color: #e8eaeb;<br>
--popup-content-background-color: #ffffff;<br>
--popup-item-background-color: #f3f5f6;<br>
--popup-item-hover-background-color: #eaeced;<br>
--popup-trial-pro-background-color: #f9fbfc;<br>
--text-black-2: #222222;<br>
--text-gray-2: #222222;<br>
--text-gray-6: #666666;<br>
--text-gray-9: #999999;<br>
--text-gray-c2: #c2c2c2;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(75, 76, 77, 0.2);<br>
--service-select-border-color: #fafafa;<br>
--service-select-selected-background-color: #f3f5f6;<br>
--download-app-background: #f3f5f6;<br>
}</p>
<p>@media only screen and (prefers-color-scheme: dark) {<br>
#mount:not([data-theme=&quot;light&quot;]) {<br>
--popup-footer-background-color: #0d0d0d;<br>
--popup-content-background-color: #191919;<br>
--popup-item-background-color: #272727;<br>
--popup-item-hover-background-color: #333333;<br>
--popup-trial-pro-background-color: #222222;<br>
--text-black-2: #ffffff;<br>
--text-gray-2: #dbdbdb;<br>
--text-gray-6: #b3b3b3;<br>
--text-gray-9: #777777;<br>
--text-gray-c2: #5b5b5b;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);<br>
--service-select-border-color: #2c2c2c;<br>
--service-select-selected-background-color: #333333;<br>
--download-app-background: #333;<br>
}<br>
}</p>
<p>[data-theme=&quot;dark&quot;] {<br>
--popup-footer-background-color: #0d0d0d;<br>
--popup-content-background-color: #191919;<br>
--popup-item-background-color: #272727;<br>
--popup-item-hover-background-color: #333333;<br>
--popup-trial-pro-background-color: #222222;<br>
--text-black-2: #ffffff;<br>
--text-gray-2: #dbdbdb;<br>
--text-gray-6: #b3b3b3;<br>
--text-gray-9: #777777;<br>
--text-gray-c2: #5b5b5b;<br>
--service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);<br>
--service-select-border-color: #2c2c2c;<br>
--service-select-selected-background-color: #333333;<br>
--download-app-background: #333;<br>
}</p>
<p>.text-balck {<br>
color: var(--text-black-2);<br>
}</p>
<p>.text-gray-2 {<br>
color: var(--text-gray-2);<br>
}</p>
<p>.text-gray-6 {<br>
color: var(--text-gray-6);<br>
}</p>
<p>.text-gray-9 {<br>
color: var(--text-gray-9);<br>
}</p>
<p>.text-gray-c2 {<br>
color: var(--text-gray-c2);<br>
}</p>
<p>#mount {<br>
min-width: 268px;<br>
}</p>
<p>.main-button {<br>
font-size: 15px;<br>
vertical-align: middle;<br>
border-radius: 12px;<br>
padding: unset;<br>
height: 44px;<br>
line-height: 44px;<br>
}</p>
<p>.pt-4 {<br>
padding-top: 16px;<br>
}</p>
<p>.p-2 {<br>
padding: 8px;<br>
}</p>
<p>.pl-5 {<br>
padding-left: 48px;<br>
}</p>
<p>.p-0 {<br>
padding: 0;<br>
}</p>
<p>.pl-2 {<br>
padding-left: 8px;<br>
}</p>
<p>.pl-4 {<br>
padding-left: 24px;<br>
}</p>
<p>.pt-2 {<br>
padding-top: 8px;<br>
}</p>
<p>.pb-2 {<br>
padding-bottom: 8px;<br>
}</p>
<p>.pb-4 {<br>
padding-bottom: 16px;<br>
}</p>
<p>.pb-5 {<br>
padding-bottom: 20px;<br>
}</p>
<p>.pr-5 {<br>
padding-right: 48px;<br>
}</p>
<p>.text-sm {<br>
font-size: 13px;<br>
}</p>
<p>.text-base {<br>
font-size: 16px;<br>
}</p>
<p>.w-full {<br>
width: 100%;<br>
}</p>
<p>.flex {<br>
display: flex;<br>
}</p>
<p>.flex-row {<br>
flex-direction: row;<br>
}</p>
<p>.flex-wrap {<br>
flex-wrap: wrap;<br>
}</p>
<p>.flex-end {<br>
justify-content: flex-end;<br>
}</p>
<p>.flex-grow {<br>
flex-grow: 1;<br>
}</p>
<p>.justify-between {<br>
justify-content: space-between;<br>
}</p>
<p>.mb-0 {<br>
margin-bottom: 0px;<br>
}</p>
<p>.mb-2 {<br>
margin-bottom: 8px;<br>
}</p>
<p>.mb-4 {<br>
margin-bottom: 16px;<br>
}</p>
<p>.mb-3 {<br>
margin-bottom: 12px;<br>
}</p>
<p>.inline-block {<br>
display: inline-block;<br>
}</p>
<p>.py-2 {<br>
padding-top: 8px;<br>
padding-bottom: 8px;<br>
}</p>
<p>.py-2-5 {<br>
padding-top: 6px;<br>
padding-bottom: 6px;<br>
}</p>
<p>.mt-0 {<br>
margin-top: 0;<br>
}</p>
<p>.mt-2 {<br>
margin-top: 8px;<br>
}</p>
<p>.mt-3 {<br>
margin-top: 12px;<br>
}</p>
<p>.mt-4 {<br>
margin-top: 16px;<br>
}</p>
<p>.mt-5 {<br>
margin-top: 20px;<br>
}</p>
<p>.mt-6 {<br>
margin-top: 24px;<br>
}</p>
<p>.mb-1 {<br>
margin-bottom: 4px;<br>
}</p>
<p>.ml-4 {<br>
margin-left: 24px;<br>
}</p>
<p>.ml-3 {<br>
margin-left: 16px;<br>
}</p>
<p>.ml-2 {<br>
margin-left: 8px;<br>
}</p>
<p>.ml-1 {<br>
margin-left: 4px;<br>
}</p>
<p>.mr-1 {<br>
margin-right: 4px;<br>
}</p>
<p>.mr-2 {<br>
margin-right: 8px;<br>
}</p>
<p>.mr-3 {<br>
margin-right: 16px;<br>
}</p>
<p>.mx-2 {<br>
margin-left: 8px;<br>
margin-right: 8px;<br>
}</p>
<p>.pl-3 {<br>
padding-left: 12px;<br>
}</p>
<p>.pr-3 {<br>
padding-right: 12px;<br>
}</p>
<p>.p-3 {<br>
padding: 12px;<br>
}</p>
<p>.px-1 {<br>
padding-left: 4px;<br>
padding-right: 4px;<br>
}</p>
<p>.px-3 {<br>
padding-left: 12px;<br>
padding-right: 12px;<br>
}</p>
<p>.pt-3 {<br>
padding-top: 12px;<br>
}</p>
<p>.px-6 {<br>
padding-left: 18px;<br>
padding-right: 18px;<br>
}</p>
<p>.px-4 {<br>
padding-left: 16px;<br>
padding-right: 16px;<br>
}</p>
<p>.pt-6 {<br>
padding-top: 20px;<br>
}</p>
<p>.py-3 {<br>
padding-top: 12px;<br>
padding-bottom: 12px;<br>
}</p>
<p>.py-0 {<br>
padding-top: 0;<br>
padding-bottom: 0;<br>
}</p>
<p>.left-auto {<br>
left: auto !important;<br>
}</p>
<p>.max-h-28 {<br>
max-height: 112px;<br>
}</p>
<p>.max-h-30 {<br>
max-height: 120px;<br>
}</p>
<p>.overflow-y-scroll {<br>
overflow-y: scroll;<br>
}</p>
<p>.text-xs {<br>
font-size: 12px;<br>
}</p>
<p>.flex-1 {<br>
flex: 1;<br>
}</p>
<p>.flex-3 {<br>
flex: 3;<br>
}</p>
<p>.flex-4 {<br>
flex: 4;<br>
}</p>
<p>.flex-2 {<br>
flex: 2;<br>
}</p>
<p>.items-center {<br>
align-items: center;<br>
}</p>
<p>.max-content {<br>
width: max-content;<br>
}</p>
<p>.justify-center {<br>
justify-content: center;<br>
}</p>
<p>.items-end {<br>
align-items: flex-end;<br>
}</p>
<p>.items-baseline {<br>
align-items: baseline;<br>
}</p>
<p>.my-5 {<br>
margin-top: 48px;<br>
margin-bottom: 48px;<br>
}</p>
<p>.my-4 {<br>
margin-top: 24px;<br>
margin-bottom: 24px;<br>
}</p>
<p>.my-3 {<br>
margin-top: 16px;<br>
margin-bottom: 16px;<br>
}</p>
<p>.pt-3 {<br>
padding-top: 12px;<br>
}</p>
<p>.px-3 {<br>
padding-left: 12px;<br>
padding-right: 12px;<br>
}</p>
<p>.pt-2 {<br>
padding-top: 8px;<br>
}</p>
<p>.px-2 {<br>
padding-left: 8px;<br>
padding-right: 8px;<br>
}</p>
<p>.pt-1 {<br>
padding-top: 4px;<br>
}</p>
<p>.px-1 {<br>
padding-left: 4px;<br>
padding-right: 4px;<br>
}</p>
<p>.pb-2 {<br>
padding-bottom: 8px;<br>
}</p>
<p>.justify-end {<br>
justify-content: flex-end;<br>
}</p>
<p>.w-auto {<br>
width: auto;<br>
}</p>
<p>.shrink-0 {<br>
flex-shrink: 0;<br>
}</p>
<p>select.language-select,<br>
select.translate-service,<br>
select.min-select {<br>
--form-element-spacing-horizontal: 0;<br>
margin-bottom: 0px;<br>
max-width: unset;<br>
flex: 1;<br>
overflow: hidden;<br>
font-size: 13px;<br>
border: none;<br>
border-radius: 8px;<br>
padding-right: 30px;<br>
padding-left: 0px;<br>
background-position: center right 12px;<br>
background-size: 16px auto;<br>
background-image: var(--icon-xia);<br>
text-overflow: ellipsis;<br>
color: var(--text-gray-2);<br>
background-color: transparent;<br>
box-shadow: unset !important;<br>
cursor: pointer;<br>
}</p>
<p>select.more {<br>
background-position: center right;<br>
padding-right: 20px;<br>
}</p>
<p>select.transform-padding-left {<br>
padding-left: 12px;<br>
transform: translateX(-12px);<br>
background-position: center right 0px;<br>
}</p>
<p>select.translate-service {<br>
color: var(--text-black-2);<br>
}</p>
<p>.min-select-container.disabled {<br>
opacity: 0.5;<br>
pointer-events: none;<br>
}</p>
<p>/* dark use black, for windows */<br>
@media (prefers-color-scheme: dark) {<br>
select.language-select option,<br>
select.translate-service option,<br>
select.min-select option {<br>
background-color: #666666;<br>
}<br>
}</p>
<p>.text-overflow-ellipsis {<br>
text-overflow: ellipsis;<br>
overflow: hidden;<br>
white-space: nowrap;<br>
}</p>
<p>.max-w-20 {<br>
max-width: 180px;<br>
white-space: nowrap;<br>
}</p>
<p>select.min-select-secondary {<br>
color: var(--color);<br>
}</p>
<p>select.min-select:focus {<br>
outline: none;<br>
border: none;<br>
--box-shadow: none;<br>
}</p>
<p>select.min-select-no-arrow {<br>
background-image: none;<br>
padding-right: 0;<br>
}</p>
<p>select.min-select-left {<br>
padding-right: 0px;<br>
/* padding-left: 24px; <em>/<br>
/</em> background-position: center left 0; */<br>
text-overflow: ellipsis;<br>
text-align: left;<br>
}</p>
<p>.popup-footer {<br>
background-color: var(--popup-footer-background-color);<br>
height: 40px;<br>
}</p>
<p>.text-right {<br>
text-align: right;<br>
}</p>
<p>.clickable {<br>
cursor: pointer;<br>
}</p>
<p>.close {<br>
cursor: pointer;<br>
width: 16px;<br>
height: 16px;<br>
background-image: var(--icon-close);<br>
background-position: center;<br>
background-size: auto 1rem;<br>
background-repeat: no-repeat;<br>
opacity: 0.5;<br>
transition: opacity var(--transition);<br>
}</p>
<p>.padding-two-column {<br>
padding-left: 40px;<br>
padding-right: 40px;<br>
}</p>
<p>.muted {<br>
color: #999;<br>
}</p>
<p>.text-label {<br>
color: #666;<br>
}</p>
<p>.display-none {<br>
display: none;<br>
}</p>
<p>/* dark use #18232c */<br>
@media (prefers-color-scheme: dark) {<br>
.text-label {<br>
color: #9ca3af;<br>
}<br>
}</p>
<p>.text-decoration-none {<br>
text-decoration: none;<br>
}</p>
<p>.text-decoration-none:is([aria-current], :hover, :active, :focus),<br>
[role=&quot;link&quot;]:is([aria-current], :hover, :active, :focus) {<br>
--text-decoration: none !important;<br>
background-color: transparent !important;<br>
}</p>
<p>.language-select-container {<br>
position: relative;<br>
width: 100%;<br>
background-color: var(--popup-item-background-color);<br>
height: 55px;<br>
border-radius: 12px;<br>
}</p>
<p>select.language-select {<br>
color: var(--text-black-2);<br>
font-size: 14px;<br>
padding: 8px 24px 24px 16px;<br>
position: absolute;<br>
border-radius: 12px;<br>
position: absolute;<br>
left: 0;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
}</p>
<p>select.text-gray-6 {<br>
color: var(--text-gray-6);<br>
}</p>
<p>.language-select-container label {<br>
position: absolute;<br>
bottom: 10px;<br>
left: 16px;<br>
font-size: 12px;<br>
color: var(--text-gray-9);<br>
line-height: 12px;<br>
margin: 0;<br>
}</p>
<p>.translation-service-container {<br>
background-color: var(--popup-item-background-color);<br>
border-radius: 12px;<br>
}</p>
<p>.min-select-container {<br>
display: flex;<br>
justify-content: space-between;<br>
align-items: center;<br>
height: 44px;<br>
background-color: var(--popup-item-background-color);<br>
padding-left: 16px;<br>
}</p>
<p>.min-select-container:first-child {<br>
border-top-left-radius: 10px;<br>
border-top-right-radius: 10px;<br>
}</p>
<p>.min-select-container:last-child {<br>
border-bottom-left-radius: 10px;<br>
border-bottom-right-radius: 10px;<br>
}</p>
<p>.min-select-container:only-child {<br>
border-radius: 10px;<br>
}</p>
<p>.translate-mode {<br>
width: 44px;<br>
height: 44px;<br>
border-radius: 22px;<br>
background-color: var(--popup-item-background-color);<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
flex-shrink: 0;<br>
cursor: pointer;<br>
}</p>
<p>.translate-mode svg {<br>
fill: var(--text-gray-2);<br>
}</p>
<p>.widgets-container {<br>
display: flex;<br>
align-items: stretch;<br>
justify-content: space-between;<br>
width: 100%;<br>
gap: 9px;<br>
}</p>
<p>/* 当只有两个小组件时的样式优化 */<br>
.widgets-container.widgets-two-items {<br>
gap: 16px;<br>
}</p>
<p>.widgets-container.widgets-two-items .widget-item {<br>
flex: 0 1 auto;<br>
min-width: 93px;<br>
max-width: 120px;<br>
}</p>
<p>.widget-item {<br>
display: flex;<br>
max-width: 93px;<br>
flex-direction: row;<br>
align-items: center;<br>
justify-content: center;<br>
background-color: var(--popup-item-background-color);<br>
font-size: 12px;<br>
min-height: 44px;<br>
height: 100%;<br>
border-radius: 8px;<br>
cursor: pointer;<br>
flex: 1;<br>
padding: 8px 4px;<br>
text-align: center;<br>
}</p>
<p>.widget-icon-text {<br>
white-space: nowrap;<br>
overflow: hidden;<br>
text-overflow: ellipsis;<br>
color: var(--text-gray-2);<br>
}</p>
<p>.widgets-container svg {<br>
fill: var(--text-gray-2);<br>
color: var(--text-gray-2);<br>
}</p>
<p>.share-button-container {<br>
display: flex;<br>
align-items: center;<br>
cursor: pointer;<br>
padding: 2px 3px 0 8px;<br>
}</p>
<p>.share-button-container svg {<br>
fill: var(--text-gray-9);<br>
}</p>
<p>.min-select-container:hover,<br>
.language-select-container:hover,<br>
.widget-item:hover,<br>
.translate-mode:hover {<br>
background-color: var(--popup-item-hover-background-color);<br>
}</p>
<p>.main-button:hover {<br>
background-color: #f5508f;<br>
}</p>
<p>.share-button-container:hover {<br>
background-color: var(--popup-item-background-color);<br>
border-radius: 6px;<br>
}</p>
<p>.error-boundary {<br>
background: #fff2f0;<br>
border: 1px solid #ffccc7;<br>
display: flex;<br>
padding: 12px;<br>
font-size: 14px;<br>
color: rgba(0, 0, 0, 0.88);<br>
word-break: break-all;<br>
margin: 12px;<br>
border-radius: 12px;<br>
flex-direction: column;<br>
}</p>
<p>.upgrade-pro {<br>
border-radius: 11px;<br>
background: linear-gradient(57deg, #272727 19.8%, #696969 82.2%);<br>
padding: 2px 8px;<br>
transform: scale(0.85);<br>
}</p>
<p>.upgrade-pro span {<br>
background: linear-gradient(180deg, #ffeab4 17.65%, #f8c235 85.29%);<br>
background-clip: text;<br>
-webkit-background-clip: text;<br>
-webkit-text-fill-color: transparent;<br>
font-size: 12px;<br>
margin-left: 4px;<br>
}</p>
<p>.upgrade-pro svg {<br>
margin-top: -2px;<br>
}</p>
<p>.upgrade-pro:hover {<br>
background: linear-gradient(57deg, #3d3d3d 19.8%, #949494 82.2%);<br>
}</p>
<p>.border-bottom-radius-0 {<br>
border-bottom-left-radius: 0 !important;<br>
border-bottom-right-radius: 0 !important;<br>
}</p>
<p>.trial-pro-container {<br>
border-radius: 0px 0px 12px 12px;<br>
background: var(--popup-trial-pro-background-color);<br>
display: flex;<br>
align-items: center;<br>
height: 44px;<br>
padding-left: 16px;<br>
padding-right: 12px;<br>
font-size: 12px;<br>
}</p>
<p>.trial-pro-container label {<br>
line-height: 13px;<br>
color: var(--text-black-2);<br>
}</p>
<p>.trial-pro-container img {<br>
margin-left: 5px;<br>
}</p>
<p>.cursor-pointer {<br>
cursor: pointer;<br>
}</p>
<p>.upgrade-pro-discount-act {<br>
height: 25px;<br>
display: flex;<br>
padding: 0 4px;<br>
align-items: center;<br>
border-radius: 15px;<br>
background: linear-gradient(<br>
90deg,<br>
#cefbfa 11.33%,<br>
#d7f56f 63.75%,<br>
#fccd5e 100%<br>
);<br>
transform: scale(0.9);<br>
box-shadow: 0px 1.8px 3.6px 0px rgba(0, 0, 0, 0.1);<br>
cursor: pointer;<br>
}</p>
<p>.upgrade-pro-discount-act span {<br>
font-size: 12px;<br>
font-weight: 700;<br>
margin-left: 4px;<br>
color: #222222;<br>
}</p>
<p>.upgrade-pro-discount-act:hover {<br>
text-decoration: unset;<br>
background: linear-gradient(<br>
90deg,<br>
#e2fffe 11.33%,<br>
#e6ff91 63.75%,<br>
#ffdf93 100%<br>
);<br>
}</p>
<p>.custom-select-container {<br>
width: 200px;<br>
position: relative;<br>
flex: 1;<br>
}</p>
<p>#translation-service-select {<br>
padding-right: 12px;<br>
padding-left: 6px;<br>
}</p>
<p>.custom-select-content {<br>
border-radius: 12px;<br>
background: var(--popup-content-background-color);<br>
box-shadow: var(--service-select-content-shadow);<br>
border: 1px solid var(--service-select-border-color);<br>
padding: 4px 5px;<br>
position: absolute;<br>
left: -10px;<br>
right: 0;<br>
z-index: 100;<br>
overflow-y: auto;<br>
}</p>
<p>.custom-select-item.default {<br>
width: 100%;<br>
padding: 0;<br>
}</p>
<p>.custom-select-item {<br>
font-size: 13px;<br>
padding: 5px 6px;<br>
border-radius: 8px;<br>
display: flex;<br>
align-items: center;<br>
cursor: pointer;<br>
color: var(--text-black-2);<br>
width: auto;<br>
overflow: hidden;<br>
height: 30px;<br>
line-height: 30px;<br>
}</p>
<p>.custom-select-item-img {<br>
width: 20px;<br>
height: 20px;<br>
margin-right: 4px;<br>
}</p>
<p>@media (prefers-color-scheme: dark) {<br>
.custom-select-item-img {<br>
margin-right: 6px;<br>
}<br>
}</p>
<p>.custom-select-content .custom-select-item.selected,<br>
.custom-select-content .custom-select-item:hover {<br>
background: var(--service-select-selected-background-color);<br>
}</p>
<p>.custom-select-item &gt; span {<br>
white-space: nowrap;<br>
overflow: hidden;<br>
text-overflow: ellipsis;<br>
}</p>
<p>.custom-select-item-pro {<br>
font-size: 12px;<br>
margin-left: 6px;<br>
display: flex;<br>
}</p>
<p>.custom-select-item-pro img {<br>
margin: 0 3px;<br>
width: 20px;<br>
flex-shrink: 0;<br>
}</p>
<p>.custom-select-group-header {<br>
font-size: 12px;<br>
font-weight: 500;<br>
color: var(--text-gray-9);<br>
padding: 6px 8px 4px;<br>
margin-top: 2px;<br>
text-transform: uppercase;<br>
letter-spacing: 0.5px;<br>
}</p>
<p>.more-container {<br>
position: relative;<br>
}</p>
<p>.new-menu-indicator {<br>
position: absolute;<br>
width: 8px;<br>
height: 8px;<br>
background-color: #ef3434;<br>
border-radius: 50%;<br>
right: 18px;<br>
top: 4px;<br>
}</p>
<p>.download-app {<br>
display: inline-flex;<br>
align-items: center;<br>
gap: 4px;<br>
border-radius: 8px;<br>
background: var(--download-app-background);<br>
padding: 4px 8px;<br>
color: var(--text-gray-6);<br>
font-size: 12px;<br>
cursor: pointer;<br>
transition: all 0.2s ease-in-out;<br>
}</p>
<p>/* Popup 动画效果 */<br>
@keyframes popup-fade-in {<br>
from {<br>
opacity: 0;<br>
transform: translateY(10px) scale(0.95);<br>
}<br>
to {<br>
opacity: 1;<br>
transform: translateY(0) scale(1);<br>
}<br>
}</p>
<p>@keyframes popup-fade-out {<br>
from {<br>
opacity: 1;<br>
transform: translateY(0) scale(1);<br>
}<br>
to {<br>
opacity: 0;<br>
transform: translateY(10px) scale(0.95);<br>
}<br>
}</p>
<p>.popup-generic-content {<br>
animation: popup-fade-in 0.2s ease-out;<br>
}</p>
<p>.popup-generic-content.hiding {<br>
animation: popup-fade-out 0.15s ease-in;<br>
}</p>
<p>html {<br>
font-size: 17px;<br>
}</p>
<p>@media print {<br>
.imt-fb-container {<br>
display: none !important;<br>
}<br>
}</p>
<p>#mount#mount {<br>
position: absolute;<br>
display: none;<br>
min-width: 250px;<br>
height: auto;<br>
--font-size: 17px;<br>
font-size: 17px;<br>
}</p>
<p>/* float-ball */<br>
.imt-fb-container {<br>
position: fixed;<br>
padding: 0;<br>
top: 335px;<br>
width: fit-content;<br>
display: flex;<br>
flex-direction: column;<br>
display: none;<br>
direction: ltr;<br>
}</p>
<p>.imt-fb-container.left {<br>
align-items: flex-start;<br>
left: 0;<br>
}</p>
<p>.imt-fb-container.right {<br>
align-items: flex-end;<br>
right: 0;<br>
}</p>
<p>.imt-fb-btn {<br>
cursor: pointer;<br>
background: var(--float-ball-more-button-background-color);<br>
height: 36px;<br>
width: 56px;<br>
box-shadow: 2px 6px 10px 0px #0e121629;<br>
}</p>
<p>.imt-fb-btn.left {<br>
border-top-right-radius: 36px;<br>
border-bottom-right-radius: 36px;<br>
}</p>
<p>.imt-fb-btn.right {<br>
border-top-left-radius: 36px;<br>
border-bottom-left-radius: 36px;<br>
}</p>
<p>.imt-fb-btn div {<br>
background: var(--float-ball-more-button-background-color);<br>
height: 36px;<br>
width: 54px;<br>
display: flex;<br>
align-items: center;<br>
}</p>
<p>.imt-fb-btn.left div {<br>
border-top-right-radius: 34px;<br>
border-bottom-right-radius: 34px;<br>
justify-content: flex-end;<br>
}</p>
<p>.imt-fb-btn.right div {<br>
border-top-left-radius: 34px;<br>
border-bottom-left-radius: 34px;<br>
}</p>
<p>.imt-fb-logo-img {<br>
width: 20px;<br>
height: 20px;<br>
margin: 0 10px;<br>
}</p>
<p>.imt-fb-logo-img-big-bg {<br>
width: 28px;<br>
height: 28px;<br>
margin: 0;<br>
padding: 4px;<br>
background-color: #ed6d8f;<br>
border-radius: 50%;<br>
margin: 0 5px;<br>
}</p>
<p>.imt-float-ball-translated {<br>
position: absolute;<br>
width: 11px;<br>
height: 11px;<br>
bottom: 4px;<br>
right: 20px;<br>
}</p>
<p>.btn-animate {<br>
-webkit-transform: translate3d(0, 0, 0);<br>
transform: translate3d(0, 0, 0);<br>
-webkit-transition: -webkit-transform ease-out 250ms;<br>
transition: -webkit-transform ease-out 250ms;<br>
transition: transform ease-out 250ms;<br>
transition: transform ease-out 250ms, -webkit-transform ease-out 250ms;<br>
}</p>
<p>.imt-fb-setting-btn {<br>
margin-right: 18px;<br>
width: 28px;<br>
height: 28px;<br>
}</p>
<p>.immersive-translate-popup-wrapper {<br>
background: var(--background-color);<br>
border-radius: 20px;<br>
box-shadow: 2px 10px 24px 0px #0e121614;<br>
border: none;<br>
}</p>
<p>.popup-container {<br>
border-radius: 20px;<br>
}</p>
<p>.popup-content {<br>
border-radius: 20px 20px 12px 12px;<br>
}<br>
.popup-footer {<br>
border-radius: 20px;<br>
}</p>
<p>.imt-fb-close-button {<br>
pointer-events: all;<br>
cursor: pointer;<br>
position: absolute;<br>
margin-top: -10px;<br>
}</p>
<p>.imt-fb-close-content {<br>
padding: 22px;<br>
width: 320px;<br>
pointer-events: all;<br>
}</p>
<p>.imt-fb-close-title {<br>
font-weight: 500;<br>
color: var(--h2-color);<br>
}</p>
<p>.imt-fb-close-radio-content {<br>
background-color: var(--background-light-green);<br>
padding: 8px 20px;<br>
}</p>
<p>.imt-fb-radio-sel,<br>
.imt-fb-radio-nor {<br>
width: 16px;<br>
height: 16px;<br>
border-radius: 8px;<br>
flex-shrink: 0;<br>
}</p>
<p>.imt-fb-radio-sel {<br>
border: 2px solid var(--primary);<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
}</p>
<p>.imt-fb-radio-sel div {<br>
width: 8px;<br>
height: 8px;<br>
border-radius: 4px;<br>
background-color: var(--primary);<br>
}</p>
<p>.imt-fb-radio-nor {<br>
border: 2px solid #d3d4d6;<br>
}</p>
<p>.imt-fb-primary-btn {<br>
background-color: var(--primary);<br>
width: 72px;<br>
height: 32px;<br>
color: white;<br>
border-radius: 8px;<br>
text-align: center;<br>
line-height: 32px;<br>
font-size: 16px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-default-btn {<br>
border: 1px solid var(--primary);<br>
width: 72px;<br>
height: 32px;<br>
border-radius: 8px;<br>
color: var(--primary);<br>
line-height: 32px;<br>
text-align: center;<br>
font-size: 16px;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-guide-container {<br>
width: 312px;<br>
transform: translateY(-45%);<br>
}</p>
<p>.imt-fb-guide-bg {<br>
position: absolute;<br>
left: 30px;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
z-index: -1;<br>
height: 100%;<br>
width: 90%;<br>
}</p>
<p>.imt-fb-guide-bg.left {<br>
transform: scaleX(-1);<br>
}</p>
<p>.imt-fb-guide-content {<br>
margin: 16px -30px 80px 0px;<br>
display: flex;<br>
flex-direction: column;<br>
align-items: center;<br>
}</p>
<p>.imt-fb-guide-content.left {<br>
margin: 16px 21px 60px 32px;<br>
}</p>
<p>.imt-fb-guide-img {<br>
width: 220px;<br>
height: 112px;<br>
}</p>
<p>.imt-fb-guide-message {<br>
font-size: 14px;<br>
line-height: 28px;<br>
color: #333333;<br>
white-space: pre-wrap;<br>
text-align: center;<br>
font-weight: 700;<br>
margin-bottom: 20px;<br>
}</p>
<p>.imt-manga-guide-message {<br>
font-size: 16px;<br>
line-height: 24px;<br>
color: #333333;<br>
text-align: center;<br>
font-weight: 500;<br>
margin-bottom: 12px;<br>
}</p>
<p>.imt-fb-guide-button {<br>
margin-top: 16px;<br>
line-height: 40px;<br>
height: 40px;<br>
padding: 0 20px;<br>
width: unset;<br>
}</p>
<p>.imt-fb-more-buttons {<br>
box-shadow: 0px 2px 10px 0px #00000014;<br>
border: none;<br>
background: var(--float-ball-more-button-background-color);<br>
width: 36px;<br>
display: flex;<br>
flex-direction: column;<br>
border-radius: 18px;<br>
margin-top: 0px;<br>
padding: 7px 0 7px 0;<br>
}</p>
<p>.imt-fb-more-buttons &gt; div {<br>
margin: auto;<br>
}</p>
<p>.imt-fb-side,<br>
.imt-fb-reward {<br>
border-radius: 50%;<br>
cursor: pointer;<br>
pointer-events: all;<br>
position: relative;<br>
}</p>
<p>.imt-fb-side {<br>
margin: 10px 0;<br>
}</p>
<p>.imt-fb-new-badge {<br>
width: 26px;<br>
height: 14px;<br>
padding: 3px;<br>
background-color: #f53f3f;<br>
border-radius: 4px;<br>
position: absolute;<br>
top: -5px;<br>
right: 15px;<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
}</p>
<p>.imt-fb-side *,<br>
.imt-fb-reward * {<br>
pointer-events: all;<br>
}</p>
<p>.imt-fb-more-button {<br>
width: 36px;<br>
display: flex;<br>
align-items: center;<br>
justify-content: center;<br>
cursor: pointer;<br>
}<br>
/* Sheet.css <em>/<br>
.immersive-translate-sheet {<br>
position: fixed;<br>
transform: translateY(100%);<br>
/</em> Start off screen <em>/<br>
left: 0;<br>
right: 0;<br>
background-color: white;<br>
transition: transform 0.3s ease-out;<br>
/</em> Smooth slide transition <em>/<br>
box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);<br>
/</em> Ensure it's above other content */<br>
bottom: 0;<br>
border-top-left-radius: 16px;<br>
border-top-right-radius: 16px;<br>
overflow: hidden;<br>
}</p>
<p>.immersive-translate-sheet.visible {<br>
transform: translateY(0);<br>
}</p>
<p>.immersive-translate-sheet-backdrop {<br>
position: fixed;<br>
top: 0;<br>
left: 0;<br>
right: 0;<br>
bottom: 0;<br>
background-color: rgba(0, 0, 0, 0.5);<br>
opacity: 0;<br>
transition: opacity 0.3s ease-out;<br>
}</p>
<p>.immersive-translate-sheet-backdrop.visible {<br>
opacity: 1;<br>
}</p>
<p>.popup-container-sheet {<br>
max-width: 100vw;<br>
width: 100vw;<br>
}</p>
<p>.imt-no-events svg * {<br>
pointer-events: none !important;<br>
}</p>
<p>.imt-manga-button {<br>
width: 36px;<br>
display: flex;<br>
flex-direction: column;<br>
position: relative;<br>
align-items: center;<br>
justify-content: center;<br>
cursor: pointer;<br>
pointer-events: all;<br>
margin: 0 0 10px 0;<br>
background-color: var(--float-ball-more-button-background-color);<br>
border-radius: 18px;<br>
filter: drop-shadow(0px 2px 10px rgba(0, 0, 0, 0.08));<br>
opacity: 0.5;<br>
right: 8px;<br>
padding: 10px 0 4px 0;<br>
}</p>
<p>.imt-manga-feedback {<br>
cursor: pointer;<br>
margin-bottom: 10px;<br>
}</p>
<p>.imt-fb-feedback {<br>
cursor: pointer;<br>
margin-top: 10px;<br>
}</p>
<p>.imt-fb-upgrade-button {<br>
cursor: pointer;<br>
margin-top: 10px;<br>
}</p>
<p>.imt-manga-button:hover {<br>
opacity: 1;<br>
}</p>
<p>.imt-manga-translated {<br>
position: absolute;<br>
left: 24px;<br>
top: 20px;<br>
}</p>
<p>.imt-float-ball-loading {<br>
animation: imt-loading-animation 0.6s infinite linear !important;<br>
}</p>
<p>.imt-manga-guide-bg {<br>
position: absolute;<br>
left: 0;<br>
right: 0;<br>
top: 0;<br>
bottom: 0;<br>
z-index: -1;<br>
width: 372px;<br>
transform: translateY(-50%);<br>
}<br>
.imt-manga-guide-content {<br>
position: absolute;<br>
top: 15px;<br>
left: 0;<br>
right: 0;<br>
margin: 0 40px 0;<br>
}</p>
<p>.img-manga-guide-button {<br>
width: fit-content;<br>
margin: 0 auto;<br>
}</p>
<p>.img-manga-close {<br>
position: absolute;<br>
bottom: -200px;<br>
width: 32px;<br>
height: 32px;<br>
left: 0;<br>
right: 0;<br>
margin: auto;<br>
cursor: pointer;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-more-buttons,<br>
.imt-fb-container.dragging .imt-manga-button,<br>
.imt-fb-container.dragging .btn-animate:not(.imt-fb-btn) {<br>
display: none !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn {<br>
border-radius: 50% !important;<br>
width: 36px !important;<br>
height: 36px !important;<br>
display: flex !important;<br>
align-items: center !important;<br>
justify-content: center !important;<br>
cursor: move !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn div {<br>
border-radius: 50% !important;<br>
width: 36px !important;<br>
height: 36px !important;<br>
display: flex !important;<br>
align-items: center !important;<br>
justify-content: center !important;<br>
margin: 0 !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn.left,<br>
.imt-fb-container.dragging .imt-fb-btn.right {<br>
border-radius: 50% !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-btn.left div,<br>
.imt-fb-container.dragging .imt-fb-btn.right div {<br>
border-radius: 50% !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-fb-logo-img {<br>
margin: 0 !important;<br>
padding: 4px !important;<br>
}</p>
<p>.imt-fb-container.dragging .imt-float-ball-translated {<br>
right: 2px !important;<br>
bottom: 2px !important;<br>
}</p>
<p>@-webkit-keyframes imt-loading-animation {<br>
from {<br>
-webkit-transform: rotate(0deg);<br>
}</p>
<p>to {<br>
-webkit-transform: rotate(359deg);<br>
}<br>
}</p>
<p>@keyframes imt-loading-animation {<br>
from {<br>
transform: rotate(0deg);<br>
}</p>
<p>to {<br>
transform: rotate(359deg);<br>
}<br>
}</p>
<p>.imt-fb-icon {<br>
color: #666666;<br>
}</p>
<p>[data-theme=&quot;dark&quot;] .imt-fb-icon {<br>
color: #B3B3B3;<br>
}</p>
<p>[data-theme=&quot;light&quot;] .imt-fb-icon {<br>
color: #666666;<br>
}</p>
</style><div id="mount" style="display: block;"><div class="imt-fb-container right notranslate " data-theme="dark" style="z-index: 2147483637; pointer-events: none; right: 0px; top: 388px; display: flex;"><div class="btn-animate" style="transform: translateX(60px); opacity: 1; padding-left: 10px;"><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block;"><div><div class="imt-fb-btn imt-fb-more-button imt-fb-side"><svg class="imt-fb-icon" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.60547 12.9228C8.84029 12.9228 9.03755 13.0022 9.19629 13.161C9.3551 13.3198 9.43457 13.5171 9.43457 13.7519V18.5107C9.43457 18.7453 9.35513 18.9426 9.19629 19.1015C9.03755 19.2602 8.84029 19.3398 8.60547 19.3398H3.8457C3.61127 19.3397 3.41464 19.26 3.25586 19.1015C3.09712 18.9426 3.01758 18.7453 3.01758 18.5107V13.7519C3.01758 13.517 3.09712 13.3198 3.25586 13.161C3.41465 13.0023 3.61125 12.9229 3.8457 12.9228H8.60547ZM17.208 12.9228C17.4427 12.9228 17.6399 13.0022 17.7988 13.161C17.9575 13.3198 18.0371 13.5171 18.0371 13.7519V18.5107C18.0371 18.7453 17.9576 18.9426 17.7988 19.1015C17.6399 19.2602 17.4427 19.3398 17.208 19.3398H12.4492C12.2144 19.3398 12.0171 19.2602 11.8584 19.1015C11.6995 18.9426 11.6201 18.7453 11.6201 18.5107V13.7519C11.6201 13.517 11.6995 13.3198 11.8584 13.161C12.0171 13.0022 12.2144 12.9228 12.4492 12.9228H17.208ZM4.39258 17.9648H8.05957V14.2978H4.39258V17.9648ZM12.9951 17.9648H16.6621V14.2978H12.9951V17.9648ZM14.7598 2.92179C14.8641 2.57295 15.3576 2.57295 15.4619 2.92179L15.9561 4.57511C16.1376 5.18219 16.5965 5.66815 17.1924 5.8837L18.7412 6.44327C19.0635 6.56002 19.0633 7.01583 18.7412 7.13273L17.1924 7.69327C16.5966 7.90881 16.1376 8.39389 15.9561 9.00089L15.4619 10.6552C15.3575 11.0038 14.8642 11.0037 14.7598 10.6552L14.2646 9.00089C14.0831 8.39401 13.625 7.90881 13.0293 7.69327L11.4805 7.13273C11.158 7.01598 11.1579 6.55996 11.4805 6.44327L13.0293 5.8837C13.6251 5.66814 14.0831 5.18219 14.2646 4.57511L14.7598 2.92179ZM8.60547 4.32023C8.84029 4.32023 9.03755 4.39977 9.19629 4.55851C9.35496 4.71727 9.43448 4.91396 9.43457 5.14835V9.90812C9.43457 10.1429 9.35518 10.3402 9.19629 10.4989C9.03755 10.6578 8.84029 10.7372 8.60547 10.7372H3.8457C3.61131 10.7371 3.41463 10.6576 3.25586 10.4989C3.09712 10.3402 3.01758 10.1429 3.01758 9.90812V5.14835C3.01767 4.91386 3.09721 4.71731 3.25586 4.55851C3.41466 4.39986 3.61121 4.32032 3.8457 4.32023H8.60547ZM4.39258 9.36222H8.05957V5.69523H4.39258V9.36222Z" fill="currentColor"></path></svg><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="position: absolute; right: 0px; top: 0px; display: none; transform: translate(30%, -30%);"><g clip-path="url(#clip0_34242_2370)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14Z" fill="#B1B1B1" fill-opacity="0.32"></path><mask id="mask0_34242_2370" maskUnits="userSpaceOnUse" x="1" y="1" width="12" height="12" style="mask-type: alpha;"><rect x="1" y="1" width="12" height="12" fill="#D9D9D9"></rect></mask><g mask="url(#mask0_34242_2370)"><path d="M8.90169 3.66124V6.89549L9.94631 7.94012C9.9939 7.9877 10.0317 8.04208 10.0597 8.10324C10.0877 8.16441 10.1017 8.23328 10.1017 8.30987V8.61487C10.1017 8.76095 10.0516 8.88433 9.95144 8.98499C9.85119 9.08566 9.72835 9.13599 9.58294 9.13599H7.51881V11.8871C7.51881 12.0325 7.46898 12.1553 7.36931 12.2555C7.26956 12.3557 7.14735 12.4059 7.00269 12.4059C6.85802 12.4059 6.73494 12.3557 6.63344 12.2555C6.53202 12.1553 6.48131 12.0325 6.48131 11.8871V9.13599H4.41719C4.27177 9.13599 4.14894 9.08566 4.04869 8.98499C3.94852 8.88433 3.89844 8.76095 3.89844 8.61487V8.30987C3.89844 8.23328 3.91244 8.16441 3.94044 8.10324C3.96844 8.04208 4.00623 7.9877 4.05381 7.94012L5.09844 6.89549V3.66124H4.94844C4.82094 3.64733 4.71406 3.59299 4.62781 3.49824C4.54156 3.40358 4.49844 3.28987 4.49844 3.15712C4.49844 3.01245 4.54852 2.88937 4.64869 2.78787C4.74894 2.68645 4.87177 2.63574 5.01719 2.63574H8.98294C9.12835 2.63574 9.25119 2.68558 9.35144 2.78524C9.4516 2.88491 9.50169 3.00712 9.50169 3.15187C9.50169 3.28462 9.45856 3.3992 9.37231 3.49562C9.28606 3.59212 9.17919 3.64733 9.05169 3.66124H8.90169ZM5.36169 8.09849H8.63844L7.86419 7.32424V3.67324H6.13594V7.32424L5.36169 8.09849Z" fill="white"></path></g></g><defs><clippath id="clip0_34242_2370"><rect width="14" height="14" fill="white"></rect></clippath></defs></svg></div></div></div></div><div hidden="" class="imt-no-events btn-animate " id="manga-button" style="position: relative;"><div class="imt-manga-button" style="transform: translateX(2px);"><div class=" " style="position: relative; pointer-events: all; display: inline-block;"><div><svg class="imt-manga-feedback imt-fb-icon" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.0003 14.2749C11.213 14.2749 11.3895 14.2047 11.5299 14.0643C11.6705 13.9239 11.7408 13.7473 11.7408 13.5345C11.7408 13.3218 11.6705 13.1453 11.5299 13.0049C11.3895 12.8645 11.213 12.7943 11.0003 12.7943C10.7877 12.7943 10.6111 12.8645 10.4707 13.0049C10.3302 13.1453 10.2599 13.3218 10.2599 13.5345C10.2599 13.7473 10.3302 13.9239 10.4707 14.0643C10.6111 14.2047 10.7877 14.2749 11.0003 14.2749ZM11.0003 11.0842C11.1954 11.0842 11.3587 11.0185 11.4903 10.8869C11.622 10.7552 11.6878 10.5918 11.6878 10.3967V6.23645C11.6878 6.04135 11.622 5.87803 11.4903 5.74649C11.3587 5.6148 11.1954 5.54895 11.0003 5.54895C10.8052 5.54895 10.6419 5.6148 10.5104 5.74649C10.3787 5.87803 10.3128 6.04135 10.3128 6.23645V10.3967C10.3128 10.5918 10.3787 10.7552 10.5104 10.8869C10.6419 11.0185 10.8052 11.0842 11.0003 11.0842ZM5.53562 16.8311L3.70045 18.666C3.43966 18.9269 3.13968 18.9861 2.80051 18.8434C2.4615 18.7005 2.29199 18.4434 2.29199 18.072V4.73816C2.29199 4.27509 2.45241 3.88314 2.77324 3.5623C3.09408 3.24147 3.48603 3.08105 3.9491 3.08105H18.0516C18.5146 3.08105 18.9066 3.24147 19.2274 3.5623C19.5482 3.88314 19.7087 4.27509 19.7087 4.73816V15.174C19.7087 15.637 19.5482 16.029 19.2274 16.3498C18.9066 16.6706 18.5146 16.8311 18.0516 16.8311H5.53562ZM4.95033 15.4561H18.0516C18.1221 15.4561 18.1868 15.4266 18.2454 15.3678C18.3042 15.3092 18.3337 15.2445 18.3337 15.174V4.73816C18.3337 4.66758 18.3042 4.60295 18.2454 4.54428C18.1868 4.48546 18.1221 4.45605 18.0516 4.45605H3.9491C3.87851 4.45605 3.81389 4.48546 3.75522 4.54428C3.6964 4.60295 3.66699 4.66758 3.66699 4.73816V16.7254L4.95033 15.4561Z" fill="currentColor"></path></svg></div></div><div style="position: relative;"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="manhua"><path id="Vector" d="M14.8853 4.92364C14.8853 4.92364 16.3905 10.4362 22.6668 4C22.6668 4 20.3381 10.8907 25.3364 10.0843C25.3364 10.0843 22.0563 15.6994 29 18.0599C29 18.0599 22.9934 19.306 21.1617 28C21.1617 28 17.7679 24.54 14.8853 27.3549C14.8853 27.3549 13.3233 23.5724 7.33097 26.27C7.33097 26.27 10.1141 20.6549 4.83179 21.0507C4.83179 21.0507 7.16057 18.8955 3 15.9047C3 15.9047 7.50137 16.1833 6.33697 11.7117C6.33697 11.7117 10.0005 12.3421 8.66576 6.82957C8.65156 6.81491 12.4855 9.80574 14.8853 4.92364Z" fill="#ED6D8F"></path><path id="Vector_2" d="M20.8599 13.7022C20.885 13.1361 20.9543 12.5713 20.9959 12.0052C21.0337 11.568 20.8107 11.2794 20.3876 11.18C20.0759 11.1013 19.7508 11.0867 19.433 11.137C19.1951 11.1945 18.9542 11.2396 18.7113 11.2721C18.2403 11.3028 17.9973 11.5275 17.9796 11.988C17.977 12.0833 17.9596 12.1777 17.928 12.268C17.3034 13.9102 16.6774 15.5499 16.0503 17.1873C16.0301 17.2401 16.0062 17.2904 15.9671 17.3776C15.7291 16.8975 15.4281 16.4898 15.2745 15.9986C14.8073 14.5152 14.3186 13.033 13.8312 11.5594C13.6826 11.1112 13.3489 10.9344 12.8754 11.0216C12.7889 11.0365 12.7008 11.0398 12.6134 11.0314C12.2241 10.9938 11.8311 11.0404 11.4623 11.1677C11.0946 11.2991 10.9498 11.557 11.0152 11.9254C11.0428 12.0371 11.0643 12.1503 11.0795 12.2643C11.1223 13.1902 11.1777 14.1087 11.2054 15.0321C11.257 16.7992 11.2117 18.5651 11.0858 20.3284C11.0644 20.6354 11.0304 20.9424 11.0228 21.2494C11.0115 21.6092 11.1613 21.7811 11.5266 21.8143C11.9976 21.8573 12.4711 21.8708 12.9421 21.9088C13.0309 21.9201 13.121 21.9003 13.1962 21.8528C13.2714 21.8053 13.3268 21.7334 13.3527 21.6497C13.3996 21.5394 13.4252 21.4216 13.4282 21.3022C13.4295 20.8258 13.4207 20.3493 13.4081 19.8741C13.393 19.3264 13.3917 18.7763 13.3438 18.231C13.2857 17.5839 13.266 16.934 13.2847 16.2847C13.2847 16.2466 13.291 16.2073 13.2985 16.1312C13.3338 16.2024 13.3514 16.2356 13.3665 16.2712C13.9017 17.5228 14.3617 18.8037 14.7443 20.1074C14.7928 20.2421 14.7928 20.3889 14.7443 20.5237C14.6322 20.8196 14.7141 21.037 14.9659 21.1377C15.4445 21.3268 15.9331 21.4926 16.4155 21.6731C16.4865 21.7033 16.566 21.7091 16.6408 21.6895C16.7157 21.6698 16.7815 21.6259 16.8273 21.565C16.9085 21.4643 16.9743 21.3526 17.0225 21.2335C17.0537 21.1374 17.0798 21.0399 17.1006 20.9412C17.3185 20.2425 17.5653 19.5499 17.7517 18.8438C17.9785 17.9723 18.2624 17.1158 18.6018 16.2798C18.6201 16.2439 18.6411 16.2094 18.6647 16.1766C18.6761 16.2319 18.6761 16.254 18.6761 16.2761C18.6345 17.59 18.5955 18.8978 18.5501 20.2056C18.5363 20.5949 18.491 20.9829 18.4809 21.3722C18.4721 21.705 18.6207 21.8708 18.9557 21.9002C19.4355 21.9432 19.9191 21.9592 20.4002 21.9973C20.4888 22.0079 20.5784 21.9875 20.653 21.9399C20.7277 21.8922 20.7827 21.8203 20.8082 21.7369C20.8531 21.6305 20.8766 21.5167 20.8775 21.4017C20.88 20.7668 20.8674 20.132 20.8674 19.4971C20.8662 19.2846 20.8687 19.0722 20.8523 18.8622C20.8158 18.3968 20.7264 17.9314 20.7339 17.4685C20.7515 16.2122 20.8044 14.9572 20.8599 13.7022Z" fill="white"></path></g></svg><svg hidden="true" class="imt-manga-translated" width="11" height="11" viewBox="0 0 11 11" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="5.5" cy="5.5" r="5.5" fill="#60BB4C"></circle><path d="M1.40869 5.87858L2.24161 5.18962L4.15357 6.64214C4.15357 6.64214 6.33559 4.15566 9.0067 2.48145L9.32553 2.87514C9.32553 2.87514 6.28678 5.55844 4.71748 9.07881L1.40869 5.87858Z" fill="#EFF8ED"></path></svg></div><svg class="imt-float-ball-loading" hidden="true" width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin: 9px;"><path d="M9.42859 0C9.84288 0 10.1929 0.387143 10.1929 0.847143V3.99429C10.1929 4.45429 9.84431 4.84143 9.42859 4.84143C9.01431 4.84143 8.66431 4.45571 8.66431 3.99429V0.847143C8.66431 0.387143 9.01288 0 9.42859 0Z" fill="#E9E9E9"></path><path d="M14.1301 1.38877C14.5158 1.62591 14.6301 2.12163 14.4258 2.52305L12.9515 5.19448C12.901 5.28714 12.8325 5.36876 12.75 5.43455C12.6675 5.50035 12.5727 5.54898 12.4712 5.5776C12.3696 5.60621 12.2634 5.61424 12.1586 5.60119C12.0539 5.58814 11.9529 5.55429 11.8615 5.50163C11.6787 5.38432 11.5468 5.20237 11.4923 4.9921C11.4377 4.78184 11.4645 4.55874 11.5672 4.36734L13.0415 1.69591C13.2686 1.29448 13.7443 1.15305 14.1301 1.38877Z" fill="#989697"></path><path d="M17.4685 4.75707C17.5813 4.95451 17.6123 5.18824 17.5549 5.40825C17.4975 5.62826 17.3563 5.81705 17.1614 5.93422L14.4971 7.52564C14.0971 7.76993 13.6014 7.62422 13.3657 7.20707C13.2532 7.00994 13.2222 6.77667 13.2793 6.55702C13.3365 6.33737 13.4771 6.14874 13.6714 6.03136L16.3357 4.43993C16.7371 4.21993 17.2557 4.34136 17.4685 4.7585V4.75707Z" fill="#9B999A"></path><path d="M18.8572 9.42835C18.8572 9.84263 18.47 10.1926 18.01 10.1926H14.8629C14.4029 10.1926 14.0157 9.84406 14.0157 9.42835C14.0157 9.01406 14.4029 8.66406 14.8629 8.66406H18.01C18.47 8.66406 18.8572 9.01263 18.8572 9.42835Z" fill="#A3A1A2"></path><path d="M17.4686 14.1303C17.3515 14.3134 17.1697 14.4455 16.9594 14.5003C16.7491 14.5552 16.5259 14.5286 16.3343 14.426L13.6629 12.9517C13.5702 12.9012 13.4886 12.8327 13.4228 12.7503C13.357 12.6678 13.3084 12.573 13.2798 12.4714C13.2512 12.3698 13.2431 12.2636 13.2562 12.1589C13.2692 12.0542 13.3031 11.9532 13.3558 11.8617C13.4731 11.6789 13.655 11.547 13.8653 11.4925C14.0755 11.4379 14.2986 11.4647 14.49 11.5674L17.1615 13.0417C17.5629 13.2689 17.7043 13.7446 17.4686 14.1303Z" fill="#ABA9AA"></path><path opacity="0.7" d="M14.1 17.4686C13.9026 17.5814 13.6689 17.6124 13.4489 17.555C13.2288 17.4976 13.04 17.3564 12.9229 17.1615L11.3315 14.4972C11.0872 14.0972 11.2329 13.6015 11.65 13.3658C11.8472 13.2533 12.0804 13.2224 12.3001 13.2795C12.5197 13.3366 12.7084 13.4773 12.8257 13.6715L14.4172 16.3358C14.6372 16.7372 14.5157 17.2558 14.0986 17.4686H14.1Z" fill="#B2B2B2"></path><path opacity="0.6" d="M9.42859 18.8571C9.01431 18.8571 8.66431 18.4699 8.66431 18.0099V14.8628C8.66431 14.4028 9.01288 14.0156 9.42859 14.0156C9.84288 14.0156 10.1929 14.4028 10.1929 14.8628V18.0099C10.1929 18.4699 9.84431 18.8571 9.42859 18.8571Z" fill="#BAB8B9"></path><path opacity="0.5" d="M4.72717 17.4685C4.5441 17.3514 4.41195 17.1696 4.35713 16.9593C4.30231 16.749 4.32885 16.5258 4.43145 16.3342L5.90574 13.6628C5.95622 13.5701 6.02472 13.4885 6.1072 13.4227C6.18969 13.3569 6.2845 13.3083 6.38606 13.2797C6.48762 13.251 6.59387 13.243 6.69857 13.2561C6.80327 13.2691 6.90431 13.303 6.99574 13.3556C7.38145 13.5914 7.49431 14.0885 7.29002 14.4899L5.81574 17.1614C5.5886 17.5628 5.11288 17.7042 4.72717 17.4685Z" fill="#C2C0C1"></path><path opacity="0.4" d="M1.38862 14.1002C1.27584 13.9027 1.24483 13.669 1.30223 13.449C1.35964 13.229 1.50089 13.0402 1.69576 12.923L4.36004 11.3316C4.76004 11.0873 5.25576 11.233 5.49147 11.6502C5.60393 11.8473 5.63491 12.0806 5.5778 12.3002C5.52069 12.5199 5.38 12.7085 5.18576 12.8259L2.52004 14.4173C2.12004 14.6373 1.60004 14.5159 1.38862 14.0987V14.1002Z" fill="#CBCBCB"></path><path d="M0 9.42835C0 9.01406 0.387143 8.66406 0.847143 8.66406H3.99429C4.45429 8.66406 4.84143 9.01263 4.84143 9.42835C4.84143 9.84263 4.45571 10.1926 3.99429 10.1926H0.847143C0.387143 10.1926 0 9.84406 0 9.42835Z" fill="#D2D2D2"></path><path opacity="0.2" d="M1.38852 4.72705C1.50561 4.54398 1.68746 4.41183 1.89774 4.35701C2.10803 4.30219 2.33125 4.32873 2.52281 4.43133L5.19424 5.90562C5.28689 5.9561 5.36851 6.0246 5.43431 6.10708C5.5001 6.18957 5.54874 6.28438 5.57735 6.38594C5.60597 6.48749 5.61399 6.59375 5.60094 6.69845C5.5879 6.80315 5.55405 6.90419 5.50138 6.99562C5.38407 7.17844 5.20212 7.31029 4.99186 7.36484C4.78159 7.4194 4.55849 7.39263 4.3671 7.2899L1.69567 5.81562C1.29424 5.58847 1.15281 5.11276 1.38852 4.72705Z" fill="#DADADA"></path><path d="M4.75719 1.38849C4.95463 1.27571 5.18837 1.24471 5.40838 1.30211C5.62838 1.35952 5.81718 1.50077 5.93434 1.69564L7.52577 4.35992C7.77005 4.75992 7.62434 5.25564 7.20719 5.49135C7.01006 5.60381 6.77679 5.63479 6.55714 5.57768C6.33749 5.52056 6.14886 5.37988 6.03148 5.18564L4.44005 2.51992C4.22005 2.11992 4.34148 1.59992 4.75862 1.38849H4.75719Z" fill="#E2E2E2"></path></svg></div></div><div class=" " style="position: relative; pointer-events: all; display: inline-block;"><div><div style="display: flex; align-items: center; flex-direction: row;"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block; opacity: 0;"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clippath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clippath></defs></svg><div class="imt-fb-btn  right btn-animate " dir="ltr" style="opacity: 0.7; transform: translateX(15px);"><div><svg class="imt-fb-logo-img imt-fb-logo-img-big-bg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><path fill="none" d="M0 0h24v24H0z"></path><path d="M5 15v2a2 2 0 0 0 1.85 1.995L7 19h3v2H7a4 4 0 0 1-4-4v-2h2zm13-5l4.4 11h-2.155l-1.201-3h-4.09l-1.199 3h-2.154L16 10h2zm-1 2.885L15.753 16h2.492L17 12.885zM8 2v2h4v7H8v3H6v-3H2V4h4V2h2zm9 1a4 4 0 0 1 4 4v2h-2V7a2 2 0 0 0-2-2h-3V3h3zM6 6H4v3h2V6zm4 0H8v3h2V6z" fill="rgba(255,255,255,1)"></path></svg><svg hidden="true" class="imt-float-ball-translated" width="11" height="11" viewBox="0 0 11 11" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="5.5" cy="5.5" r="5.5" fill="#60BB4C"></circle><path d="M1.40869 5.87858L2.24161 5.18962L4.15357 6.64214C4.15357 6.64214 6.33559 4.15566 9.0067 2.48145L9.32553 2.87514C9.32553 2.87514 6.28678 5.55844 4.71748 9.07881L1.40869 5.87858Z" fill="#EFF8ED"></path></svg></div></div><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: none; opacity: 0;"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clippath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clippath></defs></svg></div></div></div><div style="position: relative; width: 100%; opacity: 0;"><div title="关闭悬浮球" class="imt-fb-close-button" style="transform: translateX(100%);"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clippath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clippath></defs></svg></div></div><div class="imt-fb-more-buttons btn-animate" style="margin-top: 10px; transform: translateX(60px);"><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block;"><div><div class="imt-fb-more-button"><svg class="imt-fb-icon" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 22px; height: 22px;"><path d="M16 7.66699H10.375" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M11.625 14.333L6 14.333" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.125 16C15.1605 16 16 15.1605 16 14.125C16 13.0895 15.1605 12.25 14.125 12.25C13.0895 12.25 12.25 13.0895 12.25 14.125C12.25 15.1605 13.0895 16 14.125 16Z" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7.875 9.75C8.91053 9.75 9.75 8.91053 9.75 7.875C9.75 6.83947 8.91053 6 7.875 6C6.83947 6 6 6.83947 6 7.875C6 8.91053 6.83947 9.75 7.875 9.75Z" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><rect x="3" y="3" width="16" height="16" rx="1.66667" stroke="currentColor" stroke-width="1.4"></rect></svg></div></div></div><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block;"><div><div class="imt-fb-more-button"><svg class="imt-fb-feedback imt-fb-icon" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.0003 14.2749C11.213 14.2749 11.3895 14.2047 11.5299 14.0643C11.6705 13.9239 11.7408 13.7473 11.7408 13.5345C11.7408 13.3218 11.6705 13.1453 11.5299 13.0049C11.3895 12.8645 11.213 12.7943 11.0003 12.7943C10.7877 12.7943 10.6111 12.8645 10.4707 13.0049C10.3302 13.1453 10.2599 13.3218 10.2599 13.5345C10.2599 13.7473 10.3302 13.9239 10.4707 14.0643C10.6111 14.2047 10.7877 14.2749 11.0003 14.2749ZM11.0003 11.0842C11.1954 11.0842 11.3587 11.0185 11.4903 10.8869C11.622 10.7552 11.6878 10.5918 11.6878 10.3967V6.23645C11.6878 6.04135 11.622 5.87803 11.4903 5.74649C11.3587 5.6148 11.1954 5.54895 11.0003 5.54895C10.8052 5.54895 10.6419 5.6148 10.5104 5.74649C10.3787 5.87803 10.3128 6.04135 10.3128 6.23645V10.3967C10.3128 10.5918 10.3787 10.7552 10.5104 10.8869C10.6419 11.0185 10.8052 11.0842 11.0003 11.0842ZM5.53562 16.8311L3.70045 18.666C3.43966 18.9269 3.13968 18.9861 2.80051 18.8434C2.4615 18.7005 2.29199 18.4434 2.29199 18.072V4.73816C2.29199 4.27509 2.45241 3.88314 2.77324 3.5623C3.09408 3.24147 3.48603 3.08105 3.9491 3.08105H18.0516C18.5146 3.08105 18.9066 3.24147 19.2274 3.5623C19.5482 3.88314 19.7087 4.27509 19.7087 4.73816V15.174C19.7087 15.637 19.5482 16.029 19.2274 16.3498C18.9066 16.6706 18.5146 16.8311 18.0516 16.8311H5.53562ZM4.95033 15.4561H18.0516C18.1221 15.4561 18.1868 15.4266 18.2454 15.3678C18.3042 15.3092 18.3337 15.2445 18.3337 15.174V4.73816C18.3337 4.66758 18.3042 4.60295 18.2454 4.54428C18.1868 4.48546 18.1221 4.45605 18.0516 4.45605H3.9491C3.87851 4.45605 3.81389 4.48546 3.75522 4.54428C3.6964 4.60295 3.66699 4.66758 3.66699 4.73816V16.7254L4.95033 15.4561Z" fill="currentColor"></path></svg></div></div></div></div><div hidden="" id="immersive-translate-popup-overlay" class="immersive-translate-popup-overlay"><div class="immersive-translate-popup-wrapper" style="position: fixed; bottom: 30px; right: 65px;"></div></div></div></div></template></div></html></div></template>


