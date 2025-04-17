import sys
import os
import re
from urllib.parse import quote, urlparse
from prompt.tran2hugo import prompt as tran2hugo_prompt
from xlib.gpt import call_openai


def replace_local_image_links(
    markdown_content, base_url="https://ai.programnotes.cn/img/ai/"
):
    """
    查找 Markdown 文本中的本地图片链接，并将其替换为指定的网络 URL。

    Args:
        markdown_content (str): 包含 Markdown 文本的字符串。
        base_url (str): 用于构建新网络链接的基础 URL。

    Returns:
        str: 替换了本地图片链接后的 Markdown 文本。
    """

    def replace_link(match):
        """
        re.sub 的回调函数，用于处理每个匹配到的链接。
        """
        link_text = match.group(1)  # 图片的 Alt 文本
        link_url = match.group(2)  # 图片的原始 URL

        # print(f"找到链接: text='{link_text}', url='{link_url}'") # 调试信息

        # 检查 URL 是否是网络链接 (http/https) 或 data URI
        parsed_url = urlparse(link_url)
        if parsed_url.scheme in ["http", "https", "data"]:
            # 如果是网络链接或 data URI，则不替换，直接返回原匹配内容
            # print(f"跳过网络链接: {link_url}") # 调试信息
            return match.group(0)  # 返回整个匹配到的字符串，例如 ![]()
        else:
            # 假定为本地链接或相对路径
            try:
                # 提取文件名
                filename = os.path.basename(link_url)
                # 对文件名进行 URL 编码，确保 URL 安全性
                encoded_filename = quote(filename)
                # 构建新的网络 URL
                new_url = f"{base_url.rstrip('/')}/{encoded_filename}"  # 确保 base_url 末尾没有多余的斜杠
                # print(f"替换为: {new_url}") # 调试信息
                # 返回替换后的 Markdown 图片链接
                return f"![{link_text}]({new_url})"
            except Exception as e:
                # print(f"处理链接时出错 '{link_url}': {e}") # 调试信息
                # 如果处理过程中发生错误，返回原始匹配，避免破坏内容
                return match.group(0)

    # 正则表达式仅查找 Markdown 图片链接： ![alt text](url)
    # - !\[       匹配开头的 "!["
    # - ([^\]]+)  匹配并捕获 "]" 之前的任何非 "]" 字符 (alt 文本)
    # - \]        匹配 "]"
    # - \(        匹配 "("
    # - ([^)]+)   匹配并捕获 ")" 之前的任何非 ")" 字符 (URL)
    # - \)        匹配 ")"
    markdown_image_link_regex = (
        r"!\[([^\]]*)\]\(([^)]+)\)"  # 注意: alt 文本可以是空的，所以用 * 代替 +
    )

    # 使用 re.sub 和回调函数进行替换
    replaced_content = re.sub(markdown_image_link_regex, replace_link, markdown_content)

    return replaced_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python trans2hugo.py <markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]

    try:
        with open(markdown_file, "r", encoding="utf-8") as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {markdown_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    modified_content = replace_local_image_links(markdown_content)

    try:
        header = call_openai(tran2hugo_prompt, modified_content)
        print("hugo header", header)

        # 作者
        modified_content = replace_author(modified_content)

        # 去除markdown的1级标题,将header与剩余部分拼在一起
        post = replace_title(modified_content, header)
        try:
            with open(markdown_file, "w", encoding="utf-8") as f:
                f.write(post)
            print(f"Successfully wrote converted content to {markdown_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"Error during GPT conversion: {e}")
        sys.exit(1)


def replace_title(content: str, header: str) -> str:
    # 使用正则匹配以"#"开头的行作为标题
    match = re.match(r"^# (.*)", content, re.MULTILINE)

    if match:
        # 获取匹配到的完整标题行（包括"# "）
        full_header = match.group(0)
        # 获取匹配到的标题内容（不包括"# "）
        header_content = match.group(1)

        # 使用字符串的replace方法将匹配到的完整标题行替换为空字符串
        result = content.replace(
            full_header, header, 1
        )  # count=1 确保只替换第一个匹配项

        # 如果你只需要标题内容，可以使用 header_content
        print(f"匹配到的标题内容: {header_content}")
        print(f"处理后的内容: {result}")
        return result
    else:
        print("没有找到以'#'开头的标题")
        return content


def replace_author(content: str) -> str:
    """
    Replaces the *first* occurrence of the substring '原创'
    with '**源自** | ' in the given text.

    Args:
      text: The input string.

    Returns:
      The string with only the first replacement made.
    """
    # Use the string's replace method with the 'count' argument set to 1
    # to substitute only the first occurrence of the target substring
    # '原创' (original) with '**源自** | ' (sourced from | )
    new_text = content.replace("原创", "**源自** | ", 1)
    return new_text


if __name__ == "__main__":
    main()
