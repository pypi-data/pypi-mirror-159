# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gurmukhiutils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gurmukhiutils',
    'version': '0.1.0',
    'description': 'Python utilities library for converting, analyzing, and testing Gurmukhi strings',
    'long_description': "# Gurmukhi Utils (Python)\n\nPython utilities library for converting, analyzing, and testing Gurmukhi strings. This project is an original work inspired by the JavaScript library [`gurmukhi-utils`](https://github.com/shabados/gurmukhi-utils).\n\n## WIP\n\nThis library is a work in progress! Note that the API can change unexpectedly when upgrading. It will not be using [SemVer](https://semver.org/) until version 1.0.0. Please do not use for critical projects yet.\n\n## Contributing\n\nRequirements:\n\n- [Python](https://www.python.org/) (see version in `pyproject.toml`)\n- [Poetry](https://python-poetry.org/)\n\nWorkflow:\n\n- Fork this repository\n- Create a branch from `main`\n- Make any changes\n- Submit a pull request\n\nNote: Before creating new branches, ensuring that the forked `main` is up to date with the upstream/original `main` will ease workflow.\n\nDevelopment:\n\n- Install project dependencies with `poetry install`.\n- Automatically format/lint when committing by enabling pre-commit hooks with `poetry run pre-commit install`.\n- Run tests with `poetry run pytest`.\n\nNote: Select the Python Interpreter in VS Code to access dev dependencies.\n\nNote: The optional extensions in VS Code may help you.\n\nNote: If you don't enable the pre-commit hooks, please manually run the related commands in `.pre-commit-config.yaml` before submitting each and every PR.\n\n## Maintaining\n\n**Merging**\n\n- Pull requests should be squashed or rebased.\n- Commit messages should generally conform to [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).\n  - Valid _types_ include: `BREAK`, `feat`, `fix`, `nv`, which correlate with MAJOR, MINOR, PATCH, and no variation in [Semantic Versioning](https://semver.org/).\n\nNote: It is possible to run pytest on any branch using the Actions tab.\n\n## Todo\n\nBeyond the obvious implementation of features from the original `gurmukhi-utils` program:\n\n- GitHub workflows for pytest and making sure flake8/isort/black are passing on PR\n- Publishing on PyPi\n- Adding installation/usage docs for end-user\n- Possibly consider exporting a requirements.txt via poetry for pip using contributors (not needed for end-users).\n\n## Community\n\nThe easiest way to communicate is via [GitHub issues](https://github.com/shabados/viewer/issues). Please search for similar issues regarding your concerns before opening a new issue.\n\nGet organization updates for Shabad OS by following us on [Instagram](https://www.instagram.com/shabad_os/) and [Twitter](https://twitter.com/shabad_os/). We also invite you to join us on our public chat server hosted on [Slack](https://chat.shabados.com/).\n\nOur intention is to signal a safe open-source community. Please help us foster an atmosphere of kindness, cooperation, and understanding. By participating, you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).\n\nIf you have a concern that doesn't warrant opening a GitHub issue, please reach out to us:\n\nBhajneet S.K., Author, Maintainer, Project Lead: [@bhajneet](https://github.com/bhajneet/)\n",
    'author': 'Bhajneet S.K.',
    'author_email': 'bhajneet@gmail.com',
    'maintainer': 'Bhajneet S.K.',
    'maintainer_email': 'bhajneet@gmail.com',
    'url': 'https://github.com/shabados/gurmukhiutils',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
