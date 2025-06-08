import asyncio
from bilibili_api import video, comment

# 返回：视频标题,描述, 标签, 置顶评论,最热的5条评论
async def get_bilibili_video_info(bvid: str = "BV1NiEfzBE5k") -> dict:
    # 实例化 Video 类
    v = video.Video(bvid=bvid)
    # 获取信息
    info = await v.get_info()
    title = info.get("title", "")
    description = info.get("desc", "")

    cid = None
    pages = await v.get_pages()
    if len(pages) > 0:
        cid = pages[0]["cid"]
    tags = await v.get_tags(page_index=0, cid=cid)
    tag_names = [tag["tag_name"].replace("#","") for tag in tags]

    # 评论
    comments = await comment.get_comments(oid=v.get_aid(), type_=comment.CommentResourceType.VIDEO, order=comment.OrderType.LIKE)
    top_comments = [comment["content"]["message"] for comment in comments["replies"][:5]]

    return {
        "title": title,
        "description": description,
        "tags": tag_names,
        "top_comments": top_comments,
    }

if __name__ == "__main__":
    async def main():
        result = await get_bilibili_video_info("BV1NiEfzBE5k")
        print("视频标题:", result['title'])
        print("视频描述:", result['description'])
        print("视频标签:", result['tags'])
        print("置顶评论:", result['top_comments'])
    asyncio.run(main())
