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
    'version': '0.1.1',
    'description': 'GUI for easily use Solcore',
    'long_description': '# Sunglass\n\n*"What you need to look at Solcore!"*\n\nSunglass is a simple - and not yet fully operational - graphical user interface for the\nsolar cells and semiconductors modelling framework Solcore. \n\n## Using Sunglass\n\n1. Install it from PyPI\n\n```bash\npip install sunglass\n```\n\n2. If you want PDD support in Solcore, re-install Solcore with that support:\n\n```bash\npip install --no-deps --force-reinstall --install-option="--with_pdd" solcore\n```\n\n3. Run it!\n\n```bash\npython -m sunglass\n```\n\n## Develop Sunglass\n\n1. Install poetry following the instructions for your OS: https://python-poetry.org/docs/\n2. `git clone` this repository.\n3. Navigate to thee root folder and install sunglass with `poetry install`\n4. If you want PDD support in Solcore, re-install Solcore with that support:\n\n```bash\npip install --no-deps --force-reinstall --install-option="--with_pdd" solcore\n```',
    'author': 'Diego Alonso Álvarez',
    'author_email': 'd.alonso-alvarez@imperial.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ImperialCollegeLondon/sunglass',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
