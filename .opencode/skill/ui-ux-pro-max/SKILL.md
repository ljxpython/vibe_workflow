---
name: ui-ux-pro-max
description: |
  复用 ui-ux-pro-max-skill 的设计智能能力：样式/配色/字体/UX 指南/stack 最佳实践与本地搜索脚本。适用：任何涉及 UI/UX 设计与前端视觉质量提升的任务。
  不适用：纯后端逻辑任务。
---

# UI UX Pro Max

## 能力概览
- 可搜索数据库：styles/colors/typography/charts/ux-guidelines/stack 指南
- 本地搜索脚本：
  - `python3 ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>`

## 复用策略（按你未来的部署方式）
- 你未来会用它自己的 CLI（`uipro init --ai ...`）进行部署：那就优先依赖它的安装结果，不在本仓库重复分发。
- 本仓库的作用：让 AI 知道“该去哪里查”和“怎么查”，并把查询结果转成可执行 UI 方案。

## 推荐查询顺序（高产）
1) product → 2) style → 3) typography → 4) color → 5) ux → 6) stack

## 参考资料（按需加载）
- 能力地图与路径：读取 `references/capabilities.md`
- 集成坑点：读取 `references/gotchas.md`

## 与 /vibe 命令体系的协作
- 先 `/vibe/plan` 定验收（包含视觉验收点）
- 再 `/vibe/apply` 写入
- 验证：`/vibe/lint`、`/vibe/build`、必要时 `/vibe/preview`
