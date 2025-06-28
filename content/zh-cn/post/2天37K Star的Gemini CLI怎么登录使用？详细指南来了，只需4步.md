---
title: "2天37K Star的Gemini CLI怎么登录使用？详细指南来了，只需4步"
date: "2025-06-28"
tags: ["Gemini CLI", "登录", "教程", "Google Cloud", "Node.js"]
categories: ["AI","Gemini", "MCP" ,"开发"]
description: "本文详细介绍了Gemini CLI的登录使用方法，包括Node.js安装、权限开通、项目ID获取和网络配置。"
author: "袋鼠帝"
image: "https://ai.programnotes.cn/img/ai/614a18297fe90edfdfe7761281d2e997.png"
---

**核心内容**:
- Gemini CLI登录问题解决方案
- 安装Node.js和Gemini CLI的步骤
- 配置Google Cloud权限和网络设置

**源自** |  袋鼠帝袋鼠帝AI客栈 2025-06-28 14:08

大家好，前天分享了一篇介绍Gemini CLI的文章,但看评论区好些朋友说登录不上，授权那里会一直卡住

be like：

![](https://ai.programnotes.cn/img/ai/45ac9364660cbfbd7ed98f682ad0a14f.png)

所以，这篇文章，我带大家来解决一下这个登录不上的问题

另外，Gemini CLI的Github上提的问题太多了。。。目前已经有516个Issues

但是Star也涨的忒快，早上爬起来看还是35K，现在（中午）就37.1K了？？

![](https://ai.programnotes.cn/img/ai/da54596a7f302d5ae3c4f44d730dc1e1.png)

鉴于目前问题较多，大家可以再等等，毕竟开源的力量非常大（而且这个项目太火了）

我相信随着时间的推移（大家共建），Gemini CLI会越来越好用。

它的更新频率还不错，目前最新版v0.1.7

![](https://ai.programnotes.cn/img/ai/6fb20306cbec692b0f1965677b67f869.png)

我们本次通过，下面的指令来安装Gemini CLI

```bash
npm install -g @google/gemini-cli
```

**1. 安装Node Js**

前提是需要先安装Node.js，并且版本号要大于等于18

https://nodejs.org/zh-cn/download

nodejs安装成功后，可以通过 node -v 查看版本号（注意-v前面有个空格）

![图片](https://ai.programnotes.cn/img/ai/1c765b22ae11129c115bdbf69789e5eb.png)

**2. 安装Gemini CLI**

nodejs安装成功后,执行下面的命令安装Gemini CLI

```bash
npm install -g @google/gemini-cli
``` 

如果Gemini CLI有版本更新可以重复执行上面这条指令，每次执行会拉取最新版本

如果是Mac或者Linux用户，建议在前面加上sudo（给系统权限），否则可能会执行失败

```bash
sudo 
npm install -g @google/gemini-cli
```

安装成功之后，通过 gemini --version 来查看Gemini CLI的版本

![](https://ai.programnotes.cn/img/ai/da4a56c56ce46936c08c5a80ea82aa32.png)

****
**3. 开通Google Code Assist权限**

然后我们要在Google Cloud检查一下Google Code Assist权限是否开通

如果没有开通，需要启用（Enable）

![](https://ai.programnotes.cn/img/ai/fe7ae725ab8421defcb765c1a5149efd.png)

Google Code Assist地址：

https://console.cloud.google.com/marketplace/product/google/geminicloudassist.googleapis.com?q=search&referrer=search&inv=1&invt=Ab1S8w&project=poetic-park-411205

****
**4. 获取Google Cloud的项目ID**

获取Google Cloud的一个项目ID

![](https://ai.programnotes.cn/img/ai/b799293236152650dea3b1eb890fad0d.)

获取Google Cloud项目地址：

https://console.cloud.google.com/welcome?inv=1&invt=Ab1S-A&project=fast-gecko-411205

把整个项目ID复制备用（如果没有项目需要新建一下）

![](https://ai.programnotes.cn/img/ai/472aa8a501b11cc9d811268ef465da4d.png)

在控制台或者终端执行：
```bash
export GOOGLE_CLOUD_PROJECT=项目ID
```


**4. 配置网络**

注意：需要魔法上网哦，登录的时候最好开启魔法的
全局tun模式或者增强模式。

最好用美国节点

如果是Windows可以在控制台执行一下下面这条指令
```bash
set https_proxy=http://127.0.0.1:7890
```

如果是Mac或Linux可以在终端执行下面这条
```bash
export https_proxy=http://127.0.0.1:7890
```

以上操作最好都是新开一个控制台或者终端进行

看各自的代理端口是多少，大多数默认是7890

到这里，准备工作都做完了


**5. 登录Gemini CLI**

最后执行：

```bash
gemini
```

就开始自动登录了

![](https://ai.programnotes.cn/img/ai/614a18297fe90edfdfe7761281d2e997.png)

会拉起浏览器跳转到Google登录页，注意用刚刚在Google Cloud做了配置的那个Google邮箱登录

登录后你会跳转下面这个页面，就代表登录成功了

![](https://ai.programnotes.cn/img/ai/186860e98241d9b1d4059fdd2e53997f.png)

切换到Gemini CLI，如下。可以在对话框里面对话了

![](https://ai.programnotes.cn/img/ai/c0cb8eabc3ad8f5375b5cef1826cae8a.png)

登录一次之后，下次再执行gemini，就会自动登录，不用重复跳转网页登录。

如果觉得有用，希望给个免费的三连支持一下，感恩～

如果操作完还是有问题，欢迎评论区沟通，大家一起想想办法。
