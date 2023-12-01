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

cursor.execute("SELECT district_id FROM district")
district_ids = [row[0] for row in cursor.fetchall()]

for paper_place_id in range(1, 100):
    province_id = fake.random_element(province_ids)
    district_id = fake.random_element(district_ids)

    year = fake.random_int(min=1660, max=2023)
    month = fake.random_int(min=1, max=12)
    day = fake.random_int(min=1, max=28)

    # Format the date string to match Oracle's date format: 'yyyy-mm-dd'
    date1 = f"{year:04d}-{month:02d}-{day:02d}"

    # Define the SQL statement for inserting data into the "date_birth" table
    sql = "INSERT INTO paper_id_place (paper_place_id, province_id, district_id, date1) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (paper_place_id, province_id, district_id, date1))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
