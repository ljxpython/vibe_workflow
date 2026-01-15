.PHONY: help lint test build preview deploy

SHELL := /bin/bash

help: ## Show available targets
	@printf "Vibe Makefile targets:\n\n"
	@printf "  make lint     - Frontend lint (yarn lint) if package.json exists\n"
	@printf "  make test     - Backend tests (uv run python -m pytest) if pyproject.toml exists\n"
	@printf "  make build    - Frontend build (yarn build) if package.json exists\n"
	@printf "  make preview  - Frontend preview (yarn preview) if package.json exists\n"
	@printf "  make deploy   - Run scripts/deploy.sh (safe default)\n\n"

lint: ## Run frontend lint if present
	@if [ -f package.json ]; then \
		command -v yarn >/dev/null 2>&1 || { echo "缺少 yarn（请先安装/或改用项目实际包管理器）"; exit 1; }; \
		yarn lint; \
	else \
		echo "未发现 package.json，跳过前端 lint"; \
	fi

test: ## Run backend tests if present
	@if [ -f pyproject.toml ]; then \
		command -v uv >/dev/null 2>&1 || { echo "缺少 uv（请先安装 uv）"; exit 1; }; \
		uv run python -m pytest; \
	else \
		echo "未发现 pyproject.toml，跳过后端测试"; \
	fi

build: ## Build frontend if present
	@if [ -f package.json ]; then \
		command -v yarn >/dev/null 2>&1 || { echo "缺少 yarn（请先安装/或改用项目实际包管理器）"; exit 1; }; \
		yarn build; \
	else \
		echo "未发现 package.json，跳过前端构建"; \
	fi

preview: ## Preview frontend build if present
	@if [ -f package.json ]; then \
		command -v yarn >/dev/null 2>&1 || { echo "缺少 yarn（请先安装/或改用项目实际包管理器）"; exit 1; }; \
		yarn preview; \
	else \
		echo "未发现 package.json，跳过前端预览"; \
	fi

deploy: ## Deploy via scripts/deploy.sh
	@bash ./scripts/deploy.sh
