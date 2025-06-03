---
title: "Cline Rules"
date: "2025-06-03"
tags: ["cline", "rules", "configuration", "best practices"]
categories: ["Documentation", "Configuration"]
Description: "了解如何使用 Cline 规则为 Cline 提供系统级指导，确保一致的行为、项目特定标准，并在您的项目中维护机构知识。"
author: "YiGmMk"
image: ""
---

Cline 规则(Rules)允许你为 Cline 提供系统级别的指导。可以将它们看作是持久为你的项目或全局地为每次对话添加上下文和偏好的方式。

## 创建规则

你可以通过点击“Rules”选项卡中的“+”按钮来创建规则。这将在你的 IDE 中打开一个新文件，你可以使用它来编写你的规则。

![创建 Rules](https://ai.programnotes.cn/img/ai/mcp/cline-rules1.png)


一旦你保存了文件：

* 你的规则将被存储在你的项目中的 `.clinerules/` 目录中（如果它是一个工作区规则）。
* 或者在 `Documents/Cline/Rules` 目录中（如果它是一个全局规则）。

你也可以通过在聊天中使用 [`/newrule` 斜杠命令](https://docs.cline.bot/features/slash-commands/new-rule) 让 Cline 为你创建一个规则。

```markdown Example Cline Rule Structure [expandable]
# Project Guidelines

## Documentation Requirements

-   Update relevant documentation in /docs when modifying features
-   Keep README.md in sync with new capabilities
-   Maintain changelog entries in CHANGELOG.md

## Architecture Decision Records

Create ADRs in /docs/adr for:

-   Major dependency changes
-   Architectural pattern changes
-   New integration patterns
-   Database schema changes
    Follow template in /docs/adr/template.md

## Code Style & Patterns

-   Generate API clients using OpenAPI Generator
-   Use TypeScript axios template
-   Place generated code in /src/generated
-   Prefer composition over inheritance
-   Use repository pattern for data access
-   Follow error handling pattern in /src/utils/errors.ts

## Testing Standards

-   Unit tests required for business logic
-   Integration tests for API endpoints
-   E2E tests for critical user flows
```

### 主要优势

1. **版本控制**：`.clinerules` 文件成为项目源代码的一部分
2. **团队一致性**：确保所有团队成员行为一致
3. **项目特定**：规则和标准根据每个项目的需求量身定制
4. **机构知识**：在代码中维护项目标准和实践

将 `.clinerules` 文件放置在项目的根目录中：

```bash
your-project/
├── .clinerules
├── src/
├── docs/
└── ...
```

Cline的系统提示词是不可由用户编辑的（[点击此处查看](https://github.com/cline/cline/blob/main/src/core/prompts/system.ts)）。如需更广泛地了解提示词工程的最佳实践，请查看[此资源](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)。

### 编写有效Cline规则的技巧

*   清晰简洁：使用简单的语言，避免歧义。
*   关注期望结果：描述你想要的结果，而不是具体的步骤。
*   测试和迭代：通过实验找到最适合你工作流程的方法。

### .clinerules/ 文件夹系统

```bash
your-project/
├── .clinerules/              # Folder containing active rules
│   ├── 01-coding.md          # Core coding standards
│   ├── 02-documentation.md   # Documentation requirements
│   └── current-sprint.md     # Rules specific to current work
├── src/
└── ...
```

Cline 会自动处理 `.clinerules/` 目录下的**所有 Markdown 文件**，并将它们合并成一套统一的规则。数字前缀（可选）有助于以逻辑顺序组织文件。

#### 使用规则库

对于具有多个上下文或团队的项目，请维护一个规则库目录：

```bash
your-project/
├── .clinerules/              # Active rules - automatically applied
│   ├── 01-coding.md
│   └── client-a.md
│
├── clinerules-bank/          # Repository of available but inactive rules
│   ├── clients/              # Client-specific rule sets
│   │   ├── client-a.md
│   │   └── client-b.md
│   ├── frameworks/           # Framework-specific rules
│   │   ├── react.md
│   │   └── vue.md
│   └── project-types/        # Project type standards
│       ├── api-service.md
│       └── frontend-app.md
└── ...
```

文件夹方法的益处：

1. **情境激活**：仅从规则库复制相关规则到活动文件夹。
2. **更易维护**：更新单个规则文件，不影响其他文件。
3. **团队灵活性**：不同的团队成员可以激活特定于其当前任务的规则。
4. **减少干扰**：保持活动规则集的专注性和相关性。

使用示例：

在客户项目之间切换：

```bash
# Switch to Client B project
rm .clinerules/client-a.md
cp clinerules-bank/clients/client-b.md .clinerules/
```

适应不同的技术栈：

```bash
# Frontend React project
cp clinerules-bank/frameworks/react.md .clinerules/
```

#### 实施技巧

* 保持单个规则文件专注于特定的问题
* 使用描述性的文件名，清楚地表明规则的用途
* 考虑在跟踪 `clinerules-bank/` 的同时，git 忽略活动的 `.clinerules/` 文件夹
* 创建团队脚本以快速激活常见的规则组合

文件夹系统将您的 Cline 规则从静态文档转换为动态知识系统，该系统可以适应您团队不断变化的环境和需求。

### Managing Rules with the Toggleable Popover

为了更轻松地管理单个 `.clinerules` 文件和文件夹系统，Cline v3.13 引入了一个专用的弹出窗口 UI，可以直接从聊天界面访问。

这个弹出窗口位于聊天输入框下方，方便您：

* **即时查看活动规则：** 查看当前活动的全局规则（来自您的用户设置）和工作区规则（`.clinerules` 文件或文件夹内容）。
* **快速切换规则：** 只需单击一下，即可启用或禁用工作区 `.clinerules/` 文件夹中的特定规则文件。这非常适合仅在需要时激活上下文相关的规则（如 `react-rules.md` 或 `memory-bank.md`）。
* **轻松添加/管理规则：** 如果工作区中不存在 `.clinerules` 文件或文件夹，则可以快速创建；或者向现有文件夹添加新的规则文件。

此 UI 极大地简化了上下文切换和管理不同指令集的过程，无需在对话期间手动编辑文件或配置。

![Rules](https://ai.programnotes.cn/img/ai/mcp/cline-rules2.png)
