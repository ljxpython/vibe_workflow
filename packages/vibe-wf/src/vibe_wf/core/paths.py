from __future__ import annotations

from pathlib import Path


def resolve_target(target: str) -> Path:
    p = Path(target).expanduser()
    # Preserve relative targets (e.g. ".") but normalize for checks.
    return p.resolve()


def ensure_within_target(target_root: Path, path: Path) -> None:
    # Use absolute/normalized paths for boundary checks.
    target_root = target_root.resolve()
    path = path.resolve()

    try:
        path.relative_to(target_root)
    except ValueError as e:
        raise ValueError(f"Refusing to write outside target: {path}") from e
