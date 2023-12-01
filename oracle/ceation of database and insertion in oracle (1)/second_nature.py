import cx_Oracle
import random
from faker import Faker
import os
# Establish a connection to the Oracle database
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)


# Create a cursor object to execute SQL statements
cursor = connection.cursor() # Replace with the actual path

# Create an instance of Faker
fake = Faker()
for se_na_id in range(50):
    # Generate fake data
    name_country = fake.country()
    cursor.execute("""
        INSERT INTO second_nature  (se_na_id,name_country)
        VALUES (:se_na_id, :name_country)
    """, {
        'se_na_id':se_na_id,
        'name_country': name_country
    })

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
