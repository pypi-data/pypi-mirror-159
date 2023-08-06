# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labpacks']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'kubernetes>=23.6.0,<24.0.0',
 'psutil>=5.9.1,<6.0.0',
 'pulumi-ml>=0.1.5,<0.2.0',
 'pulumi>=3.33.2,<4.0.0',
 'pytest-kind>=21.1.3,<22.0.0',
 'pytest>=7.1.2,<8.0.0',
 'requests>=2.27.1,<3.0.0',
 'rootpath>=0.1.1,<0.2.0',
 'types-requests>=2.27.30,<3.0.0']

setup_kwargs = {
    'name': 'labpacks',
    'version': '0.1.9',
    'description': 'Easy creation of machine learning labs',
    'long_description': None,
    'author': 'Patrick Barker',
    'author_email': 'pbarker@onemedical.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
