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

position = """ CREATE TABLE signature_nsia_confirmer (
        signature_NSIA_confirmer_id   NUMBER PRIMARY KEY, 
        photo BLOB)"""

print((cursor.execute(position)))

connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
