"""
Fix missing dates ('-') in References tables.
Extracts dates from URL patterns, or falls back to operation timeframe.
Also removes remaining 'Supplementary (high...' contaminated entries.
"""
import re
from pathlib import Path

import frontmatter

OPS_DIR = Path(__file__).resolve().parent.parent / "wiki" / "operations"


def extract_date_from_url(url: str) -> str:
    """Try to extract a publication date from URL path patterns."""
    # Pattern: /2024/11/27/ or /2024/11/ or /2024-11-27
    m = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

    m = re.search(r'/(\d{4})/(\d{2})/', url)
    if m:
        return f"{m.group(1)}-{m.group(2)}"

    # Pattern: /2024-11-27- or /20241127
    m = re.search(r'/(\d{4})-(\d{2})-(\d{2})', url)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

    # Pattern: news/2024/ or article/2024/
    m = re.search(r'(?:news|article|press|story|blog|media)[/-](\d{4})', url)
    if m:
        return m.group(1)

    return ""


def get_operation_date(meta: dict) -> str:
    """Get the announced date from operation metadata."""
    tf = meta.get("timeframe", {})
    if isinstance(tf, dict):
        announced = tf.get("announced", "")
        if announced:
            return str(announced)
    return ""


def fix_dates_in_file(filepath: Path) -> dict:
    """Fix '-' dates in References table rows."""
    post = frontmatter.load(filepath)
    content = post.content
    op_date = get_operation_date(post.metadata)
    lines = content.split("\n")
    changes = 0
    supplementary_removed = 0

    new_lines = []
    for line in lines:
        # Remove remaining "Supplementary (high..." entries
        if re.search(r'Supplementary \(high', line):
            supplementary_removed += 1
            continue

        # Fix date '-' in reference rows
        if line.strip().startswith("|") and "| - |" in line and "[원본]" in line:
            url_match = re.search(r'\[원본\]\((https?://[^)]+)\)', line)
            if url_match:
                url = url_match.group(1)
                date_str = extract_date_from_url(url)
                if not date_str and op_date:
                    date_str = op_date
                if date_str:
                    line = line.replace("| - |", f"| {date_str} |", 1)
                    changes += 1

        new_lines.append(line)

    if changes > 0 or supplementary_removed > 0:
        post.content = "\n".join(new_lines)

        # If we removed supplementary entries, re-number references
        if supplementary_removed > 0:
            content = post.content
            ref_lines = re.findall(r'^\|[^\n]*\[\d+\][^\n]*$', content, re.MULTILINE)
            for i, ref_line in enumerate(ref_lines, 1):
                new_ref = re.sub(r'\[\d+\]', f'[{i}]', ref_line, count=1)
                content = content.replace(ref_line, new_ref, 1)
            post.content = content

            # Fix source_count
            actual = len(ref_lines) - supplementary_removed
            if actual > 0:
                post.metadata["source_count"] = actual

        post.metadata["updated"] = "2026-04-09"
        filepath.write_text(frontmatter.dumps(post), encoding="utf-8")

    return {
        "file": filepath.name,
        "dates_fixed": changes,
        "supplementary_removed": supplementary_removed,
    }


def main() -> None:
    print("=" * 60)
    print("  Fix Reference Dates")
    print("=" * 60)

    total_dates = 0
    total_supp = 0
    for md_file in sorted(OPS_DIR.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        result = fix_dates_in_file(md_file)
        if result["dates_fixed"] > 0 or result["supplementary_removed"] > 0:
            total_dates += result["dates_fixed"]
            total_supp += result["supplementary_removed"]
            print(f"  {result['file']}: dates={result['dates_fixed']},"
                  f" supplementary_removed={result['supplementary_removed']}")

    print(f"\n  Total dates fixed: {total_dates}")
    print(f"  Total supplementary removed: {total_supp}")
    print("Done.")


if __name__ == "__main__":
    main()
