# Makefile targets 约定（入口层）

目标：让“构建/测试/部署”成为可重复调用的确定性入口。

## 推荐 targets
- `make lint`
- `make test`
- `make build`
- `make deploy`

## 约束
- Makefile 只做编排，不堆复杂逻辑；复杂逻辑放到 `scripts/*.sh`
- 每个 target 必须可独立运行
- 每个 target 必须输出：做了什么、产物在哪、失败怎么排查
