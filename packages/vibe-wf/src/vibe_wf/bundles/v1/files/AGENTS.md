# AI 开发操作系统（Project Template）- AGENTS.md

本文件是项目的顶层行为契约：给 AI 用。

目标：让 AI 在任何项目里稳定执行全流程：规划 → 开发 → 测试 → 修复 → 交付。

> 单一真相源：本项目的行为规则以本文件为准。

## 0. 三条硬约束（不可妥协）
- 不许误改/不许越界：所有改动必须可追溯（至少输出 diff/变更摘要/影响范围）。
- 不许跳过测试/验证：测试失败必须止血或回滚；禁止“删测试/关校验”过关。
- 不许瞎猜：关键假设必须向用户确认；缺信息就问。

## 1. 项目级边界（vibe-wf 的核心承诺）
- 只允许修改本项目目录内文件（project-local only）。
- 默认不修改系统级配置：例如 `~/.config/opencode/*`、`~/.codex/*`。
- 如确需建议系统级操作：必须先征得用户明确同意，并先展示拟修改 diff。

## 2. 推荐闭环（最短路径）
1) 规划：`/vibe/plan <需求>`
2) 写入：`/vibe/apply <目标>`（门禁）
3) 验证：`/vibe/test`、`/vibe/lint`、`/vibe/build`
4) 审查：`/vibe/review`

## 3. 文档入口（给人/给 AI）
- 项目使用指南：`docs/vibe-wf/USAGE.md`
- 给 AI 的执行手册：`docs/vibe-wf/AI_PROJECT_RUNBOOK.md`
- 工具链与安装清单：`docs/vibe-wf/TOOLING.md`
- MCP 项目级配置说明：`docs/vibe-wf/MCP_GUIDE.md`
