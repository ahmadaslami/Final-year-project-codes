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

province_names = ["Badakhshan",
    "Badghis",
    "Baghlan",
    "Balkh",
    "Bamyan",
    "Daykundi",
    "Farah",
    "Faryab",
    "Ghazni",
    "Ghor",
    "Helmand",
    "Herat",
    "Jowzjan",
    "Kabul",
    "Kandahar",
    "Kapisa",
    "Khost",
    "Kunar",
    "Kunduz",
    "Laghman",
    "Logar",
    "Nangarhar",
    "Nimruz",
    "Nuristan",
    "Paktika",
    "Paktia",
    "Panjshir",
    "Parwan",
    "Samangan",
    "Sar-e Pol",
    "Takhar",
    "Uruzgan",
    "Wardak",
    "Zabul"]

# Generate and insert fake data into the "province" table
for province_id, province_name in enumerate(province_names, start=1):
    # Define the SQL statement for inserting data into the "province" table
    sql = "INSERT INTO province (province_id, name) VALUES (:1, :2)"

    # Execute the SQL statement with the generated data
    cursor.execute(sql, (province_id, province_name))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()





