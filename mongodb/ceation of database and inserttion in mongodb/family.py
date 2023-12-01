from faker import Faker
import pymongo
import random

# Create an instance of Faker
fake = Faker()

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["abid"]  # Replace "your_database_name" with the actual name of your database
family_collection = db["family"]
image_collection = db["signature_citizen"]
second_nature_table = db["second_nature"]

# Generate and insert data
for _ in range(100):
    firstname = fake.first_name()
    lastname = fake.last_name()
    fathername = fake.first_name()
    relationship = fake.random_element(elements=('Parent', 'Sibling', 'Spouse', 'Child'))
    death = fake.random_element(elements=('death', 'no death'))
    Request_of_Electronictazkare = fake.random_element(elements=('yes', 'no'))
    grandfather_frist_name = fake.first_name()
    grandfather_last_name = fake.last_name()
    fathername1= fake.random_element(elements=('male','female'))

    grandfather_name = f"{grandfather_frist_name}{grandfather_last_name}"
    date = fake.date()

    # Retrieve a random image from the image collection
    random_image = image_collection.aggregate([{"$sample": {"size": 1}}]).next()
    image_reference = random_image["_id"]

    # Randomly select a second_nature ID or set it to None
    if random.choice([True, False]):
        second_nature_document = second_nature_table.aggregate([{"$sample": {"size": 1}}]).next()
        second_nature_id = second_nature_document["_id"]
    else:
        second_nature_id = None

    # Create the document to be inserted into the family collection
    family_document = {
        "firstname": firstname,
        "lastname": lastname,
        "fathername": fathername,
        "relationship": relationship,
        "death": death,
        "Request_of_Electronictazkare": Request_of_Electronictazkare,
        "grandfather_name": grandfather_name,
        "date": date,
        "image": image_reference,
        "second_nature_id": second_nature_id,
        "gender":fathername1
    }

    # Insert the document into the family collection
    family_collection.insert_one(family_document)

# Close the MongoDB connection
client.close()
