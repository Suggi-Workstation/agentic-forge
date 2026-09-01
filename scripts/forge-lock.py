#!/usr/bin/env python3
"""Atomic lease lock for Researcher and Analyst Forge runs."""

import argparse
import json
import os
import secrets
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


LOCK_NAME = ".forge-lock"
LEASE_NAME = "lease.json"
OWNERS = ("researcher", "analyst")


class LockError(RuntimeError):
    """A safe, expected lock refusal."""


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def lease_path(root):
    return root / LOCK_NAME / LEASE_NAME


def read_lease(root):
    try:
        return json.loads(lease_path(root).read_text(encoding="ascii"))
    except (OSError, ValueError, TypeError):
        return None


def write_lease(root, payload):
    path = lease_path(root)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(payload, sort_keys=True) + "\n",
        encoding="ascii",
    )
    os.replace(temporary, path)


def new_lease(owner, lease_seconds, reclaimed):
    now = time.time()
    return {
        "owner": owner,
        "token": secrets.token_hex(16),
        "acquired_at": utc_now(),
        "heartbeat_at": utc_now(),
        "heartbeat_epoch": now,
        "lease_seconds": lease_seconds,
        "reclaimed": reclaimed,
    }


def is_stale(lease):
    if not lease:
        return True
    try:
        heartbeat = float(lease["heartbeat_epoch"])
        lease_seconds = float(lease["lease_seconds"])
    except (KeyError, TypeError, ValueError):
        return True
    return time.time() - heartbeat > lease_seconds


def remove_lock_dir(path):
    lease = path / LEASE_NAME
    temporary = lease.with_suffix(".tmp")
    if temporary.exists():
        temporary.unlink()
    if lease.exists():
        lease.unlink()
    path.rmdir()


def acquire(root, owner, lease_seconds):
    if owner not in OWNERS:
        raise LockError("owner must be researcher or analyst")
    if lease_seconds <= 0:
        raise LockError("lease-seconds must be positive")

    root.mkdir(parents=True, exist_ok=True)
    lock_dir = root / LOCK_NAME
    reclaimed = False

    for _ in range(3):
        try:
            lock_dir.mkdir(mode=0o700)
            payload = new_lease(owner, lease_seconds, reclaimed)
            write_lease(root, payload)
            return payload
        except FileExistsError:
            current = read_lease(root)
            if not is_stale(current):
                holder = current.get("owner", "unknown") if current else "unknown"
                raise LockError(f"LOCKED by {holder}")

            stale_dir = root / f"{LOCK_NAME}-stale-{secrets.token_hex(8)}"
            try:
                os.replace(lock_dir, stale_dir)
            except FileNotFoundError:
                continue
            try:
                remove_lock_dir(stale_dir)
            finally:
                if stale_dir.exists():
                    raise LockError(f"stale lock cleanup failed: {stale_dir}")
            reclaimed = True

    raise LockError("LOCKED: acquisition race did not settle")


def require_token(root, token):
    current = read_lease(root)
    if not current:
        raise LockError("LOCKED state is missing or unreadable")
    if not secrets.compare_digest(str(current.get("token", "")), token):
        raise LockError("LOCKED token mismatch")
    return current


def heartbeat(root, token):
    current = require_token(root, token)
    current["heartbeat_at"] = utc_now()
    current["heartbeat_epoch"] = time.time()
    write_lease(root, current)
    return current


def release(root, token):
    current = require_token(root, token)
    remove_lock_dir(root / LOCK_NAME)
    return {"released": True, "owner": current["owner"]}


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    acquire_parser = subparsers.add_parser("acquire")
    acquire_parser.add_argument("--owner", required=True, choices=OWNERS)
    acquire_parser.add_argument("--lease-seconds", type=float, default=2700.0)
    acquire_parser.add_argument("--root", type=Path, required=True)

    heartbeat_parser = subparsers.add_parser("heartbeat")
    heartbeat_parser.add_argument("--token", required=True)
    heartbeat_parser.add_argument("--root", type=Path, required=True)

    release_parser = subparsers.add_parser("release")
    release_parser.add_argument("--token", required=True)
    release_parser.add_argument("--root", type=Path, required=True)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "acquire":
            result = acquire(root, args.owner, args.lease_seconds)
        elif args.command == "heartbeat":
            result = heartbeat(root, args.token)
        else:
            result = release(root, args.token)
    except LockError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
