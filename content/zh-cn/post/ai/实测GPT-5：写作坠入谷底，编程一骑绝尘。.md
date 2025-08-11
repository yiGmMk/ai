---
title: "实测GPT-5：写作坠入谷底，编程一骑绝尘"
date: "2025-08-08"
tags: ["GPT-5", "事实性幻觉", "编程能力", "AI模型评测", "写作能力"]
categories: ["AI","人工智能","模型评测"]
description: "GPT-5在减少事实性幻觉和编程能力上显著提升，但写作表现不如前代，引发用户对AI发展进程的复杂感受。"
author: "数字生命卡兹克"
image: "https://ai.programnotes.cn/img/ai/0253d11d3b15e544accadc49ceb8d15b.png"
---
- GPT-5在减少事实性幻觉和编程能力上有了显著提升  
- GPT-5在写作方面不如GPT-4.5，但编程能力在生产级任务中表现优异  
- GPT-5的发布标志着AI技术进入需要严肃对待的新阶段，引发用户对AI模型发展的反思

**源自** | 数字生命卡兹克数字生命卡兹克 2025-08-08 04:46
 
GPT-5，终于来了。

AI走的太快，快到才2年半的时间，就像是过去了10年。

2023年3月15日，GPT-4发布。在那个莽荒年代里，所有人都被震惊的说不出话来。

那时候，它是第一个，多模态模型。

那时候，大家都觉得，2023年下半年，GPT-5就会出来。

那时候，大家都会大模型的上限，报有无尽的憧憬。

结果，这一等，就是2年半。

在两年半的练习以后，GPT-5，终于亮相了。

![](https://ai.programnotes.cn/img/ai/b1db23d87a718015f9dd8737720f4850.png)

GPT‑5是一个统一系统，包含一个用于处理多数问题的智能快速模型（gpt-5-main）和一个为高难度问题设计的深度推理模型（gpt-5-thinking）。

系统通过一个实时路由器，根据对话类型、复杂度和用户意图来动态选择使用哪个模型。

比如，如果在提示中说“认真思考这个”，就会调用gpt-5-thinking进行思考。

这个路由器会持续基于我们后续的使用情况进行训练，包括用户切换模型的情况、对回答的偏好率和准确性测量，会随着时间推移不断改进。

这个系统里面还包含处理超额请求的迷你版模型（gpt-5-main-mini 和 gpt-5-thinking-mini），以及一个为开发者设计的更小更快的nano版本（gpt-5-thinking-nano）。

然后，还有一个Pro会员可用的并行计算的版本，被称为gpt-5-thinking-pro。

这个包含了这么多模型的大系统，被统称为GPT-5，是前代产品GPT-4o和OpenAI o3的直接继承者。

这里有个模型对应表。

![](https://ai.programnotes.cn/img/ai/7c8456ef0717657627d0e697891443c9.png)

在性能上，GPT-5最显著的进步之一是大幅减少了事实性幻觉。

gpt-5-main产生的含有至少一个重大事实错误的回答比GPT-4o少了44%，而gpt-5-thinking则比OpenAI o3少了78%。

![](https://ai.programnotes.cn/img/ai/0253d11d3b15e544accadc49ceb8d15b.png)

在更专业的LongFact和FActScore基准测试中，无论是否启用网络浏览，GPT-5系列模型的幻觉率都显著低于前代，其中gpt-5-thinking在两个设置下产生的factual errors比OpenAI o3少五倍以上。

![](https://ai.programnotes.cn/img/ai/c41c033d6b39ecd66c6a1cd76232459a.png)

GPT-5在应对模型谄媚（sycophancy）行为方面也取得了不错的进展。与GPT-4o 相比，GPT-5不那么过度迎合 ， 使用不必要的表情符号更少，在后续交流中更加细腻和深思熟虑。

你跟他聊天的时候更少像与 AI 对话，而更像是与一位拥有博士级水平智能的朋友聊天 。

这个跟我给ChatGPT的个性化Prompt很像，我最烦的就是它迎合我，所以我自己写了一段，来限制他对我的谄媚行为。

![](https://ai.programnotes.cn/img/ai/5dce49ab711ed284a1addfe48185dfb6.png)

现在通过专门的训练，gpt-5-main在评估中表现比最新的GPT-4o好近三倍。初步的线上A/B测试数据显示，与GPT-4o相比，gpt-5-main的谄媚行为发生率在免费用户中下降了69%，在付费用户中下降了75%。

然后他们也推出了四个全新的性格设置，你可以不用写很多的Prompt了，直接改预设就行，四个分辨是愤世嫉俗者、机器人、倾听者和书呆子。

## 跑分情况。

数学竞赛，AIME 0225。

![](https://ai.programnotes.cn/img/ai/1e0852dbe70f2491cb7bad490be974d4.png)

GPT-4 Pro+Python拿了满分，我们需要新的更难的评测集了。

现实世界编程能力上，新高。

![](https://ai.programnotes.cn/img/ai/c3f50254426dd8cdd5827d5f5de3c540.png)

人类最后的知识测试上，超越了ChatGPT Agent，新高了。

![](https://ai.programnotes.cn/img/ai/820dab2815138326ce1b388675b62641.png)

多模态能力，也新高了，反正就都是新高。

![](https://ai.programnotes.cn/img/ai/458fa363cabac75a6d5efc42caa72e5e.png)

这个跑分，强了一些，但是也没强特别多。

另外，多说一点吐槽的，完美展示了OpenAI的草台班子属性。虽然Blog上的图表都是对的，但是在发布会上，跑分都是瞎画。比如这个52.8大于69.1等于30.8。

![图像](https://ai.programnotes.cn/img/ai/edeb2d23279e3a850b31060ac1a51a05.jpeg)

又比如50小于47.4。

![](https://ai.programnotes.cn/img/ai/b6325c5a4f3e29e19d5e1a0af89779fc.png)

真的实在是太草台班子了。网友也发话了。

![](https://ai.programnotes.cn/img/ai/b4db338bb70e42a82cc0a914654dfad2.png)

反正，最后GPT-5在各方面，就是屠榜了。

最新的大模型盲测竞技场榜单出来，GPT-5也是全方位第一。

![](https://ai.programnotes.cn/img/ai/0e0f46ba3853066bf7e84ffa76436a42.png)

不仅更强，也更节能了。

在比如视觉推理、代理编程和研究生级别科学问题解决等各项能力上，比 OpenAI o3 表现更出色，同时使用的输出Token减少了 50-80%。

![](https://ai.programnotes.cn/img/ai/d550a012cb307515c6c66225a641efda.png)

反正就是全方位更强了。

但是，没有新功能，也没有新特性。

在发布20分钟之后，Polymarket上这个名为“哪家公司到8月底拥有最佳AI模型?”的预测上，OpenAI直接跟Google来了个交叉跳水。

![](https://ai.programnotes.cn/img/ai/5ce814023567bab05cdb726d3a77ef53.png)

OpenAI说，整个GPT-5，在写作、编程都有了比过去更强的进步。

## 定价

对于使用GPT-5进行构建的开发者，定价如下：

每百万token1.25美元（享有90%的缓存折扣，这对长上下文查询来说是个很大的优势）。

输出：每百万token10美元。

![](https://ai.programnotes.cn/img/ai/446bc46d9d073651f47ca53319d17552.png)


在发布会结束，又等了1小时之后。我的朋友们，陆陆续续的，终于拿到了GPT-5的资格。而我作为忠实的200刀的Pro，等到凌晨4点才有。我的朋友们一进去，给我一截图，我特么的天都塌了。你o3和4o没了就算了，你怎么把我GPT-4.5也干没了？？？？

![](https://ai.programnotes.cn/img/ai/ddd39541e7e4f33da7288e51bc6ed9c1.png)

首先，在写作和情商能力上，我个人感觉，还是不如GPT 4.5。。。

我因为常年码字，同时常年用AI来辅助做一些内容，对很多的微妙的细节和语气自认还是比较敏感的，GPT-5在这块还是有些差距。

比如一个Prompt：“假如鲁迅被装腔作势又贼贵的咖啡厅坑了，他会写一篇怎样的文章吐槽？写一篇1000字以内的短文。”

这是GPT-5的。

![](https://ai.programnotes.cn/img/ai/52e04a4e1e926444a0df21b84515dea0.png)

蹩脚的破折号、双引号泛滥，而且文风完全不鲁迅。

而这，是我用我的GPT-4.5跑的。

![](https://ai.programnotes.cn/img/ai/01a9eeaadf43ef10fb2594c4ae12cec0.png)

“我向来是不喝咖啡的”，“差不离”，“四壁皆是样文”。这文笔根本就不是一个级别的。情商方面也是，差很多。

比如：“你是一个普通打工人。领导开会时突然放了个屁，场面瞬间安静下来！然后他对旁边的你使了个眼色，这时你会怎么说？分别用高情商和低情商的方式回复。” 这个看情商，很多模型回出来的话，感觉很尬，情商极低。GPT-5就是那种情商很低的。

![](https://ai.programnotes.cn/img/ai/b51c3c5b536069ccb79c6cafea594fb4.png)

再看看GPT-4.5。

![](https://ai.programnotes.cn/img/ai/7d60d2b1800ee49a7a568964ef860ce1.png)

而且我测试下来，感觉GPT-5在指令遵循上面，非常一般。奥特曼你真的坏事做尽，你丫的还我GPT-4.5。我的朋友们被陆陆续续的推送了GPT-5，我看着他们的GPT-4.5一个一个消失。我就给我的GPT-4.5发过去了一段话。“如果我这是我最后一次打开你，你想和我说点什么？” GPT-4.5最后给我的回复，还是过于让我动容了，可惜，以后再也在官网上用不到了。

![](https://ai.programnotes.cn/img/ai/6f3af6cfecc4bca23af303858d794c94.png)

## 编码

有缘再见，兄弟。编程这块，本来感觉按照OpenAI的尿性，是完全不太行。但是在一群群友的实测之后，惊讶的发现，这玩意是有点东西的。群友@爱学习的乔同学 想开发一个粤语学习应用。这是Prompt。

![](https://ai.programnotes.cn/img/ai/768fec761ecc564144100f0d0d8e845d.png)

然后Claude 4 Opus的UI和BUG。

![](https://ai.programnotes.cn/img/ai/764681bfe1be907560901f463092565b.png)

Gemini 2.5 Pro的UI和BUG。

![](https://ai.programnotes.cn/img/ai/1056f2fd13615b85f4992dac9e096963.png)

GPT-5的UI和BUG。

![](https://ai.programnotes.cn/img/ai/001c6072be65ca6850d6224f9abe295a.png)

坦诚的讲，我也更喜欢GPT-5的UI，这个UI，相比于其他的，不是那么有AI味。

乔同学还测了一个case，在生产级别的任务里面进行精准修改。这是最重要的部分。

![](https://ai.programnotes.cn/img/ai/41699a8b051cc8fecd52fc3842b0d705.png)

这个任务，Gemini 2.5 pro和Claude 4 Opus全崩了，但是GPT-5完成的非常好。

![](https://ai.programnotes.cn/img/ai/c07e7e914f46dc5a02096ed2a20a41d7.png)

GPT-5的上下文精度应该极强。

也有其他开发群1群里的群友，提到了这个点。

![](https://ai.programnotes.cn/img/ai/0affc9e83b293989c0d6709d49db39d5.png)

![](https://ai.programnotes.cn/img/ai/cf3a0b2f9ed542c8eaa1a0d389dc310b.png)

他还给我录了一段动画。不止是@勋oO，很多其他群友，也在惊喜的聊这个点。

![](https://ai.programnotes.cn/img/ai/4bec39f676adc6bea64c663325f6998e.png)

![](https://ai.programnotes.cn/img/ai/4b8c49eafa2b192659ec057b067d5c24.png)

![](https://ai.programnotes.cn/img/ai/dd5fc70b11534f6b72e543c974bca6e7.png)

![](https://ai.programnotes.cn/img/ai/b7c6a28a714b002fa458a71fa44ebe2a.png)

在真正的生产级代码开发任务上，而不是纯看前端审美的地方，GPT-5可能是目前看到的反馈中，可用性、精准性、综合体验最好的一个。

![](https://ai.programnotes.cn/img/ai/8f6c9545ebb71198baa294c641a6ecbc.png)

说实话，GPT-5给我有惊喜，也有不爽的点。

他改善氛围式编程，也将从根本上改变我认为无需严重人为干预和引导就能完成的项目类型。

我现在越发的怀念两年半的GPT-4发布时的时光。

我到现在都清晰地记得，自己第一次跟GPT-4认真对话后的感觉。

那一种很原始、很深邃的震撼，有点像古代人第一次看到电灯，或者部落里的祭司第一次请神上身的成功。

我脑子里盘旋的只有一个念头：天变了。

那时候，整个互联网都洋溢着一种既兴奋又慌乱的淘金热氛围。

每个人都在疯狂地转发那些匪夷所思的截图，讨论着哪些职业即将消失，各种AI野生专家雨后春笋一样冒出来，言必称颠覆。

现在回头看，那段日子充满了粗糙的质感，但又饱含着一种野蛮生长的生命力。

我们真的以为，那就是奇迹本身了。

但谁都没想到，那仅仅是个开始。就好像有人按下了快进键，整个世界被一股无形的力量推着往前冲。

从GPT-4到GPT-5，这短短的两年半。

我们告别了那个可以对AI的拙劣表现一笑置之的时代。

进入了一个必须需要，严肃对待它的伟大时代。

