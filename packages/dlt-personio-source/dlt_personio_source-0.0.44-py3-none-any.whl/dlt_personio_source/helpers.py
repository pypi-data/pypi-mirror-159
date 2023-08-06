from dlt.pipeline import Pipeline, PostgresPipelineCredentials
from dlt.pipeline.typing import GCPPipelineCredentials
import os

def save_schema(p, fn):
    schema_yaml = p.get_default_schema().as_yaml(remove_defaults=True)
    f = open(f'{fn}.yml', "w")
    f.write(schema_yaml)
    f.close()

def load(data=[],
            table_name='mytbl',
            schema_name='mypipe',
            credentials = {},
            schema_infile=None,
            schema_outfile=None,
            dry_run=False):

    if isinstance(credentials, dict):
        cred = GCPPipelineCredentials.from_services_dict(credentials, dataset_prefix=schema_name[0])
    elif isinstance(credentials, list):
        if credentials[0] == 'redshift':
            cred = PostgresPipelineCredentials(*credentials)


    p = Pipeline(schema_name[1:])
    if schema_infile:
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_path, f"{schema_infile}.yml")
        schema_infile = Pipeline.load_schema_from_file(file_path)
    p.create_pipeline(cred, schema=schema_infile)
    p.extract(data, table_name=table_name)
    p.unpack()
    if schema_outfile:
        save_schema(p, schema_outfile)
    if not dry_run:
        p.load()