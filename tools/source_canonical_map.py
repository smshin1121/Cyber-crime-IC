from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = ROOT / "wiki" / "analysis" / "source-canonical-map-2026-04-26.md"


@dataclass(frozen=True)
class SourceRecord:
    slug: str
    title: str
    publisher: str
    publish_date: str
    collection_url: str
    source_type: str
    raw_path: str
    text_status: str
    content_hash: str
    pages_updated: int
    word_count: int
    body_words: int
    score: int
    score_reasons: list[str]


@dataclass(frozen=True)
class CanonicalGroup:
    collection_url: str
    canonical_slug: str
    canonical_score: int
    duplicate_count: int
    alternates: list[str]
    records: list[SourceRecord]


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def word_count(text: str) -> int:
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", r"\2 \1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣_.,:%/$+-]*", text))


def int_value(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def score_source(slug: str, meta: dict[str, Any], body_words: int) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    title = str(meta.get("title") or slug)
    source_type = str(meta.get("source_type") or "")
    raw_path = str(meta.get("raw_path") or "")
    text_status = str(meta.get("text_status") or "")
    content_hash = str(meta.get("content_hash") or "")
    meta_word_count = int_value(meta.get("word_count"))
    pages_updated = len(as_list(meta.get("pages_updated")))

    if raw_path and (ROOT / raw_path).exists():
        score += 35
        reasons.append("raw_path_exists")
    elif raw_path:
        score += 12
        reasons.append("raw_path_declared")

    if text_status == "parsed":
        score += 25
        reasons.append("parsed_text")

    if content_hash:
        score += 10
        reasons.append("content_hash")

    if source_type in {"press-release", "court-document", "government-page", "legal-text"}:
        score += 12
        reasons.append(f"type:{source_type}")
    elif source_type:
        score += 5
        reasons.append(f"type:{source_type}")

    if pages_updated:
        score += min(20, pages_updated * 4)
        reasons.append(f"pages_updated:{pages_updated}")

    if meta_word_count:
        bonus = min(45, meta_word_count // 80)
        score += bonus
        reasons.append(f"word_count:{meta_word_count}")

    if body_words:
        bonus = min(35, body_words // 35)
        score += bonus
        reasons.append(f"source_page_words:{body_words}")

    title_lower = title.lower()
    slug_lower = slug.lower()
    if "page not found" in title_lower:
        score -= 35
        reasons.append("penalty:page_not_found_title")
    if "summary" in slug_lower:
        score -= 6
        reasons.append("penalty:summary_slug")
    if len(title) < 18:
        score -= 5
        reasons.append("penalty:short_title")

    return score, reasons


def load_sources() -> list[SourceRecord]:
    rows: list[SourceRecord] = []
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        collection_url = str(meta.get("collection_url") or "").strip()
        body_words = word_count(post.content or "")
        score, score_reasons = score_source(path.stem, meta, body_words)
        rows.append(
            SourceRecord(
                slug=path.stem,
                title=str(meta.get("title") or path.stem),
                publisher=str(meta.get("publisher") or ""),
                publish_date=str(meta.get("publish_date") or ""),
                collection_url=collection_url,
                source_type=str(meta.get("source_type") or ""),
                raw_path=str(meta.get("raw_path") or ""),
                text_status=str(meta.get("text_status") or ""),
                content_hash=str(meta.get("content_hash") or ""),
                pages_updated=len(as_list(meta.get("pages_updated"))),
                word_count=int_value(meta.get("word_count")),
                body_words=body_words,
                score=score,
                score_reasons=score_reasons,
            )
        )
    return rows


def build_groups(rows: list[SourceRecord]) -> list[CanonicalGroup]:
    buckets: dict[str, list[SourceRecord]] = defaultdict(list)
    for row in rows:
        if row.collection_url:
            buckets[row.collection_url].append(row)

    groups: list[CanonicalGroup] = []
    for url, members in buckets.items():
        if len(members) < 2:
            continue
        ranked = sorted(members, key=lambda row: (-row.score, -row.word_count, -row.body_words, row.slug))
        canonical = ranked[0]
        groups.append(
            CanonicalGroup(
                collection_url=url,
                canonical_slug=canonical.slug,
                canonical_score=canonical.score,
                duplicate_count=len(members),
                alternates=[row.slug for row in ranked[1:]],
                records=ranked,
            )
        )
    groups.sort(key=lambda group: (-group.duplicate_count, -group.canonical_score, group.collection_url))
    return groups


def write_json(groups: list[CanonicalGroup], path: Path) -> None:
    payload = {
        group.collection_url: {
            "canonical_slug": group.canonical_slug,
            "canonical_score": group.canonical_score,
            "duplicate_count": group.duplicate_count,
            "alternates": group.alternates,
            "records": [asdict(record) for record in group.records],
        }
        for group in groups
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(groups: list[CanonicalGroup], path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "collection_url",
                "duplicate_count",
                "canonical_slug",
                "canonical_score",
                "source_slug",
                "source_score",
                "publisher",
                "publish_date",
                "source_type",
                "word_count",
                "body_words",
                "score_reasons",
            ]
        )
        for group in groups:
            for record in group.records:
                writer.writerow(
                    [
                        group.collection_url,
                        group.duplicate_count,
                        group.canonical_slug,
                        group.canonical_score,
                        record.slug,
                        record.score,
                        record.publisher,
                        record.publish_date,
                        record.source_type,
                        record.word_count,
                        record.body_words,
                        "; ".join(record.score_reasons),
                    ]
                )


def render_report(rows: list[SourceRecord], groups: list[CanonicalGroup]) -> str:
    duplicate_sources = sorted({record.slug for group in groups for record in group.records})
    lines = [
        "---",
        "title: Source Canonical Map (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Canonical-source candidate map for duplicate source URLs."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This map selects a canonical candidate for each duplicated `collection_url`. Duplicate source pages are not deleted; alternates can stay addressable as `duplicate_of` aliases while operation/case reference lists avoid repeating the same URL.",
        "",
        f"- Source pages scanned: **{len(rows)}**",
        f"- Duplicate URL groups: **{len(groups)}**",
        f"- Source pages in duplicate URL groups: **{len(duplicate_sources)}**",
        "",
        "## Selection Rules",
        "",
        "- Prefer source pages with existing raw text, parsed status, content hash, and higher word count.",
        "- Prefer official/legal source types over generic or empty source records.",
        "- Penalize `Page not found` titles and low-information summary slugs.",
        "- Keep all alternates addressable; use `duplicate_of` metadata to separate preserved aliases from active duplicate records.",
        "",
        "## Top Canonical Groups",
        "",
        "| Rank | Count | Canonical | Score | URL | Alternates |",
        "|---:|---:|---|---:|---|---|",
    ]
    for idx, group in enumerate(groups[:100], 1):
        alternates = "<br>".join(f"[[{slug}]]" for slug in group.alternates[:12])
        if len(group.alternates) > 12:
            alternates += f"<br>... +{len(group.alternates) - 12} more"
        lines.append(
            f"| {idx} | {group.duplicate_count} | [[{group.canonical_slug}]] | {group.canonical_score} | {group.collection_url} | {alternates} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a canonical candidate map for duplicate source URLs.")
    parser.add_argument("--json", default="_workspace/source_canonical_map_2026-04-26.json")
    parser.add_argument("--csv", default="_workspace/source_canonical_map_2026-04-26.csv")
    parser.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    args = parser.parse_args()

    rows = load_sources()
    groups = build_groups(rows)
    json_path = ROOT / args.json
    csv_path = ROOT / args.csv
    report_path = ROOT / args.report
    json_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    write_json(groups, json_path)
    write_csv(groups, csv_path)
    report_path.write_text(render_report(rows, groups), encoding="utf-8")

    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")
    print(f"Source pages scanned: {len(rows)}")
    print(f"Duplicate URL groups: {len(groups)}")


if __name__ == "__main__":
    main()
