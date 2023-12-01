from pymongo import MongoClient
from faker import Faker
client = MongoClient('mongodb://localhost:27017')
db = client['NSIA']
second_nature_collection = db['second_nature']
fake = Faker()
second_nature_documents = []
for _ in range(300):
    second_nature_document = {
        'country_name': fake.country() }
    second_nature_documents.append(second_nature_document)
second_nature_collection.insert_many(second_nature_documents)
client.close()
