from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = ROOT / "wiki" / "analysis" / "source-duplicate-audit-2026-04-26.md"


@dataclass(frozen=True)
class SourceRow:
    slug: str
    title: str
    publisher: str
    publish_date: str
    collection_url: str
    content_hash: str
    raw_path: str
    duplicate_of: str
    duplicate_reason: str


def load_sources() -> list[SourceRow]:
    rows: list[SourceRow] = []
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        rows.append(
            SourceRow(
                slug=path.stem,
                title=str(meta.get("title") or path.stem),
                publisher=str(meta.get("publisher") or ""),
                publish_date=str(meta.get("publish_date") or ""),
                collection_url=str(meta.get("collection_url") or "").strip(),
                content_hash=str(meta.get("content_hash") or "").strip(),
                raw_path=str(meta.get("raw_path") or "").strip(),
                duplicate_of=str(meta.get("duplicate_of") or "").strip(),
                duplicate_reason=str(meta.get("duplicate_reason") or "").strip(),
            )
        )
    return rows


def grouped(rows: list[SourceRow], field: str) -> list[tuple[str, list[SourceRow]]]:
    buckets: dict[str, list[SourceRow]] = defaultdict(list)
    for row in rows:
        value = getattr(row, field)
        if value:
            buckets[value].append(row)
    return sorted(
        ((value, members) for value, members in buckets.items() if len(members) > 1),
        key=lambda item: (-len(item[1]), item[0]),
    )


def write_csv(rows: list[SourceRow]) -> Path:
    path = WORKSPACE / "source_duplicate_audit_2026-04-26.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "slug",
                "title",
                "publisher",
                "publish_date",
                "collection_url",
                "content_hash",
                "raw_path",
                "duplicate_of",
                "duplicate_reason",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.slug,
                    row.title,
                    row.publisher,
                    row.publish_date,
                    row.collection_url,
                    row.content_hash,
                    row.raw_path,
                    row.duplicate_of,
                    row.duplicate_reason,
                ]
            )
    return path


def render_report(rows: list[SourceRow]) -> str:
    all_url_dupes = grouped(rows, "collection_url")
    all_hash_dupes = grouped(rows, "content_hash")
    active_rows = [row for row in rows if not row.duplicate_of]
    active_url_dupes = grouped(active_rows, "collection_url")
    active_hash_dupes = grouped(active_rows, "content_hash")
    active_duplicate_pages = sorted({row.slug for _, members in active_url_dupes + active_hash_dupes for row in members})
    alias_rows = [row for row in rows if row.duplicate_of]
    alias_url_groups = grouped(alias_rows, "collection_url")

    lines = [
        "---",
        "title: Source Duplicate Audit (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Audit of duplicate source records by collection URL and content hash."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This audit checks whether multiple `wiki/sources` pages point to the same original URL or fetched content. Pages marked with `duplicate_of` are preserved aliases and are separated from active unresolved duplicates.",
        "",
        f"- Source pages audited: **{len(rows)}**",
        f"- Alias-marked source pages: **{len(alias_rows)}**",
        f"- Total duplicate URL groups including aliases: **{len(all_url_dupes)}**",
        f"- Active duplicate URL groups: **{len(active_url_dupes)}**",
        f"- Total duplicate content-hash groups including aliases: **{len(all_hash_dupes)}**",
        f"- Active duplicate content-hash groups: **{len(active_hash_dupes)}**",
        f"- Active source pages in at least one unresolved duplicate group: **{len(active_duplicate_pages)}**",
        "",
        "## Active Duplicate URL Groups",
        "",
        "| Rank | Count | URL | Source pages |",
        "|---:|---:|---|---|",
    ]

    for idx, (url, members) in enumerate(active_url_dupes[:100], 1):
        pages = "<br>".join(f"[[{row.slug}]]" for row in members[:20])
        if len(members) > 20:
            pages += f"<br>... +{len(members) - 20} more"
        lines.append(f"| {idx} | {len(members)} | {url} | {pages} |")

    lines.extend(["", "## Active Duplicate Content-Hash Groups", "", "| Rank | Count | Hash | Source pages |", "|---:|---:|---|---|"])
    for idx, (content_hash, members) in enumerate(active_hash_dupes[:100], 1):
        pages = "<br>".join(f"[[{row.slug}]]" for row in members[:20])
        if len(members) > 20:
            pages += f"<br>... +{len(members) - 20} more"
        lines.append(f"| {idx} | {len(members)} | `{content_hash}` | {pages} |")

    lines.extend(["", "## Preserved Alias URL Groups", "", "| Rank | Count | URL | Alias pages |", "|---:|---:|---|---|"])
    for idx, (url, members) in enumerate(alias_url_groups[:100], 1):
        pages = "<br>".join(f"[[{row.slug}]] -> {row.duplicate_of}" for row in members[:20])
        if len(members) > 20:
            pages += f"<br>... +{len(members) - 20} more"
        lines.append(f"| {idx} | {len(members)} | {url} | {pages} |")

    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_sources()
    csv_path = write_csv(rows)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(rows), encoding="utf-8")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORT_PATH}")
    print(f"Sources audited: {len(rows)}")
    active_rows = [row for row in rows if not row.duplicate_of]
    print(f"Alias-marked source pages: {len(rows) - len(active_rows)}")
    print(f"Active duplicate URL groups: {len(grouped(active_rows, 'collection_url'))}")
    print(f"Active duplicate content-hash groups: {len(grouped(active_rows, 'content_hash'))}")


if __name__ == "__main__":
    main()
