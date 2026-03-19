"""Tests for the GTM:OS CLI."""

from click.testing import CliRunner

from gtm_os.cli import main


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "GTM:OS" in result.output


def test_install_help():
    runner = CliRunner()
    result = runner.invoke(main, ["install", "--help"])
    assert result.exit_code == 0
    assert "--list" in result.output
    assert "--ai" in result.output


def test_uninstall_help():
    runner = CliRunner()
    result = runner.invoke(main, ["uninstall", "--help"])
    assert result.exit_code == 0
    assert "--dry-run" in result.output


def test_docs_help():
    runner = CliRunner()
    result = runner.invoke(main, ["docs", "--help"])
    assert result.exit_code == 0


def test_catalog_help():
    runner = CliRunner()
    result = runner.invoke(main, ["catalog", "--help"])
    assert result.exit_code == 0


def test_install_list():
    runner = CliRunner()
    result = runner.invoke(main, ["install", "--list"])
    assert result.exit_code == 0
    assert "today" in result.output.lower()
    assert "pipeline" in result.output.lower()


def test_docs_overview():
    runner = CliRunner()
    result = runner.invoke(main, ["docs"])
    assert result.exit_code == 0


def test_catalog_json():
    runner = CliRunner()
    result = runner.invoke(main, ["catalog"])
    assert result.exit_code == 0
    assert '"gtm-os"' in result.output
