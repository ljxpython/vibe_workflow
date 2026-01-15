---
description: 运行测试并基于输出给出修复路径
agent: build
---

根据当前项目情况运行测试并分析输出：

## 1) 先识别测试入口
- 如果项目包含 Python/uv：优先运行 `uv run python -m pytest`
- 如果项目包含前端：识别 package manager（默认 yarn）并运行对应测试脚本（如 `yarn test`）

## 2) 执行并收集输出
- Python：!`uv run python -m pytest`

> 若命令失败，必须：
> - 贴出关键错误段
> - 给出最小修复方案
> - 给出复测命令

## 3) 输出要求
- 失败归因：本次引入 vs 历史遗留（基于 git diff/近期改动判断）
- 修复策略：只修 root cause，禁止顺手重构
- 复测与验收：列出你会跑的命令清单
