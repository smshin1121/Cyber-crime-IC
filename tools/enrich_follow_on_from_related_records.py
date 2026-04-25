from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
CASES_DIR = ROOT / "wiki" / "cases"
SOURCES_DIR = ROOT / "wiki" / "sources"


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


def ensure_wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def parse_sources(meta: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for value in as_list(meta.get("sources")):
        slug = wikilink_slug(value)
        if slug:
            out.append(slug)
    return out


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def normalize_url(url: str) -> str:
    text = str(url or "").strip()
    if not text:
        return ""
    parts = urlsplit(text)
    return f"{parts.scheme}://{parts.netloc}{parts.path}"


def source_meta(slug: str) -> dict[str, Any] | None:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return None
    try:
        return dict(frontmatter.load(path).metadata)
    except Exception:
        return None


def build_references_table(source_slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(source_slugs, start=1):
        meta = source_meta(slug)
        if not meta:
            continue
        title = str(meta.get("title") or slug.replace("-", " ").title()).replace("|", " ")
        publisher = str(meta.get("publisher") or "Unknown").replace("|", " ")
        publish_date = str(meta.get("publish_date") or "Unknown").replace("|", " ")
        url = str(meta.get("collection_url") or meta.get("source_url") or "").replace("|", "%7C")
        lines.append(f"| [{idx}] | {title} | {publisher} | {publish_date} | {url} |")
    return "\n".join(lines) + "\n"


def dedupe_source_slugs(source_slugs: list[str]) -> list[str]:
    seen_urls: set[str] = set()
    seen_slugs: set[str] = set()
    out: list[str] = []
    for slug in source_slugs:
        if slug in seen_slugs:
            continue
        meta = source_meta(slug)
        url = normalize_url((meta or {}).get("collection_url") or (meta or {}).get("source_url") or "")
        if url and url in seen_urls:
            continue
        seen_slugs.add(slug)
        if url:
            seen_urls.add(url)
        out.append(slug)
    return out


def replace_references_section(content: str, table: str) -> str:
    marker = "\n## References"
    idx = content.find(marker)
    if idx != -1:
        return content[:idx].rstrip() + "\n\n" + table.rstrip() + "\n"
    if content.startswith("## References"):
        return table.rstrip() + "\n"
    pattern = re.compile(r"\n## References\s*$.*", re.DOTALL)
    if pattern.search(content):
        return pattern.sub("\n" + table.rstrip() + "\n", content).rstrip() + "\n"
    return content.rstrip() + "\n\n" + table


def related_case_sources(meta: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for value in as_list(meta.get("related_cases")):
        slug = wikilink_slug(value)
        if not slug:
            continue
        path = CASES_DIR / f"{slug}.md"
        if not path.exists():
            continue
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        out.extend(parse_sources(post.metadata))
    return out


def parent_operation_sources(meta: dict[str, Any]) -> list[str]:
    slug = wikilink_slug(meta.get("parent_operation"))
    if not slug:
        return []
    path = OPS_DIR / f"{slug}.md"
    if not path.exists():
        return []
    try:
        post = frontmatter.load(path)
    except Exception:
        return []
    return parse_sources(post.metadata)


def main() -> None:
    updated = 0
    reached_five = 0
    raised_some = 0

    for path in sorted(OPS_DIR.glob("*.md")):
        if path.stem == "_index":
            continue

        post = frontmatter.load(path)
        meta = post.metadata
        current_count = int(meta.get("source_count") or 0)
        if current_count != 1:
            continue

        existing = parse_sources(meta)
        inherited = related_case_sources(meta) + parent_operation_sources(meta)
        combined = dedupe_source_slugs(unique(existing + inherited))
        if len(combined) <= len(existing):
            continue

        meta["sources"] = [ensure_wikilink(slug) for slug in combined]
        meta["source_count"] = len(combined)
        post.content = replace_references_section(post.content, build_references_table(combined))
        path.write_text(frontmatter.dumps(post), encoding="utf-8")

        updated += 1
        if len(combined) >= 5:
            reached_five += 1
        else:
            raised_some += 1
        print(f"{path.stem}: {current_count} -> {len(combined)}")

    print(f"UPDATED {updated}")
    print(f"REACHED_FIVE {reached_five}")
    print(f"RAISED_SOME {raised_some}")


if __name__ == "__main__":
    main()
