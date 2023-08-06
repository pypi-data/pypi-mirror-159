# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['macnotesapp', 'macnotesapp.cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'markdown2>=2.4.3,<3.0.0',
 'py-applescript>=1.0.3,<2.0.0',
 'questionary>=1.10.0,<2.0.0',
 'rich>=12.4.4,<13.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['notes = macnotesapp.__main__:cli_main']}

setup_kwargs = {
    'name': 'macnotesapp',
    'version': '0.1.0',
    'description': 'Automate Apple / macOS Notes.app with python.',
    'long_description': None,
    'author': 'Rhet Turnbull',
    'author_email': 'rturnbull@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
