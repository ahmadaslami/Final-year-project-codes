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
cursor.execute("SELECT employee_id FROM employee")
employee_ids = [row[0] for row in cursor.fetchall()]
for user_id in range(1,100):
    username= fake.name()
    password=  fake.name()
    email =  fake.email()
    employee_id = fake.random_element(employee_ids)

    # Define the SQL statement for inserting data into the "date_birth" table
    sql = "INSERT INTO user1 (user_id,username,password,email,employee_id) VALUES (:1, :2, :3,:4,:5)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (user_id,username,password,email,employee_id))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()