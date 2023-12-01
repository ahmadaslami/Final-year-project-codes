import cx_Oracle
import random
from faker import Faker

# Establish a connection to the Oracle database
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)
#Create a cursor object to execute SQL statements
cursor = connection.cursor()
# Create an instance of Faker
fake = Faker()  # Set the locale to generate Afghan Persian (Dari) fake data
# Create the education table
table_creation_query = """
    CREATE TABLE civil_status (
        civil_status_id NUMBER PRIMARY KEY,
        civil_statu VARCHAR2(100)
    ) """
cursor.execute(table_creation_query)
civil_statu1 = ['single','married','cocoanut','divorce']
# Generate and insert 100 rows of sample data
for i in range(1000,100000):
    civil_status_id = i
    civil_statu = random.choice(civil_statu1)
    insert_query = """
        INSERT INTO civil_status (civil_status_id,civil_statu)
        VALUES (:1, :2)
    """
    cursor.execute(insert_query, (civil_status_id,civil_statu))
# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
