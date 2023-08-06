# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['soccer_articles']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4==4.10.0']

setup_kwargs = {
    'name': 'soccer-articles',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'keurcien',
    'author_email': 'keurcien@appchoose.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
