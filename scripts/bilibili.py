import requests 
from bs4 import BeautifulSoup
import json

def get_bilibili_video_info(bvid):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # 获取视频基本信息和描述
    api_video_info = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    response_info = requests.get(api_video_info, headers=headers)
    if response_info.status_code != 200:
        raise Exception("Failed to fetch video info")
    video_info = response_info.json()
    data = video_info['data']
    title = data.get('title', '')
    description = data.get('desc', '')

    # 获取标签信息
    aid = data['aid']
    api_tag_info = f'https://api.bilibili.com/x/tag/archive/tags?aid={aid}'
    response_tag = requests.get(api_tag_info, headers=headers)
    if response_tag.status_code != 200:
        raise Exception("Failed to fetch video tags")
    tag_data = response_tag.json()
    tags = [tag['tag_name'] for tag in tag_data.get('data', [])]

    # 获取评论（置顶评论）
    api_comment = f'https://api.bilibili.com/x/v2/reply?type=1&oid={aid}&sort=2'
    response_comment = requests.get(api_comment, headers=headers)
    if response_comment.status_code != 200:
        raise Exception("Failed to fetch comments")
    comment_data = response_comment.json()
    top_comments = comment_data['data'].get('top_replies', [])
    top_comment = top_comments[0]['content']['message'] if top_comments else '无置顶评论'

    return {
        'title': title,
        'description': description,
        'tags': tags,
        'top_comment': top_comment
    }

# 示例调用
if __name__ == "__main__":
    #bvid = 'BV1C5jRzJE3v'  # 替换为具体BV号
    #bvid = 'BV1BSFgeJEJn'  # 替换为具体BV号
    bvid = 'BV1QdEezmEEK'  # 替换为具体BV号
    result = get_bilibili_video_info(bvid)
    print("视频标题:", result['title'])
    print("视频描述:", result['description'])
    print("视频标签:", result['tags'])
    print("置顶评论:", result['top_comment'])
