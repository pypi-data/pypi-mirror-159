# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fstlk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fstlk',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'vribic',
    'author_email': 'viran.ribic@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
