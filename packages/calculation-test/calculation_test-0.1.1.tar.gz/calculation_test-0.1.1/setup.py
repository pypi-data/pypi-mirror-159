# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calculation_test']

package_data = \
{'': ['*']}

install_requires = \
['ExifRead>=2.3.2,<3.0.0',
 'addict==2.4.0',
 'geographiclib==1.50',
 'helper-mapilio>=1.1.31,<2.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.23.1,<2.0.0',
 'opencv-python>=4.5.1.48,<5.0.0.0',
 'pandas',
 'pytz>=2021.1,<2022.0',
 'requests>=2.25.1,<3.0.0',
 'scipy>=1.8.1,<2.0.0',
 'solve>=0.0.0,<0.0.1',
 'trianglesolver>=1.2,<2.0']

setup_kwargs = {
    'name': 'calculation-test',
    'version': '0.1.1',
    'description': 'mapilio calculation',
    'long_description': '# DENEME\n',
    'author': 'Kadir Coşar',
    'author_email': 'kadircosarnew@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
