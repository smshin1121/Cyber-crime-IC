"""
Windows Task Scheduler registration helper for the auto-collector.

Usage:
  python tools/register_scheduler.py preview        # show the schtasks command
  python tools/register_scheduler.py register       # actually register
  python tools/register_scheduler.py unregister     # remove the task
  python tools/register_scheduler.py status         # check current state

Default schedule: every day at 07:00 local time.
Override with --time HH:MM and --frequency DAILY|HOURLY|WEEKLY.

The task name is "CyberCrimeIC_AutoCollect". It runs:
  C:\\Users\\shin1121\\Desktop\\Cyber_crime_IC\\tools\\scheduled_collect.bat

Outputs are appended to tools/collect.log.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TASK_NAME = "CyberCrimeIC_AutoCollect"
BAT_PATH = PROJECT_ROOT / "tools" / "scheduled_collect.bat"


def build_register_cmd(time_str: str, frequency: str) -> list[str]:
    return [
        "schtasks",
        "/Create",
        "/SC", frequency,
        "/TN", TASK_NAME,
        "/TR", f'"{BAT_PATH}"',
        "/ST", time_str,
        "/F",  # force overwrite if exists
    ]


def build_unregister_cmd() -> list[str]:
    return ["schtasks", "/Delete", "/TN", TASK_NAME, "/F"]


def build_status_cmd() -> list[str]:
    return ["schtasks", "/Query", "/TN", TASK_NAME, "/V", "/FO", "LIST"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Register the auto-collector with Windows Task Scheduler")
    parser.add_argument("action", choices=["preview", "register", "unregister", "status"])
    parser.add_argument("--time", default="07:00", help="Local time HH:MM (default: 07:00)")
    parser.add_argument(
        "--frequency",
        default="DAILY",
        choices=["DAILY", "HOURLY", "WEEKLY", "MINUTE"],
        help="Schedule frequency (default: DAILY)",
    )
    args = parser.parse_args()

    if not BAT_PATH.exists():
        print(f"ERROR: Batch script not found at {BAT_PATH}", file=sys.stderr)
        sys.exit(1)

    if args.action == "preview":
        cmd = build_register_cmd(args.time, args.frequency)
        print("Would run:")
        print("  " + " ".join(cmd))
        print()
        print("This registers the auto-collector to run", end=" ")
        if args.frequency == "DAILY":
            print(f"every day at {args.time}.")
        elif args.frequency == "HOURLY":
            print("every hour.")
        elif args.frequency == "WEEKLY":
            print(f"every week.")
        print(f"Batch script: {BAT_PATH}")
        print(f"Logs: {PROJECT_ROOT / 'tools' / 'collect.log'}")
        return

    if args.action == "register":
        cmd = build_register_cmd(args.time, args.frequency)
        print("Running: " + " ".join(cmd))
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"ERROR: {result.stderr}", file=sys.stderr)
            sys.exit(result.returncode)
        print(f"\n[OK] Task '{TASK_NAME}' registered. Will run {args.frequency.lower()} at {args.time}.")
        print("To verify: python tools/register_scheduler.py status")
        return

    if args.action == "unregister":
        cmd = build_unregister_cmd()
        print("Running: " + " ".join(cmd))
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"ERROR: {result.stderr}", file=sys.stderr)
            sys.exit(result.returncode)
        print(f"[OK] Task '{TASK_NAME}' removed.")
        return

    if args.action == "status":
        cmd = build_status_cmd()
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Task '{TASK_NAME}' is NOT registered.")
            print(f"Run: python tools/register_scheduler.py register")
            sys.exit(0)
        print(result.stdout)
        return


if __name__ == "__main__":
    main()
