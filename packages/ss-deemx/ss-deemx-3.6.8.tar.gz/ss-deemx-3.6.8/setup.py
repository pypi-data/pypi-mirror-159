# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deemix', 'deemix.plugins', 'deemix.types', 'deemix.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'deezer-py>=1.3.7,<2.0.0',
 'mutagen>=1.45.1,<2.0.0',
 'pycryptodomex>=3.15.0,<4.0.0',
 'requests>=2.25.1,<3.0.0',
 'spotipy>=2.11.0,<3.0.0']

setup_kwargs = {
    'name': 'ss-deemx',
    'version': '3.6.8',
    'description': '*Deemx API, forked for spotify_sync',
    'long_description': '# dmx fork for spotify_sync',
    'author': 'JBH',
    'author_email': 'admin@jbh.cloud',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jbh-cloud/ss-deemx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
