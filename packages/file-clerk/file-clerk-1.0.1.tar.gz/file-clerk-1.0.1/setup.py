# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['file_clerk']

package_data = \
{'': ['*']}

install_requires = \
['autoflake8>=0.3.2,<0.4.0',
 'black>=22.6.0,<23.0.0',
 'bs4>=0.0.1,<0.0.2',
 'isort>=5.10.1,<6.0.0',
 'nltk>=3.7,<4.0',
 'pip-licenses>=3.5.4,<4.0.0',
 'pre-commit>=2.20.0,<3.0.0']

setup_kwargs = {
    'name': 'file-clerk',
    'version': '1.0.1',
    'description': 'A collection of functions for dealing with files and file content.',
    'long_description': None,
    'author': 'hundredvisionsguy',
    'author_email': 'cwinikka@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/HundredVisionsGuy/file-clerk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
