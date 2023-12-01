from pymongo import MongoClient
from faker import Faker
import random
# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


job_collection = db['paper_id'] # this is the table

# Instantiate Faker
fake = Faker() # the method generated the fake data

# Generate dummy data for the class collection
job_documents = []
for _ in range(100):
    job_document = {
        'year':fake.date(),
        'volume': fake.random_number(digits=5),
        'page_no': fake.random_number(digits=5),
        'registeration_no': fake.random_number(digits=6),
        'sukuk_no': fake.random_number(digits=5)
    }
    job_documents.append(job_document)

# Insert the class documents into the "class" collection
job_collection.insert_many(job_documents)
client.close()
