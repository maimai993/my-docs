<template>
  <div 
    class="voice-message" 
    :class="{ 'is-playing': isPlaying, 'is-listened': isListened }" 
    ref="messageElement"
    @click="handleContainerClick"
    :style="{ cursor: 'pointer' }"
  >
    <!-- 播放/暂停按钮 -->
    <button class="play-btn" @click.stop="togglePlay" :aria-label="isPlaying ? '暂停语音' : '播放语音'">
      <span class="play-icon" v-if="!isPlaying">▶</span>
      <span class="pause-icon" v-else>⏸</span>
    </button>
    
    <!-- 语音波形（模拟） -->
    <div class="voice-waveform">
      <div 
        v-for="(bar, index) in waveformBars" 
        :key="index" 
        class="wave-bar"
        :class="{ 'active': isPlaying && index === currentBar }"
        :style="{ height: bar.height + 'px' }"
      ></div>
    </div>
    
    <!-- 语音时长 -->
    <div class="voice-duration">
      <span class="duration-text">{{ formattedDuration }}</span>
      <span class="duration-unit">"</span>
    </div>
    
    <!-- 语音状态指示器（小红点） -->
    <div class="voice-status" v-if="!isListened">
      <span class="status-dot"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VoiceMessage',
  props: {
    duration: {
      type: Number,
      default: 0 // 语音时长，单位：秒
    },
    isListened: {
      type: Boolean,
      default: false // 是否已收听
    },
    audioUrl: {
      type: String,
      default: '' // 音频URL（可选）
    }
  },
  data() {
    return {
      isPlaying: false,
      isVisible: false,
      currentTime: 0,
      waveformBars: [],
      currentBar: 0,
      barInterval: null,
      playTimer: null,
      audio: null, // Audio实例
      isLoading: false, // 音频加载状态
      error: null // 错误信息
    }
  },
  computed: {
    formattedDuration() {
      if (this.duration <= 0) return '0'
      return Math.round(this.duration)
    }
  },
  methods: {
    // 处理容器点击事件
    handleContainerClick(event) {
      // 如果点击的是播放按钮，不处理（因为按钮有自己的点击事件）
      if (event.target.closest('.play-btn')) {
        return
      }
      this.togglePlay()
    },
    
    togglePlay() {
      if (this.isPlaying) {
        this.pauseAudio()
      } else {
        this.playAudio()
      }
    },
    
    playAudio() {
      // 如果没有音频URL，使用模拟播放
      if (!this.audioUrl) {
        this.simulatePlay()
        return
      }
      
      this.isLoading = true
      this.error = null
      
      // 如果音频实例不存在，创建新的
      if (!this.audio) {
        this.audio = new Audio(this.audioUrl)
        
        // 设置音频事件监听器
        this.audio.addEventListener('loadedmetadata', () => {
          this.isLoading = false
          // 如果组件有duration prop，使用它；否则使用音频的实际时长
          if (!this.duration && this.audio.duration) {
            this.$emit('duration-update', Math.round(this.audio.duration))
          }
        })
        
        this.audio.addEventListener('canplay', () => {
          this.isLoading = false
        })
        
        this.audio.addEventListener('error', (e) => {
          this.isLoading = false
          this.error = '音频加载失败'
          console.error('音频播放错误:', e)
          // 回退到模拟播放
          this.simulatePlay()
        })
        
        this.audio.addEventListener('ended', () => {
          this.pauseAudio()
          // 标记为已收听
          if (!this.isListened) {
            this.$emit('listened')
          }
        })
        
        this.audio.addEventListener('timeupdate', () => {
          if (this.audio) {
            this.currentTime = this.audio.currentTime
          }
        })
      }
      
      // 播放音频
      this.audio.play().then(() => {
        this.isPlaying = true
        this.isLoading = false
        this.startWaveformAnimation()
        
        // 更新播放进度定时器
        this.playTimer = setInterval(() => {
          if (this.audio && !this.audio.paused) {
            this.currentTime = this.audio.currentTime
          }
        }, 100)
      }).catch((error) => {
        this.isLoading = false
        this.error = '播放失败: ' + error.message
        console.error('播放失败:', error)
        // 回退到模拟播放
        this.simulatePlay()
      })
    },
    
    // 模拟播放（当没有音频URL或音频加载失败时使用）
    simulatePlay() {
      this.isPlaying = true
      this.startWaveformAnimation()
      
      // 模拟播放进度
      this.currentTime = 0
      this.playTimer = setInterval(() => {
        if (this.currentTime < this.duration) {
          this.currentTime += 0.1
        } else {
          this.pauseAudio()
          // 标记为已收听
          if (!this.isListened) {
            this.$emit('listened')
          }
        }
      }, 100)
      
      console.log('模拟播放音频，时长:', this.duration, '秒')
    },
    
    pauseAudio() {
      this.isPlaying = false
      this.stopWaveformAnimation()
      
      // 停止真实音频
      if (this.audio && !this.audio.paused) {
        this.audio.pause()
      }
      
      // 清除定时器
      if (this.playTimer) {
        clearInterval(this.playTimer)
        this.playTimer = null
      }
    },
    
    startWaveformAnimation() {
      // 生成随机波形条
      if (this.waveformBars.length === 0) {
        this.generateWaveform()
      }
      
      // 开始波形动画
      this.barInterval = setInterval(() => {
        this.currentBar = (this.currentBar + 1) % this.waveformBars.length
      }, 150)
    },
    
    stopWaveformAnimation() {
      if (this.barInterval) {
        clearInterval(this.barInterval)
        this.barInterval = null
      }
    },
    
    generateWaveform() {
      // 生成随机高度的波形条
      const barCount = 12
      this.waveformBars = []
      
      for (let i = 0; i < barCount; i++) {
        // 随机高度，但中间的高一些，两边的低一些（模拟真实波形）
        const baseHeight = 8
        const variation = Math.sin((i / barCount) * Math.PI) * 6
        const randomVariation = Math.random() * 3
        const height = baseHeight + variation + randomVariation
        
        this.waveformBars.push({
          height: Math.max(4, Math.min(20, height))
        })
      }
    }
  },
  mounted() {
    this.generateWaveform()
    
    // 滚动动画（可选）
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

    if (this.$refs.messageElement) {
      observer.observe(this.$refs.messageElement)
    }
  },
  
  beforeUnmount() {
    this.pauseAudio()
    
    // 清理音频资源
    if (this.audio) {
      this.audio.pause()
      this.audio.src = ''
      this.audio = null
    }
    
    // 清理定时器
    if (this.barInterval) {
      clearInterval(this.barInterval)
      this.barInterval = null
    }
    if (this.playTimer) {
      clearInterval(this.playTimer)
      this.playTimer = null
    }
  }
}
</script>

<style scoped>
.voice-message {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background-color: var(--vp-c-bg);
  border-radius: 6px;
  border: 1px solid var(--vp-c-border);
  user-select: none;
  transition: all 0.2s ease;
  min-width: 120px;
  max-width: 200px;
  cursor: pointer;
}

.voice-message:hover {
  background-color: var(--vp-c-bg-soft);
  border-color: var(--vp-c-brand);
}

.voice-message.is-playing {
  background-color: var(--vp-c-bg-alt);
  border-color: var(--vp-c-brand);
}

.play-btn {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: var(--vp-c-brand);
  color: white;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 10px;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.play-btn:hover {
  background-color: var(--vp-c-brand-dark);
  transform: scale(1.05);
}

.voice-waveform {
  display: flex;
  align-items: center;
  gap: 2px;
  height: 24px;
  flex: 1;
}

.wave-bar {
  width: 2px;
  background-color: var(--vp-c-text-2);
  border-radius: 1px;
  transition: all 0.3s ease;
}

.wave-bar.active {
  background-color: var(--vp-c-brand);
  transform: scaleY(1.2);
}

.voice-duration {
  display: flex;
  align-items: baseline;
  font-size: 12px;
  color: var(--vp-c-text-2);
  flex-shrink: 0;
  margin-left: 4px;
}

.duration-text {
  font-weight: 600;
}

.duration-unit {
  font-size: 10px;
  margin-left: 1px;
}

.voice-status {
  margin-left: 4px;
}

.status-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--vp-c-red);
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% {
    opacity: 0.6;
    transform: scale(0.9);
  }
  50% {
    opacity: 1;
    transform: scale(1.1);
  }
  100% {
    opacity: 0.6;
    transform: scale(0.9);
  }
}

/* 已收听状态 */
.voice-message.is-listened .wave-bar {
  background-color: var(--vp-c-text-3);
}

.voice-message.is-listened .play-btn {
  background-color: var(--vp-c-text-3);
}

.voice-message.is-listened .voice-duration {
  color: var(--vp-c-text-3);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .voice-message {
    padding: 6px 10px;
    min-width: 100px;
    max-width: 160px;
  }
  
  .play-btn {
    width: 20px;
    height: 20px;
    font-size: 8px;
  }
  
  .voice-waveform {
    height: 20px;
  }
  
  .voice-duration {
    font-size: 11px;
  }
}
</style>
