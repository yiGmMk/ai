---
title: "终于不用当人肉Ctrl+CV了！用n8n+MCP把小红书创作搞成半自动化"
date: "2025-06-24"
tags: ["n8n", "MCP", "小红书", "自动化", "自媒体"]
categories: ["自动化", "自媒体"]
description: "通过n8n和MCP工具实现小红书创作半自动化，摆脱重复性工作，专注于内容创作。"
author: "kayin9凯隐的无人化生产矩阵"
image: ""
---

- 利用n8n和MCP工具，将小红书创作流程半自动化，减少重复操作。
- 通过Local File Trigger节点监控指定目录，实现文件上传自动触发工作流。
- 使用AI Agent和代码节点解析文档内容，区分标题和内容，并结合MCP工具实现自动发布。

**源自** |  kayin9凯隐的无人化生产矩阵 2025-06-24 00:37

如果你在做自媒体，又如果恰好在运营小红书账号，会不会觉得反反复复复制粘贴、调格式、传图这些机械操作太浪费时间了！自从入了 n8n
 的坑，再加上现在AI工具这么猛，我算是彻底悟了：**这些破事就该让机器干，创作者就该专心搞创作**

折腾了小半个月，靠AI助攻，我搞了个项目👉 xhs_toolkit（小红书工具包），最新1.2.3版本终于能用了！今天就咱就唠唠怎么用 n8n 把创作流程钉死在自动化轨道上。

**省流版**
：你只管写文案，其他脏活累活交给流程自动化（保姆级教程）

![工作流展示](https://ai.programnotes.cn/img/ai/1eb94b2f81a9e58a7c7df213db6b3ff7.png)

工作流展示

这个工作流怎么用？
第一步：将需要发小红书的标题和文案写到 txt 或者 markdown 里
第二步：将包含内容的文档，以及准备好的相关图片放到任意空文件夹内
第三步：将文件夹上传至指定目录即可。

至于指定目录是什么？继续往下看吧
## 工作流完整概述
### 节点 1：Local File Trigger

![Local File Trigger](https://ai.programnotes.cn/img/ai/4affa06658866b69a3e9a45ed5f881b1.png)

Local File Trigger

**"这玩意儿就是个自动看门狗！**

设置这个Local File Trigger
节点（就是图里那个），专门盯着/data/xhs
这个文件夹——只要有人往里扔新文件或者新建文件夹，它立马就会：
1. 1. 支棱起来（自动触发）

1. 2. 把新文件/文件夹的信息打包成标准格式

1. 3. 直接丢给下一个流程节点处理

相当于给你的文件夹装了**红外线警报器**
，不用手动刷新检查！（当然你要先再 Folder to Watch 这里先设置好要监听的文件目录，等于告诉它盯哪个文件夹，就像图中选的这个）"
### 节点 2：Execute Command

它的作用是直接在 n8n 的容器内执行 linux 里最基本的 ls 命令

具体来说就是通过 ls 命令来显示目录中存在哪些文件，当我们上传文件进去的时候，文件就会被输出出来。那么文件夹在 docker 容器里，我们怎么上传？难道还要用 docker cp 命令手动敲吗？

不的，不需要。

我之前发过一篇文章，关于如何部署中文版的 n8n，就是这篇：
[n8n汉化版部署指南](https://mp.weixin.qq.com/s?__biz=MzkzNzk3MTEyOA==&mid=2247483745&idx=1&sn=23de8e63fb0b56f0b6a695a9104b08c6&scene=21#wechat_redirect)


熟悉 docker 命令的你应该知道我在讲什么，这里就简单带过了。我们将宿主机本地环境的目录挂载到容器内，因此仅需要往宿主机的目录传递文件或者目录即可。可是如果宿主机 linux 也在外部怎么办? 没关系，创建个 smb 共享，本地 windows 或者 macos 上挂载个共享目录就可以了，这样当你将完整的文件或者目录塞进这个共享目录就可以触发了。

所以这就是指定目录吗？是的，你说的没错。

![Execute Command](https://ai.programnotes.cn/img/ai/d8f687bf1dc1184f95bea3b5b02b0f30.png)

Execute Command
### 节点 3：Code （获取被监控目录的完整路径）

前一个节点中得到了容器内的指定目录的路径输出，长这样：
```
[
  {
    "exitCode": 0,
    "stderr": "",
    "stdout": "markdown_4.txt\nmd2card-1750115670515-1.png\nmd2card-1750115670741-2.png\nmd2card-1750115670901-3.png\nmd2card-1750115671053-4.png\nmd2card-1750115671198-5.png\nmd2card-1750115671374-6.png"
  }
]
```

它将作为入参来到这里。

![获取被监控目录的完整路径](https://ai.programnotes.cn/img/ai/2d63fc33f5fcd9adcf9f814d9fff6723.png)

获取被监控目录的完整路径

代码是这样的：
```
// 获取前两个节点的输出数据
const dirMonitorOutput = $("Local File Trigger").first().json.path; // 监控目录变更节点的输出
const execCommandOutput = $input.first().json.stdout; // Exec Command节点的输出

const basePath = dirMonitorOutput; // 例如: "/data/xhs/20250618"
const fileListString = execCommandOutput; // 文件名列表字符串

const textFiles = []; // 存储文本文件路径
const imageFiles = []; // 存储图片文件路径

// 定义常见的图片文件扩展名列表（可以根据需要调整）
const imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg'];

// 图片文件路径前缀
const imagePathPrefix = '/root/n8n-i18n-chinese';

if (fileListString && typeof fileListString === 'string') {
  const filenames = fileListString.trim().split('\n');

  for (const filename of filenames) {
    const trimmedFilename = filename.trim();
    if (trimmedFilename === '') {
      continue; // 跳过空行（如果存在）
    }

    // 构建完整的文件路径
    // 确保 basePath 和 filename 正确拼接，避免双斜杠或无斜杠
    let fullPath = basePath;
    if (!basePath.endsWith('/')) {
      fullPath += '/';
    }
    fullPath += trimmedFilename;

    const lowerFilename = trimmedFilename.toLowerCase();

    // 判断文件类型并添加到对应数组
    if (lowerFilename.endsWith('.txt')) {
      textFiles.push(fullPath);
    } else if (imageExtensions.some(ext => lowerFilename.endsWith(ext))) {
      // 为图片文件添加前缀
      const imageFullPath = imagePathPrefix + fullPath;
      imageFiles.push(imageFullPath);
    }
    // 如果需要，可以在这里添加更多文件类型的判断逻辑
  }
}

// 返回字符串格式的结果
return {
  text_files: textFiles.join(','),
  image_files: imageFiles.join(',')
};
```

得到的输出是：
```
[
  {
    "text_files": "/data/xhs/20250618/markdown_4.txt",
    "image_files": "/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115670515-1.png,/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115670741-2.png,/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115670901-3.png,/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115671053-4.png,/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115671198-5.png,/root/n8n-i18n-chinese/data/xhs/20250618/md2card-1750115671374-6.png"
  }
]
```

到这里，txt 文件和图片文件被区分出来了，并且图片路径是宿主机里所在的路径。至于这里为什么一定要是宿主机的路径，先卖个关子，一会后面会解释。
### 节点 4：Read File (s) From Disk

嗯，从磁盘读取文件，很直白的一个节点。

![Read File (s)From Disk](https://ai.programnotes.cn/img/ai/ef6a62328f1fc14f5dfc27b234d48e73.png)

Read File (s) From Disk

可以看到 n8n
 吧 txt 文件输出出来了，接下来要继续用 code 节点，获取里面的内容
### 节点 5：解析文档内容
```
const items = $input.all();
const results = [];

items.forEach(item => {
  let content = null;
  let success = false;
  
  if (item.binary && item.binary.data && item.binary.data.data) {
    try {
      const buffer = Buffer.from(item.binary.data.data, 'base64');
      content = buffer.toString('utf8');
      success = true;
    } catch (error) {
      console.log('解析错误:', error.message);
    }
  }
  
  results.push({
    content: content,
    success: success,
    original_data: item.json
  });
});

return results;
```

通过上述代码，这个文件的内容会被解析出来
```
[
  {
    "content": "# 超有趣的五大心理学效应，学会受益终身😎\n宝子们，今天我要给大家分享五个超神奇的心理学效应，学会了说不定能改变你的生活哦🤩 还能防止被别人洗脑呢！\n\n## 1. 行为启动效应\n### 明面洗脑\n心理学家约翰巴奇做了个实验，让一组人用跟老人相关的词造句，比如“皱纹”“拐杖”等。之后发现这些人离开实验室时走路速度明显变慢，还出现了很多老人相关的特征。这是因为不断重复老人相关的信息，大脑会不受控地改变行为。就像看视频里突然飞来一个球，明明知道是视频里的，身体还是会晃一下。\n\n### 潜意识洗脑\n另一组实验，让两组人谈判，一组桌子上放钱相关的东西，如钞票、金币、支票；另一组放纸、笔等中性物品。结果发现，桌子上放钱的那组人在谈判中更强调自己的利益。这是通过潜意识引导，让人不知不觉被“洗脑”。\n\n### 生活应用\n风水里生财的寄托物就是这个原理，比如金蟾蜍，放在阳光能照到且相对隐蔽的地方，给自己潜意识里赚钱的暗示。我们工作室每天打扫、添置新家具，让员工在舒适环境中工作，审美和品味会更一致，也更容易做出想要的东西。\n\n**实用建议**：想培养某个好习惯，就不断给自己相关的积极暗示，比如贴便利贴提醒自己“我每天都能坚持运动”。\n\n## 2. 邓宁克鲁格效应\n上世纪 90 年代，康奈尔心理学家发现，在某领域水平越高的人往往低估自己，水平越低的人往往高估自己。比如玩无人机，老手炸过机所以极其小心，新手没炸过机就觉得很简单。写作也是，真正厉害的作家知道写出伟大作品很难，新手却觉得一天写几万字很正常。\n\n### 判断方法\n王力行老师说的人生四行原理：我觉得我行，别人觉得我行，觉得我行的人他自己行，我身体行。最好在行业里找个大家都认可的人做朋友，听他的建议。\n\n**实用建议**：作为新手，进入新领域要保持敬畏心，多学习；老手要正视自己，增加突破的勇气。\n\n## 3. 破窗效应\n1982 年犯罪心理学家 James Wilson 发现，环境脏乱差会让犯罪率提高，因为脏乱差会给人规则不被重视的感觉。2008 年荷兰团队实验，街头涂鸦后，随手扔垃圾的概率从 25%涨到 50%。\n\n### 应用场景\n公司管理中，不能允许错误随便发生，规矩要明确，才能保证服务或产品标准化。两性关系里，男女朋友有问题要当天讲清楚，不然矛盾会越来越多。\n\n**实用建议**：生活中保持环境整洁，制定规则并严格遵守，小错误也要及时纠正。\n\n## 4. 霍桑效应\n上世纪美国霍桑工厂实验，不管是提高照明条件、取消福利等，工人工作效率都比之前高。原因是工人知道自己被观测，人被观测行为就会改变，且往往是积极改变。从哲学角度看，人活着的意义就是被关注。\n\n### 应用方法\n就像小时候班主任突然出现，我们会坐正；跟学生说他是小天才，他状态会变好。想让男朋友变得更好，就要看到他的进步和改变。\n\n**实用建议**：在团队中多关注成员的表现，给予肯定和鼓励，能提高他们的积极性和工作效率。\n\n## 5. 习得性无助\n1967 年美国心理学家塞利格曼用狗做实验，狗多次尝试冲出笼子失败后，即使门打开也不冲了，甚至蜂音器一响还没电击就开始呻吟。生活中我们做事多次失败也容易陷入习得性无助，全盘否定自己。\n\n### 正确看待\n成功和失败是客观存在的，成功是少数，失败是多数。不要因为几次失败就否定自己，要相信成功会在不断尝试中到来。\n\n**实用建议**：把失败看作成功的必经之路，每次失败后总结经验教训，继续努力。\n\n宝子们，这些心理学效应是不是很有意思😉 希望大家把它们用在积极的事情上，让自己变得更强💪\n\n#心理学效应 #行为启动效应 #邓宁克鲁格效应 #破窗效应 #霍桑效应 #习得性无助 ",
    "success": true,
    "original_data": {
      "mimeType": "text/plain",
      "fileType": "text",
      "fileName": "markdown_4.txt",
      "fileExtension": "txt",
      "fileSize": "4.22 kB"
    }
  }
]
```
### 节点 6：AI Agent（精简内容）

这个节点可有可无，我放了一个为了精简一下内容

![精简内容](https://ai.programnotes.cn/img/ai/f1e0f600053322ff8d21bd29077d38dd.png)

精简内容
### 节点 7：Code（区分标题和内容）

现在这个节点才是比较关键的部分，作用是将上一个节点的出参重新整理，区分标题和内容（你也可以换一种方式在文档中标注好标题和内容做区分，但是后续需要一段提示词让 AI 进行配合）

代码是这样的：
```
// 获取输入数据
const inputData = $input.all();
const results = [];

inputData.forEach(item => {
  const data = item.json;
  
  // 处理数组或单个对象
  let outputArray = Array.isArray(data) ? data : [data];
  
  outputArray.forEach(outputItem => {
    // 获取markdown内容
    let markdownContent = outputItem.output || outputItem;
    
    // 清理markdown代码块标记
    markdownContent = markdownContent.replace(/^```markdown\n?/, '').replace(/\n?```$/, '');
    
    // 按行分割
    const lines = markdownContent.split('\n');
    
    // 提取标题和内容
    let title = '';
    let content = '';
    
    lines.forEach(line => {
      const trimmedLine = line.trim();
      
      // 提取主标题 (第一个 # 开头的)
      if (trimmedLine.startsWith('# ') && !title) {
        title = trimmedLine.substring(2).trim();
      }
      // 其他所有内容作为正文（去除markdown格式）
      else if (trimmedLine) {
        // 简单去除markdown格式
        const cleanLine = trimmedLine
          .replace(/^#{1,6}\s+/, '')      // 去除标题标记
          .replace(/\*\*([^*]+)\*\*/g, '$1')  // 去除加粗
          .replace(/^\-\s+/, '')          // 去除列表标记
          .replace(/^\d+\.\s+/, '');      // 去除数字列表
        
        if (cleanLine) {
          content += (content ? ' ' : '') + cleanLine;
        }
      }
    });
    
    results.push({
      title: title,
      content: content,
    });
  });
});

return results;
```

得到的结果是：
```
[
  {
    "title": "5个心理学效应让你开挂💡",
    "content": "姐妹们！今天分享5个超实用的心理学效应，学会直接开挂人生✨ 职场情场都能用上！ 行为启动效应 暗示改变行为 看到老人词汇后走路变慢👵 金钱暗示实验 谈判桌放钱更自私💰 风水玄学解密 金蟾蜍=赚钱暗示🐸 小贴士：想养成好习惯就多给自己积极暗示！ 邓宁克鲁格效应 新手老手差异 菜鸟自信爆棚✈️ 四行判断法 找靠谱前辈指点👨‍🏫 小贴士：新手要虚心，老手要突破！ 破窗效应 环境影响行为 涂鸦后垃圾翻倍🗑️ 感情保鲜秘诀 矛盾不过夜💑 小贴士：保持环境整洁，及时解决问题！ 霍桑效应 被关注就变好 工人效率提升🏭 夸夸大法好 多夸对象更甜❤️ 小贴士：多关注多鼓励，效果翻倍！ 习得性无助 失败实验 狗狗放弃逃跑🐶 成功必经路 失败是过程不是终点🏁 小贴士：总结经验再出发！ 这些心理学效应真的超有用！建议收藏反复看🌟 #心理学干货 #自我提升 #职场技巧 #恋爱心理学 #成长必看"
  }
]
```
### 节点 8：Set（参数映射）

从上一个节点可以看到 title 和 content 已经被区分出来了，现在再把图片路径给拿过来放到一起，其实这个节点也可以不要，但是需要在下一个节点捋清楚从哪个节点获取什么数据。看个人习惯了

![参数映射](https://ai.programnotes.cn/img/ai/820700f980135fbd4184cda1f772ef53.png)

参数映射
> 小技巧：在上图中，涉及到变量输入环节，可以直接从左侧拖拽。左侧罗列了所有节点。如果手动输入也是可以的，输入框右上角先点击表达式，然后在输入框内先输入 {{ }}
 双花括号，用 $
 用这个符号来触发节点选择，后续的选择都用 .
 来触发，是对这个节点所有数据的操作。

### 节点 9：AI Agent（让 deepseek 帮我们发布小红书）

好了，重头戏来了。我们要让 deepseek 来完成小红书的发布工作，他自己是发布了的，所以我们需要给他一个 mcp

![xhs-mcp](https://ai.programnotes.cn/img/ai/7c4ef9786d52c9b266f7841752f6b9c3.png)

xhs-mcp

这个 mcp 是运行在n8n
所在的宿主机上的。

![xhs-toolkit](https://ai.programnotes.cn/img/ai/7c6d365942a91b25b4c4efbdfe2ea559.png)

xhs-toolkit

除了 xhs-toolkit，还需要提示词的辅助，把上一个节点整理好的 3 个关键参数告诉 AI，让他调用工具，他就能够完成发布了

![发布小红书](https://ai.programnotes.cn/img/ai/67bae99afe77d775a4d99b3e8c9fd1de.png)

发布小红书

补充一下前面留下的坑，为什么路径必须是宿主机的路径？
因为宿主机和 n8n
 同时运行在宿主机上，mcp 工具被调用的时候，是从宿主机上获取文件的，而不是 n8n
 因此挂载到容器上的路径，是被 n8n
 监听的，当文件或者文件夹上传，就会触发工作流，而文件又是 mcp 工具的文件来源。这就完成了一个闭环

![闭环关系](https://ai.programnotes.cn/img/ai/286e4a95c1993a145e8e06b131a0686d.png)

闭环关系


所以，在 linux 上只需要将宿主机上的目录给共享出来（smb 也好 nfs 也好 ftp 也好，都行），我们就可以把这整个流程当作远端的一个服务。本地专心创作，准备好文档和图片，打包成文件夹。丢进目录里即可。
## xhs-toolkit 的题外话

在工具版本更新到 1.2.3 之前，不光 linux 上运行无头浏览器存在问题，基础功能也不完善。
现在，我已经测试过了，1.2.3 版本确实已经可以正常使用了，不论是标准模式还是无头模式。不论是 mac、linux、windows 系统，都可以正常运行（Arm 没测试过，理论上也没问题）

如果你有需要，请前往 github 下载源码开始尝试吧：
![GitHub](https://ai.programnotes.cn/img/ai/8c89202d1881b45aa9cf626c3e1c51ac.svg)

GitHub
## 总结

借助 AI 的力量，许许多多的日常复杂且机械的劳动都可以利用技术手段完成自动化。尽管当前的工作流只是最最初级的满足最低要求——能用，还远达不到好用的底部。

也希望能给看到这里的朋友们一个启发，关注平时的工作，是否也可以像这样做成自动化？
