---
description: 项目专属帮助（你应该先读什么、常用命令是什么）
agent: plan
---

## 单一真相源
- 规则：请先阅读 `AGENTS.md`
- Claude Code 入口：`CLAUDE.md`
- OpenCode 项目配置：`opencode.jsonc`
- 范式规划：`plans/ai-dev-paradigm-plan.zh.md`

## 常用命令（门禁）
- `/vibe/apply <目标>`：执行真实写入（强制审计 + 验证）
- `/vibe/deploy <目标>`：部署/上线（构建 + 回滚）
- `/vibe/release <目标>`：发版（清单 + 验证）
- `/vibe/db-migrate <目标>`：数据库迁移（必须先确认）

## 常用命令（日常）
- `/vibe/plan <需求>`：生成可执行最小计划
- `/vibe/review`：审查当前改动（基于 git diff）
- `/vibe/test`：跑测试并基于输出给修复路径
- `/vibe/lint`：跑 lint（前端优先）
- `/vibe/build`：构建产物（前端 dist）
- `/vibe/preview`：本地预览构建产物
- `/vibe/ship <目标>`：一键闭环（plan→apply→test→build→deploy 的门禁编排）

## 内置模块（已 vendored，无需额外安装）
- UI/UX：`ui-ux-pro-max-skill`（本地数据库检索）
  - `/vibe/uiux-search <query+flags>`：检索 UI/UX 方案（例：`"pricing page" --domain product --stack react`）
  - `/vibe/uiux-selftest`：验证检索脚本可运行（不写入）
- 长链路计划：`planning-with-files`（3-file pattern + hooks）
  - `/vibe/pwf-bootstrap`：创建 `task_plan.md/findings.md/progress.md` 三文件（最小模板）
  - `/vibe/pwf-init [project-name]`：用 planning-with-files 官方模板初始化（更完整）

## oh-my-opencode 编排（可选但推荐）
- 项目编排配置：`.opencode/oh-my-opencode.json`
- 编排运行目录：`.sisyphus/`（plans/drafts）
- 安装/诊断（需要 Bun）：
  - `bunx oh-my-opencode install`
  - `bunx oh-my-opencode doctor`
- 两种用法：
  - 省事但复杂：输入 `ulw`
  - 精确可验证：`@plan` → `/start-work`
    - planner 计划文件默认落在：`.sisyphus/plans/`

### 选择指南（ulw vs @plan）
```
这是一个 quick fix / 单文件小改？
  └─ YES → 直接正常提问（或用 /vibe/plan）
  └─ NO  → 解释上下文很麻烦？
             └─ YES → 用 ulw 让编排器自己并行摸清情况
             └─ NO  → 需要严格验收、可验证执行吗？
                        └─ YES → 用 @plan → /start-work
                        └─ NO  → 用 ulw
```

### 门禁规则（无条件）
- 任何真实写入/部署/发版/迁移都必须走门禁：
  - `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`

> 提示：你可以输入 `/` 打开命令面板。
