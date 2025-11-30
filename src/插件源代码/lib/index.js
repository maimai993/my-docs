"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.apply = exports.Config = exports.name = void 0;
const koishi_1 = require("koishi");
const qrcode_1 = require("qrcode");
exports.name = 'QRCode';
exports.Config = koishi_1.Schema.object({});
function apply(ctx) {
    ctx.i18n.define('zh', require('./locales/zh'));
    ctx.command('qrcode <text:text>')
        .option('margin', '-m <margin>', { fallback: 4 })
        .option('scale', '-s <scale>', { fallback: 4 })
        .option('width', '-w <width>')
        .option('dark', '-d <color>')
        .option('light', '-l <color>')
        .action(async ({ options, session }, text) => {
        if (!text)
            return session.text('.expect-text');
        if (text.includes('[CQ:'))
            return session.text('.invalid-segment');
        const { margin, scale, width, dark, light } = options;
        const dataURL = await (0, qrcode_1.toDataURL)(text, { margin, scale, width, color: { dark, light } });
        // data:image/png;base64,
        return koishi_1.segment.image('base64://' + dataURL.slice(22));
    });
}
exports.apply = apply;
