<template>
  <div class="recall-message">
    <!-- 撤回系统消息 -->
    <div v-if="showSystemMessage" class="system-message-container">
      <chat-message
        nickname="系统"
        type="system"
        class="system-message"
      >
        <p>{{ nickname }}撤回了一条消息</p>
      </chat-message>
    </div>
    
    <!-- 撤回消息内容 -->
    <div ref="recallContainer" class="recall-container" :class="{ 'show-recall': showRecall }">
      <chat-message
        :nickname="nickname"
        :type="type"
        class="recall-content"
      >
        <slot />
      </chat-message>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecallMessage',
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
      showRecall: false,
      showSystemMessage: false,
      observer: null,
      timer: null,
      hasStartedTimer: false
    }
  },
  mounted() {
    this.setupIntersectionObserver()
  },
  beforeUnmount() {
    this.cleanup()
  },
  methods: {
    setupIntersectionObserver() {
      // 使用 Intersection Observer 检测组件是否在视口中
      this.observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !this.hasStartedTimer) {
            // 组件进入视口，开始计时
            this.hasStartedTimer = true
            this.startRecallTimer()
          }
        })
      }, {
        threshold: 0.1 // 当10%的组件可见时触发
      })

      this.observer.observe(this.$refs.recallContainer)
    },
    
    startRecallTimer() {
      // 3秒后显示撤回效果
      this.timer = setTimeout(() => {
        this.showRecall = true
        
        // 撤回动画结束后显示系统消息
        setTimeout(() => {
          this.showSystemMessage = true
        }, 500) // 等待撤回动画完成
      }, 3000)
    },
    
    cleanup() {
      if (this.observer) {
        this.observer.disconnect()
      }
      if (this.timer) {
        clearTimeout(this.timer)
      }
    }
  }
}
</script>

<style scoped>
.recall-message {
  position: relative;
  margin: 1.5rem 0;
}

.system-message-container {
  margin-bottom: 0.5rem;
}

.system-message {
  opacity: 0.7;
  font-size: 0.9em;
}

.system-message :deep(.message-box p) {
  color: #666;
}

.recall-container {
  position: relative;
  display: inline-block;
  border: 0px dashed transparent;
  border-radius: 6px;
  padding: 4px 6px;
  margin: -4px -6px;
  transition: all 0.5s ease-in-out;
}

.recall-container.show-recall {
  border: 2px dashed rgba(170, 170, 170, 0.6);
}

.recall-content {
  transition: all 0.5s ease-in-out;
}

.recall-container.show-recall .recall-content {
  filter: opacity(0.7);
}

.recall-container.show-recall .recall-content :deep(.avatar) {
  filter: opacity(0.7);
}

.recall-container.show-recall .recall-content :deep(.avatar img) {
  filter: opacity(0.7);
}

.recall-container.show-recall .recall-content :deep(.nickname) {
  opacity: 0.7;
}

.recall-container.show-recall .recall-content :deep(.message-box) {
  opacity: 0.7;
}

/* 确保系统消息也应用撤回样式 */
.recall-container.show-recall .recall-content.system-message :deep(.message-box p) {
  opacity: 0.7;
}
</style>
