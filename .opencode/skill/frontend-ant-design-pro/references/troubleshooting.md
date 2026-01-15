# Ant Design Pro（Umi Max）Troubleshooting

## 1) 构建失败（依赖/Node）
- 症状：安装失败、peer deps 冲突
  - 优先检查项目是否有类似 `legacy-peer-deps` 的约定
  - 统一包管理器（你这里默认 yarn）

## 2) build OOM（内存不足）
- 症状：`JavaScript heap out of memory`
- 处理顺序：
  1. 先加大 Node 内存参数（例如 `NODE_OPTIONS=--max_old_space_size=4096`）
  2. 再确认是否是构建缓存/依赖爆炸
  3. 最后才考虑业务代码层面的优化

## 3) 部署后白屏/静态资源 404
- 最高概率：`publicPath` 与真实部署子路径不一致
- 检查项：
  - 是否部署在 `/` 以外的子路径
  - 静态资源引用路径是否带上部署前缀

## 4) 接口联调在生产不通
- 关键事实：`proxy` 仅开发环境有效
- 生产需要：网关/Nginx/后端层解决转发与跨域

## 5) mock 干扰真实接口
- 症状：你以为在请求后端，实际上被 mock 拦截
- 处理：明确用无 mock 的启动方式（项目约定不同，优先看 package.json scripts）
