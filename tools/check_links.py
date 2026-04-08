"""
Static site link checker — scans all HTML files in docs/ for broken links.
Detects: missing targets, malformed URLs, [[wikilink]] leaks, double paths, etc.
"""
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


def check_all() -> dict:
    """Check all links in the static site."""
    all_files: set[str] = set()
    for f in DOCS_DIR.rglob("*"):
        if f.is_file():
            rel = f.relative_to(DOCS_DIR).as_posix()
            all_files.add(rel)

    issues: dict[str, list] = defaultdict(list)
    stats = {"total_links": 0, "internal": 0, "external": 0, "broken": 0, "malformed": 0}

    for html_file in sorted(DOCS_DIR.rglob("*.html")):
        rel_path = html_file.relative_to(DOCS_DIR).as_posix()
        content = html_file.read_text(encoding="utf-8", errors="replace")
        hrefs = re.findall(r'href="([^"]*)"', content)

        for href in hrefs:
            stats["total_links"] += 1
            href_decoded = unquote(href)

            # 1. [[wikilink]] leak — raw wikilink syntax in URL
            if "[[" in href_decoded or "]]" in href_decoded:
                issues["wikilink_leak"].append({
                    "file": rel_path,
                    "href": href_decoded,
                })
                stats["malformed"] += 1
                continue

            # 2. External links — skip target check
            if href_decoded.startswith(("http://", "https://", "mailto:")):
                stats["external"] += 1
                continue

            # 3. Fragment-only links (#section)
            if href_decoded.startswith("#"):
                continue

            # 4. Empty href
            if not href_decoded.strip():
                issues["empty_href"].append({"file": rel_path})
                stats["malformed"] += 1
                continue

            stats["internal"] += 1

            # 5. Malformed patterns
            if "//" in href_decoded and not href_decoded.startswith("//"):
                issues["double_slash"].append({
                    "file": rel_path,
                    "href": href_decoded,
                })
                stats["malformed"] += 1

            # 6. _missing/ links (known missing pages)
            if "_missing" in href_decoded:
                issues["missing_page"].append({
                    "file": rel_path,
                    "href": href_decoded,
                })
                stats["broken"] += 1
                continue

            # 7. Resolve relative path and check if target exists
            target = _resolve_href(rel_path, href_decoded)
            if target and target not in all_files:
                # Maybe it's a directory with index
                if (target + "/index.html") not in all_files:
                    issues["target_not_found"].append({
                        "file": rel_path,
                        "href": href_decoded,
                        "resolved": target,
                    })
                    stats["broken"] += 1

    return {"issues": dict(issues), "stats": stats}


def _resolve_href(from_file: str, href: str) -> str | None:
    """Resolve a relative href to a path relative to DOCS_DIR."""
    # Strip fragment
    href = href.split("#")[0]
    if not href:
        return None

    # Absolute path (starts with / or relative to root)
    if href.startswith("/"):
        return href.lstrip("/")

    # Relative path — resolve from the file's directory
    from_dir = "/".join(from_file.split("/")[:-1])
    parts = href.split("/")

    result_parts = from_dir.split("/") if from_dir else []
    for p in parts:
        if p == "..":
            if result_parts:
                result_parts.pop()
        elif p == ".":
            continue
        else:
            result_parts.append(p)

    return "/".join(result_parts)


def main() -> None:
    print("=" * 60)
    print("  Static Site Link Checker")
    print("=" * 60)

    result = check_all()
    stats = result["stats"]
    issues = result["issues"]

    print(f"\n  Total links: {stats['total_links']}")
    print(f"  Internal: {stats['internal']}")
    print(f"  External: {stats['external']}")
    print(f"  Broken: {stats['broken']}")
    print(f"  Malformed: {stats['malformed']}")

    for issue_type, items in sorted(issues.items()):
        print(f"\n  [{issue_type}] -- {len(items)} issues")
        # Deduplicate by href for cleaner output
        seen = set()
        for item in items:
            href = item.get("href", "")
            if href not in seen:
                seen.add(href)
                src = item.get("file", "")
                print(f"    {href}")
                print(f"      in: {src}")
            if len(seen) >= 15:
                remaining = len(items) - len(seen)
                if remaining > 0:
                    print(f"    ... and {remaining} more")
                break

    total_issues = sum(len(v) for v in issues.values())
    print(f"\n  TOTAL ISSUES: {total_issues}")
    print("Done.")


if __name__ == "__main__":
    main()
