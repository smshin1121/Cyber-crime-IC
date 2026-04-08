"""
Statistics synchronization tool — auto-updates overview.md and
ic-statistics-dashboard.md with computed values from wiki pages.

Run before build_static.py to keep dashboard data in sync.
"""
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
TODAY = date.today().isoformat()


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

def collect_stats() -> dict[str, Any]:
    """Scan all wiki pages and compute aggregate statistics."""
    ops_dir = WIKI_DIR / "operations"
    src_dir = WIKI_DIR / "sources"

    stats: dict[str, Any] = {
        "total_ops": 0,
        "period_counts": defaultdict(int),      # period -> count
        "coordinator_counts": defaultdict(int),  # coordinator -> count
        "crime_type_counts": defaultdict(int),
        "year_counts": defaultdict(int),
        "total_arrests": 0,
        "total_servers": 0,
        "total_domains": 0,
        "countries_seen": set(),
        "top_ci": [],  # (ci, title, slug, source_count, results_summary)
        "total_sources": 0,
        "source_publisher": defaultdict(int),
        "cat_counts": {},
    }

    # --- Operation pages ---
    if ops_dir.is_dir():
        for md in ops_dir.glob("*.md"):
            if md.name.startswith("_"):
                continue
            try:
                meta, _ = frontmatter.load(md).metadata, None
                meta = frontmatter.load(md).metadata
            except Exception:
                continue
            stats["total_ops"] += 1

            # Period
            period = meta.get("period")
            if period:
                stats["period_counts"][int(period)] += 1

            # Coordinator
            coord = meta.get("coordinating_body", meta.get("lead_agency", ""))
            coord = str(coord).strip("[]\"' ")
            if coord:
                # Normalize
                coord_norm = _normalize_coordinator(coord)
                stats["coordinator_counts"][coord_norm] += 1

            # Crime type
            ct = meta.get("crime_type", "")
            ct = str(ct).strip("[]\"' ")
            if ct:
                stats["crime_type_counts"][ct] += 1

            # Year
            tf = meta.get("timeframe", {})
            announced = ""
            if isinstance(tf, dict):
                announced = str(tf.get("announced", ""))
            if not announced or announced == "None":
                announced = str(meta.get("publish_date", ""))
            if announced and len(announced) >= 4:
                year = announced[:4]
                stats["year_counts"][year] += 1

            # Metrics
            metrics = meta.get("results", meta.get("metrics", {}))
            if isinstance(metrics, dict):
                arrests = metrics.get("arrests", 0)
                if isinstance(arrests, (int, float)):
                    stats["total_arrests"] += int(arrests)
                servers = metrics.get("servers_seized", 0)
                if isinstance(servers, (int, float)):
                    stats["total_servers"] += int(servers)
                domains = metrics.get("domains_seized", 0)
                if isinstance(domains, (int, float)):
                    stats["total_domains"] += int(domains)

            # Countries
            countries = meta.get("participating_countries", [])
            if isinstance(countries, list):
                for c in countries:
                    stats["countries_seen"].add(str(c).strip("[]\"' "))

            # CI top
            ci = meta.get("credibility_index", 0)
            if ci:
                ci = float(ci)
                stats["top_ci"].append((
                    ci,
                    meta.get("title", md.stem),
                    md.stem,
                    meta.get("source_count", 0),
                ))

    # Sort top CI descending
    stats["top_ci"].sort(key=lambda x: (-x[0], x[1]))

    # --- Source pages ---
    if src_dir.is_dir():
        for md in src_dir.glob("*.md"):
            if md.name.startswith("_"):
                continue
            try:
                meta = frontmatter.load(md).metadata
            except Exception:
                continue
            stats["total_sources"] += 1
            pub = meta.get("publisher", "Unknown")
            stats["source_publisher"][pub] += 1

    # --- Category counts ---
    for subdir in WIKI_DIR.iterdir():
        if subdir.is_dir() and not subdir.name.startswith("_"):
            count = sum(
                1 for f in subdir.glob("*.md")
                if not f.name.startswith("_")
            )
            if count > 0:
                stats["cat_counts"][subdir.name] = count

    stats["unique_countries"] = len(stats["countries_seen"] - {""})

    return stats


def _normalize_coordinator(raw: str) -> str:
    """Normalize coordinator name for aggregation."""
    low = raw.lower()
    if "europol" in low:
        return "Europol / Europol EC3"
    if "interpol" in low and "afripol" in low:
        return "INTERPOL-AFRIPOL"
    if "interpol" in low:
        return "INTERPOL / INTERPOL IGCI"
    if "doj" in low or "justice" in low or "fbi" in low:
        return "DOJ / FBI (미국 주도)"
    if "afripol" in low:
        return "INTERPOL-AFRIPOL"
    if "eurojust" in low:
        return "Eurojust"
    return raw


# ---------------------------------------------------------------------------
# Update overview.md
# ---------------------------------------------------------------------------

def update_overview(stats: dict[str, Any]) -> int:
    """Update the Cooperation Statistics table in overview.md. Returns changes count."""
    fp = WIKI_DIR / "overview.md"
    post = frontmatter.load(fp)
    content = post.content

    # Build replacement statistics table
    p1 = stats["period_counts"].get(1, 0)
    p2 = stats["period_counts"].get(2, 0)
    p3 = stats["period_counts"].get(3, 0)
    total_ops = stats["total_ops"]

    coord = stats["coordinator_counts"]
    europol = coord.get("Europol / Europol EC3", 0)
    interpol = coord.get("INTERPOL / INTERPOL IGCI", 0)
    doj = coord.get("DOJ / FBI (미국 주도)", 0)

    new_table = f"""| Metric | Value | Period |
|--------|-------|--------|
| Total operations documented | {total_ops} | 2014-2025 |
| Period 1 operations | {p1} | 2014-2018 |
| Period 2 operations | {p2} | 2019-2022 |
| Period 3 operations | {p3} | 2023-2025 |
| Europol-coordinated | {europol} | All periods |
| INTERPOL-coordinated | {interpol} | All periods |
| DOJ/US-led | {doj} | All periods |
| Total arrests (sourced operations) | {stats['total_arrests']:,}+ | Across all operations |
| Total servers seized | {stats['total_servers']:,}+ | Primarily Europol operations |
| Total domains seized | {stats['total_domains']:,}+ | All operations |
| Unique participating countries | {stats['unique_countries']}+ | All operations |
| Sources with dedicated pages | {stats['total_sources']} | {_source_summary(stats)} |
| Crime types documented | {stats['cat_counts'].get('crime-types', 0)} | All documented types |"""

    # Replace existing statistics table
    old_table_pattern = re.compile(
        r'(\| Metric \| Value \| Period \|.*?)(\n\n|\n##)',
        re.DOTALL,
    )
    match = old_table_pattern.search(content)
    if match:
        end_marker = match.group(2)
        content = content[:match.start()] + new_table + end_marker + content[match.end():]
        changes = 1
    else:
        changes = 0

    # Update operation count in executive summary
    content = re.sub(
        r'\*\*(\d+) operations\*\*',
        f'**{total_ops} operations**',
        content,
    )

    post.content = content
    post.metadata["updated"] = TODAY
    fp.write_text(frontmatter.dumps(post), encoding="utf-8")
    return changes


def _source_summary(stats: dict) -> str:
    """Build source summary string like 'Europol 6, INTERPOL 10, ...'."""
    parts = []
    for pub, cnt in sorted(
        stats["source_publisher"].items(),
        key=lambda x: -x[1],
    ):
        parts.append(f"{pub} {cnt}")
    return ", ".join(parts[:5])


# ---------------------------------------------------------------------------
# Update ic-statistics-dashboard.md
# ---------------------------------------------------------------------------

def update_dashboard(stats: dict[str, Any]) -> int:
    """Update the statistics dashboard page. Returns changes count."""
    fp = WIKI_DIR / "analysis" / "ic-statistics-dashboard.md"
    if not fp.exists():
        return 0

    post = frontmatter.load(fp)
    content = post.content
    changes = 0

    total_ops = stats["total_ops"]
    p1 = stats["period_counts"].get(1, 0)
    p2 = stats["period_counts"].get(2, 0)
    p3 = stats["period_counts"].get(3, 0)

    # Update section 1: 전체 현황 table
    overview_table = f"""| 지표 | 값 |
|------|-----|
| 총 작전 수 | {total_ops} |
| Period 1 (2014-2018) | {p1} |
| Period 2 (2019-2022) | {p2} |
| Period 3 (2023-2025) | {p3} |
| 총 출처 수 | {stats['total_sources']} (dedicated pages) + Excel 소스 |"""

    old_overview = re.compile(
        r'(\| 지표 \| 값 \|.*?)\n\n',
        re.DOTALL,
    )
    match = old_overview.search(content)
    if match:
        content = content[:match.start()] + overview_table + "\n\n" + content[match.end():]
        changes += 1

    # Update section 1: 조정기관별 분포
    coord = stats["coordinator_counts"]
    europol = coord.get("Europol / Europol EC3", 0)
    interpol = coord.get("INTERPOL / INTERPOL IGCI", 0)
    doj = coord.get("DOJ / FBI (미국 주도)", 0)
    afripol = coord.get("INTERPOL-AFRIPOL", 0)
    eurojust = coord.get("Eurojust", 0)
    other = total_ops - europol - interpol - doj - afripol - eurojust

    coord_table = f"""| 조정기관 | 작전 수 | 비고 |
|---------|---------|------|
| Europol / Europol EC3 | {europol} | 가장 많은 작전 조정; 랜섬웨어, 봇넷, 사기 포럼 등 |
| INTERPOL / INTERPOL IGCI | {interpol} | 체포 규모에서 압도적; HAECHI, Jackal, Serengeti 등 |
| DOJ / FBI (미국 주도) | {doj} | 기소·압수 중심 |
| AFRIPOL | {afripol} | 아프리카 공동 조정 |
| Eurojust | {eurojust} | 사법 공조 조정 |
| 양자/기타 (조정기관 없음) | {other} | 한국 양자작전 포함; 단독 기소 다수 |"""

    old_coord = re.compile(
        r'(\| 조정기관 \| 작전 수 \| 비고 \|.*?)\n\n',
        re.DOTALL,
    )
    match = old_coord.search(content)
    if match:
        content = content[:match.start()] + coord_table + "\n\n" + content[match.end():]
        changes += 1

    # Update section 6: 위키 커버리지 현황
    cat = stats["cat_counts"]
    coverage_table = f"""| 카테고리 | 페이지 수 | 비고 |
|---------|---------|------|
| 법적 프레임워크 | {cat.get('legal-frameworks', 0)} | 부다페스트 협약 등 |
| 기관 | {cat.get('organizations', 0)} | 주요 기관 |
| 국가 | {cat.get('countries', 0)} | 국가 프로필 |
| 작전 | {total_ops} | 2014-2025 주요 작전 (P1: {p1}, P2: {p2}, P3: {p3}) |
| 메커니즘 | {cat.get('mechanisms', 0)} | 공조 메커니즘 |
| 범죄유형 | {cat.get('crime-types', 0)} | 문서화된 범죄유형 |
| 개념 | {cat.get('concepts', 0)} | 법적 개념 |
| 출처 | {stats['total_sources']} | 전용 출처 페이지 |
| 분석 | {cat.get('analysis', 0)} | 본 대시보드 포함 |
| **총 페이지** | **{sum(cat.values())}** | _index 파일 및 메타파일 제외 |"""

    old_coverage = re.compile(
        r'(\| 카테고리 \| 페이지 수 \| 비고 \|.*?)\n\n',
        re.DOTALL,
    )
    match = old_coverage.search(content)
    if match:
        content = content[:match.start()] + coverage_table + "\n\n" + content[match.end():]
        changes += 1

    # Update info callout at top
    content = re.sub(
        r'위키에 수집된 \d+개 작전과 \d+개 출처',
        f'위키에 수집된 {total_ops}개 작전과 {stats["total_sources"]}개 출처',
        content,
    )

    post.content = content
    post.metadata["updated"] = TODAY
    post.metadata["sources_consulted"] = stats["total_sources"]
    fp.write_text(frontmatter.dumps(post), encoding="utf-8")
    return changes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("  Statistics Sync Tool")
    print("=" * 60)

    stats = collect_stats()

    print(f"\n  Operations: {stats['total_ops']}")
    print(f"  Sources: {stats['total_sources']}")
    print(f"  Arrests: {stats['total_arrests']:,}")
    print(f"  Servers: {stats['total_servers']:,}")
    print(f"  Domains: {stats['total_domains']:,}")
    print(f"  Countries: {stats['unique_countries']}")
    print(f"  Coordinators: {dict(stats['coordinator_counts'])}")

    c1 = update_overview(stats)
    print(f"\n  overview.md: {c1} table(s) updated")

    c2 = update_dashboard(stats)
    print(f"  ic-statistics-dashboard.md: {c2} table(s) updated")

    print("\nDone.")


if __name__ == "__main__":
    main()
