#!/usr/bin/env python
"""Tests for `qgofer` package."""


from typer.testing import CliRunner

from qgofer import __app_name__, __version__, cli


def test_version():
    """Test the version."""
    runner = CliRunner()
    result = runner.invoke(cli.app, ["hello", "--what-version"])
    assert result.exit_code == 0
    assert f"{__app_name__}: v{__version__}\n" in result.output
