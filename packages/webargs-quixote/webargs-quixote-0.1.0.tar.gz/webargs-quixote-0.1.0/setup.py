# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webargs_quixote']

package_data = \
{'': ['*']}

install_requires = \
['Quixote==3.0.4', 'webargs==8.1.0']

setup_kwargs = {
    'name': 'webargs-quixote',
    'version': '0.1.0',
    'description': 'webargs support for quixote',
    'long_description': '# webargs-quixote\n\n[webargs](https://webargs.readthedocs.io/en/latest/index.html) support for Quixote web framework.\n\n## Usage\n\n```python\nfrom webargs import fields\nfrom webargs_quixote import parser, use_args\n\n\n@use_args({"value": fields.Int()})\ndef home(req, args):\n    return args\n```\n\nLooks [webargs](https://webargs.readthedocs.io/en/latest/index.html) docs for more details.\n',
    'author': 'ischaojie',
    'author_email': 'zhuzhezhe95@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
