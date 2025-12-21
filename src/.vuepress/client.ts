import { defineClientConfig } from 'vuepress/client'
import ChatMessage from './components/ChatMessage.vue'
import ChatPanel from './components/ChatPanel.vue'
import MergeForward from './components/MergeForward.vue'
import RecallMessage from './components/RecallMessage.vue'
import SimpleImageMessage from './components/SimpleImageMessage.vue'
import FileMessage from './components/FileMessage.vue'
import VoiceMessage from './components/VoiceMessage.vue'


export default defineClientConfig({
  enhance({ app, router, siteData }) {
    // 全局注册自定义组件
    app.component('ChatMessage', ChatMessage)
    app.component('ChatPanel', ChatPanel)
    app.component('MergeForward', MergeForward)
    app.component('RecallMessage', RecallMessage)
    app.component('SimpleImageMessage', SimpleImageMessage)
    app.component('FileMessage', FileMessage)
    app.component('VoiceMessage', VoiceMessage)

    
    // 您可以在这里注册更多自定义组件
    // app.component('YourComponentName', YourComponent)
  },
  
  setup() {
    // 客户端设置逻辑
  },
  
  rootComponents: [
    // 根组件
  ],
})
