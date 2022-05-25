from faker import Faker
from random import randint

def dictionary_conversation(rows):
    '''
    Converts the bigquery.RowIterator object into a list of dictionaries.
    Simply makes it easier to manipulate and pre-process
    :param rows:
    :return:
    '''
    rows =  [dict(row) for row in rows]
    return rows



def generate_faker_grainular_data(dictionary):
    '''
    I'm using random.randint. That's kind of a lazy way to approach creating an id
    :param dictionary:
    :return:
    '''
    faker = Faker()
    full_name = faker.name()
    address = faker.address()
    account_id = randint(0,10000)
    # I wonder if I can use reflection to make this less painful..
    faker_fields = [{'full_name': full_name, "address": address,"account_id":account_id}]
    for field in faker_fields:
        for key,value in field.items():
            dictionary[key] = value

    return dictionary



def seed_fake_data(rows):
    faker_data =[generate_faker_grainular_data(dictionary) for dictionary in rows]
    return faker_data




def create_parameters_for_tx_funcs(list_of_dictionarites,cols):
    sub_dictionaries = []
    for _dict in list_of_dictionarites:
        subdictionary = {k:v for k,v in _dict.items() if k in cols}
        sub_dictionaries.append(subdictionary)
    return {'parameters':sub_dictionaries}






