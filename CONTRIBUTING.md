# Contributing to GTM:OS

Thanks for your interest in contributing.

## Development Setup

```bash
git clone https://github.com/b3dmar/gtm-os.git
cd gtm-os
uv sync --group dev
```

## Running Checks

```bash
uv run ruff check
uv run ruff format --check
uv run mypy --strict src/
uv run pytest
```

## Adding a Skill

1. Add a `SkillSpec` entry to `src/gtm_os/catalog.py`
2. Create the template in `src/gtm_os/templates/skills/<slug>.md`
3. Run `uv run gtm-os install --list` to verify it appears
4. Run the full check suite

## Adding an Agent

1. Add an `AgentSpec` entry to `src/gtm_os/catalog.py`
2. Create the template in `src/gtm_os/templates/agents/<slug>.md`
3. Run `uv run gtm-os install --ai claude` and verify it installs

## Pull Requests

- Keep PRs focused and under 200 lines where possible
- Run all checks before submitting
- Describe what the skill/agent does and how to test it
