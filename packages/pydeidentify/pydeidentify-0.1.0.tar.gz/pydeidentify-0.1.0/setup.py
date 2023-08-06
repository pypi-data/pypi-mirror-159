# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydeidentify']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.12.0,<2.0.0', 'transformers>=4.20.1,<5.0.0']

setup_kwargs = {
    'name': 'pydeidentify',
    'version': '0.1.0',
    'description': "A simple text deidentification tool, built on huggingface's named entity recognition pipeline",
    'long_description': None,
    'author': 'Lucasc-99',
    'author_email': 'lucascecchi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
