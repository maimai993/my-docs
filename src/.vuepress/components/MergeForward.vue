<template>
  <div class="merge-forward-wrapper">
    <!-- 作为用户消息的一部分显示 -->
    <div class="merge-forward" @click="openForwardDialog">
      <div class="forward-header">
        <span class="forward-text">群聊的聊天记录</span>
      </div>
      <div class="forward-preview">
        <div 
          v-for="(message, index) in previewMessages" 
          :key="index" 
          class="preview-message"
        >
          <span class="preview-nickname">{{ message.nickname }}：</span>
          <span class="preview-content">{{ formatPreviewContent(message.content) }}</span>
        </div>
        <div class="divider-line"></div>
        <div class="more-messages">
          查看{{ messages.length }}条转发消息
        </div>
      </div>
    </div>

    <!-- 使用Teleport将对话框渲染到body -->
    <Teleport to="body">
      <div v-if="showDialog" class="forward-dialog-overlay" @click="closeDialog">
        <div class="forward-dialog" @click.stop>
          <ChatPanel>
            <div class="forward-messages">
              <ChatMessage
                v-for="(message, index) in messages"
                :key="index"
                :nickname="message.nickname"
                :type="message.type"
              >
                <span v-html="formatContent(message.content)"></span>
              </ChatMessage>
            </div>
          </ChatPanel>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script>
export default {
  name: 'MergeForward',
  props: {
    messages: {
      type: Array,
      required: true,
      default: () => []
    },
    maxPreview: {
      type: Number,
      default: 4
    }
  },
  data() {
    return {
      showDialog: false
    }
  },
  computed: {
    previewMessages() {
      return this.messages.slice(0, this.maxPreview)
    }
  },
  methods: {
    openForwardDialog() {
      this.showDialog = true
      // 阻止滚动穿透
      document.body.style.overflow = 'hidden'
    },
    closeDialog() {
      this.showDialog = false
      document.body.style.overflow = ''
    },
    formatContent(content) {
      if (!content) return ''
      // 将换行符转换为HTML换行标签
      return content.replace(/\n/g, '<br>')
    },
    formatPreviewContent(content) {
      if (!content) return ''
      // 在预览中将换行符替换为空格
      return content.replace(/\n/g, ' ')
    }
  }
}
</script>

<style scoped>
.merge-forward-wrapper {
  /* 作为用户消息的一部分 */
  display: inline-block;
  max-width: 100%;
}

.merge-forward {
  border-radius: 8px;
  padding: 12px;
  margin: 5px 0;
  background-color: var(--vp-c-bg-alt);
  cursor: pointer;
  transition: all 0.3s ease;
  user-select: none;
  display: inline-block;
  max-width: 250px;
  min-width: 250px;
}

.merge-forward:hover {
  background-color: var(--vp-c-bg-soft);
  transform: translateY(-1px);
}

.forward-header {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.forward-icon {
  margin-right: 6px;
  font-size: 16px;
}

.forward-text {
  font-weight: 600;
  margin-right: auto;
}

.forward-count {
  font-size: 12px;
  color: var(--vp-c-text-3);
}

.forward-preview {
  font-size: 13px;
  line-height: 1.4;
}

.preview-message {
  margin-bottom: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: 1.4;
}

.preview-nickname {
  color: var(--vp-c-brand);
  font-weight: 500;
}

.preview-content {
  color: var(--vp-c-text-1);
}

.divider-line {
  height: 1px;
  background-color: var(--vp-c-divider);
  margin: 8px 0;
  opacity: 0.6;
}

.more-messages {
  color: var(--vp-c-text-3);
  font-size: 12px;
  margin-top: 4px;
}

/* 全局弹出对话框样式 */
.forward-dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  padding: 20px;
}

.forward-dialog {
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  border: none;
  background: transparent;
  box-shadow: none;
}

.forward-messages {
  max-height: 400px;
  overflow-y: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .forward-dialog {
    margin: 10px;
    max-height: 90vh;
  }
  
  .forward-messages {
    max-height: 300px;
  }
}
</style>
