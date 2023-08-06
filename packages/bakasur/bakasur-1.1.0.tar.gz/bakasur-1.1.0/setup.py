# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bakasur']

package_data = \
{'': ['*']}

install_requires = \
['datapane>=0.14.0,<0.15.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.4.4,<13.0.0',
 'typer[all]>=0.4.2,<0.5.0']

entry_points = \
{'console_scripts': ['bakasur = bakasur.main:app']}

setup_kwargs = {
    'name': 'bakasur',
    'version': '1.1.0',
    'description': 'Bakasur is your friendly demon that helps you analyse your Thuisbezorgd order history and visualise patterns.',
    'long_description': None,
    'author': 'Devendra Kulkarni',
    'author_email': 'kulkarnidevendra21@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11.0',
}


setup(**setup_kwargs)
