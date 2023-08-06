# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esg_matching',
 'esg_matching.data_source',
 'esg_matching.engine',
 'esg_matching.engine.builders',
 'esg_matching.engine.connectors',
 'esg_matching.engine.sql',
 'esg_matching.exceptions',
 'esg_matching.file_reader',
 'esg_matching.matcher',
 'esg_matching.processing',
 'esg_matching.report']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.21',
 'cx_Oracle>=8.3.0',
 'pandas>=1.4.0',
 'sqlalchemy-trino>=0.4.1']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'esg-matching',
    'version': '0.2.0',
    'description': 'Entity matching of several data sources',
    'long_description': '# esg-matching\n\nThe esg-matching is a library that is part of the Entity-Matching project developed by OS-Climate Foundation. \nIts main purpose is to provide methods to match entities from different data sources.\n\nCurrently, the library provides three main components:\n- a database engine which can connect to a local Sql-lite database or an Oracle database elsewhere\n- a file reader which can read data sources in csv format and load its content to a database\n- a database-driven matcher which can perform exact matching based on database queries. Three types of matchings are provided: direct, residual and indirect matching.\n\n## Install from PyPi\n\n```\npip install esg-matching\n```',
    'author': 'Os-Climate Foundation',
    'author_email': 'test_os-climate@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/os-climate/esg-matching',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
