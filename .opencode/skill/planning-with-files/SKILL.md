---
name: planning-with-files
description: |
  复用 planning-with-files 的“磁盘工作记忆”能力：task_plan.md/findings.md/progress.md 三文件模式 + hooks。适用：复杂多步骤任务、长链路调研、跨多次工具调用的实现与排障。
  不适用：单文件小改、快速问答。
---

# Planning with Files

## 能力概览
- 3-file pattern：`task_plan.md` / `findings.md` / `progress.md`
- Claude Code 插件 hooks：PreToolUse/Stop 等，自动重读 plan、提醒更新、检查完成

## 复用策略（按你未来的部署方式）
- 你未来会按它自己的插件方式部署：优先使用 `/planning-with-files` 来触发其 hooks 与模板。
- 本仓库的作用：让 AI 在任何复杂任务中主动采用 3-file pattern，并把关键决策/失败记录落盘。

## 参考资料（按需加载）
- 能力地图与用法：读取 `references/capabilities.md`
- 集成坑点：读取 `references/gotchas.md`

## 与 /vibe 命令体系的协作
- `/vibe/plan` 的输出应同步落盘到 `task_plan.md`
- 重要发现写入 `findings.md`
- 测试/构建/部署结果写入 `progress.md`
- 失败必须记录，且下一次尝试必须改变策略（Never Repeat Failures）
