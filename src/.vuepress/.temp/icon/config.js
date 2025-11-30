import { hasGlobalComponent } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/index.js";
import { useScriptTag } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vueuse+core@13.9.0_vue@3.5.22/node_modules/@vueuse/core/index.mjs";
import { h } from "vue";
import { VPIcon } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+plugin-icon@2.0.0_cef3658ee811e418fd0dd4be9d631e4e/node_modules/@vuepress/plugin-icon/lib/client/index.js"

export default {
  enhance: ({ app }) => {
    if(!hasGlobalComponent("VPIcon")) {
      app.component(
        "VPIcon",
        (props) =>
          h(VPIcon, {
            type: "iconify",
            prefix: "fa6-solid:",
            ...props,
          })
      )
    }
  },
  setup: () => {
    useScriptTag(`https://cdn.jsdelivr.net/npm/iconify-icon@2`);
  },
}
