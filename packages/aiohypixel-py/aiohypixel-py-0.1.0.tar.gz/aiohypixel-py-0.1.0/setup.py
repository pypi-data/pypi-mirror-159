# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohypixel-py']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'aiohypixel-py',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'JacobMonck',
    'author_email': 'jacobamonck@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
