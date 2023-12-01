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

cursor.execute("SELECT province_id FROM province")
province_ids = [row[0] for row in cursor.fetchall()]

# Generate fake data and insert it into the "district" table
for district_id in range(1, 366):
    district_name = fake.city()
    province_id = fake.random_element(province_ids)

    # Define the SQL statement for inserting data into the "district" table
    sql = "INSERT INTO district (district_id, name, province_id) VALUES (:1, :2, :3)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (district_id, district_name, province_id))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
