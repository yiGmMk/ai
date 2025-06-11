---
title: "n8n使用教程案例1-Flux绘画"
date: "2025-06-11"
tags: ["MCP", "AI", "Agent", "Function Call", "工具调用","n8n","Flux"]
categories: ["人工智能", "技术","n8n"]
description: "本文介绍以一种使用flux绘画的n8n工作流"
author: "yi"
image: "https://ai.programnotes.cn/img/n8n/flower-flux.jpg"
---

将以下提示词加到你原本提示词 或者 直接用下方提示词 即可成功调用文生图工具

```bash
你可以调用AI绘画工具，一旦用户需要画画或者有绘画需求或者你觉得有必要调用绘画工具时，请你自行生成符合用户需求的详细英文提示词并填充到下面url的{prompt}占位符中，{width}和{height}占位符的值由你根据情况自行确定，但其值均需小于等于1024，常见的三种长宽值有1024x1024,768x1024,1024x768。这样即表示你已成功生成对应提示词的相关绘画图片:
![image](https://oi.yuychat.cn/webhook/flux?prompt={prompt}&width={width}&height={height}&aiprompt=true)
**URL编码规则**
1. 空格转%20，保留英文双引号
2. URL必须是单行（无换行符）
3. 特殊符号强制编码：
- 加号 `+` → `%2B`
- 括号 `()` → `%28%29`
- 尖括号 `<>` → `%3C%3E`
- 百分号 `%` → `%25`
```

如:

```bash
https://n8n-naflhmto.ap-southeast-1.clawcloudrun.com/webhook-test/flux?prompt=海棠花,春天&width=768&height=1024&aiprompt=true
```

效果:

![海棠花,春天](https://ai.programnotes.cn/img/n8n/flower-flux.jpg)

用n8n可以快速制作一个直接访问url就能生图的工具（无水印） 调用Flux.1 dev模型生图
可以用我免费提供的生图链接，也可以看下面的教程自建一个（自定义程度更高）

- 请求变量	 取值举例	说明
- prompt	任意文本	必填项，描述生成图像的内容
- width	    768	       默认1024，可指定图片宽度
- height	1024	   默认1024，可指定图片高度
- aiprompt	true	   默认true，表示启用AI优化提示词
- seed	    1	       必须大于0小于9999999999，值默认无


## 工作流

由于自部署资源,上面展示的api随时可能失效,请自行搭建工作流体验效果

```json
{
  "name": "FluxGET请求",
  "nodes": [
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.siliconflow.cn/v1/images/generations",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"prompt_enhancement\": {{ $ifEmpty($('GET请求').item.json.query.aiprompt,true) }},\n  \"prompt\": \"{{ $('GET请求').item.json.query.prompt }}\",\n  \"image_size\": \"{{ $ifEmpty($('GET请求').item.json.query.width,1024) }}x{{ $ifEmpty($('GET请求').item.json.query.height,1024) }}\",\n  \"model\": \"black-forest-labs/FLUX.1-dev\",\n  \"seed\": {{ $('GET请求').item.json.query.seed }}\n}",
        "options": {}
      },
      "id": "fa1e2580-0c9d-42d8-af5a-dab81070c9bb",
      "name": "调用 硅基流动 推理 API",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1040,
        620
      ],
      "notesInFlow": true,
      "typeVersion": 4.2,
      "retryOnFail": false,
      "credentials": {
        "httpHeaderAuth": {
          "id": "1Mh74hpnj9mzMB8Q",
          "name": "硅基流动绘画"
        }
      },
      "onError": "continueErrorOutput",
      "notes": " "
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "=硅基流动调用失败：\n{{ $json.error.message }}\n",
        "options": {}
      },
      "id": "86350040-50c5-43bf-8ab7-8bb34655a16e",
      "name": "回复错误1",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1260,
        760
      ],
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "content": "## 如你部署出现报错，请点击上方“Executions”查看报错信息\n教程见：https://linux.do/t/topic/240907",
        "height": 98.39844317099532,
        "width": 719.7846765344628
      },
      "id": "57b5a6d5-b7a6-4bfb-8677-0ff0d3162125",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        720,
        340
      ]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.siliconflow.cn/v1/images/generations",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"prompt_enhancement\": {{ $ifEmpty($('GET请求').item.json.query.aiprompt,true) }},\n  \"prompt\": \"{{ $('GET请求').item.json.query.prompt }}\",\n  \"image_size\": \"{{ $ifEmpty($('GET请求').item.json.query.width,1024) }}x{{ $ifEmpty($('GET请求').item.json.query.height,1024) }}\",\n  \"model\": \"black-forest-labs/FLUX.1-dev\"\n}",
        "options": {}
      },
      "id": "9da5b3cc-3c2e-42d5-bc60-250ea9195019",
      "name": "调用 硅基流动 推理 API1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1040,
        1040
      ],
      "notesInFlow": true,
      "typeVersion": 4.2,
      "retryOnFail": false,
      "credentials": {
        "httpHeaderAuth": {
          "id": "1Mh74hpnj9mzMB8Q",
          "name": "硅基流动绘画"
        }
      },
      "onError": "continueErrorOutput",
      "notes": " "
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "=硅基流动调用失败：\n{{ $json.error.message }}\n",
        "options": {}
      },
      "id": "49f3e434-b3fa-4556-b757-226ce9da6ff5",
      "name": "回复错误",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1260,
        1180
      ],
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
              "id": "06e13542-cb9a-4a81-823e-07c913ba79f9",
              "leftValue": "={{ $('GET请求').item.json.query.seed }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "exists",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        820,
        820
      ],
      "id": "b9846d98-8179-4901-af34-0b21c880b218",
      "name": "Seed值有无"
    },
    {
      "parameters": {
        "path": "flux",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "6101c51c-6315-490f-ac02-a308d61c126c",
      "name": "GET请求",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        660,
        820
      ],
      "webhookId": "a5a9106f-2389-4b29-8423-8c0d94717ed2"
    },
    {
      "parameters": {
        "respondWith": "redirect",
        "redirectURL": "={{ $json.images[0].url }}",
        "options": {}
      },
      "id": "eb710a10-faa5-42d5-83de-324895c48436",
      "name": "成功响应",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1260,
        600
      ]
    },
    {
      "parameters": {
        "respondWith": "redirect",
        "redirectURL": "={{ $json.images[0].url }}",
        "options": {}
      },
      "id": "afaf7f40-e06c-4842-b276-15fa11509acd",
      "name": "成功响应1",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1260,
        1020
      ]
    }
  ],
  "pinData": {},
  "connections": {
    "调用 硅基流动 推理 API": {
      "main": [
        [
          {
            "node": "成功响应",
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
    "调用 硅基流动 推理 API1": {
      "main": [
        [
          {
            "node": "成功响应1",
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
    "Seed值有无": {
      "main": [
        [
          {
            "node": "调用 硅基流动 推理 API",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "调用 硅基流动 推理 API1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GET请求": {
      "main": [
        [
          {
            "node": "Seed值有无",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "12fd6832-cd48-4ea1-9b3c-5ba34ad52a9b",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "273cb072730a54351e245b85466131b67e03b4084264c10b9a2f40e05554ac84"
  },
  "id": "3UgUgC6VPPM3PeMv",
  "tags": []
}
```

## 部署n8n

可以使用claw cloud部署,参考 [Claw免费云服务](https://nav.programnotes.cn/page/claw),在App Store选择n8n部署即可,如果需要最新的版本,修改镜像tag为latest即可

## 参考

- https://linux.do/t/topic/453337