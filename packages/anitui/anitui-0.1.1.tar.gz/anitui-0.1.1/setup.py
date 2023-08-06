# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anitui', 'anitui.utils', 'anitui.widgets']

package_data = \
{'': ['*']}

install_requires = \
['commonmark>=0.9.1,<0.10.0',
 'pygments-arm>=0.7.5,<0.8.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.5.1,<13.0.0',
 'textual>=0.1.18,<0.2.0']

entry_points = \
{'console_scripts': ['anitui = anitui.__init__:main']}

setup_kwargs = {
    'name': 'anitui',
    'version': '0.1.1',
    'description': 'A TUI to browse Anime',
    'long_description': None,
    'author': 'cakoshakib',
    'author_email': 'cakoshakib@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
