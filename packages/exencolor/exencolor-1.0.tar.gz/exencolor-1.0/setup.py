# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['exencolor']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'exencolor',
    'version': '1.0',
    'description': 'A modern module for colored output.',
    'long_description': None,
    'author': 'Exenifix',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Exenifix/exencolor',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
