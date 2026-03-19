"""Tests for GTM:OS constants."""

from gtm_os.constants import AGENTS, SKILL_CATEGORIES, SKILLS, agent_info, skill_info


def test_skills_list():
    assert len(SKILLS) == 8
    assert all(s.endswith(".md") for s in SKILLS)


def test_agents_list():
    assert len(AGENTS) == 3
    assert all(a.endswith(".md") for a in AGENTS)


def test_skill_info_complete():
    for skill in SKILLS:
        assert skill in skill_info
        cmd, desc = skill_info[skill]
        assert cmd.startswith("/gtm-")
        assert len(desc) > 0


def test_agent_info_complete():
    for agent in AGENTS:
        assert agent in agent_info
        name, desc = agent_info[agent]
        assert len(name) > 0
        assert len(desc) > 0


def test_skill_categories():
    all_skills_in_categories = []
    for skills in SKILL_CATEGORIES.values():
        all_skills_in_categories.extend(skills)
    assert set(all_skills_in_categories) == set(SKILLS)
