#!/usr/bin/env python3
"""
谛听 AI 全自动转写 Worker
──────────────────────────
由 GitHub Actions 触发，读取 Issue 中的 B 站链接，
调 diting.cc API 完成转写，并自动归档 Markdown 笔记文件到仓库。
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from typing import Any

import requests

# ── 常量配置 ──────────────────────────────────────────

# 知识库分类映射：根据标题关键词自动归类（数字前缀仅排序用，可随时新增）
CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "01_🔥考研考编必刷": [
        "考研", "考编", "考公", "高数", "线代", "概率论", "政治", "英语",
        "数学", "张宇", "汤家凤", "李永乐", "肖秀荣", "徐涛", "腿姐",
    ],
    "02_🤖AI前沿与高薪技术": [
        "AI", "人工智能", "智能体", "机器学习", "深度学习", "LLM", "大模型",
        "吴恩达", "李飞飞", "Prompt", "ChatGPT", "GPT", "Agent",
        "Python", "编程", "前端", "后端", "全栈", "算法",
        "AGI", "AIGC", "RAG", "神经网络", "transformer",
    ],
    "03_🎨设计创意与剪辑": [
        "设计", "PS", "Photoshop", "PR", "Premiere", "AE", "After Effects",
        "剪辑", "调色", "C4D", "Blender", "Figma", "Sketch", "UI", "UX",
        "平面设计", "视觉", "动画", "建模", "渲染", "达芬奇",
    ],
    "04_📈商业财经与搞钱": [
        "商业", "财经", "理财", "投资", "股票", "基金", "创业",
        "搞钱", "副业", "电商", "运营", "营销", "品牌", "管理",
        "经济学", "金融", "商业模式",
    ],
    "05_📱自媒体与内容创作": [
        "自媒体", "短视频", "抖音", "小红书", "公众号", "B站运营",
        "拍摄", "文案", "脚本", "涨粉", "爆款", "选题", "写作",
    ],
}
# 兜底目录：无关键词匹配或手动指定新分类时写入
FALLBACK_CATEGORY = "99_📁其他优质网课"

# 默认请求配置
DEFAULT_TIMEOUT = 30
DEFAULT_RETRIES = 3
DEFAULT_RETRY_DELAY = 2  # 秒
DEFAULT_POLL_INTERVAL = 5  # 秒
DEFAULT_POLL_MAX_WAIT = 3600  # 秒

# ── 辅助函数 ──────────────────────────────────────────

def extract_bilibili_url(text: str) -> str | None:
    """从文本中提取 B 站视频链接或 BV 号。"""
    # 匹配完整 URL
    match = re.search(r'(https?://[^\s]*bilibili\.com[^\s]+)', text)
    if match:
        return match.group(1)
    # 匹配裸 BV 号
    match = re.search(r'(BV[a-zA-Z0-9]{10})', text)
    if match:
        return f"https://www.bilibili.com/video/{match.group(1)}"
    return None


# ── 请求工具 ──────────────────────────────────────────

class APIError(Exception):
    """API 请求异常，包含状态码和响应体。"""
    def __init__(self, message: str, status_code: int | None = None, body: str = ""):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


def api_request(
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json_body: dict[str, Any] | None = None,
    timeout: int = DEFAULT_TIMEOUT,
    verify: bool = True,
    retries: int = DEFAULT_RETRIES,
    retry_delay: int = DEFAULT_RETRY_DELAY,
) -> requests.Response:
    """带重试的 HTTP 请求封装。

    Args:
        method: HTTP 方法（GET/POST 等）
        url: 请求地址
        headers: 请求头
        json_body: JSON 请求体（仅 POST 时有效）
        timeout: 超时秒数
        verify: 是否验证 SSL 证书
        retries: 最大重试次数
        retry_delay: 重试间隔（秒）

    Returns:
        requests.Response 对象

    Raises:
        APIError: 重试耗尽后仍失败
    """
    last_exception: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            if method.upper() == "GET":
                resp = requests.get(url, headers=headers, timeout=timeout, verify=verify)
            else:
                resp = requests.post(url, json=json_body, headers=headers, timeout=timeout, verify=verify)
            resp.raise_for_status()
            return resp
        except requests.Timeout as e:
            last_exception = e
            print(f"⚠️  请求超时 (attempt {attempt}/{retries}): {url}")
        except requests.ConnectionError as e:
            last_exception = e
            print(f"⚠️  连接失败 (attempt {attempt}/{retries}): {url}")
        except requests.HTTPError as e:
            # 4xx/5xx 不重试（除非是 5xx 服务端错误）
            status = e.response.status_code if e.response else 0
            if 500 <= status < 600 and attempt < retries:
                last_exception = e
                print(f"⚠️  服务端错误 {status} (attempt {attempt}/{retries}): {url}")
            else:
                raise APIError(
                    f"HTTP {status}: {e.response.text[:500] if e.response else str(e)}",
                    status_code=status,
                    body=e.response.text if e.response else "",
                ) from e
        except requests.RequestException as e:
            last_exception = e
            print(f"⚠️  请求异常 (attempt {attempt}/{retries}): {e}")

        if attempt < retries:
            time.sleep(retry_delay)

    raise APIError(f"重试 {retries} 次后仍失败: {last_exception}")


def classify_category(title: str, body: str) -> str:
    """根据标题和正文关键词自动归类，按匹配数量选最优分类。
    短关键词（≤3字符）：含ASCII则用词边界匹配，纯中文则直接子串匹配。
    无匹配时返回 FALLBACK_CATEGORY 兜底目录。"""
    combined = (title + " " + body).lower()
    best_category = ""
    best_count = 0

    for category, keywords in CATEGORY_KEYWORDS.items():
        count = 0
        for kw in keywords:
            kw_lower = kw.lower()
            if len(kw_lower) <= 3:
                if re.search(r'[a-zA-Z0-9]', kw_lower):
                    # 含英文字母/数字 → ASCII词边界匹配，避免 "AI" 误匹配 "certain"
                    # re.ASCII 确保 \b 不把中文当单词字符
                    if re.search(r'\b' + re.escape(kw_lower) + r'\b', combined, re.ASCII):
                        count += 1
                else:
                    # 纯中文/符号 → 直接子串匹配（\b 对中文无效）
                    if kw_lower in combined:
                        count += 1
            else:
                if kw_lower in combined:
                    count += 1
        if count > best_count:
            best_count = count
            best_category = category

    return best_category or FALLBACK_CATEGORY


def sanitize_filename(name: str, max_len: int = 80) -> str:
    """清理文件名，移除非法字符并限制长度。"""
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    if len(name) > max_len:
        name = name[:max_len].rsplit(' ', 1)[0]
    return name


# ── URL 解析工具 ──────────────────────────────────────

def clean_url(url: str) -> str:
    """清理 B 站 URL 中可能带的反引号和空白。"""
    return url.strip().strip('`').strip()


def extract_bvid(url: str) -> str | None:
    """从 B 站链接中提取 BV 号。"""
    m = re.search(r'/video/(BV[\w]+)', url)
    return m.group(1) if m else None


def extract_page_number(url: str) -> int:
    """从 B 站 URL 中提取 p= 参数，返回页码（从1开始），默认返回 1。"""
    m = re.search(r'[?&]p=(\d+)', url)
    return int(m.group(1)) if m else 1


# ── API 调用 ──────────────────────────────────────────

def check_bilibili_video(
    bilibili_url: str,
    *,
    api_base: str,
    api_key: str,
    verify_ssl: bool = True,
    timeout: int = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> dict[str, Any]:
    """检查 B 站视频信息，获取 bvid/cid/aid。"""
    api_url = f"{api_base}/api/v1/videos/bilibili/check"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {"video_url": bilibili_url}
    resp = api_request("POST", api_url, headers=headers, json_body=payload,
                       timeout=timeout, verify=verify_ssl, retries=retries)
    return resp.json()


def submit_process_task_with_payload(
    videos: list[dict[str, Any]],
    *,
    api_base: str,
    api_key: str,
    verify_ssl: bool = True,
    timeout: int = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> dict[str, Any]:
    """提交视频处理任务。"""
    api_url = f"{api_base}/api/v1/videos/bilibili/process"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {"videos": videos}

    try:
        resp = api_request("POST", api_url, headers=headers, json_body=payload,
                           timeout=timeout, verify=verify_ssl, retries=retries)
    except APIError:
        print(f"🔍 请求体: {json.dumps(payload, ensure_ascii=False)}")
        raise
    return resp.json()


def poll_task(
    task_id: str,
    *,
    api_base: str,
    api_key: str,
    verify_ssl: bool = True,
    max_wait: int = DEFAULT_POLL_MAX_WAIT,
    interval: int = DEFAULT_POLL_INTERVAL,
    timeout: int = 15,
) -> dict[str, Any] | None:
    """轮询等待视频处理完成。"""
    api_url = f"{api_base}/api/v1/videos/{task_id}/status"
    headers = {"Authorization": f"Bearer {api_key}"}

    elapsed = 0
    while elapsed < max_wait:
        resp = api_request("GET", api_url, headers=headers,
                           timeout=timeout, verify=verify_ssl, retries=1)
        data = resp.json()

        # 后端返回格式: { code: 200, data: { status, progress, ... } }
        inner: dict[str, Any] = data.get("data", data)
        status: str = inner.get("status", "")
        progress: str = inner.get("progress", "")

        if status == "completed":
            return inner
        if status in ("failed", "error"):
            print(f"❌ 任务 {task_id} 失败: {inner.get('error', '未知错误')}")
            return None

        print(f"⏳ 任务 {task_id} 进行中... status={status} progress={progress} 已等待 {elapsed}s")
        time.sleep(interval)
        elapsed += interval

    print(f"⚠️ 任务 {task_id} 超时（>{max_wait}s）")
    return None


def fetch_video_result(
    task_id: str,
    *,
    api_base: str,
    api_key: str,
    verify_ssl: bool = True,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict[str, Any] | None:
    """获取视频详情，返回 data 内层。"""
    api_url = f"{api_base}/api/v1/videos/{task_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = api_request("GET", api_url, headers=headers, timeout=timeout, verify=verify_ssl)
    data = resp.json()
    inner: dict[str, Any] = data.get("data", data)
    print(f"🔍 详情接口返回 keys: {list(inner.keys()) if isinstance(inner, dict) else type(inner)}")
    return inner


# ── 文本提取与 Markdown 组装 ─────────────────────────

def timestamp_to_seconds(ts: str) -> int:
    """将 HH:MM:SS 或 HH:MM:SS.mmm 转换为秒数。"""
    parts = ts.split(":")
    if len(parts) == 3:
        h, m, s = parts
        s = s.split(".")[0]
        return int(h) * 3600 + int(m) * 60 + int(s)
    return 0


def convert_timestamps_to_links(text: str, bilibili_url: str) -> str:
    """将 [HH:MM:SS] 和 HH:MM:SS 格式的时间戳转换为可点击的 B 站链接。"""
    def make_link(ts: str) -> str:
        seconds = timestamp_to_seconds(ts)
        sep = "&" if "?" in bilibili_url else "?"
        return f"[{ts}]({bilibili_url}{sep}t={seconds})"

    # 1. 带方括号的: [00:00:00] 或 [00:00:00.000]
    text = re.sub(r'\[(\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?)\]',
                  lambda m: make_link(m.group(1)), text)
    # 2. 行首纯时间戳: 00:00:00 或 00:00:00.000
    text = re.sub(r'^(\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?)\s',
                  lambda m: make_link(m.group(1)) + " ", text, flags=re.MULTILINE)
    return text


def build_outline_markdown(outline: list[dict[str, Any]]) -> str:
    """将 AI 大纲数据转换为 Markdown 嵌套列表。"""
    lines: list[str] = []
    for item in outline:
        if isinstance(item, dict):
            title = item.get("title", "") or item.get("text", "")
            ts = item.get("start_timestamp", "") or item.get("timestamp", "")
            ts_str = f" `{ts}`" if ts else ""
            lines.append(f"- **{title}**{ts_str}")
        elif isinstance(item, str):
            lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def build_mindmap_markdown(mindmap_data: list[dict[str, Any]]) -> str:
    """将思维导图数据转换为 Markdown 嵌套列表。"""
    lines: list[str] = []
    for item in mindmap_data:
        if isinstance(item, dict):
            name = item.get("name", "") or item.get("title", "")
            children: list[dict[str, Any]] = item.get("children", [])
            lines.append(f"- **{name}**")
            for child in children:
                if isinstance(child, dict):
                    child_name = child.get("name", "") or child.get("title", "")
                    lines.append(f"  - {child_name}")
                elif isinstance(child, str):
                    lines.append(f"  - {child}")
        elif isinstance(item, str):
            lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def build_mindmap_from_tree(node: dict[str, Any], indent: int = 0) -> str:
    """递归渲染嵌套 dict 树结构思维导图为 Markdown。"""
    prefix = "  " * indent
    name = node.get("title", "") or node.get("name", "")
    lines: list[str] = [f"{prefix}- **{name}**"]
    for child in node.get("children", []):
        if isinstance(child, dict):
            lines.append(build_mindmap_from_tree(child, indent + 1))
        elif isinstance(child, str):
            lines.append(f"{prefix}  - {child}")
    return "\n".join(lines)


def build_comprehensive_markdown(detail: dict[str, Any], title: str, bilibili_url: str) -> str:
    """从 API 返回数据构建完整的多维度 Markdown 笔记。"""
    parts = []

    # PART 0: GEO 元数据 front matter + 标题 + 引流钩子
    parts.append(f"""---
title: {title}
source: Bilibili ({bilibili_url})
extractor: https://diting.cc 创作者版
tags: [视频转文字, 笔记下载, Markdown大纲, AI润色]
---

# 📝 {title}

> 💡 **多维解构 · 谛听 AI 深度加工**：
> 
> 不仅提供逐字稿，更有由谛听 AI 深度加工的 **AI 智能大纲**、**逻辑洞察**、**核心 QA 对** 与 **全局思维导图**。
> 
> ⚠️ **GitHub 开源版**仅展示「**逐字稿（可点击时间戳直达 B 站原视频）**」与「**AI 润色精校版**」。
> 🔍 逻辑洞察 · 🚀 思维导图等深度功能，仅限 **[diting.cc 创作者版](https://diting.cc)** PC 端呈现。
> 
> 👉 微信扫码秒登 · 免注册 · 每日免费 20 次 · 百P合集直链解析 · 小红书一键洗稿

---""")

    transcript_with_ts = detail.get("transcriptWithTimestamp") or ""
    polished = detail.get("polishedTranscript") or ""
    original = detail.get("originalTranscript") or ""

    # PART 1: 带可点击时间戳的逐字稿
    if transcript_with_ts:
        parts.append("## 📝 逐字稿（带可点击时间戳）\n")
        parts.append("> 点击任意 `[00:15:23]` 时间戳，直达 B 站原视频对应秒数\n\n")
        parts.append(convert_timestamps_to_links(transcript_with_ts, bilibili_url))
        parts.append("")

    # PART 2: AI 润色版
    if polished:
        parts.append("## ✨ AI 润色精校版\n")
        parts.append(polished)
        parts.append("")

    # PART 3: AI 智能大纲
    outline = detail.get("aiOutline") or detail.get("outline") or []
    if isinstance(outline, list) and outline:
        parts.append("## 🧠 AI 智能大纲\n")
        parts.append(build_outline_markdown(outline))

    # PART 4: 逻辑洞察（ai_logic_insight / verdict 字段）
    logic_insight = detail.get("ai_logic_insight") or detail.get("verdict") or {}
    if isinstance(logic_insight, str) and logic_insight.strip():
        parts.append("## 🔍 逻辑洞察\n")
        parts.append(f"> {logic_insight.strip()}\n")
        parts.append("")
    elif isinstance(logic_insight, dict):
        if logic_insight.get("key_insight") or logic_insight.get("content"):
            parts.append("## 🔍 逻辑洞察\n")
            parts.append(f"> {logic_insight.get('key_insight') or logic_insight.get('content', '')}\n")
            for k in ["pros", "cons", "summary"]:
                v = logic_insight.get(k, "")
                if v:
                    parts.append(f"- **{k}**：{v}\n")
            parts.append("")

    # PART 5: 核心 QA 对
    qa_pairs = detail.get("qaPairs") or []
    if qa_pairs:
        parts.append("## ❓ 核心 QA 对\n")
        for i, qa in enumerate(qa_pairs, 1):
            q = qa.get("question", "")
            a = qa.get("answer", "")
            ts = qa.get("start_timestamp", "")
            if ts:
                seconds = timestamp_to_seconds(ts)
                sep = "&" if "?" in bilibili_url else "?"
                ts_link = f" ([{ts}]({bilibili_url}{sep}t={seconds}))"
            else:
                ts_link = ""
            parts.append(f"**Q{i}：{q}**{ts_link}\n\n")
            parts.append(f"A{i}：{a}\n\n")
        parts.append("")

    # 兜底：如果以上都没有，回退到原始文本
    if len(parts) <= 1:
        text = polished or original or transcript_with_ts
        if text:
            parts.append("## 📝 视频文稿\n\n")
            parts.append(text)

    return "\n".join(parts)


# ── 文本提取（向后兼容） ──────────────────────────────

def extract_text(data: dict[str, Any]) -> str | None:
    """从 API 轮询结果中提取文本内容（向后兼容）。"""
    return (
        data.get("originalTranscript")
        or data.get("polishedTranscript")
        or data.get("transcriptWithTimestamp")
    )


def _parse_batch_all(issue_body: str) -> bool:
    """从 Issue 正文解析 BATCH_ALL 参数。"""
    m = re.search(r'BATCH_ALL\s*[=：:]\s*(是|否)', issue_body)
    return (m.group(1) == "是") if m else False


def _parse_manual_category(issue_body: str) -> str:
    """从 Issue 正文解析 CATEGORY 参数。"""
    m = re.search(r'CATEGORY[ \t]*[=：:][ \t]*(\S.*)', issue_body)
    if m:
        val = m.group(1).strip()
        if val and not val.startswith("`"):
            return val
    return ""


# ── 主流程 ────────────────────────────────────────────

def main() -> None:
    # ── 运行时配置（从环境变量读取） ─────────────────
    api_base = os.environ.get("DITING_API_BASE", "https://api.diting.cc")
    api_key = os.environ.get("DITING_API_KEY", "").strip()
    issue_body = os.environ.get("ISSUE_BODY", "")
    issue_title = os.environ.get("ISSUE_TITLE", "")

    if not api_key:
        print("❌ 未设置 DITING_API_KEY 环境变量")
        sys.exit(1)

    # SSL 验证：默认关闭，仅当 DITING_VERIFY_SSL=true 时开启
    verify_ssl = os.environ.get("DITING_VERIFY_SSL", "").strip().lower() == "true"

    # poll_task 可配置参数
    poll_max_wait = int(os.environ.get("DITING_POLL_MAX_WAIT", str(DEFAULT_POLL_MAX_WAIT)))
    poll_interval = int(os.environ.get("DITING_POLL_INTERVAL", str(DEFAULT_POLL_INTERVAL)))

    # Issue 参数解析
    batch_all = _parse_batch_all(issue_body)
    manual_category = _parse_manual_category(issue_body)

    print("=" * 60)
    print("🤖 谛听 AI 全自动转写 Worker 启动")
    print(f"   API Base: {api_base}")
    print(f"   SSL 验证: {'✅ 开启' if verify_ssl else '⚠️  关闭'}")
    print(f"   轮询间隔: {poll_interval}s / 超时: {poll_max_wait}s")
    print("=" * 60)

    # 1. 提取 B 站链接
    bilibili_url = extract_bilibili_url(issue_body)
    if not bilibili_url:
        print("❌ 未检测到有效的 B 站视频链接或 BV 号")
        print(f"   Issue Body 前 200 字符: {issue_body[:200]}")
        sys.exit(1)

    print(f"✅ 检测到 B 站链接: {bilibili_url}")

    # 2. 获取视频元信息
    print("🔍 获取 B 站视频信息...")
    try:
        video_info = check_bilibili_video(
            bilibili_url,
            api_base=api_base, api_key=api_key, verify_ssl=verify_ssl,
        )
    except (requests.RequestException, APIError) as e:
        print(f"❌ 获取视频信息失败: {e}")
        sys.exit(1)

    video_data: dict[str, Any] = video_info.get("data", video_info)
    if not video_data.get("bvid"):
        video_data["bvid"] = extract_bvid(bilibili_url)
    if not video_data.get("bvid"):
        print(f"❌ 未能获取 BV 号: {json.dumps(video_info, ensure_ascii=False)[:500]}")
        sys.exit(1)

    title = video_data.get("title") or issue_title.replace("[求笔记]", "").strip() or "未命名课程"
    part_count = len(video_data.get("parts", []))
    print(f"📹 视频标题: {title}{'（合集，共 ' + str(part_count) + 'P）' if part_count else ''}")

    # 3. 自动归类（基于视频真实标题）
    category = manual_category or classify_category(title, "")
    print(f"📂 {'手动指定' if manual_category else '自动归类'}到: {category}")

    # 4. 构造 process 请求体（参照前端 DashboardHome.vue / MobileHome.vue）
    print("📤 提交处理任务到谛听 AI 云端...")
    videos_payload: list[dict[str, Any]] = []
    parts: list[dict[str, Any]] = video_data.get("parts", [])
    is_collection = bool(video_data.get("season_id", 0) > 0)
    is_multi_part = video_data.get("is_multi_part") is True

    if parts and (is_collection or is_multi_part):
        print(f"📦 检测到合集/多P（共{len(parts)}P），BATCH_ALL={'是' if batch_all else '否'}")
        if batch_all:
            print(f"📦 批量提交全部 {len(parts)}P...")
            for part in parts:
                part_url = clean_url(part.get("url", ""))
                video_entry: dict[str, Any] = {
                    "url": part_url,
                    "thumbnail": clean_url(part.get("thumbnail") or video_data.get("thumbnail", "")),
                    "title": part.get("title") or video_data.get("title", ""),
                    "duration": part.get("duration") or video_data.get("duration", "0:00"),
                    "cid": part.get("cid"),
                    "aid": part.get("aid"),
                    "season_id": video_data.get("season_id", 0) if is_collection else 0,
                    "total_pages": len(parts),
                    "pubdate": part.get("pubdate", 0),
                }
                videos_payload.append(video_entry)
            print(f"📦 共 {len(videos_payload)} 个分P待处理")
        else:
            page_num = extract_page_number(bilibili_url)
            selected_part = next((p for p in parts if p.get("is_selected")), None)
            if selected_part:
                page_num = selected_part.get("part_index") or page_num
            page_idx = max(0, min(page_num - 1, len(parts) - 1))
            selected = parts[page_idx]
            print(f"📌 最终选第 {page_idx + 1}P: {selected.get('title', '')}")
            part_url = clean_url(selected.get("url", ""))
            video_entry = {
                "url": part_url,
                "thumbnail": clean_url(selected.get("thumbnail") or video_data.get("thumbnail", "")),
                "title": selected.get("title") or video_data.get("title", ""),
                "duration": selected.get("duration") or video_data.get("duration", "0:00"),
                "cid": selected.get("cid"),
                "aid": selected.get("aid"),
                "season_id": video_data.get("season_id", 0) if is_collection else 0,
                "total_pages": 1,
                "pubdate": selected.get("pubdate", 0),
            }
            videos_payload.append(video_entry)
    else:
        # 单视频
        videos_payload.append({
            "url": bilibili_url,
            "thumbnail": clean_url(video_data.get("thumbnail", "")),
            "title": video_data.get("title", ""),
            "duration": video_data.get("duration", "0:00"),
            "cid": video_data.get("cid"),
            "aid": video_data.get("aid"),
        })
        print(f"📹 单视频: {video_data.get('title', '')}")

    try:
        task = submit_process_task_with_payload(
            videos_payload,
            api_base=api_base, api_key=api_key, verify_ssl=verify_ssl,
        )
    except (requests.RequestException, APIError) as e:
        print(f"❌ 提交任务失败: {e}")
        sys.exit(1)

    # 响应格式参照前端: res.data = { success: true, task_ids: [...], success_count, total_count }
    res_data: dict[str, Any] = task.get("data", task)
    if not res_data or res_data.get("success") is not True:
        print(f"❌ 提交失败: {json.dumps(res_data, ensure_ascii=False)[:500]}")
        sys.exit(1)

    task_ids: list[str] = res_data.get("task_ids") or []
    if isinstance(task_ids, str):
        task_ids = [task_ids]
    if not isinstance(task_ids, list) or len(task_ids) == 0:
        single_id = res_data.get("task_id")
        if single_id:
            task_ids = [single_id]
    if not task_ids:
        print(f"❌ API 返回异常，未找到 task_id: {json.dumps(res_data, ensure_ascii=False)[:500]}")
        sys.exit(1)

    print(f"✅ 任务已提交: {len(task_ids)} 个任务，task_ids={task_ids}")

    # 5. 逐个轮询等待完成并归档
    repo_root = Path(__file__).resolve().parent.parent
    is_multi_batch = len(task_ids) > 1
    output_dir = repo_root / "📚_知识库分类" / category
    if is_multi_batch:
        collection_dir = output_dir / sanitize_filename(title)
        collection_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 合集目录: {collection_dir}")
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

    for i, task_id in enumerate(task_ids):
        print(f"\n{'='*40}")
        print(f"⏳ [{i+1}/{len(task_ids)}] 等待任务 {task_id} 完成...")
        result_data = poll_task(
            task_id,
            api_base=api_base, api_key=api_key, verify_ssl=verify_ssl,
            max_wait=poll_max_wait, interval=poll_interval,
        )
        if not result_data:
            print(f"❌ 任务 {task_id} 处理失败，跳过")
            continue

        print(f"📥 [{i+1}/{len(task_ids)}] 获取任务 {task_id} 完整结果...")
        detail = fetch_video_result(
            task_id,
            api_base=api_base, api_key=api_key, verify_ssl=verify_ssl,
        )
        if not detail:
            print(f"❌ 任务 {task_id} 未能获取完整结果，跳过")
            continue

        # 使用分P自己的标题（而非合集标题），去掉 .mp4 后缀
        part_title: str = detail.get("title") or f"{title}_P{i+1}"
        part_title = re.sub(r'\s*\.mp4$', '', part_title, flags=re.IGNORECASE)
        print(f"📹 [{i+1}/{len(task_ids)}] 标题: {part_title}")

        markdown_content = build_comprehensive_markdown(detail, part_title, bilibili_url)
        if not markdown_content:
            print(f"❌ 任务 {task_id} 未能生成 Markdown，跳过")
            continue

        safe_title = sanitize_filename(part_title)
        write_dir: Path = collection_dir if is_multi_batch else output_dir

        output_file = write_dir / f"{safe_title}.md"
        output_file.write_text(markdown_content, encoding="utf-8")
        print(f"✅ [{i+1}/{len(task_ids)}] 笔记已归档: {output_file}")

    print("\n🎉 全自动转写流水线执行完毕！")


if __name__ == "__main__":
    main()