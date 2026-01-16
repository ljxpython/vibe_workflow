from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import as_file, files
from pathlib import Path


@dataclass(frozen=True)
class BundleSpec:
    schema_version: int
    bundle_id: str
    bundle_version: str
    description: str
    files_root: str
    managed_dir: str
    copy: tuple[str, ...]


def load_v1_bundle() -> tuple[BundleSpec, Path]:

    bundle_pkg = "vibe_wf.bundles.v1"
    manifest_res = files(bundle_pkg).joinpath("manifest.json")

    with as_file(manifest_res) as manifest_path:
        bundle_root = manifest_path.parent
        spec_data = json.loads(manifest_path.read_text(encoding="utf-8"))

    install = spec_data["install"]
    spec = BundleSpec(
        schema_version=int(spec_data["schema_version"]),
        bundle_id=str(spec_data["bundle_id"]),
        bundle_version=str(spec_data["bundle_version"]),
        description=str(spec_data.get("description", "")),
        files_root=str(spec_data.get("files_root", "files")),
        managed_dir=str(spec_data.get("managed_dir", ".vibe-wf")),
        copy=tuple(install.get("copy", [])),
    )

    return spec, bundle_root
