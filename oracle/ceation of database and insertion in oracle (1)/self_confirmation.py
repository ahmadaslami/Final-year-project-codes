
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

for _ in range(10):

    # Randomly select a signature_citizen ID or finger_print_citizen ID
    if random.choice([True, False]):
        # Select a random signature_citizen ID from the signature_citizen table
        cursor.execute("SELECT signature_citizen_id FROM signature_citizen ORDER BY DBMS_RANDOM.RANDOM")
        signature_citizen_id = cursor.fetchone()[0]
        finger_print_citizen_id = None
    else:
        # Select a random finger_print_citizen ID from the finger_print_citizen table
        cursor.execute("SELECT finger_print_citizen_id FROM finger_print_citizen ORDER BY DBMS_RANDOM.RANDOM")
        finger_print_citizen_id = cursor.fetchone()[0]
        signature_citizen_id = None

    # Create the variables for date and self_confirmation_id
    date = fake.date_between(start_date='-30d', end_date='today')
    self_confirmation_id = random.randint(1, 100)

    # Create the insert statement
    insert_statement = """
        INSERT INTO self_confirmation (self_confirmation_id, date1, signature_citizen_id, finger_print_citizen_id)
        VALUES (:self_confirmation_id, :date1, :signature_citizen_id, :finger_print_citizen_id)
    """

    # Execute the insert statement
    cursor.execute(insert_statement, {
        'self_confirmation_id': self_confirmation_id,
        'date1': date,
        'signature_citizen_id': signature_citizen_id,
        'finger_print_citizen_id': finger_print_citizen_id
    })

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
