"""tools/reconcile_indexes.py

Scans wiki/<category>/*.md files and regenerates each _index.md table
plus wiki/index.md counts. Single source of truth = actual files.
Idempotent. Run after ingests or as a lint step.

Usage:
    python tools/reconcile_indexes.py             # write changes
    python tools/reconcile_indexes.py --dry-run   # report only
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Callable

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"

# ---------------------------------------------------------------------------
# Minimal frontmatter parser (stdlib only)
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _strip_quotes(value: str) -> str:
    v = value.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v


def parse_frontmatter(md_path: Path) -> dict[str, Any]:
    """Parse YAML frontmatter with a tolerant line-based parser.

    Supports:
      key: scalar
      key: [a, b]   (inline list)
      key:
        - item1
        - item2
      key:
        subkey: value
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return {}

    m = _FM_RE.match(text)
    if not m:
        return {}
    fm_text = m.group(1)

    data: dict[str, Any] = {}
    lines = fm_text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        # top-level key: must start at column 0
        if raw.startswith(" ") or raw.startswith("\t"):
            i += 1
            continue
        mkv = re.match(r"^([A-Za-z0-9_]+)\s*:(.*)$", raw)
        if not mkv:
            i += 1
            continue
        key, rest = mkv.group(1), mkv.group(2).strip()

        if rest == "":
            # Could be list or dict on following indented lines
            items: list[Any] = []
            sub: dict[str, Any] = {}
            j = i + 1
            mode: str | None = None
            while j < n:
                line = lines[j]
                if not line.strip():
                    j += 1
                    continue
                if not (line.startswith(" ") or line.startswith("\t")):
                    break
                stripped = line.strip()
                if stripped.startswith("- "):
                    mode = mode or "list"
                    if mode != "list":
                        break
                    item_val = stripped[2:].strip()
                    # dict entry inside list: "- key: value"
                    inline_kv = re.match(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$", item_val)
                    if inline_kv and inline_kv.group(2) != "":
                        items.append({inline_kv.group(1): _strip_quotes(inline_kv.group(2))})
                    elif inline_kv and inline_kv.group(2) == "":
                        items.append({inline_kv.group(1): None})
                    else:
                        items.append(_strip_quotes(item_val))
                    j += 1
                elif ":" in stripped:
                    mode = mode or "dict"
                    if mode != "dict":
                        break
                    k2, _, v2 = stripped.partition(":")
                    sub[k2.strip()] = _strip_quotes(v2.strip())
                    j += 1
                else:
                    break
            if mode == "list":
                data[key] = items
            elif mode == "dict":
                data[key] = sub
            else:
                data[key] = ""
            i = j
        elif rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            if not inner:
                data[key] = []
            else:
                data[key] = [_strip_quotes(x.strip()) for x in inner.split(",")]
            i += 1
        else:
            data[key] = _strip_quotes(rest)
            i += 1
    return data


# ---------------------------------------------------------------------------
# Field extraction helpers
# ---------------------------------------------------------------------------


def _first(value: Any, default: str = "—") -> str:
    if value is None or value == "":
        return default
    if isinstance(value, list):
        if not value:
            return default
        v0 = value[0]
        if isinstance(v0, dict):
            return str(next(iter(v0.values()), default))
        return str(v0)
    return str(value)


def _get(meta: dict, key: str, default: str = "—") -> str:
    v = meta.get(key)
    if v is None or v == "" or v == []:
        return default
    if isinstance(v, list):
        return ", ".join(str(x) for x in v if x)
    return str(v)


def _count(meta: dict, key: str) -> int:
    v = meta.get(key)
    if isinstance(v, list):
        return len(v)
    if isinstance(v, (int, float)):
        return int(v)
    if isinstance(v, str) and v.strip().isdigit():
        return int(v)
    return 0


# ---------------------------------------------------------------------------
# Category definitions — column schema & row builder
# ---------------------------------------------------------------------------


def _row_legal_frameworks(slug: str, meta: dict) -> tuple[list[str], str]:
    parties = meta.get("parties") or {}
    if isinstance(parties, dict):
        n_parties = parties.get("states_parties") or "—"
    else:
        n_parties = "—"
    scope = meta.get("scope") or {}
    flags = []
    if isinstance(scope, dict):
        if str(scope.get("substantive_law", "")).lower() == "true":
            flags.append("substantive")
        if str(scope.get("procedural_law", "")).lower() == "true":
            flags.append("procedural")
        if str(scope.get("international_cooperation", "")).lower() == "true":
            flags.append("IC")
    scope_str = " + ".join(flags) if flags else "—"
    return (
        [
            f"[[{slug}]]",
            _get(meta, "framework_type"),
            _get(meta, "status"),
            str(n_parties),
            scope_str,
            _get(meta, "adopted_date"),
        ],
        slug,
    )


def _row_organizations(slug: str, meta: dict) -> tuple[list[str], tuple[str, str]]:
    org_type = _get(meta, "org_type", "")
    hq = _get(meta, "headquarters", "")
    if hq == "—" or hq == "":
        hq = _get(meta, "country", "—")
    key_roles = meta.get("key_roles") or []
    if isinstance(key_roles, list) and key_roles:
        roles_str = "; ".join(str(r) for r in key_roles[:2])
    else:
        roles_str = "—"
    ops_count = _count(meta, "operations_participated")
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [
            f"[[{slug}]]",
            org_type or "—",
            hq or "—",
            roles_str,
            str(ops_count) if ops_count else "—",
            str(src_count),
        ],
        (org_type or "zzz", slug),
    )


def _iso_to_flag(iso: str) -> str:
    """Convert 2-letter ISO code to flag emoji (e.g., 'KR' → '🇰🇷')."""
    if not iso or len(iso) != 2 or not iso.isalpha():
        return ""
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in iso.upper())


def _row_countries(slug: str, meta: dict) -> tuple[list[str], str]:
    iso = _get(meta, "iso_code", "")
    flag = _iso_to_flag(iso)
    legal = _get(meta, "legal_system")
    # treaty_memberships → check budapest convention
    memberships = meta.get("treaty_memberships") or []
    budapest = "—"
    if isinstance(memberships, list):
        for m in memberships:
            if isinstance(m, dict):
                fw = str(m.get("framework", ""))
                if "budapest" in fw.lower():
                    status = m.get("status", "")
                    date = m.get("date", "")
                    if date:
                        year = str(date)[:4]
                        budapest = f"{status} ({year})" if status else year
                    else:
                        budapest = status or "listed"
                    break
    ic = meta.get("ic_capacity") or {}
    if isinstance(ic, dict):
        rating = ic.get("rating", "unknown") or "unknown"
        mlat = ic.get("avg_mlat_response_days", "unknown") or "unknown"
    else:
        rating, mlat = "unknown", "unknown"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [
            f"{flag}",
            f"[[{slug}]]",
            legal,
            budapest,
            str(rating),
            str(mlat),
            str(src_count),
        ],
        iso or "ZZ",
    )


def _row_operations(slug: str, meta: dict) -> tuple[list[str], tuple[str, str]]:
    case_id = _get(meta, "case_id", "—")
    period = _get(meta, "period", "—")
    status = _get(meta, "status", "—")
    ci = meta.get("credibility_index", "")
    ci_str = f"{float(ci):.2f}" if isinstance(ci, (int, float)) or (isinstance(ci, str) and ci.replace(".", "", 1).isdigit()) else "—"
    if ci_str == "0.00":
        ci_str = "—"
    tier = _get(meta, "source_tier", "—")
    if tier == "0":
        tier = "—"
    # sort: empty case_id go last
    sort_key = (case_id if case_id != "—" else "ZZZ", slug)
    return (
        [f"[[{slug}]]", case_id, period, status, ci_str, tier],
        sort_key,
    )


def _row_cases(slug: str, meta: dict) -> tuple[list[str], str]:
    jurisdiction = _get(meta, "jurisdiction")
    crime = meta.get("crime_charged") or []
    crime_str = ", ".join(str(c).replace("[[", "").replace("]]", "") for c in crime[:2]) if isinstance(crime, list) and crime else "—"
    status = _get(meta, "status")
    ic = meta.get("ic_elements") or {}
    ic_str = "—"
    if isinstance(ic, dict):
        parts = []
        if ic.get("mlat_requests"):
            parts.append("MLAT")
        if ic.get("extradition"):
            parts.append("extradition")
        if ic.get("evidence_from_abroad"):
            parts.append("evidence")
        ic_str = ", ".join(parts) if parts else "—"
    precedent = _get(meta, "precedent_value", "—")
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [
            f"[[{slug}]]",
            jurisdiction,
            crime_str,
            status,
            ic_str,
            precedent,
            str(src_count),
        ],
        slug,
    )


def _row_mechanisms(slug: str, meta: dict) -> tuple[list[str], str]:
    mtype = _get(meta, "mechanism_type")
    formality = _get(meta, "formality")
    speed = _get(meta, "speed")
    administered = _get(meta, "administered_by")
    legal = meta.get("legal_basis") or []
    legal_str = ", ".join(str(x).replace("[[", "").replace("]]", "") for x in legal[:2]) if isinstance(legal, list) and legal else "—"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [f"[[{slug}]]", mtype, formality, speed, administered, legal_str, str(src_count)],
        slug,
    )


def _row_procedures(slug: str, meta: dict) -> tuple[list[str], str]:
    ptype = _get(meta, "procedure_type")
    legal = meta.get("legal_basis") or []
    legal_str = ", ".join(str(x).replace("[[", "").replace("]]", "") for x in legal[:2]) if isinstance(legal, list) and legal else "—"
    duration = _get(meta, "average_duration")
    template = _get(meta, "template_available", "No")
    if template.lower() in ("true", "yes"):
        template = "Yes"
    elif template.lower() in ("false", "no", "—"):
        template = "No"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [f"[[{slug}]]", ptype, legal_str, duration, template, str(src_count)],
        slug,
    )


def _row_crime_types(slug: str, meta: dict) -> tuple[list[str], str]:
    category = _get(meta, "crime_category")
    crim = meta.get("criminalization_status") or {}
    broadly = "—"
    if isinstance(crim, dict):
        b = crim.get("broadly_criminalized")
        if str(b).lower() == "true":
            broadly = "Yes"
        elif str(b).lower() == "false":
            broadly = "No"
    mechanisms = meta.get("typical_mechanisms") or []
    mech_str = ", ".join(str(x).replace("[[", "").replace("]]", "") for x in mechanisms[:3]) if isinstance(mechanisms, list) and mechanisms else "—"
    operations = meta.get("notable_operations") or []
    ops_str = ", ".join(str(x).replace("[[", "").replace("]]", "") for x in operations[:3]) if isinstance(operations, list) and operations else "—"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [f"[[{slug}]]", category, broadly, mech_str, ops_str, str(src_count)],
        slug,
    )


def _row_challenges(slug: str, meta: dict) -> tuple[list[str], str]:
    cat = _get(meta, "challenge_category")
    severity = _get(meta, "severity")
    affected = meta.get("affected_mechanisms") or []
    affected_str = ", ".join(str(x) if str(x).startswith("[[") else f"[[{x}]]" for x in affected[:3]) if isinstance(affected, list) and affected else "—"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [f"[[{slug}]]", cat, severity, affected_str, str(src_count)],
        slug,
    )


def _row_concepts(slug: str, meta: dict) -> tuple[list[str], str]:
    title_ko = _get(meta, "title_ko", "—")
    cat = _get(meta, "concept_category")
    domain = _get(meta, "domain")
    applied = meta.get("applied_in_cases") or []
    applied_str = ", ".join(str(x).replace("[[", "").replace("]]", "") for x in applied[:3]) if isinstance(applied, list) and applied else "-"
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return (
        [f"[[{slug}]]", title_ko, cat, domain, applied_str, str(src_count)],
        slug,
    )


def _row_sources(slug: str, meta: dict) -> tuple[list[str], tuple[str, str]]:
    stype = _get(meta, "source_type")
    publisher = _get(meta, "publisher")
    pdate = _get(meta, "publish_date", "")
    reliability = _get(meta, "reliability")
    tier = _get(meta, "source_tier", "?")
    if tier == "—" or tier == "0":
        tier = "?"
    # sort: publish_date desc then slug asc → use negative via inverse string
    sort_key = (pdate or "0000-00-00", slug)
    return (
        [f"[[{slug}]]", stype, publisher, tier, reliability, "?"],
        sort_key,
    )


def _row_analysis(slug: str, meta: dict) -> tuple[list[str], str]:
    atype = _get(meta, "analysis_type")
    confidence = _get(meta, "confidence")
    scope = _get(meta, "scope")
    created = _get(meta, "created")
    return ([f"[[{slug}]]", atype, confidence, scope, created], slug)


def _row_timelines(slug: str, meta: dict) -> tuple[list[str], str]:
    entity = _get(meta, "entity")
    ttype = _get(meta, "timeline_type", _get(meta, "type", "—"))
    timespan = _get(meta, "timespan")
    src_count = _count(meta, "source_count") or _count(meta, "sources")
    return ([f"[[{slug}]]", entity, ttype, timespan, str(src_count)], slug)


CATEGORIES: dict[str, dict[str, Any]] = {
    "legal-frameworks": {
        "headers": ["Framework", "Type", "Status", "Parties", "Scope (IC)", "Date"],
        "row": _row_legal_frameworks,
        "reverse_sort": False,
    },
    "organizations": {
        "headers": ["Organization", "Type", "Country/HQ", "Key IC Roles", "Operations", "Sources"],
        "row": _row_organizations,
        "reverse_sort": False,
    },
    "countries": {
        "headers": ["🏳️", "Country", "Legal System", "Budapest Conv.", "IC Capacity", "MLAT Response", "Sources"],
        "row": _row_countries,
        "reverse_sort": False,
    },
    "operations": {
        "headers": ["Operation", "Case ID", "Period", "Status", "CI", "Tier"],
        "row": _row_operations,
        "reverse_sort": False,
    },
    "cases": {
        "headers": ["Case", "Jurisdiction", "Crime", "Status", "IC Elements", "Precedent Value", "Sources"],
        "row": _row_cases,
        "reverse_sort": False,
    },
    "mechanisms": {
        "headers": ["Mechanism", "Type", "Formality", "Speed", "Administered By", "Legal Basis", "Sources"],
        "row": _row_mechanisms,
        "reverse_sort": False,
    },
    "procedures": {
        "headers": ["Procedure", "Type", "Legal Basis", "Avg Duration", "Template", "Sources"],
        "row": _row_procedures,
        "reverse_sort": False,
    },
    "crime-types": {
        "headers": ["Crime Type", "Category", "Broadly Criminalized", "Key Mechanisms", "Notable Operations", "Sources"],
        "row": _row_crime_types,
        "reverse_sort": False,
    },
    "challenges": {
        "headers": ["Challenge", "Category", "Severity", "Affected Mechanisms", "Sources"],
        "row": _row_challenges,
        "reverse_sort": False,
    },
    "concepts": {
        "headers": ["Concept", "Korean (한국어)", "Category", "Domain", "Applied in Cases", "Sources"],
        "row": _row_concepts,
        "reverse_sort": False,
    },
    "sources": {
        "headers": ["Source", "Type", "Publisher", "Tier", "Reliability", "Domain"],
        "row": _row_sources,
        "reverse_sort": True,  # publish_date desc
    },
    "analysis": {
        "headers": ["Analysis", "Type", "Confidence", "Scope", "Date"],
        "row": _row_analysis,
        "reverse_sort": False,
    },
    "timelines": {
        "headers": ["Timeline", "Entity", "Type", "Timespan", "Sources"],
        "row": _row_timelines,
        "reverse_sort": False,
    },
}


# ---------------------------------------------------------------------------
# Loading & table build
# ---------------------------------------------------------------------------


def load_category_pages(category: str) -> list[tuple[str, dict]]:
    cat_dir = WIKI_DIR / category
    if not cat_dir.is_dir():
        return []
    pages: list[tuple[str, dict]] = []
    for md in sorted(cat_dir.glob("*.md")):
        if md.name.startswith("_"):
            continue
        meta = parse_frontmatter(md)
        pages.append((md.stem, meta))
    return pages


def _escape_cell(value: str) -> str:
    # Escape pipes so they don't break table rendering
    return str(value).replace("|", "\\|")


def build_index_table(category: str, pages: list[tuple[str, dict]]) -> str:
    cfg = CATEGORIES[category]
    headers: list[str] = cfg["headers"]
    row_fn: Callable = cfg["row"]
    reverse: bool = cfg["reverse_sort"]

    rows_with_keys = [row_fn(slug, meta) for slug, meta in pages]
    rows_with_keys.sort(key=lambda x: x[1], reverse=reverse)

    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["-" * (len(h) + 2) for h in headers]) + "|")
    for row, _key in rows_with_keys:
        lines.append("| " + " | ".join(_escape_cell(c) for c in row) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# _index.md rewrite
# ---------------------------------------------------------------------------


def _split_index(text: str) -> tuple[str, str, str]:
    """Split _index.md into (prefix, table_block, suffix).

    prefix: everything before the first line that starts with '|'
    table_block: contiguous block of lines starting with '|'
    suffix: everything after

    If no table exists, table_block is empty string and suffix is empty.
    """
    lines = text.split("\n")
    table_start: int | None = None
    table_end: int | None = None
    for i, line in enumerate(lines):
        if line.startswith("|"):
            if table_start is None:
                table_start = i
            table_end = i
        elif table_start is not None and table_end is not None and not line.startswith("|"):
            # table ended at previous line
            break
    if table_start is None:
        # no existing table: prefix is everything, keep a trailing blank line
        prefix = text
        if not prefix.endswith("\n"):
            prefix += "\n"
        return prefix, "", ""
    prefix = "\n".join(lines[:table_start])
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    table_block = "\n".join(lines[table_start : (table_end or table_start) + 1])
    suffix_lines = lines[(table_end or table_start) + 1 :]
    suffix = "\n".join(suffix_lines)
    return prefix, table_block, suffix


_TITLE_COUNT_RE = re.compile(r"^(# [^\n(]+?)(?:\s*\(\d+\))?\s*$", re.MULTILINE)


def _update_title_count(prefix: str, count: int) -> str:
    """If the prefix has a top-level '# Title' heading (optionally followed by
    '(N)'), update the count in parentheses."""
    def repl(m: re.Match) -> str:
        return f"{m.group(1)} ({count})"

    new_prefix, n = _TITLE_COUNT_RE.subn(repl, prefix, count=1)
    if n == 0:
        return prefix
    return new_prefix


def update_category_index(category: str, dry_run: bool = False) -> tuple[bool, int, int]:
    """Regenerate _index.md for a category.

    Returns (changed, old_row_count, new_row_count).
    """
    cat_dir = WIKI_DIR / category
    index_path = cat_dir / "_index.md"
    pages = load_category_pages(category)
    new_row_count = len(pages)

    if not index_path.exists():
        # Create a minimal stub
        cfg = CATEGORIES[category]
        header_title = category.replace("-", " ").title()
        new_table = build_index_table(category, pages)
        new_text = (
            f"---\ntype: category-index\ntitle: \"{header_title}\"\n"
            f"category: {category}\n---\n\n# {header_title} ({new_row_count})\n\n{new_table}\n"
        )
        old_row_count = 0
        if not dry_run:
            index_path.write_text(new_text, encoding="utf-8")
        return True, old_row_count, new_row_count

    original = index_path.read_text(encoding="utf-8")
    prefix, old_table, suffix = _split_index(original)

    # Count old rows: lines that start with '|' minus 2 (header + separator)
    old_row_count = 0
    if old_table:
        tlines = [l for l in old_table.split("\n") if l.startswith("|")]
        old_row_count = max(0, len(tlines) - 2)

    # Update title count in prefix if present
    prefix = _update_title_count(prefix, new_row_count)

    new_table = build_index_table(category, pages)

    # Assemble new content
    # Ensure exactly one blank line separates prefix and table, and table ends with newline
    prefix_trimmed = prefix.rstrip("\n") + "\n\n" if prefix.strip() else prefix
    new_content = prefix_trimmed + new_table + "\n"
    if suffix.strip():
        new_content += "\n" + suffix.lstrip("\n")
        if not new_content.endswith("\n"):
            new_content += "\n"

    changed = new_content != original
    if changed and not dry_run:
        index_path.write_text(new_content, encoding="utf-8")
    return changed, old_row_count, new_row_count


# ---------------------------------------------------------------------------
# Master wiki/index.md update
# ---------------------------------------------------------------------------

MASTER_CATEGORY_HEADINGS = {
    "legal-frameworks": "Legal Frameworks",
    "organizations": "Organizations",
    "countries": "Countries",
    "operations": "Operations",
    "cases": "Cases",
    "mechanisms": "Mechanisms",
    "procedures": "Procedures",
    "crime-types": "Crime Types",
    "challenges": "Challenges",
    "concepts": "Concepts",
    "sources": "Sources",
    "analysis": "Analysis",
    "timelines": "Timelines",
}


def update_master_index(counts: dict[str, int], dry_run: bool = False) -> bool:
    master = WIKI_DIR / "index.md"
    if not master.exists():
        return False
    text = master.read_text(encoding="utf-8")
    original = text

    # Update "## Heading (N)" lines
    for cat, heading in MASTER_CATEGORY_HEADINGS.items():
        n = counts.get(cat, 0)
        pattern = re.compile(rf"^(## {re.escape(heading)})\s*\(\d+\)\s*$", re.MULTILINE)
        text, _ = pattern.subn(rf"\1 ({n})", text)

    # Update "full list of N operations" style references
    ops = counts.get("operations", 0)
    text = re.sub(r"full list of \d+ operations", f"full list of {ops} operations", text)
    srcs = counts.get("sources", 0)
    text = re.sub(
        r"full list of \d+ dedicated source pages",
        f"full list of {srcs} dedicated source pages",
        text,
    )

    # Update total pages and total sources on the top metadata line
    total_pages = sum(counts.values())
    text = re.sub(r"Total pages:\s*\d+", f"Total pages: {total_pages}", text)
    text = re.sub(r"Total sources:\s*\d+", f"Total sources: {srcs}", text)

    changed = text != original
    if changed and not dry_run:
        master.write_text(text, encoding="utf-8")
    return changed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    print("Reconciling wiki indexes..." + (" (dry run)" if dry_run else ""))
    touched = 0
    changed_count = 0
    counts: dict[str, int] = {}

    for cat in CATEGORIES:
        try:
            changed, old_n, new_n = update_category_index(cat, dry_run=dry_run)
        except Exception as exc:
            print(f"  {cat}: ERROR {exc}")
            continue
        counts[cat] = new_n
        touched += 1
        if changed:
            changed_count += 1
        delta = new_n - old_n
        if delta == 0:
            delta_str = "no change"
        else:
            sign = "+" if delta > 0 else ""
            delta_str = f"{sign}{delta}"
        mark = "*" if changed else " "
        print(f"  {mark} {cat}: {old_n} -> {new_n} rows ({delta_str})")

    master_changed = update_master_index(counts, dry_run=dry_run)
    if master_changed:
        print("Updated wiki/index.md master catalog.")
    else:
        print("wiki/index.md already in sync.")

    total_changed = changed_count + (1 if master_changed else 0)
    print(f"Done: {touched} _index.md files processed, {changed_count} changed, master {'changed' if master_changed else 'unchanged'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
