from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from typing import Any

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"

ABSORBED_STATUS = "absorbed"
FOLLOW_ON_ROLE = "follow-on"
VALID_CANONICAL_PERIODS = {"1", "2", "3"}


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def scalar(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def source_count(meta: dict[str, Any]) -> int | None:
    value = meta.get("source_count")
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def list_count(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, list):
        return len(value)
    return None


def audit_page(path: Path) -> tuple[dict[str, Any], list[str]]:
    try:
        meta = dict(frontmatter.load(path).metadata)
    except Exception as exc:  # pragma: no cover - reports malformed files
        return {}, [f"frontmatter_parse_error:{exc}"]

    issues: list[str] = []
    status = norm(meta.get("status"))
    role = norm(meta.get("operation_role"))
    period = scalar(meta.get("period"))
    is_absorbed = status == ABSORBED_STATUS

    if role == FOLLOW_ON_ROLE and not is_absorbed:
        issues.append("follow_on_role_not_absorbed")
    if is_absorbed and role != FOLLOW_ON_ROLE:
        issues.append("absorbed_status_not_follow_on")

    if not is_absorbed:
        if period not in VALID_CANONICAL_PERIODS:
            issues.append(f"canonical_period_invalid:{period or 'missing'}")
        if not scalar(meta.get("coordinating_body")) and not scalar(meta.get("lead_agency")):
            issues.append("canonical_missing_coordinator_and_lead")

    declared_sources = source_count(meta)
    listed_sources = list_count(meta.get("sources"))
    if declared_sources is not None and listed_sources is not None and declared_sources != listed_sources:
        issues.append(f"source_count_mismatch:{declared_sources}!={listed_sources}")

    return meta, issues


def main() -> int:
    if not OPS_DIR.is_dir():
        print(f"Missing operations directory: {OPS_DIR}", file=sys.stderr)
        return 2

    total = 0
    issue_rows: list[tuple[str, str, str, list[str]]] = []
    scopes: Counter[str] = Counter()
    periods: Counter[str] = Counter()

    for path in sorted(OPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        total += 1
        meta, issues = audit_page(path)
        title = scalar(meta.get("title")) or path.stem
        status = norm(meta.get("status"))
        if status == ABSORBED_STATUS:
            scopes["absorbed_follow_on"] += 1
        else:
            scopes["canonical_operation"] += 1
            periods[scalar(meta.get("period")) or "missing"] += 1
        if issues:
            issue_rows.append((path.name, title, status or "missing", issues))

    print("Operation consistency audit")
    print(f"- Total records: {total}")
    print(f"- Canonical operations: {scopes['canonical_operation']}")
    print(f"- Absorbed follow-on records: {scopes['absorbed_follow_on']}")
    print(
        "- Canonical periods: "
        + ", ".join(f"P{key}: {periods[key]}" for key in sorted(periods) if key != "missing")
        + (f", missing: {periods['missing']}" if periods["missing"] else "")
    )

    if issue_rows:
        print()
        print(f"Issues: {len(issue_rows)}")
        for filename, title, status, issues in issue_rows[:200]:
            print(f"- {filename} | {status} | {title} | {', '.join(issues)}")
        if len(issue_rows) > 200:
            print(f"... {len(issue_rows) - 200} more issue rows omitted")
        return 1

    print("- Issues: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
