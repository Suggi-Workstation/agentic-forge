#!/usr/bin/env python3
"""Regression tests for Forge locking, logs, and workflow contracts."""

import fcntl
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOCK_SCRIPT = REPO_ROOT / "scripts" / "forge-lock.py"
MONITOR_SCRIPT = REPO_ROOT / "scripts" / "forge-status-monitor.py"
PYTHON = sys.executable


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

    def test_metadata_operations_wait_for_the_guard_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            guard_path = root / ".forge-lock.guard"
            with guard_path.open("a+", encoding="ascii") as guard:
                fcntl.flock(guard.fileno(), fcntl.LOCK_EX)
                process = subprocess.Popen(
                    [
                        PYTHON,
                        str(LOCK_SCRIPT),
                        "acquire",
                        "--owner",
                        "researcher",
                        "--lease-seconds",
                        "60",
                        "--root",
                        str(root),
                    ],
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                try:
                    import time

                    time.sleep(0.2)
                    self.assertIsNone(
                        process.poll(),
                        "acquire bypassed the metadata guard",
                    )
                finally:
                    fcntl.flock(guard.fileno(), fcntl.LOCK_UN)
                stdout, stderr = process.communicate(timeout=5)
                self.assertEqual(process.returncode, 0, stderr)
                self.assertIn("token", stdout)


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


class StatusMonitorTests(unittest.TestCase):
    def run_monitor(self, root, day=None):
        command = [PYTHON, str(MONITOR_SCRIPT), "--root", str(root)]
        if day:
            command.extend(("--date", day))
        return subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_monitor_is_deterministic_and_changes_with_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            status = root / "STATUS.md"
            status.write_text("state: ready\nstage: ideate\n", encoding="ascii")

            first = self.run_monitor(root)
            second = self.run_monitor(root)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)

            status.write_text("state: active\nstage: propose\n", encoding="ascii")
            changed = self.run_monitor(root)
            self.assertEqual(changed.returncode, 0, changed.stderr)
            self.assertNotEqual(first.stdout, changed.stdout)

    def test_ready_state_wakes_daily_but_active_state_does_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            status = root / "STATUS.md"
            status.write_text("state: ready\nstage: ideate\n", encoding="ascii")
            first_day = self.run_monitor(root, "2026-09-01")
            next_day = self.run_monitor(root, "2026-09-02")
            self.assertNotEqual(first_day.stdout, next_day.stdout)

            status.write_text("state: active\nstage: propose\n", encoding="ascii")
            active_first = self.run_monitor(root, "2026-09-01")
            active_next = self.run_monitor(root, "2026-09-02")
            self.assertEqual(active_first.stdout, active_next.stdout)


class RepositoryContractTests(unittest.TestCase):
    def run_validator(self, root):
        validator = REPO_ROOT / "scripts" / "validate-forge.py"
        return subprocess.run(
            [PYTHON, str(validator), "--root", str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def copy_repo(self, destination):
        shutil.copytree(
            REPO_ROOT,
            destination,
            ignore=shutil.ignore_patterns(
                ".git", "__pycache__", "*.pyc", "eval-results.json"
            ),
        )

    def write_artifact(
        self,
        root,
        directory,
        stage,
        owner,
        artifact_id,
        pipeline,
        parent,
        body,
        filename="test-topic-r01.md",
    ):
        path = root / "forge" / directory / filename
        path.write_text(
            "---\n"
            "name: test-topic\n"
            f"id: {artifact_id}\n"
            f"pipeline: {pipeline}\n"
            "research_path: agent-systems\n"
            f"stage: {stage}\n"
            f"owner: {owner}\n"
            "status: complete\n"
            f"parent: {parent}\n"
            "supersedes: none\n"
            "confidence: 0.5\n"
            "created: 2026-08-01T12:00:01Z\n"
            "---\n\n"
            f"{body}\n",
            encoding="ascii",
        )
        return path

    def test_repository_contract_passes(self):
        result = self.run_validator(REPO_ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("FORGE CONTRACT PASS", result.stdout)

    def test_validator_rejects_non_ent_progress_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            progress = root / "logbook" / "progress.log"
            with progress.open("a", encoding="ascii") as handle:
                handle.write("2026-09-01T17:45:00Z | research | PASS\n")

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("non-ENT content before first entry", result.stdout)

    def test_validator_rejects_direct_cross_repo_path_in_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            skill = root / "governance" / "skills" / "forge-research" / "SKILL.md"
            with skill.open("a", encoding="ascii") as handle:
                handle.write("\nRun git -C /srv/brain/agentic-brain commit.\n")

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("forbidden skill token", result.stdout)

    def test_validator_rejects_invalid_stage_owner_pair(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            status = root / "STATUS.md"
            text = status.read_text(encoding="ascii")
            status.write_text(
                text.replace("owner: Researcher", "owner: Analyst"),
                encoding="ascii",
            )

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("invalid stage/owner pair", result.stdout)

    def test_validator_rejects_artifact_missing_stage_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            artifact_id = "20260801T120001Z"
            self.write_artifact(
                root,
                "ideas",
                "idea",
                "Researcher",
                artifact_id,
                artifact_id,
                "root",
                "# Empty Idea",
            )

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("artifact missing required section", result.stdout)

    def test_validator_rejects_cross_pipeline_parent(self):
        idea_body = "\n".join(
            (
                "# Idea",
                "## Research Path",
                "## Research Question",
                "## Hypothesis",
                "## Why This Matters",
                "## Prior Work and Non-Duplication",
                "## Claims to Test",
                "## Expected Build",
                "## Kill Criteria",
                "## Initial Confidence",
            )
        )
        proposal_body = "\n".join(
            (
                "# Proposal",
                "## Research Question",
                "## Decision This Research Will Inform",
                "## Claim and Evidence Map",
                "## Method",
                "## Source Strategy",
                "## Counter-Hypotheses",
                "## Acceptance Tests",
                "## Kill Criteria and Stop Conditions",
                "## Worst Failure and Prevention",
                "## Execution Bound",
            )
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            first = "20260801T120001Z"
            second = "20260801T120002Z"
            self.write_artifact(
                root, "ideas", "idea", "Researcher", first, first,
                "root", idea_body, "first-topic-r01.md"
            )
            self.write_artifact(
                root, "ideas", "idea", "Researcher", second, second,
                "root", idea_body, "second-topic-r01.md"
            )
            self.write_artifact(
                root, "proposals", "proposal", "Researcher",
                "20260801T120003Z", first, second, proposal_body,
            )

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("parent belongs to another pipeline", result.stdout)

    def test_validator_rejects_provenance_cycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            idea = "20260801T120001Z"
            proposal = "20260801T120002Z"
            research = "20260801T120003Z"
            evaluation = "20260801T120004Z"
            templates = root / "governance" / "skills"
            self.write_artifact(
                root, "ideas", "idea", "Researcher", idea, idea, "root",
                (templates / "forge-ideate" / "assets" / "template.md").read_text(
                    encoding="ascii"
                ),
            )
            self.write_artifact(
                root, "proposals", "proposal", "Researcher", proposal,
                idea, evaluation,
                (templates / "forge-propose" / "assets" / "template.md").read_text(
                    encoding="ascii"
                ),
            )
            self.write_artifact(
                root, "research", "research", "Researcher", research,
                idea, proposal,
                (templates / "forge-research" / "assets" / "template.md").read_text(
                    encoding="ascii"
                ),
            )
            self.write_artifact(
                root, "evaluations", "evaluation", "Analyst", evaluation,
                idea, research,
                (templates / "forge-evaluate" / "assets" / "template.md").read_text(
                    encoding="ascii"
                ),
            )

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("provenance cycle", result.stdout)

    def test_validator_rejects_status_pointing_to_non_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            idea = "20260801T120001Z"
            template = (
                root / "governance" / "skills" / "forge-ideate" /
                "assets" / "template.md"
            ).read_text(encoding="ascii")
            self.write_artifact(
                root, "ideas", "idea", "Researcher", idea, idea, "root",
                template,
            )
            status = root / "STATUS.md"
            text = status.read_text(encoding="ascii")
            replacements = {
                "state: ready": "state: active",
                "pipeline: none": f"pipeline: {idea}",
                "research-path: none": "research-path: agent-systems",
                "stage: ideate": "stage: propose",
                "active-artifact: none": "active-artifact: README.md",
            }
            for old, new in replacements.items():
                text = text.replace(old, new)
            status.write_text(text, encoding="ascii")

            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("active STATUS artifact does not match", result.stdout)

    def test_validator_accepts_complete_researcher_analyst_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "forge"
            self.copy_repo(root)
            stages = (
                ("ideas", "idea", "Researcher", "20260801T120001Z", "root", "forge-ideate"),
                (
                    "proposals", "proposal", "Researcher",
                    "20260801T120002Z", "20260801T120001Z", "forge-propose",
                ),
                (
                    "research", "research", "Researcher",
                    "20260801T120003Z", "20260801T120002Z", "forge-research",
                ),
                (
                    "evaluations", "evaluation", "Analyst",
                    "20260801T120004Z", "20260801T120003Z", "forge-evaluate",
                ),
                (
                    "builds", "build", "Researcher", "20260801T120005Z",
                    "20260801T120004Z", "forge-build",
                ),
                (
                    "verifications", "verification", "Analyst",
                    "20260801T120006Z", "20260801T120005Z", "forge-verify",
                ),
            )
            pipeline = stages[0][3]
            skills = root / "governance" / "skills"
            for directory, stage, owner, artifact_id, parent, skill in stages:
                body = (skills / skill / "assets" / "template.md").read_text(
                    encoding="ascii"
                )
                self.write_artifact(
                    root,
                    directory,
                    stage,
                    owner,
                    artifact_id,
                    pipeline,
                    parent,
                    body,
                )

            progress = root / "logbook" / "progress.log"
            with progress.open("a", encoding="ascii") as handle:
                for index, (_, stage, owner, artifact_id, _, _) in enumerate(
                    stages, 1
                ):
                    category = "review" if owner == "Analyst" else "research"
                    handle.write(
                        f"\n## [ENT-{index:03d}] | 2026-08-01 12:00 UTC | "
                        f"{owner} | {category} | ref: STATUS.md | see: {artifact_id}\n"
                        f"Stage: {stage}. Verdict: PASS.\n"
                        f"Artifact: {artifact_id}. Pipeline: {pipeline}.\n"
                        "Handoff recorded in STATUS.md.\n"
                    )

            status = root / "STATUS.md"
            text = status.read_text(encoding="ascii")
            replacements = {
                "state: ready": "state: awaiting-review",
                "pipeline: none": f"pipeline: {pipeline}",
                "research-path: none": "research-path: agent-systems",
                "stage: ideate": "stage: review",
                "owner: Researcher": "owner: Human",
                "active-artifact: none": "active-artifact: forge/verifications/test-topic-r01.md",
                "last-verdict: none": "last-verdict: PASS",
                "last-event: none": "last-event: progress:ENT-006",
                (
                    "next-action: Researcher may run forge-loop-researcher "
                    "and select one anchor path."
                ): "next-action: Human review required.",
            }
            for old, new in replacements.items():
                text = text.replace(old, new)
            status.write_text(text, encoding="ascii")

            result = self.run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
