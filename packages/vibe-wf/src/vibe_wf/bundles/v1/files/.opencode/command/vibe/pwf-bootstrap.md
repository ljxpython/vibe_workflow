---
description: 初始化 3-file 工作记忆（task_plan/findings/progress）
agent: build
---

目标：为复杂任务初始化磁盘工作记忆文件（最小模板）。

## 执行
- !`test -f task_plan.md || printf '%s\n' '# task_plan\n\n- 目标：\n- 非目标：\n- 任务拆解：\n- 风险与缓解：\n- 验收：\n' > task_plan.md`
- !`test -f findings.md || printf '%s\n' '# findings\n\n' > findings.md`
- !`test -f progress.md || printf '%s\n' '# progress\n\n' > progress.md`

## 推荐工作流
- `/vibe/plan` 的摘要同步进 `task_plan.md`
- 重要发现写 `findings.md`
- 测试/构建输出写 `progress.md`
