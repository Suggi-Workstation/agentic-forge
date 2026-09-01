#!/usr/bin/env python3
"""Emit deterministic Forge status for the Hermes cron monitor gate."""

import argparse
from datetime import date, datetime, timezone
import sys
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--date",
        default="",
        help="UTC date override for deterministic tests (YYYY-MM-DD)",
    )
    args = parser.parse_args(argv)
    status_path = args.root.resolve() / "STATUS.md"
    try:
        status = status_path.read_text(encoding="ascii")
    except OSError as exc:
        print(f"STATUS_UNAVAILABLE: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print("STATUS_UNAVAILABLE: STATUS.md is not ASCII", file=sys.stderr)
        return 1

    if not status.strip():
        print("STATUS_UNAVAILABLE: STATUS.md is empty", file=sys.stderr)
        return 1

    try:
        day = date.fromisoformat(args.date) if args.date else datetime.now(
            timezone.utc
        ).date()
    except ValueError:
        print("STATUS_UNAVAILABLE: --date must be YYYY-MM-DD", file=sys.stderr)
        return 1

    state = ""
    for line in status.splitlines():
        if line.startswith("state:"):
            state = line.split(":", 1)[1].strip()
            break

    sys.stdout.write(status)
    if not status.endswith("\n"):
        sys.stdout.write("\n")
    if state == "ready":
        sys.stdout.write(f"cadence-day: {day.isoformat()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
