import cx_Oracle
import random
from faker import Faker

# Establish a connection to the Oracle database
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)
# Create a cursor object to execute SQL statements
# Create an instance of Faker
# SQL statement to create the "employee" table
cursor = connection.cursor()

position = """ CREATE TABLE nsia_confirmation (
        nsia_confirmation_id   NUMBER PRIMARY KEY, 
        name VARCHAR(250),
        user_type VARCHAR(250),
        ID_Card_NO number,
        family_id  NUMBER,
        FOREIGN KEY (family_id) REFERENCES family_citizen (family_id),
        signature_NSIA_confirmer_id  NUMBER,
        FOREIGN KEY (signature_NSIA_confirmer_id) REFERENCES signature_NSIA_confirmer (signature_NSIA_confirmer_id))"""

print((cursor.execute(position)))

connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
