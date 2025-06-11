---
title: "Switching Go Versions"
date: 2025-06-11T07:47:00+08:00
draft: false
tags: ["Go"]
categories: ["Go"]
---

This document describes how to switch between different Go versions when you have multiple Go versions installed on your system.

## Prerequisites

- Multiple Go versions installed (e.g., go1.22, go1.24)

## Steps

1.  **Identify the installation paths of your Go versions.**

    For example:

    -   go1.22: `/usr/lib/go-1.22`
    -   go1.24: `/home/xxx/sdk/go1.24.4`

2.  **Modify your shell configuration file.**

    The shell configuration file depends on the shell you are using. For example:

    -   Bash: `~/.bashrc` or `~/.bash_profile`
    -   Zsh: `~/.zshrc`
    -   Fish: `~/.config/fish/config.fish`

3.  **Set the `GOROOT` and `PATH` environment variables.**

    Add the following lines to your shell configuration file, replacing the paths with the actual installation paths of your desired Go version:

    ```bash
    export GOROOT=/path/to/go/version
    export PATH=$GOROOT/bin:$PATH
    ```

    For Fish shell, use:

    ```fish
    set -gx GOROOT /path/to/go/version
    set -gx PATH $GOROOT/bin $PATH
    ```

    For example, to switch to go1.24 in Fish shell, add the following lines to `~/.config/fish/config.fish`:

    ```fish
    set -gx GOROOT /home/xxx/sdk/go1.24.4
    set -gx PATH /home/xxx/sdk/go1.24.4/bin $PATH
    ```

4.  **Reload your shell configuration.**

    Run the following command to reload your shell configuration:

    ```bash
    source ~/.bashrc  # For Bash
    source ~/.zshrc  # For Zsh
    source ~/.config/fish/config.fish  # For Fish
    ```

5.  **Verify the Go version.**

    Run the following command to verify that you have successfully switched to the desired Go version:

    ```bash
    go version
    ```

    The output should show the Go version you selected.

## Example

To switch to go1.24 in Fish shell, follow these steps:

1.  Edit `~/.config/fish/config.fish` and add the following lines:

    ```fish
    set -gx GOROOT /home/xxx/sdk/go1.24.4
    set -gx PATH /home/xxx/sdk/go1.24.4/bin $PATH
    ```

2.  Run `source ~/.config/fish/config.fish` to reload the shell configuration.

3.  Run `go version` to verify that you are using go1.24.4.
