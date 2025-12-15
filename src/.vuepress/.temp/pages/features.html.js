import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/features.html.vue"
const data = JSON.parse("{\"path\":\"/features.html\",\"title\":\"功能列表\",\"lang\":\"zh-CN\",\"frontmatter\":{\"title\":\"功能列表\",\"icon\":\"list-check\",\"order\":2,\"description\":\"功能列表 麦芽糖bot提供丰富的功能，满足您的各种需求。 🛠️ 只能私聊使用 🎨 🤖 AI语音生成 🎯 🎉 只能私聊使用 ⚙️ 如果您有功能建议，欢迎在官方群内提出！\"},\"readingTime\":{\"minutes\":8.06,\"words\":2418},\"filePathRelative\":\"features.md\",\"autoDesc\":true}")
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
