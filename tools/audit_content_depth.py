from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
OPS_DIR = WIKI_DIR / "operations"
CASES_DIR = WIKI_DIR / "cases"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIR = ROOT / "raw"
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = WIKI_DIR / "analysis" / "content-depth-audit-2026-04-26.md"

PLACEHOLDER_PATTERNS = (
    "source-derived",
    "structured placeholder",
    "should be expanded",
    "should be refined",
    "procedural enrichment",
    "generated from",
    "official action title from the source corpus",
    "no visible cross-border mechanism is documented",
    "not treated as a separate international-cooperation operation",
)

QUALITY_SECTION_PATTERNS = {
    "timeline": re.compile(r"^## .*?(Timeline|Proceedings|Operational Timeline|시계열|타임라인)", re.I | re.M),
    "ic": re.compile(r"^## .*?(International Cooperation|Cooperation|Participating|공조|협력)", re.I | re.M),
    "legal": re.compile(r"^## .*?(Legal|Law|Framework|Analysis|법|분석)", re.I | re.M),
    "evidence": re.compile(r"^## .*?(Evidence|Attribution|Forensics|증거|귀속)", re.I | re.M),
    "results": re.compile(r"^## .*?(Results|Impact|Outcomes|결과|영향)", re.I | re.M),
    "sources": re.compile(r"^## .*?(Source Coverage|References|참고)", re.I | re.M),
}

CRIME_HINTS = {
    "csam-ic": re.compile(r"\b(child pornography|child sexual|child sex abuse|csam|sexual exploitation of children)\b", re.I),
    "bec-ic": re.compile(r"\b(business email compromise|\bBEC\b|CEO fraud|email compromise)\b", re.I),
    "ransomware-ic": re.compile(r"\b(ransomware|lockbit|hive|blackcat|alphv|phobos)\b", re.I),
    "malware-ic": re.compile(r"\b(malware|botnet|goznym|dridex|emotet|qakbot|danabot|banking trojan)\b", re.I),
    "dark-web-ic": re.compile(r"\b(dark web|darkweb|darknet|tor hidden|silk road|alphabay)\b", re.I),
}


@dataclass(frozen=True)
class DepthRow:
    category: str
    slug: str
    title: str
    score: int
    source_count: int
    references_count: int
    body_words: int
    source_words: int
    sections: int
    quality_sections: int
    placeholder_hits: int
    issues: list[str]


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def strip_references(body: str) -> str:
    match = re.search(r"^## References\b", body, re.I | re.M)
    if match:
        return body[: match.start()]
    match = re.search(r"^## 참고문헌\b", body, re.I | re.M)
    if match:
        return body[: match.start()]
    return body


def word_count(text: str) -> int:
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", r"\2 \1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣$€£.,%-]*", text))


def count_references(body: str) -> int:
    match = re.search(r"^## References\b", body, re.I | re.M)
    if not match:
        match = re.search(r"^## 참고문헌\b", body, re.I | re.M)
    tail = body[match.start() :] if match else body
    return len(re.findall(r"^\|\s*\[?\d+\]?\s*\|", tail, re.M))


def source_word_count(slug: str) -> int:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return 0
    try:
        post = frontmatter.load(path)
    except Exception:
        return 0
    meta_words = post.metadata.get("word_count")
    try:
        return int(meta_words)
    except Exception:
        pass
    raw_path = post.metadata.get("raw_path")
    if raw_path:
        raw = ROOT / str(raw_path)
        if raw.exists():
            try:
                return word_count(frontmatter.load(raw).content)
            except Exception:
                return word_count(raw.read_text(encoding="utf-8", errors="replace"))
    return word_count(post.content or "")


def source_slugs(meta: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for item in as_list(meta.get("sources")):
        slug = wikilink_slug(item)
        if slug:
            out.append(slug)
    return out


def crime_values(meta: dict[str, Any]) -> set[str]:
    vals = []
    vals.extend(as_list(meta.get("crime_type")))
    vals.extend(as_list(meta.get("crime_types")))
    vals.extend(as_list(meta.get("crime_charged")))
    return {wikilink_slug(v) for v in vals if wikilink_slug(v)}


def audit_page(path: Path, category: str) -> DepthRow:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    body_without_refs = strip_references(body)
    title = str(meta.get("title") or path.stem)
    text_for_scan = f"{title}\n{body_without_refs}"

    sources = source_slugs(meta)
    source_count = int(meta.get("source_count") or len(sources) or 0)
    refs = count_references(body)
    body_words = word_count(body_without_refs)
    sections = len(re.findall(r"^##\s+", body_without_refs, re.M))
    quality_sections = sum(1 for pattern in QUALITY_SECTION_PATTERNS.values() if pattern.search(body_without_refs))
    placeholder_hits = sum(text_for_scan.lower().count(pattern) for pattern in PLACEHOLDER_PATTERNS)
    source_words = sum(source_word_count(slug) for slug in sources)

    issues: list[str] = []
    score = 0

    if source_count != refs and refs:
        issues.append(f"source_count_mismatch:{source_count}!={refs}")
        score += 8

    if placeholder_hits:
        issues.append(f"placeholder_language:{placeholder_hits}")
        score += min(30, 10 + placeholder_hits * 3)

    if source_count >= 5 and body_words < 350:
        issues.append(f"source_rich_thin_body:{body_words}w")
        score += 35
    elif source_count >= 3 and body_words < 220:
        issues.append(f"thin_body:{body_words}w")
        score += 22

    if source_count >= 5 and quality_sections < 4:
        issues.append(f"missing_quality_sections:{quality_sections}/6")
        score += 18

    if source_words >= 1200 and body_words < 450:
        issues.append(f"raw_available_underused:{source_words}w_sources")
        score += 22

    if source_count >= 5 and source_words >= 2500 and body_words < 700:
        issues.append("high_source_to_body_gap")
        score += 12

    if category == "operations" and str(meta.get("title_ko") or "").startswith("공식 작전명 없음"):
        issues.append("unresolved_operation_name")
        score += 8

    if "Enforcement Action" in title and body_words < 500:
        issues.append("generated_enforcement_title")
        score += 10

    crimes = crime_values(meta)
    for expected, pattern in CRIME_HINTS.items():
        if pattern.search(text_for_scan) and expected not in crimes:
            if expected == "dark-web-ic" and ("drug-trafficking" in crimes or "csam-ic" in crimes):
                continue
            issues.append(f"possible_crime_type_mismatch:{expected}")
            score += 14
            break

    return DepthRow(
        category=category,
        slug=path.stem,
        title=title,
        score=score,
        source_count=source_count,
        references_count=refs,
        body_words=body_words,
        source_words=source_words,
        sections=sections,
        quality_sections=quality_sections,
        placeholder_hits=placeholder_hits,
        issues=issues,
    )


def audit_all() -> list[DepthRow]:
    rows: list[DepthRow] = []
    for category, directory in (("operations", OPS_DIR), ("cases", CASES_DIR)):
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("_"):
                continue
            rows.append(audit_page(path, category))
    rows.sort(key=lambda row: (-row.score, -row.source_count, row.category, row.slug))
    return rows


def render_report(rows: list[DepthRow]) -> str:
    issue_counts = Counter(issue.split(":", 1)[0] for row in rows for issue in row.issues)
    category_counts = Counter(row.category for row in rows)
    high = [row for row in rows if row.score >= 45]
    source_rich_thin = [row for row in rows if any(i.startswith("source_rich_thin_body") for i in row.issues)]
    placeholders = [row for row in rows if row.placeholder_hits]
    mismatch = [row for row in rows if any(i.startswith("possible_crime_type_mismatch") for i in row.issues)]

    lines = [
        "---",
        "title: Content Depth Audit (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Repository-wide content-depth audit for operation and case pages, focused on source-rich thin pages, placeholder prose, underused raw sources, and probable crime-type mismatches."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This audit checks whether operation and case pages contain enough source-backed substance, not merely whether they have reference rows. It was added after sampling showed pages with five references but only a minimal overview.",
        "",
        f"- Pages audited: **{len(rows)}** ({category_counts['operations']} operations, {category_counts['cases']} cases)",
        f"- High-priority pages (`score >= 45`): **{len(high)}**",
        f"- Source-rich but thin pages: **{len(source_rich_thin)}**",
        f"- Pages with placeholder/autogenerated language: **{len(placeholders)}**",
        f"- Probable crime-type mismatch flags: **{len(mismatch)}**",
        "",
        "## Issue Counts",
        "",
        "| Issue | Count |",
        "|---|---:|",
    ]
    for issue, count in issue_counts.most_common():
        lines.append(f"| {issue} | {count} |")

    lines.extend(
        [
            "",
            "## Top 100 Priority Queue",
            "",
            "| Rank | Page | Type | Score | Sources | Body words | Source words | Issues |",
            "|---:|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for idx, row in enumerate(rows[:100], start=1):
        issues = ", ".join(row.issues[:5])
        lines.append(
            f"| {idx} | [[{row.slug}]] | {row.category[:-1]} | {row.score} | {row.source_count} | {row.body_words} | {row.source_words} | {issues} |"
        )

    lines.extend(
        [
            "",
            "## Source-Rich Thin Pages",
            "",
            "| Page | Type | Sources | Body words | Source words | Quality sections |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in source_rich_thin[:80]:
        lines.append(
            f"| [[{row.slug}]] | {row.category[:-1]} | {row.source_count} | {row.body_words} | {row.source_words} | {row.quality_sections}/6 |"
        )

    lines.extend(
        [
            "",
            "## Probable Crime-Type Mismatches",
            "",
            "| Page | Type | Sources | Issue |",
            "|---|---|---:|---|",
        ]
    )
    for row in mismatch[:80]:
        issue = next(i for i in row.issues if i.startswith("possible_crime_type_mismatch"))
        lines.append(f"| [[{row.slug}]] | {row.category[:-1]} | {row.source_count} | {issue} |")

    lines.extend(
        [
            "",
            "## Remediation Rules",
            "",
            "1. **Source-rich thin pages** should be enriched first from already collected raw/source pages before any new web search.",
            "2. **Placeholder case pages** should either become real case summaries or be merged into a canonical operation/case record.",
            "3. **Follow-on operation pages** should not count reused umbrella-operation results in numeric aggregate fields unless the result is specific to that follow-on action.",
            "4. **Crime-type mismatch flags** require source-backed review, not automatic replacement.",
            "5. **Unresolved operation-name pages** may be valid, but should carry an explicit naming note and robust substantive sections.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[DepthRow], out_prefix: str) -> None:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    json_path = WORKSPACE / f"{out_prefix}.json"
    csv_path = WORKSPACE / f"{out_prefix}.csv"
    json_path.write_text(
        json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            data = asdict(row)
            data["issues"] = "; ".join(row.issues)
            writer.writerow(data)
    REPORT_PATH.write_text(render_report(rows), encoding="utf-8")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORT_PATH}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit wiki operation/case content depth.")
    parser.add_argument("--prefix", default="content_depth_audit_2026-04-26")
    args = parser.parse_args()
    rows = audit_all()
    write_outputs(rows, args.prefix)
    high = sum(1 for row in rows if row.score >= 45)
    source_rich_thin = sum(1 for row in rows if any(i.startswith("source_rich_thin_body") for i in row.issues))
    placeholders = sum(1 for row in rows if row.placeholder_hits)
    print(f"Audited {len(rows)} pages")
    print(f"High priority: {high}")
    print(f"Source-rich thin: {source_rich_thin}")
    print(f"Placeholder language: {placeholders}")


if __name__ == "__main__":
    main()
