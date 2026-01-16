---
description: 使用引导（不知道该用什么命令时先来这里）
agent: plan
---

你现在在做的是：把 AI 的工作固化为“可审计、可回滚、可验证”的闭环。

## 推荐默认路径
- 复杂需求：先 `ulw`，再 `@plan → /start-work`
- 简单需求：直接 `@plan → /start-work`

## 最短闭环
- 计划：`/vibe/plan <需求>`
- 写入：`/vibe/apply <目标>`（门禁）
- 验证：`/vibe/test` `/vibe/lint` `/vibe/build`
- 审查：`/vibe/review`

## 注意（项目级边界）
- 默认只修改项目内文件，不修改系统级配置（例如 `~/.config/opencode/*`）。
