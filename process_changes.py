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

# -- configurations begin --
BOOKMARK_COLLECTION_REPO_NAME: str = "bookmark-collection"
BOOKMARK_SUMMARY_REPO_NAME: str = "bookmark-summary"
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

@log_execution_time
def summarize_text(text: str) -> str:
    prompt: str = """
请用markdown列表格式**详细**总结我发送给你的文本。充分合理使用缩进和子列表，如果有需要可以使用多层子列表，或是在子列表中包含多个条目（3个或以上）。在每个总结项开头，用简短的词语描述该项。忽略和文章主体无关的内容（如广告）。无论原文语言为何，总是使用中文进行总结。
"""
    return call_openai_api(prompt, text)

@log_execution_time
def one_sentence_summary(text: str) -> str:
    prompt: str = "以下是对一篇长文的列表形式总结。请基于此输出对该文章的简短总结，长度不超过100个字。总是使用简体中文输出。"
    return call_openai_api(prompt, text)

def slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(r'[' + re.escape(invalid_fs_chars) + r'\s]+', '-', text.lower()).strip('-')

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

## TL;DR
{one_sentence}

## Summary
{summary}
"""


def build_index_md(title: str, url: str, summary: str, one_sentence: str, text_content: str) -> str:
    """构建 index.md 文件内容，添加 YAML 头部并包含全文内容。"""
    return f"""---
title: {title}
source: {url}
date: {CURRENT_DATE}
---

## TL;DR
{one_sentence}

## Summary
{summary}

## Full Content
{text_content}
"""


def build_summary_readme_md(summarized_bookmarks: List[SummarizedBookmark]) -> str:
    initial_prefix: str = """# Bookmark Summary
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

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
def process_bookmark_file():
    title_slug = slugify(title)  # 将标题格式化为合法文件名

    # 创建 YEAR/MONTH/ 目录（用于 raw 和 summary 文件）
    monthly_path = Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/{CURRENT_YEAR}/{CURRENT_MONTH}')
    monthly_path.mkdir(parents=True, exist_ok=True)

    # 创建 content/YEAR/MONTH/TITLE/ 目录（用于 index.md 文件）
    content_path = Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/content/{CURRENT_YEAR}/{CURRENT_MONTH}/{title_slug}')
    content_path.mkdir(parents=True, exist_ok=True)

    # 读取书签和已总结书签
    with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/README.md', 'r', encoding='utf-8') as f:
        bookmark_lines = f.readlines()

    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'r', encoding='utf-8') as f:
        summarized_bookmark_dicts = json.load(f)
        summarized_bookmarks = [SummarizedBookmark(**bookmark) for bookmark in summarized_bookmark_dicts]

    summarized_urls = {bookmark.url for bookmark in summarized_bookmarks}

    title, url = None, None
    for line in bookmark_lines:
        match = re.search(r'- \[(.*?)\]\((.*?)\)', line)
        if match and match.group(2) not in summarized_urls:
            title, url = match.groups()
            break

    if title and url:
        text_content = get_text_content(url)
        summary = summarize_text(text_content)
        one_sentence = one_sentence_summary(summary)
        timestamp = int(datetime.now().timestamp())

        # 保存原始内容到 YEAR/MONTH/title_raw.md
        with open(monthly_path / f"{title_slug}_raw.md", 'w', encoding='utf-8') as f:
            f.write(text_content)

        # 保存总结内容到 YEAR/MONTH/title.md
        summary_content = build_summary_file(title, url, summary, one_sentence)
        with open(monthly_path / f"{title_slug}.md", 'w', encoding='utf-8') as f:
            f.write(summary_content)

        # 保存 index.md 到 content/YEAR/MONTH/TITLE/index.md
        index_content = build_index_md(title, url, summary, one_sentence, text_content)
        with open(content_path / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_content)

        # 更新已总结的书签数据
        summarized_bookmarks.append(SummarizedBookmark(
            year=CURRENT_YEAR,
            month=CURRENT_MONTH,
            title=title,
            url=url,
            summary=one_sentence,
            timestamp=timestamp
        ))

        # 更新 README 和 data.json
        with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/README.md', 'w', encoding='utf-8') as f:
            f.write(build_summary_readme_md(summarized_bookmarks))

        with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'w', encoding='utf-8') as f:
            json.dump([asdict(bookmark) for bookmark in summarized_bookmarks], f, indent=2, ensure_ascii=False)




def main():
    process_bookmark_file()

if __name__ == "__main__":
    main()
