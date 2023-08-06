# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mupa_server']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'numpy>=1.23.1,<2.0.0', 'sounddevice>=0.4.4,<0.5.0']

setup_kwargs = {
    'name': 'mupa-server',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
