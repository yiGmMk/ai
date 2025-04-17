from trans2hugo import replace_local_image_links

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
