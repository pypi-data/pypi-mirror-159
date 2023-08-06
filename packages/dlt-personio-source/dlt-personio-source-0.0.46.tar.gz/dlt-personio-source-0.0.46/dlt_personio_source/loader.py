
from dlt_personio_source.helpers import load
from dlt_personio_source.personio_source import PersonioSource as P
from dlt_personio_source.personio_source_dummy import PersonioSourceDummy as D



#get credentials at this url - replace"test-1" with your org name
#https://test-1.personio.de/configuration/api/credentials/management

# To test, replace P with D (dummy source with sample data)


# get the tables we can load. Each "table" row is a dict {'table_name':'', 'data':row_generator_function}
# filter them for tables we want only
def load_personio_tables(client_id='',
                         client_secret='',
                         # for target credentials, pass a client_secrets.json or a credential json suitable for your db type.
                         target_credentials={},
                         tables = ['employees', 'absences', 'absence_types', 'attendances'],
                         schema_name = 'personio_raw',
                         dummy_data = False):
    """

    :param client_id:
    :param client_secret:
    :param target_credentials:
    :param tables: ['employees', 'absences'], default all
    :param dummy_data: If set to True, you can load sample data without credentials.
    :return:
    """
    if dummy_data:
        p = D(client_id=client_id,
              client_secret=client_secret)
    else:
        p = P(client_id=client_id,
              client_secret=client_secret)

    tables_to_load = [t for t in p.tasks() if t['table_name'] in tables]
    for table in tables_to_load:
        load(data=table['data'],
                    table_name=table['table_name'],
                    schema_name=schema_name,
                    credentials=target_credentials,
                    #if you want to reset the schema, output it here
                    #schema_outfile='personio_schema',
                    schema_infile='personio_schema',
                    dry_run=False)

        print(f"loaded {table['table_name']}")

