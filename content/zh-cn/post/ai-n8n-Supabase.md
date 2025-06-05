---
title: "用n8n做AI工作流驱动网站出海赚美金1：连接Supabase数据库"
date: "2025-06-03"
tags: ["n8n", "Supabase", "AI工作流", "出海", "自动化"]
categories: ["AI", "n8n","No-Code"]
description: "使用n8n连接Supabase数据库，构建AI工作流，驱动网站出海并赚取美金。"
author: "饼干哥哥AGI"
image: ""
---

- 使用n8n连接Supabase数据库，实现网站数据的后端处理。
- 通过n8n工作流提交新网站，并利用AI自动解析网站信息。
- 将Python后端转换为n8n工作流，降低开发和运营成本。

**源自** |  饼干哥哥饼干哥哥AGI 2025-06-03 17:57

年初的时候我做了一个AI编程工具的导航网站，打算流量上来后就可以接谷歌广告赚美金：

https://www.aicoding.help/cn

设想是根据AI编程开发的流程来推荐每个阶段的效率工具：
灵感与想法、原型与设计、编程开发、数据库与存储、部署上线、扩展能力、数据分析、内容管理、协作与运营

![Image](https://ai.programnotes.cn/img/ai/3582f9319fd5b77af17475d08f4cc7e3.png)


目前挂在了vercel上，感兴趣可以去看看，但实际上还有很多问题，待一步一步解决。

具体这个网站是怎么做的，可以参考之前的文章，基于Tap4AI项目：[2025穷鬼开发套餐：不花一分钱，部署一个AI导航网站全流程，附tap4ai、aigotools 对比](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257491207&idx=1&sn=5af373cc431a810400003eb641ffea1d&scene=21#wechat_redirect)



这个导航网站分成两部分
- 前端页面的展示，主要痛点就是怎么把网站设计的好看且合理
- 后端数据的处理，
前端页面其实不存数据，每次用户打开网站的时候，都是直接从数据库里读数据的
这样的好处就是维护方便，因为前端页面要改的话是要重新部署上线的，很麻烦。


例如我数据库用的是Supabase，如果哪个内容写错了，我只需要对Supabase里的内容进行修改就行了，有新网站也可以直接在数据库里添加即可。


所以，目前这个网站的工作量在于后端，看着简单其实挺麻烦的，日常运营有以下几个动作：
- 提交新的网站
- 爬虫，去爬新的网站，截图，AI生成相应的描述
- 把描述翻译成多个语言，例如我至少是中英日
- 写SEO文章，让谷歌收录

具体可以看这个图：

![Image](https://ai.programnotes.cn/img/ai/a2392dd327f28e94ce4a182de8d538d6.png)

目前这个后端是真的离谱，有一个单独的Python项目来跑，实在是太重了。

![Image](https://ai.programnotes.cn/img/ai/19e3872f72c95362b7731794afb4d49b.png)

因为最近都在玩n8n，而且n8n对接的都是海外的服务，很适合出海做后端服务。

我在想是不是可以把这个Python后端转成n8n的工作流呢？

说干就干，一步一步来。

![Image](https://ai.programnotes.cn/img/ai/7c1b0157ef29a03ba94ed758d2989d32.png)

## 需求拆解

首先，解决第一步：提交新网站的需求。

![Image](https://ai.programnotes.cn/img/ai/0874cffc7db9b81d2070365f31168b22.png)

在数据库，我有一个submit表，用户提交网站请求后，会插入到这里，包含名称、网址、分类、描述等字段，状态status是0

等爬虫把这网站爬完，处理好数据后，状态会更新为1，证明处理完了。

![Image](https://ai.programnotes.cn/img/ai/45975a7dbcc6969150f9afeb91a03f9e.png)


目前这一步我是很苦逼的自己写了个python脚本来手动插入数据的。

今天我们就来解决这个问题：通过n8n工作流提交网站到数据库supabase

## n8n连接Supabase

首要任务就是让n8n连上Supabase,但在此之前，需要先找到两个关键的key：

在Supabase的Project Settings里找到API Keys，下面的service_role secret

![Image](https://ai.programnotes.cn/img/ai/306613b3d3e517ba1db019e804c11d42.png)


同个目录的General找到Project ID

![Image](https://ai.programnotes.cn/img/ai/e6f0946f8d2a5f348a45ecc991aa3b83.png)


接着就可以回到n8，创建一个Supabase的Create a row节点

![Image](https://ai.programnotes.cn/img/ai/406c91c03634ce3448b563c7618d8840.png)


老规矩，先新建一个Credential，然后把前面找到的两个信息填入其中Host，一般就是你的proejct id + supabase.co 后缀，如下图。

![Image](https://ai.programnotes.cn/img/ai/46c6287d4acf8570dad8a24ca0174c55.png)

## 用例测试

测试一下，假设我们要提交bolt.new这个全栈AI开发网站

配置对应的信息
- Name: bolt.new
- Url: https://bolt.new/
- Category: 编程开发
- remark：Bolt is an in-browser AI web development agent for full stack web application development.
只要前面连接成功的话，这里就会自动从supabase中获取表格结构，你只需要去选字段就好了，非常方便

如下图，n8n表示测试成功

![Image](https://ai.programnotes.cn/img/ai/6bcf9b0323b9ebfa0df2d76d6a733c2b.png)


同时，在supabase里也能看到，多了一行。

## 完成工作流

在正式开发工作流之前，要先想清楚自己想要的产品是什么样子的。

例如当前这个项目，我想要的是：只要给一个网站，AI就能自动判断它是什么，并给出对应的信息，进而插入到Supabase表的位置。

这样拆解下来，就需要做：
- AI从用户给的信息中解析出网址
- 判断用户有没给更多信息，例如名称、描述、分类
- 如果没有，则访问该网址，判断是什么，生成名称、描述、分类
- 对结果进行结构化输出
- 传入到supabase的submit表

先看效果：

![Image](https://ai.programnotes.cn/img/ai/e0431bf5918c71d2242610df3cef178c.png)


现在我只给一个魔塔社区的网站 https://www.modelscope.cn/

就能看到AI Agent调用了Jina AI的工具去读网址，并且根据要求输出了格式


接下来看每个节点。
 
新建一个AI Agent节点：

对接上前面的用户对话框里的输入

![Image](https://ai.programnotes.cn/img/ai/3efc66f814209772cf22bf95b6448db0.png)


参考提示词：

````
我在给一个AI编程工具导航网站提交新的网站录用，需要你从用户给的信息中提取出以下内容：
```json
{        
    "name":"这个网站工具的名称",        
    "Url":"这个网站的网址",
    "Category":"分类，只能从 灵感与想法、原型与设计、编程开发、数据库与存储、部署上线、扩展能力、数据分析、内容管理、协作与运营 中选择一个",
    "remark":"这个网站工具的简单介绍不超过50字"
}
```
更具体的，你需要做：
1. AI从用户给的信息中解析出网址
2. 判断用户有没给更多信息，例如名称、描述、分类
3. 如果没有更多信息，则要调用工具`jina AI reader`访问该网址，根据返回内容判断这网站是什么，生成名称、描述、分类
4. 对结果进行结构化输出
````

可以看到这个AI Agent还是挺能配置的，这就是n8n的优势，非常自由

![Image](https://ai.programnotes.cn/img/ai/c311a7cb130cf58e5ff4e0401bc7db35.png)

在工具Tool的部分，配置一个Jina AI工具，这是一个能帮助我们读取网址内容的工具

很简单，用谷歌登录一下就有key了

如下图，URL这里可以让大模型自己去判断

![Image](https://ai.programnotes.cn/img/ai/8cbecbbec3e399645ed001f815caa5f6.png)

格式化输出这里给个例子就行

![Image](https://ai.programnotes.cn/img/ai/b3d1217f9a64ac588ec3dab12dce7641.png)

接着就可以连上Supabase节点了，把AI拆解好的内容分到对应位置：

![Image](https://ai.programnotes.cn/img/ai/f72e62bcd093fc005fc2d4cad53bb4dc.png)

非常简单！！

不过每次要打开n8n工作流里面去提交就太麻烦了，我们可以用n8n内置的表单功能

新建一个表单

![Image](https://ai.programnotes.cn/img/ai/f4b0a255590ff71fef88cc26857501a6.png)

设置好需要的参数：

![Image](https://ai.programnotes.cn/img/ai/d6af40a203da5f583e87ef9962f394a6.png)

执行的时候，就自动生成好了一个表单网站了

![Image](https://ai.programnotes.cn/img/ai/da0ec096e53b35bc14f8e97a0e3ced32.png)

因为新增了一个表单，传入到AI节点的数据结构不同了，所以我就添加了几个数据处理节点，最终同样也能向数据库提交数据。

![Image](https://ai.programnotes.cn/img/ai/edd1a32ad6edb85a9e2fa6b0d9f2bed1.png)

至此，我们就完成了第一阶段的改造，把原先通过Python提交网站的功能，变成了n8n的工作流，并且可以通过表单的形式提交；
甚至后面可以改成webhook的监听，或者改造成mcp，更加自由的添加网站。

可玩性非常高！！

接下来会继续更新用n8n驱动网站出海赚美金系列，帮助大家用n8n降低开发和运营成本。

感兴趣的可以关注公众号「饼干哥哥AGI」，后台回复「AI交流群」


