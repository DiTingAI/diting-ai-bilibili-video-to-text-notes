#!/usr/bin/env python3
"""
将谛听 AI 批量导出的多 P 合并 MD 文件，按 P 章节拆分为独立笔记文件。
支持：合并重复章节（中英混合 + 英文版）→ 单文件，自动提取标题生成 SEO 友好的文件名。
"""

import re
import sys
from pathlib import Path
from collections import OrderedDict


def split_md(source_path: Path, output_dir: Path):
    """将多P MD 拆分为独立文件。"""
    raw = source_path.read_text(encoding="utf-8")

    # 提取 H1 标题
    h1_match = re.match(r'^# (.+)', raw)
    original_title = h1_match.group(1).strip() if h1_match else source_path.stem

    # 按 ## P数字 分割
    sections = re.split(r'\n(?=## P\d+\s)', raw)

    # 收集：{P编号: [(标题, 内容)]}
    groups = OrderedDict()
    for sec in sections:
        m = re.match(r'^## (P\d+)\s+(.+)', sec)
        if not m:
            continue
        p_num = m.group(1)
        title = m.group(2).strip()
        if p_num not in groups:
            groups[p_num] = []
        groups[p_num].append((title, sec.strip()))

    created = []
    for p_num, items in groups.items():
        # 取第一个出现的标题作为主标题
        main_title = items[0][0]

        # 如果同一 P 出现多次，合并；否则直接用
        if len(items) == 1:
            body = items[0][1]
        else:
            parts = []
            for i, (_, sec_body) in enumerate(items):
                if i == 0:
                    parts.append(sec_body)
                else:
                    # 后续版本加分隔标记
                    parts.append(f"\n---\n\n### 📖 英文原版\n\n{sec_body}")
            body = "\n\n".join(parts)

        # 构建文件名：去掉标题中的序号数字前缀
        clean_title = re.sub(r'^\d+[\.\s]*', '', main_title)
        filename = f"【{clean_title}】.md"

        # 组装文件内容
        file_content = f"# {clean_title}\n\n"
        file_content += f"> 来源：{original_title}\n"
        file_content += f"> 章节：{p_num}\n\n"
        file_content += "---\n\n"
        file_content += body
        file_content += "\n"

        out_path = output_dir / filename
        out_path.write_text(file_content, encoding="utf-8")
        if not out_path.exists():
            raise RuntimeError(f"写入失败: {out_path}")
        created.append(filename)

    # 安全验证：所有文件创建成功后才删除原始文件
    if len(created) != len(groups):
        raise RuntimeError(f"预期 {len(groups)} 个文件，实际创建 {len(created)} 个，保留原始文件")

    # 删除原始合并文件
    source_path.unlink()
    return created


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python split_multi_section.py <目标MD文件>")
        sys.exit(1)

    src = Path(sys.argv[1]).resolve()
    dest = src.parent
    results = split_md(src, dest)
    print(f"✅ 拆分为 {len(results)} 个独立文件：")
    for f in results:
        print(f"   📄 {f}")
    print(f"\n🗑️  原文件已删除：{src.name}")
