<template>
  <div class="panel-view">
    <div class="controls">
      <div class="circle red"></div>
      <div class="circle yellow"></div>
      <div class="circle green"></div>
    </div>
    <div class="title">
      <span class="title-text"></span>
    </div>
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatPanel'
}
</script>

<style scoped>
.panel-view {
    position: relative;
    border-radius: 6px;
    margin: 1rem 0;
    overflow: auto hidden;
    background-color: var(--vp-c-bg-alt);
    border: 1px solid var(--vp-c-border);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.panel-view.manager,.panel-view.container {
    background-color: #032f62
}

.panel-view .controls {
    display: initial;
    position: absolute;
    top: .8rem;
    width: 100%
}

.panel-view .circle {
    position: absolute;
    top: 2px;
    width: 12px;
    height: 12px;
    border-radius: 6px
}

.panel-view .circle.red {
    left: 17px;
    background-color: #ff5f56
}

.panel-view .circle.yellow {
    left: 36px;
    background-color: #ffbd2e
}

.panel-view .circle.green {
    left: 55px;
    background-color: #27c93f
}

.panel-view .title {
    text-align: center;
    width: 100%;
    font-size: .9rem;
    line-height: 1rem
}

.panel-view .title .tab {
    color: gray;
    cursor: pointer;
    transition: .3s ease
}

.panel-view .title .tab.active {
    color: #fff;
    cursor: default
}

.panel-view .title .title-text:not(:last-child):after {
    color: gray;
    content: " - "
}

.panel-view .title .tab+.tab:before {
    cursor: default;
    content: " | ";
    color: gray
}

.panel-view .content {
    padding: .2rem 1.2rem;
    overflow: hidden;
    width: 100%;
    box-sizing: border-box;
    min-width: 0;
}

/* 确保面板内容中的图片正确显示 */
.panel-view .content img {
    max-width: 100%;
    height: auto;
}

.panel-view .content img[width*="%"] {
    max-width: none;
    width: auto !important;
}

.panel-view .content img[style*="width"] {
    max-width: none;
}

/* 确保聊天面板中的消息组件正确显示 */
.panel-view .content .chat-message {
    min-width: 0;
}

.panel-view .content .chat-message .message-box {
    min-width: 0;
}


.panel-view .content>p {
    font-size: .8rem;
    color: #909399;
    text-align: center
}

.panel-view.mini .controls {
    display: none
}

.panel-view:not(.mini) .content {
    padding-top: 2rem
}
</style>
