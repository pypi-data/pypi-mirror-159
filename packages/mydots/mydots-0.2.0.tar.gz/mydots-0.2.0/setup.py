# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mydots']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mydots = mydots.__main__:cli.main']}

setup_kwargs = {
    'name': 'mydots',
    'version': '0.2.0',
    'description': 'A simple JSON parser.',
    'long_description': 'mydots\n======\n\nA simple JSON parser.\n\n',
    'author': 'Łukasz Wieczorek',
    'author_email': 'wieczorek1990@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
