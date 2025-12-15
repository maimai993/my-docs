import comp from "D:/fo/vuepress-theme-hope/my-docs/src/.vuepress/.temp/pages/使用指南/实用工具/火烧云预报.html.vue"
const data = JSON.parse("{\"path\":\"/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7/%E7%81%AB%E7%83%A7%E4%BA%91%E9%A2%84%E6%8A%A5.html\",\"title\":\"火烧云预报\",\"lang\":\"zh-CN\",\"frontmatter\":{\"title\":\"火烧云预报\",\"icon\":null,\"order\":1,\"description\":\"火烧云预报 概述 指令名称: hsy 功能描述: 查询和订阅城市朝霞(日出)和晚霞(日落)预报 插件名称: sunsetbot 架构图 使用方法 基本语法 参数说明 使用示例 查询火烧云预报 订阅城市预报 技术特性 预报模型: 使用GFS和EC两种气象模型 预报内容: 提供朝霞(rise)和晚霞(set)预报 预报时段: 当日和次日预报 自动推送: 每...\"},\"readingTime\":{\"minutes\":2.04,\"words\":612},\"filePathRelative\":\"使用指南/实用工具/火烧云预报.md\",\"autoDesc\":true}")
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
