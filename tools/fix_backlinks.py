"""
Fix missing bidirectional backlinks on organization pages.
Scans all operations for participating_agencies and ensures
each org page lists the operation in operations_participated.
"""
from pathlib import Path

import frontmatter

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"


def fix_backlinks() -> int:
    """Add missing operations_participated entries to org pages."""
    ops_dir = WIKI_DIR / "operations"
    orgs_dir = WIKI_DIR / "organizations"

    if not ops_dir.is_dir() or not orgs_dir.is_dir():
        return 0

    # Load all org pages
    orgs: dict[str, Path] = {}
    for md in orgs_dir.glob("*.md"):
        if md.name.startswith("_"):
            continue
        orgs[md.stem] = md

    # Build mapping: org_slug -> set of operation slugs that reference it
    org_ops: dict[str, set[str]] = {slug: set() for slug in orgs}

    for md in ops_dir.glob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            meta = frontmatter.load(md).metadata
        except Exception:
            continue
        agencies = meta.get("participating_agencies", [])
        if not isinstance(agencies, list):
            continue
        for ref in agencies:
            slug = str(ref).strip("[]\"' ")
            if slug in org_ops:
                org_ops[slug].add(md.stem)

    # Update org pages
    fixed = 0
    for org_slug, expected_ops in org_ops.items():
        if not expected_ops:
            continue
        fp = orgs[org_slug]
        post = frontmatter.load(fp)
        existing = post.metadata.get("operations_participated", [])
        if not isinstance(existing, list):
            existing = []

        existing_slugs = {str(s).strip("[]\"' ") for s in existing}
        missing = expected_ops - existing_slugs

        if missing:
            new_list = sorted(
                existing_slugs | expected_ops,
                key=lambda s: s,
            )
            post.metadata["operations_participated"] = [
                f"[[{s}]]" for s in new_list
            ]
            post.metadata["updated"] = "2026-04-09"
            fp.write_text(frontmatter.dumps(post), encoding="utf-8")
            fixed += len(missing)
            print(f"  {org_slug}: +{len(missing)} backlinks"
                  f" (total {len(new_list)})")

    return fixed


def main() -> None:
    print("=" * 60)
    print("  Fix Bidirectional Backlinks")
    print("=" * 60)
    total = fix_backlinks()
    print(f"\n  Total backlinks added: {total}")
    print("Done.")


if __name__ == "__main__":
    main()
