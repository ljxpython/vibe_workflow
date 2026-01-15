# planning-with-files 能力地图（供本仓库复用）

## 核心能力
- 3-file pattern：`task_plan.md` / `findings.md` / `progress.md`
- hooks：SessionStart / PreToolUse / PostToolUse / Stop
  - PreToolUse：在 Write/Edit/Bash 前自动读 `task_plan.md` 头部（把目标拉回注意力）
  - Stop：自动运行完成性检查脚本（check-complete）

## 官方使用路径（Claude Code）
- 插件安装（示例）：
  - `/plugin marketplace add OthmanAdi/planning-with-files`
  - `/plugin install planning-with-files@planning-with-files`
- 手动触发：`/planning-with-files`

## 与 /vibe 协作建议
- `/vibe/plan` 输出后，把摘要同步写入 `task_plan.md`
- 重要发现写入 `findings.md`
- 测试/构建/部署输出写入 `progress.md`
