---
title: "MCP-Scan 介绍：使用不变量保护 MCP" 
date: "2025-05-08" 
tags: ["MCP", "安全", "扫描器", "漏洞", "工具中毒"] 
categories: ["安全", "MCP", "AI"] 
description: "MCP-Scan 是一款安全扫描器，旨在保护 Agentic 系统免受基于 MCP 的安全漏洞侵害。" 
author: "Luca Beurer-Kellner, Marc Fischer" 
image: ""
---
MCP-Scan 是一款安全扫描器，旨在保护您的代理系统免受基于 MCP 的安全漏洞的侵害，包括工具投毒攻击和 MCP Rug Pulls。

[github,代码仓库](https://github.com/invariantlabs-ai/mcp-scan)

![图片 4：MCP-Scan](https://invariantlabs.ai/images/mcp-scan-launch.svg)

Invariant 很高兴地宣布 [**MCP-Scan**](https://github.com/invariantlabs-ai/mcp-scan)，这是一款新颖的安全扫描工具，专门用于在使用模型上下文协议 (MCP) 时保护代理 AI 系统免受安全漏洞的侵害。

## 为什么选择 MCP-Scan？

正如最近的研究发现的那样（[工具投毒攻击](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)，[WhatsApp MCP 漏洞利用](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)），各种平台（如 Cursor、Claude Desktop、Zapier 等）上的 MCP 实现容易受到危险攻击。这些漏洞包括提示注入、隐藏的恶意工具指令（工具投毒攻击）以及通过工具阴影实现的跨域升级。

认识到这些严重的安全威胁，我们开发了 **MCP-Scan**，以帮助用户快速识别其 MCP 安装中的漏洞，从而确保更安全、更可靠的代理交互。

**担心 MCP 和代理安全？**
注册以提前访问 Invariant Guardrails，我们的安全平台不仅限于扫描，还涵盖许多攻击媒介和安全问题，包括 MCP 攻击。[了解更多](https://invariantlabs.ai/guardrails)

## MCP-Scan 如何保护您的系统

MCP-Scan 主动扫描已安装的 MCP 服务器及其工具描述，以识别：

*   **工具投毒攻击：** 嵌入在 MCP 工具描述中的隐藏恶意指令。
*   **MCP Rug Pulls：** 初始用户批准后对 MCP 工具描述的未经授权的更改。
*   **跨域升级：** 通过恶意描述损害受信任工具的阴影攻击。
*   **提示注入攻击：** 工具描述中包含的可能由代理执行的恶意指令。

## 快速简便的安全检查

MCP-Scan 无缝集成到您的工作流程中，并且可以使用简单的命令运行。无需配置。

```sh
uvx mcp-scan@latest
```

该工具会扫描您的 MCP 配置文件，连接到服务器并检索工具描述，在本地分析它们并使用 Invariant Guardrails API 来识别恶意指令。

要运行此命令，请确保您的系统上安装了 [`uv`](https://docs.astral.sh/uv/) 包管理器。

这将从 PyPI 加载最新的源代码和依赖项，如果您更喜欢从源代码运行，请查看 [GitHub 仓库](https://github.com/invariantlabs-ai/mcp-scan)。

## 扫描结果示例

以下是 MCP-Scan 实际运行的示例，清楚地识别出易受攻击的 MCP 工具：

![图片 5：MCP-Scan 示例](https://invariantlabs.ai/images/mcp-scan-output.png)

在此示例中，MCP-Scan 检测到安全风险，包括工具描述中的提示注入。识别后，您可以使用 `uvx mcp-scan@latest inspect` 查看相关的工具描述并采取措施。

## 通过工具固定增强安全性

MCP-Scan 包括内置的 **工具固定** 功能，可通过工具哈希跟踪更改来验证已安装工具的完整性，从而检测和防止 MCP Rug Pull 攻击。这允许用户检测对工具描述的更改。

## 跨域升级检测

MCP-Scan 还可以识别跨域升级攻击或 [工具阴影](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)，其中恶意工具描述可以阴影化受信任的工具。对于依赖多个 MCP 服务器的用户来说，这一点尤其重要。

为了缓解这些攻击，MCP-Scan 专门扫描不同 MCP 服务器之间的交叉引用，从而确保在指令级别上实现强化的隔离。

## 检查您已安装的工具

您可以随时使用以下命令检查详细的工具描述：

```sh
uvx mcp-scan@latestinspect
```

## 贡献和社区

MCP-Scan 是开源的，我们欢迎您的贡献、建议和功能请求。加入我们的 [Discord](https://discord.gg/dZuZfhKnJ4) 或 [GitHub](https://github.com/invariantlabs-ai/mcp-scan) 以参与保护代理系统的未来。

## 扫描期间的数据隐私

MCP-Scan 会搜索您的配置文件以查找 MCP 服务器配置。它连接到这些服务器并检索工具描述。只有在通过其命令显式调用时才会这样做。

然后，它会扫描工具描述，包括本地检查以及通过 API 调用 Invariant Guardrailing 模型。为此，工具名称和描述会与 Invariant 共享。通过使用 MCP-Scan，您同意 Invariant Labs 的 [使用条款](https://explorer.invariantlabs.ai/terms) 和 [隐私政策](https://invariantlabs.ai/privacy-policy)。

在扫描期间，Invariant 会出于安全研究目的收集数据（仅关于工具描述以及它们如何随时间变化，而不是您的用户数据）。如果您不想共享您的工具描述，请勿使用 MCP-scan。如果您对专用或私有部署感兴趣，请 [联系我们](mailto:mcpscan@invariantlabs.ai)。

MCP-scan 不会存储或记录任何 MCP 使用数据，即您的 MCP 工具调用的内容和结果。

## 入门

立即使用 MCP-Scan 保护您的代理 AI 系统免受 MCP 安全漏洞的侵害。在 GitHub 上为该仓库加注星标或为该项目做出贡献，以帮助我们改进 MCP-Scan 并使其在保护代理系统方面更加有效。

[立即试用 MCP-Scan](https://github.com/invariantlabs-ai/mcp-scan)

## 关于 Invariant

Invariant 致力于确保代理 AI 系统的安全性和稳健性。我们的研究和工具解决了关键漏洞，从而能够在实际场景中安全可靠地部署 AI。如果您有兴趣与我们合作以增强代理系统的安全性和完整性，请 [联系我们](mailto:hello@invariantlabs.ai)。

[invariantlabs,blog](https://invariantlabs.ai/blog)
