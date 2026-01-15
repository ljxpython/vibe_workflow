# ui-ux-pro-max-skill 能力地图（供本仓库复用）

## 核心能力
- 设计智能数据库：UI styles / color palettes / font pairings / chart types / product recommendations / UX guidelines
- 支持多技术栈：`html-tailwind`（默认）、`react`、`nextjs`、`vue`、`svelte`、`swiftui`、`react-native`、`flutter`、`shadcn`

## 本地检索入口（无需联网）
- `python3 ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> [-n <max_results>]`
- domain：product/style/typography/color/landing/chart/ux/prompt
- stack：`--stack <stack>`（默认 html-tailwind）

## 跨平台分发点（你未来会用其官方 CLI 部署）
- Claude Code：`.claude/skills/ui-ux-pro-max/`
- Cursor：`.cursor/commands/ui-ux-pro-max.md` + `.shared/ui-ux-pro-max/`
- Windsurf：`.windsurf/workflows/ui-ux-pro-max.md` + `.shared/ui-ux-pro-max/`
- Antigravity：`.agent/workflows/ui-ux-pro-max.md` + `.shared/ui-ux-pro-max/`
- GitHub Copilot：`.github/prompts/ui-ux-pro-max.prompt.md` + `.shared/ui-ux-pro-max/`

## 复用建议（与 /vibe 协作）
- UI/UX 需求触发该 skill 后：先检索 → 再把结果转成可执行 UI 方案 → 再用 `/vibe/apply` 写入
- 验证链路：`/vibe/lint`、`/vibe/build`、必要时 `/vibe/preview`
