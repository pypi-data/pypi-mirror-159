# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['constrained_attacks',
 'constrained_attacks.attacks',
 'constrained_attacks.attacks.cpgd',
 'constrained_attacks.attacks.moeva',
 'constrained_attacks.classifier',
 'constrained_attacks.constraints',
 'constrained_attacks.objective_calculator',
 'constrained_attacks.utils']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.1.0,<2.0.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pymoo>=0.5.0,<0.6.0',
 'tqdm>=4.63.1,<5.0.0']

extras_require = \
{'tensorflow': ['adversarial-robustness-toolbox[tensorflow]==1.10',
                'tensorflow==2.8']}

setup_kwargs = {
    'name': 'constrained-attacks',
    'version': '0.1.0',
    'description': 'constrained-attacks is a framework to generate adversarial examples under domain specific constraints.',
    'long_description': None,
    'author': 'Thibault Simonetto',
    'author_email': 'thibault.simonetto.001@student.uni.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
