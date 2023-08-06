# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enum_properties']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'enum-properties',
    'version': '1.0.1',
    'description': 'Add properties to Python enumeration values with a simple declarative syntax.',
    'long_description': "|MIT license| |PyPI version fury.io| |PyPI pyversions| |PyPI status| |Documentation Status|\n|Code Cov| |Test Status|\n\n.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg\n   :target: https://lbesson.mit-license.org/\n\n.. |PyPI version fury.io| image:: https://badge.fury.io/py/enum-properties.svg\n   :target: https://pypi.python.org/pypi/enum-properties/\n\n.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/enum-properties.svg\n   :target: https://pypi.python.org/pypi/enum-properties/\n\n.. |PyPI status| image:: https://img.shields.io/pypi/status/enum-properties.svg\n   :target: https://pypi.python.org/pypi/enum-properties\n\n.. |Documentation Status| image:: https://readthedocs.org/projects/enum-properties/badge/?version=latest\n   :target: http://enum-properties.readthedocs.io/?badge=latest/\n\n.. |Code Cov| image:: https://codecov.io/gh/bckohan/enum-properties/branch/main/graph/badge.svg?token=0IZOKN2DYL\n   :target: https://codecov.io/gh/bckohan/enum-properties\n\n.. |Test Status| image:: https://github.com/bckohan/enum-properties/workflows/test/badge.svg\n   :target: https://github.com/bckohan/enum-properties/actions\n\nEnum Properties\n#######################\n\nAdd properties to Python enumeration values with a simple declarative syntax.\n`Enum Properties <https://enum-properties.readthedocs.io/en/latest/>`_ is a\nlightweight extension to\n`Python's Enum class <https://docs.python.org/3/library/enum.html>`_. Example:\n\n.. code:: python\n\n    from enum_properties import EnumProperties, p\n    from enum import auto\n\n    class Color(EnumProperties, p('rgb'), p('hex')):\n\n        # name   value      rgb       hex\n        RED    = auto(), (1, 0, 0), 'ff0000'\n        GREEN  = auto(), (0, 1, 0), '00ff00'\n        BLUE   = auto(), (0, 0, 1), '0000ff'\n\n    # the named p() values in the Enum's inheritance become properties on\n    # each value, matching the order in which they are specified\n\n    Color.RED.rgb   == (1, 0, 0)\n    Color.GREEN.rgb == (0, 1, 0)\n    Color.BLUE.rgb  == (0, 0, 1)\n\n    Color.RED.hex   == 'ff0000'\n    Color.GREEN.hex == '00ff00'\n    Color.BLUE.hex  == '0000ff'\n\nProperties may also be symmetrically mapped to enumeration values, using\ns() values:\n\n.. code:: python\n\n    from enum_properties import EnumProperties, s\n    from enum import auto\n\n    class Color(EnumProperties, s('rgb'), s('hex', case_fold=True)):\n\n        RED    = auto(), (1, 0, 0), 'ff0000'\n        GREEN  = auto(), (0, 1, 0), '00ff00'\n        BLUE   = auto(), (0, 0, 1), '0000ff'\n\n    # any named s() values in the Enum's inheritance become properties on\n    # each value, and the enumeration value may be instantiated from the\n    # property's value\n\n    Color((1, 0, 0)) == Color.RED\n    Color((0, 1, 0)) == Color.GREEN\n    Color((0, 0, 1)) == Color.BLUE\n\n    Color('ff0000') == Color.RED\n    Color('FF0000') == Color.RED  # case_fold makes mapping case insensitive\n    Color('00ff00') == Color.GREEN\n    Color('00FF00') == Color.GREEN\n    Color('0000ff') == Color.BLUE\n    Color('0000FF') == Color.BLUE\n\n    Color.RED.hex == 'ff0000'\n\nPlease report bugs and discuss features on the\n`issues page <https://github.com/bckohan/enum-properties/issues>`_.\n\n`Contributions <https://github.com/bckohan/enum-properties/blob/main/CONTRIBUTING.rst>`_ are\nencouraged!\n\n`Full documentation at read the docs. <https://enum-properties.readthedocs.io/en/latest/>`_\n\nInstallation\n------------\n\n1. Clone enum-properties from GitHub_ or install a release off PyPI_ :\n\n.. code:: bash\n\n       pip install enum-properties\n\n\n.. _GitHub: http://github.com/bckohan/enum-properties\n.. _PyPI: http://pypi.python.org/pypi/enum-properties\n",
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
