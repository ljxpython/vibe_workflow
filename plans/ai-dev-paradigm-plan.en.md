# AI Development Paradigm (Personal → Team) Plan

> Goal: build an AI-facing “development OS” (AGENTS / Skills / Commands / MCP / Rules) so the AI can reliably run the full loop in any repo: plan → implement → test → fix → ship.
> 
> This document is a hybrid of **Handbook + Templates**: principles & workflows plus copyable scaffolds.

---

## 0. Scope & Acceptance Criteria

### 0.1 Scope
- Primary runtime: OpenCode (opencode)
- Primary orchestrator: oh-my-opencode (Category + Skill compositional routing)
- Project types:
  - Backend only (Python3 + uv)
  - Full-stack (React/Vue; prefer Ant Design Pro conventions)
  - Embedded AI (langgraph/langchain)

### 0.2 Definition of Done
A new repo can be bootstrapped so that:
1) In ~15 minutes, rules + entrypoints exist for a complete loop.
2) The operator can choose between two paradigms (Strict vs Flexible) with clear triggers.
3) MCP can be enabled on-demand while keeping context cost controlled.

---

## 1. Non-negotiable Principles

### 1.1 Three hard constraints (must be enforced via rules + commands)
- No accidental/overreach edits: all changes must be traceable (`git diff`/`git log`/change summary).
- No skipping validation: on test failure, stop or rollback — never “declare done”.
- No guessing: critical assumptions must be confirmed with the user.

### 1.2 “Full permissions” risk mitigation (process, not permission walls)
- High-risk actions must be explicitly gated by commands: `/vibe/apply`, `/vibe/deploy`, `/vibe/release`, `/vibe/db-migrate`.
- Before any write, produce a change plan + risk notes + validation commands.
- On failure, enter a “stop-the-bleeding loop” (stop/rollback/diagnose/retest).

---

## 2. Agent System Design (Multi-agent + Auto-routing + Explicit Gates)

### 2.4 Orchestration rollout (oh-my-opencode)
- Project-level orchestration config: `.opencode/oh-my-opencode.json`
  - Enable `sisyphus_agent`: Prometheus writes plans to `.sisyphus/plans/`; Sisyphus handles execution
  - Use `agents.Sisyphus.prompt_append` to inject Vibe gates & hard constraints (without forcing model changes)

> Note: Vibe still uses `/vibe/*` command gates as the stable control plane; orchestration helps routing and parallel context gathering but must not bypass gates.

### 2.1 Minimal role set
- `planner`: clarify requirements, decompose tasks, define acceptance and risks; no direct edits.
- `executor`: implement minimal necessary changes; stop-the-bleeding on failures.
- `reviewer`: review diffs for boundaries, style, and regression risk.
- `test-engineer`: own validation & failure diagnosis; produce repro steps and minimal tests.
- `release-engineer`: own build/package/release/deploy entrypoints and rollback strategy.
- `frontend-ui-ux-engineer` (optional): dedicated UI/UX workstream.
- `ai-engineer` (optional): langgraph/langchain graphs, prompts, evaluations.

### 2.2 Routing rules
- Default: auto-route based on task type (Category + Skill composition).
- Mandatory gates: irreversible/high-risk actions must be triggered explicitly via commands.

### 2.3 Permission strategy
- `planner`: ideally read-only + limited bash for diagnostics.
- `executor/test/release`: full permissions, but must respect gates and DoD.

---

## 3. Two Paradigms: Strict vs Flexible

### 3.1 Strict paradigm (Spec/Plan-driven)
Use for: larger scope, multi-person work, unclear requirements, higher risk.
- Core assets: a durable plan (tasks/acceptance/risks/rollback) + change record.
- Flow: plan (planner) → implement (executor) → validate (test-engineer) → deliver (release-engineer).

### 3.2 Flexible paradigm (Commands/Skills-driven)
Use for: short tasks, fast iteration, solo work.
- Core assets: high-quality commands (repeatable pipelines) + skills (tool toggles & knowledge packs).
- Flow: enter a fixed pipeline via commands to reduce free-form drift.

---

## 4. Scenario Matrix

| Scenario | Recommended paradigm | Default entry | Mandatory gates |
|---------|-----------------------|---------------|-----------------|
| Backend-only (uv) | Strict/Flexible | `/vibe/plan`→`/vibe/apply`→`/vibe/test` | `/vibe/apply` `/vibe/release` |
| Full-stack (Ant Design Pro) | Prefer Strict | `/vibe/plan`→`/vibe/apply`→`/vibe/test`→`/vibe/build` | `/vibe/deploy` |
| Embedded AI (langgraph/langchain) | Prefer Strict | `/vibe/plan`→`/vibe/apply`→`/eval` | `/vibe/release` |

---

## 5. Commands Design (Explicit gates + repeatable pipelines)

### 5.1 Layers
- Entry commands: `/vibe/plan`, `/vibe/ship`
- Gate commands: `/vibe/apply`, `/vibe/deploy`, `/vibe/release`, `/vibe/db-migrate`
- Validation commands: `/vibe/test`, `/vibe/lint`, `/vibe/build`, `/vibe/preview`
- Review command: `/vibe/review`
- Help command: `/vibe/help`

### 5.2 Command contract
Each command must output:
- Inputs: goal + constraints + impacted area
- Steps: copy-pastable steps + expected results + failure routing
- Auto-injected context:
  - `git status`, `git diff`, `git log -n 20`
  - latest test/build output

---

## 6. Skills Design (tool/knowledge packs)

### 6.1 Skill boundaries
A skill is not “a task”; it is:
- tool toggles (network/LSP/AST-grep usage)
- knowledge pack (repo conventions, testing, release)

### 6.2 Recommended initial skill set
- `git-master`: commit/review/rollback discipline
- `python-uv-backend`: uv/pytest conventions
- `frontend-ant-design-pro`: Umi Max build/deploy notes (see 8.2)
- `release-playbook`: artifact/release/deploy entrypoints
- `ui-ux-pro-max`: UI/UX retrieval + implementation guidance (backed by `ui-ux-pro-max-skill`)
- `planning-with-files`: on-disk working memory for long tasks (3-file pattern + hooks)
- `ai-langgraph-langchain`: graphs/prompts/evals

---

## 7. MCP Strategy (on-demand + context budgeting)

### 7.1 MCP servers you approved (excluding websearch/grep_app)
- `augment-context-engine` (`auggie --mcp`)
- `mcp-deepwiki` (`npx -y mcp-deepwiki@latest`)
- `playwright` (`npx -y @playwright/mcp@latest`)
- `context7` (OpenCode recommends remote `https://mcp.context7.com/mcp`; Codex can use streamable_http pointing to the same URL)
- `sequential-thinking` (`npx -y @modelcontextprotocol/server-sequential-thinking`)

### 7.2 Enablement order
1) Base → 2) Extended → 3) Automation

### 7.3 OpenCode `mcp` section template (JSON)

Copyable example file: `mcp/opencode.mcp.example.jsonc`
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

### 7.4 Codex (TOML) mapping skeleton

Copyable example file: `mcp/codex.config.toml.example`
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

## 8. End-to-end Playbooks (Plan → Implement → Test → Fix → Ship)

### 8.0 Two entry paths (how to actually use it)
- **Complex but you don’t want to explain context**: type `ulw` (oh-my-opencode will parallelize research and drive execution).
- **Complex and you need precise/verifiable execution**: use `@plan` → `/start-work`.
  - Prometheus writes the plan to `.sisyphus/plans/`
  - Sisyphus executes and delegates work to sub-agents

### 8.0.1 How orchestration and gates work together
- Orchestration: routing, parallel exploration, sequencing.
- Gates: explicit triggers for high-risk actions.
  - Any real write/deploy/release/migration must go through: `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`
- Recommended strategy:
  - `@plan` creates the plan → during execution Sisyphus prompts `/vibe/apply` when code changes are needed
  - Validation: `/vibe/test` `/vibe/lint` `/vibe/build` `/vibe/preview`
  - Review: `/vibe/review`

### 8.1 Python backend (uv)
- Standard test entrypoint: `uv run python -m pytest`

### 8.2 Frontend (Ant Design Pro / Umi Max) using yarn
Based on upstream scripts/CI patterns:
- Dev: `yarn start:dev` (prefer no-mock by default)
- Quality gate: `yarn lint` (Biome + `tsc --noEmit`)
- Build: `yarn build` → artifact in `dist/`
- Preview: `yarn preview` (build then preview)
- Pre-deploy checks: `publicPath`, asset paths, and note that proxy does not apply in production.

### 8.3 Makefile as the unified entrypoint
Define naming conventions; implementation lives in `scripts/*.sh`.
- `make lint`
- `make test` (backend: `uv run python -m pytest`)
- `make build` (frontend: `yarn build`)
- `make deploy` (calls `scripts/deploy.sh`, must print rollback steps)

---

## 9. Deliverables (what to generate next)
- `AGENTS.md`: repo-level rules (hard constraints + gates + default commands)
- `CLAUDE.md`: architecture/dir map for fast navigation
- `.opencode/command/`: entry + gate + validation commands (e.g. `/vibe/apply` `/vibe/deploy` `/vibe/release` `/vibe/db-migrate`)
- `.opencode/skill/`: domain skills and tool toggles (`SKILL.md`)
- `mcp/`: OpenCode JSON fragments + Codex TOML fragments
- `Makefile` + `scripts/`: build/test/deploy entrypoints

---

## 10. Iteration & Rollout
- Personal phase: stabilize commands + gates; collect failure cases and routes.
- Team phase: turn into a template repo with versioned rules.
- Governance: version and rollback policies for all rule assets.
