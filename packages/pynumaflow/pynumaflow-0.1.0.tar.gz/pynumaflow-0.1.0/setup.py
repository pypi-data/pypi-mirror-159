# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynumaflow',
 'pynumaflow.function',
 'pynumaflow.sink',
 'pynumaflow.tests',
 'pynumaflow.tests.function',
 'pynumaflow.tests.sink']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'dataclasses-json>=0.5.7,<0.6.0',
 'msgpack>=1.0.3,<2.0.0']

setup_kwargs = {
    'name': 'pynumaflow',
    'version': '0.1.0',
    'description': 'Provides the interfaces of writing Python User Defined Functions and Sinks for NumaFlow.',
    'long_description': None,
    'author': 'NumaFlow Developers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
