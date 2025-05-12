---
title: "使用 go-zero MCP 创建动态提示词"
date: "2025-05-12"
tags: ["go-zero", "MCP", "动态提示词", "AI应用", "代码审查"]
categories: ["微服务", "人工智能"]
description: "本文介绍了如何使用 go-zero MCP 创建动态提示词，以增强 AI 应用的灵活性和智能化。"
author: "kevwan"
image: ""
---


核心内容:
- go-zero 的 MCP SDK 支持动态 Prompts，允许 AI 应用在运行时生成基于上下文、参数驱动的 Prompts。
- MCP Prompts 具有标准化、可重用性、用户控制、动态参数和上下文感知等优点。
- 通过定义配置、实现 Prompts 处理器，并向 MCP 服务器注册 Prompts，可以实现动态 Prompts 的功能。

**源自** | kevwan 微服务实践 2025-05-12 09:36

 

在当今 AI 应用越来越复杂、需求越来越高的情况下，单纯靠模型本身已经远远不够了。要想让AI 真正成为一个有"行动力"的智能体，它必须能够**动态调用外部工具、实时访问最新数据，并与用户持续交互**。

这就是 **Model Context Protocol（MCP）** 想要解决的问题。

## 理解 MCP 中的 Prompts

![](https://ai.programnotes.cn/img/ai/9a9cfe0bba4826fe2b13c467ee66f285.jpeg)

### MCP Prompts 的优点是标准化和优化LLM交互

标准化和可重用性：

-  MCP Prompts 允许开发者创建一致的、可重用的交互模式。这意味着常见的LLM交互（如代码审查、数据分析或内容生成）可以标准化并共享，减少重复开发工作。

用户控制：

- Prompts 是用户控制的，用户可以明确选择使用的 Prompts。这提供了灵活性，确保交互符合具体需求。

- 官方文档 Model Context Protocol Documentation: Prompts 指出，Prompts 是用户控制的，支持在运行推理前选择最优 Prompts。

动态参数和上下文：

- Prompts 可以接受动态参数，并结合资源上下文（如日志、代码文件）。这使交互更具定制性和上下文感知。

多步骤工作流：

- Prompts 支持多步骤工作流，允许复杂的顺序交互。例如，调试错误时，可以先通过 Prompts 识别问题，然后建议解决方案。

### MCP Prompts 的发现、调用和集成

发现：

• 通过 prompts/list 端点获取可用 Prompts 的列表。该端点返回 Prompts 的名称、描述和所需参数。

使用：

• 通过 prompts/get 请求使用 Prompts，用户可以提供参数进行定制。例如，一个名为“create-greeting” 的 Prompts 可能接受name和style参数。

资源集成：

• Prompts 可以与资源（如数据源）结合，增强上下文感知能力。例如，Prompts 可以引用日志或代码文件。

通知：

• 服务器通过 notifications/prompts/list_changed 通知客户端 Prompts 列表的变化。

• 客户端可通过 prompts/list 重新获取更新后的列表，确保同步。

go-zero 的 MCP SDK 最关键的特性之一就是对动态 Prompts 的支持，它允许你的 AI 应用在运行时生成基于上下文、参数驱动的 Prompts。与硬编码的静态 Prompts 不同，MCP 中的动态 Prompts 可以基于用户输入、系统状态或外部数据源生成。

### MCP 中的 Prompts 类型

go-zero MCP 框架支持：
- **静态 Prompts**,固定的 Prompts 模板

- **动态 Prompts**,基于输入参数在运行时生成的 Prompts

## 使用 MCP Prompts 的好处

<table><thead><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">特性</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">描述</span></section></td></tr></thead><tbody><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">🧠 动态生成</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">创建能够适应用户输入和上下文的 Prompts</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">✅ 参数验证</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">内置输入参数验证机制</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">🔄 上下文感知</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">在多次交互中维持状态</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">📦 标准化格式</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">使用 JSON-RPC 的一致 Prompts 结构</span></section></td></tr></tbody></table>

## 在 go-zero MCP 中实现动态 Prompts

### 步骤 1：定义配置

为 MCP 服务器创建配置文件：
```yaml
name: prompt-service
port: 8080
```

### 步骤 2：实现 Prompts 处理器

在你的 Go 应用中，注册基于输入参数生成动态 Prompts 的处理器：
```go
package main

import (
    "flag"
    "fmt"

    "github.com/zeromicro/go-zero/core/conf"
    "github.com/zeromicro/go-zero/core/logx"
    "github.com/zeromicro/go-zero/mcp"
)

var configFile = flag.String("f", "etc/config.yaml", "配置文件")

func main() {
    flag.Parse()

    var c mcp.McpConf
    conf.MustLoad(*configFile, &c)

    // 创建并启动 MCP 服务器
    server := mcp.NewMcpServer(c)

    // 注册你的 Prompts 处理器
    registerMyPrompt(server)

    // 启动服务器
    logx.Info("正在启动带有 SSE 传输的 MCP 服务器")
    server.Start()
}

// registerMyPrompt 注册动态 Prompts 处理器
func registerMyPrompt(server mcp.McpServer) {
    server.RegisterPrompt(mcp.Prompt{
        Name:        "get_custom_prompt",
        Description: "基于输入参数生成自定义提示词",
        Arguments: []mcp.PromptArgument{
            {
                Name:        "user_query",
                Description: "用户的原始查询",
                Required:    true,
            },
            {
                Name:        "context_id",
                Description: "可选的上下文标识符",
                Required:    false,
            },
        },
        Handler: func(ctx context.Context, args map[string]string) ([]mcp.PromptMessage, error) {
            // 解析参数
            var req struct {
                UserQuery string `json:"user_query"`
                ContextID string `json:"context_id,optional"`
            }
            if err := mcp.ParseArguments(args, &req); err != nil {
                return nil, fmt.Errorf("参数解析失败: %w", err)
            }

            // 基于输入参数生成动态提示词
            return []mcp.PromptMessage{
                {
                    Role: mcp.RoleUser,
                    Content: mcp.TextContent{
                        Text: fmt.Sprintf(`你是一个有帮助的助手。
请回答以下问题: %s
%s`, req.UserQuery, getContextInstructions(req.ContextID)),
                    },
                },
            }, nil
        },
    })
}

func getContextInstructions(contextID string) string {
    if contextID == "" {
        return ""
    }

    // 在实际应用中，你可能会基于 contextID 从数据库或外部服务
    // 获取特定上下文的指令
    return fmt.Sprintf("\n回答时，请考虑 ID 为 %s 的上下文", contextID)
}
```
## 实际案例：Golang 代码审查助手

让我们看一个使用 go-zero MCP Prompts 的实际案例 - 一个帮助进行 Golang 代码审查的智能助手。
```go
package main

import (
    "context"
    "flag"
    "fmt"

    "github.com/zeromicro/go-zero/core/conf"
    "github.com/zeromicro/go-zero/core/logx"
    "github.com/zeromicro/go-zero/mcp"
)

var configFile = flag.String("f", "etc/config.yaml", "配置文件")

func main() {
    flag.Parse()

    var c mcp.McpConf
    conf.MustLoad(*configFile, &c)

    // 创建并启动 MCP 服务器
    server := mcp.NewMcpServer(c)

    // 注册你的提示词处理器
    registerCodeReviewPrompt(server)

    // 启动服务器
    logx.Info("正在启动带有 SSE 传输的 MCP 服务器")
    server.Start()
}

// registerCodeReviewPrompt 注册代码审查提示词处理器
func registerCodeReviewPrompt(server mcp.McpServer) {
    server.RegisterPrompt(mcp.Prompt{
        Name:        "get_code_review_prompt",
        Description: "获取一个用于审查 Go 代码的提示词，提供最佳实践和改进建议",
        Arguments: []mcp.PromptArgument{
            {
                Name:        "code_snippet",
                Description: "要审查的代码片段",
                Required:    true,
            },
            {
                Name:        "focus_areas",
                Description: "审查重点领域，如性能、并发、安全等",
                Required:    false,
            },
        },
        Handler: func(ctx context.Context, args map[string]string) ([]mcp.PromptMessage, error) {
            var req struct {
                CodeSnippet string `json:"code_snippet"`
                FocusAreas  string `json:"focus_areas,optional"`
            }
            if err := mcp.ParseArguments(args, &req); err != nil {
                return nil, fmt.Errorf("参数解析失败: %w", err)
            }

            // 创建并返回带有详细指令的提示词消息
            return []mcp.PromptMessage{
                {
                    Role: mcp.RoleUser,
                    Content: mcp.TextContent{
                        Text: `你是一位经验丰富的 Go 语言专家，精通代码审查和最佳实践。`,
                    },
                },
                {
                    Role: mcp.RoleUser,
                    Content: mcp.TextContent{
                        Text: fmt.Sprintf(`请审查以下 Go 代码，并提供改进建议：

<go-code>
%s
</go-code>

请按以下方面进行评估：
1. 代码质量和可读性
2. Go 语言最佳实践的遵循情况
3. 潜在的错误或边缘情况
4. 性能优化机会
5. 并发安全性考虑
%s

请提供具体、可行的改进建议，并解释每个建议的理由。如果有必要，提供修改后的代码示例。`,
                            req.CodeSnippet,
                            getFocusAreasInstructions(req.FocusAreas)),
                    },
                },
            }, nil
        },
    })
}

func getFocusAreasInstructions(focusAreas string) string {
    if focusAreas == "" {
        return "6. 如有额外需要关注的方面，也请列出"
    }

    return fmt.Sprintf("6. 特别关注以下方面：%s", focusAreas)
}
```

交互流程如下图：

![](https://ai.programnotes.cn/img/ai/fe872e1f75336f411fde7bb73b196c0d.jpeg)

## 高级 Prompts 技术
### 1. 多消息 Prompts

你可以返回多个 Prompts 消息来创建更复杂的对话：
```go
return []mcp.PromptMessage{
    {
        Role: mcp.RoleSystem,
        Content: mcp.TextContent{
            Type: mcp.ContentTypeText,
            Text: "你是一个专注于代码审查的 AI 助手。",
        },
    },
    {
        Role: mcp.RoleUser,
        Content: mcp.TextContent{
            Type: mcp.ContentTypeText,
            Text: fmt.Sprintf("请审查这段代码: %s", codeSnippet),
        },
    },
}, nil
```
## MCP Prompts 的最佳实践
- **具体明确**：在 Prompts 中提供清晰、详细的指令

- **包含上下文**：添加相关上下文以帮助模型理解任务

- **使用参数**：利用动态参数使 Prompts 具有适应性

-  **验证输入**：在生成 Prompts 之前始终验证用户输入

- **优雅处理错误**：当参数无效时返回有意义的错误消息

- **保持安全**：注意不要在 Prompts 中包含敏感信息

- **全面测试**：使用各种输入测试你的 Prompts，确保它们按预期工作

## 开始使用

要开始使用 go-zero MCP Prompts：
- 安装最新版本的 go-zero (>= v1.8.3)

- 定义你的配置

- 实现你的 Prompts 处理器

- 向 MCP 服务器注册 Prompts

- 启动服务器并将其连接到你的 LLM 客户端（如 Claude Desktop）

下一篇我们将介绍 go-zero MCP Resources，敬请关注。有关更多信息和高级用法，请访问 go-zero 官方文档。
## 项目仓库
https://github.com/zeromicro/go-zero

请使用 go-zero 并 **star** 该仓库以支持我们的工作！




 

