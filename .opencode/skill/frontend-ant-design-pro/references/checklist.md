# Ant Design Pro（Umi Max）上线前检查清单

## 构建与产物
- `yarn lint` 通过
- `yarn build` 成功
- 产物目录为 `dist/`

## 静态资源与路由
- `publicPath` 与实际部署路径一致（子路径部署时必须调整）
- SPA 路由回退：确保网关/Nginx/后端配置了 fallback（否则刷新 404）

## 代理与联调
- `proxy` 仅开发环境有效：生产必须靠网关/Nginx/后端解决转发与跨域

## 常见故障速查
- 白屏/资源 404：优先查 `publicPath` 与部署子路径
- build OOM：优先加大 Node 内存参数，而不是改业务代码
