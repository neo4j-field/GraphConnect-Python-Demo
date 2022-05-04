from BigQuery import get_bq_client,run_query
from Processing import dictionary_conversation,generate_faker_grainular_data,seed_fake_data



query = (
    'SELECT *  FROM `bigquery-public-data.ml_datasets.credit_card_default`'
    'LIMIT 100')


client = get_bq_client()
google_Rows = run_query(client,query=query)
list_of_dictionaries = dictionary_conversation(google_Rows)
print(seed_fake_data(list_of_dictionaries))