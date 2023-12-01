
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


# Retrieve province IDs from the "province" table
cursor.execute("SELECT province_id FROM province")
province_ids = [row[0] for row in cursor.fetchall()]

# Retrieve district IDs from the "district" table
cursor.execute("SELECT district_id FROM district")
district_ids = [row[0] for row in cursor.fetchall()]

# Generate fake data and insert it into the "village" table
for village_id in range(1, 10000):
    village_name = fake.city()
    province_id = fake.random_element(province_ids)
    district_id = fake.random_element(district_ids)

    # Define the SQL statement for inserting data into the "village" table
    sql = "INSERT INTO village (village_id, name, province_id, district_id) VALUES (:1, :2, :3, :4)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (village_id, village_name, province_id, district_id))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
