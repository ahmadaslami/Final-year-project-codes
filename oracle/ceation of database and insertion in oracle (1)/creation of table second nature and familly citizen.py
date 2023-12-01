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
position = """ CREATE TABLE second_nature (
        se_na_id NUMBER PRIMARY KEY, 
        name_country VARCHAR(250))"""

print((cursor.execute(position)))


# Create the "student" table with a foreign key constraint
employee = """
    CREATE TABLE family_citizen (
        family_id NUMBER PRIMARY KEY,
        firstname VARCHAR(250),
        lastname VARCHAR(250),
        fname VARCHAR(250),
        relation VARCHAR(250),
        death VARCHAR(250),
        req_taz VARCHAR(250),
        grandfname VARCHAR(250),
        date1 DATE,
        sig BLOB,
        gender VARCHAR(10),
        se_na_id NUMBER,
        FOREIGN KEY (se_na_id) REFERENCES second_nature (se_na_id))"""
cursor.execute(employee)


# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
