# 全栈交付检查清单

## Plan
- 目标、非目标、验收标准明确
- 风险点与回滚策略明确

## Apply（写入）
- 只做最小必要改动
- 改动可追溯（git status/log/diff）

## 后端验证
- `uv run python -m pytest` 通过

## 前端验证（如存在）
- `yarn lint` 通过
- `yarn build` 成功，产物 `dist/`
- 必要时 `yarn preview` 验证静态资源路径

## Deploy
- 目标环境明确
- 回滚命令明确
- 发布后验证明确（健康检查 + 关键路径）
