"""
사이버범죄 국제공조 위키 — Wikipedia-style Web Interface
"""
import html as html_lib
import os
import re
import site
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict

vendor_site = Path(__file__).resolve().parent.parent / ".vendor"
if vendor_site.is_dir():
    sys.path.insert(0, str(vendor_site))

user_site = site.getusersitepackages()
if user_site and user_site not in sys.path:
    sys.path.append(user_site)

import frontmatter
import markdown
from flask import Flask, render_template, request, abort, redirect, url_for
from markupsafe import Markup

app = Flask(__name__)

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"

# Category metadata (Korean labels)
CATEGORIES = {
    "legal-frameworks": {"label": "법적 프레임워크", "label_en": "Legal Frameworks", "icon": "📜"},
    "organizations": {"label": "기관", "label_en": "Organizations", "icon": "🏛️"},
    "countries": {"label": "국가", "label_en": "Countries", "icon": "🌍"},
    "operations": {"label": "작전", "label_en": "Operations", "icon": "🎯"},
    "cases": {"label": "사건", "label_en": "Cases", "icon": "⚖️"},
    "mechanisms": {"label": "공조 메커니즘", "label_en": "Mechanisms", "icon": "🔗"},
    "procedures": {"label": "절차", "label_en": "Procedures", "icon": "📋"},
    "crime-types": {"label": "범죄유형", "label_en": "Crime Types", "icon": "🔒"},
    "challenges": {"label": "과제", "label_en": "Challenges", "icon": "⚠️"},
    "concepts": {"label": "법적 개념", "label_en": "Concepts", "icon": "📖"},
    "sources": {"label": "출처", "label_en": "Sources", "icon": "📰"},
    "analysis": {"label": "분석", "label_en": "Analysis", "icon": "📊"},
    "timelines": {"label": "타임라인", "label_en": "Timelines", "icon": "📅"},
}

# Section heading translations (EN -> KO)
HEADING_MAP = {
    # Common
    "Summary": "개요",
    "Background": "배경",
    "References": "참고문헌",
    "Contradictions & Open Questions": "모순점 및 미해결 문제",
    "Contradictions &amp; Open Questions": "모순점 및 미해결 문제",
    # Operations
    "Participating Parties": "참여 기관",
    "Legal Framework": "법적 근거",
    "Operational Timeline": "작전 타임라인",
    "Results": "결과",
    "Results and Impact": "결과 및 영향",
    "Cooperation Mechanisms Used": "활용된 공조 메커니즘",
    "Challenges and Friction Points": "과제 및 마찰 요인",
    "Lessons Learned": "교훈",
    "Follow-Up Actions": "후속 조치",
    "Korean Involvement": "한국의 참여",
    "Korean Perspective": "한국 관점",
    # Organizations
    "Mandate and Authority": "임무와 권한",
    "Structure Relevant to Cybercrime IC": "사이버범죄 국제공조 관련 구조",
    "IC Capabilities": "국제공조 역량",
    "Key Operations and Cases": "주요 작전 및 사건",
    "Cooperation Track Record": "공조 실적",
    "Capacity Building": "역량 구축",
    "Korean Interactions": "한국과의 협력",
    # Legal frameworks
    "Historical Context": "역사적 배경",
    "Key Provisions for IC": "국제공조 관련 주요 조항",
    "Parties and Participation": "당사국 및 참여",
    "Implementation in Practice": "실무 적용",
    "Relationship to Other Frameworks": "다른 프레임워크와의 관계",
    "Criticisms and Debates": "비판 및 논쟁",
    # Countries
    "Legal Framework for Cybercrime": "사이버범죄 법적 체계",
    "Substantive Law": "실체법",
    "Procedural Powers": "절차적 권한",
    "MLA": "국제사법공조",
    "Treaty Memberships": "조약 가입",
    "Key Agencies": "주요 기관",
    "Capacity Assessment": "역량 평가",
    "Notable Operations and Cases": "주요 작전 및 사건",
    "Political and Diplomatic Context": "정치·외교적 맥락",
    "Challenges": "과제",
    # Concepts
    "Definition": "정의",
    "Legal Basis": "법적 근거",
    "Relevance to IC on Cybercrime": "사이버범죄 국제공조와의 관련성",
    "How It Works in Practice": "실무 적용",
    "Variations Across Jurisdictions": "관할권별 차이",
    "Common Law": "보통법",
    "Civil Law": "대륙법",
    "Key Case Law": "주요 판례",
    "Debates and Controversies": "논쟁 및 논란",
    "Korean Law": "한국법",
    "Multi-Language Terminology": "다국어 용어",
    # Mechanisms
    "How It Works": "작동 방식",
    "Scope and Capabilities": "범위 및 역량",
    "Practical Usage": "실무 활용",
    "Advantages": "장점",
    "Limitations": "한계",
    "Notable Uses": "주요 활용 사례",
    "Comparison with Alternatives": "대안과의 비교",
    "Korean Usage": "한국의 활용",
    # Procedures
    "Prerequisites": "전제조건",
    "Step-by-Step Process": "단계별 절차",
    "Required Documents": "필요 서류",
    "Timelines": "소요 기간",
    "Practical Tips": "실무 팁",
    "Country-Specific Variations": "국가별 차이",
    "Common Pitfalls": "일반적 함정",
    "Related Procedures": "관련 절차",
    "Korean Practice": "한국 실무",
    # Crime types
    "Criminalization Landscape": "범죄화 현황",
    "Typical IC Scenarios": "일반적 국제공조 시나리오",
    "Evidence Types and Locations": "증거 유형 및 소재",
    "Cooperation Pathways": "공조 경로",
    "Key Operations and Precedents": "주요 작전 및 선례",
    "Statistics and Trends": "통계 및 동향",
    "Prevention and Disruption": "예방 및 차단",
    "Korean Context": "한국 상황",
    # Overview
    "Executive Summary": "요약",
    "Top 10 Operations by Significance": "주요 작전 Top 10",
    "Recent Treaty Developments": "최근 조약 동향",
    "Emerging Challenges": "새로운 과제",
    "Cooperation Statistics": "공조 통계",
    "Recent Activity": "최근 활동",
    # Challenges
    "Nature of the Problem": "문제의 본질",
    "Impact on Cooperation": "공조에 미치는 영향",
    "Root Causes": "근본 원인",
    "Proposed Solutions": "제안된 해결책",
    "Current State of Debate": "현재 논의 현황",
    "Case Studies": "사례 연구",
    "Comparative Perspectives": "비교 관점",
    # Source
    "Key Findings": "주요 발견사항",
    "Pages Updated": "갱신된 페이지",
    "Source Assessment": "출처 평가",
}

TYPE_LABELS_KO = {
    "legal-framework": "법적 프레임워크",
    "organization": "기관",
    "country": "국가",
    "operation": "작전",
    "case": "사건",
    "mechanism": "공조 메커니즘",
    "procedure": "절차",
    "crime-type": "범죄유형",
    "challenge": "과제",
    "concept": "법적 개념",
    "source": "출처",
    "analysis": "분석",
    "timeline": "타임라인",
    "overview": "개요",
    "category-index": "카테고리 색인",
}


def resolve_wiki_path(slug):
    """Resolve a wikilink slug to an actual file path."""
    # Direct match in any subdirectory
    for subdir in WIKI_DIR.iterdir():
        if subdir.is_dir():
            candidate = subdir / f"{slug}.md"
            if candidate.exists():
                return candidate
    # Top-level match
    candidate = WIKI_DIR / f"{slug}.md"
    if candidate.exists():
        return candidate
    return None


def get_category_for_file(filepath):
    """Determine the category from a file's parent directory."""
    parent = filepath.parent.name
    if parent == "wiki":
        return None
    return parent


def parse_page(filepath):
    """Parse a markdown file with YAML frontmatter."""
    post = frontmatter.load(filepath)
    return post.metadata, post.content


def convert_wikilinks(text):
    """Convert [[wikilinks]] and [[slug|display]] to HTML links."""
    def replace_link(match):
        inner = match.group(1)
        # Handle escaped pipes in Markdown tables: [[slug\|display]] → [[slug|display]]
        inner = inner.replace("\\|", "|")
        if "|" in inner:
            slug, display = inner.split("|", 1)
        else:
            slug = inner
            display = inner
        slug = slug.strip()
        display = display.strip()
        # Handle _index links → redirect to category page
        if "/_index" in slug or slug.endswith("_index"):
            cat = slug.replace("/_index", "").replace("_index", "").strip("/")
            if cat in CATEGORIES:
                return f'<a href="/category/{cat}" class="wikilink">{display}</a>'
        # Handle category/slug format (e.g., operations/operation-cronos)
        if "/" in slug:
            parts = slug.split("/", 1)
            cat_part, slug_part = parts[0], parts[1]
            resolved = WIKI_DIR / cat_part / f"{slug_part}.md"
            if resolved.exists():
                return f'<a href="/wiki/{cat_part}/{slug_part}" class="wikilink">{display}</a>'
        resolved = resolve_wiki_path(slug)
        if resolved:
            cat = get_category_for_file(resolved)
            if cat:
                href = f"/wiki/{cat}/{slug}"
            else:
                href = f"/wiki/{slug}"
            return f'<a href="{href}" class="wikilink">{display}</a>'
        return f'<a href="/wiki/_missing/{slug}" class="wikilink wikilink-missing">{display}</a>'
    return re.sub(r'\[\[([^\]]+)\]\]', replace_link, text)


def convert_callouts(html):
    """Convert Obsidian callouts to styled HTML."""
    callout_pattern = re.compile(
        r'<blockquote>\s*<p>\[!(info|warning|caution|note)\]\s*(.*?)</p>(.*?)</blockquote>',
        re.DOTALL
    )
    callout_icons = {
        "info": "ℹ️", "warning": "⚠️",
        "caution": "🔶", "note": "📝"
    }
    def replace_callout(match):
        ctype = match.group(1)
        title = match.group(2).strip() or ctype.title()
        body = match.group(3).strip()
        icon = callout_icons.get(ctype, "ℹ️")
        return (
            f'<div class="callout callout-{ctype}">'
            f'<div class="callout-title">{icon} {title}</div>'
            f'<div class="callout-body">{body}</div></div>'
        )
    return callout_pattern.sub(replace_callout, html)


def open_external_links_in_new_tab(html: str) -> str:
    """Normalize external links with new-tab behavior and full-URL tooltips."""

    def replace(match):
        attrs_before = match.group(1) or ""
        url = match.group(2)
        attrs_after = match.group(3) or ""
        attrs = f"{attrs_before}href=\"{url}\"{attrs_after}"

        if "target=" not in attrs:
            attrs += ' target="_blank"'
        if "rel=" not in attrs:
            attrs += ' rel="noopener noreferrer"'
        if "title=" not in attrs:
            attrs += f' title="{html_lib.escape(url, quote=True)}"'
        if "data-full-url=" not in attrs:
            attrs += f' data-full-url="{html_lib.escape(url, quote=True)}"'

        class_match = re.search(r'class="([^"]*)"', attrs)
        if class_match:
            classes = class_match.group(1).split()
            if "external-link" not in classes:
                classes.append("external-link")
                attrs = re.sub(
                    r'class="[^"]*"',
                    f'class="{" ".join(classes)}"',
                    attrs,
                    count=1,
                )
        else:
            attrs += ' class="external-link"'

        return f"<a {attrs.strip()}>"

    html = re.sub(
        r"<a\s+([^>]*?)href=\"(https?://[^\"]+)\"([^>]*)>",
        replace,
        html,
    )
    return re.sub(
        r'(<a\b[^>]*class="[^"]*\bexternal-link\b[^"]*"[^>]*>)(https?://[^<]+)(</a>)',
        r"\1Link\3",
        html,
    )


def style_reference_tables(html: str) -> str:
    """Mark reference tables so CSS can size columns predictably."""

    def replace(match):
        table_html = match.group(0)
        if not all(token in table_html for token in ("<th>#</th>", "<th>URL</th>")):
            return table_html
        if not ("<th>Source</th>" in table_html or "<th>Title</th>" in table_html):
            return table_html
        if 'class="' in table_html.split(">", 1)[0]:
            table_html = re.sub(
                r'<table([^>]*?)class="([^"]*)"',
                lambda m: f'<table{m.group(1)}class="{m.group(2)} reference-table"',
                table_html,
                count=1,
            )
        else:
            table_html = table_html.replace("<table>", '<table class="reference-table">', 1)
        colgroup = (
            "<colgroup>"
            '<col class="col-ref-num">'
            '<col class="col-ref-source">'
            '<col class="col-ref-publisher">'
            '<col class="col-ref-date">'
            '<col class="col-ref-url">'
            "</colgroup>"
        )
        return table_html.replace(">", f">{colgroup}", 1)

    return re.sub(r"<table>.*?</table>", replace, html, flags=re.S)


def bilingual_headings(html: str) -> str:
    """Replace section headings with bilingual KO/EN spans."""
    def replace_heading(match):
        tag = match.group(1)       # h2 or h3
        attrs = match.group(2)     # any attributes
        text = match.group(3)      # heading text (may contain HTML)
        close_tag = match.group(4)
        # Strip HTML tags for lookup
        plain = re.sub(r'<[^>]+>', '', text).strip()
        ko = HEADING_MAP.get(plain)
        if ko:
            return (
                f'<{tag}{attrs}>'
                f'<span class="heading-ko">{ko}</span>'
                f'<span class="heading-en">{text}</span>'
                f'</{close_tag}>'
            )
        # Check if it's already Korean (한국 in text) — keep as-is
        return match.group(0)

    return re.sub(
        r'<(h[23])([^>]*)>(.*?)</(h[23])>',
        replace_heading,
        html,
    )


def render_markdown(text):
    """Render markdown to HTML with wikilinks, callouts, and bilingual headings."""
    text = convert_wikilinks(text)
    text = linkify_bare_urls_in_markdown(text)
    html = markdown.markdown(
        text,
        extensions=[
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code",
            "markdown.extensions.toc",
            "markdown.extensions.attr_list",
        ],
        extension_configs={"toc": {"toc_depth": "2-3"}}
    )
    html = convert_callouts(html)
    html = open_external_links_in_new_tab(html)
    html = style_reference_tables(html)
    html = bilingual_headings(html)
    return Markup(html)


def render_infobox_value(text):
    """Render simple inline content for infobox cells."""
    if text is None:
        return Markup("")
    html = str(text)
    html = convert_wikilinks(html)
    html = linkify_bare_urls_in_markdown(html)
    html = open_external_links_in_new_tab(html)
    return Markup(html)


def linkify_bare_urls_in_markdown(text):
    """Turn bare URLs into Markdown links so rendering is consistent."""
    pattern = re.compile(r'(?P<prefix>(^|[\s|>]))(?P<url>https?://[^\s<|]+)', re.M)

    def replace(match):
        prefix = match.group("prefix")
        url = match.group("url")
        trailing = ""
        while url and url[-1] in ".,;:":
            trailing = url[-1] + trailing
            url = url[:-1]
        return f"{prefix}[Link]({url}){trailing}"

    return pattern.sub(replace, text)


def get_all_pages():
    """Get metadata for all wiki pages."""
    pages = []
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue
        try:
            meta, _ = parse_page(md_file)
        except Exception:
            meta = {}
        slug = md_file.stem
        cat = get_category_for_file(md_file)
        pages.append({
            "slug": slug,
            "category": cat,
            "title": meta.get("title", slug.replace("-", " ").title()),
            "type": meta.get("type", ""),
            "meta": meta,
        })
    return pages


TYPE_LABELS_EN = {
    "legal-framework": "Legal Framework",
    "organization": "Organization",
    "country": "Country",
    "operation": "Operation",
    "case": "Case",
    "mechanism": "Mechanism",
    "procedure": "Procedure",
    "crime-type": "Crime Type",
    "challenge": "Challenge",
    "concept": "Concept",
    "source": "Source",
    "analysis": "Analysis",
    "timeline": "Timeline",
    "overview": "Overview",
    "category-index": "Category Index",
}


def build_infobox(meta, page_type):
    """Build infobox data from frontmatter with bilingual labels."""
    infobox = []
    type_label_ko = TYPE_LABELS_KO.get(page_type, page_type)
    type_label_en = TYPE_LABELS_EN.get(page_type, page_type)
    infobox.append(("유형", "Type", type_label_ko, type_label_en))

    # (field, ko_label, en_label)
    field_map = {
        "operation": [
            ("status", "상태", "Status"),
            ("operation_type", "작전유형", "Op Type"),
            ("timeframe", "기간", "Period"),
            ("lead_agency", "주도기관", "Lead Agency"),
            ("crime_type", "범죄유형", "Crime Type"),
        ],
        "organization": [
            ("org_type", "기관유형", "Org Type"),
            ("headquarters", "본부", "HQ"),
            ("established", "설립", "Est."),
            ("member_states", "회원국", "Members"),
        ],
        "country": [
            ("iso_code", "ISO 코드", "ISO Code"),
            ("legal_system", "법체계", "Legal System"),
            ("region", "지역", "Region"),
        ],
        "legal-framework": [
            ("framework_type", "유형", "Type"),
            ("status", "상태", "Status"),
            ("adopted_date", "채택일", "Adopted"),
            ("entry_into_force", "발효일", "In Force"),
        ],
        "mechanism": [
            ("mechanism_type", "유형", "Type"),
            ("formality", "형식성", "Formality"),
            ("speed", "속도", "Speed"),
        ],
        "concept": [
            ("title_ko", "한국어", "Korean"),
            ("concept_category", "분류", "Category"),
            ("domain", "분야", "Domain"),
        ],
        "source": [
            ("source_type", "출처유형", "Source Type"),
            ("publisher", "발행처", "Publisher"),
            ("publish_date", "발행일", "Pub Date"),
            ("reliability", "신뢰도", "Reliability"),
            ("credibility", "신빙성", "Credibility"),
        ],
        "crime-type": [
            ("crime_category", "분류", "Category"),
        ],
    }

    for entry in field_map.get(page_type, []):
        field, label_ko, label_en = entry
        val = meta.get(field)
        if val and val not in ("", 0, [], {}):
            if isinstance(val, dict):
                parts = [f"{k}: {v}" for k, v in val.items() if v]
                val = ", ".join(parts[:3])
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val[:5])
            infobox.append((label_ko, label_en, str(val), str(val)))

    # Metrics (for operations)
    metrics = meta.get("metrics") or meta.get("results")
    if isinstance(metrics, dict):
        metric_labels = {
            "arrests": ("체포", "Arrests"),
            "servers_seized": ("서버 압수", "Servers Seized"),
            "domains_seized": ("도메인 압수", "Domains Seized"),
            "cryptocurrency_seized": ("암호화폐 압수", "Crypto Seized"),
            "participating_countries": ("참여국", "Countries"),
            "participating_agencies": ("참여기관", "Agencies"),
            "financial_seized": ("금융 압수", "Financial Seized"),
        }
        for key, (label_ko, label_en) in metric_labels.items():
            v = metrics.get(key)
            if v and v not in (0, "", "0"):
                infobox.append((label_ko, label_en, str(v), str(v)))

    # Parties (for legal frameworks)
    parties = meta.get("parties")
    if isinstance(parties, dict):
        sp = parties.get("states_parties")
        if sp:
            infobox.append(("당사국", "Parties", str(sp), str(sp)))

    # IC capacity (for countries)
    ic = meta.get("ic_capacity")
    if isinstance(ic, dict):
        rating = ic.get("rating")
        if rating:
            infobox.append(("공조 역량", "IC Capacity", rating, rating))

    # Source count
    sc = meta.get("source_count")
    if sc:
        infobox.append(("출처 수", "Sources", str(sc), str(sc)))

    rendered_infobox = []
    for label_ko, label_en, val_ko, val_en in infobox:
        rendered_infobox.append(
            (
                label_ko,
                label_en,
                render_infobox_value(val_ko),
                render_infobox_value(val_en),
            )
        )
    return rendered_infobox


# --- Korean Content Generator ---

# Common term translations for body text
TERM_KO = {
    "completed": "완료", "ongoing": "진행중", "success": "성공",
    "partial": "부분 성공", "failure": "실패", "unknown": "미상",
    "takedown": "테이크다운", "joint-investigation": "합동수사",
    "arrest-sweep": "일제검거", "infrastructure-seizure": "인프라 압수",
    "arrest": "체포", "seizure": "압수", "indictment": "기소",
    "extradition": "인도", "asset_freeze": "자산동결",
    "high": "높음", "medium": "보통", "low": "낮음",
    "formal-mlat": "공식 MLAT", "informal-police-cooperation": "비공식 경찰 협력",
    "convention": "협약", "protocol": "의정서", "bilateral-treaty": "양자조약",
    "in-force": "발효중", "not-yet-in-force": "미발효",
    "common-law": "보통법", "civil-law": "대륙법", "mixed": "혼합",
    "international-org": "국제기구", "regional-org": "지역기구",
    "national-agency": "국가기관", "national-unit": "국가부서",
    "cyber-dependent": "사이버 의존형", "cyber-enabled": "사이버 활용형",
    "content-related": "콘텐츠 관련",
    "legal": "법적", "technical": "기술적", "political": "정치적",
    "institutional": "제도적", "capacity": "역량",
    "critical": "심각", "confirmed": "확인됨",
    "probably-true": "유력", "possibly-true": "가능성 있음",
    "public": "공개", "restricted": "제한", "confidential": "비공개",
}


def _t(val: str) -> str:
    """Translate a known term, or return original."""
    if not val:
        return ""
    clean = str(val).strip("[]\"' ")
    return TERM_KO.get(clean, clean)


def _strip_wikilink(val) -> str:
    """Extract display name from wikilink or plain string."""
    s = str(val).strip("[]\"' ")
    if "|" in s:
        return s.split("|", 1)[1]
    return s.replace("-", " ").replace("_", " ").title() if s.islower() else s


def _extract_slug(val) -> str:
    """Extract slug from wikilink or plain string. [[slug|display]] → slug."""
    s = str(val).strip("[]\"' ")
    if "|" in s:
        return s.split("|", 1)[0]
    return s


def _format_list(items, limit=10) -> str:
    """Format a list of items for Korean display."""
    if not isinstance(items, list):
        return str(items)
    names = [_strip_wikilink(i) for i in items[:limit]]
    result = ", ".join(names)
    if len(items) > limit:
        result += f" 외 {len(items) - limit}개"
    return result


def generate_ko_content(meta: dict, en_content: str, page_type: str) -> str:
    """Generate Korean markdown content from frontmatter metadata."""
    generators = {
        "operation": _gen_ko_operation,
        "source": _gen_ko_source,
        "organization": _gen_ko_organization,
        "country": _gen_ko_country,
        "legal-framework": _gen_ko_legal_framework,
        "mechanism": _gen_ko_mechanism,
        "crime-type": _gen_ko_crime_type,
        "concept": _gen_ko_concept,
        "challenge": _gen_ko_challenge,
        "procedure": _gen_ko_procedure,
        "analysis": _gen_ko_analysis,
    }
    gen = generators.get(page_type)
    if gen:
        return gen(meta, en_content)
    return ""


def _gen_ko_operation(meta: dict, en: str) -> str:
    """Generate Korean content for operation pages."""
    title = meta.get("title_ko") or meta.get("title", "")
    status = _t(meta.get("status", ""))
    op_type = _t(meta.get("operation_type", ""))
    outcome = _t(meta.get("outcome", ""))

    tf = meta.get("timeframe", {})
    announced = tf.get("announced", "") if isinstance(tf, dict) else ""
    start = tf.get("start", "") if isinstance(tf, dict) else ""
    end = tf.get("end", "") if isinstance(tf, dict) else ""
    period_str = f"{start} ~ {end}" if start and end else str(announced)

    coord = _strip_wikilink(meta.get("coordinating_body", ""))
    lead = _strip_wikilink(meta.get("lead_agency", ""))
    crime = _strip_wikilink(meta.get("crime_type", ""))
    target = meta.get("target_entity", "")

    countries = meta.get("participating_countries", [])
    agencies = meta.get("participating_agencies", [])
    countries_str = _format_list(countries)
    agencies_str = _format_list(agencies)
    num_countries = len(countries) if isinstance(countries, list) else 0

    results = meta.get("results", {})
    if not isinstance(results, dict):
        results = {}
    arrests = results.get("arrests", 0)
    servers = results.get("servers_seized", 0)
    domains = results.get("domains_seized", 0)
    crypto = results.get("cryptocurrency_seized", "")
    other = results.get("other", [])

    ci = meta.get("credibility_index", "")
    src_count = meta.get("source_count", 0)

    lines = []
    lines.append("## 개요\n")

    # Build summary
    summary_parts = [f"**{title}**"]
    if coord:
        coord_slug = _extract_slug(meta.get("coordinating_body", ""))
        summary_parts.append(f"[[{coord_slug}|{coord}]]의 조정 하에 수행된")
    summary_parts.append(f"{op_type} 작전으로,")
    if period_str:
        summary_parts.append(f"**{period_str}** 기간 동안")
    if num_countries:
        summary_parts.append(f"**{num_countries}개국**이 참여하였다.")
    else:
        summary_parts.append("국제 공조로 진행되었다.")

    lines.append(" ".join(summary_parts))

    if target:
        lines.append(f"\n대상: {target}\n")

    # Results section
    result_items = []
    if arrests:
        result_items.append(f"**{arrests:,}명** 체포")
    if servers:
        result_items.append(f"**{servers:,}대** 서버 압수")
    if domains:
        result_items.append(f"**{domains:,}개** 도메인 압수/차단")
    if crypto:
        result_items.append(f"**{crypto}** 암호화폐 압수")

    if result_items:
        lines.append("\n## 결과\n")
        for item in result_items:
            lines.append(f"- {item}")
        if isinstance(other, list):
            for o in other:
                lines.append(f"- {o}")

    # Participants
    lines.append("\n## 참여 기관\n")
    if lead:
        lines.append(f"**주도기관:** {lead}")
    if coord and coord != lead:
        lines.append(f"\n**조정기관:** {coord}")
    if agencies_str:
        lines.append(f"\n**참여기관:** {agencies_str}")
    if countries_str:
        lines.append(f"\n**참여국:** {countries_str}")

    # Lessons learned
    lessons = meta.get("lessons_learned", [])
    if isinstance(lessons, list) and lessons:
        lines.append("\n## 교훈\n")
        for lesson in lessons:
            lines.append(f"- {lesson}")

    # Related operations
    related = meta.get("related_operations", [])
    if isinstance(related, list) and related:
        lines.append("\n## 관련 작전\n")
        for r in related:
            lines.append(f"- {r}")

    # Credibility
    if ci:
        lines.append(f"\n> 신뢰도 지수(CI): **{ci}** | 출처: {src_count}건")

    # Extract references table from English content (keep as-is)
    ref_match = re.search(r'(## References\n.*)', en, re.DOTALL)
    if ref_match:
        lines.append("\n## 참고문헌\n")
        ref_table = ref_match.group(1).replace("## References\n", "").strip()
        lines.append(ref_table)

    return "\n".join(lines)


def _gen_ko_source(meta: dict, en: str) -> str:
    """Generate Korean content for source pages."""
    title = meta.get("title", "")
    pub = meta.get("publisher", "")
    pub_date = meta.get("publish_date", "")
    src_type = _t(meta.get("source_type", ""))
    reliability = _t(meta.get("reliability", ""))
    credibility = _t(meta.get("credibility", ""))
    lang = meta.get("language", "en")
    raw_path = meta.get("raw_path", "")

    findings = meta.get("key_findings", [])
    pages = meta.get("pages_updated", [])

    lines = []
    lines.append("## 출처 정보\n")
    lines.append(f"| 항목 | 내용 |")
    lines.append(f"|------|------|")
    lines.append(f"| 제목 | {title} |")
    lines.append(f"| 발행처 | {pub} |")
    lines.append(f"| 발행일 | {pub_date} |")
    lines.append(f"| 출처유형 | {src_type} |")
    lines.append(f"| 신뢰도 | {reliability} |")
    lines.append(f"| 신빙성 | {credibility} |")
    lines.append(f"| 언어 | {lang} |")
    if raw_path:
        lines.append(f"| 원본 경로 | `{raw_path}` |")

    if isinstance(findings, list) and findings:
        lines.append("\n## 주요 발견사항\n")
        for f in findings:
            lines.append(f"- {f}")

    if isinstance(pages, list) and pages:
        lines.append("\n## 갱신된 페이지\n")
        for p in pages:
            lines.append(f"- {p}")

    return "\n".join(lines)


def _gen_ko_organization(meta: dict, en: str) -> str:
    """Generate Korean content for organization pages."""
    title = meta.get("title", "")
    title_ko = meta.get("official_name_ko", "")
    org_type = _t(meta.get("org_type", ""))
    hq = meta.get("headquarters", "")
    est = meta.get("established", "")
    mandate = meta.get("mandate", "")
    members = meta.get("member_states", "")
    parent = _strip_wikilink(meta.get("parent_org", ""))
    country = _strip_wikilink(meta.get("country", ""))
    key_roles = meta.get("key_roles", [])
    partners = meta.get("cooperation_partners", [])
    ops = meta.get("operations_participated", [])

    lines = []
    lines.append("## 개요\n")
    desc = f"**{title}**"
    if title_ko:
        desc += f" ({title_ko})"
    desc += f"은(는) {org_type}으로"
    if est:
        desc += f" {est}년 설립되었으며"
    if hq:
        desc += f" {hq}에 본부를 두고 있다."
    else:
        desc += "."
    lines.append(desc)
    if mandate:
        lines.append(f"\n**임무:** {mandate}")
    if parent:
        lines.append(f"\n**상위기관:** {parent}")
    if country:
        lines.append(f"\n**소속국:** {country}")
    if members:
        lines.append(f"\n**회원국:** {members}개국")

    if isinstance(key_roles, list) and key_roles:
        lines.append("\n## 국제공조 역할\n")
        for r in key_roles:
            lines.append(f"- {r}")

    if isinstance(ops, list) and ops:
        lines.append(f"\n## 참여 작전 ({len(ops)}건)\n")
        for o in ops[:20]:
            lines.append(f"- {o}")
        if len(ops) > 20:
            lines.append(f"- *외 {len(ops)-20}건*")

    if isinstance(partners, list) and partners:
        lines.append("\n## 협력 기관\n")
        lines.append(_format_list(partners))

    return "\n".join(lines)


def _gen_ko_country(meta: dict, en: str) -> str:
    """Generate Korean content for country pages."""
    title = meta.get("title", "")
    iso = meta.get("iso_code", "")
    legal_sys = _t(meta.get("legal_system", ""))
    region = meta.get("region", "")
    legis = meta.get("cybercrime_legislation", {})
    treaties = meta.get("treaty_memberships", [])
    agencies = meta.get("key_agencies", [])
    ic = meta.get("ic_capacity", {})
    ops = meta.get("operations_participated", [])
    assessment = meta.get("cooperation_assessment", "")

    lines = []
    lines.append("## 개요\n")
    lines.append(f"**{title}** (ISO: {iso})은(는) {region} 지역의 {legal_sys} 국가이다.")

    if isinstance(legis, dict) and legis.get("primary_law"):
        lines.append(f"\n## 사이버범죄 법제\n")
        lines.append(f"- **주요 법률:** {legis['primary_law']}")
        if legis.get("primary_law_date"):
            lines.append(f"- **제정일:** {legis['primary_law_date']}")
        procs = legis.get("procedural_powers", [])
        if procs:
            lines.append(f"- **절차적 권한:** {', '.join(procs)}")

    if isinstance(treaties, list) and treaties:
        lines.append(f"\n## 조약 가입 현황\n")
        lines.append("| 조약 | 상태 | 일자 |")
        lines.append("|------|------|------|")
        for t in treaties:
            if isinstance(t, dict):
                lines.append(f"| {t.get('framework','')} | {_t(t.get('status',''))} | {t.get('date','')} |")

    if isinstance(agencies, list) and agencies:
        lines.append(f"\n## 주요 기관\n")
        for a in agencies:
            lines.append(f"- {a}")

    if isinstance(ic, dict):
        lines.append(f"\n## 공조 역량 평가\n")
        if ic.get("rating"):
            lines.append(f"- **종합 등급:** {_t(ic['rating'])}")
        if ic.get("digital_forensics"):
            lines.append(f"- **디지털 포렌식:** {_t(ic['digital_forensics'])}")
        if ic.get("24_7_availability"):
            lines.append(f"- **24/7 대응:** 가능")
        mlat = ic.get("avg_mlat_response_days")
        if mlat:
            lines.append(f"- **평균 MLAT 응답일:** {mlat}일")

    if isinstance(ops, list) and ops:
        lines.append(f"\n## 참여 작전 ({len(ops)}건)\n")
        for o in ops[:15]:
            lines.append(f"- {o}")

    if assessment:
        lines.append(f"\n## 공조 평가\n")
        lines.append(assessment)

    return "\n".join(lines)


def _gen_ko_legal_framework(meta: dict, en: str) -> str:
    """Generate Korean for legal framework pages."""
    title = meta.get("title", "")
    title_ko = meta.get("official_name_ko", "")
    ftype = _t(meta.get("framework_type", ""))
    adopted = meta.get("adopted_date", "")
    entry = meta.get("entry_into_force", "")
    status = _t(meta.get("status", ""))
    sponsor = _strip_wikilink(meta.get("sponsoring_body", ""))
    parties = meta.get("parties", {})
    provisions = meta.get("key_provisions", [])

    lines = []
    lines.append("## 개요\n")
    desc = f"**{title}**"
    if title_ko:
        desc += f" ({title_ko})"
    desc += f"은(는) {ftype}으로"
    if adopted:
        desc += f" {adopted}에 채택되었으며"
    if entry:
        desc += f" {entry}에 발효되었다."
    else:
        desc += "."
    desc += f" 현재 상태: **{status}**."
    lines.append(desc)
    if sponsor:
        lines.append(f"\n**주관기관:** {sponsor}")

    if isinstance(parties, dict):
        sp = parties.get("states_parties", 0)
        sig = parties.get("signatories", 0)
        lines.append(f"\n## 당사국 현황\n")
        lines.append(f"- 당사국: {sp}개국")
        lines.append(f"- 서명국: {sig}개국")
        non = parties.get("notable_non_parties", [])
        if non:
            lines.append(f"- 주요 미가입국: {', '.join(str(n) for n in non)}")

    if isinstance(provisions, list) and provisions:
        lines.append(f"\n## 주요 조항\n")
        lines.append("| 조항 | 주제 | 관련성 |")
        lines.append("|------|------|--------|")
        for p in provisions:
            if isinstance(p, dict):
                lines.append(f"| {p.get('article','')} | {p.get('topic','')} | {p.get('relevance','')} |")

    return "\n".join(lines)


def _gen_ko_mechanism(meta: dict, en: str) -> str:
    """Generate Korean for mechanism pages."""
    title = meta.get("title", "")
    mtype = _t(meta.get("mechanism_type", ""))
    formality = _t(meta.get("formality", ""))
    speed = meta.get("speed", "")
    purpose = meta.get("purpose", "")
    admin = _strip_wikilink(meta.get("administered_by", ""))
    limitations = meta.get("limitations", [])

    lines = []
    lines.append("## 개요\n")
    lines.append(f"**{title}**은(는) {mtype} 유형의 {formality} 공조 메커니즘이다.")
    if purpose:
        lines.append(f"\n**목적:** {purpose}")
    if admin:
        lines.append(f"\n**운영기관:** {admin}")
    if speed:
        lines.append(f"\n**처리 속도:** {speed}")

    scope = meta.get("scope", {})
    if isinstance(scope, dict):
        enabled = [k.replace("_", " ") for k, v in scope.items() if v]
        if enabled:
            lines.append(f"\n## 범위\n")
            for e in enabled:
                lines.append(f"- {e}")

    if isinstance(limitations, list) and limitations:
        lines.append(f"\n## 한계\n")
        for lim in limitations:
            lines.append(f"- {lim}")

    return "\n".join(lines)


def _gen_ko_crime_type(meta: dict, en: str) -> str:
    """Generate Korean for crime-type pages."""
    title = meta.get("title", "")
    cat = _t(meta.get("crime_category", ""))
    challenges = meta.get("typical_ic_challenges", [])
    frameworks = meta.get("relevant_legal_frameworks", [])
    ops = meta.get("notable_operations", [])

    lines = []
    lines.append("## 개요\n")
    lines.append(f"**{title}** — {cat} 범죄 유형.")

    crim = meta.get("criminalization_status", {})
    if isinstance(crim, dict):
        if crim.get("broadly_criminalized"):
            lines.append("\n대부분의 국가에서 범죄화되어 있다.")
        if crim.get("definition_varies"):
            lines.append("다만, 정의는 국가별로 차이가 있다.")

    if isinstance(frameworks, list) and frameworks:
        lines.append(f"\n## 관련 법적 프레임워크\n")
        for f in frameworks:
            lines.append(f"- {f}")

    if isinstance(ops, list) and ops:
        lines.append(f"\n## 주요 작전\n")
        for o in ops:
            lines.append(f"- {o}")

    if isinstance(challenges, list) and challenges:
        lines.append(f"\n## 국제공조 과제\n")
        for c in challenges:
            lines.append(f"- {c}")

    return "\n".join(lines)


def _gen_ko_concept(meta: dict, en: str) -> str:
    """Generate Korean for concept pages."""
    title = meta.get("title", "")
    title_ko = meta.get("title_ko", "")
    definition = meta.get("definition", "")
    cat = _t(meta.get("concept_category", ""))
    domain = meta.get("domain", "")
    relevance = meta.get("relevance_to_ic", "")
    related = meta.get("related_concepts", [])

    lines = []
    lines.append("## 정의\n")
    desc = f"**{title}**"
    if title_ko:
        desc += f" ({title_ko})"
    desc += f" — {cat}."
    lines.append(desc)
    if definition:
        lines.append(f"\n{definition}")
    if domain:
        lines.append(f"\n**분야:** {domain}")
    if relevance:
        lines.append(f"\n## 사이버범죄 국제공조 관련성\n")
        lines.append(relevance)
    if isinstance(related, list) and related:
        lines.append(f"\n## 관련 개념\n")
        for r in related:
            lines.append(f"- {r}")

    return "\n".join(lines)


def _gen_ko_challenge(meta: dict, en: str) -> str:
    """Generate Korean for challenge pages."""
    title = meta.get("title", "")
    cat = _t(meta.get("challenge_category", ""))
    severity = _t(meta.get("severity", ""))
    solutions = meta.get("proposed_solutions", [])
    affected = meta.get("affected_mechanisms", [])

    lines = []
    lines.append("## 개요\n")
    lines.append(f"**{title}** — {cat} 유형의 과제 (심각도: {severity}).")
    if isinstance(affected, list) and affected:
        lines.append(f"\n**영향받는 메커니즘:** {_format_list(affected)}")
    if isinstance(solutions, list) and solutions:
        lines.append(f"\n## 제안된 해결책\n")
        for s in solutions:
            lines.append(f"- {s}")

    return "\n".join(lines)


def _gen_ko_procedure(meta: dict, en: str) -> str:
    """Generate Korean for procedure pages."""
    title = meta.get("title", "")
    ptype = _t(meta.get("procedure_type", ""))
    duration = meta.get("average_duration", "")
    steps = meta.get("steps", [])
    pitfalls = meta.get("common_pitfalls", [])

    lines = []
    lines.append("## 개요\n")
    lines.append(f"**{title}** — {ptype} 절차.")
    if duration:
        lines.append(f"\n**평균 소요 기간:** {duration}")

    if isinstance(steps, list) and steps:
        lines.append(f"\n## 단계별 절차\n")
        for s in steps:
            if isinstance(s, dict):
                step_n = s.get("step", "")
                actor = s.get("actor", "")
                action = s.get("action", "")
                lines.append(f"{step_n}. **{actor}** — {action}")

    if isinstance(pitfalls, list) and pitfalls:
        lines.append(f"\n## 일반적 함정\n")
        for p in pitfalls:
            lines.append(f"- {p}")

    return "\n".join(lines)


def _gen_ko_analysis(meta: dict, en: str) -> str:
    """Generate Korean for analysis pages — keep English content as-is."""
    # Analysis pages are complex; return empty to fall back to English
    return ""


# Translation cache loaded once at startup / build time
_translation_cache: Dict[str, str] = {}


def load_translation_cache() -> None:
    """Load pre-built translation cache from _workspace/."""
    global _translation_cache
    cache_file = Path(__file__).resolve().parent.parent / "_workspace" / "translation_cache.json"
    if cache_file.exists():
        import json
        raw = json.loads(cache_file.read_text(encoding="utf-8"))
        # Build slug -> translated_content mapping (use latest hash)
        by_slug: Dict[str, str] = {}
        for key, val in raw.items():
            slug = key.rsplit(":", 1)[0]
            by_slug[slug] = val
        _translation_cache.update(by_slug)


def render_bilingual(meta: dict, en_content: str, page_type: str,
                     category: str = "", slug: str = ""):
    """Render both English and Korean content for a page."""
    en_html = render_markdown(en_content)

    # Cached translations have repeatedly lagged behind source updates and
    # reintroduced stale counts and broken wikilinks. Prefer fresh generation.
    if slug == "index" or page_type == "category-index":
        return en_html, None

    ko_md = generate_ko_content(meta, en_content, page_type)
    if ko_md:
        ko_html = render_markdown(ko_md)
    else:
        ko_html = None

    return en_html, ko_html


# Load translations at import time
load_translation_cache()


# --- Routes ---

@app.route("/")
def home():
    return redirect(url_for("page", slug="index"))


@app.route("/wiki/<slug>")
def page(slug):
    filepath = WIKI_DIR / f"{slug}.md"
    if not filepath.exists():
        filepath = resolve_wiki_path(slug)
    if not filepath or not filepath.exists():
        abort(404)
    meta, content = parse_page(filepath)
    page_type = meta.get("type", "")
    category = get_category_for_file(filepath)
    en_html, ko_html = render_bilingual(
        meta, content, page_type, category=category or "", slug=slug)
    title = meta.get("title", slug.replace("-", " ").title())
    infobox = build_infobox(meta, page_type)
    cat_label = CATEGORIES.get(category, {}).get("label", "")
    return render_template(
        "article.html", title=title, content=en_html, content_ko=ko_html,
        meta=meta, infobox=infobox, category=category, cat_label=cat_label,
        slug=slug, page_type=page_type,
    )


@app.route("/wiki/<category>/<slug>")
def category_page(category, slug):
    filepath = WIKI_DIR / category / f"{slug}.md"
    if not filepath.exists():
        abort(404)
    meta, content = parse_page(filepath)
    page_type = meta.get("type", "")
    en_html, ko_html = render_bilingual(
        meta, content, page_type, category=category, slug=slug)
    title = meta.get("title", slug.replace("-", " ").title())
    infobox = build_infobox(meta, page_type)
    cat_label = CATEGORIES.get(category, {}).get("label", "")
    return render_template(
        "article.html", title=title, content=en_html, content_ko=ko_html,
        meta=meta, infobox=infobox, category=category, cat_label=cat_label,
        slug=slug, page_type=page_type,
    )


@app.route("/wiki/_missing/<slug>")
def missing_page(slug):
    return render_template("missing.html", slug=slug), 404


@app.route("/category/<category>")
def category_list(category):
    cat_dir = WIKI_DIR / category
    if not cat_dir.is_dir():
        abort(404)
    pages = []
    for md_file in sorted(cat_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        try:
            meta, _ = parse_page(md_file)
        except Exception:
            meta = {}
        pages.append({
            "slug": md_file.stem,
            "title": meta.get("title", md_file.stem.replace("-", " ").title()),
            "type": meta.get("type", ""),
            "meta": meta,
        })
    cat_info = CATEGORIES.get(category, {"label": category, "icon": "📄"})
    return render_template(
        "category.html", category=category,
        cat_info=cat_info, pages=pages,
    )


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return render_template("search.html", query="", results=[])
    results = []
    query_lower = query.lower()
    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue
        try:
            meta, content = parse_page(md_file)
        except Exception:
            continue
        title = meta.get("title", md_file.stem)
        title_ko = meta.get("title_ko", meta.get("official_name_ko", ""))
        searchable = f"{title} {title_ko} {content}".lower()
        if query_lower in searchable:
            # Find context snippet
            idx = searchable.find(query_lower)
            start = max(0, idx - 80)
            end = min(len(searchable), idx + len(query_lower) + 80)
            snippet = searchable[start:end].strip()
            cat = get_category_for_file(md_file)
            results.append({
                "slug": md_file.stem,
                "category": cat,
                "title": title,
                "title_ko": title_ko,
                "type": meta.get("type", ""),
                "snippet": f"...{snippet}...",
            })
    results.sort(key=lambda r: query_lower in (r["title"] or "").lower(), reverse=True)
    return render_template("search.html", query=query, results=results)


@app.route("/stats")
def stats():
    all_pages = get_all_pages()
    cat_counts = {}
    for p in all_pages:
        cat = p["category"] or "_root"
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    total_sources = cat_counts.get("sources", 0)
    total_ops = cat_counts.get("operations", 0)

    # Aggregate operation metrics
    op_stats = {
        "total_arrests": 0, "total_servers": 0, "total_domains": 0,
        "total_countries": set(), "total_agencies": set(),
        "by_coordinator": {}, "by_crime_type": {}, "by_year": {},
    }
    ops_dir = WIKI_DIR / "operations"
    if ops_dir.is_dir():
        for md_file in ops_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue
            try:
                meta, _ = parse_page(md_file)
            except Exception:
                continue
            # Metrics
            metrics = meta.get("metrics") or meta.get("results") or {}
            if isinstance(metrics, dict):
                arrests = metrics.get("arrests", 0)
                if isinstance(arrests, (int, float)):
                    op_stats["total_arrests"] += arrests
                servers = metrics.get("servers_seized", 0)
                if isinstance(servers, (int, float)):
                    op_stats["total_servers"] += servers
                domains = metrics.get("domains_seized", 0)
                if isinstance(domains, (int, float)):
                    op_stats["total_domains"] += domains
            # Countries
            countries = meta.get("participating_countries", [])
            if isinstance(countries, list):
                for c in countries:
                    c_clean = str(c).strip("[]\"' ")
                    if c_clean:
                        op_stats["total_countries"].add(c_clean)
            # Coordinator
            coord = meta.get("coordinating_body", meta.get("lead_agency", ""))
            coord = str(coord).strip("[]\"' ")
            if coord:
                op_stats["by_coordinator"][coord] = op_stats["by_coordinator"].get(coord, 0) + 1
            # Crime type
            ct = meta.get("crime_type", "")
            ct = str(ct).strip("[]\"' ")
            if ct:
                op_stats["by_crime_type"][ct] = op_stats["by_crime_type"].get(ct, 0) + 1
            # Year
            tf = meta.get("timeframe", {})
            announced = ""
            if isinstance(tf, dict):
                announced = tf.get("announced", "")
            if not announced:
                announced = meta.get("publish_date", "")
            if announced and len(str(announced)) >= 4:
                year = str(announced)[:4]
                op_stats["by_year"][year] = op_stats["by_year"].get(year, 0) + 1

    op_stats["total_countries"] = len(op_stats["total_countries"])

    # Source stats
    source_domains = {}
    src_dir = WIKI_DIR / "sources"
    if src_dir.is_dir():
        for md_file in src_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue
            try:
                meta, _ = parse_page(md_file)
            except Exception:
                continue
            publisher = meta.get("publisher", "Unknown")
            source_domains[publisher] = source_domains.get(publisher, 0) + 1

    return render_template(
        "stats.html", total=len(all_pages),
        cat_counts=cat_counts, categories=CATEGORIES,
        total_sources=total_sources, total_ops=total_ops,
        op_stats=op_stats, source_domains=source_domains,
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.context_processor
def inject_globals():
    return {
        "categories": CATEGORIES,
        "now": datetime.now().strftime("%Y-%m-%d"),
    }


if __name__ == "__main__":
    print("=" * 60)
    print("  사이버범죄 국제공조 위키")
    print("  http://localhost:5000")
    print("=" * 60)
    app.run(debug=False, host="0.0.0.0", port=5000)
