# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['recursive_action']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'recursive-action',
    'version': '0.1.1',
    'description': 'Recursive classes and methods',
    'long_description': None,
    'author': 'Dragon',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
