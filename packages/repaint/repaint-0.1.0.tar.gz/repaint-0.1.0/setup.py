# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repaint']

package_data = \
{'': ['*'], 'repaint': ['js/*']}

install_requires = \
['cached-property>=1.5.2,<2.0.0', 'click>=8.0.0', 'websockets>=10.3,<11.0']

entry_points = \
{'console_scripts': ['repaint = repaint.cli:cli']}

setup_kwargs = {
    'name': 'repaint',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
