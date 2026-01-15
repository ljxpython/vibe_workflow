# planning-with-files 集成坑点（给 AI 用）

## 1) 三文件必须放在“项目根目录”
`task_plan.md/findings.md/progress.md` 应该在你的工作目录（项目根）创建，而不是在 skill/plugin 安装目录。

## 2) hooks 的价值在于“注意力操控”
- PreToolUse 在 Write/Edit/Bash 前重读 `task_plan.md` 头部，用来防止 goal drift。
- Stop hook 会做完成性检查：如果 phases 没完成，会阻止停止。

## 3) 与 /vibe 的协作点
- `/vibe/plan` 的结构化计划要落盘到 `task_plan.md`，否则 planning-with-files 的 hooks 读不到关键目标。
- 任何失败必须落盘并改变策略（Never Repeat Failures），否则会在长任务里重复踩坑。
