from pymongo import MongoClient
from faker import Faker
import numbers

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


NSIA_confirmation = db['NSIA_confirmation'] # this is the table
family_collection = db['family']
signature_NSIA_Employee_collection = db['signature_NSIA_Employee']

# Instantiate Faker
fake = Faker() # the method generated the fake data


NSIA_confirmation_documents = []
family_ids = [family_doc['_id'] for family_doc in family_collection.find({}, {'_id': 1})]
signature_NSIA_Employee_collection_ids = [signature_NSIA_Employee_doc['_id'] for signature_NSIA_Employee_doc in signature_NSIA_Employee_collection.find({}, {'_id': 1})]

for _ in range(100):
    NSIA_confirmation_document = {
        "name":fake.word(),
        "user_type":fake.word(),
        "ID_Card_NO":fake.random_number(digits=5),
        'family_id': fake.random.choice(family_ids),
        'signature_NSIA_Employee_id': fake.random.choice(signature_NSIA_Employee_collection_ids)
    }
    NSIA_confirmation_documents.append(NSIA_confirmation_document)

# Insert the student documents into the "student" collection
NSIA_confirmation.insert_many(NSIA_confirmation_documents)

# Close the MongoDB connection
client.close()
