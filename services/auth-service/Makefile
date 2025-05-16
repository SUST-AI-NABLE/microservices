.PHONY: dev test format lint mypy clean install build

# Development server
dev:
	uvicorn src.auth_service.driver_adapters.api.main:app --reload

# Testing
test:
	pytest

# Code quality
format:
	black .
	isort .

lint:
	ruff check .

mypy:
	mypy src

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Install package
install:
	uv pip install -e .

# Install dev dependencies
install-dev:
	uv pip install -e ".[dev]"

# Build package
build:
	python -m build
