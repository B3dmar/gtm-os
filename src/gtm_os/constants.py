"""Constants derived from the canonical catalog."""

from gtm_os.catalog import (
    AGENT_SPECS,
    SKILL_SPECS,
)

SKILL_PREFIX = "gtm-"

SKILLS = [spec.filename for spec in SKILL_SPECS]
AGENTS = [spec.filename for spec in AGENT_SPECS]

skill_info: dict[str, tuple[str, str]] = {
    spec.filename: (spec.command, spec.description) for spec in SKILL_SPECS
}

SKILL_CATEGORIES: dict[str, list[str]] = {}
for spec in SKILL_SPECS:
    SKILL_CATEGORIES.setdefault(spec.category, []).append(spec.filename)

COWORK_SKILLS: list[str] = []
COWORK_AGENTS: list[str] = []

agent_info: dict[str, tuple[str, str]] = {
    spec.filename: (spec.name, spec.description) for spec in AGENT_SPECS
}
