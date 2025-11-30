<template>
  <div class="file-message" ref="messageElement">
    <div class="file-card" :class="fileCardClass">
      <!-- 支持预览的文件类型：图片、视频 -->
      <div v-if="isPreviewable" class="previewable-file">
        <!-- 图片预览 -->
        <div v-if="fileType === 'image'" class="image-preview">
          <img 
            :src="previewUrl || downloadUrl" 
            :alt="fileName"
            @load="onPreviewLoad"
            @error="onPreviewError"
            class="preview-image"
          />
          <div v-if="previewLoading" class="preview-loading">
            <div class="loading-spinner"></div>
            <span>加载中...</span>
          </div>
          <div v-if="previewError" class="preview-error">
            <span>预览加载失败</span>
          </div>
        </div>
        
        <!-- 视频预览 -->
        <div v-if="fileType === 'video'" class="video-preview">
          <video 
            :src="previewUrl || downloadUrl" 
            :alt="fileName"
            controls
            @loadstart="onPreviewLoad"
            @error="onPreviewError"
            class="preview-video"
          >
            您的浏览器不支持视频播放
          </video>
          <div v-if="previewLoading" class="preview-loading">
            <div class="loading-spinner"></div>
            <span>加载中...</span>
          </div>
          <div v-if="previewError" class="preview-error">
            <span>预览加载失败</span>
          </div>
        </div>
        
        <!-- 文件信息（支持预览的文件：名称在下面） -->
        <div class="file-info previewable-info">
          <div class="file-name">{{ fileName }}</div>
          <div class="file-size">{{ formattedSize }}</div>
        </div>
      </div>
      
      <!-- 不支持预览的文件类型 -->
      <div v-else class="non-previewable-file">
        <div class="file-icon">
          <span class="icon" :class="fileIconClass">{{ fileIcon }}</span>
        </div>
        <div class="file-info">
          <div class="file-name">{{ fileName }}</div>
          <div class="file-size">{{ formattedSize }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FileMessage',
  props: {
    fileName: {
      type: String,
      required: true
    },
    fileSize: {
      type: [String, Number],
      default: 0
    },
    downloadUrl: {
      type: String,
      required: true
    },
    previewUrl: {
      type: String,
      default: ''
    },
    fileType: {
      type: String,
      default: 'unknown' // 'image', 'video', 'audio', 'document', 'archive', 'unknown'
    }
  },
  data() {
    return {
      previewLoading: false,
      previewError: false,
      isVisible: false
    }
  },
  computed: {
    isPreviewable() {
      return ['image', 'video'].includes(this.fileType)
    },
    
    formattedSize() {
      const size = Number(this.fileSize)
      if (size === 0) return '未知大小'
      
      const units = ['B', 'KB', 'MB', 'GB']
      let unitIndex = 0
      let formattedSize = size
      
      while (formattedSize >= 1024 && unitIndex < units.length - 1) {
        formattedSize /= 1024
        unitIndex++
      }
      
      return `${formattedSize.toFixed(unitIndex === 0 ? 0 : 1)} ${units[unitIndex]}`
    },
    
    fileCardClass() {
      return {
        'previewable': this.isPreviewable,
        'non-previewable': !this.isPreviewable,
        'visible': this.isVisible
      }
    },
    
    fileIcon() {
      const iconMap = {
        audio: '🎵',
        video: '🎬',
        document: '📄',
        archive: '📦',
        image: '🖼️',
        unknown: '📎'
      }
      return iconMap[this.fileType] || iconMap.unknown
    },
    
    fileIconClass() {
      return `file-icon-${this.fileType}`
    }
  },
  methods: {
    onPreviewLoad() {
      this.previewLoading = false
      this.previewError = false
    },
    
    onPreviewError() {
      this.previewLoading = false
      this.previewError = true
    },
    
    startPreviewLoading() {
      if (this.isPreviewable && (this.previewUrl || this.downloadUrl)) {
        this.previewLoading = true
        this.previewError = false
      }
    }
  },
  mounted() {
    this.startPreviewLoading()
    
    // 滚动动画
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
.file-message {
  position: relative;
  margin: 1rem 0;
  opacity: 1;
  transform: translateX(0);
}

.file-message.visible {
  opacity: 1;
  transform: translateX(0);
}

.file-card {
  position: relative;
  max-width: 320px;
  transition: all 0.3s ease;
}

/* 支持预览的文件样式 */
.previewable-file {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.image-preview,
.video-preview {
  position: relative;
  border-radius: 6px;
  overflow: hidden;
}

.preview-image {
  width: 100%;
  height: auto;
  max-height: 200px;
  object-fit: contain;
  display: block;
}

.preview-video {
  width: 100%;
  height: auto;
  max-height: 200px;
  display: block;
}

.previewable-info {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 8px;
  margin-top: 4px;
}

/* 不支持预览的文件样式 */
.non-previewable-file {
  display: flex;
  align-items: center;
  gap: 12px;
}

.file-icon {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  border: 1px solid var(--vp-c-border);
}

.file-icon .icon {
  font-size: 20px;
  line-height: 1;
}

.file-info {
  flex: 1;
  min-width: 0;
  padding-right: 8px;
}

.file-name {
  font-weight: 600;
  font-size: 14px;
  color: var(--vp-c-text-1);
  margin-bottom: 2px;
  word-break: break-all;
  line-height: 1.4;
}

.file-size {
  font-size: 12px;
  color: var(--vp-c-text-2);
  line-height: 1.2;
}

/* 下载按钮区域 */
.download-section {
  position: absolute;
  bottom: 0;
  right: 0;
  z-index: 1;
}

.download-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  background: var(--vp-c-brand);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 500;
  transition: all 0.2s ease;
  border: none;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.download-btn:hover {
  background: var(--vp-c-brand-dark);
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.download-icon {
  font-size: 14px;
  line-height: 1;
}

.download-text {
  line-height: 1;
}

/* 加载和错误状态 */
.preview-loading,
.preview-error {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: var(--vp-c-text-2);
  font-size: 12px;
  background: var(--vp-c-bg-soft);
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid var(--vp-c-border);
}

.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid var(--vp-c-border);
  border-top: 2px solid var(--vp-c-brand);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 4px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .file-card {
    max-width: 280px;
  }
  
  .file-name {
    font-size: 13px;
  }
  
  .file-size {
    font-size: 11px;
  }
  
  .download-btn {
    padding: 3px 6px;
    font-size: 10px;
  }
  
  .preview-image,
  .preview-video {
    max-height: 160px;
  }
  
  .non-previewable-file {
    padding-right: 50px;
    gap: 8px;
  }
}

/* 文件类型特定的图标颜色 */
.file-icon-audio {
  color: #ff6b6b;
}

.file-icon-video {
  color: #4ecdc4;
}

.file-icon-document {
  color: #45b7d1;
}

.file-icon-archive {
  color: #96ceb4;
}

.file-icon-image {
  color: #feca57;
}

.file-icon-unknown {
  color: #778beb;
}

/* 深色模式适配 */
@media (prefers-color-scheme: dark) {
  .file-icon {
    background: var(--vp-c-bg-soft);
    border-color: var(--vp-c-border);
  }
  
  .preview-loading,
  .preview-error {
    background: var(--vp-c-bg-soft);
    border-color: var(--vp-c-border);
  }
  
  .image-preview,
  .video-preview {
    background: var(--vp-c-bg-soft);
  }
}

/* VuePress 深色模式类适配 */
.dark .file-icon {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-border);
}

.dark .preview-loading,
.dark .preview-error {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-border);
}

.dark .image-preview,
.dark .video-preview {
  background: var(--vp-c-bg-soft);
}
</style>
