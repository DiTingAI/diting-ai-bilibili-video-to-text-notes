#!/usr/bin/env python3
"""
谛听 AI 全自动转写 Worker 回归测试
────────────────────────────────────
测试 transcribe_worker.py 中所有纯函数的正确性。
运行方式：pytest scripts/test_transcribe_worker.py -v
"""

import sys
import pytest
from pathlib import Path

# 确保可以导入 transcribe_worker 中的函数
sys.path.insert(0, str(Path(__file__).resolve().parent))

from transcribe_worker import (
    extract_bilibili_url,
    classify_category,
    sanitize_filename,
    clean_url,
    extract_bvid,
    extract_page_number,
    timestamp_to_seconds,
    convert_timestamps_to_links,
    build_outline_markdown,
    build_mindmap_markdown,
    build_mindmap_from_tree,
    build_comprehensive_markdown,
    extract_text,
    _parse_batch_all,
    _parse_manual_category,
    FALLBACK_CATEGORY,
)


# ════════════════════════════════════════════════════════
#  1. extract_bilibili_url — URL 提取
# ════════════════════════════════════════════════════════

class TestExtractBilibiliUrl:
    def test_full_url(self):
        url = "https://www.bilibili.com/video/BV1DfrdByE2H?spm_id_from=333.788&p=4"
        result = extract_bilibili_url(f"请转写 {url}")
        assert result == url

    def test_full_url_https(self):
        url = "https://www.bilibili.com/video/BV1234567890/"
        result = extract_bilibili_url(f"链接：{url} 谢谢")
        assert result == url

    def test_full_url_no_space_boundary(self):
        url = "https://www.bilibili.com/video/BV1xx0000000"
        result = extract_bilibili_url(f"text{url}")
        assert result == url

    def test_bare_bv_number(self):
        result = extract_bilibili_url("请转写 BV1DfrdByE2H 这个视频")
        assert result == "https://www.bilibili.com/video/BV1DfrdByE2H"

    def test_bare_bv_number_lowercase(self):
        result = extract_bilibili_url("BV1aAbBcCdDe")
        assert result == "https://www.bilibili.com/video/BV1aAbBcCdDe"

    def test_no_url(self):
        result = extract_bilibili_url("这是一段没有链接的文字")
        assert result is None

    def test_no_url_empty(self):
        result = extract_bilibili_url("")
        assert result is None

    def test_non_bilibili_url(self):
        result = extract_bilibili_url("https://www.youtube.com/watch?v=abc123")
        assert result is None


# ════════════════════════════════════════════════════════
#  2. classify_category — 分类归并
# ════════════════════════════════════════════════════════

class TestClassifyCategory:
    def test_ai_keywords(self):
        result = classify_category("吴恩达深度学习教程", "")
        assert "AI" in result

    def test_ai_agent_keywords(self):
        result = classify_category("Agent智能体开发实战", "")
        assert "AI" in result

    def test_exam_keywords(self):
        result = classify_category("2025考研数学张宇全程班", "")
        assert "考研" in result

    def test_design_keywords(self):
        result = classify_category("PS教程 Photoshop从入门到精通", "")
        assert "设计" in result

    def test_business_keywords(self):
        result = classify_category("商业财经分析 股票投资入门", "")
        assert "商业" in result

    def test_selfmedia_keywords(self):
        result = classify_category("自媒体运营 抖音短视频拍摄技巧", "")
        assert "自媒体" in result

    def test_short_keyword_boundary_ai(self):
        """短关键词 AI 不应误匹配 「certain」等单词"""
        result = classify_category("certain specific details", "")
        assert result == FALLBACK_CATEGORY

    def test_short_keyword_boundary_ps(self):
        """短关键词 PS 使用 \b 边界匹配"""
        result = classify_category("PS入门", "")
        assert "设计" in result

    def test_mixed_keywords_highest_count_wins(self):
        """匹配关键词最多的分类胜出"""
        result = classify_category("AI Python 深度学习 后端 前端 全栈", "")
        assert "AI" in result  # 匹配了 AI, Python, 深度学习, 前端, 后端, 全栈 = 6个

    def test_no_match_fallback(self):
        result = classify_category("今天天气真好", "")
        assert result == FALLBACK_CATEGORY

    def test_body_keywords(self):
        result = classify_category("某视频", "需要AI Python编程学习资料")
        assert "AI" in result

    def test_short_keyword_boundary_ui(self):
        result = classify_category("UI design tutorial", "")
        assert "设计" in result

    def test_short_keyword_boundary_ux(self):
        result = classify_category("UX research", "")
        assert "设计" in result


# ════════════════════════════════════════════════════════
#  3. sanitize_filename — 文件名清理
# ════════════════════════════════════════════════════════

class TestSanitizeFilename:
    def test_remove_special_chars(self):
        result = sanitize_filename('test:file<name>"with|chars?')
        assert result == "testfilenamewithchars"

    def test_remove_slash_backslash(self):
        result = sanitize_filename("file/name\\test")
        assert result == "filenametest"

    def test_whitespace_normalization(self):
        result = sanitize_filename("  hello   world  ")
        assert result == "hello world"

    def test_long_name_truncation(self):
        long_name = "A" * 100 + " B" * 100
        result = sanitize_filename(long_name, max_len=80)
        assert len(result) <= 80
        # 应该在80字符内最近的空格处截断
        assert "B" not in result  # B部分被截掉了

    def test_normal_name(self):
        result = sanitize_filename("【吴恩达】Agent教程")
        assert result == "【吴恩达】Agent教程"


# ════════════════════════════════════════════════════════
#  4. clean_url — URL 清理
# ════════════════════════════════════════════════════════

class TestCleanUrl:
    def test_trim_backticks(self):
        result = clean_url("`https://bilibili.com/video/BV123`")
        assert result == "https://bilibili.com/video/BV123"

    def test_trim_whitespace(self):
        result = clean_url("  https://bilibili.com/video/BV123  ")
        assert result == "https://bilibili.com/video/BV123"

    def test_clean_url_no_change(self):
        url = "https://bilibili.com/video/BV123"
        result = clean_url(url)
        assert result == url


# ════════════════════════════════════════════════════════
#  5. extract_bvid — BV 号提取
# ════════════════════════════════════════════════════════

class TestExtractBvid:
    def test_standard_bv(self):
        result = extract_bvid("https://www.bilibili.com/video/BV1DfrdByE2H?p=4")
        assert result == "BV1DfrdByE2H"

    def test_no_bv(self):
        result = extract_bvid("https://www.bilibili.com/")
        assert result is None

    def test_bv_no_params(self):
        result = extract_bvid("https://www.bilibili.com/video/BV1xx00000000/")
        assert result == "BV1xx00000000"


# ════════════════════════════════════════════════════════
#  6. extract_page_number — 分P页码提取
# ════════════════════════════════════════════════════════

class TestExtractPageNumber:
    def test_with_p_param(self):
        result = extract_page_number("https://www.bilibili.com/video/BV123?p=5")
        assert result == 5

    def test_with_amp_p_param(self):
        result = extract_page_number("https://www.bilibili.com/video/BV123?spm=1&p=3&vd=abc")
        assert result == 3

    def test_no_p_param(self):
        result = extract_page_number("https://www.bilibili.com/video/BV123")
        assert result == 1

    def test_p_first_param(self):
        result = extract_page_number("https://www.bilibili.com/video/BV123?p=42&other=abc")
        assert result == 42


# ════════════════════════════════════════════════════════
#  7. timestamp_to_seconds — 时间戳转秒数
# ════════════════════════════════════════════════════════

class TestTimestampToSeconds:
    def test_hh_mm_ss(self):
        assert timestamp_to_seconds("01:30:45") == 5445

    def test_hh_mm_ss_ms(self):
        assert timestamp_to_seconds("00:05:30.500") == 330

    def test_zero(self):
        assert timestamp_to_seconds("00:00:00") == 0

    def test_one_hour(self):
        assert timestamp_to_seconds("01:00:00") == 3600

    def test_max_value(self):
        assert timestamp_to_seconds("99:59:59") == 359999

    def test_invalid_format(self):
        # 格式不对返回 0
        assert timestamp_to_seconds("abc") == 0
        assert timestamp_to_seconds("12:34") == 0


# ════════════════════════════════════════════════════════
#  8. convert_timestamps_to_links — 时间戳→可点击链接
# ════════════════════════════════════════════════════════

class TestConvertTimestampsToLinks:
    BASE_URL = "https://www.bilibili.com/video/BV123"

    def test_bracketed_timestamp(self):
        text = "[00:05:30] 这是第一段内容"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert "[00:05:30](https://www.bilibili.com/video/BV123?t=330)" in result
        assert "这是第一段内容" in result

    def test_line_start_timestamp(self):
        text = "00:01:15 开始介绍"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert "[00:01:15](https://www.bilibili.com/video/BV123?t=75)" in result

    def test_multiple_timestamps(self):
        text = "[00:00:00] 开头\n[00:01:00] 第一章\n00:02:00 第二章"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert "[00:00:00](https://www.bilibili.com/video/BV123?t=0)" in result
        assert "[00:01:00](https://www.bilibili.com/video/BV123?t=60)" in result
        assert "[00:02:00](https://www.bilibili.com/video/BV123?t=120)" in result

    def test_url_with_existing_query(self):
        url = "https://www.bilibili.com/video/BV123?p=1"
        text = "[00:00:10] test"
        result = convert_timestamps_to_links(text, url)
        assert "&t=10" in result

    def test_timestamp_with_ms(self):
        text = "[00:00:00.500] 毫秒时间戳"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert "[00:00:00.500](https://www.bilibili.com/video/BV123?t=0)" in result

    def test_no_timestamp(self):
        text = "这是没有时间戳的内容"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert result == text

    def test_mixed_content(self):
        text = "00:00:00 开头\n普通段落\n[00:01:00] 带括号时间戳"
        result = convert_timestamps_to_links(text, self.BASE_URL)
        assert "[00:00:00]" in result
        assert "[00:01:00]" in result
        assert "普通段落" in result


# ════════════════════════════════════════════════════════
#  9. build_outline_markdown — AI 大纲渲染
# ════════════════════════════════════════════════════════

class TestBuildOutlineMarkdown:
    def test_dict_items(self):
        outline = [
            {"title": "第一章", "start_timestamp": "00:00:00"},
            {"title": "第二章", "timestamp": "00:05:30"},
        ]
        result = build_outline_markdown(outline)
        assert "- **第一章** `00:00:00`" in result
        assert "- **第二章** `00:05:30`" in result

    def test_string_items(self):
        outline = ["第一节", "第二节"]
        result = build_outline_markdown(outline)
        assert "- 第一节" in result
        assert "- 第二节" in result

    def test_mixed_items(self):
        outline = [
            {"title": "概述", "text": ""},
            "自由文本",
        ]
        result = build_outline_markdown(outline)
        assert "- **概述**" in result
        assert "- 自由文本" in result

    def test_no_timestamp(self):
        outline = [{"title": "无时间戳章节"}]
        result = build_outline_markdown(outline)
        assert "`" not in result  # 未提供时间戳时不显示


# ════════════════════════════════════════════════════════
# 10. build_mindmap_markdown — 思维导图渲染(list格式)
# ════════════════════════════════════════════════════════

class TestBuildMindmapMarkdown:
    def test_list_format(self):
        data = [
            {"name": "根节点", "children": [
                {"name": "子节点1"},
                {"name": "子节点2"},
            ]},
            "独立节点",
        ]
        result = build_mindmap_markdown(data)
        assert "- **根节点**" in result
        assert "  - 子节点1" in result
        assert "  - 子节点2" in result
        assert "- 独立节点" in result

    def test_string_children(self):
        data = [{"name": "主题", "children": ["要点1", "要点2"]}]
        result = build_mindmap_markdown(data)
        assert "  - 要点1" in result

    def test_title_fallback(self):
        data = [{"title": "用title字段的节点", "children": []}]
        result = build_mindmap_markdown(data)
        assert "- **用title字段的节点**" in result


# ════════════════════════════════════════════════════════
# 11. build_mindmap_from_tree — 思维导图渲染(树格式)
# ════════════════════════════════════════════════════════

class TestBuildMindmapFromTree:
    def test_single_node(self):
        node = {"title": "根", "children": []}
        result = build_mindmap_from_tree(node)
        assert result == "- **根**"

    def test_nested_tree(self):
        node = {
            "title": "根",
            "children": [
                {"title": "A", "children": [
                    {"title": "A-1", "children": []},
                ]},
                {"title": "B", "children": []},
            ],
        }
        result = build_mindmap_from_tree(node)
        lines = result.split("\n")
        assert lines[0] == "- **根**"
        assert "  - **A**" in lines
        assert "    - **A-1**" in lines
        assert "  - **B**" in lines

    def test_string_children(self):
        node = {"title": "主题", "children": ["自由文本"]}
        result = build_mindmap_from_tree(node)
        assert "  - 自由文本" in result

    def test_name_fallback(self):
        node = {"name": "用name字段", "children": []}
        result = build_mindmap_from_tree(node)
        assert result == "- **用name字段**"


# ════════════════════════════════════════════════════════
# 12. build_comprehensive_markdown — 完整笔记组装
# ════════════════════════════════════════════════════════

class TestBuildComprehensiveMarkdown:
    BASE_URL = "https://www.bilibili.com/video/BV123"

    def test_minimal_detail(self):
        """只提供最基本数据时的渲染"""
        detail = {
            "transcriptWithTimestamp": "[00:00:00] 测试内容",
        }
        result = build_comprehensive_markdown(detail, "测试标题", self.BASE_URL)
        assert "测试标题" in result
        assert "逐字稿" in result
        assert "[00:00:00]" in result

    def test_full_detail(self):
        """所有字段都提供的完整渲染"""
        detail = {
            "transcriptWithTimestamp": "[00:00:00] 全文内容",
            "polishedTranscript": "AI润色后的文字",
            "aiOutline": [{"title": "大纲标题", "start_timestamp": "00:00:00"}],
            "ai_logic_insight": {"key_insight": "核心洞察", "pros": "优点", "cons": "缺点", "summary": "总结"},
            "qaPairs": [{"question": "Q1", "answer": "A1", "start_timestamp": "00:01:00"}],
        }
        result = build_comprehensive_markdown(detail, "完整标题", self.BASE_URL)
        assert "# 📝 完整标题" in result
        assert "逐字稿" in result
        assert "AI 润色" in result
        assert "AI 智能大纲" in result
        assert "逻辑洞察" in result
        assert "核心 QA 对" in result
        assert "核心洞察" in result
        assert "**Q1" in result

    def test_logic_insight_string(self):
        """logic_insight 为字符串格式"""
        detail = {
            "ai_logic_insight": "这是一条逻辑洞察",
        }
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "逻辑洞察" in result
        assert "这是一条逻辑洞察" in result

    def test_logic_insight_verdict_fallback(self):
        """兼容 verdict 字段"""
        detail = {"verdict": "判决内容"}
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "逻辑洞察" in result
        assert "判决内容" in result

    def test_qa_without_timestamp(self):
        detail = {
            "qaPairs": [{"question": "问题", "answer": "答案"}],
        }
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "**Q1：问题**" in result
        assert "A1：答案" in result

    def test_qa_with_timestamp(self):
        detail = {
            "qaPairs": [{"question": "问题", "answer": "答案", "start_timestamp": "00:02:30"}],
        }
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "t=150" in result  # 2:30 = 150秒

    def test_fallback_to_original_when_no_transcript(self):
        """没有 transcriptWithTimestamp/polished 时回退到原始文本"""
        detail = {"originalTranscript": "原始文本"}
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "视频文稿" in result
        assert "原始文本" in result

    def test_front_matter(self):
        detail = {}
        result = build_comprehensive_markdown(detail, "标题", self.BASE_URL)
        assert "---" in result
        assert "title: 标题" in result
        assert "diting.cc" in result

    def test_empty_detail(self):
        """空的 detail 仍生成 header"""
        detail = {}
        result = build_comprehensive_markdown(detail, "空稿", self.BASE_URL)
        assert "# 📝 空稿" in result


# ════════════════════════════════════════════════════════
# 13. extract_text — 文本提取（向后兼容）
# ════════════════════════════════════════════════════════

class TestExtractText:
    def test_original_transcript(self):
        data = {"originalTranscript": "原始文本"}
        assert extract_text(data) == "原始文本"

    def test_polished_preferred_over_original(self):
        data = {"originalTranscript": "原始", "polishedTranscript": "润色"}
        # originalTranscript 排第一位，先返回
        assert extract_text(data) == "原始"

    def test_no_transcript_fields(self):
        data = {"other": "data"}
        assert extract_text(data) is None

    def test_empty_dict(self):
        assert extract_text({}) is None


# ════════════════════════════════════════════════════════
# 14. BATCH_ALL 解析逻辑
# ════════════════════════════════════════════════════════

class TestBatchAllParsing:
    """测试 _parse_batch_all 函数"""

    def test_yes(self):
        assert _parse_batch_all("BATCH_ALL=是") is True

    def test_no(self):
        assert _parse_batch_all("BATCH_ALL=否") is False

    def test_not_present(self):
        assert _parse_batch_all("没有 BATCH_ALL") is False

    def test_colon_separator(self):
        assert _parse_batch_all("BATCH_ALL：是") is True

    def test_colon_english(self):
        assert _parse_batch_all("BATCH_ALL:是") is True

    def test_multiline_body(self):
        body = """
        链接：https://bilibili.com/video/BV123
        BATCH_ALL=是
        备注：none
        """
        assert _parse_batch_all(body) is True


# ════════════════════════════════════════════════════════
# 15. MANUAL_CATEGORY 解析逻辑
# ════════════════════════════════════════════════════════

class TestManualCategoryParsing:
    """测试 _parse_manual_category 函数"""

    def test_set_category(self):
        assert _parse_manual_category("CATEGORY=03_🎨设计创意与剪辑") == "03_🎨设计创意与剪辑"

    def test_colon_separator(self):
        assert _parse_manual_category("CATEGORY：05_📱自媒体与内容创作") == "05_📱自媒体与内容创作"

    def test_custom_category(self):
        assert _parse_manual_category("CATEGORY=06_📚人文社科") == "06_📚人文社科"

    def test_not_present(self):
        assert _parse_manual_category("没有 CATEGORY") == ""

    def test_multiline_extraction(self):
        body = """
        BATCH_ALL=否
        CATEGORY=04_📈商业财经与搞钱
        """
        assert _parse_manual_category(body) == "04_📈商业财经与搞钱"

    def test_empty_value_no_newline_capture(self):
        """CATEGORY= 后为空时不应跨行捕获代码围栏"""
        assert _parse_manual_category("\n```\nCATEGORY=\n```\n") == ""

    def test_trailing_spaces(self):
        assert _parse_manual_category("CATEGORY=  01_🔥考研考编必刷  ") == "01_🔥考研考编必刷"

    def test_tabs(self):
        assert _parse_manual_category("CATEGORY\t=\t02_🤖AI前沿与高薪技术") == "02_🤖AI前沿与高薪技术"


# ════════════════════════════════════════════════════════
# 16. 集成场景测试
# ════════════════════════════════════════════════════════

class TestIntegrationScenarios:
    """模拟完整 Issue 场景"""

    def test_single_p_video_issue(self):
        """单P视频 Issue → 提取链接 + 归类"""
        body = """
        https://www.bilibili.com/video/BV1xx00000000
        考研数学张宇全程班
        """
        url = extract_bilibili_url(body)
        assert url is not None
        category = classify_category(body, "")
        assert "考研" in category

    def test_multi_p_batch_all_yes_issue(self):
        """多P合集批量 Issue"""
        body = """
        https://www.bilibili.com/video/BV123?p=1
        BATCH_ALL=是
        CATEGORY=02_🤖AI前沿与高薪技术
        """
        assert _parse_batch_all(body) is True
        assert _parse_manual_category(body) == "02_🤖AI前沿与高薪技术"

    def test_default_no_batch_issue(self):
        """默认不批量 Issue"""
        body = """
        https://www.bilibili.com/video/BV456?p=3
        为什么想要这份笔记
        """
        assert _parse_batch_all(body) is False

    def test_url_with_p_param_page_extraction(self):
        """URL 中 p= 参数提取"""
        url = "https://www.bilibili.com/video/BV123?spm=1&p=5&vd=abc"
        assert extract_page_number(url) == 5

    def test_filename_generation(self):
        """完整流程：标题 → 文件名"""
        title = "【吴恩达】2026年公认最好的【Agent智能体】教程！Agentic AI"
        safe = sanitize_filename(title)
        assert '"' not in safe
        assert "Agent智能体" in safe
        assert len(safe) <= 80


if __name__ == "__main__":
    pytest.main([__file__, "-v"])