from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file("")
client = bigquery.Client(project='bigquery-public-data',credentials=None)

QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')



query_job = client.query(QUERY)
rows = query_job.results()

for row in rows:
    print(row)



