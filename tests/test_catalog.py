"""Tests for the GTM:OS catalog."""

from gtm_os.catalog import AGENT_SPECS, SKILL_SPECS, SKILL_SPECS_BY_FILENAME, build_manifest


def test_skill_specs_not_empty():
    assert len(SKILL_SPECS) == 8


def test_agent_specs_not_empty():
    assert len(AGENT_SPECS) == 3


def test_skill_slugs_unique():
    slugs = [s.slug for s in SKILL_SPECS]
    assert len(slugs) == len(set(slugs))


def test_agent_slugs_unique():
    slugs = [a.slug for a in AGENT_SPECS]
    assert len(slugs) == len(set(slugs))


def test_skill_commands_start_with_prefix():
    for spec in SKILL_SPECS:
        assert spec.command.startswith("/gtm-"), f"{spec.slug} command missing /gtm- prefix"


def test_skill_filenames():
    for spec in SKILL_SPECS:
        assert spec.filename == f"{spec.slug}.md"


def test_agent_filenames():
    for spec in AGENT_SPECS:
        assert spec.filename == f"{spec.slug}.md"


def test_skill_specs_by_filename():
    assert len(SKILL_SPECS_BY_FILENAME) == len(SKILL_SPECS)
    for spec in SKILL_SPECS:
        assert SKILL_SPECS_BY_FILENAME[spec.filename] is spec


def test_build_manifest():
    manifest = build_manifest()
    assert manifest["name"] == "gtm-os"
    assert len(manifest["skills"]) == 8  # type: ignore[arg-type]
    assert len(manifest["agents"]) == 3  # type: ignore[arg-type]
    assert "categories" in manifest


def test_skill_manifest_entry():
    spec = SKILL_SPECS[0]
    entry = spec.manifest_entry()
    assert entry["name"] == spec.slug
    assert entry["command"] == spec.command
    assert entry["description"] == spec.description


def test_agent_manifest_entry():
    spec = AGENT_SPECS[0]
    entry = spec.manifest_entry()
    assert entry["name"] == spec.slug
    assert entry["role"] == spec.name
    assert entry["description"] == spec.description


def test_requirements_summary_empty():
    spec = SKILL_SPECS[0]  # today - no requirements
    assert spec.requirements_summary() == "-"


def test_requirements_summary_with_tools():
    spec = next(s for s in SKILL_SPECS if s.requires_tools)
    summary = spec.requirements_summary()
    assert "tools:" in summary
