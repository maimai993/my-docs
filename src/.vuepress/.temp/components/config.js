import { hasGlobalComponent } from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/index.js";
import Badge from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-plugin-components@_b4adc1a66a199aac6761c3cd8086b80d/node_modules/vuepress-plugin-components/lib/client/components/Badge.js";
import VPCard from "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/vuepress-plugin-components@_b4adc1a66a199aac6761c3cd8086b80d/node_modules/vuepress-plugin-components/lib/client/components/VPCard.js";

import "D:/fo/vuepress-theme-hope/my-docs/node_modules/.pnpm/@vuepress+helper@2.0.0-rc.1_dbd85768717be86c42cc765ce09aa19d/node_modules/@vuepress/helper/lib/client/styles/sr-only.css";

export default {
  enhance: ({ app }) => {
    if(!hasGlobalComponent("Badge")) app.component("Badge", Badge);
    if(!hasGlobalComponent("VPCard")) app.component("VPCard", VPCard);
    
  },
  setup: () => {

  },
  rootComponents: [

  ],
};
