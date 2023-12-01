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
position = """
    CREATE TABLE position (
        position_id NUMBER PRIMARY KEY,
        position_name VARCHAR2(50),
        salary NUMBER 
    )
"""
cursor.execute(position)

# Create the "student" table with a foreign key constraint
employee = """
    CREATE TABLE employee (
        employee_id NUMBER PRIMARY KEY,
        first_name VARCHAR2(250),
        last_name VARCHAR2(250),
        father_name VARCHAR2(250),
        IDcard NUMBER ,
        
        position_id NUMBER,
        FOREIGN KEY (position_id) REFERENCES position (position_id)
    )
"""
cursor.execute(employee)

user= """
    CREATE TABLE user1 (
        user_id NUMBER PRIMARY KEY,
        username VARCHAR2(250),
        password VARCHAR2(250),
        email VARCHAR2(250),
        IDcard NUMBER ,

        employee_id NUMBER,
        FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
    )
"""
cursor.execute(user)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
