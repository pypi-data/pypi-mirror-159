# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rareeventestimation',
 'rareeventestimation.enkf',
 'rareeventestimation.era',
 'rareeventestimation.evaluation',
 'rareeventestimation.problem',
 'rareeventestimation.sis']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.1,<10.0.0',
 'argparse>=1.4.0,<2.0.0',
 'matlab>=0.1,<0.2',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.2,<2.0.0',
 'plotly>=5.8.0,<6.0.0',
 'prettytable>=3.3.0,<4.0.0',
 'scipy>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'rareeventestimation',
    'version': '0.1.0',
    'description': 'Estimate rare events with consensus based sampling and other methods.',
    'long_description': '# rareeventestimation\n\nEstimate rare events with consensus based sampling and other methods.\n\n## Installation\n\n```bash\n$ pip install rareeventestimation\n```\n\n## Usage\n\n- TODO\n\n\n## License\n\n`rareeventestimation` was created by Konstantin Althaus. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`rareeventestimation` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\nThis package contains code I have not written myself.\n\n### Code from the Engineering Risk Analysis Group, Technical University of Munich\nAll files in `rareeventestimation/src/era` and `rareeventestimation/src/sis` are\nwritten by the [ERA Group](https://www.cee.ed.tum.de/era/era-group/) and\nlicensed under the MIT license. I have added minor changes.\n\n### Code from Dr. Fabian Wagner\nAll files in `rareeventestimation/src/enkf` and `src/rareeventestimation/problem/diffusion.py` are written by [Dr. Fabian Wagner](https://www-m2.ma.tum.de/bin/view/Allgemeines/FabianWagner). I have added minor changes.\n\n\n\n',
    'author': 'Konstantin Althaus',
    'author_email': 'althaus.konstantin.95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
