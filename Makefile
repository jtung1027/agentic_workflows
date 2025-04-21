.PHONY: formatcheck install-dev

formatcheck:
	@echo "Running ruff format..."
	ruff format .
	@echo "Running ruff check (with fixes)..."
	ruff check . --fix
	@echo "Running mypy..."
	mypy .
	@echo "Format, lint, and type checks complete."

# Optional: Target to install dependencies locally
install-dev:
	poetry install --with dev 