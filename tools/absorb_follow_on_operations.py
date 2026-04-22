from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
CASES_DIR = ROOT / "wiki" / "cases"
SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_CASE_DOCS_DIR = ROOT / "raw" / "case-documents"
TODAY = "2026-04-22"


def wikilink_slug(value: str) -> str:
    text = str(value).strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def humanize_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title()


def load_post(path: Path) -> tuple[Any, dict[str, Any]]:
    post = frontmatter.load(path)
    return post, post.metadata


def build_refs(source_slugs: list[str]) -> str:
    lines = [
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    row = 1
    for source_slug in source_slugs:
        path = SOURCES_DIR / f"{source_slug}.md"
        date_key = "publish_date"
        url_key = "collection_url"
        if not path.exists():
            path = RAW_CASE_DOCS_DIR / f"{source_slug}.md"
            date_key = "date_filed"
            url_key = "source_url"
        if not path.exists():
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        title = str(meta.get("title") or humanize_slug(source_slug))
        publisher = str(meta.get("publisher") or meta.get("court") or "Unknown")
        date = str(meta.get(date_key) or "Unknown")
        url = str(meta.get(url_key) or "")
        lines.append(f"| [{row}] | {title} | {publisher} | {date} | {url} |")
        row += 1
    return "\n".join(lines)


def should_absorb(meta: dict[str, Any]) -> bool:
    if str(meta.get("operation_role") or "") != "follow-on":
        return False
    if str(meta.get("status") or "") == "absorbed":
        return False
    related_cases = meta.get("related_cases") or []
    countries = meta.get("participating_countries") or []
    try:
        source_count = int(meta.get("source_count") or 0)
    except (ValueError, TypeError):
        source_count = 0
    return (
        isinstance(related_cases, list)
        and len(related_cases) == 1
        and isinstance(countries, list)
        and len(countries) == 1
        and source_count == 1
    )


def absorb_operation(path: Path, dry_run: bool = False) -> bool:
    post, meta = load_post(path)
    if not should_absorb(meta):
        return False

    related_cases = meta.get("related_cases") or []
    case_slug = wikilink_slug(related_cases[0])
    if not case_slug:
        return False
    case_path = CASES_DIR / f"{case_slug}.md"
    if not case_path.exists():
        return False

    sources = [wikilink_slug(s) for s in meta.get("sources", []) if wikilink_slug(s)]
    refs_table = build_refs(sources)
    if refs_table.count("\n") < 2:
        return False

    canonical = f"[[{case_slug}]]"
    summary = (
        f"This domestic-only U.S. follow-on record has been absorbed into the canonical case page "
        f"{canonical}. No visible cross-border mechanism is documented, so it is not treated as a "
        "separate international-cooperation operation."
    )

    meta["status"] = "absorbed"
    meta["summary"] = summary
    meta["updated"] = TODAY

    post.content = (
        "## Summary\n\n"
        f"{summary}\n\n"
        "## Canonical Record\n\n"
        f"- {canonical}\n\n"
        "## References\n\n"
        f"{refs_table}\n"
    )

    if not dry_run:
        path.write_text(frontmatter.dumps(post), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Absorb thin follow-on operation pages into case anchors.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of operations to rewrite.")
    parser.add_argument("--dry-run", action="store_true", help="Only report which pages would be changed.")
    args = parser.parse_args()

    changed = 0
    for path in sorted(OPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        if absorb_operation(path, dry_run=args.dry_run):
            print(path.stem)
            changed += 1
            if args.limit and changed >= args.limit:
                break

    print(f"changed={changed}")


if __name__ == "__main__":
    main()
