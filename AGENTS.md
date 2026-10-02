# Repository Guidelines

## Project Structure & Module Organization

This repository contains a Python 3 API for movie recommendations. `main.py` starts the server; `api/` defines the FastAPI app and routes; `agent/` contains recommendation logic, Pydantic models, prompts, configuration, and the OMDb tool. The static design reference lives in `design/ai-social-automation.aura.build/`. There is no test directory in the current checkout. Keep new API endpoints in `api/routers.py` and agent behavior in the relevant `agent/` module.

## Build, Test, and Development Commands

- `python -m venv .venv` creates a virtual environment.
- `.venv\Scripts\Activate.ps1` activates it in Windows PowerShell.
- `python -m pip install -r requirements.txt` installs pinned dependencies.
- `python main.py` starts the development server on `http://localhost:8000` with reload enabled.
- Open `http://localhost:8000/docs` for the interactive API documentation.

Set `OPENAI_API_KEY` and `API_KEY_OMDB` in a local `.env` file before starting the recommendation agent. Never commit credentials.

## Coding Style & Naming Conventions

Use four spaces for Python indentation. Follow the existing Python conventions: `snake_case` for modules, functions, and variables; `PascalCase` for classes; uppercase names for configuration constants. Keep request and response schemas in `agent/models/`, and use Pydantic models for structured API data. No formatter or linter configuration is present; keep imports organized and match nearby code.

## Testing Guidelines

No test framework, test files, or coverage requirement is configured in this checkout. If adding tests, use `pytest`, place them in a top-level `tests/` directory, and name files `test_*.py`. Run them with `python -m pytest` after adding the dependency to the project setup.

## Commit & Pull Request Guidelines

Git history is unavailable in this checkout, so no repository-specific commit convention can be confirmed. Use short, imperative commit subjects (for example, `Add health endpoint details`). Pull requests should explain the change and its effect on the API, link related work when applicable, and include request/response examples or screenshots for visible behavior changes.
