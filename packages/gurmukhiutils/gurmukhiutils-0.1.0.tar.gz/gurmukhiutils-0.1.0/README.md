# Gurmukhi Utils (Python)

Python utilities library for converting, analyzing, and testing Gurmukhi strings. This project is an original work inspired by the JavaScript library [`gurmukhi-utils`](https://github.com/shabados/gurmukhi-utils).

## WIP

This library is a work in progress! Note that the API can change unexpectedly when upgrading. It will not be using [SemVer](https://semver.org/) until version 1.0.0. Please do not use for critical projects yet.

## Contributing

Requirements:

- [Python](https://www.python.org/) (see version in `pyproject.toml`)
- [Poetry](https://python-poetry.org/)

Workflow:

- Fork this repository
- Create a branch from `main`
- Make any changes
- Submit a pull request

Note: Before creating new branches, ensuring that the forked `main` is up to date with the upstream/original `main` will ease workflow.

Development:

- Install project dependencies with `poetry install`.
- Automatically format/lint when committing by enabling pre-commit hooks with `poetry run pre-commit install`.
- Run tests with `poetry run pytest`.

Note: Select the Python Interpreter in VS Code to access dev dependencies.

Note: The optional extensions in VS Code may help you.

Note: If you don't enable the pre-commit hooks, please manually run the related commands in `.pre-commit-config.yaml` before submitting each and every PR.

## Maintaining

**Merging**

- Pull requests should be squashed or rebased.
- Commit messages should generally conform to [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).
  - Valid _types_ include: `BREAK`, `feat`, `fix`, `nv`, which correlate with MAJOR, MINOR, PATCH, and no variation in [Semantic Versioning](https://semver.org/).

Note: It is possible to run pytest on any branch using the Actions tab.

## Todo

Beyond the obvious implementation of features from the original `gurmukhi-utils` program:

- GitHub workflows for pytest and making sure flake8/isort/black are passing on PR
- Publishing on PyPi
- Adding installation/usage docs for end-user
- Possibly consider exporting a requirements.txt via poetry for pip using contributors (not needed for end-users).

## Community

The easiest way to communicate is via [GitHub issues](https://github.com/shabados/viewer/issues). Please search for similar issues regarding your concerns before opening a new issue.

Get organization updates for Shabad OS by following us on [Instagram](https://www.instagram.com/shabad_os/) and [Twitter](https://twitter.com/shabad_os/). We also invite you to join us on our public chat server hosted on [Slack](https://chat.shabados.com/).

Our intention is to signal a safe open-source community. Please help us foster an atmosphere of kindness, cooperation, and understanding. By participating, you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

If you have a concern that doesn't warrant opening a GitHub issue, please reach out to us:

Bhajneet S.K., Author, Maintainer, Project Lead: [@bhajneet](https://github.com/bhajneet/)
