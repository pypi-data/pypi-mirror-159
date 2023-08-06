# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpucompare']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.5.1,<13.0.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['gpucompare = gpucompare.__main__:app']}

setup_kwargs = {
    'name': 'gpucompare',
    'version': '1.0.0',
    'description': 'Compare GPUs',
    'long_description': '# gpucompare\n\n<div align="center">\n\n[![Build status](https://github.com/kHarshit/gpucompare/workflows/build/badge.svg?branch=master&event=push)](https://github.com/kHarshit/gpucompare/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/gpucompare.svg)](https://pypi.org/project/gpucompare/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/kHarshit/gpucompare/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/kHarshit/gpucompare/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/kHarshit/gpucompare/releases)\n[![License](https://img.shields.io/github/license/kHarshit/gpucompare)](https://github.com/kHarshit/gpucompare/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nCompare GPUs\n\n</div>\n\n## Installation\n\n```bash\npip install -U gpucompare\n```\n\nor install with `Poetry`\n\n```bash\npoetry add gpucompare\n```\n\nThen you can run\n\n```bash\ngpucompare --help\n```\n\nor with `Poetry`:\n\n```bash\npoetry run gpucompare --help\n```\n\n## Working\n\n```bash\n$ gpucompare --help\n\n Usage: gpucompare [OPTIONS]                                                                                \n                                                                                                            \n Compare GPUs                                                                                               \n                                                                                                            \n╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ *  --csv-data          TEXT  CSV file containing row-wise GPU data           [default: None] [required]  │\n│                                                                                                          │\n│                              Possible columns:                                                           │\n│                              gpu_name (str): name of gpu  [required]                                     │\n│                              architecture (str): GPU architecture                                        │\n│                              cuda_cores (int): number of cuda cores                                      │\n│                              fp32_perf (float): fp32 performance in TFLOPS                               │\n│                              fp16_perf (float): fp16 performance in TFLOPS                               │\n│                              int8_perf (float): int8 performance in TOPS                                 │\n│                              mem (float): gpu memory in GiB                                              │\n│                              mem_bandwidth (float): memory bandwidth in GB/s                             │\n│    --version   -v            Prints the version of the gpucompare package.                               │\n│    --help                    Show this message and exit.                                                 │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n\n```bash\n$ gpucompare --csv-data assets/gpu_data.csv\n# gpu_data.csv\n# gpu_name,architecture,int8_perf,mem_bandwidth\n# A2,ampere,36,200\n# A10,ampere,250,600\n# A30,ampere,330,933\n{\'A10/A2\': \'3.0x\', \'A30/A2\': \'4.67x\'}\n```\n\n## Contributing\n\nThanks for considering contributing to this project. Please follow [Contributing guidelines](https://github.com/kHarshit/gpucompare/blob/master/CONTRIBUTING.md).\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/kHarshit/gpucompare)](https://github.com/kHarshit/gpucompare/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/kHarshit/gpucompare/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{gpucompare,\n  author = {kHarshit},\n  title = {Compare GPUs},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/kHarshit/gpucompare}}\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'kHarshit',
    'author_email': 'kumar_harshit@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kHarshit/gpucompare',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
