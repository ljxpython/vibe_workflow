---
name: python-uv-backend
description: |
  Python3 + uv 项目的开发/测试/修复闭环。提供：测试入口标准化、常见项目结构与排错路径。
  适用：实现后端功能、修复后端 bug、增加/修复测试、依赖与运行问题排查。
  不适用：未明确技术栈的项目（先确认是否为 uv 管理）。
---

# Python (uv) Backend

## 约定
- 测试入口：`uv run python -m pytest`

## 标准流程
1) 澄清：期望行为、输入输出、复现步骤、错误日志。
2) 定位：优先最小复现与最相关测试。
3) 修复：只改与 root cause 相关的最小代码。
4) 验证：
   - 最小集：针对性测试
   - 全量：`uv run python -m pytest`

## 推荐命令（本仓库约定）
- `/vibe/test`：运行测试并基于输出给修复路径
- `/vibe/apply`：进入写入门禁（强制审计+验证）

## 参考资料（按需加载）
- 测试与验证规范：读取 `references/testing.md`
- 问题定位指南：读取 `references/debugging.md`
- 项目骨架参考：读取 `references/project-skeleton.md`

## 常见失败分流
- 依赖/解释器问题：确认 uv 环境与 lock 状态。
- 测试失败：先区分“本次引入” vs “历史就坏”。
- 性能/并发：先量化再优化，不做无证据重构。
