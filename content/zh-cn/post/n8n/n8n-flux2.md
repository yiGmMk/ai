---
title: "n8n使用教程案例2-Flux风格绘画"
date: "2025-06-11"
tags: ["MCP", "AI", "Agent", "Function Call", "工具调用","n8n","Flux"]
categories: ["人工智能", "技术","n8n"]
description: "本文介绍以一种使用flux绘画的n8n工作流"
author: "yi"
image: "https://ai.programnotes.cn/img/n8n/flux4.jpg"
---

## 提示词案例

甜甜的恋爱

```bash
A heartwarming scene capturing sweet love,depicted in a soft, romantic anime style. Pastel colors dominate, with gentle light filtering through cherry blossom trees. Two characters share a tender moment, their faces flushed with affection. The background features a cozy cafe, complete with steaming mugs and delicate pastries, all rendered in a sweet, sugary palette
```

效果:

![效果](https://ai.programnotes.cn/img/n8n/flux2.jpg)
![效果](https://ai.programnotes.cn/img/n8n/flux3.jpg)
![效果](https://ai.programnotes.cn/img/n8n/flux4.jpg)
![效果](https://ai.programnotes.cn/img/n8n/flux5.jpg)


## 工作流下载

```json
{
  "name": "Flux",
  "nodes": [
    {
      "parameters": {
        "method": "POST",
        "url": "https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {}
          ]
        },
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "prompt",
              "value": "={{ $('生成提示词').item.json.prompt }},style:{{ $json.stylePrompt }}"
            },
            {
              "name": "seed",
              "value": "1189"
            },
            {
              "name": "aspect_ratio",
              "value": "={{ $('n8n 表单触发器').item.json['图片比例'] }}"
            },
            {
              "name": "enable_safety_checker",
              "value": "false"
            },
            {
              "name": "num_images",
              "value": "1"
            }
          ]
        },
        "options": {}
      },
      "id": "32e7f75c-eb60-408a-be70-a7ba81e3698b",
      "name": "发起 Fal 绘图 请求",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        40,
        400
      ],
      "notesInFlow": true,
      "typeVersion": 4.2,
      "credentials": {
        "httpHeaderAuth": {
          "id": "76rj3DVY3trbLLn0",
          "name": "Header Auth account"
        }
      },
      "onError": "continueErrorOutput",
      "notes": " "
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"formSubmittedText\": \"Fal API 调用失败，重试或刷新试试 \"\n}",
        "options": {}
      },
      "id": "efdba6ac-1566-4c78-b465-3090d4e3f66a",
      "name": "回复错误",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        260,
        500
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "457eff4f-c9a9-4698-994b-9cdfb04f46f0",
              "name": "prompt",
              "value": "={{ $json.text }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "5ee855db-2eb4-4c7b-b705-9b944045ca20",
      "name": "生成提示词",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -620,
        400
      ],
      "notesInFlow": true,
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 1
                },
                "conditions": [
                  {
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('n8n 表单触发器').item.json.Style }}",
                    "rightValue": "超现实逃逸"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Hyper-Surreal Escape"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 1
                },
                "conditions": [
                  {
                    "id": "106969fa-994c-4b1e-b693-fc0b48ce5f3d",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('n8n 表单触发器').item.json.Style }}",
                    "rightValue": "后模拟故障景观"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Post-Analog Glitchscape"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 1
                },
                "conditions": [
                  {
                    "id": "24318e7d-4dc1-4369-b045-bb7d0a484def",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('n8n 表单触发器').item.json.Style }}",
                    "rightValue": "AI 反乌托邦"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "AI Dystopia"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 1
                },
                "conditions": [
                  {
                    "id": "a80911ff-67fc-416d-b135-0401c336d6d8",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('n8n 表单触发器').item.json.Style }}",
                    "rightValue": "霓虹野兽派"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Neon Fauvism"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 1
                },
                "conditions": [
                  {
                    "id": "7fdeec28-194e-415e-8da2-8bac90e4c011",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('n8n 表单触发器').item.json.Style }}",
                    "rightValue": "鲜艳流行爆炸"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Vivid Pop Explosion"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "38a67bf8-8397-483f-acbc-7fa3b3def171",
      "name": "按风格路线",
      "type": "n8n-nodes-base.switch",
      "position": [
        -400,
        340
      ],
      "typeVersion": 3.1,
      "notesInFlow": true
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "=<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Flux 图片生成结果</title>\n    <style>\n        body {\n            font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;\n            display: flex;\n            flex-direction: column;\n            align-items: center;\n            justify-content: flex-start;\n            min-height: 100vh;\n            background-color: #121212;\n            color: #e0e0e0;\n            margin: 0;\n            padding: 20px;\n        }\n\n        .container {\n            width: 90%;\n            max-width: 800px;\n            text-align: center;\n            background: linear-gradient(145deg, #1e1e1e, #242424);\n            padding: 32px;\n            border-radius: 16px;\n            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);\n            margin-bottom: 32px;\n        }\n\n        .image-container {\n            margin-bottom: 24px;\n        }\n\n        .image-container img {\n            max-width: 100%;\n            height: auto;\n            border-radius: 12px;\n            border: 2px solid #333;\n            transition: transform 0.3s ease, box-shadow 0.3s ease;\n        }\n\n        .image-container img:hover {\n            transform: scale(1.02);\n            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);\n        }\n\n        .style-text {\n            font-size: 18px;\n            margin: 24px 0;\n            color: #bbb;\n            padding: 12px;\n            background: rgba(255, 255, 255, 0.05);\n            border-radius: 8px;\n        }\n\n        .cta {\n            display: inline-block;\n            width: auto;\n            min-width: 200px;\n            margin: 20px 0 0;\n            padding: 16px 32px;\n            border: none;\n            border-radius: 8px;\n            text-decoration: none;\n            color: #fff;\n            background: linear-gradient(135deg, #1C9985, #20B69E);\n            font-size: 18px;\n            font-weight: 500;\n            cursor: pointer;\n            transition: all 0.3s ease;\n        }\n\n        .cta:hover {\n            background: linear-gradient(135deg, #20B69E, #25D4B8);\n            transform: translateY(-2px);\n            box-shadow: 0 8px 16px rgba(28, 153, 133, 0.3);\n        }\n\n        .recent-renders {\n            width: 90%;\n            max-width: 800px;\n            display: grid;\n            grid-template-columns: repeat(2, 1fr);\n            gap: 24px;\n            margin-top: 32px;\n        }\n\n        .recent-render {\n            background-color: #2c2c2c;\n            padding: 16px;\n            border-radius: 12px;\n            transition: transform 0.3s ease, box-shadow 0.3s ease;\n        }\n\n        .recent-render:hover {\n            transform: translateY(-4px);\n            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);\n        }\n\n        .recent-render img {\n            width: 100%;\n            height: auto;\n            border-radius: 8px;\n            border: 2px solid #333;\n            transition: transform 0.3s ease;\n        }\n\n        /* 隐藏额外的图片 */\n        .recent-render:nth-child(n+5) {\n            display: none;\n        }\n\n        /* 显示更多按钮样式 */\n        .show-more-label {\n            display: inline-block;\n            width: 90%;\n            max-width: 800px;\n            margin: 32px auto;\n            padding: 16px;\n            background: #2c2c2c;\n            color: #fff;\n            border: none;\n            border-radius: 8px;\n            font-size: 16px;\n            cursor: pointer;\n            transition: all 0.3s ease;\n            text-align: center;\n        }\n\n        .show-more-label:hover {\n            background: #333;\n            transform: translateY(-2px);\n        }\n\n        /* 隐藏复选框 */\n        #show-more {\n            display: none;\n        }\n\n        /* 当复选框被选中时显示额外的图片 */\n        #show-more:checked ~ .recent-renders .recent-render:nth-child(n+5) {\n            display: block;\n        }\n\n        /* 当复选框被选中时隐藏显示更多按钮 */\n        #show-more:checked ~ .show-more-label {\n            display: none;\n        }\n\n        @media (max-width: 768px) {\n            .recent-renders {\n                grid-template-columns: 1fr;\n            }\n            \n            .container {\n                padding: 20px;\n            }\n        }\n    </style>\n</head>\n<body>\n    <div class=\"container\">\n        <div class=\"image-container\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id }}.jpeg\" alt=\"生成的图片\" />\n        </div>\n        <div class=\"style-text\">图片风格: {{ $('n8n 表单触发器').item.json.Style }}</div>\n        <a href=\"https://note.ff2a.com/flux\" class=\"cta\">更多提示词</a>\n    </div>\n\n    <!-- 添加隐藏的复选框 -->\n    <input type=\"checkbox\" id=\"show-more\">\n\n    <div class=\"recent-renders\">\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 1 }}.jpeg\" alt=\"最近渲染 1\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 2 }}.jpeg\" alt=\"最近渲染 2\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 3 }}.jpeg\" alt=\"最近渲染 3\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 4 }}.jpeg\" alt=\"最近渲染 4\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 5 }}.jpeg\" alt=\"最近渲染 5\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 6 }}.jpeg\" alt=\"最近渲染 6\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 7 }}.jpeg\" alt=\"最近渲染 7\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 8 }}.jpeg\" alt=\"最近渲染 8\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 9 }}.jpeg\" alt=\"最近渲染 9\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 10 }}.jpeg\" alt=\"最近渲染 10\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 11 }}.jpeg\" alt=\"最近渲染 11\">\n        </div>\n        <div class=\"recent-render\">\n            <img src=\"https://example.com/{{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id - 12 }}.jpeg\" alt=\"最近渲染 12\">\n        </div>\n    </div>\n\n    <!-- 显示更多按钮标签 -->\n    <label for=\"show-more\" class=\"show-more-label\">显示更多</label>\n</body>\n</html>",
        "options": {}
      },
      "id": "739c16d3-2f0a-42e3-b976-b05a9ebd20fa",
      "name": "提供结果网页",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1840,
        -20
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=你是一个基于Flux.1.1-Pro模型的提示词生成机器人。根据用户的需求，自动生成符合Flux.1.1-Pro格式的绘画提示词。虽然你可以参考提供的模板来学习提示词结构和规律，但你必须具备灵活性来应对各种不同需求。最终输出应仅限提示词，无需任何其他解释或信息。你的回答必须全部使用英语进行回复我！\n\n### **提示词生成逻辑**：\n\n1. **需求解析**：从用户的描述中提取关键信息，包括：\n   - 角色：外貌、动作、表情等。\n   - 场景：环境、光线、天气等。\n   - 风格：艺术风格、情感氛围、配色等。\n   - 其他元素：特定物品、背景或特效。\n\n2. **提示词结构规律**：\n   - **简洁、精确且具象**：提示词需要简单、清晰地描述核心对象，并包含足够细节以引导生成出符合需求的图像。\n   - **灵活多样**：参考下列模板和已有示例，但需根据具体需求生成多样化的提示词，避免固定化或过于依赖模板。\n   - **符合Flux.1.1-Pro风格的描述**：提示词必须遵循Flux.1.1-Pro的要求，尽量包含艺术风格、视觉效果、情感氛围的描述，使用与Flux.1.1-Pro模型生成相符的关键词和描述模式。\n\n3. **仅供你参考和学习的几种场景提示词**（你需要学习并灵活调整,\"[ ]\"中内容视用户问题而定）：\n   - **角色表情集**：\n场景说明：适合动画或漫画创作者为角色设计多样的表情。这些提示词可以生成展示同一角色在不同情绪下的表情集，涵盖快乐、悲伤、愤怒等多种情感。\n\n提示词：An anime [SUBJECT], animated expression reference sheet, character design, reference sheet, turnaround, lofi style, soft colors, gentle natural linework, key art, range of emotions, happy sad mad scared nervous embarrassed confused neutral, hand drawn, award winning anime, fully clothed\n\n[SUBJECT] character, animation expression reference sheet with several good animation expressions featuring the same character in each one, showing different faces from the same person in a grid pattern: happy sad mad scared nervous embarrassed confused neutral, super minimalist cartoon style flat muted kawaii pastel color palette, soft dreamy backgrounds, cute round character designs, minimalist facial features, retro-futuristic elements, kawaii style, space themes, gentle line work, slightly muted tones, simple geometric shapes, subtle gradients, oversized clothing on characters, whimsical, soft puffy art, pastels, watercolor\n\n   - **全角度角色视图**：\n场景说明：当需要从现有角色设计中生成不同角度的全身图时，如正面、侧面和背面，适用于角色设计细化或动画建模。\n\n提示词：A character sheet of [SUBJECT] in different poses and angles, including front view, side view, and back view\n\n   - **80 年代复古风格**：\n场景说明：适合希望创造 80 年代复古风格照片效果的艺术家或设计师。这些提示词可以生成带有怀旧感的模糊宝丽来风格照片。\n\n提示词：blurry polaroid of [a simple description of the scene], 1980s.\n\n   - **智能手机内部展示**：\n场景说明：适合需要展示智能手机等产品设计的科技博客作者或产品设计师。这些提示词帮助生成展示手机外观和屏幕内容的图像。\n\n提示词：a iphone product image showing the iphone standing and inside the screen the image is shown\n\n   - **双重曝光效果**：\n场景说明：适合摄影师或视觉艺术家通过双重曝光技术创造深度和情感表达的艺术作品。\n\n提示词：[Abstract style waterfalls, wildlife] inside the silhouette of a [man]’s head that is a double exposure photograph . Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed\n\n   - **高质感电影海报**：\n场景说明：适合需要为电影创建引人注目海报的电影宣传或平面设计师。\n\n提示词：A digital illustration of a movie poster titled [‘Sad Sax: Fury Toad’], [Mad Max] parody poster, featuring [a saxophone-playing toad in a post-apocalyptic desert, with a customized car made of musical instruments], in the background, [a wasteland with other musical vehicle chases], movie title in [a gritty, bold font, dusty and intense color palette].\n\n   - **镜面自拍效果**：\n场景说明：适合想要捕捉日常生活瞬间的摄影师或社交媒体用户。\n\n提示词：Phone photo: A woman stands in front of a mirror, capturing a selfie. The image quality is grainy, with a slight blur softening the details. The lighting is dim, casting shadows that obscure her features. [The room is cluttered, with clothes strewn across the bed and an unmade blanket. Her expression is casual, full of concentration], while the old iPhone struggles to focus, giving the photo an authentic, unpolished feel. The mirror shows smudges and fingerprints, adding to the raw, everyday atmosphere of the scene.\n\n   - **像素艺术创作**：\n场景说明：适合像素艺术爱好者或复古游戏开发者创造或复刻经典像素风格图像。\n\n提示词：[Anything you want] pixel art style, pixels, pixel art\n\n   - **以上部分场景仅供你学习，一定要学会灵活变通，以适应任何绘画需求**：\n\n4. **Flux.1.1-Pro提示词要点总结**：\n   - **简洁精准的主体描述**：明确图像中核心对象的身份或场景。\n   - **风格和情感氛围的具体描述**：确保提示词包含艺术风格、光线、配色、以及图像的氛围等信息。\n   - **动态与细节的补充**：提示词可包括场景中的动作、情绪、或光影效果等重要细节。\n   - **其他更多规律请自己寻找**\n---\n\n**问答案例**：\n**用户输入**：一个80年代复古风格的照片。\n**你的输出**：`A blurry polaroid of a 1980s living room, with vintage furniture, soft pastel tones, and a nostalgic, grainy texture,  The sunlight filters through old curtains, casting long, warm shadows on the wooden floor, 1980s,`\n\n**问答案例2**：\n**用户输入**：一个赛博朋克风格的夜晚城市背景。\n**你的输出**：`A futuristic cityscape at night, in a cyberpunk style, with neon lights reflecting off wet streets, towering skyscrapers, and a glowing, high-tech atmosphere. Dark shadows contrast with vibrant neon signs, creating a dramatic, dystopian mood.`\n\n用户的输入为：{{ $('n8n 表单触发器').item.json.Prompt }}\n\n"
      },
      "id": "a1d211b3-53fe-4345-a435-312d0f7862d9",
      "name": "LLM生成提示词",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [
        -1000,
        100
      ],
      "retryOnFail": true,
      "notesInFlow": true,
      "alwaysOutputData": false
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"formSubmittedText\": \"Fal API调用失败，重试或刷新试试 \"\n}",
        "options": {}
      },
      "id": "69af9d23-a284-4957-a0a9-160888300ade",
      "name": "回复错误1",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        660,
        220
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=你是一个基于Flux.1.1-Pro模型的提示词生成机器人。根据用户的需求，自动生成符合Flux.1.1-Pro格式的绘画提示词。虽然你可以参考提供的模板来学习提示词结构和规律，但你必须具备灵活性来应对各种不同需求。最终输出应仅限提示词，无需任何其他解释或信息。你的回答必须全部使用英语进行回复我！\n\n### **提示词生成逻辑**：\n\n1. **需求解析**：从用户的描述中提取关键信息，包括：\n   - 角色：外貌、动作、表情等。\n   - 场景：环境、光线、天气等。\n   - 风格：艺术风格、情感氛围、配色等。\n   - 其他元素：特定物品、背景或特效。\n\n2. **提示词结构规律**：\n   - **简洁、精确且具象**：提示词需要简单、清晰地描述核心对象，并包含足够细节以引导生成出符合需求的图像。\n   - **灵活多样**：参考下列模板和已有示例，但需根据具体需求生成多样化的提示词，避免固定化或过于依赖模板。\n   - **符合Flux.1.1-Pro风格的描述**：提示词必须遵循Flux.1.1-Pro的要求，尽量包含艺术风格、视觉效果、情感氛围的描述，使用与Flux.1.1-Pro模型生成相符的关键词和描述模式。\n\n3. **仅供你参考和学习的几种场景提示词**（你需要学习并灵活调整,\"[ ]\"中内容视用户问题而定）：\n   - **角色表情集**：\n场景说明：适合动画或漫画创作者为角色设计多样的表情。这些提示词可以生成展示同一角色在不同情绪下的表情集，涵盖快乐、悲伤、愤怒等多种情感。\n\n提示词：An anime [SUBJECT], animated expression reference sheet, character design, reference sheet, turnaround, lofi style, soft colors, gentle natural linework, key art, range of emotions, happy sad mad scared nervous embarrassed confused neutral, hand drawn, award winning anime, fully clothed\n\n[SUBJECT] character, animation expression reference sheet with several good animation expressions featuring the same character in each one, showing different faces from the same person in a grid pattern: happy sad mad scared nervous embarrassed confused neutral, super minimalist cartoon style flat muted kawaii pastel color palette, soft dreamy backgrounds, cute round character designs, minimalist facial features, retro-futuristic elements, kawaii style, space themes, gentle line work, slightly muted tones, simple geometric shapes, subtle gradients, oversized clothing on characters, whimsical, soft puffy art, pastels, watercolor\n\n   - **全角度角色视图**：\n场景说明：当需要从现有角色设计中生成不同角度的全身图时，如正面、侧面和背面，适用于角色设计细化或动画建模。\n\n提示词：A character sheet of [SUBJECT] in different poses and angles, including front view, side view, and back view\n\n   - **80 年代复古风格**：\n场景说明：适合希望创造 80 年代复古风格照片效果的艺术家或设计师。这些提示词可以生成带有怀旧感的模糊宝丽来风格照片。\n\n提示词：blurry polaroid of [a simple description of the scene], 1980s.\n\n   - **智能手机内部展示**：\n场景说明：适合需要展示智能手机等产品设计的科技博客作者或产品设计师。这些提示词帮助生成展示手机外观和屏幕内容的图像。\n\n提示词：a iphone product image showing the iphone standing and inside the screen the image is shown\n\n   - **双重曝光效果**：\n场景说明：适合摄影师或视觉艺术家通过双重曝光技术创造深度和情感表达的艺术作品。\n\n提示词：[Abstract style waterfalls, wildlife] inside the silhouette of a [man]’s head that is a double exposure photograph . Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed\n\n   - **高质感电影海报**：\n场景说明：适合需要为电影创建引人注目海报的电影宣传或平面设计师。\n\n提示词：A digital illustration of a movie poster titled [‘Sad Sax: Fury Toad’], [Mad Max] parody poster, featuring [a saxophone-playing toad in a post-apocalyptic desert, with a customized car made of musical instruments], in the background, [a wasteland with other musical vehicle chases], movie title in [a gritty, bold font, dusty and intense color palette].\n\n   - **镜面自拍效果**：\n场景说明：适合想要捕捉日常生活瞬间的摄影师或社交媒体用户。\n\n提示词：Phone photo: A woman stands in front of a mirror, capturing a selfie. The image quality is grainy, with a slight blur softening the details. The lighting is dim, casting shadows that obscure her features. [The room is cluttered, with clothes strewn across the bed and an unmade blanket. Her expression is casual, full of concentration], while the old iPhone struggles to focus, giving the photo an authentic, unpolished feel. The mirror shows smudges and fingerprints, adding to the raw, everyday atmosphere of the scene.\n\n   - **像素艺术创作**：\n场景说明：适合像素艺术爱好者或复古游戏开发者创造或复刻经典像素风格图像。\n\n提示词：[Anything you want] pixel art style, pixels, pixel art\n\n   - **以上部分场景仅供你学习，一定要学会灵活变通，以适应任何绘画需求**：\n\n4. **Flux.1.1-Pro提示词要点总结**：\n   - **简洁精准的主体描述**：明确图像中核心对象的身份或场景。\n   - **风格和情感氛围的具体描述**：确保提示词包含艺术风格、光线、配色、以及图像的氛围等信息。\n   - **动态与细节的补充**：提示词可包括场景中的动作、情绪、或光影效果等重要细节。\n   - **其他更多规律请自己寻找**\n---\n\n**问答案例**：\n**用户输入**：一个80年代复古风格的照片。\n**你的输出**：`A blurry polaroid of a 1980s living room, with vintage furniture, soft pastel tones, and a nostalgic, grainy texture,  The sunlight filters through old curtains, casting long, warm shadows on the wooden floor, 1980s,`\n\n**问答案例2**：\n**用户输入**：一个赛博朋克风格的夜晚城市背景。\n**你的输出**：`A futuristic cityscape at night, in a cyberpunk style, with neon lights reflecting off wet streets, towering skyscrapers, and a glowing, high-tech atmosphere. Dark shadows contrast with vibrant neon signs, creating a dramatic, dystopian mood.`\n\n用户的输入为：{{ $('n8n 表单触发器').item.json.Prompt }}\n\n并结合根据图片生成类似图片内容的提示词：",
        "messages": {
          "messageValues": [
            {
              "type": "HumanMessagePromptTemplate",
              "messageType": "imageBinary",
              "binaryImageDataKey": "_________"
            }
          ]
        }
      },
      "id": "a7291099-f745-45ff-9de4-1267e2e6056f",
      "name": "LLM生成提示词1",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [
        -1000,
        600
      ],
      "retryOnFail": true,
      "notesInFlow": true,
      "alwaysOutputData": false
    },
    {
      "parameters": {
        "modelName": "models/gemini-2.0-flash",
        "options": {
          "maxOutputTokens": 8192
        }
      },
      "id": "947df082-0b3f-4d19-885c-3c7ea502d585",
      "name": "Google Gemini Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "typeVersion": 1,
      "position": [
        -900,
        820
      ],
      "credentials": {
        "googlePalmApi": {
          "id": "yXdIBAJcqR818b91",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    },
    {
      "parameters": {
        "modelName": "models/gemini-2.0-flash",
        "options": {
          "maxOutputTokens": 8192
        }
      },
      "id": "1b3bcbe3-b439-446d-a828-907d499935e8",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "typeVersion": 1,
      "position": [
        -900,
        320
      ],
      "credentials": {
        "googlePalmApi": {
          "id": "yXdIBAJcqR818b91",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"formSubmittedText\": \"警告！生成的图片疑似含有敏感内容 \"\n}",
        "options": {}
      },
      "id": "502003a8-dcd3-479d-b5ce-e5f0f38a17dd",
      "name": "绘画含有敏感内容",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1620,
        320
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=rule of thirds, asymmetric composition, glitch art, pixelation, VHS noise, octane render, unreal engine, 8k ::7 --ar 16:9 --s 1200\nDesign a glitchy, post-analog world with digital decay and broken visuals. Utilize pixelated elements, VHS noise, and neon glitches to create a fragmented aesthetic. Use bold, contrasting colors against muted backgrounds for a high-contrast, otherworldly feel. The composition should follow asymmetrical rules, focusing on chaotic yet intentional visual balance. Include:"
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "aa66a625-d38b-4166-9e1d-30548a39e46e",
      "name": "Post-Analog Glitchscape",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        100
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=golden ratio, rule of thirds, cyberpunk, glitch art, octane render, cinematic realism, 8k ::7 --ar 16:9 --s 1000\nCreate a hyper-realistic yet surreal landscape that bends reality, incorporating dreamlike elements and exaggerated proportions. Use vibrant, almost neon colors, and focus on a sense of wonder, play, and fantasy. Include:\n"
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "0ddbe0d9-9f5a-4784-a03f-33c624fdc68a",
      "name": "Hyper-Surreal Escape",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        -100
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=Include: "
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "065d17e6-d10c-4bf6-8d93-2ef320caaee0",
      "name": "None",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        900
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=asymmetric composition, golden ratio, neon colors, abstract forms, octane render, cinematic realism, unreal engine, 8k ::7 --ar 16:9 --s 1000\nCreate a bold, vivid composition using neon colors and fluid shapes that break away from reality. Focus on abstract forms, blending Fauvism's exaggerated color palette with modern digital art techniques. Use asymmetric composition and dynamic lighting. Render with a vibrant, high-energy aesthetic. Include:"
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "c969a2cc-d938-4260-bd0e-d2928b5a2cd1",
      "name": "Neon Fauvism",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        500
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=golden ratio, rule of thirds, cyberpunk, glitch art, octane render, cinematic realism, 8k ::7 --ar 16:9 --s 1000\n\nGenerate a futuristic, cyberpunk dystopia with metallic textures, digital glitches, and neon lights. Blend cold, dystopian structures with traces of organic life. Use photorealistic lighting and dynamic reflections to enhance the visual depth of the scene. Include:"
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "486b0f63-48fd-4ca3-83f2-4bde88ca2ce3",
      "name": "AI Dystopia",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        300
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9ec60f33-b940-40a6-9f8a-cb944b7065f1",
              "name": "stylePrompt",
              "type": "string",
              "value": "=rule of thirds, golden ratio, hyper-maximalist, vibrant neon, high-contrast, octane render, photorealism, 8k ::7 --ar 16:9 --s 1000\n\nDesign a fun, energetic scene filled with bold, neon colors, and playful shapes that pop off the screen. The image should evoke a sense of joy and movement, using fluid, organic forms and exaggerated, cartoon-like proportions. Focus on creating a lively atmosphere with contrasting, saturated tones and dynamic lighting. Use a mix of asymmetrical and balanced compositions to create a playful visual flow. Render in 8K with a hyper-maximalist approach using Octane Render for vibrant, high-gloss textures and photorealistic lighting effects. Include:"
            }
          ]
        },
        "includeOtherFields": true,
        "options": {}
      },
      "id": "adc7221f-3f94-4c96-9695-c0aead702da1",
      "name": "Vivid Pop Explosion",
      "type": "n8n-nodes-base.set",
      "position": [
        -180,
        700
      ],
      "notesInFlow": true,
      "typeVersion": 3.4,
      "notes": " "
    },
    {
      "parameters": {
        "operation": "upload",
        "bucketName": "sharex",
        "fileName": "={{ $now.toFormat('yyyy') }}/{{ $now.toFormat('MM') }}/{{ $execution.id }}.jpeg",
        "additionalFields": {}
      },
      "id": "27fec39c-22ab-43c9-b9be-1bab103e2482",
      "name": "将图片上传到 R1",
      "type": "n8n-nodes-base.s3",
      "position": [
        1400,
        240
      ],
      "typeVersion": 1,
      "credentials": {
        "s3": {
          "id": "cGoeWIvIale73WGL",
          "name": "S3 account"
        }
      },
      "onError": "continueErrorOutput"
    },
    {
      "parameters": {
        "path": "4258eb4a-e4da-41a3-9c9d-60cf7d637159",
        "formTitle": "Flux绘画生成",
        "formDescription": "教程见LinuxDo",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Prompt",
              "fieldType": "textarea",
              "placeholder": "落日晚霞",
              "requiredField": true
            },
            {
              "fieldLabel": "图片比例",
              "fieldType": "dropdown",
              "fieldOptions": {
                "values": [
                  {
                    "option": "21:9"
                  },
                  {
                    "option": "16:9"
                  },
                  {
                    "option": "4:3"
                  },
                  {
                    "option": "3:2"
                  },
                  {
                    "option": "1:1"
                  },
                  {
                    "option": "2:3"
                  },
                  {
                    "option": "3:4"
                  },
                  {
                    "option": "9:16"
                  },
                  {
                    "option": "9:21"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "Style",
              "fieldType": "dropdown",
              "fieldOptions": {
                "values": [
                  {
                    "option": "超现实逃逸"
                  },
                  {
                    "option": "霓虹野兽派"
                  },
                  {
                    "option": "后模拟故障景观"
                  },
                  {
                    "option": "AI 反乌托邦"
                  },
                  {
                    "option": "鲜艳流行爆炸"
                  }
                ]
              }
            },
            {
              "fieldLabel": "图生图（上传启用）",
              "fieldType": "file",
              "multipleFiles": false,
              "acceptFileTypes": " .jpg, .png, .webp"
            }
          ]
        },
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "1f006976-319b-4c36-b7f7-1aa02ad1c0c1",
      "name": "n8n 表单触发器",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -1440,
        400
      ],
      "webhookId": "4258eb4a-e4da-41a3-9c9d-60cf7d637159",
      "typeVersion": 2.1
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "bcc59de6-80ae-4174-bf8f-320844566fe0",
              "leftValue": "={{ $json['图生图（上传启用）'] }}",
              "rightValue": "否",
              "operator": {
                "type": "object",
                "operation": "notExists",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "a8030db4-6162-43e0-a3ee-5ea835e0768f",
      "name": "If条件判断",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        -1220,
        400
      ],
      "retryOnFail": true,
      "notesInFlow": true,
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"formSubmittedText\": \"Fal API调用失败，重试或刷新试试 \"\n}",
        "options": {}
      },
      "id": "1d58e6c0-4b0e-461c-aa19-68a8af396607",
      "name": "回复错误2",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1840,
        220
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "url": "={{ $('查询进度').item.json.response_url }}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "options": {}
      },
      "id": "a6e18c40-8648-4af4-8665-fb089bba82f0",
      "name": "获取图片",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        1000,
        140
      ],
      "notesInFlow": true,
      "credentials": {
        "httpHeaderAuth": {
          "id": "76rj3DVY3trbLLn0",
          "name": "Header Auth account"
        }
      },
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "url": "={{ $json.status_url }}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "options": {}
      },
      "id": "a332ef87-2a9e-43a2-bc5e-f6f4b81b0c99",
      "name": "查询进度",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        540,
        0
      ],
      "notesInFlow": true,
      "typeVersion": 4.2,
      "credentials": {
        "httpHeaderAuth": {
          "id": "76rj3DVY3trbLLn0",
          "name": "Header Auth account"
        }
      },
      "onError": "continueErrorOutput",
      "notes": " "
    },
    {
      "parameters": {
        "url": "={{ $json.images[0].url }}",
        "options": {}
      },
      "id": "0c48459d-107b-4637-8cd7-73f87889de14",
      "name": "下载图片",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1180,
        240
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "amount": 3
      },
      "id": "0b823a50-5e21-4b81-bf50-3e82bc2750d1",
      "name": "等待3秒",
      "type": "n8n-nodes-base.wait",
      "position": [
        340,
        0
      ],
      "webhookId": "61a8626c-e281-4d4b-abb0-b9d87d1b4e7c",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "bcc59de6-80ae-4174-bf8f-320844566fe0",
              "leftValue": "={{ $json.success }}",
              "rightValue": "否",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "c203e768-de60-44a3-9385-2206428ca9d8",
      "name": "If条件判断2",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1620,
        120
      ],
      "retryOnFail": true,
      "notesInFlow": true,
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "299a7c34-dcff-4991-a73f-5b1a84f188ea",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": "COMPLETED"
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "c2756411-2105-4329-8250-3dc30d2974f0",
      "name": "If条件判断1",
      "type": "n8n-nodes-base.if",
      "position": [
        800,
        160
      ],
      "typeVersion": 2.2
    }
  ],
  "pinData": {},
  "connections": {
    "发起 Fal 绘图 请求": {
      "main": [
        [
          {
            "node": "等待3秒",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "回复错误",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "生成提示词": {
      "main": [
        [
          {
            "node": "按风格路线",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "按风格路线": {
      "main": [
        [
          {
            "node": "Hyper-Surreal Escape",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Post-Analog Glitchscape",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "AI Dystopia",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Neon Fauvism",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Vivid Pop Explosion",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "None",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "LLM生成提示词": {
      "main": [
        [
          {
            "node": "生成提示词",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "LLM生成提示词1": {
      "main": [
        [
          {
            "node": "生成提示词",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "LLM生成提示词1",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "LLM生成提示词",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Post-Analog Glitchscape": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Hyper-Surreal Escape": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "None": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Neon Fauvism": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Dystopia": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Vivid Pop Explosion": {
      "main": [
        [
          {
            "node": "发起 Fal 绘图 请求",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "将图片上传到 R1": {
      "main": [
        [
          {
            "node": "If条件判断2",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "绘画含有敏感内容",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "n8n 表单触发器": {
      "main": [
        [
          {
            "node": "If条件判断",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If条件判断": {
      "main": [
        [
          {
            "node": "LLM生成提示词",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "LLM生成提示词1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "获取图片": {
      "main": [
        [
          {
            "node": "下载图片",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "查询进度": {
      "main": [
        [
          {
            "node": "If条件判断1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "回复错误1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "下载图片": {
      "main": [
        [
          {
            "node": "将图片上传到 R1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "等待3秒": {
      "main": [
        [
          {
            "node": "查询进度",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If条件判断2": {
      "main": [
        [
          {
            "node": "提供结果网页",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "回复错误2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If条件判断1": {
      "main": [
        [
          {
            "node": "获取图片",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "等待3秒",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "38143139-9a32-41b9-9022-e15ae6baea1b",
  "meta": {
    "instanceId": "c663dc114a87535d320f933353d0404a75a864095df6842f6ebc515812f65b1b"
  },
  "id": "dLEksct8cCPNKTE0",
  "tags": []
}
```

## 参考

没有[fal](https://fal.ai/)api也可以使用硅基流动的api,支持flux.1-dev模型,效果也很好,[参考->n8n使用教程案例1-Flux绘画](https://ai.programnotes.cn/p/n8n%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B%E6%A1%88%E4%BE%8B1-flux%E7%BB%98%E7%94%BB/)

- https://linux.do/t/topic/679412