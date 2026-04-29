from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
WORKSPACE = ROOT / "_workspace"
DEFAULT_DATE = date.today().isoformat()


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


def normalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(url.strip())
    query_pairs = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        low = key.lower()
        if low.startswith("utm_") or low in {"fbclid", "gclid", "ref", "source"}:
            continue
        query_pairs.append((key, value))
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), host, path, urlencode(query_pairs), ""))


def write_csv(rows: list[SourceRow], run_date: str) -> Path:
    path = WORKSPACE / f"source_duplicate_audit_{run_date}.csv"
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


def render_report(rows: list[SourceRow], run_date: str) -> str:
    all_url_dupes = grouped(rows, "collection_url")
    all_hash_dupes = grouped(rows, "content_hash")
    active_rows = [row for row in rows if not row.duplicate_of]
    active_url_dupes = grouped(active_rows, "collection_url")
    active_hash_review = grouped(active_rows, "content_hash")
    active_hash_dupes = [
        (content_hash, members)
        for content_hash, members in active_hash_review
        if len({normalize_url(row.collection_url) for row in members if row.collection_url}) <= 1
    ]
    review_hash_only = [
        (content_hash, members)
        for content_hash, members in active_hash_review
        if len({normalize_url(row.collection_url) for row in members if row.collection_url}) > 1
    ]
    active_duplicate_pages = sorted({row.slug for _, members in active_url_dupes + active_hash_dupes for row in members})
    alias_rows = [row for row in rows if row.duplicate_of]
    alias_url_groups = grouped(alias_rows, "collection_url")

    lines = [
        "---",
        f"title: Source Duplicate Audit ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
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
        f"- Active duplicate content-hash groups after URL normalization: **{len(active_hash_dupes)}**",
        f"- Review-only identical content-hash groups with distinct URLs: **{len(review_hash_only)}**",
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

    lines.extend(["", "## Review-Only Content-Hash Groups With Distinct URLs", "", "| Rank | Count | Hash | Source pages |", "|---:|---:|---|---|"])
    for idx, (content_hash, members) in enumerate(review_hash_only[:100], 1):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=DEFAULT_DATE)
    args = parser.parse_args()
    rows = load_sources()
    csv_path = write_csv(rows, args.date)
    report_path = ROOT / "wiki" / "analysis" / f"source-duplicate-audit-{args.date}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(rows, args.date), encoding="utf-8")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")
    print(f"Sources audited: {len(rows)}")
    active_rows = [row for row in rows if not row.duplicate_of]
    active_hash_review = grouped(active_rows, "content_hash")
    active_hash_dupes = [
        (content_hash, members)
        for content_hash, members in active_hash_review
        if len({normalize_url(row.collection_url) for row in members if row.collection_url}) <= 1
    ]
    print(f"Alias-marked source pages: {len(rows) - len(active_rows)}")
    print(f"Active duplicate URL groups: {len(grouped(active_rows, 'collection_url'))}")
    print(f"Active duplicate content-hash groups: {len(active_hash_dupes)}")
    print(f"Review-only content-hash groups: {len(active_hash_review) - len(active_hash_dupes)}")


if __name__ == "__main__":
    main()
