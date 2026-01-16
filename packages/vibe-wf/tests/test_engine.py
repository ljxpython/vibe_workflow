from __future__ import annotations

from pathlib import Path

from vibe_wf.core.engine import apply_v1_bundle, doctor_v1, uninstall_v1


def test_init_dry_run_reports_conflicts_for_existing_files(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("user", encoding="utf-8")

    res = apply_v1_bundle(tmp_path, dry_run=True, force=False)
    assert res.conflicts
    assert "AGENTS.md" in res.conflicts


def test_apply_then_doctor_then_uninstall_roundtrip(tmp_path: Path) -> None:
    res = apply_v1_bundle(tmp_path, dry_run=False, force=False)
    assert not res.conflicts

    manifest_path = tmp_path / ".vibe-wf" / "manifest.json"
    assert manifest_path.exists()

    doc = doctor_v1(tmp_path)
    assert doc.installed is True
    assert doc.missing == 0

    uninstall = uninstall_v1(tmp_path, dry_run=False, force=False)
    assert uninstall.kept_modified == 0

    assert not manifest_path.exists()


def test_uninstall_keeps_modified_files_without_force(tmp_path: Path) -> None:
    res = apply_v1_bundle(tmp_path, dry_run=False, force=False)
    assert not res.conflicts

    target = tmp_path / "AGENTS.md"
    target.write_text("modified", encoding="utf-8")

    uninstall = uninstall_v1(tmp_path, dry_run=False, force=False)
    assert uninstall.kept_modified >= 1
    assert target.exists()


def test_engine_never_writes_outside_target(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside"
    outside.mkdir()

    marker = outside / "marker.txt"
    marker.write_text("pre", encoding="utf-8")

    apply_v1_bundle(tmp_path, dry_run=False, force=False)

    assert marker.read_text(encoding="utf-8") == "pre"
