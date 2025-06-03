---
title: "分享一个纯 Go 实现的 Word 文档操作库 - WordZero"
date: "2025-06-03"
tags: ["Go", "Word", "文档操作", "WordZero", "开源库"]
categories: ["开发工具", "Go"]
description: "WordZero 是一个纯 Go 实现的 Word 文档操作库，支持复杂的表格操作和样式处理。"
author: "Unknown Author"
image: ""
---

核心内容:
- 纯 Go 实现的 Word 文档操作库 WordZero，无外部依赖。
- 支持复杂的表格操作、样式和格式处理，性能优秀。
- 提供基础功能、表格功能、模板功能和高级功能，API 设计直观。

最近在做一个项目需要生成 Word 报告，试了几个库都不太满意，要么功能太简单，要么需要付费不完全开源。索性自己撸了一个，现在分享给大家。

## 为什么又造轮子？

市面上的 Go Word 库要么只能做简单的文本插入，要么需要安装 Office 或者 LibreOffice 。我需要的是：

*   纯 Go 实现，无外部依赖
*   支持复杂的表格操作
*   能处理样式和格式
*   性能要好，适合批量生成

## 主要特性

### 基础功能

*   创建/读取/修改 .docx 文档
*   文本格式化（字体、颜色、粗体等）
*   18 种预定义样式，支持 Word 导航窗格
*   段落对齐、间距、缩进

### 表格功能（这个比较实用）

```go
// 创建表格很简单
table := doc.AddTable(&document.TableConfig{
    Rows: 3, Columns: 4,
})

// 设置内容和样式
table.SetCellText(0, 0, "姓名")
table.MergeCells(0, 0, 0, 1) // 合并单元格

// 还有迭代器，方便批量处理
table.ForEach(func(info *document.CellInfo) {
    if info.Row == 0 {
        info.Cell.SetBackgroundColor("E6F3FF")
    }
})
```

### 模板功能

支持模板继承，可以定义基础模板然后扩展：

```go
baseTemplate := `{{companyName}} 报告
{{#block "content"}}默认内容{{/block}}`

salesTemplate := `{{extends "base"}}
{{#block "content"}}
销售额：{{sales}}
新客户：{{customers}}
{{/block}}`
```

### 高级功能

*   页眉页脚、目录生成
*   脚注尾注、列表编号
*   页面设置（ A4 、Letter 等）
*   图片插入

## 性能表现

做了个简单的基准测试，生成同样的文档：

*   **Go (WordZero)**: 2.62ms
*   JavaScript: 9.63ms
*   Python: 55.98ms

Go 确实快不少。

## 使用体验

API 设计比较直观，支持链式调用：

```go
doc := document.New()

doc.AddParagraph("标题").
    SetStyle(style.StyleHeading1).
    SetAlignment(document.AlignmentCenter)

doc.AddParagraph("正文内容").
    SetFontFamily("微软雅黑").
    SetFontSize(12).
    SetColor("333333")

doc.Save("report.docx")
```

## 项目地址

GitHub: [https://github.com/ZeroHawkeye/wordZero](https://github.com/ZeroHawkeye/wordZero)

Gitee: [https://gitee.com/Zmata\_admin/WordZero](https://gitee.com/Zmata_admin/WordZero)

有详细的文档和示例，examples 目录下有各种使用场景的 demo 。

## 适用场景

*   报表生成系统
*   合同文档批量生成
*   数据导出为 Word 格式
*   文档模板填充
*   自动化办公

目前还在持续更新中，如果有需求或者 bug 欢迎提 issue 。

***

_纯 Go 实现，零依赖，开箱即用。如果对你有帮助记得给个 star ⭐_

## 参考

- [v2ex](https://www.v2ex.com/t/1135912)
- GitHub: https://github.com/ZeroHawkeye/wordZero
- Gitee: https://gitee.com/Zmata_admin/WordZero

---
## 评论

17 条回复 \*\*•\*\*2025-06-03 11:38:32 +08:00

![Image 4: wangritian](https://cdn.v2ex.com/avatar/acd6/85e6/497030_normal.png?m=1711472308)1

\*\*[wangritian](https://www.v2ex.com/member/wangritian)\*\*2 小时 23 分钟前

go 确实没有好用的开源 word 操作库，之前是 kotlin 接 apache 那套然后用 cgo 调用 jar 曲线救国的，star 支持一下

![Image 5: jazzychai](https://cdn.v2ex.com/avatar/e71d/b23f/168706_normal.png?m=1516760029)2

\*\*[jazzychai](https://www.v2ex.com/member/jazzychai)\*\*2 小时 9 分钟前

star 了，刚好要做一个 word 相关的功能，本来想用 Python 曲线救国，试一下能不能满足业务需求

![Image 6: sholmesian](https://cdn.v2ex.com/avatar/3257/7ef0/63808_normal.png?m=1495522856)3

\*\*[sholmesian](https://www.v2ex.com/member/sholmesian)\*\*2 小时 7 分钟前 via iPhone

这个正需要，已 start.

![Image 7: icinessz](https://cdn.v2ex.com/gravatar/67de0ce8245ba03fa958d259f4d641e5?s=48&d=retro)4

\*\*[icinessz](https://www.v2ex.com/member/icinessz)\*\*1 小时 56 分钟前

太感谢了，一直在找类似的库

![Image 8: tuimaochang](https://cdn.v2ex.com/gravatar/ee0f162bbf983f37ab6f3d6cb4a46f66?s=48&d=retro)5

\*\*[tuimaochang](https://www.v2ex.com/member/tuimaochang)\*\*1 小时 35 分钟前

大佬牛逼！

![Image 9: body007](https://cdn.v2ex.com/avatar/3380/9f1c/616616_normal.png?m=1739862442)6

\*\*[body007](https://www.v2ex.com/member/body007)\*\*1 小时 28 分钟前

为大佬点赞。

![Image 10: bronyakaka](https://cdn.v2ex.com/avatar/4bc4/38c9/676530_normal.png?m=1735389040)7

\*\*[bronyakaka](https://www.v2ex.com/member/bronyakaka)\*\*1 小时 25 分钟前

很不错，很实用

![Image 11: moell](https://cdn.v2ex.com/avatar/1205/9742/192194_normal.png?m=1738904748)8

\*\*[moell](https://www.v2ex.com/member/moell)\*\*1 小时 24 分钟前

已 star

![Image 12: 676529483](https://cdn.v2ex.com/avatar/e129/50d6/352970_normal.png?m=1674873037)9

\*\*[676529483](https://www.v2ex.com/member/676529483)\*\*1 小时 18 分钟前![Image 13: ❤️](https://www.v2ex.com/static/img/heart_neue_red.png?v=16ec2dd0a880be6edda1e4a2e35754b3) 1

支持下，以前有个项目要用 xls ，go 只支持 xlsx ，最后只能 Python 曲线救国了

![Image 14: caotian](https://cdn.v2ex.com/gravatar/3714e83484ebd70b56ed11d2df86323a?s=48&d=retro)10

\*\*[caotian](https://www.v2ex.com/member/caotian)\*\*1 小时 17 分钟前

已 start, 有没有图表支持? 如果有的话, 就可以换掉 poi-tl 那套了, 那个库报了 Vulnerability 一直不更新修复, 快不敢用了.

![Image 15: dbskcnc](https://cdn.v2ex.com/avatar/144c/f058/230943_normal.png?m=1659945817)11

\*\*[dbskcnc](https://www.v2ex.com/member/dbskcnc)\*\*1 小时 10 分钟前

虽然基本不用 word,不过还是支持

![Image 16: shengxiadiaoling](https://cdn.v2ex.com/avatar/3bf5/8d86/676336_normal.png?m=1734587217)12

\*\*[shengxiadiaoling](https://www.v2ex.com/member/shengxiadiaoling)\*\*52 分钟前

牛

![Image 17: vfs](https://cdn.v2ex.com/avatar/ec20/25a5/583944_normal.png?m=1728985857)13

\*\*[vfs](https://www.v2ex.com/member/vfs)\*\*34 分钟前

目前还没有需求，但是很赞

![Image 18: Reficul](https://cdn.v2ex.com/avatar/8793/f1f9/65092_normal.png?m=1419262431)14

\*\*[Reficul](https://www.v2ex.com/member/Reficul)\*\*12 分钟前

@[wangritian](https://www.v2ex.com/member/wangritian)

你这个转接的有点 6 啊。 kotlin -> jvm -> cgo -> go

![Image 19: clow](https://cdn.v2ex.com/gravatar/d6e36067c8461c96e0ea78d9421ae78c?s=48&d=retro)15

@[caotian](https://www.v2ex.com/member/caotian) 多谢支持，图表还没实现，加到 todo 里了

![Image 20: clow](https://cdn.v2ex.com/gravatar/d6e36067c8461c96e0ea78d9421ae78c?s=48&d=retro)16

**[clow](https://www.v2ex.com/member/clow)**

@[dbskcnc](https://www.v2ex.com/member/dbskcnc) 多谢支持~

![Image 21: lexno](https://cdn.v2ex.com/gravatar/7a4abac3f161e701fde7f416d420e6fd?s=48&d=retro)17

\*\*[lexno](https://www.v2ex.com/member/lexno)

支不支持已有的 word 模板，然后使用这个模板来生成数据，我看现有的示例好像都是用库本身产生一个 document ，然后再进行模板填充？
