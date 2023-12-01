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
cursor = connection.cursor()
# Create an instance of Faker
# SQL statement to create the "employee" table
position = """ CREATE TABLE self_confirmation (
        self_confirmation_id  NUMBER PRIMARY KEY, 
        date1 date,
        signature_citizen_id  NUMBER,
        FOREIGN KEY (signature_citizen_id) REFERENCES signature_citizen (signature_citizen_id),
        finger_print_citizen_id   NUMBER,
        FOREIGN KEY (finger_print_citizen_id) REFERENCES finger_print_citizen (finger_print_citizen_id))"""

print((cursor.execute(position)))



connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
