# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mbpy_endpoints']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.4.4,<13.0.0', 'uplink>=0.9.7,<0.10.0']

setup_kwargs = {
    'name': 'mbpy-endpoints',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Adam Morris',
    'author_email': 'classroomtechtools.ctt@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
