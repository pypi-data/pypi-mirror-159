# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brr']

package_data = \
{'': ['*']}

install_requires = \
['Pillow==9.2.0', 'click==8.1.3']

entry_points = \
{'console_scripts': ['brr = brr.braille_renderer:cli']}

setup_kwargs = {
    'name': 'brr',
    'version': '0.2.0',
    'description': 'terminal image renderer using braille characters in true color',
    'long_description': None,
    'author': 'jeppetp',
    'author_email': 'jepptp@gmail.com',
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
