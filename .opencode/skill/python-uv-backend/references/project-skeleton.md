# Python（uv）项目骨架（参考）

> 目的：帮助 AI 快速判断项目结构与测试入口。

## 常见结构
- `pyproject.toml`（uv/依赖/工具配置）
- `src/` 或顶层包目录
- `tests/`

## 测试入口
- 标准：`uv run python -m pytest`
- 若存在 Makefile：优先 `make test`（但需确认其内部命令一致）
