# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enum_properties']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'enum-properties',
    'version': '1.0.0',
    'description': 'Add properties to Python enumeration values with a simple declarative syntax.',
    'long_description': None,
    'author': 'Brian Kohan',
    'author_email': 'bckohan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://enum-properties.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
