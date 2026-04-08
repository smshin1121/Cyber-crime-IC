"""
사이버범죄 국제공조 위키 — Wikipedia-style Web Interface
"""
import os
import re
from pathlib import Path
from datetime import datetime

import frontmatter
import markdown
from flask import Flask, render_template, request, abort, redirect, url_for
from markupsafe import Markup

app = Flask(__name__)

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"

# Category metadata (Korean labels)
CATEGORIES = {
    "legal-frameworks": {"label": "법적 프레임워크", "icon": "📜"},
    "organizations": {"label": "기관", "icon": "🏛️"},
    "countries": {"label": "국가", "icon": "🌍"},
    "operations": {"label": "작전", "icon": "🎯"},
    "cases": {"label": "사건", "icon": "⚖️"},
    "mechanisms": {"label": "공조 메커니즘", "icon": "🔗"},
    "procedures": {"label": "절차", "icon": "📋"},
    "crime-types": {"label": "범죄유형", "icon": "🔒"},
    "challenges": {"label": "과제", "icon": "⚠️"},
    "concepts": {"label": "법적 개념", "icon": "📖"},
    "sources": {"label": "출처", "icon": "📰"},
    "analysis": {"label": "분석", "icon": "📊"},
    "timelines": {"label": "타임라인", "icon": "📅"},
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


def render_markdown(text):
    """Render markdown to HTML with wikilinks and callouts."""
    text = convert_wikilinks(text)
    html = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "attr_list"],
        extension_configs={"toc": {"toc_depth": "2-3"}}
    )
    html = convert_callouts(html)
    return Markup(html)


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


def build_infobox(meta, page_type):
    """Build infobox data from frontmatter."""
    infobox = []
    type_label = TYPE_LABELS_KO.get(page_type, page_type)
    infobox.append(("유형", type_label))

    field_map = {
        "operation": [
            ("status", "상태"), ("operation_type", "작전유형"),
            ("timeframe", "기간"), ("lead_agency", "주도기관"),
            ("crime_type", "범죄유형"),
        ],
        "organization": [
            ("org_type", "기관유형"), ("headquarters", "본부"),
            ("established", "설립"), ("member_states", "회원국"),
        ],
        "country": [
            ("iso_code", "ISO 코드"), ("legal_system", "법체계"),
            ("region", "지역"),
        ],
        "legal-framework": [
            ("framework_type", "유형"), ("status", "상태"),
            ("adopted_date", "채택일"), ("entry_into_force", "발효일"),
        ],
        "mechanism": [
            ("mechanism_type", "유형"), ("formality", "형식성"),
            ("speed", "속도"),
        ],
        "concept": [
            ("title_ko", "한국어"), ("concept_category", "분류"),
            ("domain", "분야"),
        ],
        "source": [
            ("source_type", "출처유형"), ("publisher", "발행처"),
            ("publish_date", "발행일"), ("reliability", "신뢰도"),
            ("credibility", "신빙성"),
        ],
        "crime-type": [
            ("crime_category", "분류"),
        ],
    }

    for field, label in field_map.get(page_type, []):
        val = meta.get(field)
        if val and val not in ("", 0, [], {}):
            if isinstance(val, dict):
                parts = [f"{k}: {v}" for k, v in val.items() if v]
                val = ", ".join(parts[:3])
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val[:5])
            infobox.append((label, str(val)))

    # Metrics (for operations)
    metrics = meta.get("metrics") or meta.get("results")
    if isinstance(metrics, dict):
        metric_labels = {
            "arrests": "체포", "servers_seized": "서버 압수",
            "domains_seized": "도메인 압수",
            "cryptocurrency_seized": "암호화폐 압수",
            "participating_countries": "참여국",
            "participating_agencies": "참여기관",
            "financial_seized": "금융 압수",
        }
        for key, label in metric_labels.items():
            v = metrics.get(key)
            if v and v not in (0, "", "0"):
                infobox.append((label, str(v)))

    # Parties (for legal frameworks)
    parties = meta.get("parties")
    if isinstance(parties, dict):
        sp = parties.get("states_parties")
        if sp:
            infobox.append(("당사국", str(sp)))

    # IC capacity (for countries)
    ic = meta.get("ic_capacity")
    if isinstance(ic, dict):
        rating = ic.get("rating")
        if rating:
            infobox.append(("공조 역량", rating))

    # Source count
    sc = meta.get("source_count")
    if sc:
        infobox.append(("출처 수", str(sc)))

    return infobox


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
    html = render_markdown(content)
    title = meta.get("title", slug.replace("-", " ").title())
    page_type = meta.get("type", "")
    infobox = build_infobox(meta, page_type)
    category = get_category_for_file(filepath)
    cat_label = CATEGORIES.get(category, {}).get("label", "")
    return render_template(
        "article.html", title=title, content=html, meta=meta,
        infobox=infobox, category=category, cat_label=cat_label,
        slug=slug, page_type=page_type,
    )


@app.route("/wiki/<category>/<slug>")
def category_page(category, slug):
    filepath = WIKI_DIR / category / f"{slug}.md"
    if not filepath.exists():
        abort(404)
    meta, content = parse_page(filepath)
    html = render_markdown(content)
    title = meta.get("title", slug.replace("-", " ").title())
    page_type = meta.get("type", "")
    infobox = build_infobox(meta, page_type)
    cat_label = CATEGORIES.get(category, {}).get("label", "")
    return render_template(
        "article.html", title=title, content=html, meta=meta,
        infobox=infobox, category=category, cat_label=cat_label,
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
