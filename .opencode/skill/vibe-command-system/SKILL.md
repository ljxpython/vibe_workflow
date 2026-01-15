---
name: vibe-command-system
description: |
  本仓库的 OpenCode 命令体系与门禁策略（全部命令在 /vibe/* 命名空间下）。提供：命令地图、何时用门禁命令、如何跑闭环。
  适用：你需要选择/编排命令来完成规划→开发→测试→修复→上线的闭环，或需要避免与内置命令冲突。
  不适用：与本仓库无关的外部项目（先确认是否使用本套命令体系）。
---

# Vibe Command System

## 命名空间规则
- 本仓库所有自定义命令都在 `/vibe/*` 下，避免与内置命令或其他项目命令冲突。

## 一键入口
- `/vibe/help`：查看入口与常用命令
- `/vibe/ship <目标>`：生成闭环 checklist（但不会越过门禁自动执行高风险动作）

## 门禁命令（高风险）
- `/vibe/apply <目标>`：真实写入
- `/vibe/deploy <目标>`：部署/上线
- `/vibe/release <目标>`：发版
- `/vibe/db-migrate <目标>`：数据库迁移

## 日常命令
- `/vibe/plan <需求>`：最小可执行计划（含验收/风险/回滚）
- `/vibe/review`：审查当前变更（Approve/Request changes）
- `/vibe/test`：跑测试并基于输出给修复路径
- `/vibe/lint`：质量门禁（前端优先）
- `/vibe/build`：构建产物
- `/vibe/preview`：部署前预览

## 参考资料（按需加载）
- 命令地图：读取 `references/command-map.md`

## 强约束（必须遵守）
- 不许误改/不许越界：所有改动可追溯
- 不许跳过测试/验证：失败必须止血或回滚
- 不许瞎猜：关键假设必须向用户确认
