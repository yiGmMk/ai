import json
import os
from bilibili_sdk import get_bilibili_video_info
import asyncio
from datetime import datetime
from xlib.gpt import call_openai


async def generate_markdown(data, output_dir="content/zh-cn/post/bilibili"):
    """
    读取JSON文件，提取BVID，使用bilibili_api获取视频信息，
    并将每个视频的相关内容保存为一个Markdown文件，
    在文章开始总结下相关信息。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_list = data.get("list", [])
    for video in video_list:
        bvid = video.get("bvid")
        if not bvid:
            continue

        try:
            video_info = await get_bilibili_video_info(bvid)
            title = video_info.get("title", "无标题")
            description = video_info.get("description", "无描述")
            tags = video_info.get("tags", [])
            top_comments = video_info.get("top_comments", [])

            ai_desc = call_openai(
                prompt="这是一个视频，请根据标题,描述和标签生成一个简短的摘要。",
                content=f"""
标题: {title}
描述: {description}
标签: {", ".join(tags)}
""",
            )

            # 创建Markdown内容
            markdown_content = "---\n"
            markdown_content += f'title: "{title}"\n'
            markdown_content += f"date: \"{datetime.now().strftime('%Y-%m-%d')}\"\n"
            markdown_content += f"tags: {json.dumps(tags, ensure_ascii=False)}\n"
            markdown_content += 'categories: ["bilibili"]\n'
            markdown_content += f'description: "{ai_desc}"\n'
            markdown_content += "---\n\n"
            markdown_content += f"{{{{< bilibili {bvid} >}}}}\n\n"
            markdown_content += "## 视频信息\n\n"
            markdown_content += "**描述:**\n"
            markdown_content += f"{description}\n\n"
            markdown_content += "**置顶评论:**\n"
            markdown_content += (
                f"{top_comments[0] if top_comments else '无置顶评论'}\n\n"
            )
            markdown_content += "**热门评论:**\n"
            for i, comment in enumerate(top_comments[1:]):
                markdown_content += f"{i+1}. {comment}\n"

            # 保存为Markdown文件
            filename = f"{bvid}.md"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)

        except Exception as e:
            print(f"Error processing {bvid}: {e}")
            continue


if __name__ == "__main__":

    async def main():
        json_file = "scripts/data.json"
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        await generate_markdown(data)
        print("Markdown文件生成完成！")

    asyncio.run(main())
