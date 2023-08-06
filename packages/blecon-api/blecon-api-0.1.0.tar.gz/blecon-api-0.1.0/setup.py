# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blecon_api']

package_data = \
{'': ['*']}

install_requires = \
['requests[all]>=2.27.1,<3.0.0', 'typer[all]>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['blecon-api = blecon_api.main:app']}

setup_kwargs = {
    'name': 'blecon-api',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'danros',
    'author_email': 'dan.ros@blecon.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
