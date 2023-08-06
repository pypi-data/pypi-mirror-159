# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leafhopper', 'leafhopper.descriptors']

package_data = \
{'': ['*']}

install_requires = \
['pytablewriter[html]>=0.64.2,<0.65.0']

entry_points = \
{'console_scripts': ['leafhopper = leafhopper.main:main']}

setup_kwargs = {
    'name': 'leafhopper',
    'version': '0.1.1',
    'description': 'A command line for generating project dependencies table',
    'long_description': None,
    'author': 'Yue Ni',
    'author_email': 'niyue.com@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/niyue/leafhopper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
