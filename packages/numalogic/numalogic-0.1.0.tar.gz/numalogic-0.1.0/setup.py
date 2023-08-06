# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numalogic',
 'numalogic.models',
 'numalogic.models.autoencoder',
 'numalogic.models.autoencoder.variants',
 'numalogic.models.forecast',
 'numalogic.models.forecast.variants',
 'numalogic.preprocess',
 'numalogic.registry',
 'numalogic.synthetic',
 'numalogic.tests',
 'numalogic.tests.models',
 'numalogic.tests.models.autoencoder',
 'numalogic.tests.models.autoencoder.variants',
 'numalogic.tests.models.forecast',
 'numalogic.tests.preprocess',
 'numalogic.tests.registry',
 'numalogic.tests.synthetic',
 'numalogic.tests.tools',
 'numalogic.tools']

package_data = \
{'': ['*'], 'numalogic.tests': ['resources/data/*']}

install_requires = \
['mlflow-skinny>=1.27.0,<2.0.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pytz>=2022.1,<2023.0',
 'scikit-learn>=1.0,<2.0',
 'torch>=1.12.0,<2.0.0',
 'torchinfo>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'numalogic',
    'version': '0.1.0',
    'description': 'Collection of operational Machine Learning models and tools.',
    'long_description': None,
    'author': 'Numalogic Developers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
