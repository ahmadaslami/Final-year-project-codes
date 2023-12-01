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
#Create a cursor object to execute SQL statements
cursor = connection.cursor()
# Create an instance of Faker
fake = Faker()  # Set the locale to generate Afghan Persian (Dari) fake data
# Create the education table
# Generate and insert 100 rows of sample data
photo_folder = "E:\Every thing\Mobile Applications\image3"  # Replace with the actual path
native_language1 = ["pashto","dari"]
internal_languages1 = ["pashto","Dari","Turkmeny","Uzbeky","pushuy"]

foreign_language1 =  ['Abkhaz',
    'Afar',
    'Afrikaans',
    'Akan',
    'Albanian',
    'Amharic',
    'Arabic',
    'Aragonese',
    'Armenian',
    'Assamese',
    'Avaric',
    'Avestan',
    'Aymara',
    'Azerbaijani',
    'Bambara',
    'Bashkir',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bihari',
    'Bislama',
    'Bosnian',
    'Breton',
    'Bulgarian',
    'Burmese',
    'Catalan',
    'Chamorro',
    'Chechen',
    'Chichewa',
    'Chinese',
    'Chuvash',
    'Cornish',
    'Corsican',
    'Cree',
    'Croatian',
    'Czech',
    'Danish',
    'Divehi',
    'Dutch',
    'Dzongkha',
    'English',
    'Esperanto',
    'Estonian',
    'Ewe',
    'Faroese',
    'Fijian',
    'Finnish',
    'French',
    'Fula',
    'Galician',
    'Ganda',
    'Georgian',
    'German',
    'Greek',
    'Guaraní',
    'Gujarati',
    'Haitian',
    'Hausa',
    'Hebrew',
    'Herero',
    'Hindi',
    'Hiri Motu',
    'Hungarian',
    'Icelandic',
    'Ido',
    'Igbo',
    'Indonesian',
    'Interlingua',
    'Interlingue',
    'Inuktitut',
    'Inupiaq',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kalaallisut',
    'Kannada',
    'Kanuri',
    'Kashmiri',
    'Kazakh',
    'Khmer',
    'Kikuyu',
    'Kinyarwanda',
    'Kirundi',
    'Komi',
    'Kongo',
    'Korean',
    'Kurdish',
    'Kwanyama',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Limburgish',
    'Lingala',
    'Lithuanian',
    'Luba-Katanga',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Manx',
    'Maori',
    'Marathi',
    'Marshallese',
    'Moldavian',
    'Mongolian',
    'Nauru',
    'Navajo',
    'Ndonga',
    'Northern Ndebele',
    'Nepali',
    'Norwegian',
    'Norwegian Bokmål',
    'Norwegian Nynorsk',
    'Nuosu',
    'Occitan',
    'Ojibwe',
    'Old Church Slavonic',
    'Oriya',
    'Oromo',
    'Ossetian',
    'Pāli',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Quechua',
    'Romansh',
    'Romanian',
    'Russian',
    'Samoan',
    'Sango',
    'Sanskrit',
    'Sardinian',
    'Scottish Gaelic',
    'Serbian',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovene',
    'Somali',
    'Southern Ndebele',
    'Southern Sotho',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swati',
    'Swedish',
    'Tagalog',
    'Tahitian',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Tibetan',
    'Tigrinya',
    'Tonga']
blood_group1 = ["O-","O+","AB+","AB-","B-","B+","A+","A-"]
nationalities = ["Pashton","Tajik","Hezara"]
religions = ["Imam Hanafi sahub","Imam Malik sahub","Imam shafiy sahub","Imam Hanbali sahub"]
faith1 = ["Islam"]

disability_types1 = ["completely","partial"]
genders = ["Male","Female"]
voting_places = [
    "Badakhshan",
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
    "Zabul"
]

cursor.execute("SELECT province_id FROM province")
province_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT district_id FROM district")
district_ids = [row[0] for row in cursor.fetchall()]



cursor.execute("SELECT village_id FROM village")
village_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT date_birth_id FROM date_birth")
date_birth_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT edu_id FROM education")
edu_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT real_residence_id FROM real_residence")
real_residence_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT current_id FROM current_station")
current_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT civil_status_id FROM civil_status")
civil_status_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT kochi_id FROM kochi")
kochi_ids = [row[0] for row in cursor.fetchall()]




cursor.execute("SELECT job_id FROM job")
job_ids = [row[0] for row in cursor.fetchall()]



cursor.execute("SELECT se_na_id FROM second_nature")
se_na_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT paper_id FROM paper_id")
paper_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT  paper_place_id FROM paper_id_place")
paper_place_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT  self_confirmation_id FROM self_confirmation")
self_confirmation_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT  gen_id FROM general_confirmation")
gen_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT  NSIA_confirmation_id FROM nsia_confirmation")
NSIA_confirmation_ids = [row[0] for row in cursor.fetchall()]



cursor.execute("SELECT  family_id FROM family_citizen")
family_ids = [row[0] for row in cursor.fetchall()]

# Initialize counters for the three parts of the citizen ID
part1 = 1200
part2 = 200
part3 = 1

def generate_citizen_id():
    global part1, part2, part3

    # Increment part3 and handle rollover
    part3 += 1
    if part3 > 70:
        part3 = 1
        part2 += 1
        if part2 > 230:
            part2 = 200
            part1 += 1
            if part1 > 1900:
                raise Exception("Citizen ID range exceeded")

    return f"{part1}-{part2}-{part3}"

num_citizens = 100  # Adjust the number of citizens you want to generate

for _ in range(num_citizens):
    citizen_id = generate_citizen_id()
    firstname = fake.first_name()
    lastname = fake.last_name()
    fathername = fake.first_name()
    father_lastname = fake.last_name()
    grand_father_name = fake.first_name()
    grand_father_last_name = fake.last_name()
    mother_name = fake.name()
    photo_file = random.choice(os.listdir(photo_folder))
    photo_path = os.path.join(photo_folder, photo_file)
    with open(photo_path, 'rb') as file:
        photo = file.read()
    military_service = "yes" if random.choice([True, False]) else None
    phone_number = fake.random_int(min=10**8,max=10**10) if random.choice([True, False]) else None
    email_address = fake.email() if random.choice([True, False]) else None
    native_language = random.choice(native_language1)
    foreign_language = random.choice(foreign_language1) if random.choice([True, False]) else None
    internal_language = random.choice(internal_languages1) if random.choice([True, False]) else None
    blood_group = random.choice(blood_group1) if random.choice([True, False]) else None
    nationality = random.choice(nationalities)
    religion = random.choice(religions)
    faith = random.choice(faith1)
    disability_type  = random.choice(disability_types1) if random.choice([True, False]) else None
    gender = random.choice(genders)
    voting_place  = random.choice(voting_places) if random.choice([True,False]) else None
    province_id = random.choice(province_ids)
    district_id = random.choice(district_ids)
    village_id = random.choice(village_ids)
    date_birth_id = random.choice(date_birth_ids)
    edu_id = random.choice(edu_ids)
    real_residence_id = random.choice(real_residence_ids)
    current_id = random.choice(current_ids)
    civil_status_id = random.choice(civil_status_ids)
    kochi_id = random.choice(kochi_ids) if random.choice([True,False]) else None
    job_id = random.choice(job_ids) if random.choice([True,False]) else None
    se_na_id = random.choice(se_na_ids) if random.choice([True,False]) else None
    paper_id  = random.choice(paper_ids) if random.choice([True,False]) else None
    paper_place_id   = random.choice(paper_place_ids) if random.choice([True,False]) else None
    self_confirmation_id   = random.choice(self_confirmation_ids)
    gen_id = random.choice(gen_ids) if random.choice([True,False]) else None
    # Randomly select a signature_citizen ID or finger_print_citizen ID
    if random.choice([True, False]):

        # Select a random finger_print_citizen ID from the finger_print_citizen table
        cursor.execute("SELECT signature_citizen_id  FROM signature_citizen ORDER BY DBMS_RANDOM.RANDOM")
        signature_citizen_id  = cursor.fetchone()[0]
        finger_print_citizen_id  = None


    else:
        # Select a random signature_citizen ID from the signature_citizen table
        cursor.execute("SELECT finger_print_citizen_id FROM finger_print_citizen ORDER BY DBMS_RANDOM.RANDOM")
        finger_print_citizen_id = cursor.fetchone()[0]
        signature_citizen_id = None
    NSIA_confirmation_id = random.choice(NSIA_confirmation_ids)
    family_id = random.choice(family_ids) if random.choice([True,False]) else None

    insert_query = """
        INSERT INTO citizen (citizen_id,firstname,lastname,fathername,father_lastname,grand_father_name,grand_father_last_name,mother_name,photo,military_service,phone_number,email_address,native_language,foreign_language,internal_language,blood_group,nationality,religion,faith,
        disability_type,gender,voting_place,province_id,district_id,village_id,date_birth_id,edu_id,real_residence_id,current_id,
        civil_status_id,kochi_id,job_id,se_na_id,paper_id,paper_place_id,self_confirmation_id,gen_id,signature_citizen_id,finger_print_citizen_id,
        NSIA_confirmation_id,family_id)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19,
        :20, :21, :22, :23, :24, :25, :26, :27, :28, :29, :30, :31, :32, :33, :34, :35, :36, :37, :38, :39, :40, :41)"""
    cursor.execute(insert_query, (citizen_id,firstname,lastname,fathername,father_lastname,grand_father_name,grand_father_last_name,mother_name,photo,military_service,phone_number,email_address,native_language,foreign_language,internal_language,blood_group,nationality,religion,faith,
                                  disability_type,gender,voting_place,province_id,district_id,village_id,date_birth_id,edu_id,real_residence_id,
                                  current_id,civil_status_id,kochi_id,job_id,se_na_id,paper_id,paper_place_id,self_confirmation_id,
                                  gen_id,signature_citizen_id,
                                  finger_print_citizen_id,NSIA_confirmation_id,family_id))
# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
