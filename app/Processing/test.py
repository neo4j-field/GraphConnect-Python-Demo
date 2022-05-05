from faker import Faker


faker = Faker()
full_name = faker.name()
first_name, last_name = full_name.split(" ")
print(first_name,last_name)