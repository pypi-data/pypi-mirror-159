# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isprime_pypackage']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['isprime_pyPackage = isprime_pypackage:isPrime']}

setup_kwargs = {
    'name': 'isprime-pypackage',
    'version': '0.1.0',
    'description': 'A python pacakge to check if a number is prime',
    'long_description': None,
    'author': 'Arslan909',
    'author_email': 'Arslan909@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
