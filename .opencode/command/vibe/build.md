---
description: 构建项目产物（尤其前端 dist）并给出部署输入
agent: build
---

构建当前项目，并输出产物位置与部署输入。

## 默认约定
- 前端（Ant Design Pro/Umi Max）：`yarn build`，产物 `dist/`
- 后端：按项目实际构建方式（若无显式构建则跳过）

## 执行
- 前端（若存在）：!`yarn build`

## 输出要求
- 构建是否成功
- 产物路径（例如 `dist/`）
- 常见失败分流（OOM/依赖冲突/publicPath 等）
