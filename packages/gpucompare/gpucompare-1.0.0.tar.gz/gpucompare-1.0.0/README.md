# gpucompare

<div align="center">

[![Build status](https://github.com/kHarshit/gpucompare/workflows/build/badge.svg?branch=master&event=push)](https://github.com/kHarshit/gpucompare/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/gpucompare.svg)](https://pypi.org/project/gpucompare/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/kHarshit/gpucompare/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/kHarshit/gpucompare/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/kHarshit/gpucompare/releases)
[![License](https://img.shields.io/github/license/kHarshit/gpucompare)](https://github.com/kHarshit/gpucompare/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Compare GPUs

</div>

## Installation

```bash
pip install -U gpucompare
```

or install with `Poetry`

```bash
poetry add gpucompare
```

Then you can run

```bash
gpucompare --help
```

or with `Poetry`:

```bash
poetry run gpucompare --help
```

## Working

```bash
$ gpucompare --help

 Usage: gpucompare [OPTIONS]                                                                                
                                                                                                            
 Compare GPUs                                                                                               
                                                                                                            
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --csv-data          TEXT  CSV file containing row-wise GPU data           [default: None] [required]  │
│                                                                                                          │
│                              Possible columns:                                                           │
│                              gpu_name (str): name of gpu  [required]                                     │
│                              architecture (str): GPU architecture                                        │
│                              cuda_cores (int): number of cuda cores                                      │
│                              fp32_perf (float): fp32 performance in TFLOPS                               │
│                              fp16_perf (float): fp16 performance in TFLOPS                               │
│                              int8_perf (float): int8 performance in TOPS                                 │
│                              mem (float): gpu memory in GiB                                              │
│                              mem_bandwidth (float): memory bandwidth in GB/s                             │
│    --version   -v            Prints the version of the gpucompare package.                               │
│    --help                    Show this message and exit.                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

```bash
$ gpucompare --csv-data assets/gpu_data.csv
# gpu_data.csv
# gpu_name,architecture,int8_perf,mem_bandwidth
# A2,ampere,36,200
# A10,ampere,250,600
# A30,ampere,330,933
{'A10/A2': '3.0x', 'A30/A2': '4.67x'}
```

## Contributing

Thanks for considering contributing to this project. Please follow [Contributing guidelines](https://github.com/kHarshit/gpucompare/blob/master/CONTRIBUTING.md).

## 🛡 License

[![License](https://img.shields.io/github/license/kHarshit/gpucompare)](https://github.com/kHarshit/gpucompare/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/kHarshit/gpucompare/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{gpucompare,
  author = {kHarshit},
  title = {Compare GPUs},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kHarshit/gpucompare}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
