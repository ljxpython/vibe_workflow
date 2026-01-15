# Vibe Deployment Tool (vibe-kit) Technical Spec

> Goal: safely and repeatably deploy this repo’s “AI development OS” assets (e.g. `AGENTS.md`, `CLAUDE.md`, `.opencode/command/vibe/*`, `.opencode/skill/*`, MCP snippets) into any target project, while integrating external repos via their official installation paths (not re-implementing them).

---

## 0. Background

Your system has two layers:
1) **Vibe-owned assets**: rules, commands, skills, paradigm docs.
2) **External reusable assets**:
   - `ui-ux-pro-max-skill`: design intelligence + local search
   - `planning-with-files`: on-disk working memory + hooks (Claude Code plugin/skill)

This spec turns “manual copy/paste” into a reliable, auditable deployment tool.

---

## 1. Goals

1) One-shot bootstrap: install/update Vibe assets into a target repo.
2) Optional components:
   - commands only (`/vibe/*`)
   - skills only
   - rules sync (`AGENTS.md`/`CLAUDE.md`)
3) Safety & auditability:
   - backups for overwritten files
   - dry-run support
   - rollback support
4) External integration by orchestration (not reimplementation):
   - `ui-ux-pro-max-skill` via official `uipro` CLI
   - `planning-with-files` via official Claude Code plugin commands

---

## 2. Non-goals

- Not replacing external projects’ official installers.
- Not deploying to production environments directly.
- Not building a GUI; prefer CLI + config.

---

## 3. Users & Use Cases

- Personal bootstrap for new projects.
- Team-wide standardization.
- Upgrade flows (sync to latest Vibe assets).

---

## 4. Asset Boundaries & Mapping

### 4.1 Vibe assets (this repo)
Must be deployable (selectively):
- `AGENTS.md`
- `CLAUDE.md`
- `.opencode/command/vibe/*.md`
- `.opencode/skill/*/SKILL.md`
- `.opencode/skill/*/references/*.md`
- `plans/ai-dev-paradigm-plan.zh.md`
- `plans/ai-dev-paradigm-plan.en.md`

Optional:
- MCP config snippets (prefer “generate snippets” vs overwriting user config)

### 4.2 External projects (orchestrate only)
- `ui-ux-pro-max-skill`:
  - recommended: `npm install -g uipro-cli` + `uipro init --ai <type>`
  - path gotchas: `.claude` vs `.shared` vs `.trae` are handled by their CLI
- `planning-with-files`:
  - recommended (Claude Code):
    - `/plugin marketplace add OthmanAdi/planning-with-files`
    - `/plugin install planning-with-files@planning-with-files`

---

## 5. CLI Design (proposal)

Tool name: `vibe-kit` (avoid confusion with `/vibe/*` slash commands).

- `vibe-kit init --target <path> [--profile <name>] [--dry-run]`
- `vibe-kit sync --target <path> [--dry-run]`
- `vibe-kit uninstall --target <path>`
- `vibe-kit doctor --target <path>`

### Profiles
- `minimal`: rules + `/vibe/*` commands
- `standard`: minimal + skills + plans
- `full`: standard + print external installation guidance (no auto-install by default)

---

## 6. Safety Requirements

- Dry-run prints what will be written/overwritten.
- Backups for any overwritten file:
  - `<target>/.vibe-kit-backup/<timestamp>/...`
- Conflict policy:
  - do not overwrite user-modified files unless `--force`
  - if overwriting, must backup + print a diff summary
- Idempotency: repeated runs should be safe.

---

## 7. Versioning

- Source version should come from git tag or a dedicated version file.
- Target repo gets an install marker:
  - `.vibe-kit/version.json` (source version, install time, profile, installed components)

---

## 8. Testing the Deployment Tool

Minimum checks:
- run `init` into an empty temp project
- verify expected files exist
- run `doctor` to confirm health
- run `uninstall` to restore state

---

## 9. Collaboration with `/vibe/*`

- `vibe-kit` only installs assets.
- `/vibe/*` commands run the execution loop (plan/apply/test/build/deploy).
- external capabilities are enabled via `external-*` skills + external official installers.

---

## 10. Open Questions (must answer before implementation)

1) Implementation language: Python (uv) vs Node?
2) Platforms: macOS-only vs cross-platform (Windows/Linux)?
3) Allow auto-running external installers, or print-only with explicit confirmation?
