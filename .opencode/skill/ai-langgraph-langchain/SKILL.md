---
name: ai-langgraph-langchain
description: |
  内嵌 AI 项目的工程化工作流：graph/chain 结构、提示词资产、评估用例与回归验证。提供：最小评估基线与变更审计要求。
  适用：langgraph/langchain 相关的功能实现、调参、回归修复与评估。
  不适用：没有评估样本/指标定义的 AI 需求（先让用户确认验收与评估集）。
---

# LangGraph / LangChain Engineering

## 核心原则
- AI 功能必须有可复现评估：输入集 → 期望输出/指标 → 运行方式。
- 任何 prompt/graph 改动都视为“高风险变更”，必须留证据与回归评估。

## 最小评估基线（建议）
1) 固定 10~30 条代表性样本（覆盖边界场景）。
2) 每次改动输出：命中率/失败样本/误差类型。
3) 失败必须能回滚：保留上一个可用版本的 prompt/graph。

## 推荐命令（本仓库约定）
- `/vibe/plan`：把验收与评估口径写死
- `/vibe/apply`：进入写入门禁（prompt/graph 变更视为高风险）
- `/vibe/release`：发版门禁（必须附带评估结果与回滚）

## 参考资料（按需加载）
- 最小评估基线：读取 `references/eval-baseline.md`
- 失败类型分类：读取 `references/failure-taxonomy.md`

## 输出要求
- 明确：评估方法、样本来源、结论与风险。
