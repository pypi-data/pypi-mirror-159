# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orgpedia', 'orgpedia.components', 'orgpedia.extracts']

package_data = \
{'': ['*']}

install_requires = \
['docint>=0.1.0,<0.2.0']

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
    'version': '0.1.1',
    'description': 'Orgpedia - Information about organizations.',
    'long_description': '# docInt README\nReadme about docInt, document intelligence\n',
    'author': 'Orgpedia Foundation',
    'author_email': 'orgpedia.foundation@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mukundesh/orgpedia',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
