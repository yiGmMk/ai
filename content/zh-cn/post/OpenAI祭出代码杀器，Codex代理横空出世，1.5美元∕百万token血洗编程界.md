---
title: "OpenAI祭出代码杀器，Codex代理横空出世，1.5美元/百万token血洗编程界"
date: "2025-05-18"
tags: ["OpenAI", "Codex", "AI编码", "软件工程", "AI代理"]
categories: ["人工智能", "软件开发"]
description: "OpenAI发布Codex研究预览版，一款功能强大的AI编码代理，旨在革新软件工程。"
author: "丁灵波"
image: "https://ai.programnotes.cn/img/ai/6aa0ff754bb7aeffa3ff7b58718d4831.png"
---


**核心内容点**:
- OpenAI推出了功能最强的AI编码代理Codex，可以并行处理多项任务。
- Codex经历了多次演变，最新版由codex-1模型支持，专为软件工程优化。
- OpenAI的AI编码展望是构建一整套Codex相关工具，支持实时协作和异步委托，并与开发者现有工具进行更深入的集成。
  
今天，OpenAI推出了该公司迄今为止功能最强的AI编码代理：Codex研究预览版。  
  
这是一款基于云的软件工程代理，可以并行处理多项任务，例如编写功能、解答代码库相关问题、修复错误以及提交拉取请求以供审核等，每个任务都在其专属的云沙盒环境中运行，并能预加载代码库。  
  
![](https://ai.programnotes.cn/img/ai/a42dbbdce290e033621043b8aaa2ac82.png)  
  
近几个月来，面向软件工程师（也称为氛围编码员）的AI工具人气持续飙升。谷歌和微软等大厂纷纷对外宣称，他们公司大约30%的代码现在已由人工智能编写。今年2月，Anthropic发布了自己的代理编码工具Claude Code；4月，谷歌更新了其人工智能编码助手Gemini Code Assist，增加了更多代理功能；5月份，OpenAI被曝达成协议将以30亿美元收购AI开发工具初创公司Windsurf，但双方均未明确回应。  
  
外界推测，Codex的最新发布  
表明，OpenAI可能转向于自主构建而非直接收购  
AI编码产品。  
  
## **一波三折的Codex**  
  
Codex系列并非第一次推出，过去几年经历了多次演变。  
    
最初的Codex于2021年就首次亮相，作为将自然语言翻译成代码的模型，可通过OpenAI的应用程序编程接口 (API) 使用，它是GitHub Copilot背后的引擎，GitHub Copilot是一款流行的自动完成式编码助手，由微软、GitHub和OpenAI联合开发。  
  
![](https://ai.programnotes.cn/img/ai/86d59fd8d064b4c359563523ef1bddc4.png)  
  
  
GitHub Copilot于2023年3月正式脱离OpenAI的Codex模型，采用GPT-4作为其Copilot X升级的一部分，以实现更深层次的IDE集成，同年，OpenAI关闭了对Codex的公开访问，然而，由于来自研究者们的公开呼吁，Codex模型最终保留可供OpenAI研究访问计划的研究者使用。  
  
![](https://ai.programnotes.cn/img/ai/6aa0ff754bb7aeffa3ff7b58718d4831.png)  
  
当下，OpenAI正在构建一个开源轻量级编码代理Codex CLI，目前该项目在  GitHub上已获得**21.8k**颗星，得到开发者广泛关注。  
  
最新版的Codex由codex-1模型提供支持，codex-1是OpenAI o3模型的一个衍生版本，专门针对软件工程进行了优化，它使用强化学习在各种环境中针对真实世界的编码任务进行训练，以生成与人类风格和PR偏好高度相似的代码，精确遵循指令，并可以迭代运行测试直至获得通过结果。  
  
今天，OpenAI还发布了codex-1的精简版本，这是专为Codex CLI使用而设计的o4-mini版本，这个新模型支持CLI中更快的工作流程，并针对低延迟代码问答和编辑进行了优化，同时保留了指令遵循和样式方面的相同优势，它现在作为Codex CLI中的默认模型，并在API中以codex-mini-latest的形式提供。  
  
OpenAI方面表示，未来几周，用户将可以免费畅享Codex的强大功能，之后，将推出限速访问和灵活的定价方案，开发者可以按需购买更多使用量。对于使用codex-mini-latest构建的开发人员，该模型可在Responses API上使用，价格为每100万个输入令牌1.50美元，每100万个输出令牌6美元，目前有75%的即时缓存折扣。  
  
## **专为编码定制模型**  
  
开发者目前可以通过ChatGPT的侧边栏访问Codex，并通过输入提示并点击“代码”按钮为其分配新的编码任务，每个任务都在预加载了开发者代码库的独立隔离环境中独立处理。  
  
Codex可以读取和编辑文件，以及运行包括测试工具、linters和类型检查器在内的命令，任务完成通常需要1到30分钟，具体取决于复杂程度，开发者可以实时监控Codex的进度。  
  
![](https://ai.programnotes.cn/img/ai/4390b190dc2216eb5bc8b2dc616d2d4a.gif)  
  
在产品中，开发者可以配置Codex环境，使其尽可能与实际开发环境匹配。  
  
Codex可以通过放置在代码库中的AGENTS.md文件进行引导，开发者可以在其中告知Codex如何导航代码库、运行哪些命令进行测试以及如何最好地遵循项目的标准实践，与人类开发人员一样，Codex代理在配置好开发环境、可靠的测试设置和清晰的文档后，性能最佳。   
  
![](https://ai.programnotes.cn/img/ai/cec9ddd06c4e928118b7875d2c778b4d.png)  
  
在编码评估和内部基准测试中，codex-1表现出强劲性能。  
  
OpenAI表示，训练codex-1的主要目标是使输出与人类的编码偏好和标准紧密结合，与OpenAI o3模型相比，codex-1始终能够生成更清晰的补丁，可供立即进行人工审核并集成到标准工作流程中。  
  
![](https://ai.programnotes.cn/img/ai/8cd113d3c956db2e87dcf849d9ad8777.png)  
  
![](https://ai.programnotes.cn/img/ai/d4dca4159ed475781342a1ea9b02f43c.png)  
  
为了平衡安全性和实用性，Codex经过了训练，能够识别并精准拒绝旨在开发恶意软件的请求，同时清晰区分并支持合法任务。  
  
此外，Codex代理完全在云端安全隔离的容器中运行，在任务执行期间，互联网访问被禁用，代理的交互仅限于通过GitHub代码库明确提供的代码以及用户通过安装脚本配置的预安装依赖项，代理无法访问外部网站、API或其他服务。  
  
最后，OpenAI宣称其技术团队已开始将Codex纳入其日常工具包，OpenAI 工程师最常使用它来替代那些重复且范围明确的任务，例如重构、重命名和编写测试，  
它同样适用于构建新功能、连接组件、修复错误以及起草文档。  
  
## **OpenAI的AI编码展望**  
  
对于AI编码布局，OpenAI表示最新版的 Codex 仅仅是个开始。  
  
未来，开发者可以自主掌控想要完成的重点工作，其余工作则能全面委托给代理——借助AI，开发速度会更快，效率更高，为了实现这一目标，OpenAI正在构建一整套Codex相关工具，支持实时协作和异步委托。  
  
最终，实时配对和任务委托将逐渐融合，开发者将通过IDE和日常工具与AI代理协作，提出问题、获取建议并卸载耗时较长的任务，所有这些都在统一的工作流程中进行。  
  
OpenAI还在推进与开发者现有的工具进行更深入的集成：  
目前Codex已与GitHub连接，不久后开发者将能够从Codex CLI、ChatGPT桌面应用，甚至是问题跟踪器或CI系统等工具中分配任务。  
  
![](https://ai.programnotes.cn/img/ai/224ee15baf8f3998be26b5b0a1f26542.jpeg)  
  
根据SimilarWeb的市场分析数据，过去12周内，以开发人员为中心的AI工具的流量激增了75%，凸显了行业对编码助手作为基本基础设施而非实验性附加组件的需求日益增长。  
  
OpenAI曾与快速发展的AI开发工具初创公司Cursor和Windsurf进行收购谈判，据称，Cursor拒绝了收购，Windsurf原则上同意OpenAI以30亿美元价格收购，但这笔收购目前尚没有尘埃落定，就在昨天，Windsurf还推出了其专注于编码的基础模型SWE-1强化市场竞争。  
  
新的Codex代理推出，外界分析认为是OpenAI向Windsurf、Cursor等施压的一种方式，增加谈判筹码进而达成更有性价比的交易或收购，同时与谷歌、Anthropic等在AI编码代理领域展开正面对抗，重塑市场竞争格局。  
  
原标题：《加速AI编码竞赛！OpenAI上线软件工程代理Codex研究预览版，可并行处理多项任务》