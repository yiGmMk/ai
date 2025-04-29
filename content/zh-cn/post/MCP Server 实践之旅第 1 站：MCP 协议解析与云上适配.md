---
title: "MCP Server 实践之旅第 1 站：MCP 协议解析与云上适配"
date: "2025-04-27"
tags: ["MCP", "Serverless", "函数计算", "SSE", "STDIO", "JSON-RPC", "大模型", "AI"]
categories: ["Serverless", "AI"]
description: 本文深入解析 Model Context Protocol (MCP) 协议，比较 STDIO 和 SSE 两种传输方式，并探讨函数计算平台如何作为理想的 MCP Server 计算底座。
author: "西流"
image: "https://ai.programnotes.cn/img/ai/cea90706b53bfd8b2db5b7fb2c1c291f.png"
---
核心内容点1: MCP协议解析，包括STDIO和SSE两种传输方式的比较。
核心内容点2: 函数计算平台作为MCP Server的优势，解决分布式系统复杂性、资源限制和安全挑战。
核心内容点3:  MCP技术演进方向预测，包括协议架构升级、通用性扩展、新交互模式和生态系统扩展。

**源自** | 西流  Serverless   2025-04-27 18:02  
  
在人工智能技术高速发展的今天，数据孤岛、工具碎片化、上下文割裂问题已成为制约大模型发挥潜力的关键瓶颈。Model Context Protocol（MCP）作为 Anthropic 于 2024 年推出的开源协议，正引领着 AI 与数据交互的标准化进程。MCP 通过构建 Client-Server 架构，将大型语言模型（LLM）与分散的垂类数据源无缝连接，不仅解决了传统开发中"一事一议"的高成本难题，更通过 JSON-RPC 通信机制实现了跨平台互操作。其创新性体现在工具（Tools）、资源（Resources）、提示（Prompts）等五大核心原语的设计，使得 AI 应用既能安全访问本地数据库，又可灵活调用云端 API。
  
**作为 AI 领域的"USB-C 接口"，MCP 正重构智能系统与数字世界的连接方式，为下一代自主智能体的发展奠定技术基石。**  

然而 MCP Server 在真实部署中面临分布式系统复杂性、资源限制（如连接池/超时控制）及长连接身份验证等安全挑战。函数计算平台通过协议原生支持与架构级优化（如自动扩缩容、会话持久化机制），系统性化解技术痛点，成为承载 MCP Server 的理想计算底座。   
本系列将从技术原理到实战场景，深入解析函数计算如何攻克上述难题——本文作为开篇，将揭示 MCP 协议深度解析和云上最佳适配。  
  
![图片,MCP Timeline](https://ai.programnotes.cn/img/ai/3f106fa3b49058bdffcdf84db7dfc4af.png)  
  

## **什么是 MCP?**  
  
![图片](https://ai.programnotes.cn/img/ai/cea90706b53bfd8b2db5b7fb2c1c291f.png)  
  
MCP Clearly Explained [1]  
  
MCP 引入堪称 AI 协作的 USB-C 接口，其建立了通用的数据交互标准，数据提供者可以通过 MCP 服务器向 AI 系统提供结构化信息，而 AI 系统则可通过 MCP 客户端高效访问这些信息。  
  
- MCP Host（如 Claude Desktop、Cursor IDE、Cline）可视作一个 AI Agent，通过 LLM 实现意图解析与任务编排，协调 MCP Server 执行原子化子任务，同时维护全生命周期对话管理，是整个系统的启动入口。  
  
- MCP Server 提供特定功能（工具、数据访问、领域提示）的外部程序，连接到 Google Drive、Github、数据库和 Web 浏览器等各种数据源），就像工具箱中的工具，每个服务器都专注于特定任务，这种设计使得在不破坏整个系统的情况下，可以轻松地替换或升级单个组件，能让大模型能很好地理解工具的功能范围及使用方法。  
  
- MCP Client 是 MCP Host 引用的中间件，负责与 MCP Server 建立连接，处理STDIO/SSE 等  
通信协议、消息格式化和状态管理，确保人工智能模型与服务器之间进行可靠且安全的通信。  
  
MCP 协议已经成为大语言模型（LLM）生态系统中不可或缺的核心组件，其解决了流式响应、实时交互、工具调用等场景中的众多技术挑战：  
  
a.流式传输优先：采用增量传输而非整体响应  
  
**b. 协议一致性** ：保证不同模型实现间的互操作性  
  
**c. 低延迟高效率**：最小化传输开销和响应时间  
  
**d. 可扩展性**：支持未来新功能的无缝集成  

## **MCP 协议解析**  
  
  
01 生命周期  
  
![图片](https://ai.programnotes.cn/img/ai/66348da8788c0eeccccf977af0df6e06.png)  
  
MCP LifyCycle [2]  
  
02 传输方式  
  
MCP 使用 JSON-RPC 来编码消息。JSON-RPC 消息必须使用 UTF-8 编码，协议目前定义了两种用于客户端-服务器通信的标准传输机制：  
  
- STDIO，通过标准输入和标准输出进行通信  
  
2. SSE,HTTP 与服务器发送事件  

**STDIO**  
```
[客户端] → stdin请求 → [MCP服务器] → stdout响应 → [客户端]
```  
  
STDIO（标准输入输出）是 MCP 协议在本地或容器化环境中的主要实现方式。在技术层面，其工作原理如下：  
  
**- 进程间通信机制**  ：MCP 利用操作系统提供的标准 IO 流（文件描述符 0 [stdin]、1 [stdout]）在进程间传递数据  
  
**JSON 序列化** ：消息以 JSON 格式序列化，每行一个完整的 JSON 对象  
  
在本地计算环境或容器化部署场景中，基于 STDIO 的实现通常会被打包为独立的二进制可执行文件。不同技术栈的实现形态各具特色：  
- Node.js 生态通常通过 npx 提供，例如 "npx -y  @amap/amap-maps-mcp-server"  
  
- Python 生态则以 uvx 提供,  例如 "uvx mcp-server-time --local-timezone=Asia/Shanghai"  
  
这种交付方式不仅简化了部署流程，还显著降低了环境依赖和配置的复杂性，使得跨平台部署变得极其轻量和高效。STDIO 以 JSON 行（JSON Lines/JSONL）格式进行通信，一个典型的交互流程如下：  
```
{"type":"stdin","content":"{\"jsonrpc\":\"2.0\",\"id\":0,\"method\":\"initialize\",\"params\":{\"protocolVersion\":\"2024-11-05\",\"capabilities\":{\"sampling\":{},\"roots\":{\"listChanged\":true}},\"clientInfo\":{\"name\":\"mcp-inspector\",\"version\":\"0.7.0\"}}}","timestamp":"2025-03-31T01:55:13.505Z"}
{"type":"stdout","content":"npm run build-server","timestamp":"2025-03-31T01:55:13.530Z"}
{"type":"stdout","content":"> @modelcontextprotocol/server-filesystem@0.6.2 build-server\n> webpack --config webpack.config.js --env target=server","timestamp":"2025-03-31T01:55:13.707Z"}
{"type":"stdout","content":"asset index.js 286 KiB [compared for emit] (name: main) 1 related asset\norphan modules 288 KiB [orphan] 48 modules\n./server.ts + 47 modules 291 KiB [not cacheable] [built] [code generated]\nwebpack 5.98.0 compiled successfully in 618 ms","timestamp":"2025-03-31T01:55:15.007Z"}
{"type":"stdout","content":"node dist/server/index.js","timestamp":"2025-03-31T01:55:15.017Z"}
{"type":"stdout","content":"start server","timestamp":"2025-03-31T01:55:15.053Z"}
{"type":"stdout","content":"{\"result\":{\"protocolVersion\":\"2024-11-05\",\"capabilities\":{\"tools\":{},\"resources\":{}},\"serverInfo\":{\"name\":\"example-server\",\"version\":\"-0.0\"}},\"jsonrpc\":\"2.0\",\"id\":0}","timestamp":"2025-03-31T01:55:15.056Z"}
{"type":"stdin","content":"{\"jsonrpc\":\"2.0\",\"method\":\"notifications/initialized\"}","timestamp":"2025-03-31T01:55:15.064Z"}
{"type":"stdin","content":"{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/list\",\"params\":{}}","timestamp":"2025-03-31T01:55:2-855Z"}
{"type":"stdout","content":"{\"result\":{\"tools\":[{\"name\":\"add\",\"description\":\"calc ohyee's add a and b\",\"inputSchema\":{\"type\":\"object\",\"properties\":{\"a\":{\"type\":\"number\"},\"b\":{\"type\":\"number\"}},\"required\":[\"a\",\"b\"],\"additionalProperties\":false,\"$schema\":\"http://json-schema.org/draft-07/schema#\"}}]},\"jsonrpc\":\"2.0\",\"id\":1}","timestamp":"2025-03-31T01:55:2-858Z"}
{"type":"stdin","content":"{\"jsonrpc\":\"2.0\",\"id\":2,\"method\":\"tools/call\",\"params\":{\"_meta\":{\"progressToken\":0},\"name\":\"add\",\"arguments\":{\"a\":1,\"b\":2}}}","timestamp":"2025-03-31T01:55:24.869Z"}
{"type":"stdout","content":"get 1 + 2","timestamp":"2025-03-31T01:55:24.873Z"}
{"type":"stdout","content":"{\"result\":{\"content\":[{\"type\":\"text\",\"text\":\"4\"}]},\"jsonrpc\":\"2.0\",\"id\":2}","timestamp":"2025-03-31T01:55:24.873Z"}
{"type":"interrupt","content":"Process interrupted by user","timestamp":"2025-03-31T01:55:42.514Z"}
```  
  
**TIPS：**  
  
开发 STDIO MCP Server 期间,  将调试日志打印到文件描述符 2 [stderr] 是一个不错的实践。  
  
  
**SSE**  
```
                HTTP POST请求
              ↗---------------→
[客户端]                            [MCP服务器]
              ↖-----------------↙
                 SSE事件流推送
```  
  
SSE（Server-Sent Events）是 MCP 在网络环境中的主要实现技术，尤其适合云服务和远程 API 调用场景。其技术实现细节包括：  
  
**- HTTP 长连接** ：SSE 建立在 HTTP/-1 或 HTTP/2 协议之上，使用 Content-Type: text/event-stream头  
  
**2. 增量数据传输** ：服务器按照 SSE 格式推送事件数据，每个事件以 data:   
前缀标识  
  
**3. 事件解析**：客户端使用 EventSourceAPI 或兼容库自动解析事件流  
  
一个最简单的典型 MCP SSE 请求时序图如下：   
  
![图片](https://ai.programnotes.cn/img/ai/47a73e98fc5b44cd7e97dbf15aafc51d.png)  
  
MCP SSE 请求时序图  
  
- Client 发起一个 GET 请求，建立了一个 SSE 长连接  
 **[Connection1]**  
  
1. Server 回复 path 以及 sessionId**[Connection1]**  
  
2. Client 使用2 中 path 及 sessionId发起 initialize HTTP POST 请求 **[Connection2]**  
  
3. Client 发送包含协议版本和能力的 initialize请求  
  
4. Server 端快速响应 202，无 body **[Connection2]**  
  
5. Server 返回 3 请求的响应真正的 message**[Connection1]**  
  
**Server 以其协议版本和能力响应**  
  
6. Client 使用2 中 path 及 sessionId  发起 initialized HTTP POST 请求作为确认 **[Connection3]**  
  
7. Server 端快速响应 202，无body **[Connection3]**  
  
8. Client使用2 中 path 及 sessionId 发起 list tools HTTP POST 请求 **[Connection4]**  
  
9. Server 端快速响应 202，无body **[Connection4]**  
  
10. Server 返回 8 请求的响应真正的 message，即工具列表**[Connection1]**
1- Client使用 2 中 path 及 sessionId 发起 call tool HTTP POST 请求 **[Connection5]**  
  
12. Server 端快速响应 202，无body **[Connection5]**  
  
13. Server 返回 11 请求的响应真正的 message，即工具调用结果**[Connection1]**  
  
接下来，我们可以通过一个 hello_world MCP Server + curl 工具来完整演示整个流程：  
  
**Terminal 1:**  
```
$ curl -v http://start-mnodejs-g-qzhihvopgs.cn-hangzhou.fcapp.run/sse
```  
  
**Terminal 2:**  
```
# initialize
$ curl -X POST --header "Content-Type: application/json" --data '{ "jsonrpc": "2.0", "id": 0, "method": "initialize", "params": { "protocolVersion": "2024-11-05", "capabilities": { "roots": { "listChanged": true }, "sampling": {} }, "clientInfo": { "name": "ExampleClient", "version": "-0.0" } } }' "http://start-mnodejs-g-qzhihvopgs.cn-hangzhou.fcapp.run/messages?sessionId=c828f039-260a-416c-92bf-c05ad9a40599"

# initialized
$ curl -X POST --header "Content-Type: application/json" --data '{ "jsonrpc": "2.0", "method": "notifications/initialized" }' "http://start-mnodejs-g-qzhihvopgs.cn-hangzhou.fcapp.run/messages?sessionId=c828f039-260a-416c-92bf-c05ad9a40599"

# list tools
$ curl -X POST --header "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}' "http://start-mnodejs-g-qzhihvopgs.cn-hangzhou.fcapp.run/messages?sessionId=c828f039-260a-416c-92bf-c05ad9a40599"

# call tool
$ curl -X POST --header "Content-Type: application/json" --data '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"hello_world","arguments":{}}}' "http://start-mnodejs-g-qzhihvopgs.cn-hangzhou.fcapp.run/messages?sessionId=c828f039-260a-416c-92bf-c05ad9a40599"
```  
  
![图片](https://ai.programnotes.cn/img/ai/04873c393a48def35b1e5a1829ca57a0.png)  
  
从上面的时序图以及一个具体实践的流程看过来，我们可以明显看到 SSE 的优势和不足：  
  
**优势：**  
  
- 协议轻量化, 基于 HTTP 协议实现，无需复杂握手，兼容现有基础设施，开发成本低  
  
- 实时流式推送 ，支持服务器主动推送文本数据（如日志、进度更新），适合长任务交互  
  
- 资源效率高，单连接复用推送  
  
**不足：**  
  
- 单向通信限制， 仅支持服务端→客户端推送，需配合 HTTP 请求实现双向交互，这个就要求 SSE 长连接和后续配合该会话的 HTTP 请求必须在同一个 MCP Server 服务实例， 对于 MCP Server 实例需要横向扩展的场景提出了 Session 会话亲和的技术要求。  
  
- 协议演进趋势 ，  Streamable HTTP 提案 2025.3.17 通过，后者支持动态流式升级与无状态服务，更适应云原生架构  
  
**TIPS:**  
  
**重要的事情说三遍，重要的事情说三遍， 重要的事情说三遍**  
  
- MCP Client 端应该为所有请求实现适当的超时，以防止连接挂起和资源耗尽  
  
- MCP Client 端应该及时释放掉，应防止 MCP Client 端的泄露导致服务端 SSE 长连接数目一直增长消耗服务端资源  
  
- 服务端应该设计合理的 Server Timeout 自动清理连接时长明显有问题的 SSE 长连接  
  
**MCP Proxy**  
  
鉴于 SSE 协议的配套实现在 2025 年 4 月左右才正式推出， 结合 MCP 时间线，当前市场中存量 MCP Server 绝大部分采用 stdio 传输机制实现,  为了在不改动任何存量 MCP Server 代码的前提下，实现从 stdio 到 SSE 的无缝转换，我们需要提供一个 stdiotosse 的 proxy，通过这一代理层，为 MCP 生态描绘一条平滑、低成本的技术演进路径，确保了协议创新不会给开发者带来额外的迁移负担。  
  
MCP Stdio 传输方式和上古 Web 开发   
  
CGI[3](Common Gateway Interface) 程序特别类似，如下图，http client 发送请求到 http server，http server 将 method，header 等信息，body 通过 stdin 传给 CGI 程序，CGI 程序执行动态页面渲染，最后把渲染后的 HTML 页面通过 stdout 返回给 http server,  最后再返回给 client 端  
  
![图片](https://ai.programnotes.cn/img/ai/c48a5d0fdbcad7201de0b50644390a00.png)  
  
借助这个思路， 很快就能推导出下面的 proxy 方案：  
  
![图片](https://ai.programnotes.cn/img/ai/6c5b1561d502b55a82782885e23043f8.png)  
  
社区里面也有了相关的轮子，比如热门的supergateway  ,  只要输入如下命令即可实现一个存量的 stdio server 即可转换成 SSE Server  
```
supergateway \
    --stdio "npx -y @modelcontextprotocol/server-filesystem ./my-folder" \
    --port 8000 --baseUrl http://localhost:8000 \
    --ssePath /sse --messagePath /message
```  
- Subscribe to events: GET http://localhost:8000/sse  
  
- Send messages: POST http://localhost:8000/message  
  
但是这会带来另外一个问题， 承载 SSE 协议的是一个 http server,  天然就需要去支撑一定的并发能力，单个 mcp server stdio process 没有并行处理能力，支持不了一定的并发处理。为此，我们借鉴 CGI 的思想继续推导：PHP 在 Web 领域的实践，使用的是 fastcgi 进程池，如下图中的 FastCGI 进程管理器：  
  
![图片](https://ai.programnotes.cn/img/ai/d28a7d11ddc0aeadb8ffd32852fa6def.png)  
  
发送到服务器的 Web 请求将被分配给进程池中的 CGI 进程。该 CGI 进程将处理该单个请求。如果同时收到多个请求，则将启动多个 CGI 进程并行处理它们。然而，每个进程一次只能处理一个请求。服务器能够通过对 CGI 进程进行上下文切换来处理并发请求。操作系统调度程序将跟踪所有 CGI 进程，并在需要时切换正在 CPU 上运行的 CGI 进程，以使每个 CGI 进程在需要时都能获得属于自己的、公平的 CPU 时间份额。  
  
因此， 将 stdiotosse 的 proxy 设计成如下方案是一个很不错的抉择，通过一个 MCP Server Stdio Process Pool 来提高并行处理能力，从而让前面支持 sse 协议的 http server 有更好的并行并发处理能力。  
  
![图片](https://ai.programnotes.cn/img/ai/d80d9a514ca1cb5b8aae26855c53a4e5.png)  
  
目前我们在supergateway[4] 的基础上， 增加了动态 MCP Server Stdio 进程池的实现，这个进程池的默认初始化值为 1， 最大进程数目为 10，这个两个值可以通过两个环境变量 MCP_STDIO_PROCESS_PRE_FORK 和 MCP_STDIO_PROCESS_MAX 来设置。MCP Server Stdio 进程池管理流程如下图：  
  
![图片](https://ai.programnotes.cn/img/ai/423d627cc16ead159e96e316be7fd03e.png)  
  
实现的 diff：  
  
https://github.com/aliyun-fc/supergateway/compare/04ff7d6fc12908a86efc60d0be59b42588b30018..d8bbf3b9e3677cd089f3118d7f34e7c50f4bcdec  
  
**TIPS:**  
  
- 如果 MCP Server Stdio Process 是 IO 密集型， MCP_STDIO_PROCESS_PRE_FORK 和 MCP_STDIO_PROCESS_MAX 数目可以适当调大一些来支持更高的并发处理能力  
  
- 如果 MCP Server Stdio Process 是 CPU 密集型， MCP_STDIO_PROCESS_PRE_FORK 和 MCP_STDIO_PROCESS_MAX 数目可以适当调小一些，同时实例 CPU 和内存规格也要按需调大一些  
  
**并发压测：**  
  
Stdio Server 逻辑如 index.ts 所示，latency 为 0.15s ~ 1s 随机， 实例规格为 1C2G  
  
![图片](https://ai.programnotes.cn/img/ai/1a2f53ee4c4a21143ad8a3a7a070ba0b.png)  
  
压测客户端代码(100 个并发 client， 每次 client 串行执行 3 次, 执行正常  )：  
```
import asyncio
from mcp.client.sse import sse_client
from mcp import ClientSession
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LoadTestClient")

# 控制最大并发数
CONCURRENCY_LIMIT = asyncio.Semaphore(100)  # 根据服务器能力调整

async def robust_client_instance(instance_id: int):
    async with CONCURRENCY_LIMIT:
        try:
            async with sse_client(
                "https://mcp-server-gi-mmqoiftdwm.cn-hangzhou.fcapp.run/sse",
                headers={
                    "Authorization": "Bearer YOUR_API_KEY",
                    "X-Instance-ID": str(instance_id),
                },
            ) as streams:

                if streams is None:
                    raise ConnectionError("SSE连接失败")

                async with ClientSession(
                    read_stream=streams[0],
                    write_stream=streams[1],
                ) as session:
                    start = time.time()
                    await session.initialize()
                    logger.info(
                        f"实例{instance_id}; initialize 耗时: {time.time() - start}"
                    )
                    start = time.time()
                    r = await asyncio.wait_for(session.list_tools(), timeout=10.0)
                    logger.info(
                        f"实例{instance_id};list_tools 工具数: {len(r.tools)}; 耗时: {time.time() - start}"
                    )

                    # 执行操作
                    for i in range(3):
                        try:
                            # 设置call_tool超时
                            start = time.time()
                            result = await asyncio.wait_for(
                                session.call_tool(
                                    "add", {"a": instance_id, "b": 1 + i}
                                ),
                                timeout=10.0,
                            )
                            logger.info(
                                f"实例{instance_id}; 第 {i} 次迭代; call_tool 耗时: {time.time() - start}"
                            )

                            if result.isError:
                                logger.error(
                                    f"实例{instance_id} 第 {i} 次迭代, call_tool 调用失败: {result.content}"
                                )
                                raise Exception(
                                    f"实例{instance_id} 第 {i} 次迭代, call_tool 调用失败: {result.content}"
                                )
                            else:
                                logger.info(
                                    f"实例{instance_id} 第 {i} 次迭代, call_tool 调用成功: {result.content}"
                                )
                                assert (
                                    int(result.content[0].text) == instance_id + 1 + i
                                )

                        except asyncio.TimeoutError:
                            logger.error(f"实例{instance_id} 第 {i} 次迭代操作超时")
                            continue  # 跳过当前迭代继续执行

        except Exception as e:
            logger.error(f"实例{instance_id} 最终失败: {str(e)}")


async def main():
    tasks = [robust_client_instance(i) for i in range(100)]
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
```  
  
**为什么选择函数计算**  
  
作为 MCP Server 托管运行时真实世界中部署 MCP Server 面临的技术挑战包括[5]： 
  
- **分布式系统复杂性**  ：需要在多节点环境中维护连接状态  
  
- **2. 资源限制处理**  ：
  
- 连接池管理：有效分配和复用连接资源    
- 超时控制：处理未响应或长时间计算情况  
- 负载均衡：在多实例间均衡分配请求  
  
- **3. 安全隐患**  ：  
- 针对长连接的 DDoS 攻击防护  
- 身份验证与会话维护：在长时间连接中保持认证状态  
  
- **4. 故障恢复机制**  ：服务中断时的会话恢复和状态保持  
  
- 5. 高资源利用率与低成本  ：绝大多数 MCP Server 的业务流量呈现典型的稀疏性（Sparse Access）与突发性（Burstiness）特征——请求分布高度离散且流量峰谷波动显著。传统固定实例池（Instance Pool）的常驻模式导致资源闲置率过高。
  
阿里云函数计算作为阿里云 Serverless 计算平台， 有极致的按需自动弹性扩缩容速度和能力、零服务器管理免运维、多 AZ 容灾的高可用以及毫秒级按需计费能力。 在此基础上， 我们针对 MCP Server 远程服务能力做了如下增强：  
  
- 推出支持 SSE 协议且具备并发能力的 MCP Runtime（内置我们上文阐述的 MCP Proxy），存量 STDIO 模式的 MCP Server 无需任何改动即可变为符合 SSE 协议的远端服务  
  
- 在满足 MCP 场景 SSE 协议亲和调度的基础上（见 SSE 协议不足 1），让业务在面对 burst 流量 ，依然有快速弹性扩容能力。后续我们会专门出一篇文章来介绍 "MCP Server SSE 请求亲和性的技术与实战"  
  
- MCP Server SSE 作为远程服务需要鉴权访问等安全能力：  
- 函数 HTTP 触发器及自定义域名提供多种鉴权方式，针对 AI 场景新提供了基于 Opaque Bearer Authorization 访问鉴权能力，与现有 AI 服务身份认证体系无缝对接  
  
- 函数计算支持针对具体函数设置执行角色，运行时提供动态获取临时 Token，实现完全的无 AK 方案，这对接入阿里云体系内产品的 MCP Server 是一个非常安全合规的企业级姿势。  
  
- 每个函数运行环境都是一个安全容器， 平台侧负责函数实例沙箱容器的漏洞修复及安全升级， 某个实例的 OOM 等异常不会扩散。  
  
- 函数计算函数最大执行时长为 24 小时，基本可以满足绝大部分的长连接请求， 同时设置合理的 timeout，可以解决因为客户端 client 泄露导致的长连接一直消耗服务端资源的问题。  
  
以上可以看出， 函数计算 Serverless 平台解决了绝大部分列出的真实世界中部署 MCP Server 面临的技术挑战；对于由于 SSE 协议本身带来的  
不支持断线重连/恢复会话，我们也持续跟进社区   
Streamable HTTP**[6]**  
 协议进展，让 Streamable HTTP 更顺利在  
函数计算 Serverless 平台落地。  
  
**上手案例：**  
- 直接登录 Function AI**[7]**  平台体验 Mcp Server 一键部署  
  
- 参考 https://github.com/devsapp/mcp-servers  

查看各种 MCP Server on FC 的代码示例  
  
**合作方：**  
- 阿里云百练 MCP 广场 https://bailian.console.aliyun.com/?tab=mcp#/mcp-market  
  
- 魔搭社区 MCP 广场 https://www.modelscope.cn/mcp  
  
- 宜搭: 钉钉客户端创建 ai 助理的技能正在灰度中  
  
**总结**  
  
**MCP 的演进本质是加速 AI 基础设施的普及：**  
- **技术层**  ：通过协议标准化降低开发门槛，使中小开发者能快速构建复杂 AI 应用。  
  
- **商业层**  ：催生“MCP 工具商店”等新商业模式，工具开发者可通过协议分成获利。   
  
- **社会层**  ：推动 AI 从“专家系统”转向“普惠技术”，例如农民通过自然语言指令操作智能农业设备。  
  
随着 Anthropic、OpenAI 等巨头加速协议迭代，MCP 或将成为 AI 时代的" USB-C接口"  ——**既奠定技术底座，又重构产业规则**  
。  
开发者需密切关注协议演进，提前布局工具链生态，把握先机。  
  
**MCP 技术演进的核心方向预测：**  
- 协议架构升级：从 SSE 到 Streamable HTTP 的跨越  
  
- 通用性扩展， 多模态统一接口， 扩展同一协议支持文本、图像、音频和视频  
  
- 新交互模式， 分布式协作， 多个模型协同工作的协议扩展  
  
- 生态系统扩展与标准化博弈，会有一个类似 npm 这样的 MCP Server Registry 出现  
  
函数计算 Serverless 平台致力解决生产环境部署 MCP Server 面临的技术挑战，革新 MCP Server 的部署范式，给 MCP 社区蓬勃发展和 MCP Server 大规模落地、行业加速创新提供坚实的技术基础,    
让全球开发者无障碍构建下一代 AI 服务,  重构行业创新速度，普惠 AI 黄金时代！  
  
## 相关链接： 
  
[1] 图解「模型上下文协议（MCP）」：从与传统 API 的比较入手  
  
https://www.51cto.com/article/81154-html  
  
  
[2] MCP Specification  
  
https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle  
  
  
[3] CGI  
  
https://baike.baidu.com/item/CGI/607810  
  
  
[4] supergateway  
  
https://github.com/supercorp-ai/supergateway  
  
  
  
[5] AI 中的 MCP 技术解析：stdio 与 SSE 实现  
  
https://wicos.me/jishu/1160/  
  
  
[6]   
Streamable HTTP  
  
https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206  
  
  
[7] Function AI  
  
https://cap.console.aliyun.com/explore?lang=MCP+Server  
  
  
