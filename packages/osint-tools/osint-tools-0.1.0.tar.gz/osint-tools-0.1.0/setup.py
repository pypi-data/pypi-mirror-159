# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['osint_tools']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.79.0,<0.80.0']

setup_kwargs = {
    'name': 'osint-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alexander Slessor',
    'author_email': 'alexjslessor@gmail.com.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
