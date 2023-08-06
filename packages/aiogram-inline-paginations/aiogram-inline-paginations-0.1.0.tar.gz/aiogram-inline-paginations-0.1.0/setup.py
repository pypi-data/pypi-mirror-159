# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram-inline-paginations']

package_data = \
{'': ['*']}

install_requires = \
['aiogram>=2.21,<3.0',
 'pip>=22.1.2,<23.0.0',
 'setuptools>=63.2.0,<64.0.0',
 'wheel>=0.37.1,<0.38.0']

setup_kwargs = {
    'name': 'aiogram-inline-paginations',
    'version': '0.1.0',
    'description': 'A simple library for aiogram that allows you to easily do pagination for any Inline keyboards.',
    'long_description': None,
    'author': 'Daniil Shamraev',
    'author_email': 'shamraev.2002@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
