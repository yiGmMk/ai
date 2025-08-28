---
title: "Jina AI Remote MCP Server"
date: "2025-08-28"
tags: ["MCP", "Jina AI", "remote server", "API", "tools"]
categories: ["MCP", "AI"]
description: "A remote MCP server providing access to Jina APIs and tools.Jina AI 模型上下文协议（MCP）服务器，提供对 Jina Reader、Embeddings 和 Reranker API 的访问，并附带 URL 到 Markdown、网络搜索、图像搜索以及嵌入/重排序工具。"
author: "Jina AI"
image: ""
---

一个远程模型上下文协议（MCP）服务器，提供对 Jina Reader、Embeddings 和 Reranker API 的访问，并附带一套 URL 到 Markdown、网络搜索、图像搜索以及嵌入/重排序工具：

| 工具                     | 描述                                                                                                                                                                                                            | 是否需要 Jina API 密钥？ |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `primer`                 | 获取本地化的、时间感知的响应的当前上下文信息                                                                                                                                                                    | 否                        |
| `read_url`               | 通过 [Reader API](https://jina.ai/reader) 从网页中提取干净、结构化的内容作为 markdown                                                                                                                          | 可选*                     |
| `capture_screenshot_url` | 通过 [Reader API](https://jina.ai/reader) 捕获网页的高质量屏幕截图                                                                                                                                            | 可选*                     |
| `guess_datetime_url`     | 分析网页以获取具有置信度分数的最后更新/发布日期时间                                                                                                                                                            | 否                        |
| `search_web`             | 通过 [Reader API](https://jina.ai/reader) 搜索整个网络以获取当前信息和新闻                                                                                                                                      | 是                        |
| `search_arxiv`           | 通过 [Reader API](https://jina.ai/reader) 在 arXiv 存储库上搜索学术论文和预印本                                                                                                                                 | 是                        |
| `search_images`          | 通过 [Reader API](https://jina.ai/reader) 搜索整个网络中的图像（类似于 Google 图片）                                                                                                                             | 是                        |
| `expand_query`           | 通过 [Reader API](https://jina.ai/reader) 基于查询扩展模型扩展和重写搜索查询                                                                                                                                 | 是                        |
| `parallel_read_url`      | 通过 [Reader API](https://jina.ai/reader) 并行读取多个网页以实现高效的内容提取                                                                                                                                | 可选*                     |
| `parallel_search_web`    | 通过 [Reader API](https://jina.ai/reader) 并行运行多个网络搜索，以实现全面的主题覆盖和不同的视角                                                                                                             | 是                        |
| `parallel_search_arxiv`  | 通过 [Reader API](https://jina.ai/reader) 并行运行多个 arXiv 搜索，以实现全面的研究覆盖和不同的学术角度                                                                                                       | 是                        |
| `sort_by_relevance`      | 通过 [Reranker API](https://jina.ai/reranker) 根据与查询的相关性对文档进行重新排序                                                                                                                            | 是                        |
| `deduplicate_strings`    | 通过 [Embeddings API](https://jina.ai/embeddings) 和 [submodular optimization](https://jina.ai/news/submodular-optimization-for-diverse-query-generation-in-deepresearch) 获取前 k 个语义上唯一的字符串 | 是                        |
| `deduplicate_images`     | 通过 [Embeddings API](https://jina.ai/embeddings) 和 [submodular optimization](https://jina.ai/news/submodular-optimization-for-diverse-query-generation-in-deepresearch) 获取前 k 个语义上唯一的图像   | 是                        |

> 可选工具在没有 API 密钥的情况下也能工作，但有[速率限制](https://jina.ai/api-dashboard/rate-limit)。为了获得更高的速率限制和更好的性能，请使用 Jina API 密钥。您可以从 [https://jina.ai](https://jina.ai) 获取免费的 Jina API 密钥。

## Usage

对于支持远程 MCP 服务器的客户端：
```json
{
  "mcpServers": {
    "jina-mcp-server": {
      "url": "https://mcp.jina.ai/sse",
      "headers": {
        "Authorization": "Bearer ${JINA_API_KEY}" // 可选
      }
    }
  }
}
```

对于尚不支持远程 MCP 服务器的客户端，你需要使用 [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) 本地代理来连接到远程 MCP 服务器。

```json
{
  "mcpServers": {
    "jina-mcp-server": {
      "command": "npx",
      "args": [
        "mcp-remote", 
        "https://mcp.jina.ai/sse"
        // 可选的 bearer token
        "--header",
        "Authorization: Bearer ${JINA_API_KEY}"
        ]
    }
  }
}
```

## 故障排除

### 我陷入了工具调用循环——发生了什么？

这是 LMStudio 中一个常见问题，当默认上下文窗口为 4096 且你正在使用像 `gpt-oss-120b` 或 `qwen3-4b-thinking` 这样的思考模型时，就会发生这种情况。随着思考和工具调用的持续进行，一旦你达到上下文窗口限制，AI 就会开始丢失任务开始时的信息。这就是它陷入这种滚动上下文窗口的原因。

解决方案是以足够的上下文长度加载模型，以包含完整的工具调用链和思考过程。

![设置足够长的上下文](https://ai.programnotes.cn/img/ai/jina/1.png)

### 我看不到所有工具。

有些 MCP 客户端具有本地缓存，并且不会主动更新工具定义。如果你没有看到所有可用的工具，或者工具看起来已过时，你可能需要删除并重新添加 jina-mcp-server 到你的 MCP 客户端配置。这将强制客户端刷新其缓存的工具定义。在 LMStudio 中，你可以点击刷新按钮来加载新工具。

![更新本地 mcp 客户端](https://ai.programnotes.cn/img/ai/jina/2.png)

### Claude Desktop 在 Windows 上显示“服务器已断开”

Cursor 和 Claude Desktop (Windows) [存在一个 bug](https://www.npmjs.com/package/mcp-remote#:~:text=Note%3A%20Cursor,env%20vars%0A%20%20%7D%0A%7D%2C)，当它调用 npx 时，参数内部的空格不会被转义，最终导致这些值被破坏。你可以使用以下方法解决这个问题：

```json
{
  // 其他配置...
  "args": [
    "mcp-remote",
    "https://mcp.jina.ai/sse",
    "--header",
    "Authorization:${AUTH_HEADER}" // 注意 ':' 周围没有空格
  ],
  "env": {
    "AUTH_HEADER": "Bearer <JINA_API_KEY>" // 环境变量中可以有空格
  }
},
```

### Cursor 在此 MCP 状态上显示红点

[很可能是 Cursor 的一个 UI bug](https://forum.cursor.com/t/why-is-my-mcp-red/100518)，但 MCP 工作正常，没有任何问题。如果红点让你感到烦恼，你可以关闭/打开来“重启”MCP（事实上，由于你将它用作远程MCP，这并不是真正的“服务器重启”，而主要是一个本地代理重启）。

![cursor shows red dot](https://ai.programnotes.cn/img/ai/jina/3.png)

If your Large Language Model (LLM) isn't utilizing certain tools even when they're enabled in your MCP client, it's probably showing a preference for specific tools, a common behavior when an LLM is trained with a defined toolset. For instance, `parallel_*` tools are rarely used organically unless directly instructed. In Cursor, you can modify your `.mdc` file with the following rule:

```text
---
alwaysApply: true
---

When you are uncertain about knowledge, or the user doubts your answer, always use Jina MCP tools to search and read best practices and latest information. Use search_arxiv and read_url together when questions relate to theoretical deep learning or algorithm details. search_web and search_arxiv cannot be used alone - always combine with read_url or parallel_read_url to read from multiple sources. Remember: every search must be complemented with read_url to read the source URL content. For maximum efficiency, use parallel_* versions of search and read when necessary.
```

## 开发者指南

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/jina-ai/MCP.git
cd MCP

# 安装依赖
npm install

# 启动开发服务器
npm run start
```

### 部署到 Cloudflare Workers

[![部署到 Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/jina-ai/MCP)

这将会把你的 MCP 服务器部署到一个 URL，例如：`jina-mcp-server.<your-account>.workers.dev/sse`
