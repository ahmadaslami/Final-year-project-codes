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
fake = Faker()  # Set the locale to generate Afghan Persian (Dari) fake data


# Create the paper_id table
table_creation_query = """
    CREATE TABLE paper_id (
        paper_id NUMBER PRIMARY KEY,
        year NUMBER,
        volume NUMBER,
        page_no NUMBER,
        registeration_no VARCHAR2(100),
        sukuk_no VARCHAR2(100)
    )
"""
cursor.execute(table_creation_query)

# Generate and insert 10,000 rows of sample data
for i in range(10001,100000):
    paper_id = i
    year = random.randint(1800, 2023)
    volume = random.randint(1, 100)
    page_no = random.randint(1, 500)
    registeration_no = random.randint(1, 500)
    sukuk_no = random.randint(1, 500)

    insert_query = """
        INSERT INTO paper_id (paper_id, year, volume, page_no, registeration_no, sukuk_no)
        VALUES (:1, :2, :3, :4, :5, :6)
    """
    cursor.execute(insert_query, (paper_id, year, volume, page_no, registeration_no, sukuk_no))

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
