#!/usr/bin/env python3
"""Normalize operation frontmatter source links to resolvable source slugs.

Some older operation pages used human citation labels in `sources` instead of
`wiki/sources` slugs. This tool keeps existing valid source-page links and uses
References-table URLs to recover resolvable source slugs where possible.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
OPS_DIR = ROOT / "wiki" / "operations"
SOURCES_DIR = ROOT / "wiki" / "sources"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
SOURCE_BLOCK_RE = re.compile(r"(?m)^sources:\n(?:^[ \t]+-\s.*(?:\n|$))*")
SOURCE_COUNT_RE = re.compile(r"(?m)^source_count:\s*.*$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REF_ROW_RE = re.compile(r"(?m)^\|\s*\[\d+\]\s*\|(?P<row>.*)$")


def clean(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.replace('\\"', '"').replace("\\'", "'").strip()


def normalize_url(url: str) -> str:
    text = clean(url)
    if not text or text == "?":
        return ""
    parts = urlsplit(text)
    if not parts.scheme or not parts.netloc:
        return text.rstrip("/")
    return f"{parts.scheme.lower()}://{parts.netloc.lower()}{parts.path.rstrip('/')}"


def escape_cell(value: str) -> str:
    return " ".join((value or "?").split()).replace("|", "\\|")


def read_frontmatter(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text, text
    return match.group(1), text[match.end():], text


def flat_frontmatter(path: Path) -> dict[str, str]:
    fm, _, _ = read_frontmatter(path)
    data: dict[str, str] = {}
    for line in fm.splitlines():
        if not line or line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = clean(value)
    return data


def source_index() -> tuple[set[str], dict[str, str], dict[str, dict[str, str]]]:
    slugs: set[str] = set()
    by_url: dict[str, str] = {}
    meta_by_slug: dict[str, dict[str, str]] = {}
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name == "_index.md":
            continue
        slug = path.stem
        slugs.add(slug)
        meta = flat_frontmatter(path)
        meta_by_slug[slug] = meta
        for key in ("collection_url", "source_url", "url", "attribution_url"):
            url = normalize_url(meta.get(key, ""))
            if url and url not in by_url:
                by_url[url] = slug
    return slugs, by_url, meta_by_slug


def existing_source_slugs(fm: str, valid_slugs: set[str]) -> list[str]:
    match = SOURCE_BLOCK_RE.search(fm)
    if not match:
        return []
    out: list[str] = []
    for line in match.group(0).splitlines()[1:]:
        item = line.split("-", 1)[-1].strip()
        link = WIKILINK_RE.search(item)
        slug = link.group(1).strip() if link else clean(item)
        if slug in valid_slugs and slug not in out:
            out.append(slug)
    return out


def reference_urls(body: str) -> list[str]:
    if "## References" not in body:
        return []
    tail = body.split("## References", 1)[1]
    next_heading = re.search(r"^##\s+", tail, re.M)
    if next_heading:
        tail = tail[: next_heading.start()]
    urls: list[str] = []
    for match in REF_ROW_RE.finditer(tail):
        cells = [cell.strip() for cell in match.group(0).strip().strip("|").split("|")]
        if len(cells) >= 5:
            urls.append(normalize_url(cells[-1]))
    return [url for url in urls if url]


def render_sources_block(slugs: list[str]) -> str:
    if not slugs:
        return "sources:\n"
    lines = ["sources:"]
    lines.extend(f'  - "[[{slug}]]"' for slug in slugs)
    return "\n".join(lines) + "\n"


def source_row(index: int, slug: str, meta_by_slug: dict[str, dict[str, str]]) -> str:
    meta = meta_by_slug.get(slug, {})
    title = meta.get("title") or slug
    publisher = meta.get("publisher") or "?"
    date = meta.get("publish_date") or meta.get("date") or meta.get("created") or "?"
    url = (
        meta.get("collection_url")
        or meta.get("source_url")
        or meta.get("url")
        or meta.get("attribution_url")
        or "?"
    )
    return (
        f"| [{index}] | {escape_cell(title)} | {escape_cell(publisher)} | "
        f"{escape_cell(date)} | {escape_cell(url)} |"
    )


def render_references(slugs: list[str], meta_by_slug: dict[str, dict[str, str]]) -> str:
    rows = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    rows.extend(source_row(index, slug, meta_by_slug) for index, slug in enumerate(slugs, 1))
    return "\n".join(rows).rstrip() + "\n"


def replace_references(body: str, refs: str) -> str:
    marker = "\n## References"
    pos = body.find(marker)
    if pos == -1:
        if body.startswith("## References"):
            start = 0
        else:
            return body.rstrip() + "\n\n" + refs
    else:
        start = pos + 1
    next_heading = re.search(r"\n## (?!References\b)", body[start + 1 :])
    if next_heading:
        end = start + 1 + next_heading.start()
        return body[:start] + refs.rstrip() + "\n" + body[end:]
    return body[:start] + refs


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def slug_url(slug: str, meta_by_slug: dict[str, dict[str, str]]) -> str:
    meta = meta_by_slug.get(slug, {})
    return normalize_url(
        meta.get("collection_url")
        or meta.get("source_url")
        or meta.get("url")
        or meta.get("attribution_url")
        or ""
    )


def unique_by_slug_and_url(items: list[str], meta_by_slug: dict[str, dict[str, str]]) -> list[str]:
    seen_slugs: set[str] = set()
    seen_urls: set[str] = set()
    out: list[str] = []
    for item in items:
        if not item or item in seen_slugs:
            continue
        url = slug_url(item, meta_by_slug)
        if url and url in seen_urls:
            continue
        seen_slugs.add(item)
        if url:
            seen_urls.add(url)
        out.append(item)
    return out


def normalize_file(
    path: Path,
    valid_slugs: set[str],
    by_url: dict[str, str],
    meta_by_slug: dict[str, dict[str, str]],
    dry_run: bool,
) -> bool:
    fm, body, original = read_frontmatter(path)
    if not fm:
        return False
    slugs = existing_source_slugs(fm, valid_slugs)
    for url in reference_urls(body):
        slug = by_url.get(url)
        if slug:
            slugs.append(slug)
    slugs = unique_by_slug_and_url(unique(slugs), meta_by_slug)
    new_fm = SOURCE_COUNT_RE.sub(f"source_count: {len(slugs)}", fm)
    if SOURCE_BLOCK_RE.search(new_fm):
        new_fm = SOURCE_BLOCK_RE.sub(render_sources_block(slugs), new_fm)
    else:
        new_fm = new_fm.rstrip() + "\n" + render_sources_block(slugs).rstrip()
    new_body = replace_references(body, render_references(slugs, meta_by_slug)) if slugs else body
    updated = "---\n" + new_fm.rstrip() + "\n---\n" + new_body.lstrip()
    if updated == original:
        return False
    if not dry_run:
        path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Operation files to normalize; defaults to all operations.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    valid_slugs, by_url, meta_by_slug = source_index()
    paths = [ROOT / item for item in args.paths] if args.paths else sorted(OPS_DIR.glob("*.md"))
    changed: list[str] = []
    for path in paths:
        if path.name == "_index.md":
            continue
        if normalize_file(path, valid_slugs, by_url, meta_by_slug, args.dry_run):
            changed.append(path.relative_to(ROOT).as_posix())
    for path in changed:
        print(path)
    print(f"{'would update' if args.dry_run else 'updated'}: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
