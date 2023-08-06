# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_colorgen']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['Py_colorgen = colorgen.py:colour_combination']}

setup_kwargs = {
    'name': 'py-colorgen',
    'version': '0.1.0',
    'description': 'A python script to create random color combination generator',
    'long_description': '# Py_colorgen\n\nA python based random color generator(Hex, rgb, hsl)\n\n## System Requirements\n\n-   Python3\n\n## Installation Instructions\n\n```py\npip install Py_colorgen\n```\n\n## Options\n\n```\n  -h, --help                    show this help message and exit\n\n  -r --rgb                      RGB random color combination and exit\n\n  -s --hsl                      HSL random color combination and exit\n\n  On default it generates Hex color combination and exit\n```',
    'author': 'Arslan909',
    'author_email': 'Arslan909@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
