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
        writer.writerow(["slug", "title", "publisher", "publish_date", "collection_url", "content_hash", "raw_path"])
        for row in rows:
            writer.writerow([row.slug, row.title, row.publisher, row.publish_date, row.collection_url, row.content_hash, row.raw_path])
    return path


def render_report(rows: list[SourceRow]) -> str:
    url_dupes = grouped(rows, "collection_url")
    hash_dupes = grouped(rows, "content_hash")
    duplicate_source_pages = sorted({row.slug for _, members in url_dupes + hash_dupes for row in members})

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
        "This audit checks whether multiple `wiki/sources` pages point to the same original URL or fetched content. Duplicate source pages are not always wrong, but operation and case pages should not repeat the same URL as separate references unless the duplicated pages contain distinct extracted facts that are intentionally modeled.",
        "",
        f"- Source pages audited: **{len(rows)}**",
        f"- Duplicate URL groups: **{len(url_dupes)}**",
        f"- Duplicate content-hash groups: **{len(hash_dupes)}**",
        f"- Source pages in at least one duplicate group: **{len(duplicate_source_pages)}**",
        "",
        "## Top Duplicate URL Groups",
        "",
        "| Rank | Count | URL | Source pages |",
        "|---:|---:|---|---|",
    ]

    for idx, (url, members) in enumerate(url_dupes[:100], 1):
        pages = "<br>".join(f"[[{row.slug}]]" for row in members[:20])
        if len(members) > 20:
            pages += f"<br>... +{len(members) - 20} more"
        lines.append(f"| {idx} | {len(members)} | {url} | {pages} |")

    lines.extend(["", "## Top Duplicate Content-Hash Groups", "", "| Rank | Count | Hash | Source pages |", "|---:|---:|---|---|"])
    for idx, (content_hash, members) in enumerate(hash_dupes[:100], 1):
        pages = "<br>".join(f"[[{row.slug}]]" for row in members[:20])
        if len(members) > 20:
            pages += f"<br>... +{len(members) - 20} more"
        lines.append(f"| {idx} | {len(members)} | `{content_hash}` | {pages} |")

    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_sources()
    csv_path = write_csv(rows)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(rows), encoding="utf-8")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORT_PATH}")
    print(f"Sources audited: {len(rows)}")
    print(f"Duplicate URL groups: {len(grouped(rows, 'collection_url'))}")
    print(f"Duplicate content-hash groups: {len(grouped(rows, 'content_hash'))}")


if __name__ == "__main__":
    main()
