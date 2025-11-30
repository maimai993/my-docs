<template>
  <div class="simple-image-message" ref="messageElement">
    <div v-if="text" class="text-content">
      {{ text }}
    </div>
    <div class="image-container">
      <img 
        :src="imageSrc" 
        :alt="imageAlt" 
        :style="imageStyle"
        @load="onImageLoad"
        @error="onImageError"
        ref="imageElement"
      />
      <div v-if="loading" class="image-loading">
        <div class="loading-spinner"></div>
        <span>加载中...</span>
      </div>
      <div v-if="loadError" class="image-error">
        <span>图片加载失败</span>
      </div>
    </div>
    <div v-if="caption" class="image-caption">
      {{ caption }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SimpleImageMessage',
  props: {
    imageSrc: {
      type: String,
      required: true
    },
    imageAlt: {
      type: String,
      default: '图片'
    },
    text: {
      type: String,
      default: ''
    },
    caption: {
      type: String,
      default: ''
    },
    maxWidth: {
      type: [String, Number],
      default: 380
    },
    maxHeight: {
      type: [String, Number],
      default: 280
    },
    borderRadius: {
      type: String,
      default: '8px'
    }
  },
  data() {
    return {
      loading: true,
      loadError: false,
      naturalWidth: 0,
      naturalHeight: 0,
      displayWidth: 0,
      displayHeight: 0
    }
  },
  computed: {
    imageStyle() {
      const style = {
        borderRadius: this.borderRadius,
        maxWidth: '100%',
        height: 'auto',
        display: this.loading || this.loadError ? 'none' : 'block'
      }

      // 如果已经计算了显示尺寸，使用计算后的尺寸
      if (this.displayWidth && this.displayHeight) {
        style.width = `${this.displayWidth}px`
        style.height = `${this.displayHeight}px`
      }

      return style
    }
  },
  methods: {
    onImageLoad(event) {
      this.loading = false
      this.loadError = false
      
      const img = event.target
      this.naturalWidth = img.naturalWidth
      this.naturalHeight = img.naturalHeight
      
      this.calculateDisplaySize()
    },
    
    onImageError() {
      this.loading = false
      this.loadError = true
    },
    
    calculateDisplaySize() {
      const maxWidth = typeof this.maxWidth === 'string' ? 
        parseInt(this.maxWidth) : this.maxWidth
      const maxHeight = typeof this.maxHeight === 'string' ? 
        parseInt(this.maxHeight) : this.maxHeight
      
      let width = this.naturalWidth
      let height = this.naturalHeight
      
      // 如果图片宽度超过最大宽度，按比例缩放
      if (width > maxWidth) {
        const ratio = maxWidth / width
        width = maxWidth
        height = height * ratio
      }
      
      // 如果缩放后的高度仍然超过最大高度，再次按比例缩放
      if (height > maxHeight) {
        const ratio = maxHeight / height
        height = maxHeight
        width = width * ratio
      }
      
      this.displayWidth = Math.round(width)
      this.displayHeight = Math.round(height)
    }
  }
}
</script>

<style scoped>
.simple-image-message {
  display: inline-block;
  max-width: 100%;
  margin: 8px 0;
}

.text-content {
  margin-bottom: 8px;
  font-size: 14px;
  color: var(--vp-c-text-1);
  line-height: 1.5;
  word-wrap: break-word;
  white-space: pre-wrap;
}

.image-container {
  position: relative;
  display: inline-block;
  max-width: 100%;
}

.image-container img {
  transition: opacity 0.3s ease;
  border: 1px solid var(--vp-c-border);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.image-loading,
.image-error {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: var(--vp-c-text-2);
  font-size: 14px;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid var(--vp-c-border);
  border-top: 2px solid var(--vp-c-brand);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 8px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.image-caption {
  margin-top: 8px;
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.4;
  text-align: center;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .simple-image-message {
    max-width: 90%;
  }
}
</style>
