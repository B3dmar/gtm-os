"""Tests for provider implementations."""

from pathlib import Path

from gtm_os.providers import get_provider, supported_providers
from gtm_os.providers.claude import ClaudeProvider
from gtm_os.providers.codex import CodexProvider
from gtm_os.providers.cowork import CoworkProvider


def test_supported_providers():
    providers = supported_providers()
    assert "claude" in providers
    assert "codex" in providers
    assert "cowork" in providers


def test_get_provider():
    provider = get_provider("claude")
    assert isinstance(provider, ClaudeProvider)


def test_claude_skill_target():
    provider = ClaudeProvider()
    target = provider.resolve_skill_target(Path("/tmp/commands"), "today.md")
    assert target == Path("/tmp/commands/gtm-today.md")


def test_claude_agent_target():
    provider = ClaudeProvider()
    target = provider.resolve_agent_target(Path("/tmp/agents"), "researcher.md")
    assert target == Path("/tmp/agents/gtm-researcher.md")


def test_codex_skill_target():
    provider = CodexProvider()
    target = provider.resolve_skill_target(Path("/tmp/skills"), "today.md")
    assert target == Path("/tmp/skills/gtm-today/SKILL.md")


def test_codex_agent_target():
    provider = CodexProvider()
    target = provider.resolve_agent_target(Path("/tmp/agents"), "researcher.md")
    assert target == Path("/tmp/agents/gtm-researcher.toml")


def test_cowork_skill_target():
    provider = CoworkProvider()
    target = provider.resolve_skill_target(Path("/tmp/skills"), "today.md")
    assert target == Path("/tmp/skills/today/SKILL.md")


def test_cowork_agent_target():
    provider = CoworkProvider()
    target = provider.resolve_agent_target(Path("/tmp/agents"), "researcher.md")
    assert target == Path("/tmp/agents/researcher/AGENT.md")
