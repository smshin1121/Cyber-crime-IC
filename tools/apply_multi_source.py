"""
Apply multi-source CI recalculation and add all source URLs to References.
Reads multi_source_map.json and patches wiki operation pages.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
WIKI_OPS = PROJECT / "wiki" / "operations"
MAP_FILE = PROJECT / "_workspace" / "multi_source_map.json"


def slugify(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:60].strip("-")


def find_operation_file(op_name: str) -> Path | None:
    """Try to find the wiki operation file matching an operation name."""
    slug = slugify(op_name)
    # Direct match
    candidate = WIKI_OPS / f"{slug}.md"
    if candidate.exists():
        return candidate
    # Try with 'operation-' prefix
    candidate = WIKI_OPS / f"operation-{slug}.md"
    if candidate.exists():
        return candidate
    # Fuzzy match: search all files
    words = [w for w in slug.split("-") if len(w) > 3]
    if not words:
        return None
    for f in WIKI_OPS.glob("*.md"):
        if f.name.startswith("_"):
            continue
        fname = f.stem.lower()
        if any(w in fname for w in words):
            return f
    return None


def update_ci_in_frontmatter(content: str, new_ci: float) -> str:
    """Update credibility_index in YAML frontmatter."""
    return re.sub(
        r"(credibility_index:\s*)\S+",
        f"\\g<1>{new_ci}",
        content,
    )


def update_references(content: str, urls: list[str]) -> str:
    """Add all source URLs to the References table."""
    if not urls:
        return content

    # Build new references table
    ref_rows = []
    for i, url in enumerate(urls, 1):
        # Extract domain for publisher name
        domain = re.search(r"https?://(?:www\.)?([^/]+)", url)
        publisher = domain.group(1) if domain else "Unknown"
        ref_rows.append(
            f"| [{i}] | Source {i} | {publisher} | - | [원본]({url}) |"
        )

    new_table = (
        "## References\n\n"
        "| # | Title | Publisher | Date | URL |\n"
        "|---|-------|----------|------|-----|\n"
        + "\n".join(ref_rows)
    )

    # Replace existing References section or append
    if "## References" in content:
        content = re.sub(
            r"## References.*",
            new_table,
            content,
            flags=re.DOTALL,
        )
    else:
        content = content.rstrip() + "\n\n" + new_table + "\n"

    return content


def main() -> None:
    if not MAP_FILE.exists():
        print(f"ERROR: {MAP_FILE} not found")
        sys.exit(1)

    with open(MAP_FILE, encoding="utf-8") as f:
        ops = json.load(f)

    # Only process operations with 2+ sources (CI improvement candidates)
    multi_source = [o for o in ops if o["num_sources"] > 1]
    print(f"Operations with 2+ sources: {len(multi_source)}")

    updated = 0
    not_found = 0

    for op in multi_source:
        name = op["operation_name"]
        filepath = find_operation_file(name)

        if not filepath:
            not_found += 1
            continue

        content = filepath.read_text(encoding="utf-8")
        original = content

        # Update CI
        content = update_ci_in_frontmatter(content, op["ci"])

        # Update References with all URLs
        content = update_references(content, op["urls"])

        if content != original:
            filepath.write_text(content, encoding="utf-8")
            updated += 1
            print(f"  UPDATED {filepath.name}: CI={op['ci']} ({op['num_sources']} sources)")

    print(f"\nDone. Updated: {updated}, Not found: {not_found}")


if __name__ == "__main__":
    main()
