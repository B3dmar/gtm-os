"""Tests to verify all templates exist and have valid frontmatter."""

from gtm_os.catalog import AGENT_SPECS, SKILL_SPECS
from gtm_os.utils.frontmatter import split_frontmatter
from gtm_os.utils.paths import get_template_path


def test_all_skill_templates_exist():
    template_dir = get_template_path("skills")
    for spec in SKILL_SPECS:
        path = template_dir / spec.filename
        assert path.exists(), f"Missing skill template: {spec.filename}"


def test_all_agent_templates_exist():
    template_dir = get_template_path("agents")
    for spec in AGENT_SPECS:
        path = template_dir / spec.filename
        assert path.exists(), f"Missing agent template: {spec.filename}"


def test_skill_templates_have_frontmatter():
    template_dir = get_template_path("skills")
    for spec in SKILL_SPECS:
        content = (template_dir / spec.filename).read_text()
        meta, body = split_frontmatter(content)
        assert "description" in meta, f"{spec.filename} missing description in frontmatter"
        assert len(body.strip()) > 0, f"{spec.filename} has empty body"


def test_agent_templates_have_frontmatter():
    template_dir = get_template_path("agents")
    for spec in AGENT_SPECS:
        content = (template_dir / spec.filename).read_text()
        meta, body = split_frontmatter(content)
        assert "name" in meta, f"{spec.filename} missing name in frontmatter"
        assert "description" in meta, f"{spec.filename} missing description in frontmatter"
        assert len(body.strip()) > 0, f"{spec.filename} has empty body"
