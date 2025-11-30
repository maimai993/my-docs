import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/guide/bar/index.html.vue"
const data = JSON.parse("{\"path\":\"/guide/bar/\",\"title\":\"Bar 功能\",\"lang\":\"zh-CN\",\"frontmatter\":{\"title\":\"Bar 功能\",\"icon\":\"lightbulb\",\"description\":\"介绍 我们支持 bar 功能，... 详情 ...\",\"head\":[[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"Bar 功能\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[{\\\"@type\\\":\\\"Person\\\",\\\"name\\\":\\\"麦芽糖bot开发团队\\\"}]}\"],[\"meta\",{\"property\":\"og:url\",\"content\":\"https://maltose-bot.com/guide/bar/\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"麦芽糖\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"Bar 功能\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"介绍 我们支持 bar 功能，... 详情 ...\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"zh-CN\"}]]},\"readingTime\":{\"minutes\":0.07,\"words\":21},\"filePathRelative\":\"guide/bar/README.md\",\"autoDesc\":true}")
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
