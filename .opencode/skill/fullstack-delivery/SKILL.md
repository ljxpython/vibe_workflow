---
name: fullstack-delivery
description: |
  全栈交付技能：把后端（Python+uv）与前端（Ant Design Pro/yarn）的开发、验证、构建、部署串成可执行闭环。提供：闭环步骤、命令顺序、风险点与回滚。
  适用：你需要把一个需求从规划推进到可上线交付（含前后端联动）。
  不适用：不清楚是否包含前端/后端、或目标环境/部署方式不明确（必须先问清楚）。
---

# Full-stack Delivery

## 入口
- `/vibe/ship <目标>`：生成闭环 checklist

## 强制澄清（缺一不可）
1) 本次交付包含：后端 / 前端 / 都包含？
2) 目标环境：dev/test/stage/prod？
3) 部署方式：静态资源发布到哪里？后端如何发布？
4) 验收标准：关键路径是什么？

## 标准闭环（默认顺序）
1) `/vibe/plan`：把目标/非目标/验收/风险/回滚写死
2) `/vibe/apply`：进入写入门禁（最小改动）
3) `/vibe/test`：后端 `uv run python -m pytest`
4) `/vibe/lint`：前端 lint（如存在）
5) `/vibe/build`：前端构建产物（通常 `dist/`）
6) `/vibe/preview`：部署前预览（可选但推荐）
7) `/vibe/review`：审查当前改动（Approve/Request changes）
8) `/vibe/deploy`：上线门禁（必须包含回滚与发布后验证）

## 参考资料（按需加载）
- 闭环检查清单：读取 `references/checklist.md`
- 故障分流：读取 `references/failure-routing.md`
