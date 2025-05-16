---
title: "MCP Ultimate Guide"
date: "2025-05-16"
tags: ["MCP", "AI Agent", "Function Calling", "Claude", "AI Application"]
categories: ["Artificial Intelligence", "MCP", "AI Agent", "Technology"]
Description: "This article explores the Model Context Protocol (MCP), explains its breakthrough significance, how it works, and how it is used, and compares the differences between MCP and Function Calling and AI Agent."
author: "guangzhengli"
image: "https://ai.programnotes.cn/img/ai/MCP.png"
---
Core content:
- MCP is an open, universal, consensus protocol standard led by Claude to address the problem of slow integration of AI models with existing systems.
- MCP defines standardized protocols to enable AI models to interact seamlessly with different APIs and data sources, replacing fragmented Agent code integration, thus making AI systems more reliable and efficient.
- MCP Server is the key to implementing AI Agent automation. It acts as an intermediate layer to inform the AI ​​Agent which services, APIs and data sources exist, so that the AI ​​Agent can decide independently whether to call a service to complete the task.

**From** | guangzhengli AI independent development

I haven't updated AI-related blogs in almost a year. On the one hand, I'm busy with side projects. On the other hand, although AI technology is changing with each passing day, there is not much new development of the AI ​​application layer. It's basically the three things that [2023 blog] (https://guangzhengli.com/blog/zh/gpt-embeddings/) are mentioned, Prompt, RAG, and Agent.

However, since Claude (Anthropic) led the release of MCP (Model Context Protocol Model Context Protocol) at the end of November last year, the development of the AI ​​application layer has entered a new era.

However, there seems to be no information on the explanation and development of MCP, so the author decided to organize some of his experiences and thoughts into an article, hoping to help everyone.

## Why is MCP a breakthrough

We know that AI models have developed very rapidly over the past year, and from GPT 4 to Claude Sonnet 3.5 to Deepseek R1, both reasoning and hallucination have improved very significantly.

There are many new AI applications, but one thing we can all feel is that the AI ​​applications on the market are basically brand new services and do not integrate with our usual services and systems. In other words, the integration of AI models and our existing systems is developing very slowly.

For example, we cannot currently use an AI application to search online, send emails, publish your own blog, etc. It is not difficult to implement these functions individually, but if you want to integrate them all into one system, it will become out of reach.

If you don’t have a specific feeling yet, we can think about daily development and imagine that in IDE, we can do the following tasks through IDE’s AI.

* Ask AI to query the existing data from the local database to assist in development
* Ask AI to search Github Issue to determine if a problem is a known bug
* Code Review via AI to send comments from a PR to colleagues' instant messaging software (such as Slack)
* Complete deployment through AI query or even modify the current AWS and Azure configuration

The functions mentioned above are now becoming a reality through MCP. You can follow [Cursor MCP](https://docs.cursor.com/context/model-context-protocol) and [Windsurf MCP](https://www.youtube.com/watch?v=Y_kaQmhGmZk) for more information. You can try the Cursor MCP + [browsertools](https://browsertools.agentdesk.ai/installation) plug-in to experience the ability to automatically obtain Chrome dev tools console log in Cursor.

Why is AI integration of existing services so slow? There are many reasons for this. On the one hand, enterprise-level data is very sensitive, and most companies take a long time and process to move. Another aspect is the technology aspect, we lack an open, general, and consensus protocol standard.

MCP is an open, general and consensus protocol standard led by Claude (Anthropic). If you are a developer who is familiar with AI models, you must be familiar with Anthropic. They released the Claude 3.5 Sonnet model, which should be the strongest programming AI model so far (3.7😅 was released as soon as it was written).

> I would like to mention here that the best opportunity for release of this protocol should belong to OpenAI. If OpenAI promoted the protocol when it first released GPT, I believe no one would refuse it. However, OpenAI has become CloseAI and has only released one closed GPTs. This standard protocol that requires dominance and consensus is generally difficult to form spontaneously in the community and is generally dominated by industry giants.

After Claude released MCP, the official Claude Desktop opened up MCP functionality and promoted the open source organization [Model Context Protocol](https://github.com/modelcontextprotocol), which is participated by different companies and communities. For example, the following lists some examples of MCP servers being released by different organizations.

### MCP official integrated teaching:

* **[Git](https://github.com/modelcontextprotocol/servers/blob/main/src/git)** - Git Read, operate, search.
* **[GitHub](https://github.com/modelcontextprotocol/servers/blob/main/src/github)** - Repo management, file manipulation, and GitHub API integration.
* **[Google Maps](https://github.com/modelcontextprotocol/servers/blob/main/src/google-maps)** - Integrate Google Map to get location information.
* **[PostgreSQL](https://github.com/modelcontextprotocol/servers/blob/main/src/postgres)** - Read-only database query.
* **[Slack](https://github.com/modelcontextprotocol/servers/blob/main/src/slack)** - Slack message sending and querying.

### 🎖️ Examples of MCP official support by third-party platforms

MCP server built by third-party platforms.

* **[Grafana](https://github.com/grafana/mcp-grafana)** - Search for query data in Grafana.
* **[JetBrains](https://github.com/JetBrains/mcp-jetbrains)** – JetBrains IDEs.
* **[Stripe](https://github.com/stripe/agent-toolkit)** - Interact with the Stripe API.

### 🌎 Community MCP Server

Here are some MCP servers developed and maintained by the open source community.

* **[AWS](https://github.com/rishikavikondala/mcp-server-aws)** - Use LLM to operate AWS resources.
* **[Atlassian](https://github.com/sooperset/mcp-atlassian)** - Interact with Confluence and Jira, including searching/querying Confluence space/pages, accessing Jira Issue and projects.
* **[Google Calendar](https://github.com/v-3/google-calendar)** - Integrate with Google Calendar, schedule, find time, and add/remove events.
* **[Kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - Connect to a Kubernetes cluster and manage pods, deployments, and services.
* **[X (Twitter)](https://github.com/EnesCinr/twitter-mcp)** - Interact with the Twitter API. Post a tweet and search for tweets by query.
* **[YouTube](https://github.com/ZubeidHendricks/youtube-mcp-server)** - Integrate with YouTube API, video management, short video creation, etc.

## Why MCP?

After seeing this, you may have a question. When OpenAI released GPT function calling in 2023, wasn’t it possible to implement similar functions? Isn’t the AI ​​Agent introduced in our previous blog just used to integrate different services? Why is MCP again?

What is the difference between function calling, AI Agent, and MCP?

### Function Calling

* Function Calling refers to the mechanism by which the AI ​​model automatically executes functions based on the context.
* Function Calling acts as a bridge between AI models and external systems. Different models have different implementations of Function Calling, and the methods of code integration are also different. Defined and implemented by different AI model platforms.

If we use Function Calling, we need to provide a set of functions to the LLM through code and provide clear function description, function input and output, then the LLM can reason and execute functions based on clear structured data.

The disadvantage of Function Calling is that it cannot handle many rounds of dialogue and complex needs, and is suitable for tasks with clear boundaries and clear descriptions. If you need to deal with a lot of tasks, then the code of Function Calling is difficult to maintain.

### Model Context Protocol (MCP)

* MCP is a standard protocol, like the Type C protocol of electronic devices (can be charged or transmitted data), allowing AI models to interact seamlessly with different APIs and data sources.
* MCP is designed to replace fragmented Agent code integration, making AI systems more reliable and efficient. By establishing common standards, service providers can launch the AI ​​capabilities they serve based on protocols, thus enabling developers to build more powerful AI applications faster. Developers do not need to re-create the wheel. Open source projects can build a strong AI Agent ecosystem.
* MCP can maintain context between different applications/services, thereby enhancing the overall ability to perform tasks autonomously.

It can be understood that MCP is to layer different tasks, each layer provides specific capabilities, descriptions, and limitations. The MCP Client judges based on different tasks, selects whether a certain capability needs to be called, and then builds an Agent that can handle complex, multi-step dialogue and unified context through the input and output of each layer.

### AI Agent

* AI Agent is an intelligent system that can run autonomously to achieve specific goals. Traditional AI chat only provides advice or requires manual tasks, and AI Agent can analyze specific situations, make decisions, and take action on its own.
* AI Agent can leverage the functional description provided by MCP to understand more context and automate tasks across various platforms/services.

### think

Why is Claude widely accepted after launching MCP? In fact, I have personally participated in the development of several small AI projects in the past year. During the development process, it is really troublesome to integrate AI models into existing systems or third-party systems.

Although there are some frameworks on the market that support Agent development, such as [LangChain Tools](https://www.langchain.com/), [LlamaIndex](https://docs.llamaindex.ai/en/stable/) or [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction).

Although LangChain and LlamaIndex are both open source projects, the overall development is still quite chaotic. First of all, the abstraction level of the code is too high. What you want to promote is to let developers complete certain AI functions in just a few lines of code. This is very useful in the demo stage. However, in actual development, as long as the business starts to be complex, poor code design brings a very bad programming experience. Also, these projects are too commercialized and ignore the construction of the overall ecology.

Another one is the Vercel AI SDK. Although I personally think that the Vercel AI SDK code is better abstract, it is just that the front-end UI combination and some AI functions are packaged well. The biggest problem is that it is too deeply bound to Nextjs and does not support other frameworks and languages.

Therefore, Claude promotes MCP as a good time. First of all, Claude Sonnet 3.5 has a high status in the minds of developers, and MCP is an open standard, so many companies and communities are willing to participate, hoping that Claude can always maintain a good open ecosystem.

The benefits of MCP for community ecology are mainly the following two points:

* Open standards to service providers, which can open their APIs and some capabilities to MCPs.
* No need to remake the wheel, developers can use existing open source MCP services to enhance their agents.

## How MCP works

Then let’s introduce how MCP works. First, let’s take a look at the [official MCP architecture diagram] (https://modelcontextprotocol.io/introduction).

![Image 2: MCP architecture diagram](https://ai.programnotes.cn/img/ai/MCP.png)

It is divided into the following five parts:

* MCP Hosts: Hosts refers to applications where LLM starts connections, such as Cursor, Claude Desktop, [Cline](https://github.com/cline/cline).
* MCP Clients: The client is used to maintain a 1:1 connection to the Server within the Hosts application.
* MCP Servers: Provides context, tools and tips for the Client through standardized protocols.
* Local Data Sources: Local files, databases, and APIs.
* Remote Services: External files, databases, and APIs.

The core of the entire MCP protocol lies in Server, because Host and Client are familiar with computer networks, which are very easy to understand, but how does Server understand it?

Looking at Cursor's AI Agent development process, we will find that the entire process of AI automation will evolve from Chat to Composer to a complete AI Agent.

AI Chat just provides suggestions on how to convert AI responses into behavior and the end result, all relying on humans, such as manual copy-paste, or making some modifications.

AI Composer can automatically modify code, but requires human participation and confirmation, and cannot do other operations other than modifying code.

AI Agent is a completely automated program. In the future, it can automatically read Figma pictures, automatically produce code, automatically read logs, automatically debug code, and automatically push code to GitHub.

MCP Server exists to realize the automation of AI Agent. It is an intermediate layer that tells the AI ​​Agent which services, APIs, and data sources currently exist. The AI ​​Agent can decide whether to call a certain service based on the information provided by the server, and then execute the functions through Function Calling.

### How MCP Server Works

Let's first look at a simple example. Suppose we want the AI ​​Agent to automatically search for GitHub Repository, then search for Issue, then determine whether it is a known bug, and finally decide whether we need to submit a new Issue function.

Then we need to create a Github MCP Server, which needs to provide three capabilities: finding Repository, searching Issues and creating Issue.

Let's take a look at the code:

```ts
const server = new Server(
  {
    name: "github-mcp-server",
    version: VERSION,
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async() => {
  return {
    tools: [
      {
        name: "search_repositories",
        Description: "Search for GitHub repositories",
        inputSchema: zodToJsonSchema(repository.SearchRepositoriesSchema),
      },
      {
        name: "create_issue",
        Description: "Create a new issue in a GitHub repository",
        inputSchema: zodToJsonSchema(issues.CreateIssueSchema),
      },
      {
        name: "search_issues",
        Description: "Search for issues and pull requests across GitHub repositories",
        inputSchema: zodToJsonSchema(search.SearchIssuesSchema),
      }
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    if (!request.params.arguments) {
      throw new Error("Arguments are required");
    }

    switch (request.params.name) {
      case "search_repositories": {
        const args = repository.SearchRepositoriesSchema.parse(request.params.arguments);
        const results = await repository.searchRepositories(
            args.query,          args.page,          args.perPage        );       
            return {          
                content: [{ 
                    type: "text", 
                    text: JSON.stringify(results, null, 2) }],        };   
                       }      
      case "create_issue": {        
        const args = issues.CreateIssueSchema.parse(request.params.arguments);        
        const { owner, repo, ...options } = args;        
        const issue = await issues.createIssue(owner, repo, options);       
                        return {          content: [{ type: "text", text: JSON.stringify(issue, null, 2) }],        };      }     
       case "search_issues": {       
         const args = search.SearchIssuesSchema.parse(request.params.arguments);        
         const results = await search.searchIssues(args);        
         return {          content: [{ type: "text", text: JSON.stringify(results, null, 2) }],        };      }      
        default:        
            throw new Error(`Unknown tool: ${request.params.name}`);    }  } catch (error) {}});
            async function runServer() {  const transport = new StdioServerTransport(); 
            await server.connect(transport);  
                       console.error("GitHub MCP Server running on stdio");}runServer().catch((error) => { 
                         console.error("Fatal error in main():", error);  process.exit(1);});
```

In the above code, we use `server.setRequestHandler` to tell the Client what capabilities we provide, describe the role of this capability through the `description` field, and describe the input parameters required to complete this capability through the `inputSchema`.

Let's take a look at the specific implementation code:

```ts
export const SearchOptions = z.object({
  q: z.string(),
  order: z.enum(["asc", "desc"]).optional(),
  page: z.number().min(1).optional(),
  per_page: z.number().min(1).max(100).optional(),
});

export const SearchIssuesOptions = SearchOptions.extend({
  sort: z.enum([
    "comments",
    ...  ]).optional(),
});

export async function searchUsers(params: z.infer<typeof SearchUsersSchema>) {
  return githubRequest(buildUrl("https://api.github.com/search/users", params));
}

export const SearchRepositoriesSchema = z.object({
  query: z.string().describe("Search query (see GitHub search syntax)"),
  page: z.number().optional().describe("Page number for pagination (default: 1)"),
  perPage: z.number().optional().describe("Number of results per page (default: 30, max: 100)"),
});

export async function searchRepositories(
  query: string,
  page: number = 1,
  perPage: number = 30
) {
  const url = new URL("https://api.github.com/search/repositories");
  url.searchParams.append("q", query);
  url.searchParams.append("page", page.toString());
  url.searchParams.append("per_page", perPage.toString());

  const response = await githubRequest(url.toString());
  return GitHubSearchResponseSchema.parse(response);
}
```

It can be clearly seen that our final implementation uses the `https://api.github.com` API to interact with Github. We use the `githubRequest` function to call the GitHub API and finally return the result.

Before calling the official Github API, MCP's main job is to describe what capabilities the Server provides (provided to LLM), which parameters are needed (what the specific functions of the parameters are), and what the final result is returned.

So MCP Server is not a novel and advanced thing, it is just a consensus protocol.

If we want to implement a more powerful AI Agent, for example, we want the AI ​​Agent to automatically search for the relevant GitHub Repository based on the local error log, then search for Issue, and finally send the result to Slack.

Then we may need to create three different MCP Servers, one is Local Log Server, used to query local logs; one is GitHub Server, used to search for Issue; and the other is Slack Server, used to send messages.

After the user enters the ``I need to query the local error log and send the relevant Issue to the Slack` instruction, I will judge which MCP Servers to call by myself and decide the order of call. Finally, based on the results returned by different MCP Servers, I will decide whether the next server needs to be called to complete the entire task.

## How to use MCP

If you haven't tried how to use MCP, we can consider using Cursor (I have only tried Cursor), Claude Desktop or Cline to experience it.

Of course, we do not need to develop MCP Servers ourselves. The benefits of MCP are universal and standard, so developers do not need to re-create wheels (but learning can re-create wheels).

The first thing I recommend is some servers from the official organization: [official MCP Server List] (https://github.com/modelcontextprotocol/servers).

At present, the MCP Server in the community is still quite chaotic, with many lacking tutorials and documents, and many code functions are also problematic. We can try some examples of [Cursor Directory](https://cursor.directory/) on our own. The author will not go into details about the specific configuration and actual combat. You can refer to the official documentation.

## Some resources of MCP

Below are some MCP resources that I personally recommend, you can refer to.

*   [https://guangzhengli.com/blog/zh/gpt-embeddings/](https://guangzhengli.com/blog/zh/gpt-embeddings/)
    
*   [https://docs.cursor.com/context/model-context-protocol](https://docs.cursor.com/context/model-context-protocol)
    
*   [https://www.youtube.com/watch?v=Y\_kaQmhGmZk](https://www.youtube.com/watch?v=Y_kaQmhGmZk)
    
*   [https://browsertools.agentdesk.ai/installation](https://browsertools.agentdesk.ai/installation)
    
*   [https://github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)
    
*   [https://github.com/grafana/mcp-grafana](https://github.com/grafana/mcp-grafana)
    
*   [https://github.com/JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)
    
*   [https://github.com/stripe/agent-toolkit](https://github.com/stripe/agent-toolkit)
    
*   [https://github.com/rishikavikondala/mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)
    
*   [https://github.com/sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)
    
*   [https://github.com/v-3/google-calendar](https://github.com/v-3/google-calendar)
    
*   [https://github.com/Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)
    
*   [https://github.com/EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp)
    
*   [https://github.com/ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)
    
*   [https://www.langchain.com/](https://www.langchain.com/)
    
*   [https://docs.llamaindex.ai/en/stable/](https://docs.llamaindex.ai/en/stable/)
    
*   [https://sdk.vercel.ai/docs/introduction](https://sdk.vercel.ai/docs/introduction)
    
*   [https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)
    
*   [https://github.com/cline/cline](https://github.com/cline/cline)
    
*   [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
    
*   [https://www.anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)
    
*   [https://cursor.directory](https://cursor.directory/)
    
*   [https://www.pulsemcp.com/](https://www.pulsemcp.com/)
    
*   [https://glama.ai/mcp/servers](https://glama.ai/mcp/servers)
*   [为什么 MCP 是一个突破](https://guangzhengli.com/blog/zh/model-context-protocol#%E4%B8%BA%E4%BB%80%E4%B9%88-mcp-%E6%98%AF%E4%B8%80%E4%B8%AA%E7%AA%81%E7%A0%B4)
    
*   [MCP 官方集成教学：](https://guangzhengli.com/blog/zh/model-context-protocol#mcp-%E5%AE%98%E6%96%B9%E9%9B%86%E6%88%90%E6%95%99%E5%AD%A6)
*   [🎖️ 第三方平台官方支持 MCP 的例子](https://guangzhengli.com/blog/zh/model-context-protocol#%EF%B8%8F-%E7%AC%AC%E4%B8%89%E6%96%B9%E5%B9%B3%E5%8F%B0%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81-mcp-%E7%9A%84%E4%BE%8B%E5%AD%90)
*   [🌎 社区 MCP 服务器](https://guangzhengli.com/blog/zh/model-context-protocol#-%E7%A4%BE%E5%8C%BA-mcp-%E6%9C%8D%E5%8A%A1%E5%99%A8)
*   [为什么是 MCP？](https://guangzhengli.com/blog/zh/model-context-protocol#%E4%B8%BA%E4%BB%80%E4%B9%88%E6%98%AF-mcp)
    
*   [Function Calling](https://guangzhengli.com/blog/zh/model-context-protocol#function-calling)
*   [Model Context Protocol (MCP)](https://guangzhengli.com/blog/zh/model-context-protocol#model-context-protocol-mcp)
*   [AI Agent](https://guangzhengli.com/blog/zh/model-context-protocol#ai-agent)
*   [思考](https://guangzhengli.com/blog/zh/model-context-protocol#%E6%80%9D%E8%80%83)
*   [MCP 如何工作](https://guangzhengli.com/blog/zh/model-context-protocol#mcp-%E5%A6%82%E4%BD%95%E5%B7%A5%E4%BD%9C)
    
*   [MCP Server 的工作原理](https://guangzhengli.com/blog/zh/model-context-protocol#mcp-server-%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
*   [如何使用 MCP](https://guangzhengli.com/blog/zh/model-context-protocol#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8-mcp)
    
*   [MCP 的一些资源](https://guangzhengli.com/blog/zh/model-context-protocol#mcp-%E7%9A%84%E4%B8%80%E4%BA%9B%E8%B5%84%E6%BA%90)
    
*   [MCP 官方资源](https://guangzhengli.com/blog/zh/model-context-protocol#mcp-%E5%AE%98%E6%96%B9%E8%B5%84%E6%BA%90)
*   [社区的 MCP Server 的列表](https://guangzhengli.com/blog/zh/model-context-protocol#%E7%A4%BE%E5%8C%BA%E7%9A%84-mcp-server-%E7%9A%84%E5%88%97%E8%A1%A8)
*   [写在最后](https://guangzhengli.com/blog/zh/model-context-protocol#%E5%86%99%E5%9C%A8%E6%9C%80%E5%90%8E)
    
*   [References](https://guangzhengli.com/blog/zh/model-context-protocol#references)
