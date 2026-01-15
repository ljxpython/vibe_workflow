---
description: 使用引导（不知道该用什么命令时先来这里）
agent: plan
---

你现在在做的是：把 AI 的工作固化为“可审计、可回滚、可验证”的闭环。

如果你不知道该用哪个命令：先回答下面 3 个问题，然后按推荐路径走。

## 先回答 3 个问题（决定你该走哪条路）
1) **你能一句话说清楚要改哪里 + 验收是什么吗？**（能/不能）
2) **你需要 AI 先帮你摸清上下文/找入口吗？**（需要/不需要）
3) **这次是否涉及高风险动作？**（写代码/上线/发版/迁移）

## 推荐默认路径（推荐 1）：先 `ulw`，再 `@plan → /start-work`
适合：复杂需求、上下文很烦、涉及多模块、或需要上线。

- 第一步（摸清上下文）：输入 `ulw`，用自然语言描述需求（允许模糊）
- 第二步（严格落地）：`@plan → /start-work` 生成可执行计划（含验收/风险/回滚）
- 第三步（若是长任务）：`/vibe/pwf-init`（完整模板）或 `/vibe/pwf-bootstrap`（最小模板）
- 第四步（真写代码）：必须 `/vibe/apply <目标>` 进入写入门禁
- 第五步（验证）：`/vibe/test` `/vibe/lint` `/vibe/build`（或 `make test/lint/build`）
- 第六步（上线/发版/迁移）：分别走 `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`

## 备选路径（推荐 2）：直接 `@plan → /start-work`，不清楚才 `ulw`
适合：简单需求、你能讲清上下文、改动范围小。

- `@plan → /start-work`
- 需要改文件：`/vibe/apply <目标>`
- 验证：`/vibe/test` `/vibe/lint` `/vibe/build`

## 一句话速查（你只想要答案）
- **我只是要一个计划**：`/vibe/plan <需求>`
- **我要真实改代码**：`/vibe/apply <目标>`（门禁）
- **我要跑测试/定位失败**：`/vibe/test`
- **我要跑 lint/build**：`/vibe/lint` / `/vibe/build`
- **我要上线**：`/vibe/deploy <环境/目标>`（门禁）
- **我要发版**：`/vibe/release <版本/目标>`（门禁）
- **我要迁移数据库**：`/vibe/db-migrate <目标>`（门禁）

## 内置模块（用来加速，不是必选）
### 1) 长链路任务：planning-with-files（3-file 磁盘工作记忆）
- `/vibe/pwf-init [project-name]`：官方完整模板
- `/vibe/pwf-bootstrap`：最小模板
- 三文件：`task_plan.md` / `findings.md` / `progress.md`

### 2) UI/UX：ui-ux-pro-max-skill（本地检索）
- 检索：`/vibe/uiux-search "<query>" --domain <domain> --stack <stack> --max-results <n>`
- 自检（建议你测试前先跑一次）：`/vibe/uiux-selftest`

## 门禁规则（无条件）
任何真实写入/部署/发版/迁移都必须走门禁：
- `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`

## 配置入口（迷路时回到这里）
- 规则单一真相源：`AGENTS.md`
- Claude Code 入口：`CLAUDE.md`
- OpenCode 配置：`opencode.jsonc`
- oh-my-opencode 配置：`.opencode/oh-my-opencode.json`
- 编排运行目录：`.sisyphus/`

> 提示：输入 `/` 打开命令面板；输入 `ulw` 进入编排器。
