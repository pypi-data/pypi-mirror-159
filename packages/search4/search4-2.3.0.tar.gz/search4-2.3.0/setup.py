# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['search4']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'colorama>=0.4.5,<0.5.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['search4 = search4.search4:main']}

setup_kwargs = {
    'name': 'search4',
    'version': '2.3.0',
    'description': 'Sweet OSINT tool to find people on the social media.',
    'long_description': '<p align="center">\n<a href="https://github.com/meanii/Search4">\n<img src="https://media.discordapp.net/attachments/749199487854968843/775966094670037012/IMG_20200828_114636_438.jpg" alt="search4"></a>\n\n> An OSINT tool that helps you to find people on the internet. It\'s small and fast!\n</p>\n\n<hr>\n\n#### Prerequisites\n\n- [Install python3 as per your distro.](https://realpython.com/installing-python)\n\nInstalling search4\n\n- Now you can install search4 using git:\n\n```\npip3 install -U search4\n```\n\nOr, if you already downloaded search4, you can install it directly from the directory:\n```\npip3 install .\n```\n\nYou can use the `-e` flag to install the project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.\n\n<hr>\n\n#### Demo\n\n```\nsearch4 -u username\n```\n\n<a href="https://asciinema.org/a/384004">\n<img src="https://media.discordapp.net/attachments/749199487854968843/798402820163239956/image0.png"></a>\n\n---\n###  Copyright & License\n- Copyright (C)  2022 [meanii](https://github.om/meanii )\n- Licensed under the terms of the [GNU General Public License v3.0](https://github.com/meanii/Search4/blob/master/LICENSE)',
    'author': 'anil chauhan',
    'author_email': 'anilchauhanxda@gmail.com',
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
