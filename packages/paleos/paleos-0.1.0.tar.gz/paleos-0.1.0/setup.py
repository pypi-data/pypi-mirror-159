# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paleos']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.21.4,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'scipy>=1.7.3,<2.0.0',
 'statsmodels>=0.13.1,<0.14.0']

setup_kwargs = {
    'name': 'paleos',
    'version': '0.1.0',
    'description': 'A package to help with paleoclimate data wrangling',
    'long_description': '# Welcome to Paleos\n\nPaleos is a lightweight python package for helping with lab based paleoclimate\ndata wrangling. Currently, the package implements methods to help with age\nmodels and has examples of how existing python tools can be used to quickly \nmanipulate paleoclimate related data.\n\nAdditional features may be added in the future. However, those looking for more\nadvanced capabilities are pointed to [pyleoclim](https://pypi.org/project/pyleoclim/).\n\n',
    'author': 'Neeraj Shah',
    'author_email': 'nss350@gmail.com',
    'maintainer': 'Neeraj Shah',
    'maintainer_email': 'nss350@gmail.com',
    'url': 'https://github.com/audersea/paleos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
