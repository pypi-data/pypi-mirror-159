# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['umbreon', 'umbreon.cogs']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.7.3,<2.0.0',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'jishaku>=2.3.2,<3.0.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'requests>=2.27.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'umbreon',
    'version': '0.1.0',
    'description': 'A fun multi-purpose Discord bot.',
    'long_description': None,
    'author': 'mudkipdev',
    'author_email': '86132148+mudkipdev@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mudkipdev/umbreon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
