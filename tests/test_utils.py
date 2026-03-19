"""Tests for utility modules."""

import pytest

from gtm_os.exceptions import PathTraversalError
from gtm_os.utils.frontmatter import split_frontmatter
from gtm_os.utils.paths import get_package_root, get_template_path, sanitize_slug


def test_split_frontmatter():
    content = "---\ntitle: Test\n---\n\nBody text"
    meta, body = split_frontmatter(content)
    assert meta["title"] == "Test"
    assert "Body text" in body


def test_split_frontmatter_no_frontmatter():
    content = "Just body text"
    meta, body = split_frontmatter(content)
    assert meta == {}
    assert body == content


def test_sanitize_slug_valid():
    assert sanitize_slug("today") == "today"
    assert sanitize_slug("deep-dive") == "deep-dive"


def test_sanitize_slug_traversal():
    with pytest.raises(PathTraversalError):
        sanitize_slug("../etc/passwd")

    with pytest.raises(PathTraversalError):
        sanitize_slug("foo/bar")


def test_get_package_root():
    root = get_package_root()
    assert (root / "__init__.py").exists()


def test_get_template_path():
    skills_path = get_template_path("skills")
    assert skills_path.name == "skills"
    assert skills_path.exists()
