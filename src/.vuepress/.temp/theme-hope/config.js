import { Layout, NotFound, injectDarkMode, setupDarkMode, setupSidebarItems, scrollPromise } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-theme-hope@2.0.0-r_31226c9b5695aaf3537c930a2aad7e1c/node_modules/vuepress-theme-hope/lib/bundle/exports/base.js";

import { defineCatalogInfoGetter } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+plugin-catalog@2._f2e90827e0245cd6a7237838a8c351d8/node_modules/@vuepress/plugin-catalog/lib/client/index.js"
import { h } from "vue"
import { resolveComponent } from "vue"
import { GlobalEncrypt, LocalEncrypt } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-theme-hope@2.0.0-r_31226c9b5695aaf3537c930a2aad7e1c/node_modules/vuepress-theme-hope/lib/bundle/exports/encrypt.js";
import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-theme-hope@2.0.0-r_31226c9b5695aaf3537c930a2aad7e1c/node_modules/vuepress-theme-hope/lib/bundle/styles/encrypt/bundle.scss"

import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/styles/colors.css";
import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/styles/normalize.css";
import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/styles/sr-only.css";
import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-theme-hope@2.0.0-r_31226c9b5695aaf3537c930a2aad7e1c/node_modules/vuepress-theme-hope/lib/bundle/styles/bundle.scss";

defineCatalogInfoGetter((meta) => {
  const title = meta.title;
  const shouldIndex = meta.index ?? true;
  const icon = meta.icon;

  return shouldIndex ? {
    title,
    content: icon ? () =>[h(resolveComponent("VPIcon"), { icon, sizing: "both" }), title] : null,
    order: meta.order,
    index: meta.index,
  } : null;
});

export default {
  enhance: ({ app, router }) => {
    const { scrollBehavior } = router.options;

    router.options.scrollBehavior = async (...args) => {
      await scrollPromise.wait();

      return scrollBehavior(...args);
    };

    // inject global properties
    injectDarkMode(app);

    app.component("GlobalEncrypt", GlobalEncrypt);
    app.component("LocalEncrypt", LocalEncrypt);
  },
  setup: () => {
    setupDarkMode();
    setupSidebarItems();

  },
  layouts: {
    Layout,
    NotFound,

  }
};
