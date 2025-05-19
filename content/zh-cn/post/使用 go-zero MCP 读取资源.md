```yaml
---
title: "使用 go-zero MCP 读取资源"
date: "2025-05-18"
tags: ["go-zero", "MCP", "资源管理", "AI应用", "微服务"]
categories: ["微服务", "AI"]
description: "本文介绍了如何使用 go-zero MCP SDK 来管理和使用 MCP 资源，为 AI 模型提供数据访问能力。"
author: "kevwan"
image: ""
---
```

**核心内容点**:
- 介绍了 MCP 资源的核心功能，包括访问最新数据、结构化处理和资源定位。
- 展示了使用 go-zero MCP SDK 读取资源的最简单示例，通过 URI 读取对应内容。
- 强调了资源管理在构建强大 AI 应用中的重要性，以及 MCP 协议如何使 AI 模型能够访问丰富的外部数据。

**源自** |kevwan微服务实践 2025-05-18 17:22

在构建智能 AI 应用时，资源管理是至关重要的一环。本文将介绍如何使用 go-zero MCP SDK 来使用 MCP 资源。

## MCP 资源概述

MCP（Model Context Protocol）资源允许 AI 模型访问和操作外部数据，包括文件、数据库和 API 等。资源是 MCP 协议的关键组件之一，为 AI 模型提供了与外部世界交互的标准化接口。
### 资源的核心功能

通过 MCP 资源，AI 模型可以：
- **访问最新数据** ：通过统一的资源 URI 系统获取实时的外部数据，确保模型始终使用最新信息

- **结构化处理**：以标准格式处理复杂数据，支持文本、二进制、JSON等多种数据类型

-**资源定位**：通过统一的 URI 机制访问不同类型的外部资源

### 资源的标识与结构

资源在 MCP 中通过 URI 标识符进行唯一识别，遵循 RFC3986 规范。每个资源都由以下核心组件构成：
- • **URI**：资源的唯一标识符，如 file:///data/example.txt 或 db://collection/item

- • **名称**：人类可读的资源名称，用于在界面或日志中显示

- • **描述**：对资源用途和内容的简要说明

- • **MIME类型**：资源内容的媒体类型，如 text/plain 或 image/png

- • **处理函数**：负责实际读取、写入或处理资源内容的逻辑
资源内容可以多种格式存在，包括文本内容（text）和二进制数据（通过 Base64 编码的 blob）。
## 最简单的示例

这是一个最简单的示例，通过给定的 URI 读取对应内容。
```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/zeromicro/go-zero/core/conf"
    "github.com/zeromicro/go-zero/mcp"
)

const fileContent = `package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
`

// Example MCP server demonstrating tool, prompt, and resource registration
func main() {
    // Load configuration from YAML file
    var c mcp.McpConf
    if err := conf.Load("config.yaml", &c); err != nil {
        log.Fatalf("Failed to load config: %v", err)
    }

    // Create MCP server
    server := mcp.NewMcpServer(c)
    defer server.Stop()

    goResource := mcp.Resource{
        Name:        "go-example",
        URI:         "file:///project/src/main.go",
        Description: "A simple Go example with multiple files",
        Handler: func(ctx context.Context) (mcp.ResourceContent, error) {
            return mcp.ResourceContent{
                MimeType: "text/x-go",
                Text:     fileContent,
            }, nil
        },
    }
    server.RegisterResource(goResource)

    fmt.Printf("Starting MCP server on :%d\n", c.Port)
    defer server.Stop()
    server.Start()
}
```
## 资源内容格式

资源内容可以采用多种格式，go-zero MCP SDK 支持：
- **文本内容**：通过 Text 字段提供纯文本内容

- **二进制内容**：通过 Blob 字段提供 Base64 编码的二进制数据

- **MIME类型**：通过 MimeType 字段指定内容的媒体类型

通过这些方式，MCP 资源极大地扩展了 AI 模型的能力，使其能够访问、处理和生成外部数据，从而构建更加实用和强大的 AI 应用。

## 结论

通过 go-zero MCP SDK，我们可以轻松实现和管理 MCP 资源。上述示例展示了如何创建一个简单的文件资源服务，该服务允许 AI 模型通过标准协议读写文件。当然你也可以基于 Tools 扩展更多功能，如目录浏览、文件搜索或自定义元数据处理等。

资源管理是构建强大 AI 应用的关键部分，它让 AI 模型能够与外部世界交互，获取最新数据，并持久化重要信息。通过标准化的 URI 系统和资源处理机制，MCP 协议使 AI 模型能够访问丰富的外部数据，并以一致的方式进行交互，从而构建更加智能和实用的 AI 应用系统。

在实际应用中，资源可以与工具（Tools）和提示（Prompts）结合使用，创建完整的 AI 交互系统。例如，一个文档管理 AI 可以使用资源来存储和检索文档，使用工具来处理文档内容，使用提示来生成人类可读的响应。这种组合为构建复杂的 AI 应用提供了强大而灵活的框架。
## 项目地址

https://github.com/zeromicro/go-zero



 

