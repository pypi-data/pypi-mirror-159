# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pulumi_ml']

package_data = \
{'': ['*']}

install_requires = \
['pulumi-aws>=5.4.0,<6.0.0',
 'pulumi-docker>=3.2.0,<4.0.0',
 'pulumi-kubernetes>=3.19.1,<4.0.0',
 'pulumi>=3.33.1,<4.0.0']

setup_kwargs = {
    'name': 'pulumi-ml',
    'version': '0.1.10',
    'description': 'Machine learning tools using Pulumi',
    'long_description': None,
    'author': 'Patrick Barker',
    'author_email': 'pbarker@onemedical.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
