from bigquery import get_bq_client,run_query
from processing import dictionary_conversation,seed_fake_data,create_parameters_for_tx_funcs
from neo4j import Neo4j,create_client,create_address,create_marital,create_account
from neo4j import create_payment1,create_payment2,create_payment3,create_payment4,create_payment5,create_payment6

'''
CONFIGURATION
'''
uri = 'bolt://35.203.107.99:7687'
username = 'neo4j'
database = 'neo4j'
password = 'test'
query = (
    'SELECT *  FROM `bigquery-public-data.ml_datasets.credit_card_default`'
    'LIMIT 10000')



'''
Bq + Neo Clients
'''
bq_client = get_bq_client()
neo_client = Neo4j(url=uri,username=username,database=database,password=password)



'''
ETL processing 
'''
google_Rows = run_query(bq_client,query=query)
list_of_dictionaries = dictionary_conversation(google_Rows)
base_data = seed_fake_data(list_of_dictionaries)


'''
Ingesting into neo4j 
'''

client_params = create_parameters_for_tx_funcs(base_data,['id','age','full_name','sex'])
marital_params =create_parameters_for_tx_funcs(base_data,['id','marital_status'])
address_params = create_parameters_for_tx_funcs(base_data,['id','address'])
account_params = create_parameters_for_tx_funcs(base_data,['id','account_id','limit_balance','default_payment_next_month'])
create_payment1_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_1'])
create_payment2_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_2'])
create_payment3_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_3'])
create_payment4_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_4'])
create_payment5_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_5'])
create_payment6_params = create_parameters_for_tx_funcs(base_data,['account_id','pay_amt_6'])


neo_client.write(tx_func=create_client,parameters=client_params)
neo_client.write(tx_func=create_address,parameters=address_params)
neo_client.write(tx_func=create_marital,parameters=marital_params)
neo_client.write(tx_func=create_account,parameters=account_params)
neo_client.write(tx_func=create_payment1,parameters=create_payment1_params)
neo_client.write(tx_func=create_payment2,parameters=create_payment2_params)
neo_client.write(tx_func=create_payment3,parameters=create_payment3_params)
neo_client.write(tx_func=create_payment4,parameters=create_payment4_params)
neo_client.write(tx_func=create_payment5,parameters=create_payment5_params)
neo_client.write(tx_func=create_payment6,parameters=create_payment6_params)






