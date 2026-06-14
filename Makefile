.PHONY: install lint format test qa docs docs-open smoke help

DOCS_SOURCE := docs
DOCS_BUILD := $(DOCS_SOURCE)/_build

install: ## Install template dependencies
	@uv sync --all-groups

lint: ## Run Ruff checks
	@uv run ruff check .

format: ## Format with Ruff
	@uv run ruff format .

test: ## Run template tests
	@uv run pytest -q

docs: ## Build template documentation
	@uv run --group docs sphinx-build $(DOCS_SOURCE) $(DOCS_BUILD)/html -b html -W

docs-open: docs ## Open docs in the browser
	@uv run -m webbrowser $(DOCS_BUILD)/html/index.html

smoke: ## Generate a project and run its QA
	@tmp_dir=$$(mktemp -d); \
	echo "Using $$tmp_dir"; \
	uv run copier copy --trust . "$$tmp_dir/internal-app" --defaults; \
	$(MAKE) -C "$$tmp_dir/internal-app" qa

qa: lint test docs ## Run all quality checks

help: ## Show available targets
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_.-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
