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
position = """ CREATE TABLE district (
        district_id NUMBER PRIMARY KEY, 
        name VARCHAR(250),
        province_id  NUMBER,
        FOREIGN KEY (province_id) REFERENCES province (province_id))"""

print((cursor.execute(position)))



connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
