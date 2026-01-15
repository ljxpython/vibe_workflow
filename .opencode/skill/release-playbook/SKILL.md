---
name: release-playbook
description: |
  把交付与上线流程产品化：构建、产物、部署入口、回滚策略与发布后验证。提供：Makefile target 规范与 scripts/ 约定。
  适用：需要交付、发版、部署、构建产物的任务。
  不适用：不清楚目标环境/部署方式时（必须先向用户确认）。
---

# Release Playbook

## 统一入口约定
- 以 `Makefile` 作为入口，以 `scripts/*.sh` 作为实现。

## 建议 targets
- `make lint`
- `make test`（后端：`uv run python -m pytest`）
- `make build`（前端：`yarn build`）
- `make deploy`（调用 `scripts/deploy.sh`）

## 参考资料（按需加载）
- Makefile targets 约定：读取 `references/makefile-targets.md`
- 回滚策略：读取 `references/rollback.md`

## 推荐命令（本仓库约定）
- `/vibe/build`：构建产物
- `/vibe/deploy`：上线门禁（必须给回滚）
- `/vibe/release`：发版门禁（必须给发布清单与发布后验证）

## 必须输出
- 产物位置（例如前端 `dist/`）
- 部署命令与目标地址
- 回滚命令与触发条件
- 发布后验证（健康检查、关键路径验证）
