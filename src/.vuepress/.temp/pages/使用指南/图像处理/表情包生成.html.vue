<template><div><h1 id="表情包生成" tabindex="-1"><a class="header-anchor" href="#表情包生成"><span>表情包生成</span></a></h1>
<h2 id="概述" tabindex="-1"><a class="header-anchor" href="#概述"><span>概述</span></a></h2>
<p><a href="https://koishi.chat" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/框架-koishi-5445a2?style=flat" alt="" loading="lazy"></a> <a href="https://www.npmjs.com/package/koishi-plugin-memes-api" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/npm/v/koishi-plugin-memes-api" alt="" loading="lazy"></a> <a href="https://github.com/lgc-KoiDev/koishi-plugin-memes-api" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/-github-202020?style=flat&amp;logo=github" alt="" loading="lazy"></a><br>
<strong>指令名称</strong>: meme</p>
<p><strong>功能描述</strong>: 提供多种模板的表情包生成功能，支持自定义文字和图片</p>
<p><strong>插件名称</strong>: memes-api</p>
<h2 id="主要功能指令" tabindex="-1"><a class="header-anchor" href="#主要功能指令"><span>主要功能指令</span></a></h2>
<h3 id="生成表情包" tabindex="-1"><a class="header-anchor" href="#生成表情包"><span>生成表情包</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>meme generate &#x3C;表情关键词> [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="查看表情详情" tabindex="-1"><a class="header-anchor" href="#查看表情详情"><span>查看表情详情</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>meme info &#x3C;表情关键词></span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="查看表情列表" tabindex="-1"><a class="header-anchor" href="#查看表情列表"><span>查看表情列表</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>meme list</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h3 id="随机生成表情" tabindex="-1"><a class="header-anchor" href="#随机生成表情"><span>随机生成表情</span></a></h3>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>meme random</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h2 id="快捷使用方式" tabindex="-1"><a class="header-anchor" href="#快捷使用方式"><span>快捷使用方式</span></a></h2>
<div class="language- line-numbers-mode" data-highlighter="shiki" data-ext="" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34"><pre class="shiki shiki-themes one-light one-dark-pro vp-code" v-pre=""><code class="language-"><span class="line"><span>&#x3C;表情关键词> [参数]</span></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h2 id="使用示例" tabindex="-1"><a class="header-anchor" href="#使用示例"><span>使用示例</span></a></h2>
<h3 id="生成-5000兆-表情" tabindex="-1"><a class="header-anchor" href="#生成-5000兆-表情"><span>生成 <code v-pre>5000兆</code> 表情</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">5000兆 我去 洛天依</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/meme1.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="生成-rua-表情" tabindex="-1"><a class="header-anchor" href="#生成-rua-表情"><span>生成 <code v-pre>rua</code> 表情</span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">rua -圆 @自己</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/meme2.gif" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="生成-微信支付-表情-特定参数-自定义二维码链接" tabindex="-1"><a class="header-anchor" href="#生成-微信支付-表情-特定参数-自定义二维码链接"><span>生成 <code v-pre>微信支付</code> 表情 <a href="#%E8%A1%A8%E6%83%85%E7%89%B9%E5%AE%9A%E5%8F%82%E6%95%B0%E7%A4%BA%E4%BE%8B"><code v-pre>特定参数</code></a> <code v-pre>自定义二维码链接</code></span></a></h3>
<chat-panel>
<chat-message nickname="用户" type="user">微信支付 --message https://tangbot.xyz/</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/meme3.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>具体参数用法请查看<a href="#%E8%A1%A8%E6%83%85%E7%89%B9%E5%AE%9A%E5%8F%82%E6%95%B0%E7%A4%BA%E4%BE%8B">表情特定参数示例</a></p>
</div>
<h2 id="完整表情包列表" tabindex="-1"><a class="header-anchor" href="#完整表情包列表"><span>完整表情包列表</span></a></h2>
<h3 id="文字表情包" tabindex="-1"><a class="header-anchor" href="#文字表情包"><span>文字表情包</span></a></h3>
<details>
  <summary>点击展开列表</summary>
<ul>
<li>5000兆 (5000choyen)</li>
<li>戒导 (abstinence)</li>
<li>逆转裁判气泡 (ace_attorney_dialog)</li>
<li>二次元入口 (acg_entrance)</li>
<li>添乱/给社会添乱 (add_chaos)</li>
<li>上瘾/毒瘾发作 (addiction)</li>
<li>一样 (alike)</li>
<li>支付宝支付 (alipay)</li>
<li>一直 (always)</li>
<li>我永远喜欢 (always_like)</li>
<li>防诱拐 (anti_kidnap)</li>
<li>阿尼亚喜欢 (anya_suki)</li>
<li>鼓掌 (applaud)</li>
<li>阿罗娜扔 (arona_throw)</li>
<li>升天 (ascension)</li>
<li>问问 (ask)</li>
<li>亚托莉枕头 (atri_pillow)</li>
<li>宁宁举牌 (ayachi_holdsign)</li>
<li>ba说 (ba_say)</li>
<li>继续干活/打工人 (back_to_work)</li>
<li>后空翻 (backflip)</li>
<li>悲报 (bad_news)</li>
<li>拍头 (beat_head)</li>
<li>揍 (beat_up)</li>
<li>啃 (bite)</li>
<li>真寻挨骂 (blamed_mahiro)</li>
<li>高血压 (blood_pressure)</li>
<li>蔚蓝档案标题/batitle (bluearchive)</li>
<li>波奇手稿 (bocchi_draft)</li>
<li>布洛妮娅举牌/大鸭鸭举牌 (bronya_holdsign)</li>
<li>奶茶 (bubble_tea)</li>
<li>遇到困难请拨打 (call_110)</li>
<li>咖波画 (capoo_draw)</li>
<li>咖波指 (capoo_point)</li>
<li>咖波撕 (capoo_rip)</li>
<li>咖波蹭/咖波贴 (capoo_rub)</li>
<li>咖波说 (capoo_say)</li>
<li>咖波炖 (capoo_stew)</li>
<li>咖波撞/咖波头槌 (capoo_strike)</li>
<li>舰长 (captain)</li>
<li>这个引起的 (caused_by_this)</li>
<li>奖状/证书 (certificate)</li>
<li>馋身子 (chanshenzi)</li>
<li>字符画 (charpic)</li>
<li>追列车/追火车 (chase_train)</li>
<li>国旗 (china_flag)</li>
<li>智乃扔/智乃抛 (chino_throw)</li>
<li>鼠鼠搓 (clauvio_twist)</li>
<li>小丑 (clown)</li>
<li>小丑面具 (clown_mask)</li>
<li>迷惑 (confuse)</li>
<li>兑换券 (coupon)</li>
<li>捂脸 (cover_face)</li>
<li>爬 (crawl)</li>
<li>群青 (cyan)</li>
<li>白天黑夜/白天晚上 (daynight)</li>
<li>像样的亲亲 (decent_kiss)</li>
<li>入典/典中典/黑白草图 (dianzhongdian)</li>
<li>恐龙/小恐龙 (dinosaur)</li>
<li>注意力涣散 (distracted)</li>
<li>离婚协议/离婚申请 (divorce)</li>
<li>狗都不玩 (dog_dislike)</li>
<li>管人痴 (dog_of_vtb)</li>
<li>不要靠近 (dont_go_near)</li>
<li>不要按 (dont_press)</li>
<li>别碰 (dont_touch)</li>
<li>douyin (douyin)</li>
<li>吃 (eat)</li>
<li>皇帝龙图 (emperor_dragon)</li>
<li>意若思镜 (erised_mirror)</li>
<li>灰飞烟灭 (fade_away)</li>
<li>狂爱/狂粉 (fanatic)</li>
<li>闭嘴/我爸爸 (father_work)</li>
<li>击剑/🤺 (fencing)</li>
<li>我打宿傩/我打宿傩吗 (fight_with_sunuo)</li>
<li>满脑子 (fill_head)</li>
<li>整点薯条 (find_chips)</li>
<li>流萤举牌 (firefly_holdsign)</li>
<li>闪瞎 (flash_blind)</li>
<li>弹/脑瓜崩 (flick)</li>
<li>红温 (flush)</li>
<li>回南天/水雾 (fogging)</li>
<li>关注 (follow)</li>
<li>芙莉莲拿 (frieren_take)</li>
<li>哈哈镜 (funny_mirror)</li>
<li>垃圾/垃圾桶 (garbage)</li>
<li>原神吃 (genshin_eat)</li>
<li>原神启动 (genshin_start)</li>
<li>喜报 (good_news)</li>
<li>google (google)</li>
<li>谷歌验证码 (google_captcha)</li>
<li>猩猩扔 (gorilla_throw)</li>
<li>鬼畜 (guichu)</li>
<li>手枪 (gun)</li>
<li>锤 (hammer)</li>
<li>凉宫春日举 (haruhi_raise)</li>
<li>高低情商/低高情商 (high_EQ)</li>
<li>打穿/打穿屏幕 (hit_screen)</li>
<li>记仇 (hold_grudge)</li>
<li>抱紧 (hold_tight)</li>
<li>抱/抱抱 (hug)</li>
<li>抱大腿 (hug_leg)</li>
<li>胡桃啃 (hutao_bite)</li>
<li>坐牢 (imprison)</li>
<li>不文明 (incivilization)</li>
<li>inside (intel_inside)</li>
<li>采访 (interview)</li>
<li>杰瑞盯 (jerry_stare)</li>
<li>假面骑士 (jiamianqishi)</li>
<li>急急国王 (jiji_king)</li>
<li>汐汐/今汐 (jinhsi)</li>
<li>旧病复发 (jiubingfufa)</li>
<li>啾啾 (jiujiu)</li>
<li>跳 (jump)</li>
<li>万花筒/万花镜 (kaleidoscope)</li>
<li>凯露指 (karyl_point)</li>
<li>远离 (keep_away)</li>
<li>压岁钱不要交给 (keep_your_money)</li>
<li>踢球 (kick_ball)</li>
<li>卡比锤/卡比重锤 (kirby_hammer)</li>
<li>亲/亲亲 (kiss)</li>
<li>可莉吃 (klee_eat)</li>
<li>敲 (knock)</li>
<li>心奈印章 (kokona_seal)</li>
<li>泉此方看 (konata_watch)</li>
<li>偷学 (learn)</li>
<li>左右横跳 (left_right_jump)</li>
<li>让我进去 (let_me_in)</li>
<li>舔糖/舔棒棒糖 (lick_candy)</li>
<li>等价无穷小 (lim_x_0)</li>
<li>听音乐 (listen_music)</li>
<li>小天使 (little_angel)</li>
<li>加载中 (loading)</li>
<li>看扁 (look_flat)</li>
<li>看图标 (look_this_icon)</li>
<li>循环 (loop)</li>
<li>寻狗启事 (lost_dog)</li>
<li>永远爱你 (love_you)</li>
<li>洛天依要/天依要 (luotianyi_need)</li>
<li>洛天依说/天依说 (luotianyi_say)</li>
<li>罗永浩说 (luoyonghao_say)</li>
<li>鲁迅说/鲁迅说过 (luxun_say)</li>
<li>真寻看书 (mahiro_readbook)</li>
<li>麦克阿瑟说 (maikease)</li>
<li>旅行伙伴觉醒 (maimai_awaken)</li>
<li>旅行伙伴加入 (maimai_join)</li>
<li>交个朋友 (make_friend)</li>
<li>结婚申请/结婚登记 (marriage)</li>
<li>流星 (meteor)</li>
<li>米哈游 (mihoyo)</li>
<li>上香 (mourning)</li>
<li>低语 (murmur)</li>
<li>我朋友说 (my_friend)</li>
<li>我的意见如下/我的意见是 (my_opinion)</li>
<li>我老婆/这是我老婆 (my_wife)</li>
<li>纳西妲啃/草神啃 (nahida_bite)</li>
<li>亚文化取名机/亚名 (name_generator)</li>
<li>需要/你可能需要 (need)</li>
<li>猫羽雫举牌/猫猫举牌 (nekoha_holdsign)</li>
<li>你好骚啊 (nihaosaoa)</li>
<li>伊地知虹夏举牌/虹夏举牌 (nijika_holdsign)</li>
<li>无响应 (no_response)</li>
<li>诺基亚/有内鬼 (nokia)</li>
<li>不喊我 (not_call_me)</li>
<li>请假条 (note_for_leave)</li>
<li>我推的网友 (oshi_no_ko)</li>
<li>osu (osu)</li>
<li>out (out)</li>
<li>加班 (overtime)</li>
<li>女神异闻录5预告信/P5预告信 (p5letter)</li>
<li>这像画吗 (paint)</li>
<li>小画家 (painter)</li>
<li>熊猫龙图 (panda_dragon_figure)</li>
<li>推锅/甩锅 (pass_the_buck)</li>
<li>拍 (pat)</li>
<li>佩佩举 (pepe_raise)</li>
<li>完美 (perfect)</li>
<li>摸/摸摸/摸头/rua (petpet)</li>
<li>捏/捏脸 (pinch)</li>
<li>像素化 (pixelate)</li>
<li>pjsk/世界计划 (pjsk)</li>
<li>普拉娜吃/普拉娜舔 (plana_eat)</li>
<li>顶/玩 (play)</li>
<li>打棒球 (play_baseball)</li>
<li>打篮球/火柴人打篮球 (play_basketball)</li>
<li>玩游戏 (play_game)</li>
<li>一起玩 (play_together)</li>
<li>出警 (police)</li>
<li>警察 (police1)</li>
<li>ph/pornhub (pornhub)</li>
<li>土豆 (potato)</li>
<li>捣 (pound)</li>
<li>打印 (printing)</li>
<li>舔/舔屏/prpr (prpr)</li>
<li>可达鸭 (psyduck)</li>
<li>打拳 (punch)</li>
<li>四棱锥/金字塔 (pyramid)</li>
<li>切格瓦拉 (qiegewala)</li>
<li>举 (raise_image)</li>
<li>举牌 (raise_sign)</li>
<li>看书 (read_book)</li>
<li>遥控/控制 (remote_control)</li>
<li>复读 (repeat)</li>
<li>撕 (rip)</li>
<li>怒撕 (rip_angrily)</li>
<li>撕衣服 (rip_clothes)</li>
<li>诈尸/秽土转生 (rise_dead)</li>
<li>滚 (roll)</li>
<li>三维旋转 (rotate_3d)</li>
<li>贴/贴贴/蹭/蹭蹭 (rub)</li>
<li>快跑 (run)</li>
<li>快逃 (run_away)</li>
<li>安全感 (safe_sense)</li>
<li>催眠app (saimin_app)</li>
<li>挠头 (scratch_head)</li>
<li>刮刮乐 (scratchcard)</li>
<li>滚屏 (scroll)</li>
<li>源石封印 (seal)</li>
<li>世界第一可爱 (sekaiichi_kawaii)</li>
<li>晃脑 (shake_head)</li>
<li>白子舔 (shiroko_pero)</li>
<li>食屎啦你 (shishilani)</li>
<li>震惊 (shock)</li>
<li>谁反对 (shuifandui)</li>
<li>别说了 (shutup)</li>
<li>坐得住/坐的住 (sit_still)</li>
<li>一巴掌 (slap)</li>
<li>口号 (slogan)</li>
<li>砸 (smash)</li>
<li>卖掉了 (sold_out)</li>
<li>无语 (speechless)</li>
<li>球面旋转 (sphere_rotate)</li>
<li>蜘蛛/蜘蛛爬 (spider)</li>
<li>盯着你 (stare_at_you)</li>
<li>steam消息 (steam_message)</li>
<li>踩 (step_on)</li>
<li>炖 (stew)</li>
<li>跳舞/火柴人跳舞 (stickman_dancing)</li>
<li>科目三 (subject3)</li>
<li>吸/嗦 (suck)</li>
<li>精神支柱 (support)</li>
<li>回旋转/旋风转 (swirl_turn)</li>
<li>对称 (symmetric)</li>
<li>唐可可举牌 (tankuku_raisesign)</li>
<li>嘲讽 (taunt)</li>
<li>讲课/敲黑板 (teach)</li>
<li>拿捏/戏弄 (tease)</li>
<li>望远镜 (telescope)</li>
<li>体温枪 (thermometer_gun)</li>
<li>想什么 (think_what)</li>
<li>这是鸡/🐔 (this_chicken)</li>
<li>丢/扔 (throw)</li>
<li>抛/掷 (throw_gif)</li>
<li>捶 (thump)</li>
<li>捶爆/爆捶 (thump_wildly)</li>
<li>紧贴/紧紧贴着 (tightly)</li>
<li>该走了 (time_to_go)</li>
<li>一起 (together)</li>
<li>汤姆嘲笑 (tom_tease)</li>
<li>上坟/坟前比耶 (tomb_yeah)</li>
<li>顶尖 (top_notch)</li>
<li>恍惚 (trance)</li>
<li>推车 (trolley)</li>
<li>转 (turn)</li>
<li>搓 (twist)</li>
<li>万能表情/空白表情 (universal)</li>
<li>反了 (upside_down)</li>
<li>震动 (vibrate)</li>
<li>好起来了 (wakeup)</li>
<li>墙纸 (wallpaper)</li>
<li>胡桃平板 (walnut_pad)</li>
<li>胡桃放大 (walnut_zoom)</li>
<li>王境泽 (wangjingze)</li>
<li>洗衣机 (washer)</li>
<li>波纹 (wave)</li>
<li>微信支付 (wechat_pay)</li>
<li>为所欲为 (weisuoyuwei)</li>
<li>我想上的 (what_I_want_to_do)</li>
<li>最想要的东西 (what_he_wants)</li>
<li>为什么@我 (why_at_me)</li>
<li>为什么要有手 (why_have_hands)</li>
<li>风车转 (windmill_turn)</li>
<li>许愿失败 (wish_fail)</li>
<li>木鱼 (wooden_fish)</li>
<li>膜/膜拜 (worship)</li>
<li>吴京中国 (wujing)</li>
<li>五年怎么过的 (wunian)</li>
<li>乌鸦哥 (wuyage)</li>
<li>压力大爷 (yalidaye)</li>
<li>椰树椰汁 (yeshu)</li>
<li>你不懂啦 (you_dont_get)</li>
<li>致电/你应该致电 (you_should_call)</li>
<li>你的跨年 (your_new_years_eve)</li>
<li>yt/youtube (youtube)</li>
<li>曾小贤 (zengxiaoxian)</li>
<li>雷军举牌 (mi_leijun_holdsign)</li>
<li>刘伟说大伟说大伟哥说 (mihoyo_liuwei_say)</li>
<li>和泉纱雾画画 (izumi_sagiri_painting)</li>
<li>今汐坐 (kurogames_jinhsi_sit)</li>
<li>扔史 (throwing_poop)</li>
<li>弗洛洛吃 (kurogames_phrolova_eat)</li>
<li>漂泊者舔 (kurogames_rover_lick)</li>
<li>舰载激光武器 (shipborne_laser_weapons)</li>
<li>okOKOk (ok)</li>
<li>薇尔莉特 (violet_evergarden)</li>
<li>玉足 (mihoyo_columbina_jade_feet)</li>
<li>没救了希格雯指 (mihoyo_sigewinne_fingered)</li>
<li>骑士doro骑士Doro骑士DORO骑士 (doro_knight)</li>
<li>国庆快乐国庆节快乐 (happy_national_day)</li>
<li>骑马 (horse_riding)</li>
<li>周边写真 (doro_surrounding_photos)</li>
<li>猫舔猫猫舔 (cat_lick)</li>
<li>开灯桃乐丝开灯doro开灯Doro开灯DORO开灯 (doro_openlight)</li>
<li>摸鱼 (slacking_off)</li>
<li>被窝 (quilt)</li>
<li>比心 (sending_love)</li>
<li>放屁 (fart)</li>
<li>家人们谁懂啊 (family_know)</li>
<li>燃起来了 (ignite)</li>
<li>看看腿 (look_leg)</li>
<li>符咒 (rune)</li>
<li>新年好 (happy_new_year)</li>
<li>心跳 (heartbeat)</li>
<li>咖波砸蛋 (capoo_smash_egg)</li>
<li>Ciallo～(∠・ω&lt; )⌒★CiallocialloCiallo<sub>ciallo</sub>Ciallo～(∠・ω&lt; )⌒☆ (yuzu_soft_ciallo)</li>
<li>猫抓猫猫抓 (cat_scratch)</li>
<li>咖波掏 (capoo_fished_out)</li>
<li>ly01ly-1LY-1 (ly01)</li>
<li>坤坤想要 (ikun_need_tv)</li>
<li>土豆地雷 (potato_mines)</li>
<li>松伦晚餐松伦哥晚餐 (kurogames_songlun_dinner)</li>
<li>刘伟晚餐共进晚餐大伟哥晚餐 (mihoyo_liuwei_dinner)</li>
</ul>
</details>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>该列表仅包含部分表情，请以 <code v-pre>meme list</code> 为准确</p>
</div>
<h2 id="表情详情示例" tabindex="-1"><a class="header-anchor" href="#表情详情示例"><span>表情详情示例</span></a></h2>
<h3 id="_5000兆" tabindex="-1"><a class="header-anchor" href="#_5000兆"><span>5000兆</span></a></h3>
<p><strong>关键词</strong>: 5000兆<br>
<strong>需要图片数目</strong>: 0<br>
<strong>需要文字数目</strong>: 2<br>
<strong>默认文字</strong>: [我去, 洛天依]<br>
<strong>预览</strong>: [图片]</p>
<h3 id="戒导" tabindex="-1"><a class="header-anchor" href="#戒导"><span>戒导</span></a></h3>
<p><strong>关键词</strong>: 戒导<br>
<strong>需要图片数目</strong>: 1<br>
<strong>需要文字数目</strong>: 0<br>
<strong>参数</strong>:</p>
<ul>
<li><code v-pre>-t/--time &lt;time: str&gt;</code> 指定时间</li>
<li><code v-pre>-n/--name &lt;name: str&gt;</code> 指定名字<br>
<strong>预览</strong>: [图片]</li>
</ul>
<h3 id="阿尼亚喜欢" tabindex="-1"><a class="header-anchor" href="#阿尼亚喜欢"><span>阿尼亚喜欢</span></a></h3>
<p><strong>关键词</strong>: 阿尼亚喜欢<br>
<strong>标签</strong>: &quot;间谍过家家&quot;、&quot;阿尼亚·福杰&quot;<br>
<strong>需要图片数目</strong>: 1<br>
<strong>需要文字数目</strong>: 0 ~ 1<br>
<strong>默认文字</strong>: [阿尼亚喜欢这个]<br>
<strong>预览</strong>: [图片]</p>
<h2 id="表情特定参数示例" tabindex="-1"><a class="header-anchor" href="#表情特定参数示例"><span>表情特定参数示例</span></a></h2>
<ul>
<li>戒导:<br>
<code v-pre>-t/--time &lt;time&gt;</code> 指定时间<br>
<code v-pre>-n/--name &lt;name&gt;</code> 指定名字</li>
<li>支付宝支付/微信支付:<br>
<code v-pre>-m/--message &lt;message&gt;</code> 指定二维码内容</li>
<li>原神吃:<br>
<code v-pre>-c/--character &lt;character&gt;</code> 指定角色编号</li>
<li>咖波系列:<br>
<code v-pre>-p/--position &lt;position&gt;</code> 指定位置(right/left/both)</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>该参数列表仅包含部分表情<br>
您可以使用 <code v-pre>[关键词] -h</code> 查看支持的参数详情</p>
</div>
<chat-panel>
<chat-message nickname="用户" type="user">支付宝支付 -h</chat-message>
<chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/meme5.png" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>此帮助图里显示有可用参数 <code v-pre>--message</code> [二维码内容]</p>
</div>
<chat-message nickname="用户" type="user">原来这个二维码可以<span style="color: #31de8dff;">自定义内容啊</span></chat-message><div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>当内容是标准链接时<br>
扫描二维码会自动跳转到该链接</p>
</div>
<chat-message nickname="用户" type="user">支付宝支付 --message https://tangbot.xyz/</chat-message><chat-message nickname="bot" type="bot">
<figure><img src="@source/使用指南/图像处理/meme6.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
</chat-message>
</chat-panel>
<h3 id="参数格式说明" tabindex="-1"><a class="header-anchor" href="#参数格式说明"><span>参数格式说明</span></a></h3>
<ol>
<li>参数可以单独使用或组合使用</li>
<li>多个参数用空格分隔</li>
<li>带值的参数格式为 <code v-pre>-参数名 值</code> 或 <code v-pre>--参数名=值</code></li>
<li>布尔参数只需指定参数名即可启用</li>
</ol>
<h2 id="技术特性" tabindex="-1"><a class="header-anchor" href="#技术特性"><span>技术特性</span></a></h2>
<ul>
<li><strong>模板系统</strong>: 基于预定义的表情包模板</li>
<li><strong>文字渲染</strong>: 自动调整文字大小和位置以适应模板</li>
<li><strong>图片处理</strong>: 智能裁剪和调整上传图片以适应模板</li>
<li><strong>缓存机制</strong>: 缓存常用模板和生成结果</li>
<li><strong>并发处理</strong>: 支持同时处理多个生成请求</li>
<li><strong>图片压缩</strong>: 自动优化生成的表情包大小</li>
</ul>
<h2 id="注意事项" tabindex="-1"><a class="header-anchor" href="#注意事项"><span>注意事项</span></a></h2>
<ol>
<li>部分模板可能涉及版权问题，请谨慎使用</li>
<li>建议使用清晰度高、背景简单的图片</li>
<li>单行文字建议不超过15个字符</li>
<li>多行文字建议不超过3行</li>
<li>复杂模板可能需要更长的生成时间</li>
</ol>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>表情包生成功能基于meme-generator-api实现，能够快速生成各种流行的表情包模板。该功能简单实用，适合日常娱乐和社交分享。</p>
</div>
</div></template>


