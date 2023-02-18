"""Top-level package for qgofer."""


def qgofer_version():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('version'):
                return line.split('=')[1].strip().strip('"')


def qgofer_name():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('name'):
                return line.split('=')[1].strip().strip('"')


def qgofer_description():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('description'):
                return line.split('=')[1].strip().strip('"')


__author__ = """acquayefrank"""
__email__ = 'dev@qgofer.com'
__version__ = qgofer_version()
__license__ = 'MIT'
__app_name__ = qgofer_name()
__description__ = qgofer_description()
