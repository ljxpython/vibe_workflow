---
name: frontend-ant-design-pro
description: |
  Ant Design Pro（Umi Max）前端项目的开发/质量门禁/构建/部署前检查。提供：yarn 脚本约定、产物目录、常见坑点。
  适用：前端开发、构建失败排查、上线前静态资源检查、与后端联调。
  不适用：非 Umi Max/非 Ant Design Pro 的前端项目（先识别脚手架）。
---

# Ant Design Pro (Umi Max)

## 关键事实（用于自动化）
- 开发命令通常为：`yarn start:dev`
- 质量门禁：`yarn lint`（Biome + `tsc --noEmit`）
- 构建命令：`yarn build`，产物目录通常为 `dist/`
- 预览：`yarn preview`（先 build 再 preview）

## 部署前检查（最常出错）
1) `publicPath` 是否与部署路径一致（否则静态资源 404/白屏）。
2) `proxy` 仅对开发环境有效：生产必须靠网关/Nginx/后端解决转发与跨域。
3) 构建 OOM 时优先考虑 Node 内存参数，而不是乱改代码。

## 参考资料（按需加载）
- 上线前检查清单：读取 `references/checklist.md`
- 故障排查手册：读取 `references/troubleshooting.md`

## 推荐命令（本仓库约定）
- `/vibe/lint`：质量门禁
- `/vibe/build`：构建产物（通常 `dist/`）
- `/vibe/preview`：部署前本地预览
- `/vibe/deploy`：上线门禁（含部署前检查）

## 输出要求
- 对任何构建/部署问题：给出“复现命令 + 预期 vs 实际 + 最小修复方案”。
