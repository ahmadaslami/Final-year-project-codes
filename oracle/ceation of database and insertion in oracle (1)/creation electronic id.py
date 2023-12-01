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
cursor = connection.cursor()
# Create an instance of Faker
# SQL statement to create the "employee" table
position = """ CREATE TABLE electronic_idcard (
        electronic_id_card   NUMBER PRIMARY KEY, 
        idcard_number number)"""

print((cursor.execute(position)))


connection.commit()

cursor.close()
connection.close()
