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

## 📖 三步上手（配置你自己的 API Key，零成本打造自动化流水线）

> 💡 **提示**：本仓库仅提供代码和模板。为了让 Actions 跑起来，你需要花 3 秒去 [diting.cc](https://diting.cc) 免费获取属于你自己的超级 API Key，每人每天无条件白嫖 20 次额度！

| 步骤 | 你需要做的 | 自动化说明 |
| :--- | :--- | :--- |
| **① Fork 仓库 & 领 Key** | 1. 点击右上角 **Fork** 本仓库<br>2. 前往 👉 **[diting.cc](https://diting.cc)** 获取免费 API Key | 微信扫码即领，每人每天送 20 次免费额度 |
| **② 配置 Secrets** | 在你 Fork 后的私有仓库中点击 `Settings` ➔ `Secrets and variables` ➔ `Actions`，添加：`DITING_API_KEY` | 隐私安全：你的 Key 只有你自己的 GitHub 自动化脚本能调 |
| **③ 提交 Issue 挂机** | 在你 Fork 的仓库里新建一个 Issue，粘贴 B 站链接 | GitHub Actions 自动触发，云端服务器集群接管多线程转写 |

⚠️ **防恶意刷单规则**：如果你直接在我们的【官方仓库】提交 Issue 试用，每个 GitHub 账号每天限额 2 次。**强烈建议直接 Fork 并在你自己的仓库配置 Key，或者直接去 [https://diting.cc](https://diting.cc) 网页端使用，额度每日全自动刷新！**

---

## ⚡ 笔记长什么样？

点击文稿中所有的蓝色时间戳如 `[00:15:23]`，可双端无缝直达 B 站原视频对应秒数。每篇由谛听 AI 导出的标准化笔记均包含：
1. **智能精校逐字稿**（完美修复 AI 润色完整度，100% 不丢字断片）
2. **AI 润色精校版**（全自动修正口语、优化排版表达）
3. **AI 智能大纲**（核心知识脉络、结构化实体提取）
4. **核心 QA 问答对**（一分钟透视原片核心含金量）

🔍 **注：[全局思维导图]、[发言人隔离]、[多矩阵自媒体洗稿] 等变态级重度生产力功能，仅限 [https://diting.cc](https://diting.cc) 创作者版 PC 端呈现。**

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

"""

# 表格模板
TABLE_HEADER = "| 📌 课程/爆款视频长尾词 | 📊 包含P数 | ⚡ Markdown 语义笔记直链 | 🚀 云端算力引擎 |\n"
TABLE_DIVIDER = "| :--- | :--- | :--- | :--- |\n"

# README 尾部模板
README_FOOTER = """
---

 # 🎁 谛听 AI · 创作者扶持与"大V口碑赞助"计划
 
 为了回馈自媒体与开源社区，我们面向重度内容创作者、UP主和学习博主推出官方技术赞助。**因云端高并发服务器算力成本高昂，每月仅限 30 个赞助名额：**
 
 - **申请门槛**：B 站粉丝 ≥ 5000，或小红书/抖音/公众号粉丝 ≥ 1万（重度垂直的学习类、干货类、搞钱类博主优先）。
     
 - **大V置换权益**：点击下方二维码添加创始人微信，经核对主页后，**100% 免费开通价值 ¥598 /年的创作者全年无忧超级会员，**。
     
 - **大V应尽义务**：获得赞助的创作者，**需在正常体验产品后，在您的任一公域渠道（如朋友圈、博主互助群、小红书、视频置顶评论区）为【谛听 AI】进行一次真实的效率工具安利或体验评测**（需带上您的专属【分享赚】推荐链接，后续群友注册您还能继续躺赚现金抽成）。

<p align="center">
  <img src="https://github.com/user-attachments/assets/7855b3c1-8968-433a-82e0-0b6fd14b7db3" alt="创始人微信" width="200"/>
  <br>
  <b>📱 扫码添加创始人企业微信（备注：GitHub开源）直接领红包/开通大V免单</b>
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
  <br>
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
    """从文件名提取 SEO 关键词，去掉扩展名和序号前缀。"""
    name = filename.replace(".md", "")
    # 去掉 P01_ 这样的序号前缀
    name = re.sub(r'^[Pp]?\d+[._\s-]*', '', name)
    return name.strip()


def generate_readme():
    """扫描全库并生成完整的 README.md。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 从 git remote 获取仓库全名
    repo_full_name = os.environ.get("GITHUB_REPOSITORY", "user/repo")

    # 收集统计数据
    categories = [d for d in sorted(BASE_DIR.iterdir()) if d.is_dir() and d.name != ".gitkeep"]
    total_notes = 0
    active_categories = 0

    content = README_HEADER
    content = content.replace("{{UPDATED_AT}}", now)
    content = content.replace("{{REPO_FULL_NAME}}", repo_full_name)

    # 遍历每个分类
    for category in categories:
        cat_name = category.name
        subfolders = get_subfolders(category)

        # 如果分类下直接有 .md 文件（无子文件夹结构）
        direct_notes = get_notes(category)

        if not subfolders and not direct_notes:
            continue

        active_categories += 1
        content += f"### {cat_name}\n\n"

        if subfolders:
            content += TABLE_HEADER + TABLE_DIVIDER
            for subfolder in subfolders:
                notes = get_notes(subfolder)
                total_notes += len(notes)
                course_name = subfolder.name

                for note in notes:
                    keyword = extract_keyword(note.name)
                    # 构建相对链接
                    rel_path = f"./📚_知识库分类/{cat_name}/{course_name}/{note.name}".replace(" ", "%20")
                    content += f"| {keyword} 文案字幕下载 | 批量托管 | [📂 点击免积分阅读]({rel_path}) | [diting.cc 谛听 AI](https://diting.cc) |\n"

        if direct_notes:
            content += TABLE_HEADER + TABLE_DIVIDER
            total_notes += len(direct_notes)
            for note in direct_notes:
                keyword = extract_keyword(note.name)
                rel_path = f"./📚_知识库分类/{cat_name}/{note.name}".replace(" ", "%20")
                content += f"| {keyword} 文案字幕下载 | 批量托管 | [📂 点击免积分阅读]({rel_path}) | [diting.cc 谛听 AI](https://diting.cc) |\n"

        content += "\n"

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