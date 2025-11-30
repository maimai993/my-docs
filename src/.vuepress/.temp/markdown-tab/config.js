import { CodeTabs } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+plugin-markdown-t_4b89531936795501e214ede5fb24db69/node_modules/@vuepress/plugin-markdown-tab/lib/client/components/CodeTabs.js";
import { Tabs } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+plugin-markdown-t_4b89531936795501e214ede5fb24db69/node_modules/@vuepress/plugin-markdown-tab/lib/client/components/Tabs.js";
import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+plugin-markdown-t_4b89531936795501e214ede5fb24db69/node_modules/@vuepress/plugin-markdown-tab/lib/client/styles/vars.css";

export default {
  enhance: ({ app }) => {
    app.component("CodeTabs", CodeTabs);
    app.component("Tabs", Tabs);
  },
};
