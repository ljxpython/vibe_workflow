---
description: 一键闭环交付（默认自动路由 + 门禁显式触发）
agent: plan
---

目标：把一次需求从“清晰”推进到“可交付”。

## 输入
$ARGUMENTS

## 重要原则
- 本命令本身只负责：生成闭环计划与执行清单。
- 涉及真实写入/部署/发版/迁移时，必须提示用户改用门禁命令显式触发：
  - `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`

## 选择指南（ulw vs @plan）
- quick fix / 单文件小改：直接用 `/vibe/plan`（或正常提问）
- 多步骤/长链路任务：先 `/vibe/pwf-init`（完整模板）或 `/vibe/pwf-bootstrap`（最小模板）
- 复杂但不想解释上下文：直接输入 `ulw`
- 复杂且需要严格验收：用 `@plan` → `/start-work`（计划落盘 `.sisyphus/plans/`）

## 闭环流程（输出为可复制清单）
1) **Plan**：用 `/vibe/plan` 生成最小可执行计划（含验收、风险、回滚）。
2) **Apply Gate**：若需要改代码，提示用户用 `/vibe/apply <目标>` 进入写入门禁。
3) **Validate**：
   - 后端：`uv run python -m pytest`
   - 前端：`yarn lint`、`yarn build`、必要时 `yarn preview`
4) **Review**：提示运行 `/vibe/review` 做变更审查。
5) **Deploy/Release**：
   - 若要上线：提示用 `/vibe/deploy <目标环境>`
   - 若要发版：提示用 `/vibe/release <版本/目标>`

## 输出要求
- 产出一份“命令级 checklist”（按顺序）。
- 产出失败分流：每一步失败时如何止血。
- 如果缺少关键信息，先列出问题让用户确认（不允许瞎猜）。
