# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sunglass']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.3,<2.0.0', 'solcore>=5.7.7,<6.0.0']

setup_kwargs = {
    'name': 'sunglass',
    'version': '0.1.0',
    'description': 'GUI for easily use Solcore',
    'long_description': None,
    'author': 'Diego Alonso Álvarez',
    'author_email': 'd.alonso-alvarez@imperial.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
