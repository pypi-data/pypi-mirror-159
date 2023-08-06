# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pynecraft']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pynecraft',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ken Arnold',
    'author_email': 'arnold@peak.im',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
