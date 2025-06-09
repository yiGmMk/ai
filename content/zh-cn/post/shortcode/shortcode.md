---
title: "Hugo Stack Shortcode Test"
date: "2025-06-09"
tags: ["Hugo", "Shortcode", "Test"]
categories: ["Hugo"]
description: "使用 Hugo 的嵌入式短代码在您的内容中插入视频、图像和社交媒体嵌入等元素。"
params:
  color: red
  size: medium
---

Use embedded, custom, or inline shortcodes to insert elements such as videos, images, and social media embeds into your content.

## 二维码/QR

使用: qr text="https://ai.programnotes.cn"

{{< qr text="https://programnotes.cn" />}}

{{< qr >}}
https://ai.programnotes.cn
{{< /qr >}}

要为电话号码创建 QR 码: qr text="tel:+12065550101"

{{< qr text="tel:+12065550101" />}}

## Bilibili

{{< bilibili BV1Aq78zHE9k >}}

## 腾讯视频

{{< tencent g0014r3khdw >}}

## vimeo 

要显示具有此 URL 的 Vimeo 视频, https://vimeo.com/channels/staffpicks/55073825

{{< vimeo 55073825 >}}

## 评论

不支持

## 详细信息

{{< details summary="See the details" >}}
This is a **bold** word.
{{< /details >}}

## 参数

We found a {{< param "color" >}} shirt.


## Instagram

{{< instagram CxOWiQNP2MO >}}

## X/推特

显示具有此 URL 的 X 推文: https://x.com/SanDiegoZoo/status/1453110110599868418

{{< x user="SanDiegoZoo" id="1453110110599868418" >}}

## YouTube

显示具有此 URL 的 YouTube 视频: https://www.youtube.com/watch?v=0RKpf3rK57I

{{< youtube 0RKpf3rK57I >}}

## 参考

- [中文文档](https://gohugo.com.cn/shortcodes/youtube/)
- [stack主题文档](https://stack.jimmycai.com/writing/shortcodes)