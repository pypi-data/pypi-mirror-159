# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bstadlbauer', 'bstadlbauer.flytekitplugins.dask']

package_data = \
{'': ['*']}

install_requires = \
['dask-kubernetes>=2022.5.2,<2023.0.0',
 'dask[distributed]>=2022.7.0,<2023.0.0',
 'flytekit>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'bstadlbauer.flytekitplugins-dask',
    'version': '0.0.0',
    'description': 'A pure Python flytekit plugin to work with dask clusters',
    'long_description': None,
    'author': 'Bernhard Stadlbauer',
    'author_email': '11799671+bstadlbauer@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
