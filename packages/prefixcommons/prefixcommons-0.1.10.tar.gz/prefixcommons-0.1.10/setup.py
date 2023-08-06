# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prefixcommons']

package_data = \
{'': ['*'], 'prefixcommons': ['registry/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'pytest-logging>=2015.11.4,<2016.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'prefixcommons',
    'version': '0.1.10',
    'description': 'A python API for working with ID prefixes',
    'long_description': "prefixcommons\n=============\n\nA python API for working with ID prefixes in the context of\n`prefixcommons <http://prefixcommons.org>`__\n\nCurrent functionality: Uses JSON-LD contexts to expand and contract\nCURIEs to URIs\n\nE.g. GO:0008150 <=> http://purl.obolibrary.org/obo/GO\\_0008150\n\nExample\n=======\n\n::\n   \n   >>> from prefixcommons import contract_uri\n   >>> print(contract_uri('http://purl.obolibrary.org/obo/GO_0008150'))\n   ['GO:0008150']\n   \n   >>> from prefixcommons import expand_uri\n   >>> print(expand_uri('GO:000850'))\n   http://purl.obolibrary.org/obo/GO_0008150\n\nThe above uses standard JSON-LD context files from \n`prefixcommons/biocontext <https://github.com/prefixcommons/biocontext>`__\n\nYou can pass your own\n\n::\n\n   >>> cmaps = [{'GO': 'http://purl.obolibrary.org/obo/GO_'}]\n   >>> print(contract_uri('http://purl.obolibrary.org/obo/GO_0008150'), cmaps)\n   ['GO:0008150']\n\n",
    'author': 'cmungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/prefixcommons/prefixcommons-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
