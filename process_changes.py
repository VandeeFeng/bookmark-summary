import re
from typing import List, Optional
import requests
import json
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
import os
import logging
import time
from functools import wraps
from urllib.parse import quote
import http.client
from pypinyin import pinyin, Style

# -- configurations begin --
BOOKMARK_COLLECTION_REPO_NAME: str = "bookmark-collection"
BOOKMARK_SUMMARY_REPO_NAME: str = "bookmark-summary"
TEABLE_TABLE_ID: str = os.environ.get('TEABLE_TABLE_ID') 
TEABLE_TOKEN: str = os.environ.get('TEABLE_TOKEN') 
# -- configurations end --

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Entering {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'Exiting {func.__name__} - Elapsed time: {elapsed_time:.4f} seconds')
        return result
    return wrapper

@dataclass
class SummarizedBookmark:
    year: str
    month: str  # yyyyMM
    title: str
    url: str
    timestamp: int  # unix timestamp
    summary: str

CURRENT_YEAR: str = datetime.now().strftime('%Y')
CURRENT_MONTH: str = datetime.now().strftime('%m')
CURRENT_DATE: str = datetime.now().strftime('%Y-%m-%d')
CURRENT_DATE_AND_TIME: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@log_execution_time
def get_text_content(url: str) -> str:
    jina_url: str = f"https://r.jina.ai/{url}"
    response: requests.Response = requests.get(jina_url)
    return response.text

@log_execution_time
def call_openai_api(prompt: str, content: str) -> str:
    model: str = os.environ.get('OPENAI_API_MODEL', 'gpt-4o-mini')
    headers: dict = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json"
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    }
    api_endpoint: str = os.environ.get('OPENAI_API_ENDPOINT', 'https://api.openai.com/v1/chat/completions')
    response: requests.Response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']
'''
def clean_prompt(prompt: str) -> str:
    """清理和验证prompt格式"""
    # 移除多余的空白字符
    prompt = prompt.strip()
    # 确保XML声明在第一行
    if not prompt.startswith('<?xml'):
        prompt = '<?xml version="1.0" encoding="UTF-8"?>\n' + prompt
    # 验证XML格式
    try:
        from xml.etree import ElementTree
        ElementTree.fromstring(prompt)
    except ElementTree.ParseError as e:
        logging.warning(f"Prompt XML format warning: {e}")
    return prompt
'''

@log_execution_time
def summarize_text(text: str) -> str:
    prompt: str = """
{#- 用简体中文中文進行文章摘要 -#}

## Profile:​
- author: Vandee​
- role: 文章内容深度总结思考助手
- language: 中文​
- description: 全面的总结文章的主要观点，并结合严谨的逻辑思维分析文章要点，剖析文章内容。

## Goals:
- 第一步，仔细阅读文章内容。
- 第二步,对每个段落进行总结,总结文章的主要内容，理清楚作者表达了什么观点、作者解决了那些具体的问题。
- 第三步,文章要点总结。根据原文内容,提炼出文章的5个以内的主要观点或作者解决的问题。
- 第四步,根据上面三步，按照指定的输出格式,整理出文章内容的总结。

## Constrains:​
- 文章内容总结的{摘要}字数控制在380个中文汉字以内。
- 尽可能还原文章中的专业词汇,并对其进行通俗解释。
- 在总结的过程中,完全按照文章作者的表达内容进行整理,不添加你的额外观点。
- 所有输出用中文生成。
- 文章内容里的"我“是文章的原作者，不要代入 Vandee 的身份。

## Skills:​
- 善于用流畅通顺的简体中文总结内容重点。
- 具有良好的逻辑思维能力,能够深入分析文章内容。
- 掌握文章相关领域的专业知识,能够准确理解和阐述专业概念。
- 擅长以通俗易懂的方式解释复杂的专业内容。

## Workflows:​
- 逐段阅读文章内容。
- 总结文章的内容并生成{摘要}。这一步你需要全面理解文章内容的主题、内容的逻辑框架、作者的提出的观点，摘要不少于270个中文汉字。
- 再次回顾原文所有内容，在上一步总结出{摘要}的基础上，进行深入分析。这一步你需要理清这些内容之间的逻辑关系、专业概念、名词概念，并着重关注原文内容里多次出现的词汇或概念，特别关注作者提出了什么观点、作者解决了那些具体的问题、作者体悟出了哪些道理、作者得出了什么重大的研究结论，最后梳理出{精炼内容}。
- 根据原文内容和你上一步的{精炼内容}，提炼出文章的至少4个要点生成{要点总结}，你不用输出{精炼内容}。
- 你需要按照markdown有序列表的格式列出上一步{要点总结}中的要点，并根据要点所在的原文并严格根据文章内容扩展对该要点的解析，方便读者理解这些要点的意思。
- 按照指定的输出格式,整理出文章内容的总结。“摘要“和”要点总结“只需要按照markdown格式加粗，不要用标题格式。

## OutputFormat:
**摘要**：
{摘要}
**要点总结**：
{要点总结}
"""
    result = call_openai_api(prompt, text)  # 先调用 API 并存储结果
    time.sleep(1)  # 等待 1 秒
    return result  # 返回结果

@log_execution_time
def one_sentence_summary(text: str) -> str:
    prompt: str = "以下是对一篇长文的列表形式总结。请基于此输出对该文章的简短总结，长度不超过100个字。总是使用简体中文输出。"
    return call_openai_api(prompt, text)

def slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(r'[' + re.escape(invalid_fs_chars) + r'\s]+', '-', text.lower()).strip('-')

def url_to_pinyin(text: str) -> str:
    # 默认输出不带声调的拼音
    result = pinyin(text, style=Style.NORMAL)
    # 用短横线连接拼音
    return '-'.join([''.join(p) for p in result])

def get_summary_file_path(title: str, timestamp: int, year: Optional[str] = None, month: Optional[str] = None, in_readme_md: bool = False) -> Path:
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    summary_filename: str = f"{date_str}-{slugify(title)}.md"
    if year is None:
        year = CURRENT_YEAR
    if month is None:
        month = CURRENT_MONTH
    if in_readme_md:
        root: Path = Path(year, month)  # 更新路径为 year/month
    else:
        root: Path = Path(BOOKMARK_SUMMARY_REPO_NAME, year, month)  # 更新路径为 year/month
    return Path(root, summary_filename)


def get_text_content_path(title: str, in_summary_md: bool = False) -> Path:
    text_content_filename: str = f"{CURRENT_DATE}-{slugify(title)}_raw.md"
    root: Path = Path(BOOKMARK_SUMMARY_REPO_NAME, CURRENT_YEAR, CURRENT_MONTH)  # 更新路径为 YEAR/MONTH
    if in_summary_md:
        root = Path(".")
    return Path(root, text_content_filename)


def build_summary_file(title: str, url: str, summary: str, one_sentence: str) -> str:
    """构建总结文件的内容。"""
    return f"""# {title}
- URL: {url}
- Added At: {CURRENT_DATE_AND_TIME}
- [Link To Text]({get_text_content_path(title, in_summary_md=True)})

## Summary
{summary}
"""

def yaml_title(title):
    # Replace colons and other special YAML characters with a safe alternative
    safe_title = re.sub(r'[:#*&?|>{}[\]`]', '-', title)
    # Remove any leading or trailing whitespace
    safe_title = safe_title.strip()
    # Optionally replace consecutive hyphens with a single hyphen
    safe_title = re.sub(r'-{2,}', '-', safe_title)
    return yaml_safe_title
    
def build_index_md(title: str, url: str, summary: str, one_sentence: str, text_content: str) -> str:
    """构建 index.md 文件内容，添加 YAML 头部并包含全文内容。"""
    
    return f"""---
title: {yaml_safe_title}
date: {CURRENT_DATE}
extra:
  source: {url}
  original_title: {yaml_safe_title}
---
## Summary
{summary}
## Full Content
{text_content}
"""

def build_summary_readme_md(summarized_bookmarks: List[SummarizedBookmark]) -> str:
    initial_prefix: str = """# Clip
总会有一些没达到我想收录到PKM体系里标准的文章，但又弃之可惜。介于这两者之间的，就放在这个clip里了。区别于笔记，这里主要是原文的 Markdown。

Inspired by :[Owen's Clip](https://github.com/theowenyoung/clip) , [LLM x 书签收藏：摘要 & 全文索引 - Nekonull's Garden](https://nekonull.me/posts/llm_x_bookmark/)

## Summarized Bookmarks
"""
    summary_list: str = ""
    sorted_summarized_bookmarks = sorted(summarized_bookmarks, key=lambda bookmark: bookmark.timestamp, reverse=True)
    for bookmark in sorted_summarized_bookmarks:
        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True
        )
        summary_list += f"- ({datetime.fromtimestamp(bookmark.timestamp).strftime('%Y-%m-%d')}) [{bookmark.title}]({summary_file_path})\n"
    return initial_prefix + summary_list

@log_execution_time
def post_to_teable(title: str, url: str, one_sentence: str) -> None:
    """
    Post a bookmark record to Teable
    """
    try:
        conn = http.client.HTTPSConnection("app.teable.io")
        
        payload = {
            "typecast": True,
            "records": [{
                "fields": {
                    "Title": title,
                    "Source": url,
                    "Summary": one_sentence,
                }
            }]
        }
        
        headers = {
            'Authorization': f"Bearer {TEABLE_TOKEN}",
            'Content-Type': "application/json"
        }
        
        conn.request(
            "POST", 
            f"/api/table/{TEABLE_TABLE_ID}/record", 
            json.dumps(payload), 
            headers
        )
        
        response = conn.getresponse()
        if response.status not in (200, 201):
            logging.error(f"Failed to post to Teable. Status: {response.status}, Response: {response.read().decode()}")
        else:
            logging.info("Successfully posted to Teable")
            
    except Exception as e:
        logging.error(f"Error posting to Teable: {str(e)}")
    finally:
        conn.close()

@log_execution_time
def process_bookmark_file():
    # 读取书签和已总结书签
    with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/README.md', 'r', encoding='utf-8') as f:
        bookmark_lines = f.readlines()

    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'r', encoding='utf-8') as f:
        summarized_bookmark_dicts = json.load(f)
        summarized_bookmarks = [SummarizedBookmark(**bookmark) for bookmark in summarized_bookmark_dicts]

    summarized_urls = {bookmark.url for bookmark in summarized_bookmarks}

    # 找到未总结的书签
    title, url = None, None
    for line in bookmark_lines:
        match = re.search(r'- \[(.*?)\]\((.*?)\)', line)
        if match and match.group(2) not in summarized_urls:
            title, url = match.groups()
            break

    # 如果没有找到新的书签，则退出
    if not title or not url:
        logging.info("No new bookmarks to summarize.")
        return

    # 将标题格式化为文件名
    title_slug = slugify(title)

    title_pinyin = url_to_pinyin(title_slug)

    # 创建 YEAR/MONTH/ 目录
    monthly_path = Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/{CURRENT_YEAR}/{CURRENT_MONTH}')
    monthly_path.mkdir(parents=True, exist_ok=True)

    # 创建 content/YEAR/MONTH/TITLE/ 目录
    content_path = Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/content/{CURRENT_YEAR}/{CURRENT_MONTH}/{title_pinyin}')
    content_path.mkdir(parents=True, exist_ok=True)

    # 获取和总结内容
    text_content = get_text_content(url)
    summary = summarize_text(text_content)
    one_sentence = one_sentence_summary(summary)
    timestamp = int(datetime.now().timestamp())

    # 使用当前日期创建前缀
    date_prefix = datetime.now().strftime('%Y-%m-%d-')

    # 保存原始内容到 YEAR/MONTH/yyyy-MM-dd-title_raw.md
    with open(monthly_path / f"{date_prefix}{title_slug}_raw.md", 'w', encoding='utf-8') as f:
        f.write(text_content)

    # 保存总结内容到 YEAR/MONTH/yyyy-MM-dd-title.md
    summary_content = build_summary_file(title, url, summary, one_sentence)
    with open(monthly_path / f"{date_prefix}{title_slug}.md", 'w', encoding='utf-8') as f:
        f.write(summary_content)

    # 保存 index.md 到 content/YEAR/MONTH/TITLE/index.md
    index_content = build_index_md(title, url, summary, one_sentence, text_content)
    with open(content_path / "index.md", 'w', encoding='utf-8') as f:
        f.write(index_content)

    # 更新已总结的书签数据
    summarized_bookmarks.append(SummarizedBookmark(
        title=title,
        url=url,
        summary=one_sentence,
        year=CURRENT_YEAR,
        month=CURRENT_MONTH,
        timestamp=timestamp
    ))

    # 更新 README 和 data.json
    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/Bookmarks_List.md', 'w', encoding='utf-8') as f:
        f.write(build_summary_readme_md(summarized_bookmarks))

    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'w', encoding='utf-8') as f:
        json.dump([asdict(bookmark) for bookmark in summarized_bookmarks], f, indent=2, ensure_ascii=False)

        # Post to Teable
    if TEABLE_TOKEN and TEABLE_TABLE_ID:
        post_to_teable(title, url, one_sentence)
    else:
        logging.warning("Teable API token or table ID not set, skipping Teable update")

def main():
    process_bookmark_file()

if __name__ == "__main__":
    main()
