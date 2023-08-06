# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reproducible_builds', 'reproducible_builds.data']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<8.2.0', 'packaging>=21.3,<21.4', 'requests>=2.28,<2.29']

setup_kwargs = {
    'name': 'reproducible-builds',
    'version': '0.1.0',
    'description': 'Reproducible builds for the python package ecosystem',
    'long_description': None,
    'author': 'Martin Carnogursky',
    'author_email': 'admin@sourcecode.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SourceCode-AI/reproducible-python-builds',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
