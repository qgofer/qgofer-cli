"""Console script for qgofer_cli."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("qgofer-cli")
    click.echo("=" * len("qgofer-cli"))
    click.echo("All your documents are one quick search away.")


if __name__ == "__main__":
    main()  # pragma: no cover
