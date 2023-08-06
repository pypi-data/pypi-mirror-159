# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_match']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pretty-match',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Skonik',
    'author_email': 's.konik.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
