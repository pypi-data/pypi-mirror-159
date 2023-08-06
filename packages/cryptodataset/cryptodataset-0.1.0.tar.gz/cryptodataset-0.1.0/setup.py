# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cryptodataset']

package_data = \
{'': ['*']}

install_requires = \
['ccxt>=1.90.10,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['cryptodata = cryptodata.cli:cli']}

setup_kwargs = {
    'name': 'cryptodataset',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'なるみ',
    'author_email': None,
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
