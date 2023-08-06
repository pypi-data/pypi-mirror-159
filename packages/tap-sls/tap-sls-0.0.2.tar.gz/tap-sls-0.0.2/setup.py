# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_sls', 'tap_sls.tests']

package_data = \
{'': ['*'], 'tap_sls': ['schemas/*']}

install_requires = \
['aliyun-log-python-sdk>=0.7.12,<0.8.0',
 'requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['tap-sls = tap_sls.tap:TaptapSls.cli']}

setup_kwargs = {
    'name': 'tap-sls',
    'version': '0.0.2',
    'description': '`tap-tap-sls` is a Singer tap for tap-sls, built with the Meltano SDK for Singer Taps.',
    'long_description': None,
    'author': 'FirstName LastName',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
