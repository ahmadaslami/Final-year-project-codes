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


# Create the "student" table with a foreign key constraint
citizen = """
    CREATE TABLE citizen (
        citizen_id VARCHAR(250) PRIMARY KEY,
        firstname VARCHAR(250),
        lastname VARCHAR(250),
        fathername VARCHAR(250),
        father_lastname VARCHAR(250), 
        grand_father_name VARCHAR(250),
        grand_father_last_name VARCHAR(250),
        mother_name VARCHAR(250),
        photo BLOB,
        military_service VARCHAR(250) NULL,
        phone_number    VARCHAR(250) NULL,
        email_address   VARCHAR(250) NULL,
        native_language VARCHAR(250),
        foreign_language VARCHAR(250) NULL,
        internal_language VARCHAR(250) NULL,
        blood_group VARCHAR(250) NULL,
        nationality VARCHAR(250),
        religion VARCHAR(250),
        faith VARCHAR(250),
        disability_type VARCHAR(250) NULL,
        gender  VARCHAR(250),
        voting_place  VARCHAR(250) NULL,
        province_id  NUMBER,
        FOREIGN KEY (province_id) REFERENCES province (province_id),
        district_id  NUMBER,
        FOREIGN KEY (district_id) REFERENCES district (district_id),
        village_id  NUMBER,
        FOREIGN KEY (village_id) REFERENCES village (village_id),
        date_birth_id  NUMBER,
        FOREIGN KEY (date_birth_id) REFERENCES date_birth (date_birth_id),
        edu_id  NUMBER,
        FOREIGN KEY (edu_id) REFERENCES education (edu_id),
        real_residence_id  NUMBER,
        FOREIGN KEY (real_residence_id) REFERENCES real_residence (real_residence_id),
        current_id  NUMBER,
        FOREIGN KEY (current_id) REFERENCES current_station(current_id),
        civil_status_id  NUMBER,
        FOREIGN KEY (civil_status_id) REFERENCES civil_status(civil_status_id),


        kochi_id  NUMBER,
	FOREIGN KEY (kochi_id) REFERENCES kochi(kochi_id),


        job_id  NUMBER,
        FOREIGN KEY (job_id) REFERENCES job(job_id),
        se_na_id  NUMBER,
        FOREIGN KEY (se_na_id) REFERENCES second_nature (se_na_id),
        paper_id  NUMBER,
        FOREIGN KEY (paper_id) REFERENCES paper_id  (paper_id),
        paper_place_id  NUMBER,
        FOREIGN KEY (paper_place_id) REFERENCES paper_id_place (paper_place_id),
        self_confirmation_id  NUMBER,
        FOREIGN KEY (self_confirmation_id) REFERENCES self_confirmation (self_confirmation_id),
        gen_id  NUMBER,
        FOREIGN KEY (gen_id) REFERENCES general_confirmation (gen_id),
        signature_citizen_id  NUMBER,
        FOREIGN KEY (signature_citizen_id) REFERENCES signature_citizen (signature_citizen_id),
        finger_print_citizen_id  NUMBER,
        FOREIGN KEY (finger_print_citizen_id) REFERENCES finger_print_citizen (finger_print_citizen_id),
        NSIA_confirmation_id  NUMBER,
        FOREIGN KEY (NSIA_confirmation_id) REFERENCES NSIA_confirmation (NSIA_confirmation_id),
        family_id  NUMBER,
        FOREIGN KEY (family_id) REFERENCES family_citizen (family_id))"""




cursor.execute(citizen)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Class and Student tables created successfully.")
