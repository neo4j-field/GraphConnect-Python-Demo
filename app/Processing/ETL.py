from faker import Faker


def dictionary_conversation(rows):
    '''
    Converts the BigQuery.RowIterator object into a list of dictionaries.
    Simply makes it easier to manipulate and pre-process
    :param rows:
    :return:
    '''
    rows =  [dict(row) for row in rows]
    return rows



def generate_faker_grainular_data(dictionary):
    faker = Faker()
    full_name = faker.name()
    first_name,last_name = full_name.split()
    address = faker.address()

    # I wonder if I can use reflection to make this less painful..
    faker_fields = [{'full_name': full_name, "first_name": first_name, "last_name": last_name, "address": address}]

    for key,value in faker_fields:
        dictionary[key] = value

    return dictionary



def seed_fake_data(rows):
    faker_data =[generate_faker_grainular_data(dictionary) for dictionary in rows]
    return faker_data






