---
title: "MCP Client|Apify Beta"
date: "2024-05-16"
tags: ["Apify", "MCP", "SSE", "AI agent", "actuator"]
categories: ["AI","MCP", "Tools"]
Description: "The Apify beta MCP client connects the AI ​​agent to the Apify ecosystem, and supports connecting to the MCP server through SSE to achieve interaction with the Apify executor."
author: "Unknown Author"
image: "https://raw.githubusercontent.com/apify/tester-mcp-client/refs/heads/main/docs/chat-ui.png"
---

**Core content:**
- Connect to the MCP server through the SSE protocol to achieve interaction with the Apify executor.
- Provide a class chat interface to display tool calls and results.
- The client is completely free, and only needs to pay for the LLM service provider usage fee and the Apify platform resource consumption.

This client connects AI agents to 5,000+ web crawlers and automated actuators (Actors) in the Apify ecosystem, supporting data extraction from websites, social media, search engines and maps.

## 🚀 Core functions

- 🔌 Connect to the MCP server via Server Push Event (SSE)
- 💬 Provides class chat interface display tool calls and results
- 🇦 Connect [Apify MCP Server](https://apify.com/apify/actors-mcp-server) to call multiple Apify executors
- 💥 Dynamically select tools based on context (server support is required)
- 🔓 Use authorization headers to ensure secure connections with API keys
- 🪟 Open source project, can review code or submit improvements

## 🎯 Functional Scene

After connecting to [Executor-MCP-Server] (https://apify.com/apify/actors-mcp-server), you can use the interactive chat interface:

- Query "The Most Popular Social Media Crawler Actuator"
- Get "The Best Instagram Crawlers"
- Consult "Which executor should be used to extract LinkedIn data"
- Learn about "How to Crawl Google Search Results"

![Client interface screenshot](https://raw.githubusercontent.com/apify/tester-mcp-client/refs/heads/main/docs/chat-ui.png)

## 📖 How it works

The client connects to the MCP server through the SSE protocol and implements the following functions:

- Establish an SSE connection through the `/sse` endpoint
- Send user query via `POST /message`
- Receive streaming responses in real time (via `GET /sse`), which may contain:
  - Large language model output
  - **Tool calls **Module
- Call and display the dialogue flow according to the response coordination tool

## ⚙️How to use

### Standard Mode (Apify Platform)

Run the client on the Apify platform and connect to any SSE-enabled MCP server. Configure the following parameters via the UI or API:

- MCP Server URL
- System prompt words
- API Key

After running, the log will generate a dynamic access link (different for each run):

```shell
INFO Please visit https://.........runs.apify.net to interact with the MCP server
```

### Standby mode (Apify platform)

In development 🚧

## 💰 Billing Plan

The client is completely free, only pay:

- LLM service provider usage fee
- Apify platform resource consumption

Adopt the [Bill by Event] (https://docs.apify.com/sdk/js/docs/guides/pay-per-event) mode:

- Actuator startup fee (billed at 128MB memory unit)
- Runtime fee (billed per 5 minutes/128MB unit)
- Query response fee (billed according to the model, and the built-in API key can be exempted)

When using your own LLM key, 128MB of memory runs for about $0.06 for 1 hour.
Apify free version (no credit card required) can run for 80 hours per month - fully meet testing needs!

## 📖 Technical Architecture

```plaintext
Browser ← (SSE) → Test Client ← (SSE) → MCP Server
```

This link encapsulates customized bridge logic within the client, keeping the MCP server pure.

1. Visit `https://tester-mcp-client.apify.actor?token=API key` (using http://localhost:3000 for local development)
2. Load `index.html` and `client.js` from the `public/` directory
3. The browser creates SSE stream through `GET /sse`
4. User query is submitted through `POST /message`
5. Query processing flow:
   - Calling large language model
   - Call the tool on demand
6. Return chunking results through `sseEmit(role, content)`

### Local Development

The client has been open sourced to [GitHub](https://github.com/apify/rag-web-browser), and can be modified as needed:

```bash
git clone https://github.com/apify/tester-mcp-client.git
cd tester-mcp-client
npm install
```

Create a configuration file with reference to `.env.example`:

```plaintext
APIFY_TOKEN=Your token
LLM_PROVIDER_API_KEY=Your key
```

Run the development server:

```bash
npm start
```

Visit [http://localhost:3000](http://localhost:3000) to start the test.

**I wish you a happy conversation with the Apify actuator! **

## ⓘ Notes

The current version does not support:

- Advanced MCP features such as Prompts and Resource
- Dialogue History Storage (refreshing the page will clear the record)

## Reference Resources

- [ModelContextProtocol](https://modelcontextprotocol.org/)
- [Apify Executor MCP Server](https://apify.com/apify/actors-mcp-server)
- [Billing instructions by event](https://docs.apify.com/sdk/js/docs/guides/pay-per-event)
- [Detailed explanation of AI agent](https://blog.apify.com/what-are-ai-agents/)\n- [MCP protocol core value](https://blog.apify.com/what-is-model-context-protocol/)
