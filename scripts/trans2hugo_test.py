from trans2hugo import replace_local_image_links, replace_author


def test_1():
    # --- 示例用法 ---
    markdown_input = """
    这是一个 Markdown 示例。
    
    本地图片链接：![本地图片](/path/to/图像 with space.png)
    
    网络图片链接：![网络图片](https://example.com/image.jpg)
    
    另一个本地图片：![图 2](./images/another_image.jpeg)
    
    相对路径：![相对图片](relative/path/image3.gif)
    
    带 data URI 的图片：![Data URI](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...)
    
    普通链接：[这是一个链接](https://google.com)
    """

    base_image_url = "https://your-cdn.com/images/"  # 可以替换成你的基础 URL

    output_content = replace_local_image_links(markdown_input, base_image_url)
    print("--- 原始 Markdown ---")
    print(markdown_input)
    print("\n--- 替换后的 Markdown ---")
    print(output_content)

    # --- 另一个示例，使用默认 base_url ---
    markdown_input_2 = "![我的图片](my_local_pic.jpg)"
    output_content_2 = replace_local_image_links(markdown_input_2)
    print("\n--- 示例 2 ---")
    print(f"输入: {markdown_input_2}")
    print(f"输出: {output_content_2}")


def test_替换作者():
    content = """
#  MCP 正当时：FunctionAI MCP 开发平台来了！  
 
原创 封崇  阿里云云原生   2025-04-14 18:02  

![](087ee75c2a26ff67233996986126ecfa.gif)  
    
MCP：AI 时代的“操作系统接口”,Cloud Native  
2024 年 11 月，Anthropic 发布模型上下文协议（MCP），这一开放标准迅速引发开发者社区的"协议觉醒"。其本质是通过标准化接口实现 LLM 与外部世界的双向交互，正如 USB 协议统一外设接入，MCP 正成为 AI 应用连接数字生态的通用总线。随着 Cursor、Claude   
Desktop

**生态暴发期的痛点**  
尽管 MCP 生态呈现指数级增长，GitHub 仓库星标数半年突破 3.5 万，但生产级落地仍面临三重挑战：  
    """
    output_content = replace_author(content)
    print("--- 替换作者后的 Markdown ---", output_content)


test_1()

print("test2\n")

test_替换作者()
