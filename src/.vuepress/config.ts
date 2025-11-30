import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "麦芽糖",
  description: "vuepress-theme-hope 的麦芽糖",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
