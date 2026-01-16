from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .bundle import load_v1_bundle
from .fs import atomic_write_text, atomic_write_bytes, copy_to_backup
from .hashing import sha256_file
from .manifest import ManagedFile, ProjectManifest
from .paths import ensure_within_target


@dataclass(frozen=True)
class ApplyResult:
    created: int
    overwritten: int
    skipped: int
    conflicts: tuple[str, ...]
    target: Path
    manifest_path: Path


@dataclass(frozen=True)
class DoctorResult:
    installed: bool
    total: int
    ok: int
    modified: int
    missing: int


@dataclass(frozen=True)
class UninstallResult:
    removed: int
    kept_modified: int
    missing: int


def apply_v1_bundle(target_root: Path, *, dry_run: bool, force: bool) -> ApplyResult:
    spec, bundle_root = load_v1_bundle()

    files_root = bundle_root / spec.files_root
    state_dir = target_root / spec.managed_dir
    manifest_path = state_dir / "manifest.json"
    version_path = state_dir / "version.json"

    existing: ProjectManifest | None = None
    if manifest_path.exists():
        existing = ProjectManifest.load(manifest_path)

    existing_map = {f.path: f.sha256 for f in existing.managed_files} if existing else {}

    planned: list[tuple[str, str]] = []
    conflicts: list[str] = []

    for rel in spec.copy:
        src = files_root / rel
        if not src.is_file():
            raise FileNotFoundError(f"Bundle is missing file: {rel}")

        dest = target_root / rel
        ensure_within_target(target_root, dest)

        if dest.exists():
            if dest.is_dir():
                conflicts.append(rel)
                planned.append((rel, "conflict"))
                continue

            if sha256_file(dest) == sha256_file(src):
                planned.append((rel, "skip"))
                continue

            if existing_map.get(rel) == sha256_file(dest):
                planned.append((rel, "overwrite"))
                continue

            if force:
                planned.append((rel, "overwrite"))
            else:
                planned.append((rel, "conflict"))
                conflicts.append(rel)
        else:
            planned.append((rel, "create"))

    if conflicts and not force:
        return ApplyResult(
            created=0,
            overwritten=0,
            skipped=0,
            conflicts=tuple(conflicts),
            target=target_root,
            manifest_path=manifest_path,
        )

    created = overwritten = skipped = 0

    if dry_run:
        for _, action in planned:
            if action == "create":
                created += 1
            elif action == "overwrite":
                overwritten += 1
            elif action == "skip":
                skipped += 1
        return ApplyResult(
            created=created,
            overwritten=overwritten,
            skipped=skipped,
            conflicts=tuple(conflicts),
            target=target_root,
            manifest_path=manifest_path,
        )

    state_dir.mkdir(parents=True, exist_ok=True)

    backup_dir: Path | None = None
    if any(action == "overwrite" for _, action in planned):
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_dir = state_dir / "backup" / ts
        backup_dir.mkdir(parents=True, exist_ok=True)

    managed_files: list[ManagedFile] = []

    for rel, action in planned:
        src = files_root / rel
        dest = target_root / rel

        if action == "skip":
            skipped += 1
        else:
            if dest.exists() and backup_dir is not None and action == "overwrite":
                copy_to_backup(dest, backup_dir, rel)

            atomic_write_bytes(dest, src.read_bytes())

            if action == "create":
                created += 1
            elif action == "overwrite":
                overwritten += 1

        managed_files.append(ManagedFile(path=rel, sha256=sha256_file(dest)))

    new_manifest = ProjectManifest(
        schema_version=1,
        bundle_id=spec.bundle_id,
        bundle_version=spec.bundle_version,
        managed_files=tuple(managed_files),
    )

    atomic_write_text(manifest_path, json.dumps(
        {
            "schema_version": new_manifest.schema_version,
            "bundle_id": new_manifest.bundle_id,
            "bundle_version": new_manifest.bundle_version,
            "managed_files": [
                {"path": f.path, "sha256": f.sha256} for f in new_manifest.managed_files
            ],
        },
        indent=2,
        sort_keys=True,
    ) + "\n")

    atomic_write_text(
        version_path,
        json.dumps(
            {
                "bundle_id": spec.bundle_id,
                "bundle_version": spec.bundle_version,
                "installed_at": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )

    return ApplyResult(
        created=created,
        overwritten=overwritten,
        skipped=skipped,
        conflicts=tuple(conflicts),
        target=target_root,
        manifest_path=manifest_path,
    )


def doctor_v1(target_root: Path) -> DoctorResult:
    spec, _ = load_v1_bundle()

    state_dir = target_root / spec.managed_dir
    manifest_path = state_dir / "manifest.json"

    if not manifest_path.exists():
        return DoctorResult(installed=False, total=0, ok=0, modified=0, missing=0)

    manifest = ProjectManifest.load(manifest_path)

    total = len(manifest.managed_files)
    ok = modified = missing = 0

    for item in manifest.managed_files:
        p = target_root / item.path
        if not p.exists():
            missing += 1
            continue
        if p.is_dir():
            missing += 1
            continue
        if sha256_file(p) != item.sha256:
            modified += 1
            continue
        ok += 1

    return DoctorResult(installed=True, total=total, ok=ok, modified=modified, missing=missing)


def uninstall_v1(target_root: Path, *, dry_run: bool, force: bool) -> UninstallResult:
    spec, _ = load_v1_bundle()

    state_dir = target_root / spec.managed_dir
    manifest_path = state_dir / "manifest.json"
    version_path = state_dir / "version.json"

    if not manifest_path.exists():
        return UninstallResult(removed=0, kept_modified=0, missing=0)

    manifest = ProjectManifest.load(manifest_path)

    removed = kept_modified = missing = 0

    for item in manifest.managed_files:
        p = target_root / item.path
        ensure_within_target(target_root, p)

        if not p.exists():
            missing += 1
            continue
        if p.is_dir():
            missing += 1
            continue

        if sha256_file(p) != item.sha256 and not force:
            kept_modified += 1
            continue

        if not dry_run:
            p.unlink()
        removed += 1

    if not dry_run:
        try:
            manifest_path.unlink()
        except FileNotFoundError:
            pass
        try:
            version_path.unlink()
        except FileNotFoundError:
            pass

    return UninstallResult(removed=removed, kept_modified=kept_modified, missing=missing)
