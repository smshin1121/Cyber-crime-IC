"""
References cleanup tool — removes contaminated 'Supplementary source' entries
and fixes source_count mismatches in wiki operation pages.
"""
import re
from pathlib import Path

import frontmatter

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
OPS_DIR = WIKI_DIR / "operations"


def clean_supplementary_sources(filepath: Path) -> dict:
    """Remove 'Supplementary source' rows from References table and fix numbering."""
    post = frontmatter.load(filepath)
    content = post.content
    lines = content.split("\n")

    # Find the References table
    ref_start = None
    ref_header_end = None
    ref_lines = []
    non_ref_lines_before = []
    non_ref_lines_after = []
    in_ref_table = False
    table_ended = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Detect reference table start (header row with # | Title | ...)
        if not in_ref_table and re.match(r'\|\s*#\s*\|', stripped):
            ref_start = i
            in_ref_table = True
            non_ref_lines_before = lines[:i]
            continue
        # Skip separator row
        if in_ref_table and ref_start is not None and ref_header_end is None:
            if re.match(r'\|[-\s|]+\|', stripped):
                ref_header_end = i
                continue
        # Collect reference rows
        if in_ref_table and ref_header_end is not None:
            if stripped.startswith("|") and "|" in stripped[1:]:
                ref_lines.append(line)
            else:
                table_ended = True
                non_ref_lines_after = lines[i:]
                break

    if not table_ended and in_ref_table:
        non_ref_lines_after = []

    if ref_start is None:
        return {"file": filepath.name, "action": "no_table", "removed": 0}

    # Filter out supplementary/contaminated rows
    clean_refs = []
    removed = 0
    for line in ref_lines:
        if "Supplementary source" in line or "Source 1 |" in line or "Source 2 |" in line:
            # Check if it's a generic "Source N" with no real title
            if "Supplementary source" in line:
                removed += 1
                continue
            # For "Source N" pattern, check if URL is relevant
            # These are from the initial batch import — keep them as they're legitimate
        clean_refs.append(line)

    if removed == 0:
        return {"file": filepath.name, "action": "no_contamination", "removed": 0}

    # Re-number references
    renumbered = []
    for idx, line in enumerate(clean_refs, 1):
        # Replace [N] at start of row
        renumbered.append(re.sub(
            r'\|\s*\[\d+\]\s*\|',
            f'| [{idx}] |',
            line,
            count=1,
        ))

    # Rebuild content
    new_lines = non_ref_lines_before + [
        f"| # | Title | Publisher | Date | URL |",
        f"|---|-------|----------|------|-----|",
    ] + renumbered + non_ref_lines_after

    post.content = "\n".join(new_lines)

    # Fix source_count to match remaining references
    actual_count = len(renumbered)
    old_count = post.metadata.get("source_count", 0)
    post.metadata["source_count"] = actual_count

    # Fix sources list in frontmatter
    if "sources" in post.metadata and isinstance(post.metadata["sources"], list):
        # Keep only as many as actual_count
        post.metadata["sources"] = post.metadata["sources"][:actual_count]

    # Write back
    filepath.write_text(frontmatter.dumps(post), encoding="utf-8")

    return {
        "file": filepath.name,
        "action": "cleaned",
        "removed": removed,
        "remaining": actual_count,
        "old_count": old_count,
        "new_count": actual_count,
    }


def fix_source_count(filepath: Path) -> dict:
    """Fix source_count to match actual references in the table."""
    post = frontmatter.load(filepath)
    content = post.content

    # Count reference rows
    ref_count = 0
    in_ref_table = False
    past_header = False
    for line in content.split("\n"):
        stripped = line.strip()
        if re.match(r'\|\s*#\s*\|', stripped):
            in_ref_table = True
            continue
        if in_ref_table and not past_header:
            if re.match(r'\|[-\s|]+\|', stripped):
                past_header = True
                continue
        if in_ref_table and past_header:
            if stripped.startswith("|") and re.search(r'\[\d+\]', stripped):
                ref_count += 1
            elif not stripped.startswith("|"):
                break

    old_count = post.metadata.get("source_count", 0)
    if ref_count > 0 and ref_count != old_count:
        post.metadata["source_count"] = ref_count
        post.metadata["updated"] = "2026-04-09"
        filepath.write_text(frontmatter.dumps(post), encoding="utf-8")
        return {
            "file": filepath.name,
            "action": "count_fixed",
            "old": old_count,
            "new": ref_count,
        }
    return {"file": filepath.name, "action": "count_ok", "count": old_count}


def main() -> None:
    print("=" * 60)
    print("  Reference Cleanup Tool")
    print("=" * 60)

    # Phase 1: Remove supplementary sources
    contaminated = [
        "phobos-8base-crackdown.md",
        "operation-synergia-ii.md",
        "operation-avalanche.md",
        "qakbot-gallyamov-indictment.md",
        "cryptex-pm2btc-sanctions.md",
        "hive-ransomware-takedown.md",
        "darkode-takedown.md",
        "fake-shopping-sites-takedown-2024.md",
        "botnet-takedown-europol-2023.md",
        "goznym-takedown.md",
        "korea-cambodia-scam-repatriation.md",
        "banking-trojan-fraud-sentencing-2017.md",
        "marketplace-a-dekhtyarchuk-indictment.md",
        "911-s5-botnet-takedown.md",
        "africa-cyber-surge-ii.md",
    ]

    print("\n--- Phase 1: Remove Supplementary Sources ---")
    total_removed = 0
    for name in contaminated:
        fp = OPS_DIR / name
        if fp.exists():
            result = clean_supplementary_sources(fp)
            total_removed += result.get("removed", 0)
            print(f"  {result['file']}: {result['action']}"
                  f" (removed={result.get('removed', 0)},"
                  f" remaining={result.get('remaining', '?')})")
        else:
            print(f"  {name}: NOT FOUND")

    print(f"\n  Total supplementary refs removed: {total_removed}")

    # Phase 2: Fix source_count on all operation pages
    print("\n--- Phase 2: Fix source_count ---")
    fixed = 0
    for md_file in sorted(OPS_DIR.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        result = fix_source_count(md_file)
        if result["action"] == "count_fixed":
            fixed += 1
            print(f"  {result['file']}: {result['old']} → {result['new']}")

    print(f"\n  Fixed {fixed} source_count mismatches")
    print("\nDone.")


if __name__ == "__main__":
    main()
