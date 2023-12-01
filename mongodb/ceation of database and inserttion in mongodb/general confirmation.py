import random
from datetime import datetime, timedelta
from faker import Faker
import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["abid"]  # Replace "your_database_name" with the actual name of your database
collection = db["general_confirmation"]
electronic_idcard_table = db["electronic_idcard"]
paper_id_table = db["paper_id"]
finger_print_confirmer_table = db["finger_print_confirmer"]
signature_confirmer_table = db["signature_confirmer"]

# Create an instance of Faker
fake = Faker()

# Generate and insert data 10 times
for _ in range(3):

    # Randomly select a signature_citizen ID or finger_print_citizen ID
    if random.choice([True, False]):
        # Select a random signature_citizen ID from the signature_citizen table
        electronic_idcard_document = electronic_idcard_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        finger_print_confirmer_document = finger_print_confirmer_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        electronic_idcard_id = electronic_idcard_document["_id"]
        finger_print_confirmer_id = finger_print_confirmer_document["_id"]
        paper_id_id = None
        signature_confirmer_id = None
    else:
        # Select a random finger_print_citizen ID from the finger_print_citizen table
        paper_id_document = paper_id_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        signature_confirmer_document = signature_confirmer_table.aggregate([{ "$sample": { "size": 1 }}]).next()
        paper_id_id = paper_id_document["_id"]
        signature_confirmer_id = signature_confirmer_document["_id"]
        electronic_idcard_id = None
        finger_print_confirmer_id = None




    # Create the document to be inserted
    document = {
        "firstname": fake.word(),
        "lastname": fake.word(),
        "father_name": fake.word(),
        "father_lastname": fake.word(),
        "electronic_idcard_id": electronic_idcard_id,
        "finger_print_confirmer_id": finger_print_confirmer_id,
        "paper_id_id": paper_id_id,
        "signature_confirmer_id": signature_confirmer_id,
    }

    # Insert the document into the collection
    collection.insert_one(document)

# Close the MongoDB connection
client.close()
