
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

for _ in range(1,10):

    # Randomly select a signature_citizen ID or finger_print_citizen ID
    if random.choice([True, False]):

        # Select a random finger_print_citizen ID from the finger_print_citizen table
        cursor.execute("SELECT finger_print_confirmer_id FROM finger_print_confirmer ORDER BY DBMS_RANDOM.RANDOM")
        finger_print_confirmer_id = cursor.fetchone()[0]

        cursor.execute("SELECT electronic_id_card FROM electronic_idcard ORDER BY DBMS_RANDOM.RANDOM")
        electronic_id_card = cursor.fetchone()[0]
        signature_confirmer_id = None
        paper_id = None

    else:
        # Select a random signature_citizen ID from the signature_citizen table
        cursor.execute("SELECT signature_confirmer_id FROM signature_confirmer ORDER BY DBMS_RANDOM.RANDOM")
        signature_confirmer_id = cursor.fetchone()[0]


        cursor.execute("SELECT paper_id FROM paper_id ORDER BY DBMS_RANDOM.RANDOM")
        paper_id = cursor.fetchone()[0]

        finger_print_confirmer_id = None
        electronic_id_card = None

    gen_id = random.randint(1, 100)
    firstname = fake.first_name()
    lastname = fake.last_name()
    fathername = fake.first_name()
    father_lastname = fake.last_name()


    # Create the insert statement
    insert_statement = """
        INSERT INTO general_confirmation (gen_id, firstname, lastname, fathername, father_lastname, finger_print_confirmer_id, signature_confirmer_id, electronic_id_card, paper_id)
        VALUES (:gen_id, :firstname, :lastname, :fathername, :father_lastname, :finger_print_confirmer_id, :signature_confirmer_id, :electronic_id_card, :paper_id)
    """

    # Execute the insert statement
    cursor.execute(insert_statement, {
        'gen_id': gen_id,
        'firstname': firstname,
        'lastname': lastname,
        'fathername': fathername,
        'father_lastname': father_lastname,
        'finger_print_confirmer_id': finger_print_confirmer_id,
        'signature_confirmer_id': signature_confirmer_id,
        'electronic_id_card': electronic_id_card,
        'paper_id': paper_id,

    })

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
