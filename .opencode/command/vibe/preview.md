---
description: 本地预览构建产物（部署前验收）
agent: build
---

在部署前本地预览构建产物，确保静态资源路径与入口无误。

## 执行
- !`yarn preview`

## 输出要求
- 预览端口与访问方式
- 若白屏/资源 404，优先检查 publicPath 与部署子路径
