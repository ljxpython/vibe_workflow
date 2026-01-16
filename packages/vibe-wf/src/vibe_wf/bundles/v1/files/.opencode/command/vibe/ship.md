---
description: 一键闭环交付（生成可复制 checklist）
agent: plan
---

目标：把一次需求从“清晰”推进到“可交付”（本命令只产出清单，不做高风险动作）。

## 输入
$ARGUMENTS

## 闭环清单（输出为可复制命令）
1) Plan：`/vibe/plan`
2) Apply Gate：需要写入时，用 `/vibe/apply`
3) Validate：`/vibe/test` `/vibe/lint` `/vibe/build`
4) Review：`/vibe/review`

## 规则
- 涉及真实写入时必须显式用门禁命令。
- 默认只修改项目内文件，不修改系统级配置。
