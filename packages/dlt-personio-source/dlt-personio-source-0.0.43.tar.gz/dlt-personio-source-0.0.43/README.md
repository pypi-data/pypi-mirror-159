# dlt-personio-source


# Parent tables 
```
'employees', 
'absences', 
'absence_types', 
'attendances'
```
some of these tables have sub-tables

to join the parent table to the sub table, use the join `parent.dlt_id = child.parent_dlt_id`

# Usage
install library

```pipx install dlt-personio-source```
if the library cannot be found, ensure you have the required python version as per the `pyproject.toml`file.

Run the source as below to load a sample data set.

Add credentials and remove the `dummy_data` flag to enable loading your data.


```
from dlt_personio_source import load_personio_tables

creds = {
  "type": "service_account",
  "project_id": "zinc-mantra-353207",
  "private_key_id": "example",
  "private_key": "",
  "client_email": "example@zinc-mantra-353207.iam.gserviceaccount.com",
  "client_id": "100909481823688180493"}

```
serial load:
```
tables = ['employees', 'absences', 'absence_types', 'attendances']
load_personio_tables(client_id='',
                     client_secret='',
                     target_credentials=creds,
                     tables = tables,
                     schema_name='personio_raw',
                     dummy_data = True)

```
for parallel load, create airflow tasks for each table such as:
```
tables = ['employees', 'absences', 'absence_types', 'attendances']
for table in tables:
    load_personio_tables(client_id='',
                         client_secret='',
                         target_credentials=creds,
                         tables = [table],
                         schema_name='personio_raw',
                         dummy_data = True)

```