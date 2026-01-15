# vibe_workflow

这是一个“AI 开发操作系统”工作站：用一套可复用的**规则（AGENTS）+ 命令（/vibe/*）+ 技能（skills）+ 编排器（oh-my-opencode）**，把 AI 的工作固化成可审计、可回滚、可验证的流水线。

本仓库的定位不是业务项目本身，而是你每天用来“带 AI 干活”的工具箱与模板源。

## 先读什么（单一真相源）

- 最高优先级规则：`AGENTS.md`
- Claude Code 入口：`CLAUDE.md`
- OpenCode 项目配置：`opencode.jsonc`
- 范式规划（中英双语）：
  - `plans/ai-dev-paradigm-plan.zh.md`
  - `plans/ai-dev-paradigm-plan.en.md`

## 三条硬约束（不讨论，直接执行）

1. 不许误改/不许越界：所有改动必须可追溯（至少能输出 `git diff`/变更摘要/影响范围）。
2. 不许跳过测试/验证：测试失败必须停机或回滚；禁止“删测试/关校验”过关。
3. 不许瞎猜：关键假设必须向你确认；缺信息先问。

> 这些规则在 `AGENTS.md` 里是“行为契约”，不是建议。

## 快速开始（推荐路径）

### 0) 你在用什么工具？

- **OpenCode**：使用 `.opencode/command/vibe/*.md` 提供的 `/vibe/*` 命令体系。
- **Claude Code**：使用 `.claude/settings.json` 的 hooks（会在 SessionStart 提示、PreToolUse 重读 plan、Stop 检查完成性）。
- **oh-my-opencode**：多 Agent 编排器（Prometheus 规划 + Sisyphus 执行），配置见 `.opencode/oh-my-opencode.json`，运行目录是 `.sisyphus/`。

### 1) 日常工作：先把需求变成“可验证计划”

- `/vibe/plan <需求>`
- 然后把关键结论落盘：
  - 简单任务：直接继续对话即可
  - 多步骤/长链路任务：先执行下面的 3-file 初始化（见下一节）

### 2) 多步骤/长链路任务：启用 3-file 磁盘工作记忆（强烈建议）

二选一：

- 最小模板：`/vibe/pwf-bootstrap`
- 官方完整模板：`/vibe/pwf-init [project-name]`

生成/维护这三个文件：

- `task_plan.md`：目标/拆解/风险/验收（每完成一个阶段就更新状态）
- `findings.md`：调研与关键发现（不要塞在聊天里）
- `progress.md`：执行记录、测试/构建/部署输出

> Claude Code hooks 已在 `.claude/settings.json` 配好：写入/执行前会提醒你看 plan；Stop 时会检查完成性。

### 3) 真正写代码/改文件：必须走门禁命令

- `/vibe/apply <目标>`：进入“真实写入”门禁（带审计 + 验证）

涉及上线/发版/迁移时同理：

- `/vibe/deploy <目标环境>`
- `/vibe/release <版本/目标>`
- `/vibe/db-migrate <目标>`

## 选择指南：ulw vs @plan（oh-my-opencode）

当你觉得“我解释上下文太烦了”，用编排器。

- **ulw**：省事但复杂，适合让编排器自己并行摸清情况
- **@plan → /start-work**：精确可验证，适合必须严格验收的任务（计划落盘 `.sisyphus/plans/`）

你也可以随时用 `/vibe/ship <目标>` 让 AI 输出一份“闭环 checklist”（但它不会自动越权写入，写入仍要你显式触发门禁）。

## 内置模块：UI/UX（vendored）

本仓库 vendored 了 `ui-ux-pro-max-skill`，用于本地检索 UI/UX 方案。

- 检索：`/vibe/uiux-search "<query>" --domain <domain> --stack <stack> --max-results <n>`
  - domain 可选：style/prompt/color/chart/landing/product/ux/typography
  - stack 可选：html-tailwind/react/nextjs
- 自检（推荐先跑一次）：`/vibe/uiux-selftest`

典型用法：

1. `/vibe/uiux-search "pricing page" --domain product --stack react`
2. `/vibe/plan "把检索结果落地到当前页面"`
3. `/vibe/apply "实现 UI 变更"`

> 注意：涉及前端视觉样式/布局的改动，优先委派给 UI/UX 专家代理（如果你启用了 oh-my-opencode 的多 Agent）。

## 验证与交付（Makefile 作为统一入口）

本仓库提供了统一的验证入口（如果目标项目存在对应文件才会执行）：

- `make lint`：存在 `package.json` 时执行 `yarn lint`
- `make test`：存在 `pyproject.toml` 时执行 `uv run python -m pytest`
- `make build`：存在 `package.json` 时执行 `yarn build`
- `make preview`：存在 `package.json` 时执行 `yarn preview`
- `make deploy`：执行 `scripts/deploy.sh`（默认安全：不瞎猜部署目标）

`scripts/deploy.sh` 支持一个“可审计、可回滚”的本地静态发布模式：

- `./scripts/deploy.sh --env prod --static-dest /var/www/my-app`

## MCP（可选，默认全关）

- OpenCode MCP 示例：`mcp/opencode.mcp.example.jsonc`
- Codex MCP 示例：`mcp/codex.config.toml.example`

本项目的 `opencode.jsonc` 里 MCP 默认全部 `enabled: false`，避免你本机没装命令导致启动失败。

## 目录结构速览

- `AGENTS.md`：单一真相源（行为契约）
- `CLAUDE.md`：Claude Code 入口（只做索引，避免漂移）
- `.opencode/command/vibe/`：OpenCode 命令（全部以 `/vibe/*` 命名空间提供）
- `.opencode/skill/`：OpenCode skills（按需加载 references）
- `.opencode/oh-my-opencode.json`：oh-my-opencode 编排配置（约束注入 + 默认启用规划/执行）
- `.claude/settings.json`：Claude Code hooks（3-file pattern 辅助）
- `.sisyphus/`：编排运行目录（plans/drafts）
- `plans/`：方法论/范式/策略资产（中英双语）
- `mcp/`：MCP 配置片段
- `scripts/`：可脚本化的构建/部署入口
- `oh-my-opencode/`：编排器实现
- `learn-opencode/`：OpenCode 使用教程
- `vibe-coding-cn/`：Vibe Coding 资产库

## 常见问题（你会踩的坑）

1) “我想让 AI 直接改代码”
- 先用 `/vibe/plan` 把验收与风险说清楚
- 再用 `/vibe/apply` 显式触发写入门禁

2) “ulw 不工作/编排器没起来”
- 检查 `.opencode/oh-my-opencode.json`
- 需要 Bun 时按 `.opencode/command/vibe/help.md` 的提示运行 `bunx oh-my-opencode install` / `bunx oh-my-opencode doctor`

3) “UI/UX 搜索脚本报错”
- 先跑 `/vibe/uiux-selftest`
- 确认 `python3` 可用，并确认脚本路径存在：`ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py`

---

如果你要把这套体系迁移到其他业务仓库，建议把本仓库当作“母仓库”，再做一个只复制 `.opencode/`、`.claude/`、`AGENTS.md/CLAUDE.md`、`Makefile/scripts/` 的最小部署流程（可审计、可回滚）。
