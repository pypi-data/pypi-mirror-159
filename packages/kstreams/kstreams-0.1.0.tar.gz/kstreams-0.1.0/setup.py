# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kstreams', 'kstreams.prometheus', 'kstreams.test_utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'aiokafka<1.0',
 'future>=0.18.2,<0.19.0',
 'pkgsettings>=0.12.0,<0.13.0',
 'prometheus-client<1.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'kstreams',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Marcos Schroh',
    'author_email': 'marcos.schroh@kpn.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
