import sys
import os
import re
from urllib.parse import quote

from xlib.gpt import call_openai


def replace_local_links(markdown_content):
    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)
        print(f"Found link: text='{link_text}', url='{link_url}'")  # Debugging
        # Check if the link is a local file

        # Encode the filename for URL safety
        encoded_filename = quote(os.path.basename(link_url))
        new_url = f"https://ai.programnotes.cn/img/ai/{encoded_filename}"
        print(f"Replacing with: {new_url}")  # Debugging
        return f"[{link_text}]({new_url})"

    # Regular expression to find markdown links and image links
    markdown_link_regex = r"!*\[([^\]]+)\]\(([^)]+)\)"
    replaced_content = re.sub(markdown_link_regex, replace_link, markdown_content)
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

    # Load prompts
    try:
        with open(
            os.path.join(os.path.dirname(__file__), "prompt", "tran2hugo.py"),
            "r",
            encoding="utf-8",
        ) as f:
            tran2hugo_prompt = f.read()
    except FileNotFoundError as e:
        print(f"Error: Prompt file not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading prompt file: {e}")
        sys.exit(1)

    modified_content = replace_local_links(markdown_content)

    try:
        converted_text = call_openai(tran2hugo_prompt, modified_content)
        print(converted_text)
        try:
            with open(markdown_file, "w", encoding="utf-8") as f:
                f.write(converted_text)
            print(f"Successfully wrote converted content to {markdown_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"Error during GPT conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
