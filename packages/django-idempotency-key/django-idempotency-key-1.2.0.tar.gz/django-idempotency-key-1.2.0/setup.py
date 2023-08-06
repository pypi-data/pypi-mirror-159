# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['idempotency_key', 'idempotency_key.locks']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2', 'djangorestframework>=3.8']

setup_kwargs = {
    'name': 'django-idempotency-key',
    'version': '1.2.0',
    'description': 'Django middleware for idempotency key support in view and viewset functions.',
    'long_description': None,
    'author': 'YoyoDevs',
    'author_email': 'dev@yoyowallet.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
