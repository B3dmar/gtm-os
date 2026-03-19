"""Provider registry for assistant-specific integrations."""

from gtm_os.providers.base import Provider
from gtm_os.providers.claude import ClaudeProvider
from gtm_os.providers.codex import CodexProvider
from gtm_os.providers.cowork import CoworkProvider

_PROVIDERS: dict[str, Provider] = {
    "claude": ClaudeProvider(),
    "codex": CodexProvider(),
    "cowork": CoworkProvider(),
}


def supported_providers() -> tuple[str, ...]:
    """Return currently registered provider names."""
    return tuple(sorted(_PROVIDERS))


def get_provider(name: str = "claude") -> Provider:
    """Resolve provider by name."""
    try:
        return _PROVIDERS[name]
    except KeyError as exc:
        supported = ", ".join(sorted(_PROVIDERS))
        raise ValueError(
            f"Unsupported provider '{name}'. Supported providers: {supported}"
        ) from exc


__all__ = ["get_provider", "supported_providers"]
