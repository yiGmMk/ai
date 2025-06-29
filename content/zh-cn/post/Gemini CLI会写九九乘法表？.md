---
title: "Gemini CLI 能写九九乘法表？初体验与 PromptX 结合"
date: "2025-06-27"
tags: ["Gemini CLI", "PromptX", "AI编程", "九九乘法表", "贪吃蛇"]
categories: ["AI", "开发工具"]
description: "体验 Gemini CLI，结合 PromptX 工具，测试其编写九九乘法表和贪吃蛇游戏的能力。"
author: "kayin9凯隐"
image: ""
---

- **Gemini CLI 初体验**: 作者体验了 Google 开源的 Gemini CLI，并使用 PromptX 工具进行辅助。
- **角色创建与激活**: 通过 PromptX 创建并激活了 Python 后端开发者角色，用于执行编码任务。
- **编码任务测试**: Gemini CLI 成功编写了九九乘法表和贪吃蛇游戏，但在贪吃蛇游戏中存在无法退出的问题。
  
**源自** | kayin9凯隐的无人化生产矩阵 2025-06-27 09:39

朋友们，来晚了哈，举例 gemini cli 开源已经过去 1 天多了。我才刚玩上谷歌大善人开源的这个 gc

那就来测试一下 gemini cli 到底好不好用。
个人习惯目前的编码习惯是在编码前先调整提示词，给大家介绍的一个非常好用的提示词工具。这次就用它搭配 gc 验证一下看看这个 gemini cli 究竟好不好用。

Gemini CLI 启动！

![gemini 启动!](https://ai.programnotes.cn/img/ai/639e38669245ea2f40819a4f55e2c60e.png)

gemini 启动!

先来初始化一下角色
```
> promptx_init

 ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  promptx_init (promptx MCP Server) {"workingDirectory":"D:\\kayin_pro\\gc_test"}                │
 │                                                                                                   │
 │                                                                                                   │
 │    ============================================================                                   │
 │    🎯 锦囊目的：初始化PromptX工作环境，创建必要的配置目录和文件，生成项目级资源注册表             │
 │    ============================================================                                   │
 │                                                                                                   │
 │    📜 锦囊内容：                                                                                  │
 │    🎯 PromptX 初始化完成！                                                                        │
 │                                                                                                   │
 │    ## 📦 版本信息                                                                                 │
 │    ✅ **PromptX v0.0.2-beta.19 (dpml-prompt@0.0.2-beta.19, Node.js v22.17.0)** -                   │
 │    AI专业能力增强框架                                                                             │
 │                                                                                                   │
 │    ## 🏗️ 环境准备                                                                                │
 │    ✅ 创建了 `.promptx` 配置目录                                                                   │
 │    ✅ 工作环境就绪                                                                                 │
 │                                                                                                   │
 │    ## 📋 项目资源注册表                                                                           │
 │    ✅ 项目资源目录已创建，注册表已初始化                                                           │
 │       📂 目录: .promptx\resource\domain                                                           │
 │       💾 注册表: .promptx\resource\project.registry.json                                          │
 │       💡 现在可以在 domain 目录下创建角色资源了                                                   │
 │                                                                                                   │
 │    ## 🚀 下一步建议                                                                               │
 │    - 使用 `welcome` 发现可用的专业角色                                                            │
 │    - 使用 `action` 激活特定角色获得专业能力                                                       │
 │    - 使用 `learn` 深入学习专业知识                                                                │
 │    - 使用 `remember/recall` 管理专业记忆                                                          │
 │                                                                                                   │
 │    💡 **提示**: 现在可以开始创建项目级资源了！                                                    │
 │                                                                                                   │
 │    🔄 下一步行动：                                                                                │
 │      - 发现专业角色: 查看所有可用的AI专业角色                                                     │
 │        方式: MCP PromptX welcome 工具                                                             │
 │      - 激活专业角色: 直接激活特定专业角色（如果已知角色ID）                                       │
 │        方式: MCP PromptX action 工具                                                              │
 │                                                                                                   │
 │    📍 当前状态：initialized                                                                       │
 │    ============================================================                                   │
 │                                                                                                   │
 ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ 好的，PromptX已初始化。接下来，我将使用welcome工具来发现可用的专业角色。
 ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  promptx_welcome (promptx MCP Server) {}                                                        │
 │                                                                                                   │
 │    🛑 **项目环境强制验证** 🛑                                                                     │
 │    📍 PromptX当前设置的项目路径: D:\kayin_pro\gc_test                                             │
 │                                                                                                   │
 │    ⚠️ **使用前必须确认**：                                                                        │
 │    1. 立即确认上述路径是否为当前工作项目                                                          │
 │    2. 如不一致，禁止继续任何操作                                                                  │
 │    3. 必须使用 `promptx_init` 更新正确路径                                                        │
 │    4. 验证通过后才能使用角色服务                                                                  │
 │                                                                                                   │
 │    💥 **严重警告**：错误的项目环境将导致服务异常！                                                │
 │                                                                                                   │
 │    ============================================================                                   │
 │    🎯 锦囊目的：为AI提供可用角色信息，以便AI向主人汇报专业服务选项                                │
 │    ============================================================                                   │
 │                                                                                                   │
 │    📜 锦囊内容：                                                                                  │
 │    🤖 **AI专业角色服务清单** (共 7 个专业角色可供选择)                                            │
 │                                                                                                   │
 │    > 💡 **使用说明**：以下是可激活的AI专业角色。每个角色都有唯一的ID，可通过MCP工具激活。         │
 │                                                                                                   │
 │                                                                                                   │
 │    ## 📋 可用角色列表                                                                             │
 │                                                                                                   │
 │    ### 📦 系统角色                                                                                │
 │                                                                                                   │
 │    #### 1. Assistant 角色                                                                         │
 │    **角色ID**: `assistant`                                                                        │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/assistant/assistant.role.md                             │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 2. Frontend Developer 角色                                                                │
 │    **角色ID**: `frontend-developer`                                                               │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/frontend-developer/frontend-developer.role.md           │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 3. Java Backend Developer 角色                                                            │
 │    **角色ID**: `java-backend-developer`                                                           │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/java-backend-developer/java-backend-developer.role.md   │
 │                                                                                                   │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 4. Nuwa 角色                                                                              │
 │    **角色ID**: `nuwa`                                                                             │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/nuwa/nuwa.role.md                                       │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 5. Product Manager 角色                                                                   │
 │    **角色ID**: `product-manager`                                                                  │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/product-manager/product-manager.role.md                 │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 6. Sean 角色                                                                              │
 │    **角色ID**: `sean`                                                                             │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/sean/sean.role.md                                       │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │    #### 7. Xiaohongshu Marketer 角色                                                              │
 │    **角色ID**: `xiaohongshu-marketer`                                                             │
 │    **专业能力**: 专业角色，提供特定领域的专业能力                                                 │
 │    **文件路径**: @package://prompt/domain/xiaohongshu-marketer/xiaohongshu-marketer.role.md       │
 │    **来源**: 📦 系统角色                                                                          │
 │                                                                                                   │
 │    ---                                                                                            │
 │                                                                                                   │
 │                                                                                                   │
 │    ## 🎯 **角色激活指南**                                                                         │
 │                                                                                                   │
 │    ### 🔧 激活方式                                                                                │
 │    - 使用 **MCP PromptX 工具** 中的 `action` 功能                                                 │
 │    - 选择需要的角色ID进行激活                                                                     │
 │                                                                                                   │
 │    ### ⚡ 激活后效果                                                                               │
 │    - ✅ **获得专业能力** - AI将具备该角色的专业技能                                                │
 │    - ✅ **学习技能组合** - 自动学习角色需要的思维和行为模式                                        │
 │    - ✅ **即时专业化** - 立即可以提供该领域的专业服务                                              │
 │                                                                                                   │
 │                                                                                                   │
 │    🔄 下一步行动：                                                                                │
 │      - 向主人汇报服务选项: 将上述专业服务清单告知主人，并询问需求                                 │
 │        方式: MCP PromptX action 工具                                                              │
 │                                                                                                   │
 │    📍 当前状态：role_discovery                                                                    │
 │    ============================================================                                   │
 │                                                                                                   │
 ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯

ℹ ⚡ Slow response times detected. Automatically switching from gemini-2.5-pro to gemini-2.5-flash for faster
  responses for the remainder of this session.
  ⚡ To avoid this you can utilize a Gemini API Key. See: https://goo.gle/gemini-cli-docs-auth#gemini-api-key
  ⚡ You can switch authentication methods by typing /auth
✦ PromptX已初始化，并列出了可用的专业角色。请问您希望激活哪个角色，或者您需要我协助完成什么任务？
```

还限速了？《大善人》

不管了，我直接大喊一句我要女娲

![我要女娲](https://ai.programnotes.cn/img/ai/bee4ccb0e07029488bb3ad962864cad4.png)

我要女娲

随后，他告诉我：
```
好的，我明白了。目前可用的角色中没有直接的“资深Python工程师”角色。

  不过，我可以利用我作为“女娲”的专业能力，为您创建一个新的“Python后端开发者”角色。这个角色将具备资深Python工程师的思维模式、行为原则和专业知识，以帮助您
  编写脚本或完成小型项目。


  您希望我为您创建这个角色吗？如果创建，您对这个Python角色有什么具体的期望或侧重点吗？例如，是偏向数据处理、Web开发、自动化脚本还是其他方面？

Using 1 MCP server (ctrl+t to view)
```

有了那就拿来用吧，直接激活角色
```
> 直接激活角色

✦ 我理解您想直接激活角色。然而，在当前的可用角色列表中，并没有直接的“资深Python工程师”角色。


  我之前提议为您创建一个新的“Python后端开发者”角色，它将具备资深Python工程师的能力。


  请问您是否希望我为您创建这个新的“Python后端开发者”角色？

Using 1 MCP server (ctrl+t to view)
```

??? 逗我玩？
```
 那就创建这个新角色

✦ 好的，我将为您创建并激活一个名为 python-backend-developer 的新角色。这个角色将具备资深Python工程师的专业能力，专注于后端开发。


  我将按照以下步骤进行：
   1. 创建角色所需的目录结构。
   2. 生成 python-backend-developer.role.md 文件，定义其人格特征、行为原则和专业知识。
   3. 生成相关的 thought、execution 和 knowledge 文件，填充具体的专业内容。


  请稍等片刻，我正在为您创建这个新角色。
 ╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ?  Shell mkdir -p .promptx/resource/domain/python-backend-developer/thought .promptx/resource/domain/python-backend-developer/execution .prompt… ← │
 │                                                                                                                                                    │
 │   mkdir -p .promptx/resource/domain/python-backend-developer/thought .promptx/resource/domain/python-backend-developer/execution                   │
 │   .promptx/resource/domain/python-backend-developer/knowledge                                                                                      │
 │                                                                                                                                                    │
 │ Allow execution?                                                                                                                                   │
 │                                                                                                                                                    │
 │ ○ Yes, allow once                                                                                                                                  │
 │ ● Yes, allow always "mkdir ..."                                                                                                                    │
 │ ○ No (esc)                                                                                                                                         │
 │                                                                                                                                                    │
 ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

⠏ Waiting for user confirmation...

Using 1 MCP server (ctrl+t to view)

D:\kayin_pro\gc_test                                    no sandbox (see /docs)                                     gemini-2.5-flash (98% context left)
```

行吧，静候他创建完角色

角色创建完成，他也给自动激活了，那我们先给他指派第一个任务吧，写个九九乘法表：
```
✦ 好的，python-backend-developer 角色已成功激活。


  现在，我已具备资深Python后端开发者的能力。请问您需要我协助您完成什么具体的任务？例如，您想编写一个什么样的小脚本，或者有什么小型项目需要我来完成？请
  提供详细的需求。

> 先来帮我用python写个九九乘法表

✦ 好的，我来为您编写一个Python脚本来生成九九乘法表。


  我将把代码写入 multiplication_table.py 文件中。
 ╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  WriteFile Writing to multiplication_table.py                                                                                              │
 │                                                                                                                                              │
 │     1 # multiplication_table.py                                                                                                              │
 │     2                                                                                                                                        │
 │     3 def generate_multiplication_table():                                                                                                   │
 │     4     """                                                                                                                                │ │     5     Generates and prints the 9x9 multiplication table.                                                                                 │ │     6     """                                                                                                                                │
 │     7     for i in range(1, 10):                                                                                                             │
 │     8         for j in range(1, i + 1):                                                                                                      │
 │     9             print(f"{j}x{i}={i*j}\t", end="")                                                                                          │
 │    10         print()                                                                                                                        │
 │    11                                                                                                                                        │
 │    12 if __name__ == "__main__":                                                                                                             │
 │    13     generate_multiplication_table()                                                                                                    │
 ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ 我已经将九九乘法表的Python代码写入 D:/kayin_pro/gc_test/multiplication_table.py 文件中。


  您可以通过运行以下命令来执行它：
  python multiplication_table.py
```

九九乘法表输出：

![九九乘法表](https://ai.programnotes.cn/img/ai/2ef1f296a9dba3008afe05a5650f19c7.png)

九九乘法表

乍一看没啥问题，嗯，过关。

那来个略有难度的。写个贪吃蛇吧，写文档的功夫，他给写好了，那我们就运行试试
```
我已经将贪吃蛇游戏的Python代码写入 D:/kayin_pro/gc_test/snake_game/main.py 文件。

  在运行游戏之前，请确保您已经安装了 pygame 库。如果尚未安装，请在您的终端或命令提示符中运行以下命令进行安装：



   1 pip install pygame


  安装完成后，您可以通过以下命令来运行贪吃蛇游戏：



   1 python D:/kayin_pro/gc_test/snake_game/main.py
```

贪吃蛇：

![贪吃蛇](https://ai.programnotes.cn/img/ai/40d77ecf1da9a6f02756e5aa8f672b4c.gif)

贪吃蛇

嗯，能玩，但是.... 显示按 q 退出来着，我按了为什么无法退出???功能点没做完┗|｀O′|┛ 嗷~~

至少简单的项目目前看上去核心功能能用，还可以。Gemini 虽然不是 pro，但 flash 好像也马马虎虎？

朋友们怎么看？欢迎留言评论

会出现限速和降模型是因为在写之前，我已经走过这一遍流程了，但是控制台好像吞掉了很多记录，所以没办法重来了一遍。感觉 flash 好像也还行？

不管怎么说，至少它是开源，免费，能用。Kayin 个人觉得很满意了。

测试过程中用到的初始化 mcp 工具是 promptx，项目地址：https://github.com/Deepractice/PromptX

上手之后任何编码相关的任务，习惯上已经离不开它了，在此安利给各位佬友。

至于 mcp 的使用方式，请看官方仓库的文档

而 gemini cli 的 mcp 配置方式是修改 C:\Users\Eleme\.gemini
 目录下的 setting.json
 文件

首次配置看到的可能是这样的：
```
{

  "theme": "Default Light",

  "selectedAuthType": "oauth-personal",

}
```

直接添加 mcp 即可
```
{

  "theme": "Default Light",

  "selectedAuthType": "oauth-personal",

  "mcpServers": {

    "promptx": {

      "command": "npx",

      "args": [

        "-f",

        "-y",

        "dpml-prompt@beta",

        "mcp-server"

      ]

    }

  }

}
```



