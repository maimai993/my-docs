import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/components-examples.html.vue"
const data = JSON.parse("{\"path\":\"/components-examples.html\",\"title\":\"VuePress 组件示例展示\",\"lang\":\"zh-CN\",\"frontmatter\":{\"description\":\"VuePress 组件示例展示 本页面展示了项目中所有 Vue 组件的使用示例。 组件列表 1. ChatMessage - 聊天消息组件 用于显示聊天消息，支持用户、机器人和系统三种类型。 实际效果： 2. RecallMessage - 消息撤回组件 模拟消息撤回效果，3秒后显示撤回样式。 实际效果： 3. SimpleImageMessage -...\",\"head\":[[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"VuePress 组件示例展示\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[{\\\"@type\\\":\\\"Person\\\",\\\"name\\\":\\\"麦麦\\\"}]}\"],[\"meta\",{\"property\":\"og:url\",\"content\":\"https://maltose-bot.com/components-examples.html\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"麦芽糖\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"VuePress 组件示例展示\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"VuePress 组件示例展示 本页面展示了项目中所有 Vue 组件的使用示例。 组件列表 1. ChatMessage - 聊天消息组件 用于显示聊天消息，支持用户、机器人和系统三种类型。 实际效果： 2. RecallMessage - 消息撤回组件 模拟消息撤回效果，3秒后显示撤回样式。 实际效果： 3. SimpleImageMessage -...\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"zh-CN\"}]]},\"readingTime\":{\"minutes\":3.59,\"words\":1077},\"filePathRelative\":\"components-examples.md\",\"autoDesc\":true}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
