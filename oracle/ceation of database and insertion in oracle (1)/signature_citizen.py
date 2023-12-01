import cx_Oracle
import os
import random

from faker import Faker

# Establish a connection to the Oracle database
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)


# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Create an instance of Faker
fake = Faker()  # Set the locale to generate Afghan Persian (Dari) fake data


def insert_photos_from_folder(folder_path, num_rows):
    photo_files = [f for f in os.listdir(folder_path) if
                   f.endswith('.jpg')]  # Replace '.jpg' with the file extension you have

    for signature_citizen_id in range(num_rows):
        random_photo = random.choice(photo_files)
        with open(os.path.join(folder_path, random_photo), 'rb') as photo_file:
            photo_data = photo_file.read()
            # Generate a random ID
            cursor.execute(
                "INSERT INTO signature_citizen (signature_citizen_id, photo) VALUES (:id, :photo_data)",
                id=signature_citizen_id, photo_data=photo_data)


your_folder_path = "E:\Every thing\Mobile Applications\image2"
num_rows_to_insert = 1000

insert_photos_from_folder(your_folder_path, num_rows_to_insert)
connection.commit()

cursor.close()
connection.close()
