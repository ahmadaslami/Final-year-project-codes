import random
from datetime import datetime, timedelta
from faker import Faker
import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["NSIA"]  # Replace "your_database_name" with the actual name of your database
collection = db["self_confirmation"]
signature_citizen_table = db["signature_citizen"]
finger_print_citizen_table = db["finger_print_citizen"]

# Create an instance of Faker
fake = Faker()

# Generate and insert data 10 times
for _ in range(100):

    # Randomly select a signature_citizen ID or finger_print_citizen ID
    if random.choice([True, False]):
        # Select a random signature_citizen ID from the signature_citizen table
        signature_citizen_document = signature_citizen_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        signature_citizen_id = signature_citizen_document["_id"]
        finger_print_citizen_id = None
    else:
        # Select a random finger_print_citizen ID from the finger_print_citizen table
        finger_print_citizen_document = finger_print_citizen_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        finger_print_citizen_id = finger_print_citizen_document["_id"]
        signature_citizen_id = None

    # Create the document to be inserted
    document = {
        "date": fake.date(),
        "signature_citizen_id": signature_citizen_id,
        "finger_print_citizen_id": finger_print_citizen_id
    }

    # Insert the document into the collection
    collection.insert_one(document)

# Close the MongoDB connection
client.close()
