---
title: "斩获86K Star！最强开源MCP平台【双向+本地MCP】自由度拉满，太绝了～"
date: "2025-04-29"
tags: ["n8n", "MCP", "AI workflow", "开源平台", "自动化"]
categories: ["AI", "开发工具"]
description: "n8n成为最强开源MCP平台，支持双向和本地MCP，自由度高，集成1500+工具和模板。"
author: "袋鼠帝"
image: ""
---

**核心内容:**
- n8n支持双向MCP，既可以作为客户端使用MCP-Server，也可以作为服务端发布MCP-Server。
- n8n集成了1500+工具和模板，支持通过SSE远程连接外部MCP-Server，例如高德地图MCP-Server。
- n8n通过安装社区节点，可以支持本地MCP-Server的使用，并通过配置两个Tool节点实现MCP工具的列出和执行。

**源自** |  袋鼠帝袋鼠帝AI客栈 2025-04-29 00:58

开源项目n8n,最强开源AI workflow平台,这么快（半个月）就从75K Star干到86K Star了？

![](https://ai.programnotes.cn/img/ai/5c48964d4811c53cdbdc4b275f70d567.png)

最关键的是，在最近的1.88.0版本，n8n终于官宣支持MCP了！

而且它不仅支持双向MCP，还支持添加本地（stdio）MCP。

![](https://ai.programnotes.cn/img/ai/bfae6707d7f0ccb44c6b9a44ecb63b3b.)

![](https://ai.programnotes.cn/img/ai/b799293236152650dea3b1eb890fad0d.)

双向MCP：既可以作为MCP客户端，去添加使用各种MCP-Server。又可以作为MCP服务端，发布MCP-Server供其他客户端使用。

MCP-Server目前有两种使用方式，一种是把MCP-Server的工具集成到本地使用，一种是远程调用。而n8n两种都支持了

![](https://ai.programnotes.cn/img/ai/932b35af2c9bc485d1d6c797b2c9cac8.)


加之n8n是最强AI Workflow出身，本身就集成了1500+工具和模板。
> n8n工作流用法

> 袋鼠帝，公众号：袋鼠帝AI客栈[DeepSeek+开源n8n打造24h推特(X)热点监控Workflow，太绝了！【附赠：完整工作流】](https://mp.weixin.qq.com/s/jC_bPFcha-SZmBO_EMGJMg)

现在n8n支持MCP，拥抱MCP生态后，更是有上万的MCP-Server可随意接入，我愿称之为最强开源MCP平台。

注意：n8n是平台，而不仅仅是Cusor、Trae、Cherry Studio等 的MCP客户端。

区别在于MCP客户端只是安装在电脑上的客户端软件，只能在本地添加使用MCP-Server，但无法对外提供服务。

而n8n是可部署的Web服务（比如通过docker部署），可以部署到云服务器，不管是制作的MCP-Server，亦或是开发的MCP应用，都可以一键发布到公网，对外提供服务。

好了，话不多说，接下来我们一起看看，在n8n上如何使用MCP。

PS：本期所有工作流文件都可以在公众号后台私信：“n8n-mcp” 获取

![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)

部署新版n8n

![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)


咱们本次还是用docker-compose一键部署

目前n8n的最新版是1.90.2

先创建一个docker-compose.yml文件（空格和缩进要严格按照下面yml文件格式来哦，不能乱改）

docker-compose.yml文件内容如下：
```yml
name: 'n8n'
services:
  n8n:
    image: n8nio/n8n:1.90.2
    container_name: n8n
    restart: always
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    environment:
      - NODE_ENV=production
      - N8N_SECURE_COOKIE=false
      - N8N_HOST=你的外网IP/域名
      # 可以根据需要添加其他环境变量
volumes:
  n8n_data:
    external: true
```

接下来就是进入docker-compose.yml文件所在路径的控制台/终端

通过docker-compose up -d 命令 一键部署（或更新）

如下图，就是部署成功了

![](https://ai.programnotes.cn/img/ai/1a72e1672d0e8affc6b83237c1f93ccc.png)

不过要注意，镜像是在国外，需要开启科学上网。

没有科学上网的朋友，可以参考这篇[部署dify](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247506421&idx=1&sn=240d895a1b03de12d1035cc186e142ab&scene=21#wechat_redirect)
的方案。

成功之后直接浏览器访问：

http://127.0.0.1:5678

![](https://ai.programnotes.cn/img/ai/1724290ac2e91612f2ad954494946044.png)

 

![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)

n8n的双向MCP

![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)

n8n在1.88.0版本就支持了向MCP客服端提供MCP-Server工具的功能

同时也支持通过SSE远程使用外部的MCP-Server

![](https://ai.programnotes.cn/img/ai/e03cdb30111f308da78392785c0c3eab.png)

我将通过两个例子教大家怎么用

首先是通过SSE远程连接外部MCP-Server（以高德地图MCP-Server为例）

我们先创建一个工作流（如下图）

通过聊天触发，添加一个AI Agent节点，配置好大模型（这里我配置的DeepSeek V3），memory有没有都可以。

注意：n8n里面只有支持funcation call的大模型才能使用MCP

然后点击AI Agent中Tool的加号

![](https://ai.programnotes.cn/img/ai/8a884be604d07f16f96a78c76256aaac.png)

添加MCP Client Tool

![](https://ai.programnotes.cn/img/ai/1102f6afa744db5bd6414810b8e98ea1.png)

高德的MCP-Server的SSE地址

https://mcp.amap.com/sse?key=在高德官网上申请的key

获取高德的key

https://console.amap.com/dev/key/app

![](https://ai.programnotes.cn/img/ai/c5c1b0e1c18c3fbca66ff1c82104fad9.png)

配置MCP Client Tool

把高德的MCP-Server的SSE地址填上去

![](https://ai.programnotes.cn/img/ai/3e173c01185b0d9c9ed716b555301556.png)

就ok啦

我们测试一下

通过chat发送消息（下图），可以看到成功的调用了高德MCP

![](https://ai.programnotes.cn/img/ai/e4afddc4ffa8f88e72cb4b2cee4d8230.png)


然后我们制作一个对外提供SSE调用的MCP-Server

向MCP客服端提供MCP-Server工具

另外新建一个工作流在触发节点选择使用 MCP Server Trigger

![](https://ai.programnotes.cn/img/ai/3a9207e7f6ed9a7de0b62a1d5997ef9f.png)

可以看到，MCP Server Trigger这里提供可外部访问的SSE地址

![](https://ai.programnotes.cn/img/ai/74de3c6bb0b6695a54e5b297768a9457.png)

接下来咱们只需要把想要提供出去的工具、工作流、Agent等添加到这个MCP Server Trigger节点后就行。

不过我们的n8n目前是部署在本地电脑上的，无法提供外网访问，这时需要用到内网穿透技术。

也没有多复杂，咱们安装一个提供内网穿透功能的软件：贝锐花生壳

https://hsk.oray.com/

安装完毕，打开花生壳，点击增加映射

![](https://ai.programnotes.cn/img/ai/ec399d9da3777f392b428f9e36d2835c.png)

按照下图进行配置

注意：如果不成功可能需要先去花生壳网页进行实名认证等操作

![](https://ai.programnotes.cn/img/ai/068a2b6f19c76442390f5dd488a247be.png)

先在浏览器访问一下这个外网域名，如果能正常访问到本地的n8n就代表内网穿透配置成功！

![](https://ai.programnotes.cn/img/ai/5c1d585f28d4f1af9e877cf70a28f0ae.png)

我们需要再看一下这个外网域名的端口，因为设置的时候是随机端口，所以需要创建出来才知道。

可以看到我随机到的外网端口是29764

![](https://ai.programnotes.cn/img/ai/7bb2d62d2734b45cddaa2ea530f28509.png)

然后编辑一下，把内网端口和外网端口改成一样，保存

![](https://ai.programnotes.cn/img/ai/be5dc1004f9ad146bb16af9dcbd45121.png)

修改docker-compose.yml配置

重点看下图红框中的配置

![](https://ai.programnotes.cn/img/ai/bfae6707d7f0ccb44c6b9a44ecb63b3b.)

![](https://ai.programnotes.cn/img/ai/b799293236152650dea3b1eb890fad0d.)

N8N_HOST=外网域名

增加- N8N_PORT=29746

把ports的值也都改成29746

![](https://ai.programnotes.cn/img/ai/932b35af2c9bc485d1d6c797b2c9cac8.)


![](https://ai.programnotes.cn/img/ai/a2945f749e3a4f864e0b8cbe1be70dbc.png)

PS：因为这里花生壳给的外网端口是随机的，无法指定5678，所以只能把n8n的端口都改了，改成跟花生壳提供的一致。

保存之后，我们再一次在docker-compose.yml所在路径的控制台/终端执行docker-compose up -d，目前是让修改的配置生效

![](https://ai.programnotes.cn/img/ai/e3a6c995d5270a107617c4e6c55387b3.png)

这时再打开MCP Server Trigger，这里显示的SSE地址就变成外网可访问的地址了

![](https://ai.programnotes.cn/img/ai/763105f1974e789b2c9bacc913cc87dd.png)

点击MCP Server Trigger的加号

![](https://ai.programnotes.cn/img/ai/6b3ecd5c41d58efe9eb79422bca16f00.png)

这里可以添加任何工具、工作流、Agent等等...

比如咱们可以把刚刚制作的MCP工作流添加上去

![](https://ai.programnotes.cn/img/ai/539de57e2631fe00cd10baa76d4ea006.png)

调试好之后，记得保存和激活

![](https://ai.programnotes.cn/img/ai/d57e9d33f40c631422b249ff03dbeef7.png)

点开MCP Server Trigger，复制SSE地址

![](https://ai.programnotes.cn/img/ai/274d8ff8bdbb5d446e317a5e5f42ddfa.png)

就可以在其他MCP客户端添加使用啦

比如在Cherry Studio中添加使用

![](https://ai.programnotes.cn/img/ai/e4e8d1f67aa2a990b7a47023f558c254.png)


![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)

n8n集成本地MCP

![](https://ai.programnotes.cn/img/ai/0ec84596510133a5d4a1d6f1c2bdd11e.)


实际上，n8n官方的MCP，只支持通过SSE调用远程的MCP-Server使用。

要使用本地的MCP-Server，需要用到n8n的社区节点。

点击左下角头像->setting->community nodes输入n8n-nodes-mcp，点击install（安装）

![](https://ai.programnotes.cn/img/ai/532e3fe902796661b81c576c70f3fe3f.png)

30秒左右，mcp的社区节点就安装完成了

![](https://ai.programnotes.cn/img/ai/9d3b1792e6332a07636b9edf85d6cf35.png)

我们可以在刚才制作的第一个工作流上测试

点击Tool的加号，在右边
搜索mcp，可以看到有两个MCP Client Tool节点

其中，后面带有一个小盒子图标的就是刚刚安装的社区MCP节点

![](https://ai.programnotes.cn/img/ai/78735fca5d89752f674103a6c15ca40d.png)

点开之后，进入配置页面,点击Create new credential

![](https://ai.programnotes.cn/img/ai/cef98e514dc98f7a3ee89fe228a39a18.png)

参考下图的方式进行配置，这里我们添加了一个firecrawl-mcp

![](https://ai.programnotes.cn/img/ai/927ec4df47f054707a78b101cd6a73aa.png)

配置完，别忘了保存，也可以给这个MCP凭证改写名字

操作我们选择List Tools（列出MCP工具）

![](https://ai.programnotes.cn/img/ai/3941fda0525d235fd35598e7fb627406.png)

然后再添加一个本地MCP，操作选择Execute Tool（执行工具），配置如下图

![](https://ai.programnotes.cn/img/ai/f9658b218c8e9e842b72eaa2953e5833.png)

Tool Name是固定写法（表示让大模型自己选择）

{{ $fromAI('toolname') }}

Tool Parameters也是固定写法（让大模型自己组装参数）

{{ $fromAI('Tool_Parameters', '', 'json') }}

最后测试成功～

![](https://ai.programnotes.cn/img/ai/373d1aea03a2b6f87cd967c5c17bccfc.png)

一个MCP需要添加两个Tool节点，一个是列出该MCP-Server下所有的工具，另一个是让大模型选择合适的工具执行。

「写在最后」

本文介绍了n8n的MCP使用方式

n8n既可以作为MCP-Server对外提供服务

又可以作为MCP-Client添加SSE远程MCP-Server，或者本地MCP-Server使用。

可以说自由度拉满了，这套组合，可以搭配任意的MCP，实现各种高度定制化的需求。
