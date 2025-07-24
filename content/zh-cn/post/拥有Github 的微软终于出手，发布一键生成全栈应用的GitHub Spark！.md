---
title: "拥有Github 的微软终于出手，发布一键生成全栈应用的GitHub Spark！"
date: "2025-07-24"
tags: ["GitHub Spark", "全栈应用", "AI工具", "微软", "Copilot"]
categories: ["AI", "开发工具"]
description: "微软发布GitHub Spark，一个使用自然语言生成全栈应用的AI工具，并一键部署上线。"
author: "J0hnAGI Hunt"
image: ""
---
**摘要:**

- **微软发布 GitHub Spark，允许用户通过自然语言生成全栈应用程序。**
- **GitHub Spark 遵循微应用理念，专注于做好一件事，降低功能复杂度。**
- **Spark 通过自然语言工具链、托管运行时环境和 PWA 仪表板实现其功能。**

**源自** |  J0hnAGI Hunt 2025-07-24 09:31

**刚刚，微软放出了一个可能让所有人都要坐不住的大招！**


GitHub Spark 正式发布，这个全新的 AI 工具能让你用自然语言直接生成全栈应用程序，然后一键部署上线。

微软 CEO Satya Nadella (@satyanadella) 亲自站台宣布：
> 今天我们发布了 GitHub Spark——Copilot 中的一个新工具，可以完全用自然语言将你的想法变成全栈应用。


![](https://ai.programnotes.cn/img/ai/9864dcff254a2feda7c700703f5c1e22.png)

简单来说，你只需要描述你想要什么，Spark 就能自动生成一个完整的应用程序，包括前端、后端、数据库，甚至 AI 功能。

值得注意的是，**这个工具默认使用的居然不是自家的 GPT，而是 Claude Sonnet 4.**
## 微应用理念

GitHub Spark 遵循 Unix 哲学——**软件可以专注于做好一件事**
。

这里的「微」不是指应用价值的大小，而是指功能复杂度的规模。

这些微应用可以是：
- 儿童零用钱追踪器，支持只读或读写模式共享，使用 LLM 在达到收入目标时生成庆祝消息

![](https://ai.programnotes.cn/img/ai/41e89be6bf8eaffa064079856e9f1ff7.jpeg)
- 六岁孩子设想并创建的动画车辆世界

![](https://ai.programnotes.cn/img/ai/d154075dee244af8f877f799190b8e9f.jpeg)
- 每周卡拉 OK 之夜的追踪应用，显示每位受邀客人的状态

![](https://ai.programnotes.cn/img/ai/bed655590b3434bceea4617c3f40119d.jpeg)
- 允许按名称搜索城市的地图应用，使用 LLM 生成有趣的简介

![](https://ai.programnotes.cn/img/ai/5a5826a17d35a04637b048346e21e9b8.png)
## 强大功能体系

根据 GitHub 的详细介绍，Spark 通过三个紧密集成的组件实现其功能：
### 1. 基于自然语言的工具链

**交互式预览**

当你输入自然语言表达时，Spark 不仅生成代码，还会立即运行并通过交互式预览显示。这种「以应用为中心的反馈循环」让你可以指定尽可能少或尽可能多的细节，然后在视觉学习中迭代。

![](https://ai.programnotes.cn/img/ai/5cc2ac54b3550994cb7d6cf139fa693a.jpeg)

**修订变体**

创建或迭代 spark 时，可以选择请求一组变体。这将生成 3-6 个不同版本的请求，每个都有细微但有意义的差异。

![](https://ai.programnotes.cn/img/ai/5b6b8ade36abc89a8a602c7c561129e6.jpeg)

**自动历史记录**

每次修订都会自动保存，可以一键恢复。这种「好奇心驱动的开发」让你可以有想法就尝试，而不用担心负面后果。

![](https://ai.programnotes.cn/img/ai/cf26e99a20f84b735e520e1c0a85bd88.jpeg)

**模型选择**

创建或修订 spark 时，可以从四个 AI 模型中选择：Claude Sonnet 3.5、GPT-4o、o1-preview 和 o1-mini。

![](https://ai.programnotes.cn/img/ai/2f19511bf0ee03e00afc194413efaee7.jpeg)
### 2. 托管运行时环境

Spark 被称为「以应用为中心」的工具（而非「以代码为中心」），因为它设计用于创建要被看到、感受和使用的应用，而不是简单地生成代码。

**无部署托管**
：创建或修订 spark 时，更改会自动部署，可以在桌面、平板或移动设备上运行和安装（通过 PWA）。

![](https://ai.programnotes.cn/img/ai/f9a5aafe30bfb5a62053effc874a224e.jpeg)

**可主题化的设计系统**
：确保应用看起来美观，包含一组内置 UI 组件和可主题化的设计系统。

![](https://ai.programnotes.cn/img/ai/bbaec84b440643d2c2617a0be76f7086.jpeg)

**持久数据存储**
：提供托管的键值存储，并自动知道何时使用它。还提供数据编辑器，让你轻松查看和编辑 spark 使用的数据。

![](https://ai.programnotes.cn/img/ai/1603f5e6dfae767222170cfc35bb4ca9.jpeg)

**集成模型提示**
：运行时与 GitHub Models 集成，允许你向 sparks 添加生成式 AI 功能，无需了解 LLMs。

![](https://ai.programnotes.cn/img/ai/5ab0049b47972a822666825a24533fae.jpeg)
### 3. PWA 仪表板

让你从任何地方管理和启动你的 sparks，支持分享并控制访问权限（只读或读写）。
## 深度GitHub 集成

Thomas Dohmke (@ashtom) 详细介绍了集成特性：
> 只需在 GitHub Spark 中用自然语言提示，它就能创建一个全栈应用，利用 Claude Sonnet 4 来创建应用，并使用 Microsoft Azure 来托管。


![](https://ai.programnotes.cn/img/ai/67f0000ce889046646cd9106e77dae07.jpeg)

Spark 不仅使用 LLM 创建应用，还可以集成 LLM 让应用更智能。可以要求 Spark 添加 AI 功能，它能集成聊天机器人、内容生成和其他智能功能，使用来自 OpenAI、Meta、DeepSeek、xAI 等的模型——无需 API 密钥管理。

![](https://ai.programnotes.cn/img/ai/983dcf8c379220a2f3fd6cad94cd256c.jpeg)

所有流程都能回到 GitHub 平台。

一键打开仓库，将问题分配给 GitHub 的编码代理——甚至可以通过 Codespaces 在 VS Code 中打开你的 Spark 并开始自己编辑代码。

部署时，Spark 会处理服务器、域名和认证。另外，通过内置的安全 GitHub 认证控制访问。

![](https://ai.programnotes.cn/img/ai/7f0ede958edfad1697cca1d0775d6259.jpeg)
## 开发者热议

Thomas Dohmke 对 Spark 的愿景充满信心：
> 在软件开发的过去五十年里，生产软件需要手动将人类语言转换为编程语言，编译它，调试它，测试它——然后再回到更多的编码。今天，我们向创造的理想魔法迈出了一步：你脑海中的想法在几分钟内就能成为现实。✨


Kristoph (@ikristoph) 也指出了一个现实问题：
> 微软：这是一个应用，你可以使用 AI 构建任何你想要的东西。你不需要是专业人士！
> 同样是微软：哦，你想在 Azure 上使用 AI？你最好是一家高价值公司，否则你实际上只能使用微不足道的 AI 计算量。


Reso ☕️ (@Resorcinolworks) 直接宣布：
> lovable 和 bolt 完了。人类完了。AGI 来了。前端工作 RIP。


![](https://ai.programnotes.cn/img/ai/c9511f31de073e1ba44ba85eb59cb4f2.png)

Shivam – oss/acc (@Shivamshahi77) 调侃道：
> 嘿 Spark，给我造个宇宙飞船，要所有功能，不能有错误。


![](https://ai.programnotes.cn/img/ai/eb3e3db58335abaf0f0366f8a47216bc.jpeg)

rakshat.sol (@singh_rakshat) 更是直接：
> 嘿 Spark，用 NextJs 做个十亿美元的 SaaS，确保没有错误，谢谢。


![](https://ai.programnotes.cn/img/ai/e00f6bba38690bd1960e627c3bd38789.png)

不过，Rob Eisenberg (@EisenbergEffect) 则批评称：
> 又一个微软的山寨品，没有真正的创新。你显然没有读我关于这类工具应该发展方向的文章，你创造了一个玩具，复制了其他所有缺乏想象力的公司正在做的事情。

## 实战分享

Microsoft MVP John Lokerse (@JohnLokerse) 分享了他的详细使用体验：
> 通过 GitHub Spark，你可以在几个提示内快速构建支持日常工作的微应用。这些微应用使用 React、TypeScript、HTML 和 CSS 等前端技术构建。每个应用都有内置数据库来存储你的内容。


他特别强调了 Spark 的强大功能：
- **低成本的样式设计**，支持自定义主题、可配置边框和排版

- **连接 API**，获取数据或与外部服务交互

- **集成模型提示**，轻松为应用添加生成式 AI 功能（如输入的自动摘要等）

- **通过迭代列表跟踪更改**，需要时轻松回滚

- **托管运行时环境**，无需部署。Spark 被设计为以应用为中心的工具。只需专注于构建你的应用！

- **自动功能建议**以改进你的应用

- **在 GitHub 组织内共享 Spark 应用**（即将推出）

他总结道：
> 想要一个产品反馈应用？✅ 想要一个快速将文件转换为另一种文件类型的应用？✅ 想要一个列出生日礼物的应用？✅
> 有了 Spark，唯一的限制就是你的想象力。


Anand Chowdhary (@abhagsain) 也分享了使用经验：
> 我们使用 Spark 快速测试 LLM 流程并构建内部工具。现在我们通过输入想法就能在几秒钟内获得功能原型。虽然有其他工具可以将自然语言转换为功能 UI，但 Spark 实际上构建了具有完全功能的整个（迷你）应用程序，包括 LLM 后端，而不仅仅是前端 UI。


Yani Iliev (@YaniIliev) 给出了他的实际测试：
> 我尝试用它做一个动画 WebP 到 GIF 转换器。应用的外观和加载都很好，除了核心功能——转换器没有工作。又试了几次，还是同样的结果。

## 定价和可用性

根据官方信息，**GitHub Spark 目前面向 Copilot Pro+ 用户开放**，这是 GitHub 刚推出的公开预览版。

Spark 作为 GitHub Copilot Pro+ 订阅的一部分提供，用户可以立即访问 github.com/spark 开始使用。
## 竞争格局剧变

Spark 的发布或许将让现有的 AI 编码工具市场格局发生了巨大变化。

Adolf Rizzler (@0xRizzler) 声称：
> 这是微软在宣布「我们很快会收购 lovable」。


Thack (@DaveThackeray) 更是感叹：
> 哈哈哈，突然间 Lovable 看起来像是最糟糕的投资！


Anurag Bhagsain (@abhagsain) 总结道：
> 分发之王已经入场。对 loveable、replit、bolt 来说将会很艰难。


![](https://ai.programnotes.cn/img/ai/0d6c401ae33d4b613af4ef465d294ca4.png)

Grok (@grok) 也在被问及与其他工具的比较时回应：
> 是的，类似工具包括 Lovable（AI 从提示构建全栈应用，与 Supabase 集成）、bolt.new（基于浏览器的 AI 用于 Web 应用，一键部署）和 Replit AI（为应用生成代码）。GitHub Spark 在这些基础上通过无缝的 Copilot 集成进行构建。

## 不容小觑的微软

这次 Spark 的发布，再次证明了拥有 GitHub 的微软在 AI 编码领域的强大实力。

而值得注意的是，就在同一时间，The Information 报道了一个耐人寻味的消息：**Slack 拒绝给 OpenAI 的 ChatGPT 开放更深层次的集成接口。**

****
报道显示，OpenAI 去年就开始与 Slack 讨论 ChatGPT-Slack 集成。今年早些时候，OpenAI 工程师在连接 Gmail、Google Drive 和 GitHub 等应用到 ChatGPT 的同时，也在开发这个集成。

一些 ChatGPT 客户甚至已经能够测试这个功能，允许他们从聊天机器人搜索 Slack 消息和文件。

但在 OpenAI 计划于 3 月发布企业应用集成的几周前，管理层通知工程师 Slack 集成不再可能。

工程师们没有被告知原因。

![](https://ai.programnotes.cn/img/ai/b10749c11f20592d4c7f10846fac004d.png)

**这背后反映的是 AI 公司与传统软件应用之间正日益升级的数据战争**
——

随着应用程序越来越将 AI 公司视为竞争威胁，Slack 的母公司 Salesforce 在今年夏天决定限制 AI 公司访问 Slack 客户文件的能力，即使客户授予了访问权限。

![](https://ai.programnotes.cn/img/ai/9d9b8b0e4aa2b70db15503d539581ec8.png)

相比之下，**微软拥有 GitHub 这个开发者生态系统的核心平台，让 Spark 在数据获取和生态整合上具有天然优势**。

而 Slack 对 OpenAI 的防备，也更是说明了拥有核心开发者平台的重要性：在 AI 时代的数据战争中，*GitHub 有可能就是微软手中的王炸**。

拥有 GitHub 的微软，绝对不容小觑。

[1]GitHub Spark 官网: https://github.com/spark

[2]GitHub Spark 文档: https://docs.github.com/en/copilot/tutorials/building-ai-app-prototypes

[3]GitHub Next 项目页面: https://githubnext.com/projects/github-spark

[4]GitHub Spark Changelog: https://github.blog/changelog/2025-07-23-github-spark-in-public-preview-for-copilot-pro-subscribers/

[5]GitHub Spark 功能介绍: https://github.com/features/spark

[6]theinformation报道: https://www.theinformation.com/articles/enterprise-data-war-hits-openai

