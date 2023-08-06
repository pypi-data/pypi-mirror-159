# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deap_er',
 'deap_er.algorithms',
 'deap_er.base',
 'deap_er.creator',
 'deap_er.gp',
 'deap_er.operators',
 'deap_er.operators.selection',
 'deap_er.records',
 'deap_er.strategies',
 'deap_er.utilities',
 'deap_er.utilities.hypervolume',
 'deap_er.utilities.sorting']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.4,<2.0.0', 'ray>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'deap-er',
    'version': '0.4.0',
    'description': 'Distributed Evolutionary Algorithms in Python - Entirely Reworked',
    'long_description': None,
    'author': 'Mattias Aabmets',
    'author_email': 'mattias.aabmets@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
