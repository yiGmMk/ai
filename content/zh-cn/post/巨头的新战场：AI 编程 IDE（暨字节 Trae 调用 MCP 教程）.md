---
title: "巨头的新战场：AI 编程 IDE（暨字节 Trae 调用 MCP 教程）"
date: "2025-04-22"
tags: ["AI", "IDE", "编程", "MCP", "Trae", "字节跳动", "OpenAI", "Windsurf"]
categories: ["人工智能", "软件开发"]
description: "本文介绍了AI编程IDE的最新发展趋势，以及字节跳动Trae IDE如何调用MCP，扩展AI能力。"
author: "阮一峰"
image: "https://ai.programnotes.cn/img/ai/4913db0a11fa1ae3aabc45db299f8d8c.other"
---

核心内容点1:  AI编程IDE成为巨头竞争的新战场。
核心内容点2: 字节跳动Trae IDE通过MCP调用扩展AI功能。
核心内容点3: MCP协议简化了AI与外部应用的连接。

**源自** |  阮一峰  阮一峰的网络日志   2025-04-22 15:11  
  
## 一、引言  
  
本周，我要加写一篇文章。  
  
因为 AI 编程 IDE 突然成了热门，国内外都有大事发生。  
  
![](https://ai.programnotes.cn/img/ai/4913db0a11fa1ae3aabc45db299f8d8c.other)  
  
先说国外，OpenAI 要用30亿美元收购 Windsurf[1]。  
  
这个消息太惊人。Windsurf（前身叫做 Codeium）的历史很短，发布至今两年多，市场份额也不高，居然值这么多钱！  
  
OpenAI 最新一轮融资（今年3月）不过400亿美元[2]，现在一下子要拿出30亿去收购，看中 Windsurf 哪一点呀！  
  
OpenAI 自己没有编程助手，所以唯一的解释是，它要收购 IDE 打入 AI 编程市场，这个市场对它很重要。  

## 二、MarsCode 更名 Trae  
  
再看国内，字节也有大动作。  
  
它旗下的编程助手，最早是 MarsCode 插件，后来又多了一个独立的 AI IDE 产品Trae[3]。  
  
![](https://ai.programnotes.cn/img/ai/817a9bdeff2ea52ea60b4c0a3fc8de37.other)  
  
本周，MarsCode 宣布改名为 Trae 插件[4]，不再作为独立品牌发展了。  
  
以后，**字节的 AI 编程助手，将只有 Trae 这一个品牌**，分成两种产品形态。  
  
习惯传统 IDE 的用户，可以加装 Trae 插件；想要更好 AI 体验的用户，可以安装独立的 Trae IDE。  
  
这个消息公布的同时，Trae 新版本也一起发布，加入了重磅的新功能（后面会详谈）。  
  
可以看出，字节是下了决心，整合了产品，准备在 AI 编程工具上发力了。  
## 三、AI IDE + MCP  
  
为什么国内外的巨头，在同一个时间，不约而同都看上了 AI IDE？  
  
我猜想，答案是 MCP 的出现。  
  
有了 MCP 以后，AI IDE 可以扩展外部能力，从而无所不能，这让它成为巨头的必争之地。  
  
![](https://ai.programnotes.cn/img/ai/a90755c6b441ea16d6786f1201813415.other)  
  
下面，我来解释 MCP 是什么，怎么在 Trae 里面调用。大家看了，就会理解为什么 MCP 这么重要。  
## 四、Trae 的简介  
  
我选择 Trae 来演示，主要因为它是国产软件，有中文界面和文档，并且完全免费（国外产品都需要付费）。  
  
前面说过，Trae 分成插件和 IDE 两种形态，它的 IDE 又分成国内版和海外版。这些产品的功能基本一致，就是内置的 AI 模型不一样。  
> 国内版：内置 deepseek R1、V3、v3-0324 和 doubao 1.5 pro 模型  
> 海外版：内置 Claude 3.5、3.7，Gemini 2.5 pro，GPT-4o、GPT-4.1 模型  
  
  
我建议使用国内版，因为海外版的内置模型经常需要排队，很浪费时间，而且可能还会通信不畅。  
  
不过，**这两个版本都支持自定义模型**  
，你可以提供密钥，接入你指定的模型。所以，版本的差别也不算很重要。  
  
![](https://ai.programnotes.cn/img/ai/1e8f395052f6d381a63769f44935955c.other)  
  
顺便提一下，Trae 这个词的意思是“**T**he**R**eal**A**I**E**ngineer”（真正的 AI 工程师）。我以前总是以为 Trae 的意思是 True Ai。  

## 五、Trae 的新版本  
  
Trae 的 MCP 调用功能，是从新版本 v0.5.0 开始加入的。  
  
没安装的朋友，可以去官网[5]下载新版。已经安装的朋友，请检查一下版本。  
  
它的界面这一次简化了，聊天框和 Builder（项目生成）合并成一个对话框（下图）。所有跟 AI 的对话，都在这里输入。  
  
![](https://ai.programnotes.cn/img/ai/39d4b2baa387a0a6b6f98762acbe0b0a.other)  
  
上图中，左下角多了两个按钮：“@智能体”和“#上下文”。这就是本次新增的核心功能。  
  
至于 Trae 的基本用法，这里就不提了，可以看  
[以前的文章](https://mp.weixin.qq.com/s?__biz=MzI4NjAxNjY4Nw==&mid=2650240097&idx=1&sn=52d38ba994d9f2a53f3c3c3a37b7632e&scene=21#wechat_redirect)  
[6]  
。  
## 六、调用智能体  
  
MCP 调用的入口，就是上图左下角的“@智能体”按钮。  
  
如果想要扩展 AI 的功能，就要使用这个按钮。因为 AI 模型的本质只是语言模型，自身的功能是有限的，必须通过外部应用（智能体）来扩展功能。  
  
点击“@智能体”（或者输入@），就会弹出一个对话框，显示目前可用的智能体（下图）。  
  
![](https://ai.programnotes.cn/img/ai/8433f0ebbc47c849b64075fea49b5ca1.other)  
  
可以看到，Trae 内置了两个智能体:“@Build” 和 “@Builder with MCP”。  
  
其中，“@Build”用来让 AI 生成一个可运行的新项目。  
> @Build 俄罗斯方块网页小游戏  
  
  
输入上面的命令，就会生成一个 HTML 文件，打开就是俄罗斯方块小游戏。  
  
![](https://ai.programnotes.cn/img/ai/c566082f23c911a966b10dae9ce4b93c.other)  
  
另一个内置的智能体“@Build with MCP”，就是用来连接 MCP 服务器。
  
## 七、MCP 是什么  
  
我先解释一下，MCP 是什么，很容易理解。  
  
我们知道，AI 模型通过连接外部应用，来扩展功能。每个外部应用的接口，都不一样，如果要接入10个应用，就要写10种接入代码，非常麻烦。而且，要是换一个模型，可能所有接入代码都要重写。  
  
![](https://ai.programnotes.cn/img/ai/8ebb4a7c1bf369a9f8951723e9ac6a1a.other)  
  
有鉴于此，Anthropic 公司在2024年11月提出了 MCP 协议。外部应用只需要支持这个协议，提供一个 MCP 接口（又称 MCP 服务器），那么 AI 模型就可以用统一的格式接入，不需要了解外部应用的接入细节。  
  
所以，**MCP 可以理解成一个 AI 与外部应用之间的适配层**  
。对于 AI 来说，只要安装某个应用的 MCP 服务器，就能接入该应用，不用写任何代码（除了少数的配置项）。  
  
由于 MCP 解决了 AI 应用的接入痛点，诞生至今仅半年，已经变得极其流行，就连 Anthropic 的竞争对手 OpenAI 公司都公开支持，网上开源的 MCP 服务器项目已经有上万个。  
## 八、调用 MCP  
  
现在就来看 Trae 怎么调用 MCP。  
  
点击 AI 标签栏右上角的齿轮图标，弹出一个菜单，选择菜单项 MCP。  
  
![](https://ai.programnotes.cn/img/ai/95d790b14f49dd853e2f0274e2a50f95.other)  
  
它会跳出一个 MCP 的标签页（下图），点击底部的“+ 添加 MCP Servers”。  
  
![](https://ai.programnotes.cn/img/ai/80c615c2c464fb950ed11a36b52dea32.other)  
  
Trae 内置了 MCP 市场，提供一些常用的 MCP 服务器。如果里面没有你需要的，可以点击“手动配置”，添加你自己的 MCP。  
  
![](https://ai.programnotes.cn/img/ai/66a90b1d282cf6f0ccac3a4624fd97db.other)  
  
为了便于演示，我选择第一个服务器 Puppeteer，让 AI 可以调用无头浏览器。  
  
鼠标点击 Puppeteer 的名字，会进入该开源项目的主页，可以查看一下它提供的内部命令（即能力）。  
  
![](https://ai.programnotes.cn/img/ai/43b6887c7626ebd40187072f791be58e.other)  
  
上图中可以看到，这个 MCP 服务器提供 puppeteer_navigator（打开指定网址）、puppeteer_screenshot（截图）、puppeteer_select（选中页面元素）等内部命令，供 AI 模型调用。  
  
用户不需要记住这些命令，只需了解它有哪些能力就可以了。  
  
接着，点击它后面的加号，添加该 MCP 服务器。  
  
![](https://ai.programnotes.cn/img/ai/673d55b11f39472c853aa7a0dd114c95.other)  
  
这个 MCP 带有“轻松配置”标签，表示不需要任何设置，可以直接运行。  
  
![](https://ai.programnotes.cn/img/ai/3f73910dabb2bceb86c0e21b6032b08a.other)  
  
所有自己添加的 MCP，默认都放在内置的智能体“@Build with MCP”，所以可以通过这个智能体来使用。  
  
在 AI 对话框里面，选中智能体“@Build with MCP”，然后输入下面的命令“打开 https://www.baidu.com”，试试看新安装的 Puppeteer 服务器。  
  
![](https://ai.programnotes.cn/img/ai/b72e0a122699ca9a4be359dc21952d39.other)  
  
正常情况下，Trae 会让你选择一个项目文件夹，然后就会打开一个浏览器窗口，显示百度的首页。  
  
![](https://ai.programnotes.cn/img/ai/6c0b16eb30d28f673d1f58dd057c59bd.other)  
  
这就是 MCP 的作用。AI 本来没有能力控制浏览器，但是现在就可以通过 MCP 来控制。  
  
接着，可以给出一些更复杂的命令，比如生成截图，也能顺利完成。  
  
![](https://ai.programnotes.cn/img/ai/51b1fd49d521b796e1b26ad0107e1f24.other)  
  
这就是调用 MCP 的基本流程。你还可以把添加的 MCP 服务器保存成智能体（下图）。  
  
![](https://ai.programnotes.cn/img/ai/010226efcb2481a5074dd5ba4082d5a7.other)  
  
然后，通过你起的名字，调用该智能体（下图），从而连接指定的 MCP 服务器。  
  
![](https://ai.programnotes.cn/img/ai/f3b76874b4cfcad32e6c2c0ec0e99507.other)  
## 九、上下文功能  
  
除了 MCP 调用，Trae 的本次更新，还加强了上下文功能，这里也简单提一下。  
  
所谓上下文，就是额外提供的信息，帮助 AI 模型思考，来完成任务。  
  
通过#  
号，可以调出上下文菜单。  
  
![](https://ai.programnotes.cn/img/ai/133a2029fccbd09a280d2be3fb3849a7.other)  
  
从上图可以看到，可以提供的上下文，包括额外的代码（code）、文件（file）、目录（folder）、工作区（workspace）。  
  
本次更新多了两个选项，“Doc”表示额外的文档。  
  
![](https://ai.programnotes.cn/img/ai/39c9a33ecf31a6962252f2c03b0d4e6e.other)  
  
点击“添加文档集”，就可以添加文档目录，作为 AI 模型的上下文。  
  
![](https://ai.programnotes.cn/img/ai/a93287d06e89ae97e9b45b1601064996.other)  
  
另一个选项“Web”，表示用网上信息作为上下文。这为 AI 提供了实时联网能力。  
  
![](https://ai.programnotes.cn/img/ai/317a2550c56cec9fa8274fe183e96317.other)  
  
![](https://ai.programnotes.cn/img/ai/0a96b866ae4bb321153f42a2fe0b0ece.other)  
  
上图的实时天气问题，AI 只有具有联网能力，才能回答。  
## 十、总结  
  
有了 MCP 调用和联网能力，AI IDE 就具备了巨大的想象空间，不仅仅是编程工具，而成了一个无所不能的 AI 控制台。  
  
那些大公司一定是看到了这一点，所以才愿意投入大量资源，去做这个产品。  
  
我认为，在 AI IDE 里面调用 MCP 服务器，将成为近期软件业的热点，值得大家重点关注。  
  
（完）  
### References  
  
[1]收购 Windsurf:https://www.jiemian.com/article/12627036.html  
[2]400亿美元:https://www.cnbc.com/2025/03/31/openai-closes-40-billion-in-funding-the-largest-private-fundraise-in-history-softbank-chatgpt.html  
[3]Trae:https://sourl.cn/dLaMpy  
[4]改名为 Trae 插件:https://docs.trae.com.cn/plugin/faq  
[5]官网:https://sourl.cn/dLaMpy  
[6]以前的文章: http://www.ruanyifeng.com/blog/2025/03/trae.html  
  
  
