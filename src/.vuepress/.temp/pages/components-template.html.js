import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/components-template.html.vue"
const data = JSON.parse("{\"path\":\"/components-template.html\",\"title\":\"[项目名称] 组件示例展示\",\"lang\":\"zh-CN\",\"frontmatter\":{\"description\":\"[项目名称] 组件示例展示 本页面展示了项目中所有 Vue 组件的使用示例。 组件列表 1. [组件名称] - [组件描述] [在此处添加组件的详细描述，说明其用途和功能] 实际效果： <[组件名称] [属性1]=\\\"[示例值1]\\\" [属性2]=\\\"[示例值2]\\\"> [示例内容] </[组件名称]> 2. [组件名称] - [组件描述] [在此处添加组件的...\"},\"readingTime\":{\"minutes\":0.79,\"words\":237},\"filePathRelative\":\"components-template.md\",\"autoDesc\":true}")
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
