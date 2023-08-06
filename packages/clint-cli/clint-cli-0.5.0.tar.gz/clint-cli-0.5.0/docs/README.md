<p align="center">
    English - <a href="README.es.md">Español</a>
</p>

# CLint: Conventional commits linter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`CLint` is a command line tool that allows you to validate messages related to git commits in different ways, ensuring
that the message is [Conventional Commits compliant](https://www.conventionalcommits.org/en/v1.0.0/#specification).

## Technologies

- [python](https://www.python.org/), for its awesomeness. Supported versions: 3.7.2+
- [poetry](https://python-poetry.org/), for packaging and dependency management
- [change](https://github.com/adamtabrams/change), to help generate the changelog

## Installation

For now, the only way to install `CLint` is through `pip` (or tools like `poetry` and `pipenv`, which use `pip` behind
the scenes), but we are working on making `CLint` available through package managers, like `homebrew`, `chocolatey` and
others.

```sh
# Install with pip
$ pip install clint-cli

# Install with poetry
$ poetry add clint-cli

# Install with pipenv
$ pipenv install clint-cli
```

## Key features

- Validate a commit message in the command line.
- Allow to handle git `commit-msg` hook.
- Validate a commit message in the command line through pipes.

## Planned features

- Make [pre-commit](https://pre-commit.com/) compatible.
- Allow to build a commit message through command line prompts.

## Usage examples

```sh
# Validate a sample message
$ clint "feat(scope): validate this message"
Your commit message is CC compliant!
```

```sh
# Validate from file
$ echo "feat(scope): validate this message" > commit_message.txt
$ clint --file commit_message.txt
Your commit message is CC compliant!
```

```sh
# Validate through pipes
$ cat commit_message.txt | clint
Your commit message is CC compliant!
```

```sh
# Validation error for invalid type (typo)
$ echo "feta(scope): validate this message" | clint
type_valid: Type 'feta' is not valid.
```

```sh
# Enable git hook on /path/to/repo
$ clint --enable-hook
Enable hook: Hook enabled at /path/to/repo/.git/hooks/commit-msg
```

```sh
# Disable git hook on /path/to/repo
$ clint --disable-hook
Disable hook: Hook disabled at /path/to/repo/.git/hooks/commit-msg
```

## Changelog

You can view the history of changes in the project [changelog](../CHANGELOG.md).

## Project status

`CLint` is currently in **beta** status, and is under active development. The goal is to achieve at least
the [planned features](#planned-features), and then continue maintaining the code, making it compatible with future
versions of Python and the libraries used in the project.

## Source

`CLint` tries to be what other tools already are, like the
great [commitlint](https://github.com/conventional-changelog/commitlint). The difference
with [similar tools](https://www.conventionalcommits.org/en/about/#tooling-for-conventional-commits) is that those are
built over `Node.js`, so they are focused on `Javascript` developers. If you are not, you will be forced to
install `Node.js` anyway in order to use those tools.

## License

`CLint` is distributed under the [GPL v3 license](../COPYING).
