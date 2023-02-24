"""Console script for qgofer_cli."""

import os
from typing import Optional

import typer

from qgofer import __app_name__, __description__, __version__

from .app import App, create_index_list, process_index_list
from .utils import init_path

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Show the current version of qgofer that has been installed."""
    if value:
        typer.echo(f"{__app_name__}: v{__version__}\n")
        raise typer.Exit()
    return None


@app.command("wake-up")
def init(
    home_dir=typer.Option(
        None,
        "--home-dir",
        "-d",
        help="The user home directory to use for qgofer.",
        callback=init_path,
    ),
    root_dir=typer.Option(
        None, "--root-dir", "-r", help="The root directory to start searching from.", callback=init_path
    ),
) -> None:
    """Initialize qgofer."""
    typer.echo("Initializing qgofer...")
    qgofer_app = App(home_dir, root_dir)
    qgofer_app = create_index_list(qgofer_app)
    qgofer_app = process_index_list(qgofer_app)
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
