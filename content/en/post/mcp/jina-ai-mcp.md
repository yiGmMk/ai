---
title: "Jina AI Remote MCP Server"
date: "2025-08-28"
tags: ["MCP", "Jina AI", "remote server", "API", "tools"]
categories: ["MCP", "AI"]
description: "A remote MCP server providing access to Jina APIs and tools."
author: "Jina AI"
image: ""
---

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=jina-mcp-server&config=eyJ1cmwiOiJodHRwczovL21jcC5qaW5hLmFpL3NzZSIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciBqaW5hXzg3ZGEyOTM2NDI2NDQzNDliNmE0MGM4Mzc4NDViNGYzR0hpZ3FXay1yNmtIY0ZPSm1jY29rb1RiaWpZYiJ9fQ%3D%3D)
[![Add MCP Server jina-mcp-server to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=jina-mcp-server&config=eyJ1cmwiOiJodHRwczovL21jcC5qaW5hLmFpL3NzZSIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciBqaW5hXzI5NGQ5NmRiODFiYTQ1ZjY5MDFiOGM2OTRmM2I3NDU4ZVJMaV9MRS1xOGNqejRCeUE3REJ2cGZPUm5fdSJ9fQ%3D%3D)

A remote Model Context Protocol (MCP) server that provides access to Jina Reader, Embeddings and Reranker APIs with a suite of URL-to-markdown, web search, image search, and embeddings/reranker tools:

| Tool                     | Description                                                                                                                                                                                                     | Is Jina API Key Required? |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `primer`                 | Get current contextual information for localized, time-aware responses                                                                                                                                          | No                        |
| `read_url`               | Extract clean, structured content from web pages as markdown via [Reader API](https://jina.ai/reader)                                                                                                           | Optional*                 |
| `capture_screenshot_url` | Capture high-quality screenshots of web pages via [Reader API](https://jina.ai/reader)                                                                                                                          | Optional*                 |
| `guess_datetime_url`     | Analyze web pages for last update/publish datetime with confidence scores                                                                                                                                       | No                        |
| `search_web`             | Search the entire web for current information and news via [Reader API](https://jina.ai/reader)                                                                                                                 | Yes                       |
| `search_arxiv`           | Search academic papers and preprints on arXiv repository via [Reader API](https://jina.ai/reader)                                                                                                               | Yes                       |
| `search_images`          | Search for images across the web (similar to Google Images) via [Reader API](https://jina.ai/reader)                                                                                                            | Yes                       |
| `expand_query`           | Expand and rewrite search queries based on the query expansion model via [Reader API](https://jina.ai/reader)                                                                                                   | Yes                       |
| `parallel_read_url`      | Read multiple web pages in parallel for efficient content extraction via [Reader API](https://jina.ai/reader)                                                                                                   | Optional*                 |
| `parallel_search_web`    | Run multiple web searches in parallel for comprehensive topic coverage and diverse perspectives via [Reader API](https://jina.ai/reader)                                                                        | Yes                       |
| `parallel_search_arxiv`  | Run multiple arXiv searches in parallel for comprehensive research coverage and diverse academic angles via [Reader API](https://jina.ai/reader)                                                                | Yes                       |
| `sort_by_relevance`      | Rerank documents by relevance to a query via [Reranker API](https://jina.ai/reranker)                                                                                                                           | Yes                       |
| `deduplicate_strings`    | Get top-k semantically unique strings via [Embeddings API](https://jina.ai/embeddings) and [submodular optimization](https://jina.ai/news/submodular-optimization-for-diverse-query-generation-in-deepresearch) | Yes                       |
| `deduplicate_images`     | Get top-k semantically unique images via [Embeddings API](https://jina.ai/embeddings) and [submodular optimization](https://jina.ai/news/submodular-optimization-for-diverse-query-generation-in-deepresearch)  | Yes                       |

> Optional tools work without an API key but have [rate limits](https://jina.ai/api-dashboard/rate-limit). For higher rate limits and better performance, use a Jina API key. You can get a free Jina API key from [https://jina.ai](https://jina.ai)

## Usage

For client that supports remote MCP server:
```json
{
  "mcpServers": {
    "jina-mcp-server": {
      "url": "https://mcp.jina.ai/sse",
      "headers": {
        "Authorization": "Bearer ${JINA_API_KEY}" // optional
      }
    }
  }
}
```

For client that does not support remote MCP server yet, you need [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) a local proxy to connect to the remote MCP server.

```json
{
  "mcpServers": {
    "jina-mcp-server": {
      "command": "npx",
      "args": [
        "mcp-remote", 
        "https://mcp.jina.ai/sse"
        // optional bearer token
        "--header",
        "Authorization: Bearer ${JINA_API_KEY}"
        ]
    }
  }
}
```

## Troubleshooting

### I got stuck in a tool calling loop - what happened?

This is a common issue with LMStudio when the default context window is 4096 and you're using a thinking model like `gpt-oss-120b` or `qwen3-4b-thinking`. As the thinking and tool calling continue, once you hit the context window limit, the AI starts losing track of the beginning of the task. That's how it gets trapped in this rolling context window.

The solution is to load the model with enough context length to contain the full tool calling chain and thought process.

![set long enough context](https://ai.programnotes.cn/img/ai/jina/1.png)

### I can't see all tools.

Some MCP clients have local caching and do not actively update tool definitions. If you're not seeing all the available tools or if tools seem outdated, you may need to remove and re-add the jina-mcp-server to your MCP client configuration. This will force the client to refresh its cached tool definitions. In LMStudio, you can click the refresh button to load new tools.

![update local mcp clients](https://ai.programnotes.cn/img/ai/jina/2.png)

### Claude Desktop says "Server disconnected" on Windows

Cursor and Claude Desktop (Windows) [have a bug](https://www.npmjs.com/package/mcp-remote#:~:text=Note%3A%20Cursor,env%20vars%0A%20%20%7D%0A%7D%2C) where spaces inside args aren't escaped when it invokes npx, which ends up mangling these values. You can work around it using:

```json
{
  // rest of config...
  "args": [
    "mcp-remote",
    "https://mcp.jina.ai/sse",
    "--header",
    "Authorization:${AUTH_HEADER}" // note no spaces around ':'
  ],
  "env": {
    "AUTH_HEADER": "Bearer <JINA_API_KEY>" // spaces OK in env vars
  }
},
```

### Cursor shows a red dot on this MCP status

[Likely a UI bug from Cursor](https://forum.cursor.com/t/why-is-my-mcp-red/100518), but the MCP works correctly without any problem. You can toggle off/on to "restart" the MCP if you find the red dot annoying (fact is, since you are using this as a remote MCP, it's not a real "server restart" but mostly a local proxy restart).

![cursor shows red dot](https://ai.programnotes.cn/img/ai/jina/3.png)

### My LLM never uses some tools

Assuming all tools are enabled in your MCP client but your LLM still never uses some tools, it's likely your LLM favors some tools over others, which is pretty common when an LLM is trained with a specific set of tools. For example, we rarely see `parallel_*` tools being used organically by LLMs unless they are explicitly instructed to do so. In Cursor, you can add the following rule to your `.mdc` file:

```text
---
alwaysApply: true
---

When you are uncertain about knowledge, or the user doubts your answer, always use Jina MCP tools to search and read best practices and latest information. Use search_arxiv and read_url together when questions relate to theoretical deep learning or algorithm details. search_web and search_arxiv cannot be used alone - always combine with read_url or parallel_read_url to read from multiple sources. Remember: every search must be complemented with read_url to read the source URL content. For maximum efficiency, use parallel_* versions of search and read when necessary.
```

## Developer Guide

### Local Development

```bash
# Clone the repository
git clone https://github.com/jina-ai/MCP.git
cd MCP

# Install dependencies
npm install

# Start development server
npm run start
```

### Deploy to Cloudflare Workers

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/jina-ai/MCP)

This will deploy your MCP server to a URL like: `jina-mcp-server.<your-account>.workers.dev/sse`