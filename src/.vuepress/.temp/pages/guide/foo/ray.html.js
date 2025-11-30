import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/guide/foo/ray.html.vue"
const data = JSON.parse("{\"path\":\"/guide/foo/ray.html\",\"title\":\"Ray\",\"lang\":\"zh-CN\",\"frontmatter\":{\"title\":\"Ray\",\"icon\":\"circle-info\",\"description\":\"功能详情...\",\"head\":[[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"Ray\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[{\\\"@type\\\":\\\"Person\\\",\\\"name\\\":\\\"麦芽糖bot开发团队\\\"}]}\"],[\"meta\",{\"property\":\"og:url\",\"content\":\"https://maltose-bot.com/guide/foo/ray.html\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"麦芽糖\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"Ray\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"功能详情...\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"zh-CN\"}]]},\"readingTime\":{\"minutes\":0.03,\"words\":10},\"filePathRelative\":\"guide/foo/ray.md\",\"autoDesc\":true}")
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
