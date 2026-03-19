"""gtm_os — GTM workflow skills and agents for Claude Code, Codex, and Cowork."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("gtm-os")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"
