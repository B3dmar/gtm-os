"""GTM:OS CLI - GTM workflow skills for Claude Code, Codex, and Cowork."""

import logging
import sys
from pathlib import Path

import click
from rich.console import Console

from gtm_os.exceptions import GtmOsError
from gtm_os.providers import supported_providers

console = Console()
AI_CHOICES = supported_providers()

logger = logging.getLogger(__name__)


class GtmOsGroup(click.Group):
    """Click group that catches GtmOsError and prints clean messages."""

    def invoke(self, ctx: click.Context) -> None:
        try:
            super().invoke(ctx)
        except GtmOsError as exc:
            console.print(f"[red]Error:[/red] {exc}")
            logger.debug("GtmOsError details", exc_info=True)
            sys.exit(1)


@click.group(cls=GtmOsGroup)
@click.version_option()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging output")
def main(verbose: bool) -> None:
    """GTM:OS: install and manage GTM workflow skills for Claude Code/Codex."""
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s %(name)s:%(lineno)d %(message)s",
        force=True,
    )


@main.command()
@click.option(
    "--list", "list_skills", is_flag=True, help="List available skills without installing"
)
@click.option(
    "--clean", is_flag=True, help="Remove stale artifacts not in current skill/agent lists"
)
@click.option(
    "--ai",
    type=click.Choice(AI_CHOICES),
    default="claude",
    show_default=True,
    help="AI assistant provider",
)
def install(list_skills: bool, clean: bool, ai: str) -> None:
    """Install GTM:OS skills globally for the selected AI provider."""
    from gtm_os.commands.install import run_install

    run_install(list_skills, console, clean=clean, ai=ai)


@main.command()
@click.option(
    "--dry-run", is_flag=True, help="Preview what would be removed without making changes"
)
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
@click.option(
    "--ai",
    type=click.Choice(AI_CHOICES),
    default="claude",
    show_default=True,
    help="AI assistant provider",
)
def uninstall(dry_run: bool, yes: bool, ai: str) -> None:
    """Remove GTM:OS artifacts from global provider config."""
    from gtm_os.commands.uninstall import run_uninstall

    run_uninstall(dry_run, yes, console, ai=ai)


@main.command()
@click.argument("skill", required=False)
def docs(skill: str | None) -> None:
    """Show documentation for GTM:OS workflow or a specific skill."""
    from gtm_os.commands.docs import run_docs

    run_docs(skill, console)


@main.command()
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=None,
    help="Write catalog JSON to a file instead of stdout",
)
def catalog(output: Path | None) -> None:
    """Export the machine-readable GTM:OS catalog as JSON."""
    from gtm_os.commands.catalog import run_catalog

    run_catalog(output, console)


@main.command("build-plugin")
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=None,
    help="Output directory (default: ./cowork-plugin)",
)
def build_plugin(output: Path | None) -> None:
    """Generate Cowork plugin directory from source templates."""
    from gtm_os.commands.build_plugin import run_build_plugin

    run_build_plugin(output, console)


if __name__ == "__main__":
    main()
