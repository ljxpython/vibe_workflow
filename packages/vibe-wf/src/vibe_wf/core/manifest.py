from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ManagedFile:
    path: str
    sha256: str


@dataclass(frozen=True)
class ProjectManifest:
    schema_version: int
    bundle_id: str
    bundle_version: str
    managed_files: tuple[ManagedFile, ...]

    @staticmethod
    def load(path: Path) -> "ProjectManifest":
        data = json.loads(path.read_text(encoding="utf-8"))
        files = tuple(ManagedFile(**item) for item in data.get("managed_files", []))
        return ProjectManifest(
            schema_version=int(data["schema_version"]),
            bundle_id=str(data["bundle_id"]),
            bundle_version=str(data["bundle_version"]),
            managed_files=files,
        )

    def dump(self, path: Path) -> None:
        data = {
            "schema_version": self.schema_version,
            "bundle_id": self.bundle_id,
            "bundle_version": self.bundle_version,
            "managed_files": [
                {"path": f.path, "sha256": f.sha256} for f in self.managed_files
            ],
        }
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
