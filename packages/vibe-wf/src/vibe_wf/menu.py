from __future__ import annotations

import json

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from .core.engine import apply_v1_bundle, doctor_v1, uninstall_v1
from .core.paths import resolve_target


def _print_banner(console: Console) -> None:
    console.print(
        Panel.fit(
            "VIBE-WF\n\n项目级工作流引导工具（OpenCode + oh-my-opencode）\n\n承诺：只修改项目内文件，不修改系统级配置",
            border_style="cyan",
        )
    )


def run_menu() -> None:
    console = Console()
    _print_banner(console)

    target = "."

    while True:
        console.print("\n请选择功能：")
        console.print("  1. 完整初始化（写入项目内资产与文档）")
        console.print("  2. 同步更新（只覆盖已托管文件；遇到用户改动默认提示冲突）")
        console.print("  +. Doctor（只读诊断）")
        console.print("  -. 卸载（移除工具托管文件）")
        console.print("  T. 更改目标目录（当前：%s）" % target)
        console.print("  Q. 退出")

        choice = Prompt.ask("?", default="Q").strip().lower()

        if choice == "q":
            return

        if choice == "t":
            new_target = Prompt.ask("目标目录", default=target).strip()
            if new_target:
                target = new_target
            continue

        target_root = resolve_target(target)

        if choice == "1":
            res = apply_v1_bundle(target_root, dry_run=False, force=False)
            if res.conflicts:
                console.print("检测到冲突（默认不覆盖）：", style="yellow")
                for p in res.conflicts:
                    console.print(f"- {p}")
                force = Prompt.ask("是否覆盖冲突文件？(y/N)", default="N").strip().lower()
                if force in {"y", "yes"}:
                    res = apply_v1_bundle(target_root, dry_run=False, force=True)
            console.print(
                json.dumps(
                    {
                        "target": str(res.target),
                        "created": res.created,
                        "overwritten": res.overwritten,
                        "skipped": res.skipped,
                        "conflicts": list(res.conflicts),
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
            continue

        if choice == "2":
            res = apply_v1_bundle(target_root, dry_run=False, force=False)
            if res.conflicts:
                console.print("检测到冲突（说明用户修改过或存在同名文件）：", style="yellow")
                for p in res.conflicts:
                    console.print(f"- {p}")
                force = Prompt.ask("是否强制覆盖这些冲突文件？(y/N)", default="N").strip().lower()
                if force in {"y", "yes"}:
                    res = apply_v1_bundle(target_root, dry_run=False, force=True)
            console.print(
                json.dumps(
                    {
                        "target": str(res.target),
                        "created": res.created,
                        "overwritten": res.overwritten,
                        "skipped": res.skipped,
                        "conflicts": list(res.conflicts),
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
            continue

        if choice == "+":
            doc = doctor_v1(target_root)
            console.print(
                json.dumps(
                    {
                        "installed": doc.installed,
                        "total": doc.total,
                        "ok": doc.ok,
                        "modified": doc.modified,
                        "missing": doc.missing,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
            continue

        if choice == "-":
            res = uninstall_v1(target_root, dry_run=False, force=False)
            if res.kept_modified:
                console.print("发现被用户修改过的托管文件（默认保留）：", style="yellow")
                force = Prompt.ask("是否强制删除这些已修改文件？(y/N)", default="N").strip().lower()
                if force in {"y", "yes"}:
                    res = uninstall_v1(target_root, dry_run=False, force=True)
            console.print(
                json.dumps(
                    {
                        "removed": res.removed,
                        "kept_modified": res.kept_modified,
                        "missing": res.missing,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
            continue

        console.print("未知选项。", style="red")
