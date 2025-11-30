<template>
  <div class="chat-message" :class="messageClass" ref="messageElement">
    <div class="avatar">
      <img :src="avatarSrc" :alt="nickname" />
    </div>
    <div class="nickname">{{ nickname }}</div>
    <div class="message-box" :style="messageBoxStyle">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatMessage',
  props: {
    nickname: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'user' // 'user', 'bot', or 'system'
    }
  },
  data() {
    return {
      isVisible: false
    }
  },
  computed: {
    messageClass() {
      return {
        'user-message': this.type === 'user',
        'bot-message': this.type === 'bot',
        'system-message': this.type === 'system',
        'visible': this.isVisible
      }
    },
    avatarSrc() {
      // 根据昵称返回对应的QQ头像
      if (this.nickname === '马化腾') {
        return 'https://q1.qlogo.cn/g?b=qq&nk=10001&s=640' }
      if (this.nickname === '腾讯视频') {
        return 'https://q1.qlogo.cn/g?b=qq&nk=123456&s=640'
      }
      return this.type === 'user' 
        ? 'https://q1.qlogo.cn/g?b=qq&nk=2237886846&s=640' 
        : 'https://q1.qlogo.cn/g?b=qq&nk=3929982192&s=640'
    },
    messageBoxStyle() {
      return {}
    }
  },
  mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.isVisible = true
          observer.unobserve(entry.target)
        }
      })
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    })

    observer.observe(this.$refs.messageElement)
  }
}
</script>

<style scoped>
.chat-message {
    position: relative;
    margin: 1.5rem 0;
    padding: 0.5rem 0;
    opacity: 0;
    transform: translateX(-20px);
    transition: opacity 0.4s ease-out, transform 0.4s ease-out;
}

.chat-message.visible {
    opacity: 1;
    transform: translateX(0);
}

.chat-message .avatar {
    width: 2.8rem;
    height: 2.8rem;
    position: absolute;
    border-radius: 100%;
    transform: translateY(-1px);
    -webkit-user-select: none;
    user-select: none;
    pointer-events: none;
    overflow: hidden;
    border: 2px solid var(--vp-c-border);
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.chat-message .nickname {
    -webkit-user-select: none;
    user-select: none;
    position: relative;
    margin: 0 0 .4rem 4.2rem;
    font-weight: 700;
    font-size: .9rem
}

.chat-message:not(.no-padding) .message-box {
    padding: .5rem .7rem
}

.chat-message .message-box {
    position: relative;
    margin-left: 4.2rem;
    width: fit-content;
    max-width: 100%;
    border-radius: .5rem;
    background-color: var(--vp-c-bg);
    word-break: break-all;
    line-height: 26px!important;
    border: 1px solid var(--vp-c-border);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chat-message .message-box>img {
    border-radius: .5rem
}

.chat-message .message-box img {
    vertical-align: middle;
    max-width: 100%;
    height: auto;
}

.chat-message .message-box p>img {
    margin: .2rem 0;
}

/* 专门处理百分比宽度图片的样式 */
.chat-message .message-box img[width*="%"] {
    max-width: none;
    width: auto !important;
}

.chat-message .message-box img[style*="width"] {
    max-width: none;
}

/* 确保包含百分比宽度设置的图片容器正确显示 */
.chat-message .message-box {
    min-width: 0;
    overflow-wrap: break-word;
    display: inline-block;
    max-width: calc(100% - 4.2rem);
}


.chat-message .message-box p {
    margin: 0!important;
    line-height: 26px!important
}

.chat-message .message-box p.indent-1 {
    padding-left: 1rem
}

.chat-message .message-box p.indent-2 {
    padding-left: 2rem
}

.chat-message .message-box blockquote {
    font-size: .9rem;
    margin: 0 0 .2rem;
    background-color: #f3f6f9;
    border: none;
    border-radius: .5rem;
    padding: .2rem .6rem;
    background-color: var(--vp-c-bg-alt);
    color: var(--vp-c-text-2)
}

/* 系统提示居中样式 */
.chat-message.system-message {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 1px 0;
    padding: 0;
    background-color: transparent;
    border: none;
    box-shadow: none;
    transform: none;
    width: 100%;
}

.chat-message.system-message .avatar,
.chat-message.system-message .nickname {
    display: none;
}

.chat-message.system-message .message-box {
    margin-left: 0;
    width: auto;
    text-align: center;
    background-color: transparent;
    border: none;
    box-shadow: none;
    padding: 0;
    display: inline-block;
    white-space: nowrap;
    max-width: 100%;
}

.chat-message.system-message .message-box p {
    font-size: 13px;
    font-weight: 500;
    line-height: 1.3;
    margin: 0 !important;
    display: inline;
    white-space: nowrap;
}


/* 响应式设计 */
@media (max-width: 768px) {
    .chat-message.system-message {
        margin: 1px 0;
    }
    
    .chat-message.system-message .message-box p {
        font-size: 12px;
    }
}
</style>
