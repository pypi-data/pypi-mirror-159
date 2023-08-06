# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['primer_io']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'primer-io',
    'version': '0.1.1',
    'description': 'A project created exclusively to reserve the `primer-io` namespace.',
    'long_description': '# Primer.io\n\nThe namespace of the project has been reserved for the future use by Primer.io.\nPlease email mykola@primer.io if you have any questions.',
    'author': 'Mykola Solodukha',
    'author_email': 'mykola@primer.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mykolasolodukha/primer-io',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
