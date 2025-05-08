---
title: "Introducing MCP-Scan: Protecting MCP with Invariant"
date: "2025-05-08"
tags: ["MCP", "security", "scanner", "vulnerabilities", "tool poisoning"]
categories: ["security","MCP", "AI"]
description: "MCP-Scan is a security scanner designed to protect agentic systems from MCP-based security vulnerabilities."
author: "Luca Beurer-Kellner, Marc Fischer"
image: ""
---

MCP-Scan, a security scanner designed to protect your agentic systems from MCP-based security vulnerabilities, including Tool Poisoning Attacks and MCP Rug Pulls.

[Repository](https://github.com/invariantlabs-ai/mcp-scan)

![Image 4: MCP-Scan](https://invariantlabs.ai/images/mcp-scan-launch.svg)

Invariant is excited to announce [**MCP-Scan**](https://github.com/invariantlabs-ai/mcp-scan), a novel security scanning tool designed specifically to protect agentic AI systems from security vulnerabilities when using the Model Context Protocol (MCP).

## Why MCP-Scan?

As recent research uncovered ([Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), [WhatsApp MCP Exploits](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)), MCP implementations across various platforms—such as Cursor, Claude Desktop, Zapier, and others—are susceptible to dangerous attacks. These vulnerabilities include prompt injections, hidden malicious tool instructions (Tool Poisoning Attacks), and cross-origin escalations through tool shadowing.

Recognizing these serious security threats, we developed **MCP-Scan** to help users quickly identify vulnerabilities within their MCP installations, ensuring safer and more secure agent interactions.

**Concerned about MCP and agent security?**  
Sign up for early access to Invariant Guardrails, our security platform that goes beyond just scanning, covering many attack vectors and security issues, including MCP attacks. [Learn More](https://invariantlabs.ai/guardrails)

## How MCP-Scan Protects Your Systems

MCP-Scan proactively scans installed MCP servers and their tool descriptions to identify:

*   **Tool Poisoning Attacks:** Hidden malicious instructions embedded in MCP tool descriptions.
*   **MCP Rug Pulls:** Unauthorized changes to MCP tool descriptions after initial user approval.
*   **Cross-Origin Escalations:** Shadowing attacks that compromise trusted tools through malicious descriptions.
*   **Prompt Injection Attacks:** Malicious instructions contained within tool descriptions that could be executed by the agent.

## Quick and Easy Security Checks

MCP-Scan seamlessly integrates into your workflow and can be run with a simple command. No configuration is required.

```sh
uvx mcp-scan@latest
```

The tool scans through your MCP configuration files, connecting to servers and retrieving tool descriptions, analyzing them locally and using the Invariant Guardrails API to identify malicious instructions.

To run this command, make sure you have the [`uv`](https://docs.astral.sh/uv/) package manager installed on your system.

This will load the latest source and dependencies from PyPI, if you would rather run from source, check out the [GitHub repository](https://github.com/invariantlabs-ai/mcp-scan).

## Example Scan Result

Here's an example of MCP-Scan in action, clearly identifying a vulnerable MCP tool:

![Image 5: MCP-Scan Example](https://invariantlabs.ai/images/mcp-scan-output.png)

In this example, MCP-Scan detects security risks, including prompt injections in the tool descriptions. Once identified, you can use `uvx mcp-scan@latest inspect` to view the relevant tool descriptions and take action.

## Enhanced Security through Tool Pinning

MCP-Scan includes built-in **Tool Pinning** to detect and prevent MCP Rug Pull attacks, verifying the integrity of installed tools by tracking changes via tool hashing. This allows users to detect changes to tool descriptions.

## Cross-Origin Escalation Detection

MCP-Scan also identifies cross-origin escalation attacks or [tool shadowing](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), where a malicious tool description can shadow a trusted tool. This is particularly important for users who rely on multiple MCP servers.

To mitigate these attacks, MCP-Scan scans specifically for cross-references among different MCP servers, ensuring hardened isolation on an instruction level.

## Inspect Your Installed Tools

You can inspect detailed tool descriptions at any time using:

```sh
uvx mcp-scan@latestinspect
```

## Contributing and Community

MCP-Scan is open source, and we welcome your contributions, suggestions, and feature requests. Join our [Discord](https://discord.gg/dZuZfhKnJ4) or [GitHub](https://github.com/invariantlabs-ai/mcp-scan) to participate in securing the future of agentic systems.

## Data Privacy during Scanning

MCP-Scan searches through your configuration files to find MCP server configurations. It connects to these servers and retrieves tool descriptions. It does so only when explicitly called via its command.

It then scans tool descriptions, both with local checks and by invoking Invariant Guardrailing models via an API. For this, tool names and descriptions are shared with Invariant. By using MCP-Scan, you agree to the Invariant Labs [terms of use](https://explorer.invariantlabs.ai/terms) and [privacy policy](https://invariantlabs.ai/privacy-policy).

During scans, Invariant is collecting data for security research purposes (only about tool descriptions and how they change over time, not your user data). Do not use MCP-scan if you don't want to share your tool descriptions. If you are interested in dedicated or private deployments, please [reach out to us](mailto:mcpscan@invariantlabs.ai).

MCP-scan does not store or log any MCP usage data, i.e. the contents and results of your MCP tool calls.

## Getting Started

Protect your agentic AI systems from MCP security vulnerabilities today with MCP-Scan. Star the repository or contribute to the project on GitHub to help us improve MCP-Scan and make it even more effective in securing agentic systems.

[Try MCP-Scan Now](https://github.com/invariantlabs-ai/mcp-scan)

## About Invariant

Invariant is dedicated to ensuring the safety and robustness of agentic AI systems. Our research and tools address critical vulnerabilities, enabling the safe and secure deployment of AI in real-world scenarios. [Reach out](mailto:hello@invariantlabs.ai) if you are interested in collaborating with us to enhance the security and integrity of your agentic systems.

[invariantlabs,blog](https://invariantlabs.ai/blog)
