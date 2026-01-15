---
description: UI/UX 检索脚本自检（不写入、可在 CI 运行）
agent: build
---

目标：验证 ui-ux-pro-max-skill 的搜索脚本可正常运行（不写入任何文件）。

## 执行
- !`python3 ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py --help >/dev/null`
- !`python3 ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py "smoke test" --domain ux --max-results 1 >/dev/null`

## 失败时怎么做
- 先确认 Python 可用：`python3 --version`
- 再确认脚本路径存在：`ls ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py`
- 若报依赖/导入错误：检查 `ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/` 目录是否完整
