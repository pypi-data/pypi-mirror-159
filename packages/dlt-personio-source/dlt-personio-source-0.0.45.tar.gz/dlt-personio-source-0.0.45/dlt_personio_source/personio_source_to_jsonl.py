#used to export the dummy data
import jsonlines
from personio_source import PersonioSource

#get credentials at this url - replace"test-1" with your org name
#https://test-1.personio.de/configuration/api/credentials/management

p = PersonioSource(client_id='',
               client_secret='')

schema_prefix = 'raw'
schema_name = 'personio'

tables = p.tasks()

for table in tables:
    with jsonlines.open(f"{table['table_name']}.jsonl", mode='w') as writer:
        writer.write_all(table['data'])
