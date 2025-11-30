import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/test-merge-forward.html.vue"
const data = JSON.parse("{\"path\":\"/test-merge-forward.html\",\"title\":\"测试简化后的 MergeForward 组件\",\"lang\":\"zh-CN\",\"frontmatter\":{\"description\":\"测试简化后的 MergeForward 组件 这是一个测试页面，用于验证简化后的 MergeForward 组件是否正常工作。 示例用法\"},\"readingTime\":{\"minutes\":0.18,\"words\":53},\"filePathRelative\":\"test-merge-forward.md\",\"autoDesc\":true}")
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
