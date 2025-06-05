---
title: "N8N 流程自动化 - 使用 N8N+多维表格 自动编写周报和多渠道发送周报"
date: "2025-05-31"
tags: ["N8N", "流程自动化", "多维表格", "周报", "飞书"]
categories: ["自动化", "n8n","效率工具"]
description: "本文介绍如何使用N8N和飞书多维表格实现任务管理流程自动化，自动编写并多渠道发送周报。"
author: "数翼数翼"
image: ""
---

- **核心内容点1**: 使用 N8N 和飞书多维表格实现任务管理流程的自动化。
- **核心内容点2**: 通过配置 N8N 节点，读取多维表格数据，并利用 AI 生成周报。
- **核心内容点3**: 实现周报的多渠道发送，如飞书、企业微信、邮件等。

**源自** |  数翼数翼 2025-05-31 00:21

今天介绍如何基于 **多维表格**和**N8N** 打造自己的任务管理流程和自动化进行周报编写发送。

内容包含：
- • 设计自己的任务管理流程

- • 创建飞书应用

- • 获取飞书应用访问凭证

- • 安装配置N8N飞书节点

- • 配置流程读取数据整理周报

- • 相关应用授权操作

- • 通过飞书消息发送周报

- • 多渠道发送周报

- • 如何查找社区节点

本文基于飞书实现，类似思路的大家也可以使用企业微信，钉钉，Notion 等服务，甚至是本地Excel文件来实现。 只需要把数据读取和处理的部分换成自己平台的数据即可。

## 设计自己的管理流程

每个人根据自己岗位不同、工作习惯不同、公司要求不同都会多多少少形成自己的任务管理流程以及方法论。

我今天介绍一个比较适合大家的方案，按周管理事务，每周进行轮转，
- • 用多维表格来记录和管理任务

- • 每周五下午固定时间自动发送周报

- • 每周一早上把任务转到本周

- • 清理已完成的任务

## 新建飞书多维表格

我们新建一个飞书多维表格，名字叫做 工作任务和计划，添加你常用的列，比如：
- • 名称
- • 优先级
- • 状态
- • 描述
- • 进度
- • 开始时间
- • 结束时间
- • 计划时间等等

![](https://ai.programnotes.cn/img/ai/bc3510b85c73cd43362dac1c69b64f35.png)

我建立了这样一个表格，并且录入了一些样例数据给大家做Demo用。

## 创建飞书应用

我们如果希望用 n8n 对飞书做自动化，需要创建一个飞书应用，然后获取应用的访问凭证。

大家可以打开下面链接，按照文档一步步操作。

如何创建企业应用[1]

![](https://ai.programnotes.cn/img/ai/980c7d8ec86dca38251d79696e9e1a81.png)

点击**创建企业自建应用**，

![](https://ai.programnotes.cn/img/ai/243040ab0035059ff1f5e2ee01d1cd2e.png)

输入应用名字，再点击 **创建** 即可。

![填写应用信息](https://ai.programnotes.cn/img/ai/63adbc85c05d26cf6e8c869319fc34d9.png)

填写应用信息

### 获取应用访问凭证

接下来获取应用的访问凭证，拿到访问凭证就可以不在飞书应用里面也可以访问和操作飞书数据了。

如何获取应用访问凭证[2]

在刚才创建的应用页面，点击打开 **凭证与基础信息** 子页面， 复制 App ID 和 App Secret 备用。

![获取](https://ai.programnotes.cn/img/ai/98c21243c92a2cff21f11ae3c8b0b071.png)

获取

## 安装 n8n 飞书节点

虽然 n8n 官方没有提供飞书节点，但是万能的社区有飞书节点的实现，安装也很简单：

社区节点的安装教程可以参考下面文档：
- • 
如何安装社区节点[3]

进入 n8n 应用的设置，点击设置页面的 Community nodes，点击 Install，填写我们要安装的界面名称 n8n-nodes-feishu-lite，然后再点击 Install，

![](https://ai.programnotes.cn/img/ai/699b48a254e468e428c04e35513750db.png)

等几秒钟，弹窗关闭就可以看到列表中有我们的节点了。

![](https://ai.programnotes.cn/img/ai/140089efadba33da973d24a125fd3801.png)
## 使用飞书节点

新建一个 n8n 工作里，点击搜搜节点 feishu 可以看到我们安装的节点了：

![搜索Feishu节点](https://ai.programnotes.cn/img/ai/cb5ca5aaa0aa010b3f49eed5fe716e9b.png)

搜索Feishu节点,点击节点，选择一个操作，比如最后一个操作 获取当前应用AccessToken才测试一下链接是否可用。

在节点配置页面创建账户，点击 **Credential** 的 **Create new credential**, 选择 Feishu，填写我们刚刚复制的 App ID 和 App Secret，点击Save。

![填写App信息](https://ai.programnotes.cn/img/ai/3abdf9ce94a0b63475a9c4283c82ff93.png)

填写App信息

然后我们执行测试即可看到运行结果。

![测试飞书连接](https://ai.programnotes.cn/img/ai/d28524a2009d97527b2b0683e4ccb14a.png)

测试飞书连接
## 应用权限

在执行飞书操作的过程中，如果没有授权就会遇到错误，根据错误信息中的地址，打开控制台进行授权即可，

比如任务相关而全新啊

![勾选权限点击开通](https://ai.programnotes.cn/img/ai/0218ce2d8b899bb58ffcdd7406599463.png)

勾选权限点击开通

或者 ip_list 的权限：

![ip_list 权限](https://ai.programnotes.cn/img/ai/0f47ca90023f20ce7675a4e99d747ac4.png)

ip_list 权限

部分权限开通的时候需要你设置应用可见的权限范围，我们如果是开发测试，或者是自己用的话，直接选择全部就好了：

![](https://ai.programnotes.cn/img/ai/874d311ceae27b8a8026f5cceff4b1f3.png)

大家可以一次把权限设置好，也可以在任务出错的时候再设置，后续关于权限设置我就不再介绍了。
## 获取多维表格访问凭证

现在我们打开刚才创建的的多维表格，点击上面的复制链接按钮复制当前多维表格的链接，以便我们解析多维表格获取其 app_token
。

![拷贝多维表格地址](https://ai.programnotes.cn/img/ai/b319074e17b3e2deb74114ab2fd383e8.png)

拷贝多维表格地址

在 n8n 工作流中新增飞书节点，
- • 选择 **资源** -> 多维表格

- • **操作** -> 解析多维表格地址

- • **多维表格地址** 粘贴你刚才拷贝的地址

点击测试，结果中可以看到多维表格的信息里面有一个 app_token，这个 Token 就是飞书多维表格的访问凭证。

![App Token](https://ai.programnotes.cn/img/ai/204767db6beb074101c1ee7640f1162a.png)

App Token

我们使用 获取多维表格元数据 来测试下 app_token 是否可用。

在后面添加一个飞书节点，操作选择 **获取多维表格元数据**，把 app_token 拖入到 app_token 输入框中，点击测试。

![多维表元数据](https://ai.programnotes.cn/img/ai/d8af5ea38b7252699c3c2181a5ed1ca6.png)

多维表元数据

可以看到，我们能够正确获取多维表的名称信息。
## 列出数据表

一个多维表格可能有多个数据表，每个数据表的数据都不一样，我们可以通过 列出数据表
 来获取多维表格中的数据表列表，然后选择一个数据表来读取数据。

在后面添加一个飞书节点，操作选择 **列出数据表**，把 app_token 拖入到 多维表格 Token 输入框中，点击测试。

![列出数据表](https://ai.programnotes.cn/img/ai/51562ea60cf69a1715f5a4d05a382ac4.png)

列出数据表
## 读取数据

在后面添加一个飞书节点，操作选择 **查询记录**，把 **获取元数据节点** 的 app_token 拖入到 多维表格 Token 输入框中， 把上一步的 Table ID 拖入到 多维表格ID 输入框，点击测试。

![读取数据](https://ai.programnotes.cn/img/ai/324845897438b4fd37d48740c54754bc.png)

读取数据

右侧执行结果就是我们多维表格的数据，大家测试的时候可以自行对照一下，是不是一样的。
## 处理数据

我们现在希望把表格中的数据作为参考资料让 AI 帮我们整理成周报。但是 表格中的列比较多，很多是在周报中不需要的， 我们先获取我们需要的任务字段。

先增加一个 Split out 拆分节点，把数据进行拆分，独立处理。不需要什么配置，点击确认即可。

![拆分数据](https://ai.programnotes.cn/img/ai/fbb3c9308b5e659631827592f902fb6d.png)

拆分数据

接着增加一个 Edit Fields 节点，把我们需要的字段拖入，测试无误，点击确认即可。

![选择需要的字段](https://ai.programnotes.cn/img/ai/2badb1f6a3d3ade0d2fa80c20a9e2388.png)

选择需要的字段

再增加一个 Edit Fields 节点，把任务数据组织成 Markdown 格式，当然我们也可以把这两个节点的功能放在一起完成。

![](https://ai.programnotes.cn/img/ai/115d8855443b580c50fd5fa672dfe0f5.png)

我的 Markdown 格式是这样的：
```
## {{ $json.task }} - description: {{ $json.description }}- status: {{ $json.status }}- percent: {{ $json.percent }}- deadline: {{ $json.deadline }}
```

再增加一个 Aggregate 节点，把之前拆分的数据聚合起来：

![聚合](https://ai.programnotes.cn/img/ai/b4b37a0c0c432f77fd356e17d04dd627.png)

聚合
## AI 生成周报

现在我们已经把数据整理成 Markdown 格式，再用 AI 生成周报就很简单了。

添加一个 OpenAI 节点，我们选择 deepseek-v3 模型，输入系统提示词，并且把上一步的输出投入到用户提示词， 运行即可看到结果：

![](https://ai.programnotes.cn/img/ai/af0d5e5cf3deb91466032aec41f575e0.png)

系统提示词可以根据自己的岗位、角色、汇报对象、公司风格等多方面来限制，比如：
```
作为一家科技公司的设计总监，请根据我提供的本周任务清单，生成一份结构清晰、专业简洁的周报。周报需包含以下核心模块,使用Markdown格式，并体现数据驱动和结果导向：  
1.**本周核心任务概览**   
- 按优先级列出3-5项重点任务（例如：产品迭代推进、技术架构优化、跨部门协作等）     
- 标注每项任务的进度状态（已完成/进行中/受阻）及关键里程碑  
2.**量化成果展示**   
- 用数据量化成果（如：完成XX模块开发（100%）、系统性能提升XX%、解决XX个关键Bug）     
- 技术类任务需注明具体技术指标（如API响应时间、代码覆盖率等）  
3.**风险与问题分析**   
- 列出遇到的瓶颈（如第三方服务延迟、测试环境不稳定）     
- 附上已采取的解决方案及待协调资源  
4.**下周计划与资源需求**   
- 明确下周3项核心目标（建议区分「延续性任务」和「新启动任务」）     
- 提出需要支持的资源（人力、预算、其他部门配合等）  
5.**行业洞察建议（可选）**   
- 结合本周工作，附加1-2条对行业技术趋势的观察（如AI工具应用、竞品动态）  
**风格要求：**
- 避免流水账，用「结论先行+数据支撑」的表述  
- 技术术语需易懂（如用「用户认证系统升级」而非「OAuth2.0改造」）  
- 重要内容加粗或分点标注  
- 调理清晰，避免冗长请确保周报内容简洁、清晰，在500字以内。
```
## 发送周报

周报生成好了，我们现在发送给自己看看。

新建一个飞书节点，选择发送消息动作，配置接受者ID和消息内容。

![](https://ai.programnotes.cn/img/ai/48f94f250ea3edd2685cba0d767ad516.png)

获取联系人ID可以参考下面文档：

如何获取用户OpenID[4]

最简单的就是通过控制塔调试获取：

![获取用户ID](https://ai.programnotes.cn/img/ai/c06899b54aacfffcef74d3a9086746c4.png)

获取用户ID

填入用户ID，进行测试，可以看到消息发送成功！

打开飞书消息，可以看到刚刚发送的消息：

![飞书消息](https://ai.programnotes.cn/img/ai/1c1d4c4d3443a17317a3ac9acf58d63f.png)

飞书消息

如果消息不满意，我们就可以修改前面的提示词，再次生成周报，直到满意为止。
## 构建多种通知方式

有时候我们希望周报不仅仅是发送出来，而是希望多渠道通知，比如提交一份、发给自己一份、同时备份一份， 下面给看看如何实现同时发送多个地方。

增加一个 **Edit Fields** 节点，把周报复制成一个数组，我们设置 length: 4 表示复制成四个：

![](https://ai.programnotes.cn/img/ai/935fd067bddbac5a25ee8e6af28436a6.png)

表达式填写如下：
```
{{ Array.from({ length: 4 }, (_, i) => ({ key: i, value: $json.message.content })) }}
```

数据转换不会写没关系，只要把你的需求告诉 AI（比如 DeepSeek、OpenAI 等），AI 写好拷贝进来就行。 如果有有流程不会实现，AI 也都会一步步教你。

然后增加一个 **Split Out** 节点，执行拆分逻辑，默认配置即可。

增加一个 **Switch** 节点，设置数组不同的逻辑，Switch 节点配合如下：

![](https://ai.programnotes.cn/img/ai/aab2e4e363b462357794fd45b7707771.png)

可以看到 Switch 节点后面有多个四个分支，每个分支都是一个新的消息，后续连接自己的逻辑即可。

![](https://ai.programnotes.cn/img/ai/884ebf9ea9676672764f08e53df6c977.png)

比如：
- • 一个飞书发给自己

- • 一个 HTTP 发送给企业微信

- • 一个有邮件发送，汇报给领导

- • 一个存储在数据库，以便我们你以后统计用

![](https://ai.programnotes.cn/img/ai/3f2995959afe900f571c0e2023ed2ad2.png)
> 发送邮件需要配置 SMTP 信息，和邮件客户端配置类似，大家自行配置即可。

### 查找社区节点

如果默认节点不满足你的需求，不用去百度找（效率太低），官方网站上都可以搜索到：
- • 
https://community.n8n.io/[5]

![](https://ai.programnotes.cn/img/ai/f727ca4e14350a14f2a8ac941d541973.png)
## 总结

完整的流程如下，一条直线：最后 Switch 一下，我为了看着方便，换了行展示。

![](https://ai.programnotes.cn/img/ai/ee2fd39cd407641062fca0bd4963dac6.png)

限于篇幅文章开始方案中的每周自动流传任务我们放到下一篇讲。
#### 引用链接

[1] 如何创建企业应用: https://open.feishu.cn/document/develop-process/self-built-application-development-process
[2] 如何获取应用访问凭证: https://open.feishu.cn/document/server-docs/api-call-guide/calling-process/get-access-token?lang=zh-CN
[3] 如何安装社区节点: https://docs.n8n.io/integrations/community-nodes/installation/
[4] 如何获取用户OpenID: https://open.feishu.cn/document/faq/trouble-shooting/how-to-obtain-openid?lang=zh-CN
[5]: https://community.n8n.io/


