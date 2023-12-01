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


# Create the paper_id table
table_creation_query = """
    CREATE TABLE general_confirmation (
        gen_id NUMBER PRIMARY KEY,
        firstname VARCHAR(250),
        lastname VARCHAR(250),
        fathername VARCHAR(250),
        father_lastname VARCHAR(250),
        finger_print_confirmer_id   NUMBER,
        FOREIGN KEY (finger_print_confirmer_id ) REFERENCES finger_print_confirmer (finger_print_confirmer_id ),
        
        signature_confirmer_id   NUMBER,
        FOREIGN KEY (signature_confirmer_id ) REFERENCES signature_confirmer (signature_confirmer_id),
        
        
        electronic_id_card   NUMBER,
        FOREIGN KEY (electronic_id_card) REFERENCES electronic_idcard (electronic_id_card),
        
        
        paper_id   NUMBER,
        FOREIGN KEY (paper_id) REFERENCES paper_id  (paper_id)
    )
"""
cursor.execute(table_creation_query)


connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
