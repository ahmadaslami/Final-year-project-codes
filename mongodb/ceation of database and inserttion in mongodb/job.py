from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


job_collection = db['job'] # this is the table

# Instantiate Faker
fake = Faker() # the method generated the fake data

# Generate dummy data for the class collection
job_documents = []
for _ in range(10000000):
    job_document = {
        'job_name': fake.word()
    }
    job_documents.append(job_document)

# Insert the class documents into the "class" collection
job_collection.insert_many(job_documents)
client.close()
