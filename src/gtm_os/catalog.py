"""Canonical catalog for GTM:OS skills and agents."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SkillSpec:
    """Machine-readable definition for an installable skill."""

    slug: str
    command: str
    description: str
    category: str
    providers: tuple[str, ...]
    triggers: tuple[str, ...] = ()
    requires_tools: tuple[str, ...] = ()
    requires_mcp: tuple[str, ...] = ()
    requires_env: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"

    def requirements_summary(self) -> str:
        parts = [
            *(f"tools:{tool}" for tool in self.requires_tools),
            *(f"mcp:{mcp}" for mcp in self.requires_mcp),
            *(f"env:{env}" for env in self.requires_env),
        ]
        return ", ".join(parts) if parts else "-"

    def manifest_entry(self) -> dict[str, object]:
        return {
            "name": self.slug,
            "filename": self.filename,
            "command": self.command,
            "description": self.description,
            "category": self.category,
            "providers": list(self.providers),
            "triggers": list(self.triggers),
            "requires_tools": list(self.requires_tools),
            "requires_mcp": list(self.requires_mcp),
            "requires_env": list(self.requires_env),
            "tags": list(self.tags),
        }


@dataclass(frozen=True)
class AgentSpec:
    """Machine-readable definition for an installable agent."""

    slug: str
    name: str
    description: str
    providers: tuple[str, ...] = ("claude", "codex")
    focus: tuple[str, ...] = ()

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"

    def manifest_entry(self) -> dict[str, object]:
        return {
            "name": self.slug,
            "filename": self.filename,
            "role": self.name,
            "description": self.description,
            "providers": list(self.providers),
            "focus": list(self.focus),
        }


SKILL_SPECS: tuple[SkillSpec, ...] = (
    SkillSpec(
        slug="today",
        command="/gtm-today",
        description="Morning brief — overdue follow-ups, due today, pipeline snapshot, priorities",
        category="Daily Ops",
        providers=("claude", "codex"),
        triggers=("morning", "daily brief", "what's due", "pipeline status"),
        tags=("daily", "pipeline"),
    ),
    SkillSpec(
        slug="pipeline",
        command="/gtm-pipeline",
        description="Pipeline hygiene — stale leads, missing actions, stage transitions, metrics",
        category="Daily Ops",
        providers=("claude", "codex"),
        triggers=("pipeline", "hygiene", "stale leads", "metrics"),
        tags=("daily", "pipeline", "hygiene"),
    ),
    SkillSpec(
        slug="qualify",
        command="/gtm-qualify",
        description="Run 6-question decision filter against a lead",
        category="Strategy",
        providers=("claude", "codex"),
        triggers=("qualify", "decision filter", "evaluate lead"),
        tags=("strategy", "qualification"),
    ),
    SkillSpec(
        slug="deep-dive",
        command="/gtm-deep-dive",
        description="ICP analysis from real pipeline data — distribution, gaps, refinements",
        category="Strategy",
        providers=("claude", "codex"),
        triggers=("ICP analysis", "deep dive", "pipeline analysis"),
        tags=("strategy", "analysis"),
    ),
    SkillSpec(
        slug="signals",
        command="/gtm-signals",
        description="Buying signal research — job postings, funding, hiring, news",
        category="Research",
        providers=("claude", "codex"),
        triggers=("signals", "buying signals", "research prospect"),
        requires_tools=("web",),
        tags=("research", "signals"),
    ),
    SkillSpec(
        slug="prep",
        command="/gtm-prep",
        description="Meeting prep — attendee profiles, company context, talking points, objection prep",
        category="Research",
        providers=("claude", "codex"),
        triggers=("prep", "meeting prep", "prepare for meeting"),
        requires_tools=("web",),
        tags=("research", "meetings"),
    ),
    SkillSpec(
        slug="personalize",
        command="/gtm-personalize",
        description="Research + write personalized outreach — LinkedIn msg, email, follow-up variants",
        category="Outreach",
        providers=("claude", "codex"),
        triggers=("personalize", "outreach", "write message"),
        requires_tools=("web",),
        tags=("outreach", "writing"),
    ),
    SkillSpec(
        slug="sequence",
        command="/gtm-sequence",
        description="Multi-touch outreach sequence with timing, channels, conditional branches",
        category="Outreach",
        providers=("claude", "codex"),
        triggers=("sequence", "cadence", "multi-touch"),
        tags=("outreach", "sequences"),
    ),
)

AGENT_SPECS: tuple[AgentSpec, ...] = (
    AgentSpec(
        "researcher",
        "Researcher",
        "Prospect/company dossier with cited sources",
        focus=("research", "sourcing"),
    ),
    AgentSpec(
        "copywriter",
        "Copywriter",
        "Outreach copy matching user voice, multiple variants",
        focus=("writing", "outreach"),
    ),
    AgentSpec(
        "analyst",
        "Analyst",
        "Pipeline analytics — conversions, velocity, segment performance",
        focus=("analytics", "pipeline"),
    ),
)

SKILL_SPECS_BY_FILENAME: dict[str, SkillSpec] = {spec.filename: spec for spec in SKILL_SPECS}


def build_manifest() -> dict[str, object]:
    """Build a machine-readable project manifest."""

    categories: dict[str, list[str]] = {}
    for spec in SKILL_SPECS:
        categories.setdefault(spec.category, []).append(spec.filename)

    return {
        "version": "0.1.0",
        "name": "gtm-os",
        "description": "GTM workflow skills and agents for Claude Code, Codex, and Cowork",
        "repository": "https://github.com/b3dmar/gtm-os",
        "skills": [spec.manifest_entry() for spec in SKILL_SPECS],
        "agents": [spec.manifest_entry() for spec in AGENT_SPECS],
        "categories": categories,
    }
