# Vibe 部署工具（vibe-kit）技术规格（Spec）

> 目标：把本仓库的“AI 开发操作系统”资产（`AGENTS.md`、`CLAUDE.md`、`.opencode/command/vibe/*`、`.opencode/skill/*`、MCP 片段等）按需、安全、可审计地部署到任意目标项目，并能选择性调用外部项目（`ui-ux-pro-max-skill`、`planning-with-files`）的官方安装方式。

---

## 0. 背景与动机

你当前的体系由两层组成：
1) **本仓库自有资产（vibe）**：规则、命令、技能、范式文档。
2) **外部可复用资产**：
   - `ui-ux-pro-max-skill`：UI/UX 设计智能与本地检索
   - `planning-with-files`：磁盘工作记忆与 hooks（Claude Code 插件/skill）

目标是把“资产部署”从手工复制变成可重复、可回滚、可配置的工具。

---

## 1. 目标（Goals）

1) 一键初始化：在目标项目中生成/更新 Vibe 资产。
2) 可选组件安装：
   - 仅部署 `/vibe/*` commands
   - 仅部署 skills
   - 同步/更新 `AGENTS.md`/`CLAUDE.md`
3) 安全与可追溯：
   - 所有写入有备份与变更摘要
   - 支持 dry-run
   - 支持回滚（撤回到安装前状态）
4) 外部项目对接（只编排，不重实现）：
   - `ui-ux-pro-max-skill`：建议通过其官方 `uipro` CLI 部署
   - `planning-with-files`：建议通过 Claude Code `/plugin ...` 官方方式安装

---

## 2. 非目标（Non-goals）

- 不替代外部项目官方安装机制（不复制它们的多平台目录，不做 fork 同步）。
- 不直接执行生产部署（生产相关仍由 `/vibe/deploy` 门禁控制，部署工具只负责“资产安装/同步”）。
- 不引入复杂 GUI；优先 CLI + 配置文件。

---

## 3. 目标用户与使用场景

### 3.1 用户
- 第一用户：你自己（个人快速开新项目）
- 第二用户：团队（统一规范、降低沟通成本）

### 3.2 场景
- 新项目初始化：把 Vibe 规则与命令带进来
- 旧项目升级：从 Vibe vX 同步到 vY
- 选择性启用：例如仅启用 `/vibe/*` 命令体系

---

## 4. 资产边界与目录映射

### 4.1 Vibe 资产（本仓库）
必须可选部署：
- `AGENTS.md`
- `CLAUDE.md`
- `.opencode/command/vibe/*.md`
- `.opencode/skill/*/SKILL.md`
- `.opencode/skill/*/references/*.md`
- `plans/ai-dev-paradigm-plan.zh.md`
- `plans/ai-dev-paradigm-plan.en.md`

可选：
- MCP 配置片段（以“生成片段/提示用户粘贴”为主，避免覆盖用户现有配置）

### 4.2 外部项目（只对接提示/编排）
- `ui-ux-pro-max-skill`：
  - 推荐：`npm install -g uipro-cli` + `uipro init --ai <type>`
  - 注意：不同助手依赖路径不同（`.claude` vs `.shared` vs `.trae`），由其 CLI 保证一致性
- `planning-with-files`：
  - 推荐：Claude Code 插件安装
    - `/plugin marketplace add OthmanAdi/planning-with-files`
    - `/plugin install planning-with-files@planning-with-files`

---

## 5. CLI 设计（建议）

> 工具名暂定 `vibe-kit`（避免与 `/vibe/*` slash commands 混淆）。

### 5.1 命令
- `vibe-kit init --target <path> [--profile <name>] [--dry-run]`
  - 初始化并写入 Vibe 资产
- `vibe-kit sync --target <path> [--dry-run]`
  - 把目标项目同步到当前 Vibe 版本
- `vibe-kit uninstall --target <path>`
  - 回滚：恢复安装前备份
- `vibe-kit doctor --target <path>`
  - 诊断：列出缺失文件、版本漂移、潜在冲突

### 5.2 Profiles（配置组）
- `minimal`：只装 `AGENTS.md` + `CLAUDE.md` + `.opencode/command/vibe/*`
- `standard`：minimal + `.opencode/skill/*` + `plans/*`
- `full`：standard + 输出外部项目安装建议（不自动安装，除非显式 opt-in）

---

## 6. 安全策略（必须）

1) **Dry-run**：输出将要写入/覆盖/移动的文件列表。
2) **备份**：对将覆盖的文件创建备份目录，例如：
   - `<target>/.vibe-kit-backup/<timestamp>/...`
3) **冲突处理**：
   - 默认不覆盖用户修改的同名文件（除非 `--force`）
   - 如果覆盖，必须先备份并输出 diff 摘要
4) **幂等性**：重复运行 `init/sync` 不应造成重复目录或不可逆损坏。

---

## 7. 版本策略

- Vibe 资产应有版本号（建议从 git tag 或内置 `VIBE_VERSION` 文件获取）。
- 在目标项目写入一个小的版本标记文件：
  - `.vibe-kit/version.json`（记录来源版本、安装时间、profile、安装的组件集合）

---

## 8. 测试与验证（部署工具自身）

最小验证：
- 在临时目录创建一个空项目，运行 `init`，检查：
  - 文件是否齐全
  - `doctor` 是否能正确报告状态
  - `uninstall` 是否能恢复

---

## 9. 与当前 /vibe 体系的协作

- 部署工具只负责“把资产带进目标项目”。
- 目标项目里由 `/vibe/*` 命令体系接管执行闭环（plan/apply/test/build/deploy）。
- 外部能力通过 `external-*` skills 提示 AI 如何使用，并通过其官方方式部署。

---

## 10. 待确认（在开始实现前必须确认）

1) `vibe-kit` 的实现语言：Python（uv）还是 Node？
2) 目标平台：macOS 优先还是必须跨平台（Windows/Linux）？
3) 是否允许工具自动执行外部安装命令（默认建议只输出指令 + 让你确认）。
