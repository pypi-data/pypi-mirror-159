# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['beryl_events_utils']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.39,<2.0.0',
 'asyncpg>=0.26.0,<0.27.0',
 'uvloop>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'beryl-events-utils',
    'version': '2.0.1',
    'description': "A set of async utils for Beryl's Events system",
    'long_description': "<div align=center>\n\n# Beryl-Events-Utils\n\n![PyPI](https://img.shields.io/pypi/v/beryl-events-utils?label=PyPi&logo=pypi&logoColor=white) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beryl-events-utils?label=Python&logo=python&logoColor=white) ![PyPI - License](https://img.shields.io/pypi/l/beryl-events-utils?label=License&logo=pypi&logoColor=white)\n\nA set of async utils for Beryl's Events system\n\n<div align=left>\n\n# Info\n\nBeryl, which is a discord bot offers a events system, where users can set an event and then later check how much more days is there left. The events system is powered off of PostgreSQL and thus requires an PostgreSQL server in order to use. These are the base corountines used by Beryl.\n\n# Installation\n\n## Pip\n\n```sh\npip install beryl-events-utils\n```\n\n## Poetry\n\n```sh\npoetry add beryl-events-utils\n```\n\n# License\n\nMIT\n",
    'author': 'No767',
    'author_email': '73260931+No767@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/No767/Beryl-Events-Utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
