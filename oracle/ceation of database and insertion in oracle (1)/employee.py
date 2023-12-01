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
cursor.execute("SELECT position_id FROM position")
position_ids = [row[0] for row in cursor.fetchall()]
for employee_id in range(1,100):
    first_name= fake.name()
    last_name=  fake.name()
    father_name =  fake.first_name_male()
    IDcard=fake.random_number(digits=5)
    position_id = fake.random_element(position_ids)

    # Define the SQL statement for inserting data into the "date_birth" table
    sql = "INSERT INTO employee (employee_id,first_name,last_name,father_name,IDcard,position_id) VALUES (:1, :2, :3,:4,:5,:6)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (employee_id,first_name,last_name,father_name,IDcard,position_id))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()