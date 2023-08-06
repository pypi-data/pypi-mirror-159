# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['obey']

package_data = \
{'': ['*']}

install_requires = \
['tabulate>=0.8.10,<0.9.0']

setup_kwargs = {
    'name': 'obey',
    'version': '0.0.1',
    'description': 'Python package for creating command line interfaces',
    'long_description': None,
    'author': 'Artem Legotin',
    'author_email': 'hello@artemlegotin.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
