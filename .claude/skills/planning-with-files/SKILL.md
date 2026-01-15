---
name: planning-with-files
description: |
  本仓库内置 planning-with-files 能力（vendored）：用 task_plan.md/findings.md/progress.md 三文件作为磁盘工作记忆。
  hooks 已通过 .claude/settings.json 启用（PreToolUse/PostToolUse/Stop）。
  用法建议：先 /vibe/pwf-bootstrap 初始化三文件。
---

# Planning with Files (Vendored)

- 初始化三文件：`/vibe/pwf-bootstrap`
- 完成性检查（Stop hook）：`bash planning-with-files/scripts/check-complete.sh task_plan.md`
