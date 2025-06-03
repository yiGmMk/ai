---
title: "译|Cline Workflows"
date: "2025-06-03"
tags: ["workflows", "Cline", "automation"]
categories: ["development", "automation"]
description: "Learn how to create and use workflows in Cline to automate repetitive tasks."
author: "YiGmMk"
image: ""
---

- 工作流(Workflows)允许你定义一系列步骤，以指导 Cline 完成重复性任务。
- 工作流与 Cline Rules 共存。
- 工作流的优点在于它们可以完全根据你的需求进行定制。

工作流(Workflows)允许你定义一系列步骤，以指导 Cline 完成一系列重复性任务，例如部署服务或提交 PR。

要在聊天中调用工作流，输入 `/[workflow-name.md]`。

## 如何创建和使用工作流

工作流与 [Cline 规则](https://docs.cline.bot/features/cline-rules) 并存。 创建一个工作流非常简单：

在 Cline 中使用工作流

![Cline 中的工作流标签页](https://ai.programnotes.cn/img/ai/mcp/workflow.png)

1. 创建一个 Markdown 文件，其中包含 Cline 应该采取的步骤的清晰说明。
2. 将其保存为 `.md` 扩展名，并放在您的工作流目录中。
3. 要触发一个工作流，只需键入 `/`，然后输入工作流文件名。
4. 按照提示提供任何必需的参数。

真正的强大之处在于您如何构建您的工作流文件。您可以：

* 利用 Cline 的[内置工具](https://docs.cline.bot/exploring-clines-tools/cline-tools-guide)，例如 `ask_followup_question`、`read_file`、`search_files` 和 `new_task`。
* 使用您已经安装的命令行工具，例如 `gh` 或 `docker`。
* 引用外部 [MCP 工具调用](https://docs.cline.bot/mcp/mcp-overview)，例如 Slack 或 Whatsapp。
* 将多个操作按特定顺序链接在一起。

## 真实世界的例子

I have created a PR Review workflow that is already saving me a lot of time.评估PR的Workflow

````md pr-review.md [expandable]
You have access to the `gh` terminal command. I already authenticated it for you. Please review it to use the PR that I asked you to review. You're already in the `cline` repo.

<detailed_sequence_of_steps>

# GitHub PR Review Process - Detailed Sequence of Steps

## 1. Gather PR Information

1. Get the PR title, description, and comments:

    ```bash
    gh pr view <PR-number> --json title,body,comments
    ```

2. Get the full diff of the PR:
    ```bash
    gh pr diff <PR-number>
    ```

## 2. Understand the Context

1. Identify which files were modified in the PR:

    ```bash
    gh pr view <PR-number> --json files
    ```

2. Examine the original files in the main branch to understand the context:

    ```xml
    <read_file>
    <path>path/to/file</path>
    </read_file>
    ```

3. For specific sections of a file, you can use search_files:
    ```xml
    <search_files>
    <path>path/to/directory</path>
    <regex>search term</regex>
    <file_pattern>*.ts</file_pattern>
    </search_files>
    ```

## 3. Analyze the Changes

1. For each modified file, understand:

    - What was changed
    - Why it was changed (based on PR description)
    - How it affects the codebase
    - Potential side effects

2. Look for:
    - Code quality issues
    - Potential bugs
    - Performance implications
    - Security concerns
    - Test coverage

## 4. Ask for User Confirmation

1. Before making a decision, ask the user if you should approve the PR, providing your assessment and justification:

    ```xml
    <ask_followup_question>
    <question>Based on my review of PR #<PR-number>, I recommend [approving/requesting changes]. Here's my justification:

    [Detailed justification with key points about the PR quality, implementation, and any concerns]

    Would you like me to proceed with this recommendation?</question>
    <options>["Yes, approve the PR", "Yes, request changes", "No, I'd like to discuss further"]</options>
    </ask_followup_question>
    ```

## 5. Ask if User Wants a Comment Drafted

1. After the user decides on approval/rejection, ask if they would like a comment drafted:

    ```xml
    <ask_followup_question>
    <question>Would you like me to draft a comment for this PR that you can copy and paste?</question>
    <options>["Yes, please draft a comment", "No, I'll handle the comment myself"]</options>
    </ask_followup_question>
    ```

2. If the user wants a comment drafted, provide a well-structured comment they can copy:

    ```
    Thank you for this PR! Here's my assessment:

    [Detailed assessment with key points about the PR quality, implementation, and any suggestions]

    [Include specific feedback on code quality, functionality, and testing]
    ```

## 6. Make a Decision

1. Approve the PR if it meets quality standards:

    ```bash
    # For single-line comments:
    gh pr review <PR-number> --approve --body "Your approval message"

    # For multi-line comments with proper whitespace formatting:
    cat << EOF | gh pr review <PR-number> --approve --body-file -
    Thanks @username for this PR! The implementation looks good.

    I particularly like how you've handled X and Y.

    Great work!
    EOF
    ```

2. Request changes if improvements are needed:

    ```bash
    # For single-line comments:
    gh pr review <PR-number> --request-changes --body "Your feedback message"

    # For multi-line comments with proper whitespace formatting:
    cat << EOF | gh pr review <PR-number> --request-changes --body-file -
    Thanks @username for this PR!

    The implementation looks promising, but there are a few things to address:

    1. Issue one
    2. Issue two

    Please make these changes and we can merge this.
    EOF
```

当我收到一个新的PR需要审查时，过去我总是手动收集上下文：查看PR描述、检查代码差异、浏览相关文件，最后形成自己的意见。现在我只需：

- 在聊天中输入 /pr-review.md
- 粘贴PR编号
- 让Cline自动处理其余所有工作

我的工作流使用了gh命令行工具和Cline内置的ask_followup_question功能，可以：

- 提取PR描述和评论
- 检查代码差异
- 浏览相关文件获取上下文
- 分析潜在问题
- 询问我是否可以批准该PR（如果一切看起来没问题），并给出批准的理由
- 如果我回复"是"，Cline就会通过gh命令自动批准该PR

这将我的PR审查流程从繁琐的手动多步骤操作转变为只需一个命令就能获取所有必要信息的高效方式。

这只是一个工作流文件的示例。你可以在我们的[提示仓库](https://github.com/cline/prompts)中找到更多灵感。

## 构建你自己的工作流

工作流的最大优势在于它们可以完全根据你的需求进行定制。你可以为各种重复性任务创建工作流：

- 对于版本发布，可以创建一个工作流来获取所有已合并的PR，生成变更日志并处理版本号升级
- 项目初始化非常适合工作流。只需运行一个命令就能创建文件夹结构、安装依赖并配置相关设置
- 需要生成报告？创建一个工作流从不同来源抓取数据并按你喜欢的格式呈现。你甚至可以用图表库可视化数据，再通过slidev等工具生成演示文稿
- 你还可以用工作流在提交PR后，通过Slack或WhatsApp等MCP服务器自动起草团队消息

有了工作流，你的想象力就是唯一的限制。真正的价值在于发现那些日常重复的繁琐任务。

如果你能描述为"首先我做X，然后做Y，最后做Z"这样的流程，那它就非常适合作为工作流的候选方案。

从让你感到困扰的小任务开始，将其转化为工作流，然后不断优化。你会惊讶于这种方式能自动化你一天中多少工作时间。

## 原文

- https://docs.cline.bot/features/slash-commands/workflows#how-to-create-and-use-workflows