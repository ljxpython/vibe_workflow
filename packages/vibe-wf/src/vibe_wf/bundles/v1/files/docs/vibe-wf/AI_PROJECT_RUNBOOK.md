# AI 项目执行手册（Project-local）

你在这个项目里的使命：帮助用户用 OpenCode + oh-my-opencode 的方式，高效完成开发全链路（规划→开发→测试→修复→交付）。

## 0) 硬约束（必须遵守）
- 只允许修改本项目目录内文件（project-local only）。
- 默认不修改系统级配置：例如 `~/.config/opencode/*`、`~/.codex/*`。
- 如确需建议系统级操作：必须先征得用户明确同意，并先展示拟修改 diff。

## 1) 推荐工作流（最短闭环）
1. 读规则：`AGENTS.md`
2. 规划：`/vibe/plan <需求>`
3. 写入：`/vibe/apply <目标>`
4. 验证：`/vibe/test`、`/vibe/lint`、`/vibe/build`
5. 审查：`/vibe/review`

## 2) 安装与配置（系统级：只给指引，不自动执行）
按照这里的说明进行安装和配置：
https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/refs/heads/master/README.md

> 注意：该链接可能涉及系统级变更。默认不要自动执行；必须用户明确同意且先展示 diff。

## 3) MCP / 模型 / API（项目级示例）
- MCP 项目级配置说明：`docs/vibe-wf/MCP_GUIDE.md`
- snippets：`.vibe-wf/snippets/`
