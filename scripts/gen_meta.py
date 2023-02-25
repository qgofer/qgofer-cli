"""generate projects metadata from pyproject.toml."""


def qgofer_version():
    """Get version from pyproject.toml."""
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('version'):
                return line.split('=')[1].strip().strip('"')


def qgofer_name():
    """Get name from pyproject.toml."""
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('name'):
                return line.split('=')[1].strip().strip('"')


def qgofer_description():
    """Get description from pyproject.toml."""
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('description'):
                return line.split('=')[1].strip().strip('"')


def generate_metadata():
    """Generate metadata."""
    version = qgofer_version()
    name = qgofer_name()
    description = qgofer_description()
    with (open('./qgofer/__init__.py', 'w')) as f:
        f.write('"""Top-level package for qgofer."""\n\n')
        f.write('__author__ = "acquayefrank"\n')
        f.write("__email__ = 'dev@qgofer.com'\n")
        f.write(f"__version__ = '{version}'\n")
        f.write("__license__ = 'MIT'\n")
        f.write(f"__app_name__ = '{name}'\n")
        f.write(f"__description__ = '{description}'\n")


if __name__ == "__main__":
    generate_metadata()
