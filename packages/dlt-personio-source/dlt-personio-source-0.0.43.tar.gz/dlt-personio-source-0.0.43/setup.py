# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dlt_personio_source']

package_data = \
{'': ['*'], 'dlt_personio_source': ['sample_data/*']}

install_requires = \
['personio-py>=0.2.1,<0.3.0', 'python-dlt']

setup_kwargs = {
    'name': 'dlt-personio-source',
    'version': '0.0.43',
    'description': '',
    'long_description': '# dlt-personio-source\n\n\n# Parent tables \n```\n\'employees\', \n\'absences\', \n\'absence_types\', \n\'attendances\'\n```\nsome of these tables have sub-tables\n\nto join the parent table to the sub table, use the join `parent.dlt_id = child.parent_dlt_id`\n\n# Usage\ninstall library\n\n```pipx install dlt-personio-source```\nif the library cannot be found, ensure you have the required python version as per the `pyproject.toml`file.\n\nRun the source as below to load a sample data set.\n\nAdd credentials and remove the `dummy_data` flag to enable loading your data.\n\n\n```\nfrom dlt_personio_source import load_personio_tables\n\ncreds = {\n  "type": "service_account",\n  "project_id": "zinc-mantra-353207",\n  "private_key_id": "example",\n  "private_key": "",\n  "client_email": "example@zinc-mantra-353207.iam.gserviceaccount.com",\n  "client_id": "100909481823688180493"}\n\n```\nserial load:\n```\ntables = [\'employees\', \'absences\', \'absence_types\', \'attendances\']\nload_personio_tables(client_id=\'\',\n                     client_secret=\'\',\n                     target_credentials=creds,\n                     tables = tables,\n                     schema_name=\'personio_raw\',\n                     dummy_data = True)\n\n```\nfor parallel load, create airflow tasks for each table such as:\n```\ntables = [\'employees\', \'absences\', \'absence_types\', \'attendances\']\nfor table in tables:\n    load_personio_tables(client_id=\'\',\n                         client_secret=\'\',\n                         target_credentials=creds,\n                         tables = [table],\n                         schema_name=\'personio_raw\',\n                         dummy_data = True)\n\n```',
    'author': 'Adrian Brudaru',
    'author_email': 'adrian@scalevector.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
