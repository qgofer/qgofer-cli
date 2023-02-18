"""Console script for qgofer_cli."""

from typing import Optional

import typer

from qgofer_cli import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="All your documents are one quick search away.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    """Main entrypoint."""
    typer.echo("qgofer-cli")
    typer.echo("=" * len("qgofer-cli"))
    typer.echo("All your documents are one quick search away.")
    return None
