---
description: 运行质量门禁（lint/typecheck）并给出修复建议
agent: build
---

运行当前项目的质量门禁，并基于输出给出最小修复建议。

## 默认约定
- 后端（Python/uv）：优先运行测试而非 lint（若项目提供 ruff/mypy/flake8，再按项目约定运行）
- 前端（Ant Design Pro/Umi Max）：`yarn lint`

## 执行
- 前端（若存在）：!`yarn lint`

## 输出要求
- 给出失败文件列表与最小修复步骤
- 说明是否与本次变更相关
- 给出复测命令
