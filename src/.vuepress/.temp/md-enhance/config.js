import CodeDemo from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-plugin-md-enhance@_2b4e43ebf7cb95bb46b166b79f4f6409/node_modules/vuepress-plugin-md-enhance/lib/client/components/CodeDemo.js";
import MdDemo from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-plugin-md-enhance@_2b4e43ebf7cb95bb46b166b79f4f6409/node_modules/vuepress-plugin-md-enhance/lib/client/components/MdDemo.js";

export default {
  enhance: ({ app }) => {
    app.component("CodeDemo", CodeDemo);
    app.component("MdDemo", MdDemo);
  },
};
