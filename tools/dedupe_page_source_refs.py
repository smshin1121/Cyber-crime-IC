from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter

from source_canonical_map import score_source, word_count


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
WORKSPACE = ROOT / "_workspace"


@dataclass(frozen=True)
class SourceMeta:
    slug: str
    title: str
    publisher: str
    publish_date: str
    collection_url: str
    score: int


@dataclass(frozen=True)
class PageChange:
    path: Path
    title: str
    original_count: int
    deduped_count: int
    removed_sources: list[str]
    kept_sources: list[str]


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


def wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def source_meta(slug: str) -> SourceMeta:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return SourceMeta(slug, slug, "", "", "", -1000)
    post = frontmatter.load(path)
    meta = post.metadata
    score, _ = score_source(slug, meta, word_count(post.content or ""))
    return SourceMeta(
        slug=slug,
        title=str(meta.get("title") or slug),
        publisher=str(meta.get("publisher") or meta.get("collection_domain") or ""),
        publish_date=str(meta.get("publish_date") or ""),
        collection_url=str(meta.get("collection_url") or "").strip(),
        score=score,
    )


def escape_cell(value: str) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def render_references(sources: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(sources, 1):
        meta = source_meta(slug)
        url = meta.collection_url or f"[[{slug}]]"
        lines.append(
            f"| [{idx}] | {escape_cell(meta.title)} | {escape_cell(meta.publisher)} | {escape_cell(meta.publish_date)} | {escape_cell(url)} |"
        )
    return "\n".join(lines) + "\n"


def replace_references(body: str, sources: list[str]) -> str:
    refs = render_references(sources)
    match = re.search(r"^## References\s*$", body, re.M)
    if not match:
        body = body.rstrip() + "\n\n"
        return body + refs
    return body[: match.start()].rstrip() + "\n\n" + refs


def dedupe_sources(source_values: list[Any]) -> tuple[list[str], list[str]]:
    slugs = [wikilink_slug(item) for item in source_values]
    slugs = [slug for slug in slugs if slug]
    buckets: dict[str, list[SourceMeta]] = defaultdict(list)
    ordered_keys: list[str] = []

    for slug in slugs:
        meta = source_meta(slug)
        key = meta.collection_url or f"slug:{slug}"
        if key not in buckets:
            ordered_keys.append(key)
        buckets[key].append(meta)

    kept: list[str] = []
    removed: list[str] = []
    for key in ordered_keys:
        members = buckets[key]
        if len(members) == 1:
            kept.append(members[0].slug)
            continue
        ranked = sorted(members, key=lambda item: (-item.score, item.slug))
        kept.append(ranked[0].slug)
        removed.extend(item.slug for item in ranked[1:])
    return kept, removed


def page_paths() -> list[Path]:
    paths: list[Path] = []
    for directory in (WIKI_DIR / "operations", WIKI_DIR / "cases"):
        paths.extend(path for path in sorted(directory.glob("*.md")) if not path.name.startswith("_"))
    return paths


def process_page(path: Path, apply: bool) -> PageChange | None:
    post = frontmatter.load(path)
    meta = post.metadata
    source_values = as_list(meta.get("sources"))
    if len(source_values) < 2:
        return None

    kept, removed = dedupe_sources(source_values)
    if not removed:
        return None

    if apply:
        meta["sources"] = [wikilink(slug) for slug in kept]
        meta["source_count"] = len(kept)
        post.metadata = meta
        post.content = replace_references(post.content or "", kept)
        path.write_text(frontmatter.dumps(post), encoding="utf-8")

    return PageChange(
        path=path,
        title=str(meta.get("title") or path.stem),
        original_count=len(source_values),
        deduped_count=len(kept),
        removed_sources=removed,
        kept_sources=kept,
    )


def write_report(changes: list[PageChange]) -> Path:
    path = WORKSPACE / "page_source_ref_dedupe_2026-04-26.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["page", "title", "original_count", "deduped_count", "removed_sources", "kept_sources"])
        for change in changes:
            writer.writerow(
                [
                    str(change.path.relative_to(ROOT)).replace("\\", "/"),
                    change.title,
                    change.original_count,
                    change.deduped_count,
                    "; ".join(change.removed_sources),
                    "; ".join(change.kept_sources),
                ]
            )
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove repeated same-URL source references inside operation/case pages.")
    parser.add_argument("--apply", action="store_true", help="Write changes. Omit for dry-run.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of pages to modify/report.")
    args = parser.parse_args()

    changes: list[PageChange] = []
    for path in page_paths():
        change = process_page(path, apply=args.apply)
        if not change:
            continue
        changes.append(change)
        if args.limit and len(changes) >= args.limit:
            break

    report_path = write_report(changes)
    mode = "applied" if args.apply else "dry-run"
    print(f"Mode: {mode}")
    print(f"Pages with repeated source URLs: {len(changes)}")
    print(f"Report: {report_path}")
    for change in changes[:20]:
        rel = change.path.relative_to(ROOT)
        print(f"- {rel}: {change.original_count} -> {change.deduped_count}; removed {', '.join(change.removed_sources)}")


if __name__ == "__main__":
    main()
