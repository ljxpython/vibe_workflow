---
description: 门禁：部署/上线（构建产物 + 执行部署脚本）
agent: build
---

你正在执行一个高风险动作：部署/上线。

## 目标
$ARGUMENTS

## 强制前置检查
1) 明确部署目标环境（dev/test/stage/prod）与回滚策略。
2) 必须先跑验证：
   - 后端：`uv run python -m pytest`
   - 前端（若存在）：`yarn lint`、`yarn build`
3) 前端（Ant Design Pro / Umi Max）部署前检查：
   - 产物目录是否为 `dist/`
   - `publicPath` 是否与部署路径一致
   - 确认：代理配置仅开发环境有效（生产不可依赖 proxy）

## 部署入口（推荐）
- 优先走 Makefile：`make deploy`
- Makefile 内部应调用：`scripts/deploy.sh`

## 审计输出（最小必要）
- !`git status --porcelain`
- !`git log --oneline -10`
- !`git diff --stat`

## 完成条件
- 输出：部署命令、产物位置、目标地址/健康检查方式。
- 输出：回滚命令与触发条件。
