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
# Generate fake data and insert it into the "date_birth" table
for position_id in range(1,100000):
    position_name= fake.word()
    salary=random.randint(10000, 150000)

    # Define the SQL statement for inserting data into the "date_birth" table
    sql = "INSERT INTO position (position_id,position_name, salary) VALUES (:1, :2, :3)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (position_id, position_name, salary))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()