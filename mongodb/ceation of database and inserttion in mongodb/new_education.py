from pymongo import MongoClient
from faker import Faker
import random

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['N']

edu = ['master','doctor','bachelor','14_pass','school_graduated','primary_education','no_education']
province_collection = db['education'] ## this is the table

# Instantiate Faker
fake = Faker() ## the method generated the fake data

# Generate dummy data for the class collection
province_documents = []
for _ in range(1000):
    province_document = {
        'edu': random.choice(edu)
    }
    province_documents.append(province_document)

# Insert the class documents into the "class" collection
province_collection.insert_many(province_documents)
# Close the MongoDB connection
client.close()
