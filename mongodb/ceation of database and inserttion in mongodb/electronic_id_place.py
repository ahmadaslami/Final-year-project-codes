from pymongo import MongoClient
from faker import Faker

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Specify the database and collection names
db = client['NSIA']


paper_id_pace_collection = db['electronic_id_place'] # this is the table
province_collection = db['province']
district_collection = db['district']

# Instantiate Faker
fake = Faker() # the method generated the fake data


paper_id_pace_documents = []
district_ids = [district_doc['_id'] for district_doc in district_collection.find({}, {'_id': 1})]
province_ids = [province_doc['_id'] for province_doc in province_collection.find({}, {'_id': 1})]

for _ in range(100000):
    paper_id_pace_document = {
        'date': fake.date(),
        'province_id': fake.random.choice(province_ids),
        'district': fake.random.choice(district_ids),
    }
    paper_id_pace_documents.append(paper_id_pace_document)

# Insert the student documents into the "student" collection
paper_id_pace_collection.insert_many(paper_id_pace_documents)

# Close the MongoDB connection
client.close()
