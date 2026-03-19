"""gtm-os docs command - show overview or skill documentation."""

from __future__ import annotations

import logging

from rich.console import Console
from rich.markdown import Markdown

from gtm_os.catalog import SKILL_SPECS
from gtm_os.utils.files import safe_read_text
from gtm_os.utils.paths import get_template_path

logger = logging.getLogger(__name__)


def run_docs(skill: str | None, console: Console) -> None:
    """Show documentation for GTM:OS or a specific skill."""

    if skill:
        _show_skill_docs(skill, console)
    else:
        _show_overview(console)


def _show_overview(console: Console) -> None:
    """Show dynamic overview documentation derived from the catalog."""

    category_rows: list[str] = []
    categories: dict[str, list[tuple[str, str]]] = {}
    for spec in SKILL_SPECS:
        categories.setdefault(spec.category, []).append((spec.command, spec.description))

    for category, rows in categories.items():
        category_rows.append(f"## {category}\n")
        category_rows.append("| Command | Purpose |")
        category_rows.append("|---------|---------|")
        for command, description in rows:
            category_rows.append(f"| `{command}` | {description} |")
        category_rows.append("")

    overview = "\n".join(
        [
            "# GTM:OS Workflow",
            "",
            "## CLI Commands",
            "",
            "| Command | Purpose |",
            "|---------|---------|",
            "| `gtm-os install` | Install global skills and agents for selected provider |",
            "| `gtm-os uninstall` | Remove global skills and agents |",
            "| `gtm-os docs` | Show workflow and skill documentation |",
            "| `gtm-os catalog` | Export the machine-readable skill/agent catalog as JSON |",
            "",
            f"## Skills ({len(SKILL_SPECS)})",
            "",
            *category_rows,
            "## Workflow",
            "",
            "1. **Daily ops** - `/gtm-today` and `/gtm-pipeline` for daily rhythm",
            "2. **Research** - `/gtm-signals` and `/gtm-prep` for prospect intelligence",
            "3. **Qualify** - `/gtm-qualify` to run the decision filter",
            "4. **Outreach** - `/gtm-personalize` and `/gtm-sequence` for messaging",
            "",
            "Run `gtm-os docs [skill]` for detailed skill documentation.",
        ]
    )
    console.print(Markdown(overview))


def _normalize_skill_slug(skill: str) -> str:
    normalized = skill.strip().lower()
    normalized = normalized.lstrip("/")
    if normalized.startswith("gtm-"):
        normalized = normalized.removeprefix("gtm-")
    return normalized


def _show_skill_docs(skill: str, console: Console) -> None:
    """Show documentation for a specific skill."""

    normalized_skill = _normalize_skill_slug(skill)
    skill_file = get_template_path("skills") / f"{normalized_skill}.md"

    if not skill_file.exists():
        console.print(f"[red]Unknown skill: {normalized_skill}[/red]")
        console.print("Run [cyan]gtm-os docs[/cyan] to see available skills.")
        return

    content = safe_read_text(skill_file)
    console.print(Markdown(content))
