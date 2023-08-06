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
    'version': '0.1.1',
    'description': 'constrained-attacks is a framework to generate adversarial examples under domain specific constraints.',
    'long_description': '# Constrained attacks\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![arXiv](https://img.shields.io/badge/arXiv-2112.01156-b31b1b.svg)](https://arxiv.org/abs/2112.01156)\n\n## Description\n\nConstrained attacks is a framework for constraints adversarial examples unified across multiple constraints\' domain.\nIt currently supports a large diversity of constraints (linear and non-linear).\nWe instantiated our framework with two attacks:\n- MoEvA2: a multi-objective genetic based approach\n- C-PGD: a gradient based approach extended from PGD (cite) to support domain constraints.\n\nTo learn more, check out our paper [A Unified Framework for Adversarial Attack and Defense in Constrained Feature\n    Space](https://arxiv.org/abs/2112.01156).\n\n## Installation\n\n### Using pip\n\n```shell\npip install constrained-attacks\n```\n\n## Dependencies\n\nconstrained-attacks requires:\n\n- python = "~3.8"\n- numpy = "^1.22.3"\n- joblib = "^1.1.0"\n- pymoo = "^0.5.0"\n- tqdm = "^4.63.1"\n- pandas = "^1.4.1"\n\nAdditional optional requirements for C-PGD are:\n- tensorflow = "2.8"\n- adversarial-robustness-toolbox[tensorflow] = "1.10"\n\n## Examples\n\nYou can find a usage example\n- for MoEvA2: [tests/attacks/moeva/test_moeva_run.py](tests/attacks/moeva/test_moeva_run.py)\n- for C-PGD: [tests/attacks/cpgd/test_pgd_run.py](tests/attacks/cpgd/test_pgd_run.py)\n- for the constraints definition: [tests/attacks/moeva/url_constraints.py](tests/attacks/moeva/url_constraints.py).\n\n## Citation\n\nIf you have used our framework for research purposes, you can cite our publication by:\n\nBibTex:\n```\n@article{simonetto2021unified,\n  title={A unified framework for adversarial attack and defense in constrained feature space},\n  author={Simonetto, Thibault and Dyrmishi, Salijona and Ghamizi, Salah and Cordy, Maxime and Traon, Yves Le},\n  journal={arXiv preprint arXiv:2112.01156},\n  year={2021}\n}\n```\n',
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
