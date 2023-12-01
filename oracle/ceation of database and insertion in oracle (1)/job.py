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

job_name = [
    "Software Engineer",
    "Graphic Designer",
    "Accountant",
    "Marketing Manager",
    "Sales Representative",
    "Nurse",
    "Teacher",
    "Financial Analyst",
    "Human Resources Manager",
    "Project Manager",
    "Data Scientist",
    "Customer Service Representative",
    "Web Developer",
    "Architect",
    "Lawyer",
    "Chef",
    "Electrician",
    "Mechanical Engineer",
    "Pharmacist",
    "Social Media Manager"
]


# Generate and insert fake data into the "province" table
for job_id, job_name in enumerate(job_name, start=1):
    # Define the SQL statement for inserting data into the "province" table
    sql = "INSERT INTO job (job_id, job_name) VALUES (:1, :2)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (job_id, job_name))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()





