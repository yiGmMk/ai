---
title: "OpenAI Codex：AI编程新纪元，效率提升10倍！"
date: "2025-05-17"
tags: ["OpenAI", "Codex", "AI编程", "智能体", "软件开发"]
categories: ["人工智能", "Codex", "编程"]
description: "OpenAI发布云端AI编程智能体Codex，标志着AI编程新时代的到来。"
author: "新智元"
image: ""
---

**核心内容:**

- OpenAI发布了名为Codex的云端AI编程智能体，它基于新模型codex-1，专为软件工程打造。
- Codex能够快速构建功能模块、解答代码库问题、修复代码漏洞、提交PR和自动执行测试验证，极大地提高了开发效率。
- Codex已向ChatGPT Pro、Enterprise和Team用户开放，通过与GitHub集成，重塑软件开发的底层逻辑。

**源自** | 新智元

从今天起，AI编程正式开启新时代！

刚刚，Greg Brockman带队与OpenAI六人团队开启线上直播，震撼发布了一款云端AI编程智能体——Codex。

用奥特曼的话来说就是，一个人就能打造无数爆款应用的时代来了！

![](https://ai.programnotes.cn/img/ai/2037d4785feed998a79b6071df469077.png)

![](https://ai.programnotes.cn/img/ai/336688d58fb78f9f69402c25017b281b.png)

Codex由新模型codex-1加持，这是o3的一个特调版本，专为软件工程量身打造。

它不仅能在云端沙盒环境中安全地并行处理多项任务，而且通过与GitHub无缝集成，还可以直接调用你的代码库。

它不仅仅是一款工具，更是一位「10x工程师」，能够同时做到：
- 快速构建功能模块

- 深入解答代码库问题

- 精准修复代码漏洞

- 提交PR

- 自动执行测试验证

过去，这些任务或许耗费开发者数小时乃至数日，如今Codex最多在30分钟内高效完成。

![](https://ai.programnotes.cn/img/ai/1f93e10714f7bbae5d315e3894fc98fb.png)

点击ChatGPT侧边栏，输入提示后，直接点击「代码」分配任务，或「提问」咨询代码库相关问题

通过强化学习，Codex基于真实世界的编码任务和多样化环境训练，生成的代码不仅符合人类偏好，还能无缝融入标准工作流。

基准测试显示，codex-1在SWE-bench上拿下72.1%的高分，一举击败了Claude 3.7以及o3-high。

![](https://ai.programnotes.cn/img/ai/85fe928217eabf0c28c89a7479d7d633.png)

从今天起，Codex将向全球ChatGPT Pro、Enterprise和Team用户正式开放，Plus和Edu用户很快就能上手了。

![](https://ai.programnotes.cn/img/ai/bd3ece4e66e4a27bdef3aba77cef652d.png)

可以说，AI编程智能体Codex的横空出世，或将重塑软件开发的底层逻辑，彻底点燃了编程革命的火种。

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**Codex多任务并行，AI编程超级加速器**

早在2021年，OpenAI首次发布了CodeX模型，开启了「氛围编程」（vibe coding）的时代。

这种编程方式让开发者与AI协同工作，代码生产变得更加直观、高效。

几周前，OpenAI又推出了CodeX CLI，一款可在本地终端运行的智能体。

但这只是开始！

OpenAI今天推出全新的Codex智能体，再次将软件工程推向一个全新的高度。

接下来，一睹Codex编码的惊艳表现吧。

连接GitHub账户后，OpenAI研究员Thibault Sottiaux选择了一个开源仓库preparedness repo。

![](https://ai.programnotes.cn/img/ai/3b5d05903595fd8eca1c3130d58fd661.png)

然后，他收到了三个任务：
- 第一个是提问：让代码智能体Codex解释代码库，说明整体结构

- 第二个是代码任务：要求在代码库中查找并修复某个地方bug

- 第三个任务是提问：遍历代码库，主动提出自己可以执行的任务建议

![](https://ai.programnotes.cn/img/ai/e8fbff717118142cd7e4a158e0abeab9.png)

接下来演示中，Thibault向Codex下达多个任务，比如拼写和语法纠错、智能任务委派、多仓库适配。

在纠错方面，他故意在指令中加入拼写错误，Codex不仅理解了意图，还主动找出了代码库中的拼写和语法问题并修复，细致到令人惊叹。

![](https://ai.programnotes.cn/img/ai/379f8918bcfff0abc578d50d48412a1f.gif)

当Thibault提出希望代码库「易维护、无bug」的目标时，Codex遍历代码库后，主动发现了可变默认值、不一致的超时设置等问题，并自行生成了修复任务。

这种「自我委派」能力，堪称智能体的巅峰表现。
<table><tbody><tr><td><section nodeleaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.75em;letter-spacing: 0.034em;font-style: normal;font-weight: normal;text-align: justify;margin-left: 8px;margin-right: 8px;"><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3Sl5NOWt2DufctLfibB2O8wibyicTksNl4QFB1U4OWVibxsnFd8pqSUXs4kRtXgjFHJZnZpiaXFUW0k9g/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5623283909939594" data-type="png" data-w="1821" style="width:100%;" data-width="1821" data-height="1024" data-backw="252" data-backh="142" data-imgfileid="505110819"/></section></td><td><section nodeleaf="" style="color: rgba(0, 0, 0, 0.9);font-size: 17px;font-family: mp-quote, -apple-system-font, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;line-height: 1.75em;letter-spacing: 0.034em;font-style: normal;font-weight: normal;text-align: justify;margin-left: 8px;margin-right: 8px;"><img data-src="https://mmbiz.qpic.cn/sz_mmbiz_png/UicQ7HgWiaUb3Sl5NOWt2DufctLfibB2O8wAJBWYxZoRiaPoyhKvjBzADGH5jNQQSzwV3bb7M2fU0SdpvGh34GlIhQ/640?wx_fmt=png&amp;from=appmsg" class="rich_pages wxw-img" data-ratio="0.5623283909939594" data-type="png" data-w="1821" style="width:100%;" data-width="1821" data-height="1024" data-backw="252" data-backh="142" data-imgfileid="505110822"/></section></td></tr></tbody></table>
值得注意的是，Codex智能体运行在OpenAI计算基础设施上，与强化学习共享同一套久经考验的系统。

每个任务都在独立的虚拟沙盒中运行，配备专属的文件系统、CPU、内存、和网络策略，确保了高效安全。

![](https://ai.programnotes.cn/img/ai/821869441b9b50e3cff29bd9363d8db8.png)

除了preparedness仓库，Codex还无缝处理了CodeX CLI库，展现其在不同项目中的泛化能力。

不论是开源项目，还是内部代码库，Codex都游刃有余。

Codex接收到了用户反馈的bug，因为特殊字符文件名导致了diff命令报错。

![](https://ai.programnotes.cn/img/ai/08f69639b4e3f378dac4f2de5676fd75.png)

在解决过程中，它不仅能复现问题，还可以编写测试脚本、运行linter检查，并生成PR，整个过程仅需几分钟。

Thibault直言，「这原本可能花费我30分钟，甚至几个小时完成」。

![](https://ai.programnotes.cn/img/ai/6d767657d032a5ea0de50ca2a6d06f5e.gif)

此外，OpenAI研究员Katy Shi演示中强调，Codex的PR包含了详细的摘要，清晰说明了修改内容和引用的代码，测试结果一目了然。

![](https://ai.programnotes.cn/img/ai/0f62ef024c7461950cbbbda12151697b.gif)

一番演示下来，Greg表示，Codex让自己深刻感受到了AGI！

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**对齐人类偏好**

**实战4个开源库**

OpenAI训练codex-1的一个主要目标，是确保其输出能高度符合人类的编码偏好与标准。

与OpenAI o3相比，codex-1能稳定生成更为简洁的代码修改补丁，可以直接供人工审查并集成到标准工作流程中。

为了体现Codex生成代码的简洁和高效，OpenAI提供了Codex和o3对比的4个开源库实战实例：

****
**astropy**

astropy是一个用于天文学的Python开源库。

![](https://ai.programnotes.cn/img/ai/daab422c6682826b050d9824ac20a2eb.png)

第一个问题是astropy/astropy的仓库中，Modeling模块中的separability_matrix无法正确计算嵌套CompoundModels的可分离性。

![](https://ai.programnotes.cn/img/ai/1a956d0b5264196492bb990d64cd899e.png)

可以看到，在修改前后的代码版本对比中，使用Codex修改生成了十分简洁的代码。

相比之下，o3修改的代码就显得有些冗长了，甚至还将一些「不必要」的注释加入了源代码中。

![](https://ai.programnotes.cn/img/ai/23bae2f1449d99a4ccfd809884a2c021.png)

****
**matplotlib**

****
Matplotlib是一个用于创建静态、动画和交互式可视化的Python综合性库。

![](https://ai.programnotes.cn/img/ai/3d9e53f48fa71a04d1f61d4e68ac471a.png)

这次问题是修复Bug：在mlab._spectral_helper中的窗口校正（windows correction）不正确。

![](https://ai.programnotes.cn/img/ai/69c53e7140b58f88573396c85d2553f1.png)

同样可以看到，Codex修改代码的过程更为简洁。

![](https://ai.programnotes.cn/img/ai/4c58ec904cdd0cbcda660bf9dcc1f645.png)

****
**django**

****
Django是基于Python的Web框架，这个问题是修复仅包含duration（时长）的表达式在SQLite和MySQL上无法正常工作。

![](https://ai.programnotes.cn/img/ai/669e53c526f99afde097897aa1cef4d0.png)

Codex的修复过程依然优雅，并且相比o3，还首先补上了缺少的依赖调用。

![](https://ai.programnotes.cn/img/ai/3432c9a8feb51a1acf71ccbd703e5fc6.png)

****
**expensify**

****
expensify是一个围绕聊天的财务协作的开源软件。

![](https://ai.programnotes.cn/img/ai/2a2fdd9c3734899b4958a803f589047b.png)

OpenAI给出的问题是「dd [HOLD for payment 2024-10-14] [$250] LHN - 删除缓存后，成员聊天室名称在LHN中未更新」。

![](https://ai.programnotes.cn/img/ai/7df3d1cb56b85d6b560fcffea6ee130b.png)

同样可以看到Codex的问题定位和修改更为精准和有效，o3甚至进行了一次无效的代码的修改。

![](https://ai.programnotes.cn/img/ai/fe5e099f579fbdd0de85e9bc2cfeba41.png)

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**OpenAI团队已经用上了**

OpenAI的技术团队已经开始将Codex作为他们日常工具包的一部分。

OpenAI的工程师最常使用Codex来执行重复且范围明确的任务，如重构、重命名和编写测试，这些任务会打断他们的专注。

它同样适用于搭建新功能、连接组件、修复错误和起草文档。

团队正在围绕Codex建立新的习惯：处理值班问题、在一天开始时规划任务，以及执行后台工作以保持进度。

通过减少上下文切换和提醒被遗忘的待办事项，Codex帮助工程师更快地交付并专注于最重要的事情。

在正式发布前，OpenAI与少数外部测试者合作，评估Codex在不同代码库、开发流程与团队环境中的实际表现：
- **Cisco**
作为早期设计合作伙伴，探索Codex在加速工程团队构思落地方面的潜力，并通过评估真实用例向OpenAI提供反馈，助力模型优化。

- **Temporal**
借助Codex实现功能开发、问题调试、测试编写与执行的加速，并用于重构大型代码库。Codex还能在后台处理复杂任务，帮助工程师保持专注与高效迭代。

- **Superhuman**
利用Codex自动处理小型重复任务，如提高测试覆盖率和修复集成故障；还使产品经理能够无需工程介入（除代码审查外）完成轻量级代码更改，提升配对效率。

- **Kodiak**
在Codex支持下加速调试工具开发、测试覆盖和代码重构，推进其自动驾驶系统Kodiak Driver的研发。Codex也作为参考工具，帮助工程师理解陌生代码栈，提供相关上下文与历史更改。

根据目前的使用经验来看，OpenAI建议：可同时向多个代理分配边界清晰的任务，并尝试多种任务类型与提示方式，以更全面地发掘模型能力。

****
**模型系统消息**

****
通过以下系统消息，开发者可以了解codex-1的默认行为，并针对自己的工作流进行调整。

例如，系统消息会引导Codex运行AGENTS.md文件中提到的所有测试，但如果时间紧张，就可以要求Codex跳过这些测试。
```markdown
# Instructions
- The user will provide a task.
- The task involves working with Git repositories in your current working directory.
- Wait for all terminal commands to be completed (or terminate them) before finishing.

# Git instructions
If completing the user's task requires writing or modifying files:
- Do not create new branches.
- Use git to commit your changes.
- If pre-commit fails, fix issues and retry.
- Check git status to confirm your commit. You must leave your worktree in a clean state.
- Only committed code will be evaluated.
- Do not modify or amend existing commits.

# AGENTS.md spec
- Containers often contain AGENTS.md files. These files can appear anywhere in the container's filesystem. Typical locations include `/`, `~`, and in various places inside of Git repos.
- These files are a way for humans to give you (the agent) instructions or tips for working within the container.
- Some examples might be: coding conventions, info about how code is organized, or instructions for how to run or test code.
- AGENTS.md files may provide instructions about PR messages (messages attached to a GitHub Pull Request produced by the agent, describing the PR). These instructions should be respected.
- Instructions in AGENTS.md files:
  - The scope of an AGENTS.md file is the entire directory tree rooted at the folder that contains it.
  - For every file you touch in the final patch, you must obey instructions in any AGENTS.md file whose scope includes that file.
  - Instructions about code style, structure, naming, etc. apply only to code within the AGENTS.md file's scope, unless the file states otherwise.
  - More-deeply-nested AGENTS.md files take precedence in the case of conflicting instructions.
  - Direct system/developer/user instructions (as part of a prompt) take precedence over AGENTS.md instructions.
- AGENTS.md files need not live only in Git repos. For example, you may find one in your home directory.
- If the AGENTS.md includes programmatic checks to verify your work, you MUST run all of them and make a best effort to validate that the checks pass AFTER all code changes have been made.
  - This applies even for changes that appear simple, i.e. documentation. You still must run all of the programmatic checks.

# Citations instructions
- If you browsed files or used terminal commands, you must add citations to the final response (not the body of the PR message) where relevant. Citations reference file paths and terminal outputs with the following formats:
  1) `【F:<file_path>†L<line_start>(-L<line_end>)?】`
  - File path citations must start with `F:`. `file_path` is the exact file path of the file relative to the root of the repository that contains the relevant text.
  -`line_start` is the 1-indexed start line number of the relevant output within that file.
  2) `【<chunk_id>†L<line_start>(-L<line_end>)?】`
  - Where `chunk_id` is the chunk_id of the terminal output, `line_start` and `line_end` are the 1-indexed start and end line numbers of the relevant output within that chunk.
- Line ends are optional, and if not provided, line end is the same as line start, so only 1 line is cited.
- Ensure that the line numbers are correct, and that the cited file paths or terminal outputs are directly relevant to the word or clause before the citation.
- Do not cite completely empty lines inside the chunk, only cite lines that have content.
- Only cite from file paths and terminal outputs, DO NOT cite from previous pr diffs and comments, nor cite git hashes as chunk ids.
- Use file path citations that reference any code changes, documentation or files, and use terminal citations only for relevant terminal output.
- Prefer file citations over terminal citations unless the terminal output is directly relevant to the clauses before the citation, i.e. clauses on test results.
  - For PR creation tasks, use file citations when referring to code changes in the summary section of your final response, and terminal citations in the testing section.
  - For question-answering tasks, you should only use terminal citations if you need to programmatically verify an answer (i.e. counting lines of code). Otherwise, use file citations.
```

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**Codex CLI更新**

上个月，OpenAI推出了一款轻量级开源工具——**Codex****CLI**，可以让o3和o4-mini等强大模型直接运行在本地终端中，帮助开发者更快完成任务。

![](https://ai.programnotes.cn/img/ai/2d32ea3bf5bdccb523daf31dde21f7d1.png)

这一次，OpenAI同时发布了专为Codex CLI优化的小模型版本——**codex-1的o4-mini版本**。

它具备低延迟、强指令理解力和代码编辑能力，现已成为Codex CLI的默认模型，同时也可通过API使用（名称为codex-mini-latest），并将持续迭代更新。

此外，Codex CLI的登录方式也简化了，开发者现在可以直接用ChatGPT账户登录，选择API组织，系统将自动生成并配置API密钥。

为了鼓励使用，**从今天起30天内**，使用ChatGPT账户登录Codex CLI的用户将获得免费额度：Plus用户获得5美元API使用额度；Pro用户获得50美元。

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**Codex贵不贵**

在接下来的几周内，所有用户可以「量大管饱」的试用Codex功能。

随后，OpenAI将引入限流机制和灵活定价，支持按需购买额外使用量。

对于开发者，**codex-mini-latest**
模型已在Responses API上提供，价格为：
- 每百万输入Token：**$1.50**

- 每百万输出Token：**$6.00**

- 并享有75%的提示缓存折扣

Codex当前仍处于**研究预览阶段**
，尚不支持图像输入等前端能力，也暂不具备在任务执行中进行实时纠正的能力。

此外，委派任务给Codex智能体的响应时间较长，用户可能需要适应这类**异步协作**
的工作方式。

随着模型能力不断提升，Codex将能处理更复杂、更持久的开发任务，逐步成为更像「远程开发伙伴」的存在。

![](https://ai.programnotes.cn/img/ai/c607b49f375d419947251902fbf331cc.png)

**下一步是什么**

OpenAI的目标是开发者专注自己擅长的工作，其余任务交由AI代理处理，从而提升效率与生产力。

Codex将支持**实时协作**与**异步任务委托**，两种工作模式将逐步融合。

Codex CLI等工具已经成为开发者加速编码的标配，而由ChatGPT中的Codex引领的异步、多智能体协作流程，有望成为工程师高效产出高质量代码的新范式。

未来，开发者将能在IDE和日常工具中与AI协同工作——提问、获取建议、委派复杂任务，所有操作整合在一个统一的工作流程中。

OpenAI计划进一步提升交互性和灵活性：
- 支持任务中途提供指导

- 与AI协作实施策略

- 接收主动进度更新

- 与常用工具（如GitHub、CLI、问题跟踪器、CI系统）深度集成，便捷分配任务

![](https://ai.programnotes.cn/img/ai/8ee3370731074037f0184f0d58cd1f99.png)

软件工程正成为首批因AI而大幅提效的行业之一，将全面释放个人与小团队的巨大潜力。

与此同时，OpenAI也正与合作伙伴共同研究智能体的广泛应用将如何影响开发流程、技能发展和全球人才分布。

参考资料：

https://www.youtube.com/watch?v=hhdpnbfH6NU

https://openai.com/index/introducing-codex/

