# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datawhys_dashboard', 'datawhys_dashboard.api']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.1.5,<2.0.0', 'requests>=2.27.0,<3.0.0']

setup_kwargs = {
    'name': 'datawhys-dashboard',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'DataWhys DevTeam',
    'author_email': 'devteam@datawhys.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
