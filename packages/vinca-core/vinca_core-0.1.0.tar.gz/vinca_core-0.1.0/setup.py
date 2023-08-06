# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vinca_core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vinca-core',
    'version': '0.1.0',
    'description': 'Dependency or all vinca applications. Not a standalone repository',
    'long_description': None,
    'author': 'Oscar Laird',
    'author_email': 'olaird25@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
