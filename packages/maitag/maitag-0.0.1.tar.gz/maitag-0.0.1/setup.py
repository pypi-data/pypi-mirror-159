# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['maitag']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0.6,<5.0.0',
 'fng-api>=0.0.5,<0.0.6',
 'huggingface-hub>=0.8.1,<0.9.0',
 'jupyter>=1.0.0,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'scikit-learn>=1.1.1,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'sentence-transformers>=2.2.2,<3.0.0',
 'simpletransformers>=0.63.7,<0.64.0',
 'spacy>=3.4.0,<4.0.0',
 'torch>=1.12.0,<2.0.0',
 'transformers>=4.20.1,<5.0.0']

setup_kwargs = {
    'name': 'maitag',
    'version': '0.0.1',
    'description': 'MAIT - Machine-Assisted Intent Tagging',
    'long_description': None,
    'author': 'Hobson Lane',
    'author_email': 'hobson@tangibleai.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
