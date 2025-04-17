---
title: "FunctionAI MCP 开发平台：助力AI应用连接数字生态"
date: "2025-04-14"
tags: ["MCP", "FunctionAI", "Serverless", "AI", "云原生", "函数计算", "模型上下文协议", "ServerlessDevs"]
categories: ["云计算", "人工智能"]
description: "FunctionAI基于阿里云函数计算构建，提供完整的MCP开发能力，解决本地化瓶颈、弹性困境和开发断层等问题，助力AI应用快速连接数字生态。"
author: "封崇"
image: ""
---
**源自** | 封崇  阿里云云原生   2025-04-14 18:02  
  
![](https://ai.programnotes.cn/img/ai/087ee75c2a26ff67233996986126ecfa.gif)  
  
  
MCP：AI 时代的“操作系统接口”,Cloud Native:

2024 年 11 月，Anthropic 发布模型上下文协议（MCP），这一开放标准迅速引发开发者社区的"协议觉醒"。其本质是通过标准化接口实现 LLM 与外部世界的双向交互，正如 USB 协议统一外设接入，MCP 正成为 AI 应用连接数字生态的通用总线。随着 Cursor、Claude   
Desktop   
等开发工具相继集成，特别是 OpenAI 宣布全面兼容 MCP 协议，标志着 MCP 从技术实验迈入产业级标准，这一标准化接口正重塑 AI 与数字世界的交互范式。  
  
截至 2025 年 4 月，MCP.so【1】上已经已有超过 8000 个注册的 MCP Server，涵盖数据处理、文件系统、API 网关、聊天机器人、数据库等服务类别，这一数量还在迅速增长。  

**生态暴发期的痛点**  
    
尽管 MCP 生态呈现指数级增长，GitHub 仓库星标数半年突破 3.5 万，但生产级落地仍面临三重挑战：  
  
  
**1. 本地化瓶颈**  
：当前绝大多数 MCP server 都采用传统 STDIO 模式，该模式没有鉴权能力（缺乏 OAuth 2.1 标准的双向认证机制、无法实现基于角色的访问控制），在复杂业务场景下暴露出调试困难、网络隔离性差等缺陷，难以实现访问内网环境的数据安全管控，内网穿透导致攻击面扩大；  
  
  
**2. 弹性困境**  
：MCP 工具调用流量呈现显著的非稳态特征以及"脉冲式"波动，比如智能客服系统的峰谷效应非常明显，传统虚拟机部署造成大量资源浪费；  
  
  
**3. 开发断层**  
：从本地调试到云端部署需要重构鉴权、变量管理、日志、中间件等基础组件，改造成本高，开发者大量的精力消耗在非业务代码的开发上；  
  
  
**Serverless 是 MCP 托管的最佳解决方案**  
  
  
我们观察到大部分的 MCP server 有以下特点：  
  
  
1. 稀疏调用，而且对算力的需求都比较小，0.5c/1G 的规格基本能够应对大部分场景；  
  
  
2. 代码体积比较小（<100MB），Node.js、Python 解释型语言是 MCP 的一等公民，大部分 MCP server 直接通过 npx、uv 就能一键运行；  
  
  
3. MCP server 的迭代非常快，新增、修改或弃用 MCP server 的场景会非常高频，对 MCP server 元数据管理的需求非常普遍；  
  
  
**因此灵活部署、弹性扩展的运行时对于 MCP server 的托管非常契合，这恰恰是 Serverless 的最大优势。**  
以阿里云函数计算为例：  
  
  
1. 天然的事件驱动模型，提供毫秒级弹性能力、按量付费、安全沙箱的运行时环境，完美解决了云上托管对于性能、成本、安全的需求；  
  
  
2. 官方对于 Node.js、Python 运行时的支持完善，内置代码包加速能力以及层的扩展，大幅降低代码启动时间；  
  
  
3. 控制台、SDK、ServerlessDevs 工具提供丰富的函数元数据的管理能力；  
  
  
这些能力让 Serverless 正成为托管 MCP 的最优解。作为 MCP   
的最佳运行时，函数计算已经支持阿里云百炼 MCP 服务【2】。  
  
[](https://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247573406&idx=1&sn=a9e215ecbf675b6058bf5f726063a316&scene=21#wechat_redirect)  
  
Function AI 是基于函数计算构建的 Serverless AI 应用开发平台，基于函数计算的运行时能力上线了完整的 MCP 开发能力，成为真正意义上的 MCP 开发平台。您可以进入FunctionAI 控制台【3】，快速体验 MCP 服务的能力。
  
**方式一：通过模板一键部署**  
  
### 1. 选择 MCP 模板  
进入FunctionAI 控制台【4】，选择探索->筛选应用模板（MCP Server），选择一个 MCP 模板进行部署  
![](https://ai.programnotes.cn/img/ai/8eaac6393e6591a3066bc7b143fd0a95.png)  
 
### 2. 填写模板配置，部署项目  

  
![](https://ai.programnotes.cn/img/ai/a7fa62b44c44e08f70f71b3fc4504de4.png)  

### 3. 查看部署进度  

![](https://ai.programnotes.cn/img/ai/cc0d4f2dd8f2833d543882bc611b63de.png)  
  
  
**方式二：创建自定义 MCP 服务**  
  
### 1. 创建空白项目  

  
![](https://ai.programnotes.cn/img/ai/bb40530090e7acd185b2eb51ae8639e9.png)  

### 2. 创建 MCP 服务  

  
![](https://ai.programnotes.cn/img/ai/62ee312927e0fcb139bb81cf658c8270.png)  
 
### 3. 编辑 MCP 服务配置，完成后点击预览&部署  

  
![](https://ai.programnotes.cn/img/ai/1cc1b3db23afe5b9bdf7e12e76a8528c.png)  

### 4. 查看部署进度，等待部署完成  

  
![](https://ai.programnotes.cn/img/ai/0edb2bfd8a9cd1e90b3f95833401ee14.png)  
  
  
**方式三：使用 ServerlessDevs 工具本地部署**  

FunctionAI 正式发布了 ServerlessDevs【5】工具的 MCP 组件，实现本地部署 MCP 工程到 FunctionAI 的能力  
  
### 1. 安装 ServerlessDevs 工具：  

```
npm install @serverless-devs/s -g
```  

### 2. 初始化 MCP 项目  

```
s init start-fcai-mcp-nodejs
```  

### 3. 查看 s.yaml  

```
edition: 3.0.0
name: start-mcp-server-nodejs
access: 'default'
vars:
  region: 'cn-hangzhou'
resources:
  nodejs-stdio-hello-world:
    component: fcai-mcp-server
    props:
      region: ${vars.region}
      description: mcp server deployed by devs
      transport: stdio # stidio | sse
      runtime: nodejs20
      cpu: 1
      memorySize: 1024
      rootDir: ./code
      source:
        oss: auto
      build:
        default: #默认构建器
          # 构建环境
          languages:
            - nodejs20
          # 执行步骤
          steps:
            - run: npm install
            - run: npm run build
      startCommand: "node ./dist/index.js" # 启动命令
      instanceQuota: 1 # 实例数配额
```  
  
### 4. 执行部署  

```
s deploy
```  
###   
  
![](https://ai.programnotes.cn/img/ai/65cbedb605963231d21a24f01a6411a0.png)  
  
  
登录到控制台，可以查看云端的部署详情  
  
  
![](https://ai.programnotes.cn/img/ai/9008afa9b766f18ec8870be548f7eca5.png)  
  
FunctionAI 支持托管 STDIO/SSE 协议的 MCP server。如果 MCP server 代码采用 STDIO，FunctionAI 会启动一个 SSE 服务来代理 STDIO 的请求，客户端访问需要使用 SSE 方式。  
    
当 MCP 服务部署完成后，平台会生成一个 SSE 的连接地址，并且会生成 MCP server 的 schema 用于测试。  
  
用户可以直接在控制台上测试连接、测试工具，也可以使用官方的 Inspector 在本地进行测试。  
  
**方式 1：FunctionAI 控制台测试**  

![](https://ai.programnotes.cn/img/ai/1b500d2ecbe51c3bd818ab0a2d241d31.png)  
  
查看日志和监控  
  
![](https://ai.programnotes.cn/img/ai/64428131f50c544e1eb810049aa74148.png)  
  
  
![](https://ai.programnotes.cn/img/ai/625f7be471aa00cb5795a70448e9bdb4.png)  
  
  
**方式 2：Inspector 本地测试**  
  
复制 FunctionAI 生成的公网访问地址  
  
![](https://ai.programnotes.cn/img/ai/827d8ce0c33c9ca0e0377d7e76adedd4.png)  
  
  
本地启动 inspector，输入访问地址进行调试  
  
```
npx @modelcontextprotocol/inspector
```  
  
  
![](https://ai.programnotes.cn/img/ai/2fb2f7c95d741f82ad78f0ce8c95fdf5.png)  
  
  
高阶能力  
  
Cloud Native  
  
  
**鉴权**  
  
  
MCP 的鉴权只适用于 SSE 的协议，而且必须遵循 OAuth2.1 协议标准，对于大量的 STDIO 的 MCP 服务托管的改造难度非常之高，企业落地 MCP 鉴权是一个非常痛点的问题。  
  
  
FunctionAI 提供了网关侧的 Bearer 鉴权能力，用户只需要开启鉴权功能，使用平台生成的 Bearer Token，就可以让 MCP 服务自带鉴权能力。  
  
### 使用方式  
###   
  
编辑服务配置，点击开启鉴权，保存并且部署。开启后，平台会对服务生成一个只读的 Bearer Token。  
  
  
![](https://ai.programnotes.cn/img/ai/176da26d1e64590fb48d8e7e9324fcc8.png)  
  
  
![](https://ai.programnotes.cn/img/ai/9023eafd8409b7fe75ef35e317d59183.png)  
###   
### 测试鉴权生效  
  
  
使用平台生成的 Bearer Token，可以正常访问 MCP 服务  
  
  
![](https://ai.programnotes.cn/img/ai/7d5c7f3aa4dc7d4fdeab04d14dbf5154.png)  
  
  
使用错误的 token 时，访问失败  
  
  
![](https://ai.programnotes.cn/img/ai/f7d5043ba19bec75038798cf94fc5e8a.png)  
  
  
使用本地的 Inspector，输入服务的 token，访问正常。  
  
  
![](https://ai.programnotes.cn/img/ai/6807b4d0e56bbfc668a8d870fba77f27.png)  
  
  
**变量管理**  
  
  
很多的 MCP Server 代码都需要访问第三方服务，比如高德地图、Github 等，需要持有用户的访问秘钥，比如 API-Key、AccessToken，这些秘钥通常以环境变量加载或者启动命令参数注入。  
  
  
FunctionAI 提供了变量管理能力，并且支持敏感变量托管，可以实现 MCP 服务访问秘钥的安全可靠管理。  
  
### 配置方式：设置服务变量  
###   
  
选择服务->服务变量，添加服务变量的 Key 和 Value  
  
  
![](https://ai.programnotes.cn/img/ai/15b09c554b6a7fbbc9bdd1ba2f2e310e.png)  
###   
### 加载方式 1：环境变量  
###   
  
FunctionAI 上配置的服务变量会默认注入到函数启动的环境变量中，MCP 服务代码可以直接通过系统环境变量读取  
  
  
![](https://ai.programnotes.cn/img/ai/43ad2532377ad53c8c93e3cf34ccd342.png)  
###   
### 加载方式 2：启动参数  
###   
  
FunctionAI 的服务变量支持通过 ${self.KEY_NAME} 的方式引用，可以在启动命令中修改命令行参数，使用变量的引用，在启动阶段注入变量的值。  
  
  
![](https://ai.programnotes.cn/img/ai/11f9f30a1e47a380071e5affa1db4312.png)  
  
![](https://ai.programnotes.cn/img/ai/f074718d0e6abbc83b8cf03b356d8c67.png)  
  
  
**绑定代码仓库进行持续部署**  
  
  
FunctionAI 的 MCP 服务面向开发态能力，提供以代码仓库托管 MCP 服务的能力。  
  
使用方式：  
  
  
1. 编辑 MCP 服务配置，选择代码仓库，目前支持了 Github、Gitee、Codeup、GitLab、OSS 代码仓库。  
  
  
2. 选择仓库分支、MCP 工程在代码仓库中的根目录  
  
  
3. 选择构建环境：对于多语言的工程，可以选择多个构建环境  
  
  
4. 编辑构建命令：例如 npm build、pip install -r requirements.txt  
  
  
5. 可选：开启构建缓存，缓存目录根据不同语言可以设置~/.npm（Node.js）、~/.cache（Python）、~/.m2、（Java）  
  
  
![](https://ai.programnotes.cn/img/ai/e22ee2e9b7cbfb185a2ba94c6cd73174.png)  
  
  
绑定 Git 仓库后，如果指定的分支有 push 操作，会自动触发服务的持续部署  
  
  
![](https://ai.programnotes.cn/img/ai/0a0391910a8ba2fd0f98201c8ea7c8de.png)  
  
  
**极速模式**  
  
  
对于延迟敏感性的业务，FunctionAI 提供了极速模式，可以提前预留指定数量的实例快照，降低频繁冷启动带来的开销，并且只有在有活跃请求时才会产生 vCPU 费用，可以实现性能和成本的平衡。  
  
  
另外由于 MCP SSE 请求的 session 机制，同一个 session id 访问到不同实例会导致上下文丢失，因此建议开启预置快照为 1 并且实例限额为 1，这样可以让 SSE 请求打到不同弹性实例的概率更小。  
  
FunctionAI 后面会上线会话亲和性能力，尽情期待。  
  
  
![](https://ai.programnotes.cn/img/ai/66ea83970635dde4a3af53a4472379ab.png)  
  
  
开启后，可以在函数监控页面看到预留实例的个数  
  
  
![](https://ai.programnotes.cn/img/ai/d5dacedc72983e325007e050a13c84c5.png)  
  
FunctionAI 现在已经支持了完整的 MCP 开发能力，包括：  
  
- 部署形式上，支持模板直接部署、自定义 MCP 服务、ServerlessDevs 工具本地部署  
  
- 托管能力上，支持 STDIO/SSE 的自动托管，无需业务改造既能生成可用于访问的 SSE 地址  
  
- 调试能力上，支持控制台直接调试以及 Inspector 本地调试  
  
- 二次开发能力上，支持变量管理、鉴权、绑定代码仓库进行持续部署  
  
- 可观测能力上，支持函数监控、实例监控以及日志  
  
- 弹性调度上，支持标准模式以及极速模式  
  
MCP 的价值是统一了 Agent 和 LLM 之间的标准化接口，有了 MCP Server 的托管以及开发态能力只是第一步，接下来重要的是做好 MCP 和 Agent 的集成，FunctionAI 即将上线 Agent 开发能力，敬请期待。  
  
  
【1】MCP.so https://mcp.so/  
【2】Serverless MCP 运行时业界首发，函数计算让 AI 应用最后一公里提速  
【3】FunctionAI 控制台 https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fcap.console.aliyun.com%2Fexplore&clearRedirectCookie=1&lang=zh  
【4】FunctionAI 控制台 https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fcap.console.aliyun.com%2Fexplore&clearRedirectCookie=1&lang=zh  
【5】ServerlessDevs  https://www.serverless-devs.com/  
