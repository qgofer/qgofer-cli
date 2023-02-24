"""qgofer - A command line tool for searching your files."""
from qgofer import __app_name__, cli


def main():
    """Run the qgofer cli."""
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
