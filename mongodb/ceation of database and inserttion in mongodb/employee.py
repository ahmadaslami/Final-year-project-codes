from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


village_collection = db['Employee'] # this is the table
district_collection = db['position']

# Instantiate Faker
fake = Faker() # the method generated the fake data


village_documents = []
district_ids = [district_doc['_id'] for district_doc in district_collection.find({}, {'_id': 1})]

for _ in range(2):
    village_document = {
        'first_name': fake.name(),
        'last_name': fake.name(),
        'father_name': fake.name(),
        'IDCard_no': fake.name(),
        'position_id': fake.random.choice(district_ids)
    }
    village_documents.append(village_document)

# Insert the student documents into the "student" collection
village_collection.insert_many(village_documents)

# Close the MongoDB connection
client.close()
