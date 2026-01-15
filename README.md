# vibe_workflow（AI 开发操作系统 / 母仓库）

本仓库的目标：把 AI 的工作方式固化成一套**可审计、可回滚、可验证**的工程流水线，覆盖全流程：

规划 → 编写代码 → 验证 → 修复 → 上线

你把它当成“母仓库/工作站”即可：日常开发时由它提供规则、命令、技能与编排器；真正业务代码在其它仓库。

---

## 你要先记住的 3 层（最重要）

1) **编排层（推荐默认）**：oh-my-opencode
- 入口：`ulw` 或 `@plan → /start-work`
- 用途：并行摸清上下文、拆解任务、产出可执行计划、组织执行

2) **门禁层（强制）**：`/vibe/*` 高风险门禁
- 任何“真实写入/部署/发版/迁移”都必须显式触发门禁：
  - `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`

3) **验证层（统一入口）**：Makefile / scripts
- 推荐用 `make test/lint/build/preview/deploy` 做验证与交付，不要随口胡跑命令。

---

## 先读什么（单一真相源）

- 最高优先级规则：`AGENTS.md`
- Claude Code 入口：`CLAUDE.md`
- OpenCode 项目配置：`opencode.jsonc`
- 范式规划（中英双语）：
  - `plans/ai-dev-paradigm-plan.zh.md`
  - `plans/ai-dev-paradigm-plan.en.md`

---

## 三条硬约束（不讨论，直接执行）

1. 不许误改/不许越界：所有改动必须可追溯（至少能输出 `git diff`/变更摘要/影响范围）。
2. 不许跳过测试/验证：测试失败必须停机或回滚；禁止“删测试/关校验”过关。
3. 不许瞎猜：关键假设必须先确认；缺信息先问。

---

## 我应该用什么命令？（决策树 / 你照着选就行）

如果你读到这里还是不确定：先输入 `/vibe/help`，按里面的 3 个问题做选择。

### 0) 你是在做“简单需求”还是“复杂需求”？

- **简单需求**：你能一句话说明“改哪里 + 验收是什么”，通常单文件或小范围。
- **复杂需求**：你不知道入口在哪/涉及多模块/需要先摸清现状/上线风险高。

### 1) 推荐默认路径（推荐 1）：先 `ulw`，再 `@plan → /start-work`

适用场景：
- 上下文很烦、不想解释工程结构
- 或者任务本身复杂（跨模块、多步骤、要上线）

步骤（标准闭环）：
1. 输入 `ulw`，把需求用自然语言说清楚（允许模糊）。
2. 让编排器并行探索并产出方案后，再走严格落地：`@plan → /start-work`。
3. 需要落盘的长链路任务：先 `/vibe/pwf-init`（或 `/vibe/pwf-bootstrap`）。
4. 真正写代码：必须用 `/vibe/apply <目标>` 进入写入门禁。
5. 验证：用 `make test/lint/build`（或对应 `/vibe/test` `/vibe/lint` `/vibe/build`）。
6. 修复：仍然 `/vibe/apply` → 再跑同一套验证。
7. 上线/发版/迁移：分别用 `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`。

### 2) 备选路径（推荐 2）：直接 `@plan → /start-work`，不清楚才 `ulw`

适用场景：
- 需求明确、范围小、你能讲清上下文
- 你更想“快而可控”，不想让编排器先扫全仓

步骤（最短闭环）：
1. `@plan → /start-work`：让 planner 产出可执行计划（含验收/风险/回滚）。
2. 需要改文件：`/vibe/apply <目标>`。
3. 验证：`make test/lint/build`。
4. 失败则修复：`/vibe/apply` → 重跑验证。

---

## 全流程模板：从规划到上线（你可以直接照抄执行）

### Phase 1：规划（Plan）
- 复杂任务：`ulw`（摸清现状）→ `@plan → /start-work`（严格落地）
- 简单任务：直接 `@plan → /start-work`

输出必须包含：
- 目标/非目标
- 改动范围（文件/模块级）
- 验收标准（可执行）
- 风险与回滚

### Phase 2：写入（Apply Gate）
- `/vibe/apply <目标>`

写入门禁里必须做：
- 明确要改哪些文件
- 产出 `git diff`（或等价变更摘要）
- 不通过任何“删测试/关校验”方式过关

### Phase 3：验证（Validate）
推荐用 Makefile：
- `make test`：后端（存在 `pyproject.toml` 才会运行）
- `make lint`：前端（存在 `package.json` 才会运行）
- `make build`：前端构建
- `make preview`：本地预览

也可以用 /vibe：
- `/vibe/test` `/vibe/lint` `/vibe/build` `/vibe/preview`

### Phase 4：修复（Fix Loop）
- `/vibe/apply "修复 <失败点>"`
- 重跑 Phase 3 的同一套命令

### Phase 5：上线/发版/迁移（Deploy/Release/Migrate）
- 上线：`/vibe/deploy <env>`（或 `make deploy`，看你要不要走门禁式上线）
- 发版：`/vibe/release <version>`
- 迁移：`/vibe/db-migrate <target>`

---

## 长任务必备：planning-with-files（3-file 磁盘工作记忆）

当任务满足任意一条，就建议开启：
- 3 步以上
- 需要调研
- 要跨很多轮工具调用
- 要上线（必须可复盘）

二选一：
- `/vibe/pwf-init [project-name]`：使用官方完整模板
- `/vibe/pwf-bootstrap`：最小模板

三文件职责：
- `task_plan.md`：目标/拆解/风险/验收（每完成阶段就更新状态）
- `findings.md`：调研与关键发现
- `progress.md`：执行记录、测试/构建/部署输出

Claude Code hooks 已在 `.claude/settings.json` 配好：写入/执行前会提醒重读 plan，Stop 时会检查完成性。

---

## UI/UX 模块（vendored）：ui-ux-pro-max-skill

用途：本地检索 UI/UX 方案，辅助你把“设计意图”变成可执行前端改动。

- 检索：`/vibe/uiux-search "<query>" --domain <domain> --stack <stack> --max-results <n>`
  - domain 可选：style/prompt/color/chart/landing/product/ux/typography
  - stack 可选：html-tailwind/react/nextjs
- 自检（建议你测试前先跑一次）：`/vibe/uiux-selftest`

典型闭环：
1. `/vibe/uiux-search "pricing page" --domain product --stack react`
2. `@plan → /start-work`（把检索结果转成验收与改动清单）
3. `/vibe/apply "落地 UI 变更"`
4. `make lint && make build`

---

## 验证与交付入口（Makefile / scripts）

- `make lint` / `make test` / `make build` / `make preview`
- `make deploy`：执行 `scripts/deploy.sh`

`scripts/deploy.sh` 默认是“安全模式”：不会瞎猜你的部署目标。
如果你要本地静态发布（带备份可回滚）：
- `./scripts/deploy.sh --env prod --static-dest /var/www/my-app`

---

## oh-my-opencode（推荐启用）

- 编排配置：`.opencode/oh-my-opencode.json`
- 运行目录：`.sisyphus/`（plans/drafts）

如果你需要安装/诊断（需要 Bun）：
- `bunx oh-my-opencode install`
- `bunx oh-my-opencode doctor`

---

## MCP（可选，默认全关）

- OpenCode MCP 示例：`mcp/opencode.mcp.example.jsonc`
- Codex MCP 示例：`mcp/codex.config.toml.example`

`opencode.jsonc` 里 MCP 默认 `enabled: false`，避免你本机没装命令导致启动失败。

---

## 目录结构速览

- `AGENTS.md`：单一真相源（行为契约）
- `CLAUDE.md`：Claude Code 入口（只做索引，避免漂移）
- `.opencode/command/vibe/`：OpenCode 命令（全部 `/vibe/*` 命名空间）
- `.opencode/skill/`：OpenCode skills（按需加载 references）
- `.opencode/oh-my-opencode.json`：编排配置（约束注入 + 默认启用规划/执行）
- `.claude/settings.json`：Claude Code hooks（3-file pattern 辅助）
- `.sisyphus/`：编排运行目录（plans/drafts）
- `plans/`：方法论/范式/策略资产
- `mcp/`：MCP 配置片段
- `scripts/`：构建/部署入口脚本

---

## 你接下来怎么测（最小可验证用例）

1) 简单需求：
- 直接 `@plan → /start-work` → `/vibe/apply` → `make test/lint/build`

2) 复杂需求（你不想解释上下文）：
- `ulw` →（收敛后）`@plan → /start-work` → `/vibe/apply` → 验证

3) UI/UX：
- `/vibe/uiux-selftest`（确认脚本可运行）
- `/vibe/uiux-search ...` → `@plan` → `/vibe/apply` → `make lint/build`
