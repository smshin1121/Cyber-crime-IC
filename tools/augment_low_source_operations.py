from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
SOURCES_DIR = ROOT / "wiki" / "sources"
TARGETS_FILE = Path(__file__).resolve().parent / "_low_source65.txt"


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def ensure_wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def load_targets() -> list[str]:
    return [
        line.strip()
        for line in TARGETS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def collect_source_matches(targets: set[str]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {slug: [] for slug in targets}
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        pages = post.metadata.get("pages_updated") or []
        if isinstance(pages, str):
            pages = [pages]
        for page in pages:
            slug = str(page).strip()
            if slug in targets and path.stem not in mapping[slug]:
                mapping[slug].append(path.stem)
    return mapping


def parse_existing_sources(meta: dict[str, Any]) -> list[str]:
    values = meta.get("sources") or []
    if isinstance(values, str):
        values = [values]
    slugs: list[str] = []
    for value in values:
        text = str(value or "").strip()
        slug = wikilink_slug(text)
        if slug and (SOURCES_DIR / f"{slug}.md").exists():
            slugs.append(slug)
    return slugs


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output


def build_references_table(source_slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(source_slugs, start=1):
        path = SOURCES_DIR / f"{slug}.md"
        if not path.exists():
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        title = str(meta.get("title") or slug.replace("-", " ").title()).replace("|", " ")
        publisher = str(meta.get("publisher") or "Unknown").replace("|", " ")
        date = str(meta.get("publish_date") or "Unknown").replace("|", " ")
        url = str(meta.get("collection_url") or "").strip().replace("|", "%7C")
        lines.append(f"| [{idx}] | {title} | {publisher} | {date} | {url} |")
    return "\n".join(lines) + "\n"


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


def main() -> None:
    targets = load_targets()
    target_set = set(targets)
    matches = collect_source_matches(target_set)

    updated = 0
    reached_five = 0

    for slug in targets:
        op_path = OPS_DIR / f"{slug}.md"
        if not op_path.exists():
            continue
        post = frontmatter.load(op_path)
        meta = post.metadata
        existing = parse_existing_sources(meta)
        combined = unique(existing + matches.get(slug, []))
        if not combined:
            continue

        before_count = int(meta.get("source_count") or 0)
        before_sources = list(meta.get("sources") or [])
        before_content = post.content

        meta["sources"] = [ensure_wikilink(s) for s in combined]
        meta["source_count"] = len(combined)
        post.content = replace_references_section(post.content, build_references_table(combined))

        if (
            before_count != meta["source_count"]
            or before_sources != meta["sources"]
            or before_content != post.content
        ):
            op_path.write_text(frontmatter.dumps(post), encoding="utf-8")
            updated += 1
            if before_count < 5 and len(combined) >= 5:
                reached_five += 1
            print(f"{slug}: {before_count} -> {len(combined)}")

    print(f"UPDATED {updated}")
    print(f"REACHED_FIVE {reached_five}")


if __name__ == "__main__":
    main()
