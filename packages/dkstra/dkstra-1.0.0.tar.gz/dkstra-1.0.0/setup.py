# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.datasets', 'src.pandas', 'src.spark']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dkstra',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Borja Elizalde Masia',
    'author_email': 'elizalde.borja@bcg.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
