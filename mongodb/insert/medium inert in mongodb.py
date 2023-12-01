import random
from faker import Faker
from pymongo import MongoClient
from PIL import Image
import io

import pymongo
from PIL import Image
import io
import random
import os
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['NSIA']
collection = db['village1']

# Create a Faker instance
fake = Faker()
province_collection = db['province']
district_collection = db['district']



province_ids = [province_doc['_id'] for province_doc in province_collection.find({}, {'_id': 1})]
district_ids = [district_doc['_id'] for district_doc in district_collection.find({}, {'_id': 1})]

part1 = 1200
part2 = 200
part3 = 1

def generate_student_id():
    global part1, part2, part3

    # Increment part3 and handle rollover
    part3 += 1
    if part3 > 70:
        part3 = 1
        part2 += 1
        if part2 > 230:
            part2 = 200
            part1 += 1
            if part1 > 1900:
                raise Exception("Citizen ID range exceeded")

    return f"{part1}-{part2}-{part3}"

num_students =10  # Adjust the number of students you want to generate
  # Adjust the number of students you want to generate

for _ in range(num_students):
    province_id = fake.random.choice(province_ids)
    District_id = fake.random.choice(district_ids)
    data = {
        "citizen_id": generate_student_id(),
        "Province_id":province_id,
        "District_id":District_id

    }
    collection.insert_one(data)

# Close the MongoDB connection
client.close()
