# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['saghetti']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.5.1,<13.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['saghetti = saghetti.cli:main']}

setup_kwargs = {
    'name': 'saghetti',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'Patrick Arminio',
    'author_email': 'patrick.arminio@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
