from google.cloud import bigquery
from google.oauth2 import service_account
import os



def get_bq_client():
    '''

    :return: bq.client Object
    '''
    service_account_path_obj = os.path.normpath(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    credentials = service_account.Credentials.from_service_account_file(service_account_path_obj)
    client = bigquery.Client(credentials=credentials,project=credentials.project_id)
    return client

def run_query(client:bigquery.Client,query:str=None):
    '''

    :param client:
    :param query:
    :return:
    '''
    query_job = client.query(query)
    rows = query_job.result()
    return rows
