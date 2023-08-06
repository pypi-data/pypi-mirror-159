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
    'version': '0.1.2',
    'description': "A simple text deidentification tool, built on huggingface's named entity recognition pipeline",
    'long_description': '# pydeidentify\n\nA Python library for easy text deidentification\n\n## Usage\n\nView more detailed examples at https://github.com/Lucasc-99/pydeidentify\n\nDISCLAIMER: this pipeline is not 100% accurate, and may miss some entities\n\nThe models are also case sensitive, and may not tag entities if they are lower-case\n\n```python\n\nfrom pydeidentify import Deidentifier, DeidentifiedText\n\n# Deidentify using this Deidentifier class\nd = Deidentifier()\nd_text: DeidentifiedText = d.deidentify("My name is Joe Biden, I\'m from Scranton, Pennsylvania and I like to create python packages")\n\n# View output of deidentification using DeidentifiedText class\nprint(d_text.original()) # My name is Joe Biden, I\'m from Scranton, Pennsylvania and I like to create python packages\nprint(d_text) # My name is PER0, I\'m from LOC0, LOC1 and I like to create python packages\nprint(d_text.encode_mapping) # {\'Joe Biden\': \'PER0\', \'Scranton\': \'LOC0\', \'Pennsylvania\': \'LOC1\'}\nprint(d_text.decode_mapping) # {\'PER0\': \'Joe Biden\', \'LOC0\': \'Scranton\', \'LOC1\': \'Pennsylvania\'}\nprint(d_text.counts) # {\'PER\': 1, \'ORG\': 0, \'LOC\': 2, \'MISC\': 0}\n```\n\n## Contributing\nAll pull requests are welcome.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)',
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
