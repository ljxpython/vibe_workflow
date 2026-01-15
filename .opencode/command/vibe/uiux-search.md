---
description: UI/UX 资料检索（基于 ui-ux-pro-max-skill 本地数据库）
agent: build
---

目标：从 ui-ux-pro-max-skill 的本地数据库检索 UI/UX 方案与参考。

## 输入
$ARGUMENTS

## 用法示例
- `/vibe/uiux-search "pricing page" --domain product --stack react`
- `/vibe/uiux-search "primary button" --domain style --stack html-tailwind`
- `/vibe/uiux-search "typography scale" --domain typography --stack react`

## 执行
- !`python3 ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py $ARGUMENTS`

## 下一步建议
- 把检索结果转成可执行的改动计划：用 `/vibe/plan`
- 真正写入时走门禁：用 `/vibe/apply`
