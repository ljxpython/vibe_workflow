# ui-ux-pro-max-skill 集成坑点（给 AI 用）

## 1) 路径差异（最重要）
不同助手的入口文件调用的脚本路径不同：
- Claude Code 通常走 `.claude/skills/ui-ux-pro-max/scripts/search.py`
- Cursor/Windsurf/Antigravity/Copilot/Gemini 等通常走 `.shared/ui-ux-pro-max/scripts/search.py`
- Trae 可能走 `.trae/skills/ui-ux-pro-max/scripts/search.py`

结论：你未来按它项目自己的 CLI（uipro）部署时，必须让“对应助手所需的目录”都到位，不能只拷一份。

## 2) Windows 编码
`.shared/.../search.py` 明确处理了 Windows stdout 编码问题（cp1252 → utf-8），而 `.claude/.../search.py` 未必有同样处理。

如果未来在 Windows 的 Claude Code 环境出现 `UnicodeEncodeError`：优先使用 `.shared` 版本，或把同样的 stdout wrapper 同步到 `.claude` 版本。

## 3) CLI 行为与 README 可能不一致
- `uipro update` 本质上等价于强制 `init`（force=true）
- README/cli 文档里出现的 `uipro init --version <tag>` 可能只是提示文本，CLI 参数不一定真的实现

## 4) 多处副本同步
该项目强调“多平台同步”，同一份 scripts/data 会被复制到多个目录（如 `.shared`、`cli/assets` 等）。
如果你后续要维护它的源码，不要在单处改完就停，需要按它仓库的 sync rules 同步。
