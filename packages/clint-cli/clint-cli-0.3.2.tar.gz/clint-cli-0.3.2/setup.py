# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clint', 'clint.cli', 'clint.validator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['clint = clint.cli:Command.entrypoint']}

setup_kwargs = {
    'name': 'clint-cli',
    'version': '0.3.2',
    'description': 'Conventional Commits Linter',
    'long_description': '<p align="center">\n    English - <a href="README.es.md">Español</a>\n</p>\n\n# CLint: Conventional commits linter\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n`CLint` is a command line tool that allows you to validate messages related to git commits in different ways, ensuring\nthat the message is [Conventional Commits compliant](https://www.conventionalcommits.org/en/v1.0.0/#specification).\n\n## Technologies\n\n- [Python](https://www.python.org/) 3.7.2+\n- [Poetry](https://python-poetry.org/)\n\n## Installation\n\nFor now, the only way to install `CLint` is through `pip` (or tools like `poetry` and `pipenv`, which use `pip` behind\nthe scenes), but we are working on making `CLint` available through package managers, like `homebrew`, `chocolatey` and\nothers.\n\n```sh\n# Install with pip\n$ pip install clint-cli\n\n# Install with poetry\n$ poetry add clint-cli\n\n# Install with pipenv\n$ pipenv install clint-cli\n```\n\n## Key features\n\n- Validate a commit message in the command line.\n- Allow to handle git `commit-msg` hook.\n\n## Planned features\n\n- Validate a commit message in the command line through pipes.\n- Make [pre-commit](https://pre-commit.com/) compatible.\n- Allow to build a commit message through command line prompts.\n\n## Usage examples\n\n```sh\n# Validate a sample message\n$ clint "feat(scope): validate this message"\nYour commit message is CC compliant!\n```\n\n```sh\n# Validation error for invalid type (typo)\n$ clint "feta(scope): validate this message"\nValidation error: Type \'feta\' is not valid.\n```\n\n```sh\n# Enable git hook on /path/to/repo\n$ clint --enable-hook\nEnable hook: Hook enabled at /path/to/repo/.git/hooks/commit-msg\n```\n\n```sh\n# Disable git hook on /path/to/repo\n$ clint --disable-hook\nDisable hook: Hook disabled at /path/to/repo/.git/hooks/commit-msg\n```\n\n## Project status\n\n`CLint` is currently under active development. The goal is to achieve at least the [planned features](#planned-features)\n, and then continue maintaining the code, making it compatible with future versions of Python and the libraries used in\nthe project.\n\n## Source\n\n`CLint` tries to be what other tools already are, like the\ngreat [commitlint](https://github.com/conventional-changelog/commitlint). The difference\nwith [similar tools](https://www.conventionalcommits.org/en/about/#tooling-for-conventional-commits) is that those are\nbuilt over `Node.js`, so they are focused on `Javascript` developers. If you are not, you will be forced to\ninstall `Node.js` anyway in order to use those tools.\n\n## License\n\n`CLint` is distributed under the [GPL v3 license](../COPYING).\n',
    'author': 'Ricardo Cisterna',
    'author_email': 'r.cisternasantos@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rcisterna/clint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
