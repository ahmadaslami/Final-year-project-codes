import random
from faker import Faker
from pymongo import MongoClient
from PIL import Image
import io

import pymongo
from PIL import Image
import io
import random
import os
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['NSIA']
collection = db['citizen']

# Create a Faker instance
fake = Faker()
education_collection = db['education']
province_collection = db['province']
district_collection = db['district']
village_collection = db['village']
date_of_birth_collection = db['date_of_birth']
real_residence_collection = db['real_residence']
NSIA_confirmation_collection = db['NSIA_confirmation']
current_residence_collection = db['current_residence']
general_confirmation_collection = db['general_confirmation']
kochi_collection = db["kochi"]
job_collection = db["job"]
second_nature_collection = db["second_nature"]

paper_id_place_collection = db["paper_id_place"]
self_confirmation_collection = db["self_confirmation"]
family_collection = db["family"]
electronic_idcard_table = db["electronic_idcard"]
signature_citizen_table = db["signature_citizen"]
finger_print_citizen_table = db["finger_print_citizen"]
paper_id_table = db["paper_id"]
languages = ["pashto","Dari"]
folder_path = "E:\Every thing\Mobile Applications\image3"
# Get a list of image files from the folder
image_files = os.listdir(folder_path)
# Randomly select 10 images from the list
selected_images = random.sample(image_files, 9)
foregin_languages = [
    'Abkhaz',
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
internal_languages = ["pashto","Dari","Turkmeny","Uzbeky","pushuy"]
civil_status_collection = db['civil_status']
blood_groups = ["O-","O+","AB+","AB-","B-","B+","A+","A-"]
nationalities = ["Pashton","Tajik","Hezara"]
religions = ["Imam Hanafi sahub","Imam Malik sahub","Imam shafiy sahub","Imam Hanbali sahub"]
faith = ["Islam"]
disability_types = ["NO","completely","partial"]
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

province_ids = [province_doc['_id'] for province_doc in province_collection.find({}, {'_id': 1})]
district_ids = [district_doc['_id'] for district_doc in district_collection.find({}, {'_id': 1})]
village_ids = [village_doc['_id'] for village_doc in village_collection.find({}, {'_id': 1})]
date_of_birth_ids = [date_of_birth_doc['_id'] for date_of_birth_doc in date_of_birth_collection.find({}, {'_id': 1})]
real_residence_ids = [real_residence_doc['_id'] for real_residence_doc in real_residence_collection.find({}, {'_id': 1})]
current_residence_ids = [current_residence_doc['_id'] for current_residence_doc in current_residence_collection.find({}, {'_id': 1})]
civil_status_ids = [civil_status_doc['_id'] for civil_status_doc in civil_status_collection.find({}, {'_id': 1})]
kochi_ids = [kochi_doc['_id'] for kochi_doc in kochi_collection.find({}, {'_id': 1})]
job_ids = [job_doc['_id'] for job_doc in job_collection.find({}, {'_id': 1})]
second_nature_ids = [second_nature_doc['_id'] for second_nature_doc in second_nature_collection.find({}, {'_id': 1})]
paper_id_place_ids = [paper_id_place_doc['_id'] for paper_id_place_doc in paper_id_place_collection.find({}, {'_id': 1})]
self_confirmation_ids = [self_confirmation_doc['_id'] for self_confirmation_doc in self_confirmation_collection.find({}, {'_id': 1})]
general_confirmation_ids = [general_confirmation_doc['_id'] for general_confirmation_doc in general_confirmation_collection.find({}, {'_id': 1})]
NSIA_confirmation_ids = [NSIA_confirmation_doc['_id'] for NSIA_confirmation_doc in NSIA_confirmation_collection.find({}, {'_id': 1})]
family_ids = [family_doc['_id'] for family_doc in family_collection.find({}, {'_id': 1})]
education_ids = [education_doc['_id'] for education_doc in education_collection.find({}, {'_id': 1})]
# Generate and insert fake data
for _ in range(1000):  # Generate 10 records
    # Generate a random image
    image_file = random.choice(selected_images)
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_data = image_bytes.getvalue()
    religion= random.choice(religions)
    civil_status_id = fake.random.choice(civil_status_ids)
    NSIA_confirmation_id = fake.random.choice(NSIA_confirmation_ids)
    Village_id = fake.random.choice(village_ids)
    date_of_birth_id = fake.random.choice(date_of_birth_ids)
    current_residence_id = fake.random.choice(current_residence_ids)
    province_id = fake.random.choice(province_ids)
    family_id = fake.random.choice(family_ids)
    real_residence_id = fake.random.choice(real_residence_ids)
    District_id = fake.random.choice(district_ids)
    language = random.choice(languages)
    gender = random.choice(genders)
    faiths = random.choice(faith)
    voting_place = random.choice(voting_places)
    disability_type = random.choice(disability_types)
    nationality = random.choice(nationalities)
    blood_group = random.choice(blood_groups)
    internal_language= random.choice(internal_languages)
    foregin_languages = random.choice(foregin_languages)
    militry_service = random.choice([None,'yes'])
    education = random.choice([None,random.choice(education_ids)])
    phone_number = random.choice([None, fake.phone_number()])
    kochi_id = random.choice([None,random.choice(kochi_ids)])
    general_confirmation_id = random.choice(([None,random.choice(self_confirmation_ids)]))
    self_confirmation_id = random.choice(self_confirmation_ids)
    second_nature_id = random.choice([None,random.choice(second_nature_ids)])
    job_id = random.choice([None,random.choice(job_ids)])
    email_address = random.choice([None, fake.email()])
    paper_id_place_id = random.choice([None,random.choice(paper_id_place_ids) ])
    if random.choice([True, False]):
        # Select a random signature_citizen ID from the signature_citizen table
        electronic_idcard_document = electronic_idcard_table.aggregate([{"$sample": {"size": 1}}]).next()
        finger_print_citizen_document = finger_print_citizen_table.aggregate([{"$sample": {"size": 1}}]).next()
        electronic_idcard_id = electronic_idcard_document["_id"]
        finger_print_citizen_id = finger_print_citizen_document["_id"]
        paper_id_id = None
        signature_citizen_id = None
    else:
        # Select a random finger_print_citizen ID from the finger_print_citizen table
        paper_id_document = paper_id_table.aggregate([{"$sample": {"size": 1}}]).next()
        signature_citizen_document = signature_citizen_table.aggregate([{"$sample": {"size": 1}}]).next()
        paper_id_id = paper_id_document["_id"]
        signature_citizen_id = signature_citizen_document["_id"]
        electronic_idcard_id = None
        finger_print_citizen_id = None
    data = {
        'first_name': fake.name(),
        'last_name': fake.name(),
        'fathername': fake.first_name_male(),
        'father_last_name': fake.first_name_male(),
        'grand_father_name': fake.first_name_male(),
        'grand_father_last_name': fake.first_name_male(),
        'mother_name': fake.first_name_female(),
         'ID_Card_NO' : fake.random_number(digits=5),
        'photo': image_data,
        "militry_service":militry_service,
        "phone_number":phone_number,
        "Email_address":email_address,
        "Native_language": language,
        "foregin_language":foregin_languages,
        "Internal_language":internal_language,
        "Blood_Group":blood_group,
        "Nationality":nationality,
        "Religion":religion,
        "Faith":faiths,
        "Disability_type":disability_type,
        "Gender":gender,
        "Voting_place":voting_place,
        "Province_id":province_id,
        "District_id":District_id,
        "Village_id":Village_id,
        "date_of_birth_id":date_of_birth_id,
        "Education":education,
        "real_residence_id":real_residence_id,
        "current_residence_id":current_residence_id,
        "civil_status_id":civil_status_id,
        "Kochi_id":kochi_id,
        "Job_id":job_id,
        "second_nature_id":second_nature_id,
        "electronic_idcard_id": electronic_idcard_id,
        "paper_id_id": paper_id_id,
        "paper_id_place_id":paper_id_place_id,
        "self_confirmation_id":self_confirmation_id,
        "general_confirmation_id":self_confirmation_id,
       "finger_print_citizen_id":finger_print_citizen_id ,
        "signature_citizen_id":signature_citizen_id,
       "NSIA_confirmation_id":NSIA_confirmation_id,
        "family_id":family_id
    }
    collection.insert_one(data)

# Close the MongoDB connection
client.close()
