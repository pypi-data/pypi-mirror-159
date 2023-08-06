# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflow']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alfred-pyflow',
    'version': '0.1.0',
    'description': 'Minimal library for the development of Alfred Workflows.',
    'long_description': '# alfred-pyflow',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedecalendino/alfred-pyflow',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
