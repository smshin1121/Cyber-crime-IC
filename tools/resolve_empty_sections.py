from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
DEFAULT_DATE = "2026-05-02"

FM_RE = re.compile(r"\A---\r?\n(?P<frontmatter>.*?)(?P<tail>\r?\n---\r?\n)", re.S)
EMPTY_SECTION_RE = re.compile(r"^(## .+)\n+(?=## |\Z)", re.M)


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "", {}):
        return []
    return [value]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2].split("|", 1)[0]
    return text.strip().strip("'\"")


def wikilink_label(value: Any) -> str:
    text = str(value or "").strip().strip("'\"")
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        if "|" in inner:
            return inner.split("|", 1)[1].strip()
        text = inner
    text = re.sub(r"[-_]+", " ", text)
    return " ".join(part.capitalize() for part in text.split())


def split_page(text: str) -> tuple[str, str, str, int]:
    match = FM_RE.match(text)
    if not match:
        return "", "", text, 0
    return match.group("frontmatter"), match.group("tail"), text[match.end() :], match.end()


def update_frontmatter_date(frontmatter_text: str, run_date: str) -> str:
    if re.search(r"(?m)^updated:\s*", frontmatter_text):
        return re.sub(r"(?m)^updated:\s*.*$", f"updated: {run_date}", frontmatter_text)
    return frontmatter_text.rstrip() + f"\nupdated: {run_date}"


def source_meta(slug: str) -> dict[str, Any]:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return {}
    try:
        return dict(frontmatter.load(path).metadata)
    except Exception:
        return {}


def source_coverage_lines(meta: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    for item in as_list(meta.get("sources")):
        slug = wikilink_slug(item)
        smeta = source_meta(slug)
        title = str(smeta.get("title") or wikilink_label(item) or slug)
        publisher = str(smeta.get("publisher") or smeta.get("collection_domain") or "Source page")
        date = str(smeta.get("publish_date") or smeta.get("created") or "date not recorded")
        lines.append(f"- {publisher}, {date}: {title}.")
    declared = int(meta.get("source_count") or len(lines) or 0)
    if declared <= 1:
        lines.append("- Source coverage is single-source; absent details should be treated as unobserved in the current corpus, not disproven.")
    return dedupe(lines)


def evidence_lines(meta: dict[str, Any]) -> list[str]:
    lines = [
        "- The cited source set is treated as the controlling public record for this page; no additional filing-level evidence is asserted beyond the listed references and metadata.",
    ]

    ic = meta.get("ic_elements") if isinstance(meta.get("ic_elements"), dict) else {}
    present: list[str] = []
    if ic:
        labels = {
            "mlat_requests": "MLAT requests",
            "extradition": "extradition",
            "evidence_from_abroad": "foreign-evidence transfers",
            "foreign_arrests": "foreign arrests",
            "asset_freezing": "asset freezing",
        }
        for key, label in labels.items():
            value = ic.get(key)
            if as_list(value) or (isinstance(value, str) and value.strip()):
                present.append(label)

    if present:
        lines.append(f"- Recorded international-cooperation elements in metadata: {', '.join(present)}.")
    else:
        lines.append("- Current metadata does not identify MLAT requests, extradition, foreign-evidence transfers, foreign arrests, or asset-freezing elements.")

    mechanisms = [wikilink_label(item) for item in as_list(meta.get("mechanisms_used"))]
    mechanisms = [item for item in mechanisms if item]
    if mechanisms:
        lines.append(f"- Recorded cooperation mechanism metadata: {', '.join(mechanisms[:6])}.")

    declared = int(meta.get("source_count") or len(as_list(meta.get("sources"))) or 0)
    if declared <= 1:
        lines.append("- Comparative use should preserve the single-source limitation and avoid inferring that absent cooperation fields prove no cooperation occurred.")
    return dedupe(lines)


def result_lines(meta: dict[str, Any]) -> list[str]:
    results = meta.get("results") if isinstance(meta.get("results"), dict) else {}
    lines: list[str] = []
    labels = {
        "arrests": "Arrests",
        "indictments": "Indictments",
        "servers_seized": "Servers seized",
        "domains_seized": "Domains seized",
        "decryption_keys_recovered": "Decryption keys recovered",
        "victims_notified": "Victims notified",
    }
    for key, label in labels.items():
        value = results.get(key)
        try:
            numeric = int(value)
        except Exception:
            numeric = 0
        if numeric:
            lines.append(f"- {label}: {numeric}.")

    crypto = str(results.get("cryptocurrency_seized") or "").strip()
    if crypto:
        lines.append(f"- Cryptocurrency seized: {crypto}.")

    for item in as_list(results.get("other")):
        text = str(item or "").strip().rstrip(".")
        if text:
            lines.append(f"- {text}.")

    if not lines:
        lines.append("- No quantified result fields are currently recorded in frontmatter; consult the cited sources before coding outcomes.")
    return dedupe(lines)


def dedupe(lines: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for line in lines:
        key = re.sub(r"\s+", " ", line).strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(line)
    return out


def fill_lines(heading: str, meta: dict[str, Any]) -> list[str]:
    if heading == "## Evidence and Attribution Notes":
        return evidence_lines(meta)
    if heading == "## Source Coverage":
        return source_coverage_lines(meta)
    if heading == "## Results":
        return result_lines(meta)
    return ["- No additional text is currently recorded for this section."]


def process_file(path: Path, run_date: str, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    frontmatter_text, tail, body, _ = split_page(text)
    if not frontmatter_text:
        return False
    empty = [heading.strip() for heading in EMPTY_SECTION_RE.findall(body)]
    if not empty:
        return False

    meta = dict(frontmatter.load(path).metadata)
    new_body = body
    for heading in empty:
        lines = fill_lines(heading, meta)
        replacement = f"{heading}\n\n" + "\n".join(lines) + "\n\n"
        new_body = re.sub(rf"^{re.escape(heading)}\n+(?=## |\Z)", replacement, new_body, count=1, flags=re.M)

    new_frontmatter = update_frontmatter_date(frontmatter_text, run_date)
    new_text = "---\n" + new_frontmatter.rstrip() + tail + new_body
    if new_text == text:
        return False
    if not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Fill lint-empty sections using existing metadata and references.")
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    changed: list[Path] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        if process_file(path, args.date, args.dry_run):
            changed.append(path)

    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")
    print(f"Pages changed: {len(changed)}")
    for path in changed[:120]:
        print(path.relative_to(ROOT).as_posix())
    if len(changed) > 120:
        print(f"... +{len(changed) - 120} more")


if __name__ == "__main__":
    main()
