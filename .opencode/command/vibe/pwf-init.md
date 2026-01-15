---
description: 运行 planning-with-files 官方模板初始化（init-session.sh）
agent: build
---

目标：用 planning-with-files 的官方脚本初始化 3-file 工作记忆（task_plan/findings/progress），模板比 `/vibe/pwf-bootstrap` 更完整。

## 输入
$ARGUMENTS

> 可选：第一个参数可作为 project name（默认 project）。

## 执行
- !`bash planning-with-files/scripts/init-session.sh $ARGUMENTS`

## 备注
- 已存在文件会跳过，不会覆盖。
- 如果你只想要最小模板：用 `/vibe/pwf-bootstrap`。
