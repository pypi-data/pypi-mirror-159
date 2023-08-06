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
    'version': '0.1.5',
    'description': '',
    'long_description': '```python\nfrom soccer_articles import get_bbc_articles\n\nget_bbc_articles(["https://www.bbc.com/sport/football/XXX"])\n\n> [{\'source\': \'bbc\',\n  \'url\': \'https://www.bbc.com/sport/football/XXX\',\n  \'author\': \'John Doe\',\n  \'date\': \'3 hours ago\',\n  \'headline\': \'John Doe wants to join the Newteam\',\n  \'body\': \'After a brilliant season...\'\n}]\n```\n',
    'author': 'keurcien',
    'author_email': 'keurcien@appchoose.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.2,<4.0',
}


setup(**setup_kwargs)
