from pymongo import MongoClient
from faker import Faker
import random
# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


job_collection = db['position'] # this is the table

# Instantiate Faker
fake = Faker() # the method generated the fake data

# Generate dummy data for the class collection
job_documents = []
for _ in range(100):
    job_document = {
        'position_name':fake.word(),
        'salary': random.randint(10000,150000)
    }
    job_documents.append(job_document)

# Insert the class documents into the "class" collection
job_collection.insert_many(job_documents)
client.close()
