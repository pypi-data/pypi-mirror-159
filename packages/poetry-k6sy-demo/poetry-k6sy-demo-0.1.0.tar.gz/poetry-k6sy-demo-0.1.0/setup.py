# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_k6sy_demo']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.1.3,<3.0.0']

setup_kwargs = {
    'name': 'poetry-k6sy-demo',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Kalidou SY',
    'author_email': 'kalidou.harouna.sy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
