"""Teste da CLI do GasAnalytics."""

from typer.testing import CliRunner

from gas_analytics.cli import app

runner = CliRunner()


def test_cli_info():
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "GasAnalytics" in result.stdout
