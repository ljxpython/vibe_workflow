#!/usr/bin/env bash
set -euo pipefail

show_help() {
  cat <<'EOF'
用法：
  scripts/deploy.sh [--env <dev|test|stage|prod>] [--static-dest <path>] [--frontend-dist <dir>] [--dry-run]

参数：
  --env            目标环境（默认 dev）
  --static-dest    前端静态产物发布目录（可选；提供后会执行复制）
  --frontend-dist  前端构建产物目录（默认 dist）
  --dry-run        只打印将执行的动作，不落盘

示例：
  # 1) 只输出部署提示（默认行为）
  ./scripts/deploy.sh --env stage

  # 2) 发布前端 dist 到本地目录（会备份旧版本）
  ./scripts/deploy.sh --env prod --static-dest /var/www/my-app
EOF
}

ENV_NAME="dev"
STATIC_DEST=""
FRONTEND_DIST="dist"
DRY_RUN="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --env)
      ENV_NAME="${2:-}"
      shift 2
      ;;
    --static-dest)
      STATIC_DEST="${2:-}"
      shift 2
      ;;
    --frontend-dist)
      FRONTEND_DIST="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN="true"
      shift
      ;;
    -h|--help)
      show_help
      exit 0
      ;;
    *)
      echo "未知参数：$1" >&2
      echo "使用 --help 查看用法" >&2
      exit 2
      ;;
  esac
done

case "$ENV_NAME" in
  dev|test|stage|prod) ;;
  *)
    echo "非法 --env：$ENV_NAME（只允许 dev/test/stage/prod）" >&2
    exit 2
    ;;
esac

if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[审计] git status:";
  git status --porcelain || true
  echo "[审计] git rev:";
  git rev-parse --short HEAD || true
fi

echo "[信息] ENV=$ENV_NAME"

echo "[检查] 前端产物目录：$FRONTEND_DIST"

if [[ -n "$STATIC_DEST" ]]; then
  if [[ ! -d "$FRONTEND_DIST" ]]; then
    echo "未找到前端产物目录：$FRONTEND_DIST" >&2
    echo "建议先运行：make build（或 /vibe/build）" >&2
    exit 1
  fi

  timestamp="$(date +%Y%m%d%H%M%S)"
  backup_dir="${STATIC_DEST}.bak.${timestamp}"

  echo "[动作] 发布前端静态资源 → $STATIC_DEST"
  echo "[动作] 备份旧目录（如存在）→ $backup_dir"

  if [[ "$DRY_RUN" == "true" ]]; then
    echo "[dry-run] 将执行：mkdir -p '$STATIC_DEST'"
    echo "[dry-run] 将执行：若 '$STATIC_DEST' 非空则备份到 '$backup_dir'"
    echo "[dry-run] 将执行：复制 '$FRONTEND_DIST/' 到 '$STATIC_DEST/'"
    exit 0
  fi

  mkdir -p "$STATIC_DEST"

  if [[ -n "$(ls -A "$STATIC_DEST" 2>/dev/null || true)" ]]; then
    mv "$STATIC_DEST" "$backup_dir"
    mkdir -p "$STATIC_DEST"
  fi

  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$FRONTEND_DIST/" "$STATIC_DEST/"
  else
    cp -R "$FRONTEND_DIST/"* "$STATIC_DEST/"
  fi

  echo "[完成] 前端静态资源已发布到：$STATIC_DEST"
  echo "[回滚] 如需回滚：删除 '$STATIC_DEST'，并把 '$backup_dir' 改回 '$STATIC_DEST'"
  exit 0
fi

cat <<EOF
[提示] 当前脚本未配置具体部署目标，因此不会执行任何上线操作。

建议流程：
1) 验证：
   - 后端：uv run python -m pytest
   - 前端：yarn lint && yarn build
2) 预览（可选）：yarn preview
3) 部署：
   - 如果是前端静态发布：重新运行本脚本并提供 --static-dest <path>
   - 如果你有网关/Nginx/云对象存储：在 scripts/deploy.sh 中按你的环境补齐发布逻辑（不要在这里瞎猜）

你也可以用 /vibe/deploy 触发门禁流程，然后在门禁中选择最终部署命令。
EOF
