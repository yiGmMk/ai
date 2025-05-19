---
title: "手撸 MCP 管理 GitHub 项目"
date: "2025-05-19"
tags: ["MCP", "GitHub", "go-zero", "AI", "Cline"]
categories: ["AI","MCP", "go-zero", "微服务"]
description: "使用 go-zero 开发 MCP Server，通过 Cline 插件与 GitHub 进行交互，实现 issue 和 PR 的管理。"
author: "zhoushuguang"
image: ""
---

核心内容点:
- 使用 go-zero 框架实现 MCP Server，用于管理 GitHub 项目，包括查看和创建 issue、查看 PR 等操作。
- 通过 VSCode 插件 Cline 配置大模型和 MCP Server，实现自然语言与 GitHub 操作的结合。
- 详细介绍了 MCP Server 的开发过程，包括工具注册、Tool 开发，以及如何通过 GitHub API 实现具体功能。

**源自** |  zhoushuguang  微服务实践   2025-05-19 09:18  
  
MCP（Model Context Protocol）最近真的非常火，OpenAI、谷歌、微软等顶级AI公司都陆续宣布了支持MCP协议。同时，go-zero在v1.8.3版本中也新增了对MCP Server的支持，本篇文章就是基于go-zero mcp的实战。go-zero一直以简单高效而为大家所熟知，通过本次实战大家也会感受到使用go-zero来实现MCP Server同样也非常简单高效。  
  
本篇文章是实战，相关的基础知识在这里就不再赘述，如果对MCP还不了解的话可以自行查阅相关资料学习。  
  
本次实战的场景是基于AI来实现GitHub相关的操作，比如查看issue、创建issue、查看pr等操作。  
  
下面是MCP的架构图，主要由两部分组成，MCP Host和MCP Server，MCP Host选择很多，比如Claude Desktop，各种IDE，Dify等AI工具都集成了MCP Client，本次实战MCP Host是基于Vscode的插件Cline，Cline是一个非常强大的AI编程辅助工具，同时对于MCP也有很好的支持，MCP Server基于go-zero的MCP功能实现。  
  
![](https://ai.programnotes.cn/img/ai/836ceadb424e50318176e1568ffd3081.png)  
  
## zero-mcp-github 项目创建  
  
MCP Server和Http或者Rpc服务的开发没什么太大的区别，区别是MCP Server的Transport一般是通过SSE或者Stdio来实现。goctl工具暂时还不支持生成MCP Server，在后续的版本会支持。所以本次实战的项目通过手动方式创建，结构如下： 

```bash
.
├── README.md
├── etc
│   └── zero-mcp-github.yaml
├── go.mod
├── go.sum
├── internal
│   ├── config
│   │   └── config.go
│   ├── svc
│   │   └── servicecontext.go
│   └── tools
│       ├── issues.go
│       ├── issues_test.go
│       ├── pullrequests.go
│       ├── pullrequests_test.go
│       ├── tool_test.go
│       └── tools.go
└── main.go
```  
  
整体结构上和go-zero的标准结构基本一致，main.go是程序的入口，etc下为mcp server的配置文件，其他的代码都放在internal下，为mcp server的私有代码，svc主要是一些初始化，比如数据库连接的初始化，这个项目在这里主要做github client的初始化，tools是这个项目的核心，所有的mcp tool核心逻辑都在这个package下实现。  
## 入口  
  
创建和启动mcp server，调用tools.NewToolset(mcpSrv, svcCtx)，实现工具的注册。  
```go
func main() {
    flag.Parse()

    logx.DisableStat()

    var c config.Config
    conf.MustLoad(*configFile, &c)

    mcpSrv := mcp.NewMcpServer(c.McpConf)
    defer mcpSrv.Stop()

    svcCtx := svc.NewServiceContext(c)
    tools.NewToolset(mcpSrv, svcCtx)

    fmt.Printf("Starting MCP Server on %s:%d\n", c.McpConf.Host, c.McpConf.Port)
    mcpSrv.Start()
}
```  
## 资源初始化  
  
这里主要是初始化github client。使用github.com/google/go-github/v69/github实现。初始化github client需要传入token。  
```go
type ServiceContext struct {
    Config       config.Config
    GithubClient *github.Client
}

func NewServiceContext(c config.Config) *ServiceContext {
    return &ServiceContext{
        Config:       c,
        GithubClient: github.NewClient(nil).WithAuthToken(c.Github.Token),
    }
}
```  
### Github token获取  
1. 点击右上角头像，再点击Settings。  
  
  ![](https://ai.programnotes.cn/img/ai/d081824a3a54e33ec2fbf8b8b9443b87.png)  
  
2. 进入到Settings页面后，点击Developer settings  
  
    ![](https://ai.programnotes.cn/img/ai/36e59eeaa35639f6a43354944c31c09a.png)  
  
3. 点击Personal access tokens，选择Generate new token，添加描述，然后根据需求选择对应的权限和过期时间，点击Generate Token即可生成。  
  
![](https://ai.programnotes.cn/img/ai/77da52fcd1251386cfeb160700d0922b.png)  
  
![](https://ai.programnotes.cn/img/ai/80d231cb6e84a5d82c295f46fd53735c.png)  
  
## 注册Tools  
  
在addTools方法中，通过调用RegisterTool方法注册自定义的工具，在这里可以扩展任意多的工具。  
```go
func NewToolset(mcpSrv mcp.McpServer, svcCtx *svc.ServiceContext) {
    toolSet := &Toolset{
        svcCtx: svcCtx,
        mcpSrv: mcpSrv,
    }
    toolSet.addTools()
}

func (t *Toolset) addTools() {
    if err := t.mcpSrv.RegisterTool(listIssuesTool(t.svcCtx)); err != nil {
        panic(err)
    }
    if err := t.mcpSrv.RegisterTool(getIssueTool(t.svcCtx)); err != nil {
        panic(err)
    }
    if err := t.mcpSrv.RegisterTool(createIssueTool(t.svcCtx)); err != nil {
        panic(err)
    }
    if err := t.mcpSrv.RegisterTool(listPullRequests(t.svcCtx)); err != nil {
        panic(err)
    }
}
```  

## Tool开发  
  
以list_issues工具为例，来看如何开发一个mcp tool。list_issues工具功能是查看某个repo下的issues，主要包含如下几个部分：  
- • 定义工具名称：list_issues  
  
- • 定义的工具描述：List issues in a GitHub repository. （描述的越准确越有助于AI正确定位该工具）  
  
- • 输入schema的定义：实现该工具需要依赖哪些参数，比如我们这个工具就需要owner、repo等必要的参数，还有state、sort、direction等非必要参数，这些都需要通过schema来描述。  
  
- • Handler定义：真正实现工具的逻辑，在Handler中首先定义了参数，然后解析参数，如果参数解析错误就需要返回错误。到这里大家是不是觉得很神奇呢？以前开发业务接口的时候都是通过API文档和前端协商好需要传递哪些参数，而现在只需要增加参数的描述信息，然后AI就知道需要传递哪些参数，想知道内部的原理，后续的文章再做介绍。  
  
- • Tool逻辑：核心就是解析到参数后，调用github sdk把参数传递进去，拿到结果，这里其实就是我们非常熟悉的传统的开发方式了。拿到结果后返回给AI，最好明确告诉AI结果是正确的还是错误的，以便于AI根据结果正确的输出内容。  
  
通过以上简单的几个步骤就实现了一个MCP Tool，是不是非常简单呢？好像也没啥新东西，都是我们非常熟悉的知识。  
```go
func listIssuesTool(svcCtx *svc.ServiceContext) mcp.Tool {
    var listIssuesTool = func(ctx context.Context, params map[string]any) (any, error) {
        var req struct {
            Owner     string   `json:"owner"`
            Repo      string   `json:"repo"`
            State     string   `json:"state,optional"`
            Labels    []string`json:"labels,optional"`
            Sort      string   `json:"sort,optional"`
            Direction string   `json:"direction,optional"`
            Since     string   `json:"since,optional"`
            Page      float64`json:"page,optional"`
            PerPage   float64`json:"perPage,optional"`
        }
        err := mcp.ParseArguments(params, &req)
        if err != nil {
            returnnil, fmt.Errorf("failed to parse arguments: %w", err)
        }

        var sinceTime time.Time
        if req.Since != "" {
            sinceTime, err = parseISOTimestamp(req.Since)
            if err != nil {
                returnnil, fmt.Errorf("failed to parse timestamp: %w", err)
            }
        }
        opts := &github.IssueListByRepoOptions{
            State:     req.State,
            Labels:    req.Labels,
            Sort:      req.Sort,
            Direction: req.Direction,
            Since:     sinceTime,
            ListOptions: github.ListOptions{
                Page:    int(req.Page),
                PerPage: int(req.PerPage),
            },
        }

        issues, resp, err := svcCtx.GithubClient.Issues.ListByRepo(ctx, req.Owner, req.Repo, opts)
        if err != nil {
            returnnil, fmt.Errorf("failed to list issues: %w", err)
        }
        deferfunc() { _ = resp.Body.Close() }()

        if resp.StatusCode != http.StatusOK {
            body, err := io.ReadAll(resp.Body)
            if err != nil {
                returnnil, fmt.Errorf("failed to read response body: %w", err)
            }
            return mcp.CallToolResult{
                Content: []any{fmt.Sprintf("Error: %s", string(body))},
                IsError: true,
            }, nil
        }

        r, err := json.Marshal(issues)
        if err != nil {
            returnnil, fmt.Errorf("failed to marshal issue: %w", err)
        }
        return mcp.CallToolResult{
            Content: []any{r},
            IsError: false,
        }, nil
    }

    return mcp.Tool{
        Name:        "list_issues",
        Description: "List issues in a GitHub repository.",
        InputSchema: mcp.InputSchema{
            Properties: map[string]any{
                "owner": map[string]any{
                    "type":        "string",
                    "description": "Repository owner",
                },
                "repo": map[string]any{
                    "type":        "string",
                    "description": "Repository name",
                },
                "state": map[string]any{
                    "type":        "string",
                    "description": "TFilter by state",
                    "enum":        []string{"open", "closed", "all"},
                },
                "labels": map[string]any{
                    "type":        "array",
                    "description": "Filter by labels",
                    "items": map[string]any{
                        "type": "string",
                    },
                },
                "sort": map[string]any{
                    "type":        "string",
                    "description": "Sort order",
                    "enum":        []string{"created", "updated", "comments"},
                },
                "direction": map[string]any{
                    "type":        "string",
                    "description": "Sort direction",
                    "enum":        []string{"asc", "desc"},
                },
                "since": map[string]any{
                    "type":        "string",
                    "description": "Filter by date (ISO 8601 timestamp)",
                },
                "page": map[string]any{
                    "type":        "number",
                    "description": "Page number for pagination (min 1)",
                    "minimum":     1,
                },
                "perPage": map[string]any{
                    "type":        "number",
                    "description": "Results per page for pagination (min 1, max 100)",
                    "minimum":     1,
                    "maximum":     100,
                },
            },
            Required: []string{"owner", "repo"},
        },
        Handler: listIssuesTool,
    }
}
```  
## 启动MCP Server  
  
执行go run main.go启动服务  
```bash
Starting MCP Server on 0.0.0.0:8000
{"@timestamp":"2025-05-10T13:39:48.001+08:00","caller":"mcp/server.go:265","content":"New SSE connection established for client fd55b8f8-73a9-4e8a-a00f-125bc14d41e2 (active clients: 1)","level":"info"}
```  

Cline插件在Vscode中安装Cline插件，这个步骤非常简单，自行搜索教程即可。安装后在左侧导航栏会有Cline的图标。接下来需要做两个动作：一是要配置大模型，二是要配置MCP Server。  

## LLM配置  
  
配置流程如下：  
- 点击左侧导航栏的Cline图标  
  
- 在弹出的对话框中，点击右上角的设置图标  
  
- 点击API Provider，下拉框中有很多LLM可以选择，这里选择的是大家都非常熟悉的DeepSeek  
  
- 填入模型的API KEY即可，模型的API KEY获取请参考对应模型的文档  
  
- 点击右上角的Save按钮保存，配置完成  
  
![](https://ai.programnotes.cn/img/ai/5558f8b47a892b6f926696e8dbebd343.png)  
  
## MCP Server配置  
  
配置流程如下：  
- 点击对话框右上角的工具按钮  
  
- 在弹出的MCP Server页面中，选择Remote Servers  
  
- 点击Edit Configuration按钮，通过配置文件的方式添加MCP Server，文件中可以添加多个MCP Server  
  
- 定义个名称(github)，url为mcp server的地址，autoApprove可以输入对应的工具名称，要不然每次调用工具的时候都需要确认  
  
- 配置如下内容如下：
```json
{
  "mcpServers":{
    "github":{
      "url":"http://localhost:8000/sse",
      "headers":{},
      "autoApprove":[],
      "disabled":false
    }
  }
}
```  
  
![](https://ai.programnotes.cn/img/ai/1c3bc432a6212e9b9873040a4892ea32.png)  
  
切换到Installed Tab下，可以看到已经安装的MCP Server，同时这里还会列出MCP Server提供的工具，以及参数信息等。通过点击红框出的按钮可以切换该MCP Server的启动和关闭状态。  
  
![](https://ai.programnotes.cn/img/ai/2478909b70570862e08f13a3950775e9.png)  
# 效果验证  
  
经过了MCP Server的开发，Cline大模型和MCP Server的配置后，终于可以来进行效果验证了。  
  
点击右上角的+号按钮，打开一个新的对话窗口，在聊天框中输入内容 “查看zhoushuguang/beyond这个repo下的issue” ，我们想查看这个仓库下有哪些issue。  
  
大模型自动识别出当前已经有github相关的工具list_issues，并且自动拼装了owner和repo参数，到这里会停住，需要我们手动确认调用该工具，如果默认允许调用的话勾选Auto-approve即可，后续就会自动调用。  
  
![](https://ai.programnotes.cn/img/ai/431d0bca04834817336179b2ec01e895.png)  
  
大模型把工具返回的结果进行分析后返回给用户，包括了issue的id，创建时间，作者，甚至还贴出了链接，非常的人性化。  
  
![](https://ai.programnotes.cn/img/ai/0ac14cf193c5487d6424a1526c399beb.png)  
  
再试一下创建issue，内容是 “在zhoushuguang/beyond这个repo下创建一个issue，标题是：这是mcp-github测试的issue，内容是：这是mcp-github测试的issue”。  
  
![](https://ai.programnotes.cn/img/ai/d7f0c18f0a65a6917d96b71e7abf7893.png)  
  
打开github仓库，查看issue，果然新创建了一个id为56的issue。  
  
![](https://ai.programnotes.cn/img/ai/d1989dd8d8645c3d90146ef53da483ea.png)  

# 总结  
  
本次实战和大家一起使用go-zero开发了一个关于github操作的mcp-server，并且借助cline验证了效果。MCP的出现使得大模型调用外部工具更加规范和方便，通过自然语言结合MCP就能够让大模型为我真正的工作，而不仅仅局限在和大模型聊天上。  
  
希望本次实战能给大家带来一点点收获，也感受到大模型和MCP的魅力，后续将持续分享AI相关技术。  
  
代码地址：https://github.com/zhoushuguang/zero-mcp-github  

## 项目地址  
  
https://github.com/zeromicro/go-zero  

  
   
  
  
