---
title: "阿里云 MCP Server 开箱即用！"
date: "2025-04-23"
tags: ["阿里云", "MCP", "AI助手", "运维", "ECS", "RDS", "OOS", "Cline", "VS Code"]
categories: ["云计算", "人工智能"]
description: "本文介绍如何使用alibaba-cloud-ops-mcp-server和MCP实现AI助手对阿里云资源的复杂任务操作，涵盖ECS实例管理、VPC查询、云监控数据获取等运维任务。"
author: "赵帅博(川林)"
image: "https://ai.programnotes.cn/img/ai/921173eb687158463316045c885cd26a.png"
---
**源自** | 阿里云开发者 赵帅博(川林)  2025-04-23 18:00  
  
![](https://ai.programnotes.cn/img/ai/ea121adfa4f0669e87e8b52c40edbbde.jpeg)  

本文介绍了如何通过alibaba-cloud-ops-mcp-server和MCP（Model Context Protocol）实现AI助手对阿里云资源的复杂任务操作。内容涵盖背景、准备步骤（如使用VS Code与Cline配置MCP Server）、示例场景（包括创建实例、监控实例、运行命令、启停实例等），以及支持的工具列表和参考文档。借助这些工具，用户可通过自然语言与AI助手交互，完成ECS实例管理、VPC查询、云监控数据获取等运维任务，实现高效“掌上运维”。  
  
## 背景  
  
![image.png](https://ai.programnotes.cn/img/ai/921173eb687158463316045c885cd26a.png)  
  
随着人工智能技术的快速发展，AI助手逐渐从简单的对话服务向复杂任务执行方向演进。为了使AI助手具备更强的操作能力，MCP（Model Context Protocol）[1] 应运而生。MCP通过将大模型与工具调用能力结合，让AI助手能够规划并完成复杂的现实任务。  
  
  
alibaba-cloud-ops-mcp-server[2]是一款专门为阿里云资源管理设计的MCP Server，它通过集成阿里云Open API和系统运维管理（OOS）[3]的能力，为AI助手提供了一系列强大的工具支持。这些工具涵盖了阿里云资源的生命周期管理（如创建、启动、停止、重启等），包括云监控数据获取以及运行命令、更换系统镜像等功能，目前已覆盖ECS实例、RDS实例以及OSS Bucket等资源。借助alibaba-cloud-ops-mcp-server，用户可以通过自然语言与AI助手交互，快速完成复杂的运维任务。  
  
在alibaba-cloud-ops-mcp-server提供的工具中，一部分功能是通过阿里云 Open API 实现的，而像运行命令、启停实例等复杂操作，则依托于系统运维管理（OOS）[3]。OOS 不仅能够为云产品提供强大的运维操作能力，还支持复杂的任务编排，尤其在处理异步场景时表现出色。例如，在启动或停止实例的过程中，OOS 会实时检查实例状态，确保 AI 助手调用完成后，ECS 实例的状态与预期一致（如 Running 或 Stopped）。此外，OOS 还内置了多种高频运维场景的公共模板，这些模板并非简单的单步 API 调用，而是经过优化的复杂操作流程，能够显著减少多轮交互的需求，提高任务执行的准确率，同时节省模型的 token 消耗，让整个过程更加高效和可靠。  
  
## 准备步骤  
    
**使用 VS Code [4]+ Cline [5]配置MCP Server**  
  
Cline是一款强大的Vscode插件，开源且完全免费，支持打开文件/文件夹、运行任务、调试代码、管理窗口等操作，能够借助大模型的能力调用工具，规划并完成真实的复杂任务  
  
**配置流程**  
  
1. 安装 UV[6]  
  
2. 在VS Code 插件市场下载并打开Cline插件，在设置中配置大模型 API KEY  
   
![image.png](https://ai.programnotes.cn/img/ai/8edb6073f4fbcd393026df56dc4ac497.png)  
  
这里以配置阿里云百炼API Key为例：  
  
a. API Provider：选择Open AI Compatible  
  
b. Base URL：https://dashscope.aliyuncs.com/compatible-mode/v1（阿里云百炼兼容接口）  
  
c. API Key：前往 API-KEY[7] 页面获取  
  
d. Model ID：模型ID总览[8]
  
1）推荐使用上下文较长的模型，如：qwen-max-latest等支持128k上下文的模型，否则可能会因为上下文长度限制导致AI助手无法交互  
  
             
![image.png](https://ai.programnotes.cn/img/ai/1cac90ad2094f06c9b6a387440a56ed8.png)  
  
  
3. 配置MCP Servers  
  
a. 选择右上方的工具栏中的MCP Servers  
   
![image.png](https://ai.programnotes.cn/img/ai/e058a9ca595db57fb31fb70151c09d27.png)  
  
  
b. 进入MCP Server界面，点击**Configure**  
配置JSON文件，关闭json文件即可保存并完成配置。  
  
![image.png](https://ai.programnotes.cn/img/ai/7b81c4d30aa11509fd29e37a5da48697.png)  
  
```json
{
  "mcpServers": {
    "alibaba-cloud-ops-mcp-server": {
      "timeout": 600,
      "command": "uvx",
      "args": [
        "alibaba-cloud-ops-mcp-server@latest"
      ],
      "env": {
        "ALIBABA_CLOUD_ACCESS_KEY_ID": "Your Access Key ID",
        "ALIBABA_CLOUD_ACCESS_KEY_SECRET": "Your Access Key SECRET"
      }
    }
  }
}
```  
  
  
c. 配置完毕后，在Installed  
界面能够检查对应MCP Server的状态，提供的Tools数量以及详细信息。  
  
![image.png](https://ai.programnotes.cn/img/ai/e3e81f0851af883a4674e207e2171eca.png)  
  
4. 右下角配置AI助手的对话模式，为了AI助手能够实际调用工具，推荐您使用Act模式。配置完毕后您就可以在对话框开启您的对话。  
  
![image.png](https://ai.programnotes.cn/img/ai/893404a2f4e439d1cc9542c12f06ca65.png)  
  
示例场景  
  
alibaba-cloud-ops-mcp-server能够为您的AI助手提供工具，操作阿里云资源并完成日常运维操作等多种需求，以针对ECS和RDS实例的生命周期进行管理和监控为例，我们将为您展示AI助手会如何使用alibaba-cloud-ops-mcp-server  
的工具。  
  
**创建ECS实例**  
  
向AI助手发起提问后，AI助手会自动开始规划需要使用的工具并向您请求使用许可。  
  
![image.png](https://ai.programnotes.cn/img/ai/ae6b7b95c2170d4aea0d94895d02c710.png)  
  
经过不断的交互，AI助手会逐渐取得所有创建ECS实例所必需的参数。  
  
![image.png](https://ai.programnotes.cn/img/ai/2bcabcf7daac6a720f99eed945bc7407.png)  
  
![image.png](https://ai.programnotes.cn/img/ai/8ca98e440f4497f3fbc92f5fdafd29ab.png)  
  
在收集到所需信息后，AI助手会发起创建ECS实例的请求。  
  
![image.png](https://ai.programnotes.cn/img/ai/4356f70d5b1550c89c8336a88bd3f31c.png)  
  
最终AI助手成功创建了名为**alibabacloud-mcp**  
的ECS实例。  
  
![image.png](https://ai.programnotes.cn/img/ai/e59184b1a2f5f655db616d73a862d203.png)  
  
在ECS控制台验证，AI助手成功创建了ECS实例。  
  
![image.png](https://ai.programnotes.cn/img/ai/e092f9983367c7d6f2e6ff4ccf05776a.png)  
  
**监控ECS实例**  
  
当创建了ECS实例之后，我们往往希望对实例进行监控，传统的运维方式往往需要登录到ECS控制台或者云监控控制台进行查看。现在，我们可以借助alibaba-cloud-ops-mcp-server  
轻松实现掌上运维，只需和AI助手进行自然语言交互即可轻松获取ECS实例的实时状态。  
  
![image.png](https://ai.programnotes.cn/img/ai/d5a1c420c7f35dc9791f2b6960a9c074.png)  
  
在获取对应数据后，AI助手将会进行分析并为您展示ECS实例的详细监控数据。  
  
![image.png](https://ai.programnotes.cn/img/ai/c52fe54e6534be583e244e1141db9fac.png)  
  
**在ECS实例上运行命令**  
  
在实际的开发过程中，为实现运行命令，首先我们需要编写命令脚本，并通过远程登录或者ECS控制台登陆到ECS实例上，再运行对应的命令脚本。现在，借助alibaba-cloud-ops-mcp-server  
，您只需通过自然语言，即可轻松实现运行命令的复杂操作。AI助手将会分析您的指令，得出合适的命令脚本，并借助工具帮助您在ECS实例上执行指定的命令，等待命令运行结束后向您报告命令的运行结果，从而实现 分析指令-运行命令-报告结果 整条链路的打通。以在ECS实例上部署NGINX为例：  
  
![image.png](https://ai.programnotes.cn/img/ai/89c21672f4677a6de4c6875d081c0849.png)  
  
![image.png](https://ai.programnotes.cn/img/ai/f16fbad0c67fc6cdbcf8557d96df5d00.png)  
  
**启停RDS实例**  
  
在日常使用过程中，RDS实例的启动和停止是较为高频的操作类型，现在，有了alibaba-cloud-ops-mcp-server  
的支持，只要您发出指令，您的AI助手可以自动为您启动或者停止对应的RDS实例，并且等待RDS实例的状态变为期望的状态（Running或Stopped）之后, 才会向您汇报任务完成。  
- 关闭实例  
![image.png](https://ai.programnotes.cn/img/ai/47c1c2454ac806ef6f56303824169083.png)  
  
![image.png](https://ai.programnotes.cn/img/ai/074e012d153e5dce282bb453cad69e8c.png)  
  
- 启动实例  
  
       
   
![image.png](https://ai.programnotes.cn/img/ai/eb2162c19e734f76c53b79f76356b6fb.png)  
  
       
   
![image.png](https://ai.programnotes.cn/img/ai/a1b15749a6e12577d38f671a66b62548.png)  
  
  
## 结语  
  
alibaba-cloud-ops-mcp-server  
   
通过与 MCP 的深度集成，为 AI 助手赋予了强大的工具调用能力和复杂任务执行能力，显著提升了其在运维场景中的实用性和效率。无论是 阿里云资源的创建、监控、启停管理，还是在实例上运行自定义命令、更换系统镜像等操作，用户都可以通过自然语言交互轻松完成，真正实现了“掌上运维”的便捷体验。更多功能和支持的工具细节，请参阅本文附录。  
  
我们诚邀您体验  
   
alibaba-cloud-ops-mcp-server，亲身感受 AI 与云计算深度融合带来的高效与便利，开启智能运维的新篇章！如果您对 OOS 的能力感兴趣，也可以访问帮助文档[8]或登录OOS 控制台[3]，探索更多关于 OOS 的强大功能和应用场景。  
# 附  
## alibaba-cloud-ops-mcp-server支持工具列表  
  
![](https://ai.programnotes.cn/img/ai/37e8a43ed4f9d73c36ab528c99dd340a.png)  
## 参考文档：  
  
[1]MCP: https://modelcontextprotocol.io/introduction  
  
[2]alibaba-cloud-ops-mcp-server: https://github.com/aliyun/alibaba-cloud-ops-mcp-server  
  
[3]阿里云系统运维管理(OOS): https://oos.console.aliyun.com/overview?utm_content=g_1000403402  
  
[4]Visual Studio Code: https://code.visualstudio.com/  
  
[5]Cline: https://cline.bot/  
  
[6]UV: https://github.com/astral-sh/uv  
  
[7]百炼: https://bailian.console.aliyun.com/?utm_content=g_1000403403  
  
[8]OOS帮助文档: https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos?utm_content=g_1000403404  
  
