import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/": [
    "",
    {
      text: "快速开始",
      icon: "rocket",
      link: "quick-start",
    },
    {
      text: "功能列表",
      icon: "list-check",
      link: "features",
    },
    {
      text: "使用指南",
      icon: "book",
      link: "使用指南/",
      prefix: "使用指南/",
      collapsible: true,
      children: [
        {
          text: "实用工具",
          icon: "wrench",
          link: "实用工具/",
          prefix: "实用工具/",
          collapsible: true,
          children: "structure",
        },
        {
          text: "图像处理",
          icon: "image",
          link: "图像处理/",
          prefix: "图像处理/",
          collapsible: true,
          children: "structure",
        },
        {
          text: "AI功能",
          icon: "robot",
          link: "AI功能/",
          prefix: "AI功能/",
          collapsible: true,
          children: "structure",
        },
        {
          text: "游戏相关",
          icon: "gamepad",
          link: "游戏相关/",
          prefix: "游戏相关/",
          collapsible: true,
          children: "structure",
        },
        {
          text: "娱乐功能",
          icon: "play",
          link: "娱乐功能/",
          prefix: "娱乐功能/",
          collapsible: true,
          children: "structure",
        },
        {
          text: "群组管理",
          icon: "users",
          link: "群组管理/",
          prefix: "群组管理/",
          collapsible: true,
          children: "structure",
        },
      ],
    },
    {
      text: "部署配置",
      icon: "gear",
      link: "features",
    },
  ],
});
