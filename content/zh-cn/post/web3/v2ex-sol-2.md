---
title: "V2EX上关于SOL的讨论"
date: "2023-10-05"
tags: ["Solana", "SNS", "IPFS", "区块链", "V2EX"]
categories: ["区块链技术"]
description: "本文介绍了V2EX社区中关于Solana区块链域名服务的讨论，包括注册、配置IPFS网站及与V2EX的集成方法。"
author: "yi"
image: ""
---

核心内容:
- Solana Name Service (SNS) 支持使用SOL/USDC注册域名，实现钱包地址简写化
- V2EX已实现.sol域名与用户主页的站内跳转功能
- 通过IPNS记录可将网站与Solana名称绑定，支持IPFS内容访问

## Solana Name Service

https://sns.id/

你可以用 SOL 或者 USDC 注册一个 Solana 域名，这样如果别人需要给你直接转账的时候，就可以不用很长的钱包地址，而可以是类似这样的地址:  v2ex.sol

Phantom 和 solscan 网站都支持查询 Solana 域名上的余额和持有。

同时 Solana 域名上也可以运行用 IPFS 做的网站，在 .sol 后面加上 .build 就可以访问上面的 IPFS 内容，比如这是我的一个短内容博客：

https://sepia.sol.build/

## Link a Website to Solana Name

Solana 名称服务（sns.id）是运行在 Solana 区块链上的身份系统。它支持向名称中添加 IPNS 记录，并且还有一个网关可以访问带有 IPFS/IPNS 记录的 .sol 名称。

你可以在 sns.id 上注册你的 Solana 名称。建议使用 Phantom 钱包应用，并且钱包中需要有一些 USDC。

### 第一步 · 复制 IPNS

在“My Planets”下，右键点击你的网站，选择“复制 IPNS”。你将获得一个以 k51 开头的长字符串，已经复制到剪贴板。

### 第二步 · 设置 IPNS 记录
打开你的名称的记录页面，点击“编辑记录”。

找到名为 IPNS 的一行，粘贴之前复制的以 k51 开头的 IPNS 字符串。

然后点击“保存更改”。

### 第三步 · 访问
Solana 是一个高速区块链，能够在不到一秒的时间内更新你的记录。保存 IPNS 记录后，你可以通过 sol.build 公共网关访问你的网站。

## 论坛新功能: Solana 域名在 V2EX站内跳转到用户主页

如果你已经注册了 .sol 域名，那么现在 V2EX 可以支持这样的跳转：

v2ex.com/v2ex.sol -> v2ex.com/member/Livid

接下来，会有更多和 .sol 域名的集成及新玩法。

感谢 api.web3.bio 提供的好用的解析 API 。

## 参考链接

- Solana Name Service,[https://www.v2ex.com/t/1150717](https://www.v2ex.com/t/1150717)
- Link a Website to Solana Name (.sol), https://www.planetable.xyz/guides/solana/
- Solana 域名在 V2EX 站内跳转到用户主页, https://www.v2ex.com/t/1152423