---
title: "多个Go版本切换"
date: 2025-06-11T07:47:00+08:00
draft: false
tags: ["Go"]
categories: ["Go"]
---

该文档描述了当你的系统上安装了多个 Go 版本时，如何在这些版本之间进行切换。

预备条件：

- 安装了多个 Go 版本（例如，go1.22，go1.24）

## 步骤

1.  **确定你的 Go 版本的安装路径。**

    例如：

    -   go1.22: `/usr/lib/go-1.22`
    -   go1.24: `/home/xxx/sdk/go1.24.4`

2. 修改您的 shell 配置文件。

Shell 配置文件取决于您正在使用的 shell。 例如：

- Bash：`~/.bashrc` 或 `~/.bash_profile`
- Zsh：`~/.zshrc`
- Fish：`~/.config/fish/config.fish`

设置环境变量: `GOROOT` 和 `PATH` 

Fish shell，请使用：

    ```fish
    set -gx GOROOT /path/to/go/version
    set -gx PATH $GOROOT/bin $PATH
    ```

在 Fish shell 中切换到 go1.24 版本，可以将以下代码添加到 `~/.config/fish/config.fish` 文件中：

```fish
set -gx GOROOT /home/xxx/sdk/go1.24.4
set -gx PATH /home/xxx/sdk/go1.24.4/bin $PATH
```

重新加载 Shell 配置。

运行以下命令来重新加载你的 Shell 配置：

```bash
source ~/.bashrc  # 适用于 Bash
source ~/.zshrc  # 适用于 Zsh
source ~/.config/fish/config.fish  # 适用于 Fish
```

5. **验证 Go 版本。**

   运行以下命令来验证您是否已成功切换到所需的 Go 版本：

   ```bash
   go version
   ```

   输出应显示您选择的 Go 版本。

要切换到 Fish shell 中的 go1.24 版本，请按照以下步骤操作：

1. 编辑 `~/.config/fish/config.fish` 文件

2. 执行 `source ~/.config/fish/config.fish` 重新加载配置

3. 执行 `go version` 验证切换成功
