from pymongo import MongoClient
from faker import Faker
import random
fake = Faker()
client = MongoClient('mongodb://localhost:27017')
db = client['NSIA']
civil_status_collection = db['civil_status']
civil_status = ['single','married','cocoanut','divorce']
civil_status_documents = []
for _ in range(5):
    civil_status_document = {
        'civil_status': random.choice(civil_status)}
    civil_status_documents.append(civil_status_document)
civil_status_collection.insert_many(civil_status_documents)
client.close()
