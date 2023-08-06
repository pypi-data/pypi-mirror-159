# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dcmstudyclean']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'simplejson>=3.17.6,<4.0.0',
 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['dcmstudyclean = dcmstudyclean.script:cli']}

setup_kwargs = {
    'name': 'dcmstudyclean',
    'version': '0.2.0',
    'description': 'Clean dicom files into folders seperated by study id name and then create json files with key information',
    'long_description': None,
    'author': 'ryanapfel',
    'author_email': 'rapfel@usc.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
