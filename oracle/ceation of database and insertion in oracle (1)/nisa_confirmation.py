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
cursor.execute("SELECT family_id FROM family_citizen")
family_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT signature_nsia_confirmer_id FROM signature_nsia_confirmer")
signature_nsia_confirmer_ids = [row[0] for row in cursor.fetchall()]



for nsia_confirmation_id in range(366, 370):
    name = fake.word()
    user_type = fake.word()
    ID_Card_NO = fake.random_number(digits=5)
    family_id = fake.random.choice(family_ids)
    signature_nsia_confirmer_id = fake.random.choice(signature_nsia_confirmer_ids)

    # Define the SQL statement for inserting data into the "nsia_confirmation" table
    sql = "INSERT INTO nsia_confirmation (nsia_confirmation_id, name, user_type, ID_Card_NO, family_id, signature_nsia_confirmer_id) VALUES (:1, :2, :3, :4, :5, :6)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (nsia_confirmation_id, name, user_type, ID_Card_NO, family_id, signature_nsia_confirmer_id))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
