"""
Windows Task Scheduler registration helper for the auto-collector.

Usage:
  python tools/register_scheduler.py preview        # show the schtasks commands
  python tools/register_scheduler.py register       # register all 3 daily tasks
  python tools/register_scheduler.py unregister     # remove all tasks
  python tools/register_scheduler.py status         # check current state

Default schedule: 3x daily — morning (07:00), noon (12:00), evening (19:00).
Override with --times HH:MM,HH:MM,HH:MM.

Task names: CyberCrimeIC_AM / CyberCrimeIC_NOON / CyberCrimeIC_PM

Outputs are appended to tools/collect.log.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BAT_PATH = PROJECT_ROOT / "tools" / "scheduled_collect.bat"

# Default 3x daily schedule
DEFAULT_SCHEDULES: list[tuple[str, str]] = [
    ("CyberCrimeIC_AM",   "07:00"),
    ("CyberCrimeIC_NOON", "12:00"),
    ("CyberCrimeIC_PM",   "19:00"),
]

# Legacy single-task name (for cleanup)
LEGACY_TASK_NAME = "CyberCrimeIC_AutoCollect"


def _build_register_cmd(task_name: str, time_str: str) -> list[str]:
    return [
        "schtasks",
        "/Create",
        "/SC", "DAILY",
        "/TN", task_name,
        "/TR", f'"{BAT_PATH}"',
        "/ST", time_str,
        "/F",
    ]


def _build_delete_cmd(task_name: str) -> list[str]:
    return ["schtasks", "/Delete", "/TN", task_name, "/F"]


def _build_query_cmd(task_name: str) -> list[str]:
    return ["schtasks", "/Query", "/TN", task_name, "/V", "/FO", "LIST"]


def _run(cmd: list[str], *, silent: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if not silent:
        if result.stdout.strip():
            print(result.stdout.strip())
    return result


def _parse_schedules(times_csv: str) -> list[tuple[str, str]]:
    """Parse comma-separated HH:MM into (task_name, time) tuples."""
    labels = ["AM", "NOON", "PM", "EVE", "NIGHT"]
    times = [t.strip() for t in times_csv.split(",") if t.strip()]
    result = []
    for i, t in enumerate(times):
        label = labels[i] if i < len(labels) else f"T{i}"
        result.append((f"CyberCrimeIC_{label}", t))
    return result


def _remove_legacy_task() -> None:
    """Remove the old single-task if it exists."""
    r = subprocess.run(
        ["schtasks", "/Query", "/TN", LEGACY_TASK_NAME],
        capture_output=True, text=True, errors="replace",
    )
    if r.returncode == 0:
        print(f"  Removing legacy task '{LEGACY_TASK_NAME}'...")
        _run(_build_delete_cmd(LEGACY_TASK_NAME), silent=True)
        print(f"  [OK] Legacy task removed.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Register the auto-collector with Windows Task Scheduler (3x daily)",
    )
    parser.add_argument("action", choices=["preview", "register", "unregister", "status"])
    parser.add_argument(
        "--times",
        default="07:00,12:00,19:00",
        help="Comma-separated HH:MM times (default: 07:00,12:00,19:00)",
    )
    args = parser.parse_args()

    if not BAT_PATH.exists():
        print(f"ERROR: Batch script not found at {BAT_PATH}", file=sys.stderr)
        sys.exit(1)

    schedules = _parse_schedules(args.times)

    if args.action == "preview":
        print("Would register the following tasks:\n")
        for name, time_str in schedules:
            cmd = _build_register_cmd(name, time_str)
            print(f"  {name} at {time_str}")
            print(f"    {' '.join(cmd)}")
        print(f"\nBatch script: {BAT_PATH}")
        print(f"Logs: {PROJECT_ROOT / 'tools' / 'collect.log'}")
        return

    if args.action == "register":
        _remove_legacy_task()
        ok_count = 0
        for name, time_str in schedules:
            cmd = _build_register_cmd(name, time_str)
            print(f"Registering {name} at {time_str}...")
            result = _run(cmd, silent=True)
            if result.returncode != 0:
                print(f"  [FAIL] {name}: {result.stderr.strip()}")
            else:
                print(f"  [OK] {name} registered.")
                ok_count += 1
        print(f"\n{ok_count}/{len(schedules)} tasks registered.")
        if ok_count == len(schedules):
            times_str = ", ".join(t for _, t in schedules)
            print(f"Auto-collector will run daily at: {times_str}")
        print("To verify: python tools/register_scheduler.py status")
        return

    if args.action == "unregister":
        _remove_legacy_task()
        for name, _ in schedules:
            print(f"Removing {name}...")
            result = _run(_build_delete_cmd(name), silent=True)
            if result.returncode != 0:
                print(f"  [SKIP] {name} not found.")
            else:
                print(f"  [OK] {name} removed.")
        print("\nAll auto-collect tasks removed.")
        return

    if args.action == "status":
        found = 0
        for name, expected_time in schedules:
            result = _run(_build_query_cmd(name), silent=True)
            if result.returncode != 0:
                print(f"  {name} ({expected_time}): NOT registered")
            else:
                print(f"  {name} ({expected_time}): REGISTERED")
                # Extract next run time from output
                for line in result.stdout.splitlines():
                    if "Next Run Time" in line or "Status" in line:
                        print(f"    {line.strip()}")
                found += 1
        # Also check legacy
        r = subprocess.run(
            ["schtasks", "/Query", "/TN", LEGACY_TASK_NAME],
            capture_output=True, text=True, errors="replace",
        )
        if r.returncode == 0:
            print(f"\n  [WARN] Legacy task '{LEGACY_TASK_NAME}' still exists.")
            print(f"  Run 'register' to migrate to 3x daily schedule.")
        print(f"\n{found}/{len(schedules)} tasks active.")
        return


if __name__ == "__main__":
    main()
