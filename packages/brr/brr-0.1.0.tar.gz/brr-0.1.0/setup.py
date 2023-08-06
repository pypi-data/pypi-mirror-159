# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['brr']

package_data = \
{'': ['*']}

install_requires = \
['Pillow==9.2.0', 'click==8.1.3']

setup_kwargs = {
    'name': 'brr',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'jeppetp',
    'author_email': 'jepptp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
