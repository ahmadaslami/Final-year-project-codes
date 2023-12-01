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
position = """ CREATE TABLE paper_id_place (
        paper_place_id  NUMBER PRIMARY KEY, 
        province_id  NUMBER,
        FOREIGN KEY (province_id) REFERENCES province (province_id),
        district_id  NUMBER,
        FOREIGN KEY (district_id) REFERENCES district (district_id),
        date1 date)"""

print((cursor.execute(position)))



connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
