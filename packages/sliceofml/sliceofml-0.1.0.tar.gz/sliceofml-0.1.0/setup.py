# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sliceofml']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'requests-oauthlib>=1.3.1,<2.0.0',
 'rich>=12.4.4,<13.0.0']

entry_points = \
{'console_scripts': ['sliceofml = sliceofml.cli:cli']}

setup_kwargs = {
    'name': 'sliceofml',
    'version': '0.1.0',
    'description': 'Slice of ML or SOML is your little 🍰 of ML.',
    'long_description': None,
    'author': 'FL33TW00D',
    'author_email': 'chris@notia.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
