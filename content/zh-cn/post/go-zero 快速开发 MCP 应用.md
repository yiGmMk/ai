---
title: "go-zero 快速开发 MCP 应用"
date: "2025-05-06"
tags: ["go-zero", "MCP", "AI", "微服务", "Server-Sent Events", "JSON-RPC", "SDK"]
categories: ["Go", "AI 应用开发","MCP"]
description: "go-zero 团队推出 MCP SDK，帮助开发者快速搭建支持 MCP 协议的 AI 应用，实现模型能力扩展、实时交互和持续对话。"
author: "kevwan"
image: ""
---

**源自** |  kevwan  微服务实践   2025-05-06 09:01  
  
在 AI 应用越来越复杂、需求越来越高的今天，单纯靠模型本身已经远远不够了。  
  
要想让 AI 真正成为一个有“行动力”的智能体，它必须能够**动态调用外部工具、实时访问最新数据，并与用户持续交互** 。  
  
这，就是 **Model Context Protocol（MCP）** 想要解决的问题。  
## 什么是 MCP？  
  
**MCP（Model Context Protocol）** 是一种为 AI 应用设计的开放协议，它让模型在推理过程中，能主动请求外部数据、调用外部工具，甚至管理长时间的对话上下文。  
  
简单理解，MCP 赋予了模型三大超能力：  
- **能力扩展**：模型可以调用各种外部系统，比如搜索引擎、数据库、计算工具。  
  
- **实时交互** ：模型能够拿到实时数据，而不是靠旧知识硬答。  
  
- **持续对话** ：用户和模型之间保持流畅的、有上下文感知的沟通。  
  
MCP 使用 **Server-Sent Events (SSE)**保持持久连接，基于 **JSON-RPC**进行标准化通信，让开发者可以非常方便地接入。  

> 🎯 一句话总结：**MCP 让你的AI应用变得聪明且灵活！**  
  
  
![mcp.jpeg](https://ai.programnotes.cn/img/ai/d404d038aceb22fb87020f7a2fc8f0c6.jpeg) 

## 为什么要用 go-zero MCP SDK？  
  
为了让大家更快、更轻松地搭建支持 MCP 协议的 AI 应用，**go-zero团队** 推出了**MCP SDK**go-zero >= v1.8.3）。  
  
它帮你处理了所有底层细节，让你专注在最重要的事情上：  

**写业务逻辑，打造智能体验。**  
  
主要特点包括：  
  
<table><thead><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">功能模块</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">描述</span></section></td></tr></thead><tbody><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">🚀 实时通信</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">基于 SSE，低延迟、稳定连接。</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">🛠️ 工具系统</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">支持动态注册外部工具，带超时、错误处理。</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">🧠 动态提示</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">支持静态和动态 Prompt，参数验证超方便。</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">📦 资源管理</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">外部资源注册、访问、变更订阅一条龙。</span></section></td></tr><tr style="box-sizing: border-box;border-width: 0px;border-style: solid;border-color: rgb(229, 229, 229);"><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">📚 JSON-RPC</span></section></td><td style="box-sizing: border-box;border: 1px solid rgb(223, 223, 223);text-align: left;line-height: 1.75;font-family: -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 14px;padding: 0.25em 0.5em;color: rgb(63, 63, 63);word-break: keep-all;"><section><span leaf="">标准规范处理请求和响应，兼容性无忧。</span></section></td></tr></tbody></table>  
  
持续迭代中，力求打造最简单易用的 MCP SDK，后续会通过 API  
 文件直接生成 MCP server。  
  
基于 **go-zero**  
 框架本身的高性能特性，整个 MCP SDK 在大规模并发场景下也能跑得非常稳。  
## 快速上手示例：打造一个智能计算器 

### 1. 写配置文件  
  
config.yaml：  
```
name: calculator-assistantport: 8080
```  
### 2. 写服务端逻辑  
  
main.go：  
```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/zeromicro/go-zero/core/conf"
    "github.com/zeromicro/go-zero/mcp"
)

func main() {
    // 加载配置
    var c mcp.McpConf
    conf.MustLoad("config.yaml", &c)

    // 创建 MCP 服务器
    server := mcp.NewMcpServer(c)
    defer server.Stop()

    // 注册计算器工具
    calculatorTool := mcp.Tool{
        Name:        "calculator",
        Description: "执行基础数学运算",
        InputSchema: mcp.InputSchema{
            Properties: map[string]any{
                "operation": map[string]any{
                    "type":        "string",
                    "description": "要执行的操作 (add, subtract, multiply, divide)",
                    "enum":        []string{"add", "subtract", "multiply", "divide"},
                },
                "a": map[string]any{
                    "type":        "number",
                    "description": "第一个操作数",
                },
                "b": map[string]any{
                    "type":        "number",
                    "description": "第二个操作数",
                },
            },
            Required: []string{"operation", "a", "b"},
        },
        Handler: func(ctx context.Context, params map[string]any) (any, error) {
            var req struct {
                Operation string`json:"operation"`
                A         float64`json:"a"`
                B         float64`json:"b"`
            }

            if err := mcp.ParseArguments(params, &req); err != nil {
                returnnil, fmt.Errorf("参数解析失败: %v", err)
            }

            // 执行操作
            var result float64
            switch req.Operation {
            case"add":
                result = req.A + req.B
            case"subtract":
                result = req.A - req.B
            case"multiply":
                result = req.A * req.B
            case"divide":
                if req.B == 0 {
                    returnnil, fmt.Errorf("除数不能为零")
                }
                result = req.A / req.B
            default:
                returnnil, fmt.Errorf("未知操作: %s", req.Operation)
            }

            // 返回格式化结果
            returnmap[string]any{
                "expression": fmt.Sprintf("%g %s %g", req.A, getOperationSymbol(req.Operation), req.B),
                "result":     result,
            }, nil
        },
    }

    // 注册工具到服务器
    if err := server.RegisterTool(calculatorTool); err != nil {
        log.Fatalf("注册计算器工具失败: %v", err)
    }

    fmt.Printf("启动 MCP 服务器，端口: %d\n", c.Port)
    server.Start()
}

func getOperationSymbol(op string)string {
    switch op {
    case"add":
        return"+"
    case"subtract":
        return"-"
    case"multiply":
        return"×"
    case"divide":
        return"÷"
    default:
        return op
    }
}
```  
### 3.启动MCP服务器  
  
在终端中运行以下命令以启动 MCP 服务器：  
```
go run main.go
```  
  
如果配置正确，您将看到类似以下的输出：  
```
MCP 服务器启动，端口：8080
```  
  
此时，MCP 服务器已经成功运行，您可以通过指定的端口与其交互。  
  
这里只演示了 tools，后续文章再介绍 prompts 和 resources。  

### 4. 配置 MCP（Claude Desktop 为例）  
  
Claude Desktop 作为客户端可以通过配置文件连接到 MCP 服务器。以下是配置 Claude Desktop 连接到文件系统 MCP 服务器的方法：  
1. 首先确保您已安装最新版本的 Claude Desktop  
  
2. 在 macOS 上，点击菜单栏中的 Claude 图标，选择"Settings..."，然后在左侧栏点击"Developer"，再点击"Edit Config"。这将创建或打开配置文件：  
• macOS: ~/Library/Application Support/Claude/claude_desktop_config.json  
• Windows: %APPDATA%\Claude\claude_desktop_config.json  
  
3. 编辑配置文件，添加 MCP 服务器信息：  
  
```json
{  
  "mcpServers": {    
    "calculator": {     
         "command": "npx",     
         "args": ["mcp-remote", "http://localhost:8080/sse"]   
    }  
  }
}
```  
配置说明：  
  
- name: MCP 服务器的显示名称  
- command: 如果需要启动本地服务，这里填写启动命令  
- args: 参数，用来指定通过 mcp-remote, 连接 http://localhost:8080/sse  
  
配置完成后，重启 Claude Desktop 应用。连接成功后，在输入框右下角会显示工具图标。  
  
## 支持的返回内容类型  
  
在 Tool 处理器里，你可以灵活返回：  
- • 文本（字符串）  
  
- • 结构化数据（map[string]any）  
  
- • 丰富内容对象（如 TextContent, ImageContent）  
  
- • 内容数组  
  
- • 标准错误对象  
  
## 交互流程  

![](https://ai.programnotes.cn/img/ai/21c4cf113c60e6811ba2e430cae9d8e7.jpeg)  
  
## 项目地址  
  
https://github.com/zeromicro/go-zero  
  
欢迎使用 go-zero 并 **star** 支持我们！  
  
   
  
