---
description: 运行测试并基于输出给出修复路径
agent: build
---

根据当前项目情况运行测试并分析输出。

## 先识别测试入口
- Python/uv 项目：`uv run python -m pytest`
- 前端项目：识别 package manager 并运行对应测试脚本（如 `yarn test`）

## 执行
- Python：!`uv run python -m pytest`

## 输出要求
- 贴出关键错误段
- 给出最小修复方案
- 给出复测命令
