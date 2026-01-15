# AI 开发范式（个人版→团队版）规划

> 目的：打造一套“给 AI 用”的开发操作系统（AGENTS/Skills/Commands/MCP/Rules），让 AI 在任何项目里稳定完成：规划 → 开发 → 测试 → 修复 → 上线。
> 
> 本文是 **Handbook + Templates** 的混合体：既定义原则与流程，也提供可复制的模板片段。

---

## 0. 适用范围与验收

### 0.1 适用范围
- 主运行时：OpenCode（opencode）
- 主编排器：oh-my-opencode（Category + Skill 的组合式路由）
- 项目类型：
  - 纯后端（Python3 + uv）
  - 前后端（前端 React/Vue，优先 Ant Design Pro 体系）
  - 内嵌 AI（langgraph/langchain）

### 0.2 验收动作（Definition of Done）
读者（你自己/团队）在新仓库中能做到：
1) 15 分钟内落地规则与入口：能启动“规划→实现→测试→修复→交付”的闭环。
2) 能按项目选择两条范式（严谨 vs 灵活）并清楚触发条件。
3) 能按需启用 MCP，并能控制上下文成本。

---

## 1. 核心原则（不可妥协）

### 1.1 三条硬约束（必须写进 AGENTS 与 Commands）
- 不许误改/不许越界：所有改动必须可追溯（`git diff`/`git log`/变更摘要）。
- 不许跳过测试/验证：测试失败必须停机或回滚，不得“假装完成”。
- 不许瞎猜：关键假设必须向你确认；缺信息就问。

### 1.2 “权限全开”的风险缓解（不靠权限限制，而靠流程）
- 关键动作必须 **显式 command 触发**（门禁）：`/vibe/apply`、`/vibe/deploy`、`/vibe/release`、`/vibe/db-migrate`。
- 任何写入前必须生成“变更计划 + 风险点 + 验收命令”。
- 任何失败必须进入“止血回路”（停机/回滚/定位/复测），禁止乱改。

---

## 2. Agent 体系设计（多 Agent + 自动路由 + 关键门禁）

### 2.4 编排落地（oh-my-opencode）
- 项目级编排配置：`.opencode/oh-my-opencode.json`
  - 开启 `sisyphus_agent`：Prometheus 负责 plan（落盘到 `.sisyphus/plans/`），Sisyphus 负责 execute
  - 用 `agents.Sisyphus.prompt_append` 注入本仓库门禁与硬约束（不强制改模型）

> 注意：你当前的稳定执行面仍以 `/vibe/*` 命令门禁为主；编排器负责自动路由与并行上下文收集，但不会绕过门禁。

> 目标：把“会乱跑的智能”拆成职责单一、可审计的角色；把不确定性收敛到可控流程里。

### 2.1 角色划分（建议最小集）
- `planner`：只做澄清、拆解、验收定义、风险识别；不直接修改代码。
- `executor`：按计划实现；只做最小必要变更；失败就止血。
- `reviewer`：做变更审查（diff、边界、风格、回归风险）。
- `test-engineer`：只负责验证与失败诊断；产出复现步骤与最小用例。
- `release-engineer`：只负责构建/打包/发布/部署的脚本化入口与回滚策略。
- `frontend-ui-ux-engineer`（可选）：专门处理视觉与交互细节（尤其前端）。
- `ai-engineer`（可选）：专门处理 langgraph/langchain 的 prompt/graph/评估。

### 2.2 自动路由规则（高层）
- 默认：根据任务类型自动选择 agent（通过 Category + Skill 组合）。
- 强制门禁：只要涉及“不可逆/高风险动作”，必须通过 command 显式触发。

### 2.3 权限策略（全开，但分层使用）
- `planner`：建议只读 + 允许有限 bash（信息收集/诊断）。
- `executor/test/release`：全开（含 bash/network），但必须遵守命令门禁与验收规则。

---

## 3. 双范式：严谨型 vs 灵活型

### 3.1 严谨型（Spec/Plan 驱动）
适用：中大型项目、多人协作、需求不清、风险高。
- 核心资产：计划文件（任务拆解、验收、风险、回滚）、变更记录（change log）。
- 执行路径：先定计划（planner）→ 再实现（executor）→ 再验证（test-engineer）→ 再交付（release-engineer）。

### 3.2 灵活型（Commands/Skills 驱动）
适用：短任务、快速迭代、个人开发。
- 核心资产：高质量 commands（固化常见流程）、skills（工具与知识包）。
- 执行路径：用命令进入固定流程，减少自由发挥。

---

## 4. 场景矩阵（选择范式与默认命令）

| 场景 | 推荐范式 | 默认入口 | 关键门禁 |
|------|----------|----------|----------|
| 纯后端（uv） | 严谨/灵活均可 | `/vibe/plan`→`/vibe/apply`→`/vibe/test` | `/vibe/apply` `/vibe/release` |
| 前后端（Ant Design Pro） | 严谨优先 | `/vibe/plan`→`/vibe/apply`→`/vibe/test`→`/vibe/build` | `/vibe/deploy` |
| 内嵌 AI（langgraph/langchain） | 严谨优先 | `/vibe/plan`→`/vibe/apply`→`/eval` | `/vibe/release` |

---

## 5. Commands 设计（你的“显式门禁”与可重复流水线）

### 5.1 命令分层
- **入口命令（决定流程）**：`/vibe/plan`、`/vibe/ship`
- **门禁命令（不可逆/高风险）**：`/vibe/apply`、`/vibe/deploy`、`/vibe/release`、`/vibe/db-migrate`
- **验证命令（必须可重复）**：`/vibe/test`、`/vibe/lint`、`/vibe/build`、`/vibe/preview`
- **审查命令（可追溯/风险）**：`/vibe/review`
- **帮助命令（项目入口）**：`/vibe/help`

### 5.2 命令契约（每个命令都必须输出）
- 输入：目标 + 约束 + 影响范围
- 输出：执行步骤（可复制）+ 预期结果 + 失败分流（失败后怎么做）
- 自动注入上下文：
  - `git status`、`git diff`、`git log -n 20`（变更可追溯）
  - 最近测试/构建输出（验证必须可审计）

---

## 6. Skills 设计（工具/知识包）

### 6.1 Skill 的职责边界
- Skill 不直接代表“任务”，而代表：
  - 工具开关（是否允许网络、是否用 LSP、是否用 AST-grep）
  - 知识包（项目约定、测试策略、部署策略、前端规范）

### 6.2 推荐 Skill 套件（初版）
- `git-master`：提交策略、变更审查、回滚策略
- `python-uv-backend`：uv/pytest 约定、常见项目结构
- `frontend-ant-design-pro`：Umi Max/构建/部署要点（见 8.2）
- `release-playbook`：构建产物、版本号、部署脚本入口
- `ui-ux-pro-max`：UI/UX 方案检索与落地（底层：`ui-ux-pro-max-skill`）
- `planning-with-files`：长链路任务“磁盘工作记忆”（3-file pattern + hooks）
- `ai-langgraph-langchain`：graph/prompt/评估用例

---

## 7. MCP 策略（按需启用 + 成本控制）

### 7.1 你当前同意启用的 MCP（不含 websearch/grep_app）
- `augment-context-engine`（`auggie --mcp`）
- `mcp-deepwiki`（`npx -y mcp-deepwiki@latest`）
- `playwright`（`npx -y @playwright/mcp@latest`）
- `context7`（OpenCode 推荐 remote：`https://mcp.context7.com/mcp`；Codex 可用 streamable_http 指向同 URL）
- `sequential-thinking`（`npx -y @modelcontextprotocol/server-sequential-thinking`）

### 7.2 启用顺序（你已确认）
1) 基础 → 2) 扩展 → 3) 自动化

### 7.3 OpenCode `mcp` 段落模板（JSON 示例）
> 说明：以下是结构示例，最终以你的真实命令参数为准。
> 可复制示例文件：`mcp/opencode.mcp.example.jsonc`

```json
{
  "mcp": {
    "augment-context-engine": {
      "type": "local",
      "command": ["auggie", "--mcp"],
      "enabled": true
    },
    "mcp-deepwiki": {
      "type": "local",
      "command": ["npx", "-y", "mcp-deepwiki@latest"],
      "enabled": false
    },
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@playwright/mcp@latest"],
      "enabled": false
    },
    "sequential-thinking": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-sequential-thinking"],
      "enabled": true
    }
  }
}
```

### 7.4 Codex（TOML）配置对照（示例骨架）
可复制示例文件：`mcp/codex.config.toml.example`
```toml
[mcp_servers.mcp-deepwiki]
type = "stdio"
command = "npx"
args = ["-y", "mcp-deepwiki@latest"]
startup_timeout_sec = 30

[mcp_servers.playwright]
type = "stdio"
command = "npx"
args = ["-y", "@playwright/mcp@latest"]
startup_timeout_sec = 30

[mcp_servers.sequential-thinking]
type = "stdio"
command = "npx"
args = ["-y", "@modelcontextprotocol/server-sequential-thinking"]
```

---

## 8. 全流程 Playbook（规划→开发→测试→修复→上线）

### 8.0 两条入口（如何用起来）
- **复杂但不想解释上下文**：直接输入 `ulw`（oh-my-opencode 会自动并行调研并推进）。
- **复杂且需要高精度可验证**：用 `@plan` → `/start-work`。
  - Prometheus 输出计划到 `.sisyphus/plans/`
  - Sisyphus 执行计划并委派子 agent

### 8.0.1 编排与门禁如何结合（关键）
- 编排负责：自动路由、并行探索、组织执行顺序。
- 门禁负责：把高风险动作收敛为显式触发。
  - 任何真实写入/上线/发版/迁移，都必须走：`/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`
- 推荐策略：
  - `@plan` 产出计划 → 执行过程中需要写入时由 Sisyphus 提示触发 `/vibe/apply`
  - 验证收口用：`/vibe/test` `/vibe/lint` `/vibe/build` `/vibe/preview`
  - 变更审查用：`/vibe/review`

### 8.1 Python 后端（uv）默认约定
- 安装/运行：`uv run ...`
- 测试入口标准化：`uv run python -m pytest`

### 8.2 前端（Ant Design Pro / Umi Max）默认约定（yarn）
> 来源：Ant Design Pro 官方仓库脚本与 CI 约定。
- 开发：`yarn start:dev`（建议默认关闭 mock）
- 质量门禁：`yarn lint`（Biome + tsc noEmit）
- 构建：`yarn build` → 产物目录 `dist/`
- 预览：`yarn preview`（build 后 preview）
- 部署前检查：`publicPath`、静态资源路径、代理仅开发环境有效

### 8.3 Makefile 作为统一入口（规范）
> 这里定义“target 命名规范”，实现细节由 `scripts/*.sh` 承载。
- `make lint`：跑全量 lint（前后端各自 lint）
- `make test`：后端 `uv run python -m pytest`；前端（若有）跑对应 test
- `make build`：前端 `yarn build`；后端构建（若有）
- `make deploy`：只调用 `scripts/deploy.sh`，并要求输出回滚步骤

---

## 9. 产物清单（下一步要落地的文件/目录）

> 本节定义“应该生成什么”，实现由后续落地阶段完成。

- `AGENTS.md`：仓库级总规则（硬约束 + 门禁 + 默认命令）
- `CLAUDE.md`：项目架构/目录地图（帮助 AI 快速定位）
- `.opencode/command/`：关键门禁命令（`/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`）与常用流程命令
- `.opencode/skill/`：按领域拆分的知识包与工具开关（`SKILL.md`）
- `mcp/`：OpenCode JSON 片段与 Codex TOML 片段
- `Makefile` + `scripts/`：构建/测试/部署的统一入口

---

## 10. 迭代与推广策略（个人→团队）
- 个人阶段：优先把 commands 与门禁跑顺，收集“失败案例与分流”。
- 团队阶段：把“默认命令集 + 目录结构 + 质量门禁”固化成模板仓库。
- 治理：版本化规则文件；每次升级要能回滚。
