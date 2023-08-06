# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monet_pytorch', 'monet_pytorch.template']

package_data = \
{'': ['*'],
 'monet_pytorch': ['config/dataset/*',
                   'config/model/*',
                   'config/special_cases/*']}

install_requires = \
['hydra-core>=1.2.0,<2.0.0', 'path>=15.0,<=16.4.0', 'torch>=1.8,<=1.12.0']

setup_kwargs = {
    'name': 'monet-pytorch',
    'version': '1.0.1',
    'description': 'Pytorch implementation of Multi-Object Network(MONet)',
    'long_description': None,
    'author': 'mikedev',
    'author_email': 'mik3dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Michedev/MONet-pytorch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
