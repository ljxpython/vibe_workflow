# 使用指南（vibe-wf）

目标：让个人在任何项目里用 OpenCode + oh-my-opencode 更高效地跑完整开发链路：规划→开发→测试→修复→交付。

## Quick Start
1) 在项目根目录运行：
```bash
uvx vibe-wf init
```

2) 打开 OpenCode，按 `CLAUDE.md` / `AGENTS.md` 的入口开始。

## 常用命令
- 规划：`/vibe/plan <需求>`
- 写入门禁：`/vibe/apply <目标>`
- 验证：`/vibe/test`、`/vibe/lint`、`/vibe/build`
- 审查：`/vibe/review`

## 卸载
```bash
uvx vibe-wf uninstall
```

> 卸载只影响项目内由 vibe-wf 管理的文件，不会修改系统配置。
