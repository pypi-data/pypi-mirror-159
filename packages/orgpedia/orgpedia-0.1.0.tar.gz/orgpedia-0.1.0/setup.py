# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orgpedia', 'tests']

package_data = \
{'': ['*']}

extras_require = \
{':extra == "doc"': ['mkdocstrings[python]>=0.19.0,<0.20.0'],
 'dev': ['tox>=3.25.1,<4.0.0',
         'bump2version>=1.0.1,<2.0.0',
         'twine>=4.0.1,<5.0.0',
         'pip>=22.1.2,<23.0.0'],
 'doc': ['mkdocs>=1.3.0,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.5.2,<4.0.0',
         'mkdocs-material>=8.3.9,<9.0.0',
         'mkdocs-autorefs>=0.4.1,<0.5.0'],
 'test': ['flake8>=3.9.2,<4.0.0',
          'black>=22.6.0,<23.0.0',
          'isort>=5.10.1,<6.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=7.1.2,<8.0.0',
          'pytest-cov>=3.0.0,<4.0.0']}

setup_kwargs = {
    'name': 'orgpedia',
    'version': '0.1.0',
    'description': 'Organization Information.',
    'long_description': '# OrgPedia\n\n\n[![pypi](https://img.shields.io/pypi/v/orgpedia.svg)](https://pypi.org/project/orgpedia/)\n[![python](https://img.shields.io/pypi/pyversions/orgpedia.svg)](https://pypi.org/project/orgpedia/)\n[![Build Status](https://github.com/mukundesh/orgpedia/actions/workflows/dev.yml/badge.svg)](https://github.com/mukundesh/orgpedia/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/mukundesh/orgpedia/branch/main/graphs/badge.svg)](https://codecov.io/github/mukundesh/orgpedia)\n\n\n\nOrganization Information\n\n\n* Documentation: <https://mukundesh.github.io/orgpedia>\n* GitHub: <https://github.com/mukundesh/orgpedia>\n* PyPI: <https://pypi.org/project/orgpedia/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Orgpedia Foundation',
    'author_email': 'orgpedia.foundation@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mukundesh/orgpedia',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
