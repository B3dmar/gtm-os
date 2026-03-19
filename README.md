# GTM:OS

Open-source GTM workflow toolkit for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/introducing-codex/), and [Claude Cowork](https://claude.ai/cowork).

8 skills and 3 agents that turn your pipeline markdown into a daily GTM operating system - morning briefs, lead qualification, prospect research, personalized outreach, and pipeline analytics.

## Install

```bash
# Install the CLI
uv tool install gtm-os
# or
pip install gtm-os

# Install skills for Claude Code
gtm-os install --ai claude

# Or for Codex
gtm-os install --ai codex
```

### Install for Claude Cowork (manual)

If you use Claude Cowork instead of Claude Code, you can add skills directly in the Cowork UI — no CLI needed.

**Option A: Build and upload (recommended)**

```bash
# Install the CLI first (see above), then:
gtm-os build-plugin

# This creates a cowork-plugin/ directory with the right layout:
# cowork-plugin/
#   skills/today/SKILL.md
#   skills/pipeline/SKILL.md
#   ...
#   agents/researcher/AGENT.md
#   ...
#   .claude-plugin/plugin.json
```

Then upload individual `SKILL.md` files from the `skills/` subdirectories:

1. Open Cowork → **Customize** → **Skills** → click **+**
2. Drag and drop any `SKILL.md` file into the upload dialog

**Option B: Upload raw skill files (no CLI)**

If you don't want to install the CLI, download `.md` files directly from [`src/gtm_os/templates/skills/`](https://github.com/B3dmar/gtm-os/tree/main/src/gtm_os/templates/skills). Before uploading, add a `name:` line to each file's frontmatter — Cowork requires both `name` and `description`:

```yaml
---
name: today
description: Morning brief - overdue follow-ups, due today, pipeline snapshot, priorities
---
```

Then drag and drop into Cowork → **Customize** → **Skills** → **+**.

## Skills

| Skill | Command | What it does |
|-------|---------|-------------|
| **Today** | `/gtm-today` | Morning brief - overdue follow-ups, due today, pipeline snapshot, priorities |
| **Pipeline** | `/gtm-pipeline` | Pipeline hygiene - stale leads, missing actions, stage transitions, metrics |
| **Qualify** | `/gtm-qualify <lead>` | Run 6-question decision filter against a lead |
| **Deep Dive** | `/gtm-deep-dive` | ICP analysis from real pipeline data - distribution, gaps, refinements |
| **Signals** | `/gtm-signals <prospect>` | Buying signal research - job postings, funding, hiring, news |
| **Prep** | `/gtm-prep <company/person>` | Meeting prep - attendee profiles, company context, talking points |
| **Personalize** | `/gtm-personalize <prospect>` | Research + write personalized outreach variants |
| **Sequence** | `/gtm-sequence <segment>` | Multi-touch outreach sequence with timing and conditional branches |

## Agents

| Agent | Focus | Model |
|-------|-------|-------|
| **Researcher** | Prospect/company dossier with cited sources | sonnet |
| **Copywriter** | Outreach copy matching your voice, multiple variants | sonnet |
| **Analyst** | Pipeline analytics - conversions, velocity, segment performance | sonnet |

## How It Works

1. **Point it at your pipeline.** GTM:OS reads a `pipeline.md` file - a simple markdown table tracking your leads, stages, and next actions.

2. **Run a command.** `/gtm-today` gives you a morning brief. `/gtm-qualify AlgeNord` runs a lead through your decision filter. `/gtm-personalize Stefan` writes personalized outreach.

3. **Your data stays local.** Everything runs through your AI assistant's context. No external APIs, no databases, no SaaS.

### Pipeline File Format

GTM:OS expects a markdown file with a table like this:

```markdown
## Active Leads

| Lead | ICP | Stage | Next Action | Last Contact |
|------|-----|-------|-------------|--------------|
| **Acme Corp** | Scaling Ops | Conversation | Send proposal by Friday | 2026-03-10 |
| **Widget Inc** | Failed Pilot | Prospect | Research buying signals | 2026-03-08 |
```

The skills look for this file in order:
1. `pipeline.md` in the current directory
2. `consulting/pipeline.md` in the repo root
3. `~/projects/b3dmar-hq/consulting/pipeline.md` as fallback

### Voice Guide

Writing skills (`personalize`, `sequence`) look for a voice guide:
1. `gtm-voice.md` in the repo root
2. `content/writing-style-guide.md` in the repo root
3. Default: direct, no-hype, value-first

## CLI Reference

```bash
gtm-os install              # Install skills + agents globally
gtm-os install --list        # List available skills without installing
gtm-os install --ai codex    # Install for Codex instead of Claude
gtm-os install --clean       # Remove stale artifacts from previous versions
gtm-os uninstall             # Remove all GTM:OS artifacts
gtm-os uninstall --dry-run   # Preview what would be removed
gtm-os docs                  # Show workflow overview
gtm-os docs today            # Show docs for a specific skill
gtm-os catalog               # Export catalog as JSON
gtm-os build-plugin          # Generate Cowork plugin directory
```

## Who This Is For

- **Solo founders** running their own sales pipeline
- **Consultants** tracking leads in markdown instead of a CRM
- **Small teams** that want GTM workflows without paying for Salesforce

## Development

```bash
git clone https://github.com/b3dmar/gtm-os.git
cd gtm-os
uv sync --group dev
uv run ruff check && uv run ruff format --check && uv run mypy --strict src/
uv run pytest
```

## License

MIT
