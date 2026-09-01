#!/usr/bin/env python3
"""Tests for the Forge-local cross-profile lease lock."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCK_SCRIPT = REPO_ROOT / "scripts" / "forge-lock.py"
PYTHON = "/opt/repo-tools/venv/bin/python"


class ForgeLockTests(unittest.TestCase):
    def run_lock(self, root, *args):
        return subprocess.run(
            [PYTHON, str(LOCK_SCRIPT), *args, "--root", str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_lock_blocks_second_owner_and_releases_by_token(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = self.run_lock(
                root,
                "acquire",
                "--owner",
                "researcher",
                "--lease-seconds",
                "60",
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            token = json.loads(first.stdout)["token"]

            blocked = self.run_lock(
                root,
                "acquire",
                "--owner",
                "analyst",
                "--lease-seconds",
                "60",
            )
            self.assertEqual(blocked.returncode, 2)
            self.assertIn("LOCKED", blocked.stderr)

            heartbeat = self.run_lock(root, "heartbeat", "--token", token)
            self.assertEqual(heartbeat.returncode, 0, heartbeat.stderr)

            wrong = self.run_lock(root, "release", "--token", "wrong-token")
            self.assertEqual(wrong.returncode, 2)
            self.assertTrue((root / ".forge-lock" / "lease.json").exists())

            released = self.run_lock(root, "release", "--token", token)
            self.assertEqual(released.returncode, 0, released.stderr)
            self.assertFalse((root / ".forge-lock").exists())

    def test_stale_lock_is_reclaimed_with_a_new_token(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = self.run_lock(
                root,
                "acquire",
                "--owner",
                "researcher",
                "--lease-seconds",
                "60",
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            lease_path = root / ".forge-lock" / "lease.json"
            lease = json.loads(lease_path.read_text(encoding="ascii"))
            lease["heartbeat_epoch"] = 0
            lease_path.write_text(json.dumps(lease), encoding="ascii")

            reclaimed = self.run_lock(
                root,
                "acquire",
                "--owner",
                "analyst",
                "--lease-seconds",
                "60",
            )
            self.assertEqual(reclaimed.returncode, 0, reclaimed.stderr)
            payload = json.loads(reclaimed.stdout)
            self.assertTrue(payload["reclaimed"])
            self.assertNotEqual(payload["token"], lease["token"])


class LogbookArchiveTests(unittest.TestCase):
    def run_archive(self, root):
        script = REPO_ROOT / "scripts" / "logbook-archive.py"
        return subprocess.run(
            [PYTHON, str(script)],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

    def write_large_ent_log(self, path, actor, category):
        header = (
            f"<!-- {path.name} -- Forge {category} events.\n"
            "    Append complete ENT blocks only.\n"
            "    See logbook/protocol.md.\n"
            "-->\n\n"
        )
        entries = []
        for index in range(1, 171):
            entries.append(
                f"## [ENT-{index:03d}] | 2026-09-01 00:00 UTC | "
                f"{actor} | {category} | ref: STATUS.md\n"
                f"Completed bounded Forge event {index}.\n\n"
            )
        path.write_text(header + "".join(entries), encoding="ascii")

    def assert_archived_without_split(self, root, name):
        active_path = root / "logbook" / f"{name}.log"
        archives = list((root / "logbook" / "archive").glob(f"{name}-*.log"))
        self.assertEqual(len(archives), 1)
        active = active_path.read_text(encoding="ascii")
        archived = archives[0].read_text(encoding="ascii")
        self.assertLessEqual(len(active.splitlines()), 400)
        self.assertIn("ENT-170", active)
        self.assertIn("ENT-001", archived)
        self.assertNotIn("ENT-001", active)
        for index in range(1, 171):
            token = f"ENT-{index:03d}"
            self.assertEqual((active + archived).count(f"## [{token}]"), 1)

    def test_progress_log_archives_complete_ent_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive_dir = root / "logbook" / "archive"
            archive_dir.mkdir(parents=True)
            progress = root / "logbook" / "progress.log"
            self.write_large_ent_log(progress, "Researcher", "research")

            result = self.run_archive(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_archived_without_split(root, "progress")

    def test_error_log_archives_only_complete_ent_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive_dir = root / "logbook" / "archive"
            archive_dir.mkdir(parents=True)
            errors = root / "logbook" / "errors.log"
            self.write_large_ent_log(errors, "Analyst", "error")

            result = self.run_archive(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_archived_without_split(root, "errors")


if __name__ == "__main__":
    unittest.main()
