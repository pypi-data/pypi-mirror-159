# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['text_embeddings',
 'text_embeddings.base',
 'text_embeddings.byte',
 'text_embeddings.hash',
 'text_embeddings.pruning',
 'text_embeddings.visual',
 'text_embeddings.x']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.1,<9.0.0',
 'einops>=0.3.0,<0.4.0',
 'grpcio==1.38.1',
 'loguru>=0.5.3,<0.6.0',
 'mmh3>=3.0.0,<4.0.0',
 'numpy>=1.21.1,<2.0.0',
 'pdoc3>=0.9.2,<0.10.0',
 'pytest>=6.2.4,<7.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'scipy>=1.8.1,<2.0.0',
 'tokenizers>=0.12.1,<0.13.0',
 'torch>=1.12.0,<2.0.0',
 'transformers>=4.8.2,<5.0.0']

setup_kwargs = {
    'name': 'text-embeddings',
    'version': '0.2.0',
    'description': 'zero-vocab or low-vocab embeddings',
    'long_description': None,
    'author': 'Chenghao Mou',
    'author_email': 'mouchenghao@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
