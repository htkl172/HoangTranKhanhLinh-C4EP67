from faker import Faker
import pymongo
from bson import ObjectId
faker = Faker()

new_data = []
for i in range(100):
    data = {
        'name' = faker.name(),
        'address' = faker.address(),
        'phone' = faker.phone_number()
    }
    new_data.append(data)