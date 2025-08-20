---
title: "DeepSeek发布V3.1模型,Gemini API截断及空回复问题即将修复"
date: "2025-08-20"
tags: ["DeepSeek-V3.1", "Gemini API Fix", "AGENTS.md Standard", "nano-banana", "Qwen-VL-Plus"]
categories: ["AI"]
description: "本文汇总了近期AI领域的重要动态：DeepSeek发布上下文长度扩展至128k的V3.1模型，Google承诺修复Gemini API的截断问题，并推出AGENTS.md编码Agent开放标准。"
author: "Juya橘鸭Juya"
image: "https://ai.programnotes.cn/img/ai/72fabc3270a93993ac9cb2da88bb141b.png"
---

- DeepSeek发布V3.1模型，上下文长度扩展至128k
- Google承诺修复Gemini API的截断及空回复问题
- AGENTS.md工作组推出编码Agent开放标准

**源自** |  Juya橘鸭Juya 2025-08-20 08:17

## 概览

- DeepSeek发布V3.1模型 #1

- Google 承诺即将修复 Gemini API 截断及空回复问题 #2

- AGENTS.md工作组成立 推出编码Agent开放标准 #3

- 谷歌新模型 nano-banana 现身 LMArena #4

- Google Whisk 扩展至77国并集成Veo 3 #5

- 阿里云百炼上架Qwen-VL-Plus新版 #6

- Kilo Code更新：新增基于用量的价格估算与QwenCode支持 #7

- Augment Code推出Agent Turn Summary功能 #8

- OpenAI在印度推出ChatGPT Go订阅服务 #9

- Microsoft Excel 推出 =COPILOT() 函数 #10

- 腾讯推出卡通制作工具ToonComposer #11

- Firecrawl发布V2版本 #12

- Allen Institute for AI 发布 OLMo 2 1B 早期训练检查点 #13

- Cursor发布全球最快MXFP8 MoE内核 #14

- 苹果Xcode 26将原生集成Claude模型 #15

- 字节跳动即将发布开源模型SeedOss-36B #16

- 字节跳动研发AI手机 #17

- 英伟达为中国开发两款Blackwell架构AI芯片 #18

- 谷歌宣布首座AI数据中心核反应堆所在地 #19

- Meta 正式宣布重组AI部门 #20

## DeepSeek发布V3.1模型 #1
> 
> **DeepSeek**发布模型DeepSeek-V3.1版本，上下文长度扩展至**128k**，其Base模型也已在**HuggingFace**发布。


**DeepSeek**宣布其线上模型已升级至V3.1版本，此次更新将官方API和网页服务的上下文长度拓展至**128k**。目前V3.1版本已在官方网页、APP以及微信小程序和API中上线。

与此同时，**DeepSeek**V3.1的Base模型（DeepSeek-V3.1-Base）也已在**Hugging Face**上发布，尽管模型卡片最初尚未更新，但相关文件已上传可供下载。
有观察指出，V3.1模型是一个混合推理模型，目前在官网中启用深度思考模式会调用V3.1模型的推理模式。并且，V3.1的网页版即使在关闭搜索功能的情况下也会主动进行搜索，除非在提示中明确指示“不要搜索”，这可能与新引入的特殊tokens设计有关。
目前**DeepSeek**尚未发布正式公告，本报会持续跟进报道。

![](https://ai.programnotes.cn/img/ai/34196f2bbcfa8ca7149f9bcb0b026192.png)

![](https://ai.programnotes.cn/img/ai/72fabc3270a93993ac9cb2da88bb141b.png)
```
https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base

```

## Google 承诺即将修复 Gemini API 截断及空回复问题 #2
> 
> **谷歌**官方回应将尽快修复Gemini 2.5 Pro模型API存在的回复截断和空回复问题。


自前段时间以来，**Google** 的 Gemini 2.5 Pro 模型 API 出现了广泛的回复截断和空回复问题。该问题影响全球用户，无论是使用免费还是付费 API key 的开发者都受到了同等影响。

**Gemini**API 负责人 **Logan Kilpatrick** 昨晚回应称：“大家好，已向团队反馈！抱歉拖了这么久，这其实是 2.5 Pro 模型最新发布时就已知的问题，但最近似乎出现了新变化，我们会尽快跟进。”

这意味着，该问题或将很快得到修复。

![](https://ai.programnotes.cn/img/ai/d8a2819198198729185924651ea5867a.png)
```
https://discuss.ai.google.dev/t/gemini-2-5-pro-with-empty-response-text/81175

```
## AGENTS.md工作组成立 推出编码Agent开放标准 #3
> 
> 一个由多家公司组成的工作组推出了名为AGENTS.md的开放标准，旨在为编码Agent提供统一、清晰的指令格式。


一个由**OpenAI Codex**、**Amp**、**Google Jules**、**Cursor**、**RooCode**和**Factory**组成的AGENTS.md工作组宣布，正式推出一个名为AGENTS.md的单一、开放且供应商中立的标准，旨在指导编码Agent在代码库中的工作方式。该格式的官方网站agents.md现已上线。

AGENTS.md被定位为“为Agent设计的README”，是一个简单、开放的格式，用于向编码Agent提供指导。其设计初衷是为了补充专为人类开发者设计的README.md文件。README.md通常包含快速入门、项目描述和贡献指南，而AGENTS.md则专注于提供编码Agent所需的额外、详细的上下文信息，例如构建步骤、测试指令、项目结构、代码约定和安全注意事项等。这种分离设计旨在为Agent提供一个清晰、可预测的指令来源，同时保持README.md
对人类贡献者的简洁性和专注度。

使用AGENTS.md的方法很简单：在代码仓库的根目录下创建一个AGENTS.md文件。对于大型的monorepo，可以在每个子项目或包内放置一个嵌套的AGENTS.md文件。Agent会自动读取目录树中最近的该文件，使其指令具有针对性，最接近的配置文件将拥有优先权。

目前，该标准已获得**Cursor**、**Amp**、**Jules**、**Factory**、**RooCode**和**Codex**等多种AI编码Agent和工具的支持。

![](https://ai.programnotes.cn/img/ai/2dce212f239dd2a9918d73c722dc2a74.png)
```
https://agents.md/

```
## 谷歌新模型 nano-banana 现身 LMArena #4
> 
> **谷歌**代号为nano-banana的新图像生成模型已在LMArena平台进行测试，其性能据称超越了GPT-Image-1。


大量**谷歌**工作人员在社交平台上发布香蕉emoji或香蕉图片，明示代号为 nano-banana 的图像生成模型为**谷歌**所有。

目前该模型在 LMArena 平台进行测试，但尚未在 AI Studio 上线。

在text-to-image（文生图）和image-edit（图像编辑）功能方面，nano-banana 展示了强大的能力，其性能被认为超越了 GPT-Image-1 模型。

该模型即将发布。

![](https://ai.programnotes.cn/img/ai/e09077ec68df90e0ca0ccff1e2d785dd.png)
```
https://lmarena.ai/?chat-modality=image

```
## Google Whisk 扩展至77国并集成Veo 3 #5
> 
> **谷歌**AI工具Whisk扩展至**77**个新国家，并集成Veo 3模型，新增了将静态图像转换为**八秒**动画的功能。


**Google Labs** 宣布，其AI工具 Whisk 正在扩展至**77**个新的国家。同时，Whisk 迎来了重大功能升级，集成了 Veo 3 的能力。通过此次升级，用户现在可以将由 Whisk 生成的静态图像转换为时长**八秒**的动画片段。这些动画片段将具备增强的细节、真实感和音频效果。

为了鼓励创作，**Google** 宣布所有创作者每月都将获得**5次**免费的动画生成额度。

![](https://ai.programnotes.cn/img/ai/5c447cdd6c3bdddaf1f642bd76644661.png)
```
https://labs.google/fx/tools/whisk
https://x.com/GoogleLabs/status/1957851006588293582

```
## 阿里云百炼上架Qwen-VL-Plus新版 #6
> 
> **阿里云**模型服务平台**百炼**上架了通义千问视觉语言模型Qwen-VL-Plus的新版本。


**阿里云**旗下模型即服务平台**百炼**（**Bailian**）近日上架了通义千问视觉语言模型Qwen-VL-Plus的新版本。

根据信息，此次上架的具体模型版本为“qwen-vl-plus-2025-08-15”。此前已经有更新过Qwen-VL-Max的新版本。

目前没有这些模型的发布公告，也暂不清楚Qwen是否会继续开源VL系列模型。
## Kilo Code更新：新增基于用量的价格估算与QwenCode支持 #7
> 
> **Kilo Code**更新后，新增了基于真实用量的AI模型价格估算功能，并支持Qwen Code作为API provider。


**Kilo Code**近期发布重要更新。Kilo Code API provider现在能够根据真实世界的使用情况显示AI模型的价格估算。用户可以在设置中查看各模型的平均每百万token成本，该数据基于Kilo Code API provider每日处理的超过**300亿**token的真实用量，并已计入缓存折扣等因素。

此次更新增加了对Qwen Code作为API provider的支持。该集成可开箱即用，用户安装Qwen Code并创建账户后，**Kilo Code**能自动找到其配置文件。

![](https://ai.programnotes.cn/img/ai/6120a15b2862ab2c6e182303221f2d7f.gif)
```
https://blog.kilocode.ai/p/kilo-code-v4791v4810-usage-based

```
## Augment Code推出Agent Turn Summary功能 #8
> 
> AI开发平台**Augment Code**推出Agent Turn Summary新功能，可将Agent的复杂操作序列浓缩为一行摘要，提升开发者效率。


AI软件开发平台**Augment Code**于**8月19日**发布了一项名为Agent Turn Summary的新功能。该功能可以将Agent在单次交互（turn）中执行的复杂操作序列浓缩为一行简洁的摘要，让开发者在几秒钟内就能掌握全局，而非花费数分钟滚动浏览大量日志。

该功能在Agent响应的末尾、反馈页脚旁边显示，内容包括工具调用的摘要与计数，以及所做更改的快照。用户可以一目了然地看到操作的整体范围，仅在需要时才展开查看完整细节。

目前，Agent Turn Summary功能已在**VS Code**和**JetBrains**的预发布版本中提供。

![](https://ai.programnotes.cn/img/ai/4058ddec4a3fe5d842b103b6d84f6514.png)
```
https://www.augmentcode.com/changelog/agent-turn-summary

```
## OpenAI在印度推出ChatGPT Go订阅服务 #9
> 
> **OpenAI**在**印度**市场推出名为ChatGPT Go的低成本订阅计划，每月定价**399卢比**，提供比免费版更高的使用额度。


**OpenAI**正式宣布在**印度**推出一项名为ChatGPT Go的全新低成本订阅计划。该订阅服务专为**印度**用户设计，定价为每月**399卢比**，约合**4.55美元**。

与免费版相比，ChatGPT Go提供了显著的权益提升，此外，该订阅服务支持通过**UPI**进行支付。

<table><thead><tr><th style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;color: rgb(0, 0, 0);line-height: 1.5em;letter-spacing: 0em;font-weight: bold;background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position: left top;background-repeat: no-repeat;background-size: auto;height: auto;border-radius: 0px;padding: 5px 10px;min-width: 85px;text-align: left;font-size: 14px !important;border: medium !important;background-color: rgb(240, 238, 230) !important;"><section><span leaf="">权益</span></section></th><th style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;color: rgb(0, 0, 0);line-height: 1.5em;letter-spacing: 0em;font-weight: bold;background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position: left top;background-repeat: no-repeat;background-size: auto;height: auto;border-radius: 0px;padding: 5px 10px;min-width: 85px;text-align: left;font-size: 14px !important;border: medium !important;background-color: rgb(240, 238, 230) !important;"><section><span leaf="">提升幅度</span></section></th></tr></thead><tbody><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;background-color: rgb(253, 252, 250) !important;"><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><section><span leaf="">消息上限</span></section></td><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><strong style="color: rgb(31, 12, 3);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(255, 254, 252, 0);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">10倍</span></strong></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;background-color: rgb(248, 247, 242) !important;"><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><section><span leaf="">图像生成数量</span></section></td><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><strong style="color: rgb(31, 12, 3);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(255, 254, 252, 0);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">10倍</span></strong></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;background-color: rgb(253, 252, 250) !important;"><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><section><span leaf="">文件上传额度</span></section></td><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><strong style="color: rgb(31, 12, 3);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(255, 254, 252, 0);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">10倍</span></strong></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;background-color: rgb(248, 247, 242) !important;"><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><section><span leaf="">内存时长</span></section></td><td style="white-space-collapse: collapse;overflow-wrap: break-word;word-break: break-all;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;text-align: left;font-size: 14px !important;border-top-width: medium !important;border-top-style: none !important;border-top-color: currentcolor !important;border-right-width: medium !important;border-right-style: none !important;border-right-color: currentcolor !important;border-bottom-width: medium !important;border-bottom-style: none !important;border-bottom-color: currentcolor !important;border-left-width: medium !important;border-left-style: none !important;border-left-color: currentcolor !important;border-image-outset: 0 !important;border-image-repeat: stretch !important;border-image-slice: 100% !important;border-image-source: none !important;border-image-width: 1 !important;"><strong style="color: rgb(31, 12, 3);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(255, 254, 252, 0);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">2倍</span></strong></td></tr></tbody></table>

**OpenAI** CEO **Sam Altman**表示，此举旨在首先在**印度**市场提供更实惠的**ChatGPT**服务。公司计划根据在**印度**的运营反馈，未来将此模式扩展到其他国家。

![](https://ai.programnotes.cn/img/ai/fa72af3bcba80e12aaf616c6ce6079bf.png)
```
https://x.com/sama/status/1957849495733166587

```
## Microsoft Excel 推出 =COPILOT() 函数 #10
> 
> **微软**为**Excel**新增=COPILOT()函数，将大型语言模型的能力直接集成到电子表格单元格中，用于数据分析和内容生成。


**微软**正在为 **Excel** 添加一项名为 =COPILOT() 的新函数，该功能将大型语言模型 (LLM) 的特性直接集成到电子表格的单元格中。

用户可以直接在网格内使用此函数来帮助填充单元格。根据指定的一组单元格数据，=COPILOT() 函数可以利用 AI 进行分析、生成内容和头脑风暴。具体功能包括生成摘要、标签、表格等。

该功能可能在部分地区无法使用。

![](https://ai.programnotes.cn/img/ai/f16bdfa92c28dba9ca5cda4cf5d6c337.gif)
```
https://x.com/satyanadella/status/1957493248718680571

```
## 腾讯推出卡通制作工具ToonComposer #11
> 
> **腾讯ARC团队**发布了免费卡通制作工具ToonComposer，该工具能结合中间帧生成与上色，并可根据文本提示填充画面内容。


**腾讯ARC团队**发布了一款名为ToonComposer的卡通制作工具，现已在**Hugging Face**上免费提供。该工具旨在帮助用户高效地创作卡通动画。

ToonComposer的核心功能是将动画制作中的两个关键步骤——in-betweening（中间帧生成）与colorization
（上色）相结合。用户只需提供基于线稿的关键帧和一个色彩参考帧，模型即可自动处理并生成完整的动画序列。

此外，该模型具备一项特殊功能，可以根据用户提供的文本提示（prompt），对草图或线稿中留白的区域进行想象和填充，从而丰富画面内容。据介绍，此模型基于**阿里巴巴万相实验室**（**@Alibaba_Wan**）的相关技术成果开发。

![](https://ai.programnotes.cn/img/ai/a33ef652681756db4f0e02a28ded1b4d.gif)
```
https://github.com/TencentARC/ToonComposer
https://huggingface.co/spaces/TencentARC/ToonComposer

```
## Firecrawl发布V2版本 #12
> 
> **Firecrawl**发布V2版本并宣布完成**1450万美元A轮**融资，新版本将网页抓取速度提升**10倍**并增加了语义爬取等新功能。


**Firecrawl**宣布推出其V2版本，并同时公布已完成由**Nexus Venture Partners**领投的**1450万美元A轮**
融资。官方称此次更新是其迄今为止最大规模的发布。

**Firecrawl**V2的核心升级在于性能和功能的扩展，旨在让agent能够更高效地爬取互联网信息。新版本将网页抓取（scraping）速度提升了**10倍**。此外，V2引入了多项新功能，包括Semantic crawling
（语义爬取）以及新闻和图片搜索功能，进一步增强了其数据获取和处理能力。

![](https://ai.programnotes.cn/img/ai/63b5e50c64e2c5a82b038719537efd8c.gif)
```
https://x.com/jasonzhou1993/status/1957933387722961217

```
## Allen Institute for AI 发布 OLMo 2 1B 早期训练检查点 #13
> 
> **Allen Institute for AI**发布了OLMo 2 1B模型从训练第**0步**到第**37000步**的早期检查点，以帮助社区研究LLM能力的涌现过程。


**Allen Institute for AI** (**AI2**) 近日发布了 OLMo 2 1B 模型的早期训练检查点集合。

这些检查点是在官方 OLMo 2 1B 模型原始训练完成后生成的。从训练的第**0步**开始，每隔**1000步**
保存一个检查点，直至第**37000步**。

旨在帮助研究社区深入探究大型语言模型（LLM）的能力是如何在训练中逐步涌现的。研究人员可以利用这些检查点进行分析、复现和比较，以更好地理解模型的发展过程。
```
https://huggingface.co/allenai/OLMo-2-0425-1B-early-training

```
## Cursor发布全球最快MXFP8 MoE内核 #14
> 
> **Cursor**团队通过重建内核并使用MXFP8格式，成功将MoE层训练速度提升**3.5倍**，实现了**1.5倍**的端到端训练总速度提升。


为解决MoE层在训练中速度过慢的问题，**Cursor**团队在内核级别对其进行了完全重建，并转向使用MXFP8
格式。

在训练其编程模型时，MoE层曾占据了**27%至53%的训练时间。经过优化后，新的MXFP8 MoE内核实现了MoE层速度提升3.5倍**，并带来了**1.5倍**的端到端训练总速度提升。该团队称，这是目前全球最快的MXFP8 MoE
内核。

![](https://ai.programnotes.cn/img/ai/3c6f1f9e84e8403879b610d23465a80b.png)
```
https://x.com/amanrsanger/status/1957932614746304898
https://cursor.com/blog/kernels

```
## 苹果Xcode 26将原生集成Claude模型 #15
> 
> **苹果**将在Xcode 26中原生集成**Anthropic**的**Claude**大模型，为开发者提供除**ChatGPT**
外的又一AI代码助手选择。


**苹果**公司正在扩展其集成开发环境Xcode 26的AI代码助手生态，将在原生支持**OpenAI**的**ChatGPT**
之外，新增对**Anthropic****Claude**大模型的原生集成。
根据Xcode 26 Beta 7版本的实测信息，开发者将可以直接在**Xcode**中登录**Claude**账户，并调用包括今年**5月**发布的Claude Sonnet 4.0和Claude Opus 4在内的模型。这一变化意味着开发者无需再像以往那样手动配置API，即可直接在**Xcode**内利用**Claude**进行代码生成、优化和辅助编程，为开发者提供了**ChatGPT**
之外的替代选项。

```
https://www.landiannews.com/archives/110273.html

```
## 字节跳动即将发布开源模型SeedOss-36B #16
> 
> 根据**Hugging Face Transformers**库的信息，**字节跳动**即将发布一款名为SeedOss-36B的**360亿**
参数稠密开源模型。


**字节跳动**即将发布一款名为SeedOss-36B的开源模型。相关信息来源于**Hugging Face Transformers**
库中的一个Pull Request。

该Pull Request由**GitHub**用户“**Fazziekey**”提交，标题为“Addiing ByteDance Seed Seed-Oss
”，旨在为即将推出的Seed Oss模型添加代码支持。

从目前披露的信息来看，SeedOss-36B很可能是一个**360亿**参数的稠密模型，而非MoE（Mixture-of-Experts
）架构。

![](https://ai.programnotes.cn/img/ai/0a6f92aeae6af97b88676b8896f207df.png)
```
https://github.com/huggingface/transformers/pull/40272
https://linux.do/t/topic/884197

```
## 字节跳动研发AI手机 #17
> 
> 据报道，**字节跳动**正与**中兴**合作研发一款暂定名为“**豆包手机**”的AI手机，预计将于今年底或明年初推出，初期仅供内部测试。


据**晚点科技**报道，**字节跳动**正在研发一款AI手机，暂定名称为“**豆包手机**”。该项目由**字节跳动**
与**中兴**合作进行，其中**字节**负责大模型功能及部分操作系统相关工作，而硬件的设计与生产则主要由**中兴**作为ODM承担。

该产品由**字节跳动**负责AI硬件的**Ocean**团队主导研发。**Ocean**团队负责人为**Kayden**，他直接向**Flow**业务负责人**朱骏**（**Alex Zhu**）汇报。该团队整合了**字节跳动**历年来收购的多个硬件产品团队，包括**锤子手机**、VR头显**PICO**、智能耳机**Ola Dance**等，同时还吸纳了去年从**荣耀**加入的手机研发人员。除了手机项目，**Ocean**团队还在探索多款AI设备，例如去年已上市发售的**Ola Friend**
智能耳机以及AI眼镜等。

根据计划，这款“**豆包手机**”预计将于今年**年底**或**明年年初**推出。在早期阶段，该设备将主要用于**字节**内部团队的测试，目前暂时没有对外公开发售的计划。
```
https://zhidx.com/p/498319.html

```
## 英伟达为中国开发两款Blackwell架构AI芯片 #18
> 
> **英伟达**正为**中国**市场开发两款基于Blackwell架构的AI芯片B30A和RTX6000D，其性能将优于当前获准销售的H20芯片。


据报道，**英伟达**正在为**中国**市场开发两款基于其最新Blackwell架构的新型AI芯片，其性能将强于当前获准在**中国**销售的H20芯片。

其中一款芯片暂定名为B30A，采用单芯片设计，其原始算力约为旗舰产品B300的一半。该芯片配备高宽带内存与NVLink技术，性能优于H20。目前该芯片的规格尚未完全确定，但**英伟达**计划最快于下月向**中国**
客户交付样品进行测试。
另一款专为**中国**市场设计的芯片于今年**5月**被报道，暂定名为RTX6000D。该芯片主要用于AI推理任务，售价将低于H20。它采用传统的GDDR显存，内存带宽为每秒**1398GB**，略低于**美国政府**今年**4月**新规设定的**1.4TB/s**限制阈值。预计首批小批量交付将在**9月**进行。

**英伟达**方面表示，其产品符合政府的要求，且所有产品均已获得相关部门批准并用于商业用途。
```
https://weibo.com/1871474290/Q0DiixAIg
https://x.com/cherylnatsu/status/1957750704065626164

```
## 谷歌宣布首座AI数据中心核反应堆所在地 #19
> 
> **谷歌**宣布其首座用于AI数据中心供电的小型模块化核反应堆将建在**美国田纳西州**的**橡树岭**
。


**谷歌**公司宣布，其首座用于为AI数据中心供电的模块化核反应堆将选址于**美国田纳西州**
的**橡树岭**
。

该项目旨在利用多个小型模块化核反应堆，为日益增长的AI计算需求提供稳定电力。这些核反应堆由**Kairos Power**公司负责研发和建造。根据计划，目前每个反应堆可以提供**50兆瓦**的电力供应。**Kairos Power**
的目标是到**2035年**，为**谷歌**提供总计**500兆瓦**的电力。
```
https://www.landiannews.com/archives/110277.html

```
## Meta 正式宣布重组AI部门 #20
> 
> **Meta**正式宣布重组其AI部门，新组织命名为**Meta Superintelligence Labs (MSL)**，下设四个专注于基础模型、研究、产品和基础设施的团队。


**Meta**已通过一份内部备忘录正式宣布对其AI部门进行重组。

新的AI组织被命名为**Meta Superintelligence Labs（MSL）**，其核心是一个名为**TBD Labs**
的新团队。**TBD Labs**将专注于基础模型，如今年**4月**发布最新版本的Llama系列。其余三个团队将分别专注于研究、产品集成和基础设施。
```
https://www.bloomberg.com/news/articles/2025-08-19/meta-restructures-ai-group-again-in-pursuit-of-superintelligence

```

**提示**：内容由AI辅助创作，可能存在**幻觉**和**错误**。

