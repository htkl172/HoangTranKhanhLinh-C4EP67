import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']
customer_collection = db['customer']

#CREATE
new_data = [
    {
    'name': 'Long',
    'age': 20,
    'address': 'Chua Lang',
    'ref': 'ads' },
    {
    'name': 'Lan',
    'age': 21,
    'address': 'Chua Lang',
    'ref': 'ads' },
    {
    'name': 'Lam',
    'age': 23,
    'address': 'Chua Lang',
    'ref': 'ads' },

]
customer_collection.insert_many(new_data)
customer_collection.insert_one({
    'name': 'Linh',
    'age': 22,
    'address': 'Chua Lang',
    'ref': 'ads' 
})


# READ
data = customer_collection.find_one({'_id': ObjectId('5e5520431649d6acb6de11f6')})
# lt: LITTLE THAN, gt: GREATER THAN
# find_one: TIM RA TH DAU TIEN, SX THEO THU TU NGAU NHIEN
print(data)
# for customer in data:
#     print(customer)

#UPDATE
customer_collection.update_one({
    'id': ObjectId('5e5520431649d6acb6de11f6')
    },
    {
        '$set': {
            'name': 'Khong phai Phuong'
        }
        
    }
)

# DELETE

customer_collection.delete_one({'_id': ObjectId('5b5bfa32a2daff0bbc7e4a35')})
customer_collection.find_one({'_id': ObjectId('5b5bfa32a2daff0bbc7e4a35')})

#FAKE
from faker import Faker

fake = Faker()
# name = fake.name()
# address = fake.address()
# job = fake.job()
# cc = fake.credit_card_number()

# for i in range(100):
#     fake_info = {
#     'name': name,
#     'address': address,
#     'job': job,
#     'credit card number': cc
#     }
#     fake_data = []
#     fake_data.append(fake_info)
# customer_collection.insert_many(fake_data)
new_data = []
for i in range(100):
    data = {
        'name': fake.name(),
        'address': fake.address(),
        'phone': fake.phone_number()
    }
    new_data.append(data)
customer_collection.insert_many(new_data)
print(new_data)