"""Console script for qgofer_cli."""

from typing import Optional

import typer

from qgofer import __app_name__, __description__, __version__

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
        help=f"{__description__}",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    """Main entrypoint."""
    name_version = f"{__app_name__} v{__version__}"
    typer.echo(name_version)
    typer.echo("=" * len(name_version))
    typer.echo(f"{__description__}")
    return None
