"""
Fix generic 'Source N' labels in References tables.
Extracts better titles from URL patterns and known publisher info.
"""
import re
from pathlib import Path

import frontmatter

OPS_DIR = Path(__file__).resolve().parent.parent / "wiki" / "operations"

# Known publisher mappings from URL domains
PUBLISHER_MAP = {
    "europol.europa.eu": "Europol",
    "interpol.int": "INTERPOL",
    "justice.gov": "US DOJ",
    "fbi.gov": "FBI",
    "bbc.com": "BBC",
    "bbc.co.uk": "BBC",
    "reuters.com": "Reuters",
    "thehackernews.com": "The Hacker News",
    "bleepingcomputer.com": "BleepingComputer",
    "krebsonsecurity.com": "Krebs on Security",
    "securityaffairs.com": "Security Affairs",
    "therecord.media": "The Record",
    "wired.com": "Wired",
    "hackread.com": "HackRead",
    "cyberscoop.com": "CyberScoop",
    "group-ib.com": "Group-IB",
    "nationalcrimeagency.gov.uk": "UK NCA",
    "ice.gov": "ICE/HSI",
    "pcmag.com": "PCMag",
    "vanguardngr.com": "Vanguard News",
    "zdnet.com": "ZDNet",
    "darkreading.com": "Dark Reading",
    "techcrunch.com": "TechCrunch",
}


def extract_title_from_url(url: str) -> str:
    """Extract a readable title from URL slug."""
    # Get the last path segment
    path = url.rstrip("/").split("/")[-1]
    # Remove common suffixes
    path = re.sub(r'\.(html|htm|php|aspx)$', '', path)
    # Replace hyphens/underscores with spaces
    title = path.replace("-", " ").replace("_", " ")
    # Capitalize
    title = title.strip().title()
    # Limit length
    if len(title) > 80:
        title = title[:77] + "..."
    return title


def get_publisher(url: str) -> str:
    """Extract publisher from URL domain."""
    domain_match = re.search(r'https?://(?:www\.)?([^/]+)', url)
    if not domain_match:
        return "Unknown"
    domain = domain_match.group(1)
    for key, name in PUBLISHER_MAP.items():
        if key in domain:
            return name
    return domain


def fix_source_labels(filepath: Path) -> dict:
    """Replace 'Source N' generic labels with URL-derived titles."""
    text = filepath.read_text(encoding="utf-8")
    changes = 0

    def replace_source_n(match):
        nonlocal changes
        full_line = match.group(0)
        # Extract URL from the line
        url_match = re.search(r'\[원본\]\((https?://[^)]+)\)', full_line)
        if not url_match:
            return full_line

        url = url_match.group(1)
        title = extract_title_from_url(url)
        publisher = get_publisher(url)

        # Replace "Source N" with extracted title
        new_line = re.sub(
            r'\|\s*Source \d+\s*\|',
            f'| {title} |',
            full_line,
            count=1,
        )
        # Also replace publisher if it was domain-based
        old_pub = re.search(r'\|\s*Source \d+\s*\|\s*([^|]+)\|', full_line)
        if old_pub:
            old_pub_text = old_pub.group(1).strip()
            if "." in old_pub_text:  # It's still a raw domain
                new_line = new_line.replace(
                    f"| {old_pub_text} |",
                    f"| {publisher} |",
                    1,
                )
        changes += 1
        return new_line

    # Match reference table rows with "Source N"
    new_text = re.sub(
        r'\|[^\n]*Source \d+[^\n]*\|',
        replace_source_n,
        text,
    )

    if changes > 0:
        filepath.write_text(new_text, encoding="utf-8")

    return {"file": filepath.name, "changes": changes}


def main() -> None:
    print("=" * 60)
    print("  Fix Source Labels")
    print("=" * 60)

    total = 0
    for md_file in sorted(OPS_DIR.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        text = md_file.read_text(encoding="utf-8")
        if re.search(r'\|\s*Source \d+\s*\|', text):
            result = fix_source_labels(md_file)
            if result["changes"] > 0:
                total += result["changes"]
                print(f"  {result['file']}: {result['changes']} labels fixed")

    print(f"\n  Total labels fixed: {total}")
    print("Done.")


if __name__ == "__main__":
    main()
