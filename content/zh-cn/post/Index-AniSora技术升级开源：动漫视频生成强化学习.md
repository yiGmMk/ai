---
title: "Index-AniSora技术升级开源：动漫视频生成强化学习"
date: "2025-05-20"
tags: ["动漫视频生成", "强化学习", "开源", "AniSora", "B站"]
categories: ["人工智能", "计算机视觉"]
description: "B站开源Index-AniSora技术，利用强化学习提升动漫视频生成效率和质量。"
author: "Bwin、HarryJ、高树、seasonyang"
image: "https://ai.programnotes.cn/img/ai/aaaa0871e840d64dc1a6f9c8e2d9e060.png"
---

- B站升级并开源Index-AniSora，一个动漫视频生成模型，采用强化学习技术。
- 该模型基于AniSora框架，已被IJCAI25接收，并提出了专为二次元视频生成的强化学习框架。
-  AnimeReward是一个专为动漫视频生成对齐设计的多维度高可信奖励系统。
 哔哩哔哩技术 2025-05-20 14:00

B站升级动画视频生成模型Index-AniSora技术并开源，支持番剧、国创、漫改动画、VTuber、动画PV、鬼畜动画等多种二次元风格视频镜头一键生成！

整个工作技术原理基于B站提出的 
AniSora: Exploring the Frontiers of Animation Video Generation in the Sora Era

实现，**该工作已经被IJCAI25接收**。再次基础上进一步提出了**首个专为二次元视频生成打造的强化学习技术框架，全面提升动画内容的生产效率与质量**Aligning Anime Video Generation with Human Feedback（https://arxiv.org/abs/2504.10044）

**所有的工作全部开源！快戳地址：**https://github.com/bilibili/Index-anisora/tree/main

我们提出了一套专门用于动漫视频生成任务的对齐管线，其整体框架如图1所示。我们构建了首个面向动漫领域的高质量奖励数据集，共包含 30,000 条人工标注的动漫视频样本。人工评估包括两个方面：**视觉外观（Visual Appearance）**与 **视觉一致性（Visual Consistency）**。其中，**视觉外观**的评价仅考虑视频帧的质量，包括视觉平滑度（VS）、视觉运动（VM）与视觉吸引力（VA）三个维度。而**视觉一致性**则进一步扩展了基本的文本-视频一致性（TC），引入了图像到视频（I2V）任务中的图像-视频一致性（IC）与动漫内容中特有的角色一致性（CC），确保更全面的评价。通过这六个维度，我们对动漫视频的整体质量进行系统性评估，从而更准确地反映人类在奖励建模中的偏好。基于此，我们进一步提出了 **AnimeReward**，一个专为动漫视频生成对齐设计的多维度高可信奖励系统。由于不同维度所关注的视觉特征存在差异，我们为不同维度采用专门的视觉-语言模型进行奖励回归，以更贴近地拟合人类偏好。我们进一步提出了 **差距感知偏好优化（GAPO）**
 ，显式地将正负样本对之间的偏好差距融入损失函数，从而提升对齐训练的效率和最终性能。


![](https://ai.programnotes.cn/img/ai/571e38823a421184f203153dae569c04.png)

图1 对齐管线整体概述


## 方法

**动漫奖励数据集构建**
为了增强数据集的动作类别多样性，我们收集的视频样本涵盖多种动作类别，包括说话、行走、挥手、亲吻、哭泣、拥抱、推拉等典型行为场景。通过人工标注，我们从 100 多种常见动作中总结出标准化的动作标签，对每个标签收集约 30～50 个视频片段，最终得到 **5000** 条真实动漫视频作为基础数据源。在文本提示词的设计方面，我们采用 Qwen2-VL 模型[1]对视频打标自动生成提示词，并使用 CogVideoX[2]中提出的提示词优化策略，生成文本提示。原始图像采用每个视频的第三帧，以作为图像到视频生成的输入。基于这些提示词和原始图像，我们使用了 5 个先进的图像到视频生成模型（Hailuo、Vidu、OpenSora[3]、OpenSora-Plan[4]和 CogVideoX[2]），生成多样化的动漫视频。结合初始的 **5000**条GT视频，我们构建了一个包含 **30000** 条动漫视频的奖励数据集，用于奖励模型的训练。此外，我们还构建了一个包含 **6000**条动漫视频的测试集，并严格保证测试集与训练集在初始图像和提示内容上无重叠，以确保测试评估的准确性与泛化性。

为了全方位评估生成动漫视频的质量，人工标注从两个方面衡量视频质量：**视觉外观与视觉一致性**。其中，视觉外观主要衡量视频的基础质量，关注其视觉表现，包括视觉的平滑度（visual smoothness）、运动幅度（visual motion）以及整体的视觉吸引力（visual appeal）；而视觉一致性则更加侧重于多模态之间的协调性，具体包含文本与视频的语义对齐（text-video consistency）、图像与视频的时空一致性（image-video consistency），以及动漫角色在视频中的稳定性（character consistency）。我们共邀请了 **6**名专业标注人员参与标注过程，对每段视频从上述 6 个维度分别打分，评分范围为 1 到 5 分，5 分表示质量最佳。每个维度的最终得分由所有标注者的打分取平均值，以确保评价的客观性和鲁棒性。


**AnimeReward训练**

与依赖单一视觉-语言模型（VLM）统一训练回归所有维度的奖励分数的方法不同，AnimeReward 对不同维度使用专门的VLM，通过奖励分数回归分别训练它们。


**Visual Smoothness**

对于动漫视频的视觉平滑度评估，我们基于Mantis-8B-Idefics2模型[5]，微调其视觉编码器，并在其后接入一个回归头，来让模型输出拟合人工打分结果。给定一个视频，我们的模型的平滑度评分机制如下：

![](https://ai.programnotes.cn/img/ai/23e77f72ffe09793497a21ea24e0f1d7.png)

其中，I_i 表示视频的第 i 帧，N 为视频的总帧数，Ev表示视觉编码器，Reg 为回归头模块。


**Visual Motion**


我们基于 ActionCLIP[6] 构建了一个动作评分模型，用于评估动漫视频中主要人物的运动幅度。在模型训练过程中，我们设计了一系列动作提示语（motion prompts），用于引导模型学习不同运动幅度的语义表达。例如：
- “主角在视频中有大幅度动作，如奔跑、跳跃、跳舞或挥手。”

- “主角在视频中保持静止，没有明显的动作。”

最终，模型根据输入视频与预设动作提示语之间的余弦相似度，计算出动作评分：

![](https://ai.programnotes.cn/img/ai/de375de0b6d8f12a799b2891bd9ba126.png)

其中，MCLIP 表示动作模型，V 表示待评估的视频片段，Tm 表示设计好的动作提示语。


**Visual Appeal**


视觉吸引力用于评估生成视频的基础质量，侧重于其整体美学表现。以往研究通常采用在真实世界图像数据集上训练的美学评分模型来进行评估。然而，这类模型在应用于动漫视频时效果不佳，不同方法生成的视频在评分上差异不明显，难以体现真实的美学偏好差异。为了解决这一问题，我们首先从视频中提取关键帧，然后对它们进行编码，训练一个美学回归模型来学习人类对动漫图像的审美标准，从而更精准地评估其视觉吸引力。吸引力评分的计算公式如下所示：


![](https://ai.programnotes.cn/img/ai/d350e008221b930f6a6abd84c34bf0f6.png)


其中，I_i 表示关键帧，K是提取的关键帧数量，SigLIP 为特征编码器，Aes 表示美学评分模型。


**Text-Video Consistency**


为了评估文本与视频的一致性，我们利用动漫文本-视频对，微调了视觉编码器与文本编码器，并在其上接入回归头，以学习文本与视频之间的语义对齐程度。文本-视频一致性分数的计算公式如下：


![](https://ai.programnotes.cn/img/ai/3d27977f96222fb5bffb2aea6878f2e5.png)


其中，Reg 表示回归头，Ev 和Et 分别表示视觉编码器和文本编码器。模型通过联合文本提示T 与对应视频V，学习它们之间的语义匹配关系。


**Image-Video Consistency**
在图像到视频生成任务中，生成视频应与输入图像尽量保持外观上的一致性。类似于文本-视频一致性的评估方法，我们微调了视觉编码器与回归头，对图像与视频之间的外观一致性进行建模评分：

![](https://ai.programnotes.cn/img/ai/1aec2b826dc80ca9fdd523c81a47d006.png)

其中，V 表示待评估的视频片段，Ip 表示输入图像，Ev 为视觉编码器，Reg为回归头。


**Character Consistency**
在动漫视频生成中，角色一致性是一个重要的因素。如果主角的身份和风格在视频中发生变化，即使视频质量较高，也可能存在侵权风险。因此，我们设计了一套系统性流程来评估角色一致性，流程包括：角色检测、分割与识别等多个阶段，该模型的框架如图2所示。具体而言，我们首先使用 GroundingDINO[7]、SAM[8] 以及追踪工具，对视频中的每一帧提取角色的掩膜（mask）。随后，我们使用 BLIP[9] 模型进行微调，以学习提取的人物掩膜与其对应的动漫角色（IP）之间的关联。


在推理阶段，我们通过计算生成视频中的动漫角色特征与角色库的对应特征之间的余弦相似度，来衡量角色在视频中的一致性。具体评分方式如下：


![](https://ai.programnotes.cn/img/ai/3715279853561adfbe309d1b614f9549.png)

其中，N 表示采样的角色帧数量，Mi 表示提取得到的第 i 帧的角色掩膜，fea_c表示对应参考角色的特征表示。


![](https://ai.programnotes.cn/img/ai/aaaa0871e840d64dc1a6f9c8e2d9e060.png)

图2 角色一致性训练和推理框架


我们将各个维度上经过训练的奖励模型整合，构建了多维动漫视频评价体系AnimeReward。对于动漫视频 v，初始帧为 x，对应的文本提示为 c，每个维度d∈D上的奖励得分记作 
![图片](https://ai.programnotes.cn/img/ai/eb8850d677ce6e7e881427203e6af5b9.png)
。


其中
![图片](https://ai.programnotes.cn/img/ai/eef353934a5ac2afd807e40af358d9bf.png)
表示该维度奖励模型的参数。


那么该视频的整体奖励分数R(v)通过对所有维度的评分取平均得到，公式如下：


![](https://ai.programnotes.cn/img/ai/45bd643ff1db6094078bc412f8e61f19.png)


通过对人类偏好的学习，AnimeReward 能够为动漫视频生成对齐提供高质量的偏好反馈信号，提升视频生成模型的整体表现与人类认知的一致性。


**动漫视频生成对齐**

传统的 DPO方法仅关注样本对之间的偏好概率 
![图片](https://ai.programnotes.cn/img/ai/c8fdf7d73a31bc1d44f3da5cc4668f48.png)
建模，其中vw 为样本对中得分较高（被偏好）的视频，vl为得分较低（不被偏好）的视频。然而，这种方法忽略了偏好强度的差异，即不同样本对的正负样本之间的偏好差距的大小。


为了解决这一问题，我们提出了差距感知偏好优化（Gap-Aware Preference Optimization, GAPO），首先为每个生成视频定义其奖励增益（Reward Gain），公式如下：

![](https://ai.programnotes.cn/img/ai/fda1e4fcd3e99c1df3a345566d1303e4.png)

其中，
![图片](https://ai.programnotes.cn/img/ai/985cade67480f1469baf61c56beb46f8.png)
表示视频vi 的归一化奖励得分，α是控制奖励增益强度的超参数。


对于每个偏好样本对（vw，vl），我们将正负样本的奖励增益差值作为差距权重因子，作用于原始 DPO 损失函数，得到 GAPO 的损失函数：



![](https://ai.programnotes.cn/img/ai/ecff8fc517abde2c0413a10315097d1a.png)


通过在对齐训练中显示引入偏好差距信息，GAPO 在优化时显著放大了偏好差异明显的样本对的影响，同时抑制了偏好差异较小的样本对的干扰，从而更高效地提升模型对人类偏好的对齐能力，特别是在动漫视频生成这类主观性强的任务中具有重要意义。


## 实验
**数据集**


在对齐训练中，我们采用开源模型 **CogVideoX-5B**[2]作为基线模型。我们首先构建了一个包含**2000**条原始动漫图像及其对应文本提示的初始训练集。基于该数据集，我们使用基线模型为每组数据采样生成  段动漫视频，再利用 **AnimeReward**
 ，对每组生成视频进行偏好奖励评分，选择其中得分最高和得分最低的两个视频，构成一个偏好样本对。最终得到包含 **2000**
对偏好样本的集合作为后续偏好对齐优化的训练集。


**实验结果**


我们采用自动化评测和人工评测两种方式来评估模型的对齐效果。自动评测包含VBench-I2V[11], VideoScore[12]和我们提出的AnimeReward三种方法。人工评测邀请了三位专业的评测人员给出主观评价。只有当三位评测者中至少两位都认为视频  比  更好或更差时，视频  才会被认为赢或输  。

**VBench-I2V**
 [11]基准的评测结果如表1所示，我们提出的偏好对齐方法在总分上取得了最优表现，在几乎所有评估指标上均显著优于基线模型，并在大多数情况下超越了 SFT（监督微调）模型。值得注意的是，在 I2V Subject 和 Subject Consistency 两个关键指标上的提升尤为显著，表明我们的对齐方法能够帮助视频生成模型在保持动漫角色一致性方面具备更强的能力。如表2所示，在 **AnimeReward**
评价体系下，除 Visual Motion 外，我们的方法在所有维度上均实现了大幅提升，说明我们的对齐模型在视觉外观与一致性方面更贴近人类偏好。在 **VideoScore** [12]评估中，我们的方法在三个维度上均优于基线模型与 SFT 模型，表现出更好的视觉质量和时序稳定性。同时，我们也观察到了，在动态程度（即 Visual Motion/ Dynamic Degree）这一指标上，对齐后的模型表现略逊于基线与 SFT 方法。对此，我们认为，高动态程度的视频更容易引发空间扭曲与伪影，从而大大降低整体视觉质量，对人类主观偏好产生负面影响。这一结果也表明，人类通常喜欢具有**更高视觉质量、更强一致性**与**更好稳定性**的视频内容，而非单纯追求高动态幅度的生成结果。


![](https://ai.programnotes.cn/img/ai/45d0457a4621fd1c9f99c960460c2306.png)

表1 在VBench-I2V上的定量性能比较


![](https://ai.programnotes.cn/img/ai/f546aacff5ae687f9fbcc4a5d3bc53d4.png)

表2 在AnimeReward和VideoScore上的量化性能比较


图3展示了人工评测的对比实验结果，我们的对齐模型相较于基线模型与 SFT 模型展现出显著优势，整体胜率超过**60%**。尽管 SFT 模型使用了偏好分数最高的优质样本进行训练，但其生成视频的质量并未得到明显提升，甚至在人工评测中的胜率低于基线模型。


![](https://ai.programnotes.cn/img/ai/d3f25d08c2d1f983ddb61863eb42f797.png)

图3 不同模型生成的动漫视频的人工评测结果


## **消融研究**


为验证我们提出的**差距感知偏好优化（GAPO）** 相较于传统DPO的优势，我们在保持实验设置一致的前提下，仅更换偏好优化算法，进行对比实验。我们在前述三种评价体系上对不同模型进行了系统评估，实验结果如表3所示。其中，**AnimeReward（AR）** 和**VideoScore（VS）** 的最终得分为各维度得分的平均值。从结果来看，GAPO 在三个评价体系中均取得了最优表现，尤其在**VBench-I2V （V-I2V）**和**AnimeReward（AR）**上相较 DPO 获得了显著提升。


![](https://ai.programnotes.cn/img/ai/9ccb72b28d27825682b89e70fd34cbc9.png)

表3 对GAPO在三个评价体系上的消融研究结果

为验证 **AnimeReward** 奖励模型在动漫视频偏好对齐任务中的优势，我们设计了对比实验，使用**VideoScore** [12]作为替代的奖励模型进行对齐训练。实验结果如表4所示。从结果可以看出，使用 AnimeReward 训练的模型在两个评价体系中均优于使用 VideoScore 训练的模型；而 VideoScore 仅仅在其自身评价体系中取得优势。为了更客观地评估两者的对齐性能，我们在图4展示了它们相对于基线模型在第三方评价基准**VBench-I2V**[11]各个维度上的可视化评价结果。除 Dynamic Degree 外，基于 AnimeReward 的对齐模型在其余**7**个维度上全面优于VideoScore。


![](https://ai.programnotes.cn/img/ai/0907666e112a4fe2055863ebef2f8017.png)

表4 基于不同奖励模型的消融研究结果


![](https://ai.programnotes.cn/img/ai/58cc6f85b9421d89dee684da7e0398a1.png)

图4 基于不同奖励模型在VBench-I2V多个维度上的可视化评估结果


## 结论

本文提出了首个针对动漫视频生成的奖励模型 **AnimeReward**，旨在模拟人类偏好对生成动漫视频进行全方位的评价。我们基于两大方面设计了六个评价维度，从多个角度衡量生成动漫视频的质量。基于 **AnimeReward**，我们进一步提出了一种新颖的优化对齐策略 **差距感知偏好优****化（Gap-Aware Preference Optimization, GAPO）**，在优化损失中显式引入偏好差距信息，从而高效提升生成模型的对齐性能。实验结果表明，仅仅依赖基线模型生成的视频数据，我们提出的对齐管线依然能够显著提升动漫视频的生成质量，使结果更贴近人类偏好，验证了该方法在偏好对齐任务中的有效性与实用性。


## demo
- 对齐效果

**提示词：**
画面中展现了石块发生爆炸的场景，发出刺眼的光芒，碎石四处飞散

**对齐前⬇️**

![](https://ai.programnotes.cn/img/ai/3793aac30508889546defa34a7669860.gif)

****


**对齐后⬇️**

![](https://ai.programnotes.cn/img/ai/0a2b992a2704dd40c647507ff0871e88.gif)



**提示词：**
画面中一个人在快速向前奔跑，他奔跑的速度很快使得人物有些模糊

**对齐前⬇️**

![](https://ai.programnotes.cn/img/ai/853d39f41be7a2fd05bdeade26a2470c.gif)

****


**对齐后⬇️**

![](https://ai.programnotes.cn/img/ai/82d9aafdc77df6794d0355c750fb4689.gif)

**提示词：**
老人的目光紧盯着那颗宝石，右手轻微摆动着手中的放大镜，嘴巴在说话，仿佛它掌握着解开某种古老知识或秘密的关键。

**对齐前⬇️**

![](https://ai.programnotes.cn/img/ai/b58b2f38c81c4ff15c57c91f7df144fb.gif)

****


**对齐后⬇️**

![](https://ai.programnotes.cn/img/ai/d658207d1cd720ca4d75821a8e6f05c4.gif)

****


## 参考文献

[1] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, et al. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution. arXiv preprint arXiv:2409.12191, 2024.

[2] Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang, et al. Cogvideox: Text-to-video diffusion models with an expert transformer. arXiv preprint arXiv:2408.06072, 2024.

[3] Zangwei Zheng, Xiangyu Peng, Tianji Yang, Chenhui Shen, Shenggui Li, Hongxin Liu, Yukun Zhou, Tianyi Li, and Yang You. Open-sora: Democratizing efficient video production for all. arXiv preprint arXiv:2412.20404, 2024.

[4] Bin Lin, Yunyang Ge, Xinhua Cheng, Zongjian Li, Bin Zhu, Shaodong Wang, Xianyi He, Yang Ye, Shenghai Yuan, Liuhan Chen, et al. Open-sora plan: Open-source large video generation model. arXiv preprint arXiv:2412.00131, 2024.

[5] Dongfu Jiang, Xuan He, Huaye Zeng, Cong Wei, Max Ku, Qian Liu, and Wenhu Chen. Mantis: Interleaved multi-image instruction tuning. arXiv preprint arXiv:2405.01483, 2024.

[6] Mengmeng Wang, Jiazheng Xing, and Yong Liu. Actionclip: A new paradigm for video action recognition. arXiv preprint arXiv:2109.08472, 2021.

[7] Tianhe Ren, Qing Jiang, Shilong Liu, Zhaoyang Zeng, Wenlong Liu, Han Gao, Hongjie Huang, Zhengyu Ma, Xiaoke Jiang, Yihao Chen, et al. Grounding dino 1.5: Advance the "edge" of open-set object detection. arXiv preprint arXiv:2405.10300, 2024.

[8] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, et al. Sam 2: Segment anything in images and videos. In ICLR, 2025.

[9] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In ICML, 2022.

[10] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In NeurIPS, 2023.

[11] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, Chenyang Si, Yuming Jiang, Yuanhan Zhang, Tianxing Wu, Qingyang Jin, et al. Vbench: Comprehensive benchmark suite for video generative models. In CVPR, 2024.

[12] Xuan He, Dongfu Jiang, Ge Zhang, Max Ku, Achint Soni, Haonan Chen, Abhranil Chandra, Ziyan Jiang, et al. Videoscore: Building automatic metrics to simulate fine-grained human feedback for video generation. In EMNLP, 2024.

作者丨Bwin、HarryJ、高树、seasonyang