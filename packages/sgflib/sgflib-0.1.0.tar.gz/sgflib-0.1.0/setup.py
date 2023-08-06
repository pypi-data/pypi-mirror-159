# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sgflib']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=6.4.1,<7.0.0', 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'sgflib',
    'version': '0.1.0',
    'description': 'SGF library',
    'long_description': None,
    'author': 'Oleksandr Hiliazov',
    'author_email': 'oleksandr.hiliazov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
