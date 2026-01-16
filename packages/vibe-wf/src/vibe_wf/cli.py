from __future__ import annotations

import json
import typer

from .core.engine import apply_v1_bundle, doctor_v1, uninstall_v1
from .core.paths import resolve_target

app = typer.Typer(add_completion=False)


@app.command()
def sync(
    target: str = ".",
    force: bool = typer.Option(False, "--force"),
    json_out: bool = typer.Option(False, "--json"),
) -> None:
    target_root = resolve_target(target)
    result = apply_v1_bundle(target_root, dry_run=False, force=force)

    if json_out:
        typer.echo(
            json.dumps(
                {
                    "target": str(result.target),
                    "created": result.created,
                    "overwritten": result.overwritten,
                    "skipped": result.skipped,
                    "conflicts": list(result.conflicts),
                    "manifest": str(result.manifest_path),
                },
                indent=2,
                sort_keys=True,
            )
        )
        raise typer.Exit(code=0 if not result.conflicts else 2)

    typer.echo(f"[vibe-wf] target: {result.target}")
    if result.conflicts:
        typer.echo("[vibe-wf] conflicts detected (use --force to overwrite):")
        for p in result.conflicts:
            typer.echo(f"- {p}")
        raise typer.Exit(code=2)

    typer.echo(
        f"[vibe-wf] done: created={result.created} overwritten={result.overwritten} skipped={result.skipped}"
    )


@app.command()
def init(
    target: str = ".",
    dry_run: bool = typer.Option(False, "--dry-run"),
    force: bool = typer.Option(False, "--force"),
    json_out: bool = typer.Option(False, "--json"),
) -> None:
    target_root = resolve_target(target)
    result = apply_v1_bundle(target_root, dry_run=dry_run, force=force)

    if json_out:
        typer.echo(
            json.dumps(
                {
                    "target": str(result.target),
                    "created": result.created,
                    "overwritten": result.overwritten,
                    "skipped": result.skipped,
                    "conflicts": list(result.conflicts),
                    "manifest": str(result.manifest_path),
                },
                indent=2,
                sort_keys=True,
            )
        )
        raise typer.Exit(code=0 if not result.conflicts else 2)

    typer.echo(f"[vibe-wf] target: {result.target}")
    if result.conflicts:
        typer.echo("[vibe-wf] conflicts detected (use --force to overwrite):")
        for p in result.conflicts:
            typer.echo(f"- {p}")
        raise typer.Exit(code=2)

    typer.echo(
        f"[vibe-wf] done: created={result.created} overwritten={result.overwritten} skipped={result.skipped}"
    )


@app.command()
def doctor(
    target: str = ".",
    json_out: bool = typer.Option(False, "--json"),
) -> None:
    target_root = resolve_target(target)
    result = doctor_v1(target_root)

    if json_out:
        typer.echo(
            json.dumps(
                {
                    "installed": result.installed,
                    "total": result.total,
                    "ok": result.ok,
                    "modified": result.modified,
                    "missing": result.missing,
                },
                indent=2,
                sort_keys=True,
            )
        )
        raise typer.Exit(code=0 if result.installed and result.missing == 0 else 2)

    if not result.installed:
        typer.echo("[vibe-wf] not installed (no manifest)")
        raise typer.Exit(code=2)

    typer.echo(
        f"[vibe-wf] ok={result.ok}/{result.total} modified={result.modified} missing={result.missing}"
    )
    raise typer.Exit(code=0 if result.missing == 0 else 2)


@app.command()
def uninstall(
    target: str = ".",
    dry_run: bool = typer.Option(False, "--dry-run"),
    force: bool = typer.Option(False, "--force"),
    json_out: bool = typer.Option(False, "--json"),
) -> None:
    target_root = resolve_target(target)
    result = uninstall_v1(target_root, dry_run=dry_run, force=force)

    if json_out:
        typer.echo(
            json.dumps(
                {
                    "removed": result.removed,
                    "kept_modified": result.kept_modified,
                    "missing": result.missing,
                },
                indent=2,
                sort_keys=True,
            )
        )
        raise typer.Exit(code=0)

    typer.echo(
        f"[vibe-wf] removed={result.removed} kept_modified={result.kept_modified} missing={result.missing}"
    )


def main() -> None:
    import sys

    if len(sys.argv) == 1:
        from .menu import run_menu

        run_menu()
        return

    app()
