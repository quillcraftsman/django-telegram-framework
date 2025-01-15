# pygenesis-django

Python Django package repository template

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/libresource/pygenesis-django/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/libresource/pygenesis-django/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/libresource/pygenesis-django/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/libresource/pygenesis-django/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/pygenesis-django.svg)](https://pypi.python.org/pypi/pygenesis-django/)
[![Development Status](https://img.shields.io/pypi/status/pygenesis-django.svg)](https://pypi.python.org/pypi/pygenesis-django)
[![Python version](https://img.shields.io/pypi/pyversions/pygenesis-django.svg)](https://pypi.python.org/pypi/pygenesis-django/)
[![License](https://img.shields.io/pypi/l/pygenesis-django)](https://github.com/libresource/pygenesis-djangoblob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/pygenesis-django.svg)](https://pypi.python.org/pypi/pygenesis-django/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/libresource/pygenesis-django/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/libresource/pygenesis-django/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/pygenesis-django)](https://pepy.tech/project/pygenesis-django)
[![Week Downloads](https://img.shields.io/pypi/dw/pygenesis-django)](https://pepy.tech/project/pygenesis-django)
[![Month Downloads](https://img.shields.io/pypi/dm/pygenesis-django)](https://pepy.tech/project/pygenesis-django)
[![All Downloads](https://img.shields.io/pepy/dt/pygenesis-django)](https://pepy.tech/project/pygenesis-django)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/libresource/pygenesis-django)](https://github.com/libresource/pygenesis-django)
[![Top Language](https://img.shields.io/github/languages/top/libresource/pygenesis-django)](https://github.com/libresource/pygenesis-django)

#### Development
- [![Release date](https://img.shields.io/github/release-date/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/releases)
[![Last Commit](https://img.shields.io/github/last-commit/libresource/pygenesis-django/main
)](https://github.com/libresource/pygenesis-django)
- [![Issues](https://img.shields.io/github/issues/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/pulls)
- [![Discussions](https://img.shields.io/github/discussions/libresource/pygenesis-django
)](https://github.com/libresource/pygenesis-django/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/libresource/pygenesis-django)

[//]: # (&#41;]&#40;https://github.com/libresource/pygenesis-django&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/libresource/pygenesis-django)

[//]: # (&#41;]&#40;https://github.com/libresource/pygenesis-djangographs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/libresource/pygenesis-django)

[//]: # (&#41;]&#40;https://github.com/libresource/pygenesis-django&#41;)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

pygenesis-django is a comprehensive Python Django package template designed to kickstart your projects instantly. 
With a clean and organized structure, it provides a hassle-free starting point for developers. 
Effortlessly begin your Python endeavors, focusing on your code, not the setup. Jumpstart your creativity with pygenesis-django.

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

- This README (Change it for your python project)
- This template base on [libresource/pygenesis](https://github.com/libresource/pygenesis). 
It contains may useful files for open source project: ([CHECKLIST.md](CHECKLIST.md), [CONTRIBUTING.md](CONTRIBUTING.md), 
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and much more). 
- `setup.py` for build your package
- `requirements.txt` and `dev-requirements.txt`
- `Makefile` with main commands to work with the project
  - run tests
  - calculate coverage
  - lint
  - build and install package
  - generate autodocumentation
  - others
- GitHub workflows 
  - generate documentation
  - run tests with coverage
  - run linter
  - publish your package in PyPi

## Requirements

- django, pylint, yamllint, sphinx, sphinx_rtd_theme
- See more in [Full Documentation](https://pygenesis-django.libresource.info/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/pygenesis-django/)
- See more in [Full Documentation](https://pygenesis-django.libresource.info/about.html#development-status)

## Install

### with pip

```commandline
pip install pygenesis-django
```

See more in [Full Documentation](https://pygenesis-django.libresource.info/install.html)

## Quickstart

Add package to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...,
    'pygenesis_django',
]
```

Run tests

```commandline
python manage.py test
```

Run info command

```commandline
python manage.py pygenesis_django_info
```

### More examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://pygenesis-django.libresource.info/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://pygenesis-django.libresource.info