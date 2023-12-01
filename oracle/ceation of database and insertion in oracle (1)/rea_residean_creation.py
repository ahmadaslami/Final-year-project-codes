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
position = """ CREATE TABLE real_residence (
        real_residence_id NUMBER PRIMARY KEY, 
        province_id  NUMBER,
        FOREIGN KEY (province_id) REFERENCES province (province_id),
        district_id  NUMBER,
        FOREIGN KEY (district_id) REFERENCES district (district_id),
        village_id  NUMBER,
        FOREIGN KEY (village_id) REFERENCES village (village_id))"""

print((cursor.execute(position)))



connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
