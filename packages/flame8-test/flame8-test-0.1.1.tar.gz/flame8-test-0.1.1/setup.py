# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flame8_test']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7,<4.0']

entry_points = \
{'console_scripts': ['flake8-markdown = flake8_markdown:main']}

setup_kwargs = {
    'name': 'flame8-test',
    'version': '0.1.1',
    'description': 'Lints Python code blocks in Markdown files using flake8',
    'long_description': 'Test publishing',
    'author': 'Abdel Jaidi',
    'author_email': 'flake8@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johnfraney/flake8-markdown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
