---
title: "Hugging Face发布SmolLM3，全流程全数据开源的3B参数多语言长上下文模型"
date: "2025-07-09"
tags: ["Hugging Face", "SmolLM3", "开源模型", "多语言", "长上下文"]
categories: ["人工智能", "模型发布"]
description: "Hugging Face发布SmolLM3，一款全流程全数据开源的3B参数多语言长上下文模型。"
author: "橘鸭Juya"
image: ""
---

核心内容:
- Hugging Face发布SmolLM3，全流程全数据开源的3B参数多语言长上下文模型。
- Meta聘用苹果前基础模型负责人Ruoming Pang。
- 智源研究院（BAAI）发布具身智能模型RoboBrain 2.0。

**源自** |Juya橘鸭Juya 2025-07-09 07:05

![](https://ai.programnotes.cn/img/ai/3907a3cfdac8f0edf9c2ce6d754aee12.png)

## 概览
- Hugging Face发布SmolLM3，全流程全数据开源的3B参数多语言长上下文模型

- Meta聘用苹果前基础模型负责人Ruoming Pang

- 智源研究院（BAAI）发布具身智能模型RoboBrain 2.0

- Skywork发布开源多模态推理模型Skywork-R1V3-38B

- 谷歌AI电影制作工具Flow更新

- 阿里巴巴开源网络智能体WebSailor

- 阿里巴巴开源多模态推理模型HumanOmniV2

- 社区发布Qwen3-8B-BitNet模型

- SK Telecom发布韩语增强模型A.X系列

- 谷歌开源MCP Toolbox for Databases

- Moonvalley发布面向专业制作的AI视频模型Marey

- LTX Studio为其视频模型发布三款新LoRA

- LobeChat更新支持MCP插件市场和一键安装

- LM Studio宣布取消商业使用限制，对所有用户免费

- 硅基流动发布命令行工具Gen-CLI

- llama.cpp已支持腾讯混元Hunyuan-A13B模型

- NovelAI开源其V2动漫模型权重

- OpenAI据报加强安全措施以防范间谍活动

- Genspark AI通话功能扩展至全球并支持多语言

- Neta Art开源其AI动漫模型训练策略

- Proactor推出首款“自主动”AI队友Proactor v1.0

## Hugging Face发布SmolLM3，全流程全数据开源的3B参数多语言长上下文模型
> 
> **Hugging Face**
发布了SmolLM3
，这是一款在**11万亿**
token上训练的**3B**
参数开源模型，具备**128k**
长上下文和独特的可切换推理模式，并开源了完整的训练方案。


**Hugging Face**发布了**3B**参数的开源语言模型SmolLM3。该模型在**11万亿**个token上进行了练，其性能在**3B**规模中处于领先地位，并能与Qwen3和Gemma3等**4B**模型相媲美。SmolLM3支持长达**128k**的上下文窗口，这是通过在**64k**上下文中训练并利用YaRN技术外推实现的。架构上，模型采用了Grouped Query Attention (GQA)和NoPE (No Positional Embeddings)等技术来优化效率和长上下文性能。

SmolLM3的一大特色是支持可切换的“think”（思考）和“no_think”（不思考）双重推理模式，并支持包括**英语、法语、西班牙语、德语、意大利语和葡萄牙语**在内的六种语言。**Hugging Face**此次不仅开源了模型权重，还公布了完整的训练方案，包括三阶段的预训练数据混合策略、用于提升长上下文和推理能力的中期训练方法，以及结合了监督微调（SFT）和锚定偏好优化（APO）的后训练流程。完整的训练配置、代码、数据集和模型合并方法均已公开，旨在推动社区在此基础上进行复现和创新。

![](https://ai.programnotes.cn/img/ai/a3b467e29b65da5d134f5ce0f3eac174.png)
```
https://huggingface.co/blog/smollm3
https://github.com/huggingface/smollm
```
## Meta聘用苹果前基础模型负责人Ruoming Pang
> 
> **苹果**公司负责内部AI基础模型开发的高管**Ruoming Pang**已离职，并加入**Meta**新成立的超级智能实验室。


据报道，**苹果**公司负责内部AI基础模型开发的高管**Ruoming Pang**已离职，并加入**Meta**。**Pang**自**2021年**从**谷歌**加入**苹果**后，一直领导一个约**100人**的团队，该团队负责开发支撑**Apple Intelligence**核心功能（如Genmoji、优先级通知和端侧文本摘要）的AI模型。

**Pang**将加入**Mark Zuckerberg**上周宣布成立的**Meta超级智能实验室（Meta Superintelligence Labs）**。近期，**Meta**还从**OpenAI**聘请了研究员**Yuanzhi Li**，以及从**Anthropic**聘请了曾参与Claude模型开发的**Anton Bakhtin**。**Pang**的离职被视为对**苹果**自研AI模型努力的又一次打击，据称他的离开可能会引发其原团队（AFM group）的更多人员流失。该团队现在将由**Zhifeng Chen**
领导。
## 智源研究院（BAAI）发布具身智能模型RoboBrain 2.0
> 
> **北京智源人工智能研究院（BAAI）**发布了开源具身智能模型RoboBrain 2.0，提供**7B**和**32B**两种规模，旨在统一物理环境中的感知、推理和规划能力。


**北京智源人工智能研究院（BAAI）**发布了其最新的开源具身智能大脑模型RoboBrain 2.0。该模型旨在统一物理环境中的感知、推理和规划能力，以完成复杂的具身任务。RoboBrain 2.0提供了**7B**和**32B**两种规模的版本，采用了包含视觉编码器和语言模型的异构架构。

RoboBrain 2.0
在多个空间和时间维度的基准测试中取得了领先的性能，其**32B**
版本在多数测试中超越了现有的开源及部分闭源模型。该模型具备多项关键的真实世界具身智能能力，包括空间理解（如功能可供性预测、空间指代）、时间决策（如闭环交互、多智能体长时程规划）以及实时场景记忆。该模型支持多图像、长视频和高分辨率视觉输入，并能够处理复杂的任务指令。其训练框架为FlagScale
，评估框架为FlagEvalMM
。

![](https://ai.programnotes.cn/img/ai/eec3c30ea802a6b49a382fba1034332a.png)
![](https://ai.programnotes.cn/img/ai/8f3a805e2e62c42e0dbf7a52017ee0ba.png)
```
https://huggingface.co/BAAI/RoboBrain2.0-7B
https://huggingface.co/papers/2507.02029

```
## Skywork发布开源多模态推理模型Skywork-R1V3-38B
> 
> **Skywork**发布了其最强开源多模态推理模型Skywork-R1V3-38B，该模型在多个推理基准测试中达到开源模型的SOTA水平。


**Skywork**发布了其系列中最新且最强大的开源多模态推理模型Skywork-R1V3-38B
。该模型通过在后训练阶段采用精细的强化学习（RL）算法，显著提升了多模态推理能力，并在多个基准测试中达到了开源模型的SOTA水平。

在关键的多模态和跨学科基准测试中，Skywork-R1V3-38B表现出色。在MMMU测试中得分**76.0**
，接近人类专家水平（**76.2**）；在EMMA-Mini (CoT)和MMK12上分别取得**40.3**和**78.5**
的开源最佳成绩。此外，它在物理、逻辑和数学等多个推理基准（如PhyX-MC-TM、SeePhys
、MME-Reasoning、VisuLogic、MathVista等）上均取得了开源模型的领先地位，其中在MME-Reasoning
上的表现甚至超过了**Claude-4-Sonnet**。该模型基于Qwen2.5构建。

![](https://ai.programnotes.cn/img/ai/e4e9fe251218e8f7379b6b85d1fad8f3.png)
```
https://huggingface.co/Skywork/Skywork-R1V3-38B
https://github.com/SkyworkAI/Skywork-R1V/blob/main/report/Skywork_R1V3.pdf
https://github.com/SkyworkAI/Skywork-R1V

```
## 谷歌AI电影制作工具Flow更新
> 
> **谷歌**的AI电影制作工具Flow新增语音生成和Veo 3 Fast支持，允许用户为角色图片配音。


**谷歌**名为Flow的AI电影制作工具，最近更新为Flow编辑器中的“帧到视频”功能增加了语音生成和Veo 3 Fast支持，用户可以上传角色图片并为其生成配音。
```
https://labs.google/flow

```
## 阿里巴巴开源网络智能体WebSailor
> 
> **阿里巴巴**开源了网络智能体WebSailor，它能自主浏览网页并完成复杂推理任务，性能接近闭源系统。


**阿里巴巴通义实验室**正式开源了其最新的网络智能体WebSailor。该智能体能够在开放的网页环境中自主进行页面跳转、信息查找、并整合多源线索完成复杂推理任务。在**OpenAI**发布的BrowseComp
等高难度网页智能体评测基准上，WebSailor刷新了开源系统的最好成绩，成为首个在这些任务上接近闭源系统能力的开源方案。

WebSailor的核心突破在于其完整的后训练方案，该方案包括三个阶段：首先通过合成名为SailorFog-QA
的高不确定性任务数据集来模拟真实世界中的模糊搜索路径；其次通过冷启动微调（RFT）增强模型在复杂任务路径中的稳定性；最后引入了名为DUPO的高效强化学习算法，将复杂智能体的强化学习训练速度提升了**2-3倍**。该项目是**通义实验室**继WebWalker和WebDancer之后，“Web智能体”系列的第三项重要发布，其模型代码、训练方法及评测数据集均已在**GitHub**上开源。

![](https://ai.programnotes.cn/img/ai/d4bb408c281186808e115cd1ac07274d.jpeg)
```
https://github.com/Alibaba-NLP/WebAgent

```
## 阿里巴巴开源多模态推理模型HumanOmniV2
> 
> **阿里巴巴通义实验室**开源了多模态推理模型HumanOmniV2，通过强制上下文总结等技术，旨在更精准地理解人类的复杂意图。


**阿里巴巴通义实验室**开源了一款名为HumanOmniV2的多模态推理模型，旨在解决现有模型在全局上下文理解不足和推理路径简单化的问题。该模型能够更精准地捕捉图像、视频、音频中的隐藏信息，从而更好地理解人类的复杂意图和“话外音”。

HumanOmniV2 引入了三项关键技术：强制上下文总结机制，要求模型在生成最终答案前先输出对多模态输入的系统性分析；由大模型驱动的多维度奖励体系，从上下文、格式、准确性和逻辑四个维度进行评估；以及基于GRPO（Generative Reasoning Policy Optimization）的优化训练方法。同时，团队还推出了一个名为IntentBench的评测基准，包含**633个**视频和**2689个**相关问题，HumanOmniV2
在此基准上实现了**69.33%**的准确率。![](https://ai.programnotes.cn/img/ai/84266ed6cce721ced7d313d5d7466733.png)

```
https://arxiv.org/abs/2506.21277
https://github.com/HumanMLLM/HumanOmniV2
https://modelscope.cn/models/iic/humanomniv2
https://huggingface.co/PhilipC/HumanOmniV2
https://huggingface.co/datasets/PhilipC/IntentBench

```
## 社区发布Qwen3-8B-BitNet模型
> 
> 社区开发者发布了Qwen3-8B-BitNet模型，这是Qwen3-8B的BitNet版本，参数量被大幅压缩至约**2.5B**
。


社区开发者发布了一款名为Qwen3-8B-BitNet的模型，这是Qwen3-8B的BitNet版本。该模型在Qwen3-8B的基础上，使用了**Prime Intellect**的SYNTHETIC-1数据集中约**10亿**个token进行微调。

在转换过程中，模型的所有线性层（包括LM Head）都被转换为BitNet架构，并在每个线性层的输入端额外增加了一个RMSNorm层。经过此番处理，模型的参数量被大幅压缩至约**2.5B**。
```
https://huggingface.co/codys12/Qwen3-8B-BitNet

```
## SK Telecom发布韩语增强模型A.X系列
> 
> **韩国SK Telecom**发布了基于Qwen2.5的韩语增强模型A.X系列，在多个韩语基准测试中表现优于**GPT-4o**。


**韩国SK Telecom公司**发布了基于Qwen2.5进行韩语持续预训练的新模型系列。该系列包含两个版本：**72B**参数的A.X-4.0和**7B**参数的A.X-4.0-Light。

这些模型专注于提升韩语处理能力，并在多个韩语基准测试中表现出色。在韩国版MMLU测试KMMLU
上，**72B**版本得分达到**78.3**，超过了**GPT-4o**的**72.5**分。在测试韩语文化和语言理解能力的CLIcK基准上，得分也达到了**83.5**，同样高于**GPT-4o**的**80.2**分。此外，该模型在处理韩语文本时，所需token数量比其他模型减少约**33%**。

![](https://ai.programnotes.cn/img/ai/f9a36a7ee6e17120888e0578bc15f8c8.png)
```
https://huggingface.co/skt/A.X-4.0
https://huggingface.co/skt/A.X-4.0-Light

```
## 谷歌开源MCP Toolbox for Databases
> 
> **谷歌**开源了MCP Toolbox for Databases，这是一个旨在简化和保护AI智能体访问数据库的服务器工具。


**谷歌**
开源了MCP Toolbox for Databases，这是一个为数据库设计的开源MCP（Model-Controller-Plugin）
服务器。该工具旨在简化开发流程，让AI智能体能够更轻松、更安全地访问数据库。它通过处理连接池、认证等复杂问题，为开发者提供了便利。

该工具箱位于应用的编排框架和数据库之间，作为一个控制平面，用于修改、分发或调用工具。它支持将IDE
与数据库连接，使AI助手能够执行诸如自然语言查询、自动化数据库管理和生成上下文感知代码等任务。**谷歌**为该工具箱提供了适用于**Python**（Core、LangChain、LlamaIndex）和**JavaScript/TypeScript**
（Core、LangChain、Genkit）的客户端SDK。

![](https://ai.programnotes.cn/img/ai/abe329513b1c9de6e606eaea8794049d.png)
```
https://github.com/googleapis/genai-toolbox
https://googleapis.github.io/genai-toolbox/

```
## Moonvalley发布面向专业制作的AI视频模型Marey
> 
> **Moonvalley**
发布了专为专业制作打造的AI视频模型Marey
，旨在提供前所未有的创意控制和视觉特效能力。


**Moonvalley**发布了号称全球首款专为专业制作而构建、经过完全授权的AI视频模型Marey
。该模型旨在为电影制作提供前所未有的创意控制能力，能够执行复杂的视觉特效（VFX
）序列，并让创作者在整个项目过程中保持完全的创意主导权。

![](https://ai.programnotes.cn/img/ai/2e2d041caea57bf7bcd2eba529f1e6ee.jpeg)
```
http://bit.ly/MeetMarey

```
## LTX Studio为其视频模型发布三款新LoRA
> 
> **LTX Studio**为其LTX Video模型推出了三款新LoRA，以增强对AI视频生成的控制能力。


**LTX Studio**为其开源视频模型LTX Video推出了三款新的LoRA，分别是Pose LoRA、Depth LoRA和Canny LoRA。这些工具旨在为AI视频生成提供前所未有的控制能力，用户可以在消费级硬件上仅用少量样本来训练新的控制类型。

## LobeChat更新支持MCP插件市场和一键安装
> 
> **LobeChat**发布**1.97.0**版本，全面升级插件市场并支持在桌面端一键安装MCP插件，简化了使用流程。


**LobeChat**
发布了1.97.0版本，带来了重大更新，其中包括全面升级的插件市场和桌面端一键安装MCP
插件的功能。新的插件市场借鉴了**VSCode**等流行应用的设计，可以展示更丰富的信息。用户现在可以直接在**LobeChat**桌面端一键安装Local类型的MCP（Model-Controller-Plugin）插件，简化了使用流程。发现页面也进行了全面焕新，以更好地展示MCP插件。

![](https://ai.programnotes.cn/img/ai/61b88c802f0ce7154d7240a95808ed8f.png)
```
https://github.com/lobehub/lobe-chat/releases/

```
## LM Studio宣布取消商业使用限制，对所有用户免费
> 
> **LM Studio**
宣布其应用对所有用户完全免费，取消了原有的商业使用限制和许可证要求。


**LM Studio** 宣布，其应用程序现在可以免费用于任何场景，包括商业工作环境。自今日起，公司和团队使用 **LM Studio** 不再需要申请或购买商业许可证。此前的政策是个人使用免费，但公司需购买商业授权。官方表示，此举是为了减少团队在工作环境中采用该应用的阻力。
## 硅基流动发布DeepSeek版命令行工具Gen-CLI
> 
> 社区开发者推出了Gen-CLI，这是一款使用DeepSeek模型作为后端的命令行AI助手，为国内开发者提供了新的选择。


社区开发者基于开源的Gemini-CLI进行了修改，推出了使用DeepSeek模型作为后端的命令行AI助手工具Gen-CLI。该工具通过调用 **硅基流动（SiliconFlow）** 平台的API运行，旨在为国内开发者提供一个类似Gemini-CLI和Claude Code的替代品。Gen-CLI能够执行分析代码库、持续修改和调试代码、一键创建简单应用等任务，甚至可以帮助非开发者处理日常文件管理问题，如从文件夹中的多份发票PDF
中提取信息并进行计算。
```
https://github.com/gen-cli/gen-cli/

```
## llama.cpp已支持腾讯混元Hunyuan-A13B模型
> 
> 开源项目llama.cpp现已正式支持**腾讯混元**的Hunyuan-A13B模型。


开源项目llama.cpp最近合并了一项更新，增加了对**腾讯混元**（Hunyuan）A13B模型的支持。这意味着用户现在可以在llama.cpp框架下运行和推理该模型。
```
https://github.com/ggml-org/llama.cpp/pull/14425/files

```
## NovelAI开源其V2动漫模型权重
> 
> **NovelAI**
已公开其NovelAI Diffusion V2动漫模型的权重，供研究和非商业用途使用。


**NovelAI**
宣布公开其基于SD1.5的NovelAI Diffusion V2动漫模型的权重。这些权重可用于研究和非商业用途，让用户可以体验该模型发布当时的图像生成效果。
## OpenAI据报加强安全措施以防范间谍活动
> 
> 据《金融时报》报道，**OpenAI**
为防范企业间谍活动，已全面改革其内部安全运营措施。


据**《金融时报》**报道，**OpenAI**已全面改革其安全运营措施，以防范企业间谍活动。据称，在**今年1月**中国初创公司 **DeepSeek** 发布了一款竞争模型后，**OpenAI** 加速了现有的安全紧缩措施。**OpenAI**指控**DeepSeek**通过“蒸馏”技术不当复制了其模型。强化的安全措施包括“信息帐篷”（information tenting）政策，该政策限制了公司内部敏感研究和代码的访问权限。
## Genspark AI通话功能扩展至全球并支持多语言
> 
> **Genspark**
的AI通话功能现已向全球开放，并新增了对**12种**语言的支持。


**Genspark**
宣布其AI通话功能现已向全球开放。新功能支持向世界各地的联系人拨打电话，并增加了对**12种**
语言的支持，包括**英语、日语、韩语、中文、西班牙语、法语、德语、意大利语、葡萄牙语、俄语、印地语和阿拉伯语**
。
```
https://www.genspark.ai/

```
## Neta Art开源其AI动漫模型训练策略
> 
> **Neta Art**
宣布将全面开源其AI动漫模型，并公开其训练逻辑，以促进社区共同发展。


**Neta Art**
宣布将全面开源其最优秀的AI动漫模型，并首先详细解释了其模型（neta-art/lu2
）检查点命名的逻辑。公司表示，此举不仅是开源检查点，更是为了公开每一阶段训练背后的逻辑和未来计划，包括即将发布的LoRA
教程，以促进社区的共同发展。
```
https://huggingface.co/neta-art/lu2/

```
## Proactor推出首款“自主动”AI队友Proactor v1.0
> 
> **Proactor**发布了v1.0版本，号称是全球首款能独立感知、思考和行动的“自主动”AI队友。


**Proactor**
发布了其v1.0版本，号称是世界上第一款“自主动”（self-active）的AI队友。该AI被设计为能够独立地感知、思考和行动，无需用户提示或热键即可主动介入。例如，它可以在讨论中实时进行事实核查并纠正错误信息，或是在会议中转录对话、生成摘要和整理任务，旨在通过预见用户需求来提升工作效率。

作者橘鸦Juya，视频版在同名**哔哩哔哩**。如果对你有所帮助，欢迎**点赞、关注、分享**。


