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
    CREATE TABLE education1 (
        edu_id NUMBER PRIMARY KEY,
        education VARCHAR2(100)
    ) """
cursor.execute(table_creation_query)
edu1 = ['master','doctor','bachelor','14_pass','school_graduated','primary_education','no_education']
# Generate and insert 100 rows of sample data
for i in range(1,1000):
    edu_id = i
    education = random.choice(edu1)
    insert_query = """
        INSERT INTO education1 (edu_id,education)
        VALUES (:1, :2)
    """
    cursor.execute(insert_query, (edu_id,education))
# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
