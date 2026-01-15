# 全栈交付失败分流（Stop-the-bleeding）

## 1) 测试失败
- 原则：先止血，再定位 root cause
- 动作：
  - 输出关键错误片段
  - 给最小修复方案
  - 复测：`uv run python -m pytest`

## 2) 前端 lint/build 失败
- 动作：
  - 先 `yarn lint` 修到通过
  - 再 `yarn build`
  - OOM 优先加 Node 内存参数

## 3) 部署后白屏/静态资源 404
- 高概率：`publicPath` / 部署子路径不一致
- 动作：回滚静态资源到上一个可用版本，再修复并复测

## 4) 生产联调问题
- 关键事实：proxy 仅开发环境
- 动作：回滚并在网关/Nginx/后端层解决转发与跨域
