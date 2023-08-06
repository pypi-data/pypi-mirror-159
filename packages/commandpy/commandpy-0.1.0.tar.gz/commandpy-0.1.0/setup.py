# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commandpy']

package_data = \
{'': ['*']}

install_requires = \
['tokenstream>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'commandpy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'iRedSC',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
