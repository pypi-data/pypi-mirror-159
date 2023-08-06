# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clayhead']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.6.0,<23.0.0', 'python-socketio[asyncio_client]>=5.7.1,<6.0.0']

setup_kwargs = {
    'name': 'clayhead',
    'version': '0.1.0',
    'description': 'Official Clayhead client SDK for Python',
    'long_description': None,
    'author': 'Bo Powers',
    'author_email': 'bo@clayhead.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
