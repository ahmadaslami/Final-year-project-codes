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


# Generate fake data and insert it into the "electronic_idcard" table
for electronic_id_card in range(100):
    idcard_number = fake.random_int(min=1000, max=99999)

    # Define the SQL statement for inserting data into the "electronic_idcard" table
    sql = "INSERT INTO electronic_idcard (electronic_id_card, idcard_number) VALUES (:1, :2)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (electronic_id_card, idcard_number))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
