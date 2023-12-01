
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
for date_birth_id in range(1,100000):
    birth_year = fake.random_int(min=1660, max=2023)
    birth_month = fake.random_int(min=1, max=12)
    birth_day = fake.random_int(min=1, max=28)

    # Define the SQL statement for inserting data into the "date_birth" table
    sql = "INSERT INTO date_birth (date_birth_id, birth_year, birth_month, birth_day) VALUES (:1, :2, :3, :4)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (date_birth_id, birth_year, birth_month, birth_day))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()