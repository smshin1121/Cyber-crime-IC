from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STATUS = "fulltext_not_available"


def mark_source(source_rel: str, raw_rel: str, run_date: str, reason: str, status: str, dry_run: bool) -> bool:
    changed = False
    for rel in (source_rel, raw_rel):
        if not rel:
            continue
        path = ROOT / rel
        if not path.exists():
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        updates = {
            "harvest_status": status,
            "harvest_note": reason,
            "last_fetch_attempt": run_date,
        }
        for key, value in updates.items():
            if meta.get(key) != value:
                meta[key] = value
                changed = True
        if changed and not dry_run:
            post.metadata = meta
            path.write_text(frontmatter.dumps(post), encoding="utf-8")
    return changed


def queue_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    outcomes = payload.get("outcomes") or []
    if outcomes and all(str(item.get("status") or "").startswith("would_") for item in outcomes):
        for item in outcomes:
            out.append(
                {
                    "source_path": item.get("source_path") or "",
                    "raw_path": item.get("raw_path") or "",
                    "reason": "Repeated live fulltext harvesting failed or is not suitable; source digest retained.",
                }
            )
        return out

    for item in outcomes:
        status = str(item.get("status") or "")
        if status not in {"fetch_failed", "parse_failed"}:
            continue
        out.append(
            {
                "source_path": item.get("source_path") or "",
                "raw_path": item.get("raw_path") or "",
                "reason": str(item.get("error") or status),
            }
        )
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--status", default=DEFAULT_STATUS)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads((ROOT / args.report).read_text(encoding="utf-8"))
    changed = 0
    samples: list[str] = []
    for item in queue_items(payload):
        source_rel = str(item.get("source_path") or "")
        raw_rel = str(item.get("raw_path") or "")
        reason = str(item.get("reason") or "fulltext not available")
        if mark_source(source_rel, raw_rel, args.date, reason, args.status, args.dry_run):
            changed += 1
            if len(samples) < 30:
                samples.append(f"- {source_rel} -> {args.status}")

    print("tools/mark_terminal_harvest_exceptions.py")
    print(f"  mode: {'dry-run' if args.dry_run else 'applied'}")
    print(f"  marked: {changed}")
    for sample in samples:
        print(sample)


if __name__ == "__main__":
    main()
