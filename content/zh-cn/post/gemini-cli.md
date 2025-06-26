---
title: "Google开源的强大LLM工具：Gemini CLI"
date: "2025-06-26"
tags: ["CLI", "AI", "Gemini", "command-line", "workflow"]
categories: ["AI Tools", "Development"]
description: "连接到工具，了解代码并加速工作流程的命令行AI工作流程工具。"
author: "未知作者"
image: "https://ai.programnotes.cn/img/ai/cli/gemini-cli-1.png"
---

核心内容：
 -  **命令行AI工作流量工具，该工具连接到工具并了解代码**
 -  **支持查询/编辑大型代码库并从PDFS/Sketch生成应用程序**
 -  **包括增强功能的自动化功能和MCP服务器集成**

[![Gemini CLI CI](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml)

![Gemini CLI Screenshot](https://ai.programnotes.cn/img/ai/cli/gemini-cli-1.png)

该存储库包含Gemini CLI，这是一个连接到您的命令行AI工作流程工具
工具，了解您的代码并加速您的工作流程。

使用Gemini CLI，您可以：

 - 查询和编辑Gemini 1M令牌上下文窗口中的大型代码库。
 - 使用Gemini的多模式功能从PDF或草图生成新应用。
 - 自动化操作任务，例如查询拉力请求或处理复杂的篮板。
 - 使用工具和MCP服务器连接新功能，包括[Imagen的媒体生成，
  veo或lyria](https://github.com/googleclecloudplatform/vertex-ai-creative-studio/tree/main/main/main/experiments/mcp-genmedia)
 - 通过[Google Search](https://ai.google.dev/gemini-api/docs/grounding)进行查询
  工具，内置于双子座。

## 开始

1.**先决条件：**确保您有[Node.js版本18](https://nodejs.org/en/download)或更高的安装。
2.**运行CLI：**在您的终端中执行以下命令：

   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```

   或以：

   ```bash
   npm install -g @google/gemini -cli
   gemini
   ```

3.**选择颜色主题**

4.**身份验证：**提示时，请使用您的个人Google帐户登录。这将使您每分钟最多可提供60个模型请求，每天使用Gemini提出1,000个模型请求。

您现在准备使用Gemini CLI！

### 用于高级使用或增加限制：

如果您需要使用特定模型或需要更高的请求容量，则可以使用API​​密钥：

1.从[Google AI Studio](https://aistudio.google.com/apikey)生成密钥。
2.将其设置为终端中的环境变量。用生成的密钥替换`your_api_key`。

   ```bash
   export gemini_api_key =“ your_api_key”
   ```

有关其他身份验证方法，包括Google Workspace帐户，请参见[authentication](https://github.com/google-gemini/gemini/gemini-cli/blob/main/main/main/docs/cli/authication.md)指南。

## 示例

CLI运行后，您可以开始与外壳的双子座进行交互。

您可以从新目录启动项目：

```sh
gemini
>给我写一个Gemini Discord Bot，该机器人使用常见问题解答文件回答问题
```

或与现有项目合作：

```sh
git clone https://github.com/google-gemini/gemini-cli
cd gemini-Cli
gemini
>给我摘要昨天进行的所有更改
```

### 下一步

 - 了解如何[为源头做出贡献或构建](https://github.com/google-gemini/gemini/gemini-cli/blob/main/main/contributing.md)。
 - 探索可用的** [cli命令](https://github.com/google-gemini/gemini-cli/blob/blob/main/main/docs/cli/commands.md)**。
 - 如果遇到任何问题，请查看** [故障排除指南](https://github.com/google-gemini/gemini/gemini-cli/blob/main/main/docs/troubleshooting.md)**。
 - 有关更全面的文档，请参见[完整文档](https://github.com/google-gemini/gemini/gemini-cli/blob/main/main/docs/index.md)。
 - 看看一些[流行任务](＃流行任务)，以获取更多灵感。

### 故障排除

前往[故障排除](https://github.com/google-gemini/gemini-cli/blob/blob/main/docs/troubleshoot.md)查看。
