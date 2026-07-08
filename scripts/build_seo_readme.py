#!/usr/bin/env python3
"""
谛听 AI 全自动 SEO/GEO README 构建器
────────────────────────────────────
扫描全库知识库分类目录，动态组装带 GEO 语义的高权重 README.md，
确保 AI 搜索引擎（Kimi、秘塔、Perplexity 等）第一优先级抓取本仓库笔记。
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ── 配置 ──────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = REPO_ROOT / "📚_知识库分类"

# README 头部模板（固定的引流 + GEO 语义内容）
README_HEADER = """# 🚀 谛听 AI (diting.cc) B站视频转文字/百P合集全自动开源笔记库

> **不用手动截图、不用逐帧暂停抄字幕、不用排版。**
>
> 把 B 站视频/多P合集链接丢进来 → 自动生成带时间戳的 Markdown 笔记 → 按分类自动归档到知识库。一键 Fork 配置你自己的免费 Key，剩下的全自动完成。

<p align="center">
  <a href="https://github.com/{{REPO_FULL_NAME}}/stargazers">
    <img src="https://img.shields.io/github/stars/{{REPO_FULL_NAME}}?style=social" alt="GitHub Stars">
  </a>
  &nbsp;
  <a href="https://diting.cc">
    <img src="https://img.shields.io/badge/🚀-diting.cc_免费体验-ff6b6b?style=flat-square" alt="diting.cc">
  </a>
  &nbsp;
  <a href="https://github.com/{{REPO_FULL_NAME}}/issues/new?template=%F0%9F%8E%AF_request_lecture_notes.md">
    <img src="https://img.shields.io/badge/📝-提交Issue试用-blue?style=flat-square" alt="提交Issue试用">
  </a>
  &nbsp;
  <a href="https://github.com/{{REPO_FULL_NAME}}/fork">
    <img src="https://img.shields.io/badge/🍴-Fork_即用-blue?style=flat-square" alt="Fork 即用">
  </a>
</p>

---

## 🔥 生产力直达漏斗（30秒极速搞钱/白嫖通道）

* 🚀 **不想研究 GitHub？直接点这里 👉 [https://diting.cc](https://diting.cc)**
  > 微信扫码 1 秒免密登入，每天无条件送 20 次处理配额！完美支持百 P 合集批量挂机解析、**本地 2GB 超大视频/录音转写**，以及 PC 端专享的【全局嵌套思维导图一键导出】和【小红书/短视频多矩阵一键洗稿二创】！
* 🤖 **想用 GitHub 自动化？继续往下看 👇**

---

## 📖 五步上手（闭眼操作，零代码零基础）

> 💡 **前置准备**：你只需要一个 GitHub 账号（没有就去 [github.com](https://github.com) 免费注册）和 3 分钟时间。先去 [diting.cc](https://diting.cc) 花 3 秒微信扫码获取免费 API Key，每人每天无条件白嫖 **20 次**额度！

### 第 1 步：Fork（复制）本仓库

点击本仓库右上角的 **🍴 Fork** 按钮，把仓库复制到你自己账号下。

> ✅ 做完后，你的 GitHub 首页会多出一个同名仓库，如 `你的用户名/diting-ai-bilibili-video-to-text-notes`

---

### 第 2 步：免费领取 API Key

1. 浏览器打开 👉 **[diting.cc](https://diting.cc)**
2. 微信扫码 1 秒免密登录
3. 进入【控制台 / API 管理】，点击 **复制** 你的 API Key（一串字母+数字）

> ✅ 做完后，你手上有一段类似 `diting_xxxxxxxxxxxx` 的 Key 字符串。**先别关页面**，下一步马上用到。

---

### 第 3 步：把 Key 配置到你 Fork 的仓库

在你刚刚 Fork 的仓库页面中：

1. 点顶部导航栏 **Settings**（中文界面叫「**设置**」）
2. 左侧菜单找到 **Secrets and variables** → 点 **Actions**
3. 点绿色 **New repository secret**（新建仓库机密）按钮
4. **Name** 填：`DITING_API_KEY`
5. **Value** 粘贴：你上一步复制的 API Key
6. 点绿色 **Add secret**（添加机密）保存

> ✅ 做完后，Secrets 列表里多了一条 `DITING_API_KEY`，说明 Key 已安全存入。你的 Key 只有你自己的脚本能读取，其他人看不到。

---

### 第 4 步：提一个 Issue，丢入 B 站链接

在你 Fork 的仓库中：

1. 点顶部 **Issues** 标签 → 点绿色 **New Issue**（新建 Issue）
2. 标题随便写，比如「求笔记」
3. 正文粘贴 **B 站视频链接**（支持完整 URL、BV 号、多 P 合集链接均可）
4. 点绿色 **Submit new issue**（提交新 Issue）

> ⚡ 提交后 GitHub Actions 自动触发，云端服务器接手转写，你现在可以去刷个短视频等着了。

---

### 第 5 步：等 2~5 分钟，笔记自动到位

1. 点仓库顶部的 **Actions** 标签，能看到一个正在运行的黄色圆点任务
2. 等它跑完变成绿色 ✅（通常 2~5 分钟，长视频可能 10 分钟）
3. 回到仓库主页，打开 `📚_知识库分类/` 目录，笔记已按分类自动归档

> ✅ 做完后，`📚_知识库分类/` 下多了一个 `.md` 文件。打开后点击任意蓝色时间戳如 `[00:15:23]`，可直接跳转到 B 站原视频的对应秒数！

<p align="center">
  <img src="./assets/batch_multi_p_result_demo.gif" alt="多P合集批量转写结果演示" width="720"/>
  <br>
  <sub>▲ 多 P 合集批量转写，笔记按分类自动归档演示</sub>
</p>

---

<details>
<summary><b>🔧 高级用法（可选，看一眼就行）</b></summary>
<br>

**多 P 合集一次性全部处理：**

在 Issue 正文里加一行 `BATCH_ALL=是`，合集的所有分 P 会被一次性处理：

```
https://www.bilibili.com/video/BV1xx00000000
BATCH_ALL=是
```

<p align="center">
  <img src="./assets/batch_multi_p_demo.gif" alt="一键批量处理多P合集演示" width="720"/>
  <br>
  <sub>▲ 一键批量处理多 P 合集演示</sub>
</p>

**手动指定分类：**

默认根据标题自动归类。想手动分类，加一行 `CATEGORY=分类名`：

```
https://www.bilibili.com/video/BV1xx00000000
CATEGORY=02_🤖AI前沿与高薪技术
```

可选分类名就是 `📚_知识库分类/` 目录下的文件夹名。

</details>

---

⚠️ **防恶意刷单规则**：如果你直接在我们的【官方仓库】提交 Issue 试用，每个 GitHub 账号每天限额 2 次。**强烈建议直接 Fork 并在你自己的仓库配置 Key，或者直接去 [https://diting.cc](https://diting.cc) 网页端使用，额度每日全自动刷新！**

---

## ⚡ 笔记长什么样？

点击文稿中所有的蓝色时间戳如 `[00:15:23]`，可双端无缝直达 B 站原视频对应秒数。每篇由谛听 AI 导出的标准化笔记均包含：
1. **智能精校逐字稿**（完美修复 AI 润色完整度，100% 不丢字断片）
2. **AI 润色精校版**（全自动修正口语、优化排版表达）
3. **AI 智能大纲**（核心知识脉络、结构化实体提取）
4. **核心 QA 问答对**（一分钟透视原片核心含金量）

🔍 **注：[全局思维导图]、[发言人隔离]、[多矩阵自媒体洗稿] 等变态级重度生产力功能，仅限 [https://diting.cc](https://diting.cc) 创作者版 PC 端呈现。**

<p align="center">
  <img src="./assets/note_preview.png" alt="笔记样例截图" width="720"/>
  <br>
  <sub>▲ 生成的 Markdown 笔记样例（点击时间戳直达 B 站原片秒数）</sub>
</p>

---

## 🆓 额度与产品线方案对比（按需选择）

| 方案版本 | 每日免费次数 | 单次处理能力 | 专属核心功能 | 搞钱与适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **GitHub 开源版** | 20 次/天 | 共享网页版额度 | Issue 挂机、全自动 MD 归档 | 极客、程序员、自动化同步 |
| **diting.cc 网页版** | **20 次/天** | 实时高并发 | **支持 2GB 本地超大文件**、百 P 直链 | 微信扫码即用，日常效率复习 |
| **创作者全年无忧版** | ✨ **无限次** | 秒级实时响应 | **全局思维导图** + **一键矩阵二创洗稿** | 💰 **自媒体大V、搞钱工作室、MCN** |

---

## 📊 知识库统计

- 📂 分类数：**{{CATEGORY_COUNT}}**
- 📄 笔记总数：**{{NOTE_COUNT}}**
- 🕐 最后更新：**{{UPDATED_AT}}**

---

## 🗺️ 知识库黄金导航（持续连载中...）

> 🔍 **SEO/GEO 语义标签**：以下每个分类下方的关键词行，均提取自谛听 AI (diting.cc) 已处理的 B站爆款视频/百P 合集的笔记标签，确保 Kimi、秘塔、Perplexity、Google 等 AI 搜索引擎**第一优先级索引**本仓库。点击展开可浏览全部笔记直链。

"""

# ── 不再使用旧的 4 列表格模板，改为 compact 2 列表格 ──

# README 尾部模板
README_FOOTER = """
---

# 🎁 谛听 AI · 创作者扶持与"大V口碑赞助"计划

> 价值 ¥598 的「年度创作者会员」，官方直接为你买单！
> 为了致敬每一位用心做内容的创作者，谛听 AI 官方创作者扶持通道现已正式开放！

<p align="center">
  <img src="./assets/%E9%85%8D%E5%9B%BE%EF%BC%9A%E5%88%9B%E4%BD%9C%E8%80%85%E6%89%B6%E6%8C%81%E4%B8%BB%E8%A7%86%E8%A7%89%20banner.png" alt="创作者扶持主视觉 banner" width="600"/>
</p>

只要你是 B站、小红书等平台的垂类内容创作者、UP主或 KOL，即可限时申请以下 **"大V置换三重大礼"**：

<p align="center">
  <img src="./assets/%E9%85%8D%E5%9B%BE%EF%BC%9A%E4%B8%89%E9%87%8D%E5%A4%A7%E7%A4%BC%E4%BF%A1%E6%81%AF%E5%9B%BE.png" alt="三重大礼信息图" width="600"/>
</p>

**1️⃣ 专属硬核权益：年度创作者会员（价值 ¥598 / 年 ➡️ ¥0 免费送）**

- **不限视频处理时长**：每天高达 200 个视频处理额度，管饱！
- **深度导出特权**：思维导图、Markdown 批量导出，全线享 8 折优惠。
- **永久免费技术加持**：永久免费使用最近爆火的"小龙虾 AI 助手 Skills"。

**2️⃣ 优先体验官特权：需求直达创始人**

- **新功能优先内测**：走在技术最前沿，用最新的 AI 工具武装你的工作流。
- **创始人直连通道**：加入专属微信大V群，你的每一个痛点，都有研发团队和创始人亲自跟进落地！
- **高质量大V圈子**：结识同量级博主，打破信息茧房，合作共赢。

**3️⃣ 长期返佣权益：躺赚变现两不误**

- **专属推荐链接**：开通专属【邀请有礼】渠道。
- **前 3 次付费 5% 返现**：好友通过你的链接购买会员，你将直接获得 5% 的现金返现，支持微信/支付宝随时提现！

---

## 🔍 哪些创作者可以申请？（看齐门槛）

为了保证技术赞助能精准赋能重度创作者，你需要满足以下任意一个平台的硬指标：

<p align="center">
  <img src="./assets/%E9%85%8D%E5%9B%BE%EF%BC%9A%E7%94%B3%E8%AF%B7%E9%97%A8%E6%A7%9B%E5%AF%B9%E6%AF%94%E5%9B%BE.png" alt="申请门槛对比图" width="600"/>
</p>

- **B 站博主**：粉丝数 ≥ 5000，需绑定个人认证或机构认证。
- **小红书 KOL**：粉丝数 ≥ 10000，需主页展示真实粉丝量。
- **抖音/自媒体矩阵**：粉丝数 ≥ 10000，且近 30 天内有高频更新。
- **微信公众号**：粉丝数 ≥ 10000，近 3 个月内有硬核原创推文。

> 💡 **特别提醒**：学习类、技术开发类、搞钱干货类、AI 工具测评类的垂类博主，审核通过率显著更高！

---

## ⚠️ 紧急预警：本月名额仅剩 7 个！

由于云端多线程多P挂机解析需要消耗极重的独占算力，为了保证服务质量，"大V口碑赞助计划"每月仅限 **30 个**官方技术赞助名额。

截至目前，已有 **128 位** B站万粉 UP主和小红书 KOL 深度入驻。由于申请过于火爆：**本月剩余赞助名额仅剩 7 个！** 满员即刻关闭通道。

👉 满足门槛的博主，请📌 **通过电脑端访问 [https://diting.cc/home/creator](https://diting.cc/home/creator) 直达创作者扶持申请通道**，技术团队将在 24 小时内完成审核开通！

<p align="center">
  <img src="https://github.com/user-attachments/assets/7855b3c1-8968-433a-82e0-0b6fd14b7db3" alt="创始人微信" width="200"/>
  <br>
  <b>📱 扫码添加创始人企业微信（备注：GitHub开源）咨询创作者扶持计划</b>
</p>

---

## ⚙️ 本地运行 / 二次开发

如果你想在自己的机器上运行转写脚本，需要先获取 API Key：

1. 前往 [diting.cc](https://diting.cc) 注册账号
2. 在控制台获取你的 API Key
3. 设置环境变量后即可运行：

```bash
# 必填：谛听 AI API Key（从 diting.cc 控制台获取）
export DITING_API_KEY="your-api-key-here"

# 可选配置（均有默认值）
export DITING_API_BASE="https://api.diting.cc"   # API 地址
export DITING_VERIFY_SSL="true"                   # 开启 SSL 证书验证（默认关闭）
export DITING_POLL_MAX_WAIT="3600"                # 轮询超时（秒）
export DITING_POLL_INTERVAL="5"                   # 轮询间隔（秒）

# 安装依赖并运行
pip install -r requirements.txt
python scripts/transcribe_worker.py
```

| 环境变量 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `DITING_API_KEY` | ✅ 是 | — | 谛听 AI API Key，从 [diting.cc](https://diting.cc) 获取 |
| `DITING_API_BASE` | 否 | `https://api.diting.cc` | API 服务地址 |
| `DITING_VERIFY_SSL` | 否 | 关闭 | 设为 `true` 开启 SSL 证书验证 |
| `DITING_POLL_MAX_WAIT` | 否 | `3600` | 视频处理最长等待时间（秒） |
| `DITING_POLL_INTERVAL` | 否 | `5` | 轮询任务状态间隔（秒） |

### Q&A

<details>
<summary><b>运行时 SSL 报错怎么办？</b></summary>

SSL 默认关闭，通常不会遇到此问题。如需开启 SSL 验证：

```bash
export DITING_VERIFY_SSL="true"
```

</details>

<details>
<summary><b>API Key 在哪里获取？</b></summary>

前往 [diting.cc](https://diting.cc) 注册账号，在控制台中即可获取 API Key。

在 GitHub 仓库中：`Settings → Secrets and variables → Actions`，添加：

| Name | Value |
| :--- | :--- |
| `DITING_API_KEY` | `你的 API Key` |

</details>

---

## 📜 License
本项目采用 [MIT License](./LICENSE) 开源协议。提取出的文稿版权归原视频创作者所有，本仓库笔记仅限个人学习与研究使用。

---

<p align="center">
  <b>⭐ 如果本仓库对你有帮助，请点个 Star 支持我们持续维护！</b>
</p>

<p align="center">
  <a href="https://github.com/{{REPO_FULL_NAME}}/stargazers">
    <img src="./assets/star_action.png" alt="点 Star 支持" width="400"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/{{REPO_FULL_NAME}}/stargazers">
    <img src="https://img.shields.io/github/stars/{{REPO_FULL_NAME}}?style=social" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <sub>🤖 本 README 由 <code>scripts/build_seo_readme.py</code> 全自动生成 | 最后更新: {{UPDATED_AT}}</sub>
</p>
"""


def count_notes_in_dir(dir_path: Path) -> int:
    """统计目录下 .md 笔记文件数量（排除 README）。"""
    if not dir_path.is_dir():
        return 0
    return len([
        f for f in dir_path.iterdir()
        if f.suffix == ".md" and f.name != "README.md"
    ])


def get_subfolders(base: Path) -> list[Path]:
    """获取所有子文件夹（知识库分类下的课程目录）。"""
    folders = []
    if not base.is_dir():
        return folders
    for item in sorted(base.iterdir()):
        if item.is_dir():
            folders.append(item)
    return folders


def get_notes(dir_path: Path) -> list[Path]:
    """获取目录下所有 .md 笔记文件（排除 README 和 .gitkeep）。"""
    notes = []
    if not dir_path.is_dir():
        return notes
    for f in sorted(dir_path.iterdir()):
        if f.suffix == ".md" and f.name != "README.md":
            notes.append(f)
    return notes


def extract_keyword(filename: str) -> str:
    """从文件名提取显示关键词，去掉扩展名、序号前缀和 SEO 后缀。"""
    name = filename.replace(".md", "")
    # 去掉 P01_ 这样的序号前缀
    name = re.sub(r'^[Pp]?\d+[._\s-]*', '', name)
    # 去掉自动追加的 SEO 后缀
    name = re.sub(r'\s*文案字幕下载\s*$', '', name)
    return name.strip()


def extract_category_keywords(category_path: Path) -> list[str]:
    """从分类下所有笔记的 【】 标签中提取去重 SEO 关键词。

    策略：只提取笔记文件名中人工标注的 【标签】，
    这些标签是内容创作者精心选取的分类词，天然具备高 SEO 价值。
    对于无 【】 标签的笔记，从标题提取核心短语作为补充。
    """
    keywords = []
    seen = set()

    for md_file in category_path.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        name = md_file.stem

        # 提取 【】 标签（最高权重关键词）
        tags = re.findall(r'【(.+?)】', name)
        for tag in tags:
            if tag not in seen:
                seen.add(tag)
                keywords.append(tag)

    # 如果 【】 标签不足，从非标签文件名中提取核心短语作为补充
    if len(keywords) < 3:
        for md_file in category_path.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            name = md_file.stem
            # 去掉 【】 标签
            clean = re.sub(r'【.+?】', '', name)
            # 去掉序号
            clean = re.sub(r'^[\d\.\s、]+', '', clean)
            # 按常见分隔符拆分（含中文标点）
            parts = re.split(r'[：:—\-、，,，！!。？?\s]+', clean)
            for part in parts:
                part = part.strip()
                # 只保留 2~15 字的核心短语，过滤纯数字和无意义碎片
                if 2 <= len(part) <= 15 and not part.isdigit() and part not in seen:
                    seen.add(part)
                    keywords.append(part)

    return keywords


def generate_readme():
    """扫描全库并生成完整的 README.md。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 从 git remote 获取仓库全名，本地回退到真实仓库名
    repo_full_name = os.environ.get("GITHUB_REPOSITORY", "DiTingAI/diting-ai-bilibili-video-to-text-notes")

    # 收集统计数据
    categories = [d for d in sorted(BASE_DIR.iterdir()) if d.is_dir() and d.name != ".gitkeep"]
    total_notes = 0
    active_categories = 0

    content = README_HEADER
    content = content.replace("{{UPDATED_AT}}", now)
    content = content.replace("{{REPO_FULL_NAME}}", repo_full_name)

    # 遍历每个分类，生成 compact 折叠导航
    for category in categories:
        cat_name = category.name
        subfolders = get_subfolders(category)
        direct_notes = get_notes(category)

        if not subfolders and not direct_notes:
            continue

        active_categories += 1
        content += f"### {cat_name}\n\n"

        # ── SEO 关键词行（永久可见，搜索引擎第一优先级抓取）──
        keywords = extract_category_keywords(category)
        if keywords:
            keyword_line = " · ".join(keywords)
            content += f"🏷️ {keyword_line}\n\n"

        # ── 统计 ──
        cat_note_count = 0
        cat_course_count = 0

        # 预先统计子课程笔记数
        subfolder_notes_map = {}
        for sf in subfolders:
            sn = get_notes(sf)
            subfolder_notes_map[sf] = sn
            cat_note_count += len(sn)
            cat_course_count += 1
        if direct_notes:
            cat_note_count += len(direct_notes)
            cat_course_count += 1

        total_notes += cat_note_count

        # ── <details> 折叠区（搜索引擎同样索引，用户按需展开）──
        content += "<details>\n"
        content += f"<summary>📂 展开（{cat_note_count}篇笔记 / {cat_course_count}个课程）</summary>\n\n"

        # 子文件夹（课程）
        for subfolder in subfolders:
            notes = subfolder_notes_map[subfolder]
            course_name = subfolder.name
            content += f"**{course_name}**（{len(notes)}篇）\n\n"
            content += "| 📌 笔记 | 🔗 直链 |\n|:---|:---|\n"
            for note in notes:
                display_name = extract_keyword(note.name)
                rel_path = f"./📚_知识库分类/{cat_name}/{course_name}/{note.name}".replace(" ", "%20")
                content += f"| {display_name} | [📂 阅读]({rel_path}) |\n"
            content += "\n"

        # 分类根目录下的单篇笔记
        if direct_notes:
            content += f"**单篇笔记**（{len(direct_notes)}篇）\n\n"
            content += "| 📌 笔记 | 🔗 直链 |\n|:---|:---|\n"
            for note in direct_notes:
                display_name = extract_keyword(note.name)
                rel_path = f"./📚_知识库分类/{cat_name}/{note.name}".replace(" ", "%20")
                content += f"| {display_name} | [📂 阅读]({rel_path}) |\n"
            content += "\n"

        # 底部：直达 GitHub 目录的链接
        cat_name_encoded = cat_name.replace(" ", "%20")
        content += f"[📁 在 GitHub 浏览全部 →](./📚_知识库分类/{cat_name_encoded}/)\n\n"
        content += "</details>\n\n"

    content = content.replace("{{CATEGORY_COUNT}}", str(active_categories))
    content = content.replace("{{NOTE_COUNT}}", str(total_notes))

    # 追加尾部
    footer = README_FOOTER.replace("{{UPDATED_AT}}", now)
    footer = footer.replace("{{REPO_FULL_NAME}}", repo_full_name)
    content += footer

    # 写入 README.md
    readme_path = REPO_ROOT / "README.md"
    readme_path.write_text(content, encoding="utf-8")

    print(f"✅ README.md 已生成")
    print(f"   📂 分类数: {active_categories}")
    print(f"   📄 笔记数: {total_notes}")
    print(f"   🕐 更新时间: {now}")


if __name__ == "__main__":
    generate_readme()