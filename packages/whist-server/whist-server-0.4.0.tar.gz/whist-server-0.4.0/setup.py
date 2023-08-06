# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['whist_server',
 'whist_server.api',
 'whist_server.api.ranking',
 'whist_server.api.room',
 'whist_server.api.user',
 'whist_server.database',
 'whist_server.services',
 'whist_server.web_socket',
 'whist_server.web_socket.events']

package_data = \
{'': ['*']}

install_requires = \
['fastapi[all]>=0.79,<0.80',
 'orjson==3.7.7',
 'passlib[bcrypt]>=1.7,<2.0',
 'pydantic>=1.9,<2.0',
 'pymongo>=4.1,<5.0',
 'python-jose[cryptography]>=3.3,<4.0',
 'whist-core>=0.3,<0.4']

entry_points = \
{'console_scripts': ['whist-server = whist_server.cli:main']}

setup_kwargs = {
    'name': 'whist-server',
    'version': '0.4.0',
    'description': 'Whist server implementation',
    'long_description': "[![codecov](https://codecov.io/gh/Whist-Team/Whist-Server/branch/main/graph/badge.svg)](https://codecov.io/gh/Whist-Team/Whist-Server)\n[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)\n![PyPI](https://img.shields.io/pypi/v/whist-server)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whist-server)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/whist-server)\n![GitHub repo size](https://img.shields.io/github/repo-size/whist-team/whist-server)\n![Lines of code](https://img.shields.io/tokei/lines/github/whist-team/whist-server)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/whist-server)\n![PyPI - License](https://img.shields.io/pypi/l/whist-server)\n\n# Whist-Server\n\nThis is the REST API server of a Whist game. It provides user management, session organization and\na convenient interface for the rules' implementation of\n[Whist-Core](https://github.com/Whist-Team/Whist-Core).\n\n## Development\n\n### Setup\nYou need [Poetry](https://python-poetry.org/) for development.\n```bash\n# Create venv and install deps\npoetry install\n```\nThe Python virtual environment will be created in the `.venv` directory.\n\n### Run tests/lint\n```bash\n# Run tests (in venv)\npython -m pytest # or pylint...\n# OR\npoetry run python -m pytest\n```\n\n### Build\nGenerates `sdist` and `bdist_wheel`.\n```bash\npoetry build\n```\n\n### Publish\nYou need the environment variable `POETRY_PYPI_TOKEN_PYPI` filled with a PyPI token.\n```bash\npoetry build\npoetry publish\n# OR\npoetry publish --build\n```\n",
    'author': 'Whist-Team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Whist-Team/Whist-Server',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
