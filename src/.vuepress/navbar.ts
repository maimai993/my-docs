import { navbar } from "vuepress-theme-hope";

export default navbar([
  "/",
  {
    text: "快速开始",
    icon: "rocket",
    link: "/quick-start",
  },
  {
    text: "查看功能",
    icon: "list-check",
    link: "/features",
  },
  {
    text: "使用指南",
    icon: "book",
    children: [
      {
        text: "实用工具",
        icon: "wrench",
        link: "/使用指南/实用工具/",
      },
      {
        text: "图像处理",
        icon: "image",
        link: "/使用指南/图像处理/",
      },
      {
        text: "AI功能",
        icon: "robot",
        link: "/使用指南/AI功能/",
      },
      {
        text: "游戏相关",
        icon: "gamepad",
        link: "/使用指南/游戏相关/",
      },
      {
        text: "娱乐功能",
        icon: "play",
        link: "/使用指南/娱乐功能/",
      },
      {
        text: "群组管理",
        icon: "users",
        link: "/使用指南/群组管理/",
      },
    ],
  },
  {
    text: "部署配置",
    icon: "gear",
    children: [
      {
        text: "准备工作",
        icon: "server",
        link: "/部署配置/",
      },
    ],
  },
  {
    text: "关于我们",
    icon: "users",
    link: "/portfolio",
  },
]);
