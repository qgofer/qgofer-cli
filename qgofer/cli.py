"""Console script for qgofer_cli."""

import os
from pathlib import Path
from typing import Optional

import typer

from qgofer import __app_name__, __description__, __version__
from qgofer.q import Q

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}: v{__version__}\n")
        raise typer.Exit()
    return None


def init_path(path: Path) -> Path:
    """Convert the string to a path object."""
    if path is None:
        return Path.home()
    return Path(path).expanduser().resolve()


@app.command("wake-up")
def init(
    home_dir: Optional[Path] = typer.Option(
        None,
        "--home-dir",
        "-d",
        help="The user home directory to use for qgofer.",
        callback=init_path,
    )
) -> None:
    """Initialize qgofer."""
    typer.echo("Initializing qgofer...")
    if home_dir is not None:
        _ = Q(home_dir)
    else:
        _ = Q()
    return None


@app.command("hello")
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--what-version",
        "-v",
        help="Show the current version of qgofer that has been installed.",
        callback=version_callback,
        is_eager=True,
    )
) -> None:
    """About qgofer."""
    try:
        username = os.getlogin()
    except FileNotFoundError:
        username = "You"
    typer.echo(f"Hello {username}, I am Q, your assistant.\n")
    typer.echo(f"My model version is '{__version__}'\n")
    description = __description__.lower()
    typer.echo(f"With my help, {description}.\n")
    return None
