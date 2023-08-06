# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['environment']

package_data = \
{'': ['*']}

install_requires = \
['setuptools>=33.0.0']

setup_kwargs = {
    'name': 'nr.python.environment',
    'version': '0.1.2',
    'description': '',
    'long_description': '# nr.python.environment\n\nUtilities to work with Python environments.\n\n### API\n\n*function* __`nr.python.environment.distributions.get_distributions(): Dict[str, Distribution]`__\n\nReturns all distributions that can be found in the current Python environment. This can be useful to build a dependency\ngraph or to collect the license of all packages used.\n',
    'author': 'Unknown',
    'author_email': 'me@unknown.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
