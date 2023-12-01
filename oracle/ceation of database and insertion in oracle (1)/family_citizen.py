import cx_Oracle
import random
from faker import Faker
import os
# Establish a connection to the Oracle database
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)
fake = Faker()

# Create a cursor object to execute SQL statements
cursor = connection.cursor()
photo_folder = "E:\Every thing\Mobile Applications\image3"  # Replace with the actual path
cursor.execute("SELECT se_na_id FROM second_nature")
second_nature_ids = [row[0] for row in cursor.fetchall()]
# Create an instance of Faker


for family_id  in range(50,60):
    # Generate fake data
    firstname = fake.first_name()
    lastname = fake.last_name()
    fname = fake.first_name()
    relation = random.choice(['Parent', 'Sibling', 'Spouse', 'Child'])
    death = random.choice(['death', 'no death'])
    req_taz = random.choice(['yes', 'no'])
    grandfname= fake.first_name()
    date1 = fake.date_between(start_date='-30d', end_date='today')
    # Select a photo file from the folder
    photo_file = random.choice(os.listdir(photo_folder))
    photo_path = os.path.join(photo_folder, photo_file)

    # Read the contents of the photo file as binary data
    with open(photo_path, 'rb') as file:
        sig = file.read()
    gender = random.choice(['male', 'female'])
    if random.random() < 0.5:
        se_na_id = None
    else:
        se_na_id = random.choice(second_nature_ids)





    # Insert data into the 'test' table
    cursor.execute("""
        INSERT INTO family_citizen (family_id,firstname, lastname,fname,relation,death,req_taz,grandfname,date1,sig,gender,se_na_id)
        VALUES (:family_id,:firstname, :lastname,:fname,:relation,:death,:req_taz,:grandfname,:date1,:sig,:gender,:se_na_id)
    """, {
        'family_id':family_id,
        'firstname':firstname,
        'lastname':lastname,
        'fname':fname,
        'relation':relation,
        'death':death,
        'req_taz':req_taz,
        'grandfname':grandfname,
        'date1':date1,
        'sig':sig,
        'gender':gender,
        'se_na_id':se_na_id
    })

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
