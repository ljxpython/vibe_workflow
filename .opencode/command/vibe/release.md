---
description: 门禁：发版（版本号/变更说明/构建/发布检查）
agent: build
---

你正在执行一个高风险动作：发版。

## 目标
$ARGUMENTS

## 强制流程
1) 识别发版对象：后端/前端/全栈/AI（langgraph/langchain）组件。
2) 输出版本策略：版本号规则、兼容性声明、回滚策略。
3) 必须先跑验证（与部署同级）：
   - 后端：`uv run python -m pytest`
   - 前端（若存在）：`yarn lint`、`yarn build`
4) 生成发布清单（Release Checklist）：
   - 变更摘要（面向用户/团队）
   - 风险点与缓解
   - 迁移步骤（如有）
   - 回滚步骤

## 审计输出
- !`git status --porcelain`
- !`git log --oneline -20`
- !`git diff --stat`

## 完成条件
- 产出可复制的发布步骤（命令级）。
- 明确“发布后验证”与失败回滚路径。
