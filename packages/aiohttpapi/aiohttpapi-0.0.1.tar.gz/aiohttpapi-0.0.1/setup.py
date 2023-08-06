# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttpapi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiohttpapi',
    'version': '0.0.1',
    'description': '',
    'long_description': '# aiohttpapi\n\n[![PyPI](https://img.shields.io/pypi/v/aiohttpapi)](https://pypi.org/project/aiohttpapi/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiohttpapi)](https://www.python.org/downloads/)\n[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/aiohttpapi)](https://github.com/daxartio/aiohttpapi)\n[![GitHub stars](https://img.shields.io/github/stars/daxartio/aiohttpapi?style=social)](https://github.com/daxartio/aiohttpapi)\n\n```\npip install aiohttpapi\n```\n\n## Contributing\n\n[Contributing](CONTRIBUTING.md)\n',
    'author': 'Danil Akhtarov',
    'author_email': 'daxartio@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/aiohttpapi',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
