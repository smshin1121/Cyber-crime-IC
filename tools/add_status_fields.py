"""
Bulk-add status and last_verified fields to all organization pages
that lack them, to conform to the extended schema.
Preserves all existing content and frontmatter fields.
"""
from pathlib import Path

import frontmatter

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TODAY = "2026-04-10"


def main() -> None:
    org_dir = WIKI / "organizations"
    country_dir = WIKI / "countries"
    changed = 0
    for md in list(org_dir.glob("*.md")) + list(country_dir.glob("*.md")):
        if md.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(md)
        except Exception as e:
            print(f"  skip (parse error) {md.name}: {e}")
            continue
        dirty = False
        # Organizations: add status + last_verified if missing
        if md.parent.name == "organizations":
            if "status" not in post.metadata:
                post.metadata["status"] = "active"
                dirty = True
            if "last_verified" not in post.metadata:
                post.metadata["last_verified"] = TODAY
                dirty = True
        else:
            # Countries: add last_verified only
            if "last_verified" not in post.metadata:
                post.metadata["last_verified"] = TODAY
                dirty = True
        if dirty:
            md.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
            changed += 1
    print(f"Added status/last_verified to {changed} files")


if __name__ == "__main__":
    main()
