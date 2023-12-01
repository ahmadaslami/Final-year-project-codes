from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


province_collection = db['date_of_birth'] ## this is the table

# Instantiate Faker
fake = Faker() ## the method generated the fake data

# Generate dummy data for the class collection
province_documents = []
for _ in range(1):
    province_document = {
        'birth_date': fake.date()
    }
    province_documents.append(province_document)

# Insert the class documents into the "class" collection
province_collection.insert_many(province_documents)


client.close()
