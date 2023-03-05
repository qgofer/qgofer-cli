# qgofer-cli


[![pypi](https://img.shields.io/pypi/v/qgofer-cli.svg)](https://pypi.org/project/qgofer-cli/)
[![python](https://img.shields.io/pypi/pyversions/qgofer-cli.svg)](https://pypi.org/project/qgofer-cli/)
[![Build Status](https://github.com/qgofer/qgofer-cli/actions/workflows/dev.yml/badge.svg)](https://github.com/qgofer/qgofer-cli/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/qgofer/qgofer-cli/branch/main/graphs/badge.svg)](https://codecov.io/github/qgofer/qgofer-cli)



All your documents are one quick search away.


* Documentation: <https://qgofer.github.io/qgofer-cli>
* GitHub: <https://github.com/qgofer/qgofer-cli>
* PyPI: <https://pypi.org/project/qgofer/>
* Free software: MIT

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `hello`: About qgofer.
* `wake-up`: Initialize qgofer.

## `hello`

About qgofer.

**Usage**:

```console
$ hello [OPTIONS]
```

**Options**:

* `-v, --what-version`: Show the current version of qgofer that has been installed.
* `--help`: Show this message and exit.

## `wake-up`

Initialize qgofer.

**Usage**:

```console
$ wake-up [OPTIONS]
```

**Options**:

* `-d, --home-dir TEXT`: The user home directory to use for qgofer.
* `-r, --root-dir TEXT`: The root directory to start searching from.
* `--help`: Show this message and exit.

## Features

## TODO

## Branching:

*branch early, and branch often*

[Git branching rules:](https://gist.github.com/acquayefrank/d459f5ec5fb591cd8664bdcfb8cec108)

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
