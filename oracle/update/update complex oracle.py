import cx_Oracle
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, ttk
from io import BytesIO
import io
import time

# Initialize variables to store the current photo and new photo bytes
current_photo = None
new_photo_bytes = None

# Create the main window
root = tk.Tk()
root.title("Citizen Data Update")
id_entry = tk.Entry(root)
firstname_entry = tk.Entry(root)
lastname_entry = tk.Entry(root)
fathername_entry = tk.Entry(root)
father_lastname_entry = tk.Entry(root)
grand_father_name_entry = tk.Entry(root)
grand_father_last_name_entry = tk.Entry(root)
mother_name_entry = tk.Entry(root)
#military_service_entry = tk.Entry(root)
phone_number_entry = tk.Entry(root)
email_address_entry = tk.Entry(root)
native_language_entry = tk.Entry(root)
foreign_language_entry = tk.Entry(root)
internal_language_entry = tk.Entry(root)
blood_group_entry = tk.Entry(root)
nationality_entry = tk.Entry(root)
religion_entry = tk.Entry(root)
faith_entry = tk.Entry(root)
disability_type_entry = tk.Entry(root)
gender_entry = tk.Entry(root)
voting_place_entry = tk.Entry(root)
province_name_entry = tk.Entry(root)
district_name_entry = tk.Entry(root)
village_name_entry = tk.Entry(root)
education_entry = tk.Entry(root)
pro_name2_entry = tk.Entry(root)


# Function to retrieve and display data


def fetch_data():
    citizen_id = id_entry.get()

    # Establish a database connection
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all data based on the entered ID

    cursor.execute(
        "SELECT c.firstname,c.lastname,c.fathername,c.father_lastname,c.grand_father_name,c.grand_father_last_name,c.mother_name,"
        "c.photo,c.phone_number,c.email_address,c.native_language,c.foreign_language,c.internal_language,c.blood_group,c.nationality,c.religion,"
        "c.faith,c.disability_type,c.gender,c.voting_place,p.province_id,p.name,d.district_id,d.name,v.village_id,v.name,e.edu_id,e.education,"
        "r.real_residence_id,p1.name,d1.name,v1.name"
        " FROM citizen c"
        " INNER JOIN province p ON c.province_id = p.province_id"
        " INNER JOIN district d ON c.district_id = d.district_id"
        " INNER JOIN village v ON c.village_id = v.village_id"
        " INNER JOIN education e ON c.edu_id = e.edu_id"

        " INNER JOIN real_residence r ON c.real_residence_id = r.real_residence_id"
        " INNER JOIN province p1 ON r.province_id = p1.province_id"
        " INNER JOIN district d1 ON r.district_id = d1.district_id"
        " INNER JOIN village v1 ON r.village_id = v1.village_id"
        " WHERE citizen_id = :citizen_id",
        {'citizen_id': citizen_id})

    data = cursor.fetchone()

    if data:
        firstname, lastname, fathername, father_lastname, grand_father_name, grand_father_last_name, mother_name, photo,phone_number, email_address, native_language, foreign_language, internal_language, blood_group, nationality, religion, faith, disability_type, gender, voting_place, province_id, province_name, district_id, district_name, village_id, village_name, edu_id, education, real_residence_id, pro_name2, district_name1, village_name = data
        print(data)

        # After fetching the data from the database and storing it in the 'data' variable
        province_name = data[20]
        # Assuming 'province_id' is at index 20
        # Query the 'province' table to get the 'province_name'
        cursor.execute("SELECT name FROM province WHERE province_id = :province_id", {'province_id': province_id})
        province_data = cursor.fetchone()
        if province_data:
            province_name = province_data[0]
            # Assuming 'name' is the column name for province_name
            # Now you have 'province_name,' and you can populate the combobox
            province_combobox.set(province_name)
            # Assuming you've created a StringVar for the combobox
        else:
            province_combobox.set("Unknown")  # Set a default value if province is not found

        district_name = data[21]  # Assuming 'province_id' is at index 20

        # Query the 'province' table to get the 'province_name'
        cursor.execute("SELECT name FROM district WHERE district_id = :district_id", {'district_id': district_id})
        district_data = cursor.fetchone()
        if district_data:
            district_name = district_data[0]  # Assuming 'name' is the column name for province_name

            # Now you have 'province_name,' and you can populate the combobox
            district_combobox.set(district_name)  # Assuming you've created a StringVar for the combobox
        else:
            district_combobox.set("Unknown")  # Set a default value if province is not found

        village_name = data[22]  # Assuming 'province_id' is at index 20

        # Query the 'province' table to get the 'province_name'
        cursor.execute("SELECT name FROM village WHERE village_id = :village_id", {'village_id': village_id})
        village_data = cursor.fetchone()
        if village_data:
            village_name = village_data[0]  # Assuming 'name' is the column name for province_name

            # Now you have 'province_name,' and you can populate the combobox
            village_combobox.set(village_name)  # Assuming you've created a StringVar for the combobox
        else:
            village_combobox.set("Unknown")  # Set a default value if province is not found

        education = data[23]
        # Assuming 'province_id' is at index 20
        # Query the 'province' table to get the 'province_name'
        cursor.execute("SELECT education FROM education WHERE edu_id = :edu_id", {'edu_id': edu_id})
        education_data = cursor.fetchone()
        if education_data:
            education = education_data[0]  # Assuming 'name' is the column name for province_name

            # Now you have 'province_name,' and you can populate the combobox
            education_combobox.set(education)  # Assuming you've created a StringVar for the combobox
        else:
            education_combobox.set("Unknown")  # Set a default value if province is not found

        district_name = data[21]  # Assuming 'province_id' is at index 20
        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        fathername_entry.delete(0, tk.END)
        father_lastname_entry.delete(0, tk.END)
        grand_father_name_entry.delete(0, tk.END)
        grand_father_last_name_entry.delete(0, tk.END)
        mother_name_entry.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
        email_address_entry.delete(0, tk.END)
        native_language_entry.delete(0, tk.END)
        foreign_language_entry.delete(0, tk.END)
        internal_language_entry.delete(0, tk.END)
        blood_group_entry.delete(0, tk.END)
        nationality_entry.delete(0, tk.END)
        religion_entry.delete(0, tk.END)
        faith_entry.delete(0, tk.END)
        disability_type_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        voting_place_entry.delete(0, tk.END)
        province_name_entry.delete(0, tk.END)
        district_name_entry.delete(0, tk.END)
        village_name_entry.delete(0, tk.END)
        education_entry.delete(0, tk.END)
        pro_name2_entry.delete(0, tk.END)

        firstname_entry.insert(0, firstname)
        lastname_entry.insert(0, lastname)
        fathername_entry.insert(0, fathername)
        father_lastname_entry.insert(0, father_lastname)
        grand_father_name_entry.insert(0, grand_father_name)
        grand_father_last_name_entry.insert(0, grand_father_last_name)
        mother_name_entry.insert(0, mother_name)
        religion_entry.insert(0, religion)
        faith_entry.insert(0, faith)
        gender_entry.insert(0, gender)
        province_name_entry.insert(0, province_name)
        district_name_entry.insert(0, district_name)
        village_name_entry.insert(0, village_name)
        pro_name2_entry.insert(0, pro_name2)

        global current_photo
        current_photo = photo.read()  # Store the current photo bytes

        # Extract the bytes from the cx_Oracle.LOB object
        photo_bytes = BytesIO(current_photo)
        image = Image.open(photo_bytes)

        # Resize the image (e.g., to a specific width and height)
        new_width = 50  # Adjust this to your desired width
        new_height = 50  # Adjust this to your desired height
        image = image.resize((new_width, new_height), Image.BILINEAR)

        # Convert the resized image to a PhotoImage
        photo_img = ImageTk.PhotoImage(image)

        # Update the photo label
        photo_label.config(image=photo_img)
        photo_label.photo = photo_img  # Keep a reference to prevent the image from being garbage collected
        #military_service_entry.insert(0, military_service)

        if phone_number is None:
            phone_number_entry.delete(0, tk.END)
            phone_label.config(text="No phone number available for this ID")
        else:
            phone_number_entry.delete(0, tk.END)
            phone_number_entry.insert(0, phone_number)

        if email_address is None:
            email_address_entry.delete(0, tk.END)
            email_address_label.config(text="No email address available for this ID")
        else:
            email_address_entry.delete(0, tk.END)
            email_address_entry.insert(0, email_address)

        if native_language is None:
            native_language_entry.delete(0, tk.END)
            native_language_label.config(text="No native language available for this ID")
        else:
            native_language_entry.delete(0, tk.END)
            native_language_entry.insert(0, native_language)

        if foreign_language is None:
            foreign_language_entry.delete(0, tk.END)
            foreign_language_label.config(text="No foreign language available for this ID")
        else:
            foreign_language_entry.delete(0, tk.END)
            foreign_language_entry.insert(0, foreign_language)

        if internal_language is None:
            internal_language_entry.delete(0, tk.END)
            internal_language_label.config(text="No Internal  language available for this ID")
        else:
            internal_language_entry.delete(0, tk.END)
            internal_language_entry.insert(0, internal_language)

        if blood_group is None:
            blood_group_entry.delete(0, tk.END)
            blood_group_label.config(text="No Blood Group available for this ID")
        else:
            blood_group_entry.delete(0, tk.END)
            blood_group_entry.insert(0, blood_group)

        if nationality is None:
            nationality_entry.delete(0, tk.END)
            nationality_label.config(text="No nationality available for this ID")
        else:
            nationality_entry.delete(0, tk.END)
            nationality_entry.insert(0, nationality)

        if disability_type is None:
            disability_type_entry.delete(0, tk.END)
            disability_type_label.config(text="No disability_type available for this ID")
        else:
            disability_type_entry.delete(0, tk.END)
            disability_type_entry.insert(0, disability_type)

        if voting_place is None:
            voting_place_entry.delete(0, tk.END)
            voting_place_label.config(text="No voting_place available for this ID")
        else:
            voting_place_entry.delete(0, tk.END)
            voting_place_entry.insert(0, voting_place)
    else:
        result_label.config(text="No data found for this ID")

    cursor.close()
    connection.close()


# Function to populate the combobox with province names
def populate_province_combobox():
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all province names from the 'province' table
    cursor.execute("SELECT name FROM province")
    province_names = [row[0] for row in cursor.fetchall()]

    # Set the values of the province_combobox
    province_combobox['values'] = province_names

    cursor.close()
    connection.close()


# Function to populate the combobox with province names
def populate_district_combobox():
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all province names from the 'province' table
    cursor.execute("SELECT name FROM district")
    district_names = [row[0] for row in cursor.fetchall()]

    # Set the values of the province_combobox
    district_combobox['values'] = district_names

    cursor.close()
    connection.close()


# Function to select a new photo from the file system
# Function to select a new photo from the file system

# Function to populate the combobox with province names
def populate_village_combobox():
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all province names from the 'province' table
    cursor.execute("SELECT name FROM village")
    village_names = [row[0] for row in cursor.fetchall()]

    # Set the values of the province_combobox
    village_combobox['values'] = village_names

    cursor.close()
    connection.close()


def populate_education_combobox():
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all province names from the 'province' table
    cursor.execute("SELECT education FROM education")
    education = [row[0] for row in cursor.fetchall()]

    # Set the values of the province_combobox
    education_combobox['values'] = education

    cursor.close()
    connection.close()


def populate_province_combobox1():
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all province names from the 'province' table
    cursor.execute("SELECT name FROM province")
    province_names = [row[0] for row in cursor.fetchall()]

    # Set the values of the province_combobox
    province_combobox['values'] = province_names

    cursor.close()
    connection.close()


def select_photo():
    global new_photo_bytes
    file_path = filedialog.askopenfilename()
    if file_path:
        new_photo_bytes = open(file_path, 'rb').read()
        update_photo(file_path)


# Function to update the displayed photo
def update_photo(file_path):
    # Open and resize the selected image
    image = Image.open(file_path)
    new_width = 50  # Adjust this to your desired width
    new_height = 50  # Adjust this to your desired height
    image = image.resize((new_width, new_height), Image.BILINEAR)

    # Convert the resized image to a PhotoImage
    photo_img = ImageTk.PhotoImage(image)

    # Update the photo label
    photo_label.config(image=photo_img)
    photo_label.photo = photo_img  # Keep a reference to prevent the image from being garbage collected


def update_data():
    start_time = time.time()
    citizen_id = id_entry.get()
    new_first_name = firstname_entry.get()
    new_last_name = lastname_entry.get()
    new_father_name = fathername_entry.get()
    new_father_lastname = father_lastname_entry.get()
    new_grand_father_name = grand_father_name_entry.get()
    new_grand_father_last_name = grand_father_last_name_entry.get()
    new_mother_name = mother_name_entry.get()
    new_phone_number = phone_number_entry.get()
    new_email_address = email_address_entry.get()
    new_native_language = native_language_entry.get()
    new_foreign_language = foreign_language_entry.get()
    new_internal_language = internal_language_entry.get()
    new_blood_group = blood_group_entry.get()
    new_nationality = nationality_entry.get()
    new_religion = religion_entry.get()
    new_faith = faith_entry.get()
    new_disability_type = disability_type_entry.get()
    new_gender = gender_entry.get()
    new_voting_place = voting_place_entry.get()

    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    global new_photo_bytes

    if new_photo_bytes:
        # Update all fields except the photo based on the entered ID
        cursor.execute(
            "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, fathername = :new_father_name, "
            "father_lastname = :new_father_lastname, grand_father_name = :new_grand_father_name, "
            "grand_father_last_name = :new_grand_father_last_name, mother_name = :new_mother_name, "
            "phone_number = :new_phone_number, email_address = :new_email_address, "
            "native_language = :new_native_language, foreign_language = :new_foreign_language, "
            "internal_language = :new_internal_language, blood_group = :new_blood_group, "
            "nationality = :new_nationality, religion = :new_religion, faith = :new_faith, "
            "disability_type = :new_disability_type, gender = :new_gender, voting_place = :new_voting_place, "
            "photo = :new_photo "  # Update photo last
            "WHERE citizen_id = :citizen_id",

            {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_father_name': new_father_name,
             'new_father_lastname': new_father_lastname, 'new_grand_father_name': new_grand_father_name,
             'new_grand_father_last_name': new_grand_father_last_name, 'new_mother_name': new_mother_name,
             'new_phone_number': new_phone_number,
             'new_email_address': new_email_address, 'new_native_language': new_native_language,
             'new_foreign_language': new_foreign_language, 'new_internal_language': new_internal_language,
             'new_blood_group': new_blood_group, 'new_nationality': new_nationality, 'new_religion': new_religion,
             'new_faith': new_faith, 'new_disability_type': new_disability_type, 'new_gender': new_gender,
             'new_voting_place': new_voting_place,
             'new_photo': new_photo_bytes, 'citizen_id': citizen_id}
        )
    else:
        # Update all fields except the photo based on the entered ID
        cursor.execute(
            "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, fathername = :new_father_name, "
            "father_lastname = :new_father_lastname, grand_father_name = :new_grand_father_name, "
            "grand_father_last_name = :new_grand_father_last_name, mother_name = :new_mother_name, "
            "phone_number = :new_phone_number, email_address = :new_email_address, "
            "native_language = :new_native_language, foreign_language = :new_foreign_language, "
            "internal_language = :new_internal_language, blood_group = :new_blood_group, "
            "nationality = :new_nationality, religion = :new_religion, faith = :new_faith, "
            "disability_type = :new_disability_type, gender = :new_gender, voting_place = :new_voting_place "
            "WHERE citizen_id = :citizen_id",

            {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_father_name': new_father_name,
             'new_father_lastname': new_father_lastname, 'new_grand_father_name': new_grand_father_name,
             'new_grand_father_last_name': new_grand_father_last_name, 'new_mother_name': new_mother_name,
             'new_phone_number': new_phone_number, 'new_email_address': new_email_address,
             'new_native_language': new_native_language, 'new_foreign_language': new_foreign_language,
             'new_internal_language': new_internal_language, 'new_blood_group': new_blood_group,
             'new_nationality': new_nationality, 'new_religion': new_religion, 'new_faith': new_faith,
             'new_disability_type': new_disability_type, 'new_gender': new_gender, 'new_voting_place': new_voting_place,
             'citizen_id': citizen_id}
        )

    connection.commit()
    cursor.close()
    connection.close()

    result_label.config(text="Data updated successfully")
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)

    time_label.config(text=f"Query run time: {total_time:.2f} seconds")



# Labels and Entry Fields using grid layout for horizontal arrangement

# Function to update the province_id when a province is selected from the combobox
def update_province_id(event):
    selected_province_name = province_combobox.get()

    # Query the database to get the province_id for the selected province_name
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute("SELECT province_id FROM province WHERE name = :selected_province_name",
                   {'selected_province_name': selected_province_name})
    result = cursor.fetchone()

    if result:
        province_id = result[0]
        # Update the province_id for the currently displayed citizen
        cursor.execute("UPDATE citizen SET province_id = :province_id WHERE citizen_id = :citizen_id",
                       {'province_id': province_id, 'citizen_id': id_entry.get()})
        connection.commit()

    cursor.close()
    connection.close()


# Function to update the province_id when a province is selected from the combobox
def update_district_id(event):
    selected_district_name = district_combobox.get()

    # Query the database to get the province_id for the selected province_name
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute("SELECT district_id FROM district WHERE name = :selected_district_name",
                   {'selected_district_name': selected_district_name})
    result = cursor.fetchone()

    if result:
        district_id = result[0]
        # Update the province_id for the currently displayed citizen
        cursor.execute("UPDATE citizen SET district_id = :district_id WHERE citizen_id = :citizen_id",
                       {'district_id': district_id, 'citizen_id': id_entry.get()})
        connection.commit()

    cursor.close()
    connection.close()


# Function to update the province_id when a province is selected from the combobox
def update_village_id(event):
    selected_village_name = village_combobox.get()

    # Query the database to get the province_id for the selected province_name
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute("SELECT village_id FROM village WHERE name = :selected_village_name",
                   {'selected_village_name': selected_village_name})
    result = cursor.fetchone()

    if result:
        village_id = result[0]
        # Update the province_id for the currently displayed citizen
        cursor.execute("UPDATE citizen SET village_id = :village_id WHERE citizen_id = :citizen_id",
                       {'village_id': village_id, 'citizen_id': id_entry.get()})
        connection.commit()

    cursor.close()
    connection.close()


# Function to update the province_id when a province is selected from the combobox
def update_education_id(event):
    selected_education_name = education_combobox.get()

    # Query the database to get the province_id for the selected province_name
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute("SELECT edu_id FROM education WHERE education = :selected_education_name",
                   {'selected_education_name': selected_education_name})
    result = cursor.fetchone()

    if result:
        edu_id = result[0]
        # Update the province_id for the currently displayed citizen
        cursor.execute("UPDATE citizen SET edu_id = :edu_id WHERE citizen_id = :citizen_id",
                       {'edu_id': edu_id, 'citizen_id': id_entry.get()})
        connection.commit()

    cursor.close()
    connection.close()


def update_province_id1(event):
    selected_province_name1 = province_combobox.get()

    # Query the database to get the province_id for the selected province_name
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute("SELECT province_id FROM province WHERE name = :selected_province_name",
                   {'selected_province_name': selected_province_name1})
    result = cursor.fetchone()

    if result:
        province_id1 = result[0]
        # Update the province_id for the currently displayed citizen
        cursor.execute(
            "UPDATE real_residence SET province_id = :province_id WHERE real_residence_id = :real_residence_id",
            {'province_id': province_id1, 'real_residence_id': id_entry.get()})
        connection.commit()

    cursor.close()
    connection.close()


label_entries = [
    ("Citizen ID:", id_entry),
    ("First Name:", firstname_entry),
    ("Last Name:", lastname_entry),
    ("Father Name:", fathername_entry),
    ("Father Last Name:", father_lastname_entry),
    ("Grand Father Name:", grand_father_name_entry),
    ("Grand Father Last Name:", grand_father_last_name_entry),
    ("Mother Name:", mother_name_entry)

]

for i, (label_text, entry_widget) in enumerate(label_entries):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry_widget.grid(row=i, column=1, padx=10, pady=5, sticky='e')

# Photo label and buttons
# Email address label and entry field in the first row and second column
phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=9, column=0, padx=10, pady=5, sticky='w')
phone_number_entry.grid(row=9, column=1, padx=10, pady=5, sticky='e')

photo_label = tk.Label(root, text="")
photo_label.grid(row=10, column=0, columnspan=2, pady=10)

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=11, column=0, pady=10)

update_button = tk.Button(root, text="Update", command=update_data)
update_button.grid(row=11, column=1, pady=10)

# Email address label and entry field in the first row and second column
email_address_label = tk.Label(root, text="Email Address:")
email_address_label.grid(row=0, column=2, padx=10, pady=5, sticky='w')
email_address_entry.grid(row=0, column=3, padx=10, pady=5, sticky='e')

# Labels for "Native Language" and "Foreign Language" in the second column
native_language_label = tk.Label(root, text="Native Language:")
native_language_label.grid(row=1, column=2, padx=10, pady=5, sticky='w')
native_language_entry.grid(row=1, column=3, padx=10, pady=5, sticky='e')

foreign_language_label = tk.Label(root, text="Foreign Language:")
foreign_language_label.grid(row=2, column=2, padx=10, pady=5, sticky='w')
foreign_language_entry.grid(row=2, column=3, padx=10, pady=5, sticky='e')

internal_language_label = tk.Label(root, text="Interal Language:")
internal_language_label.grid(row=3, column=2, padx=10, pady=5, sticky='w')
internal_language_entry.grid(row=3, column=3, padx=10, pady=5, sticky='e')

blood_group_label = tk.Label(root, text="Blood Group:")
blood_group_label.grid(row=4, column=2, padx=10, pady=5, sticky='w')
blood_group_entry.grid(row=4, column=3, padx=10, pady=5, sticky='e')

nationality_label = tk.Label(root, text="Nationality:")
nationality_label.grid(row=5, column=2, padx=10, pady=5, sticky='w')
nationality_entry.grid(row=5, column=3, padx=10, pady=5, sticky='e')

religion_label = tk.Label(root, text="Religion:")
religion_label.grid(row=6, column=2, padx=10, pady=5, sticky='w')
religion_entry.grid(row=6, column=3, padx=10, pady=5, sticky='e')

faith_label = tk.Label(root, text="Faith:")
faith_label.grid(row=7, column=2, padx=10, pady=5, sticky='w')
faith_entry.grid(row=7, column=3, padx=10, pady=5, sticky='e')

disability_type_label = tk.Label(root, text="Disability Type:")
disability_type_label.grid(row=8, column=2, padx=10, pady=5, sticky='w')
disability_type_entry.grid(row=8, column=3, padx=10, pady=5, sticky='e')

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=9, column=2, padx=10, pady=5, sticky='w')
gender_entry.grid(row=9, column=3, padx=10, pady=5, sticky='e')

voting_place_label = tk.Label(root, text="Voting Place:")
voting_place_label.grid(row=0, column=4, padx=10, pady=5, sticky='w')
voting_place_entry.grid(row=0, column=5, padx=10, pady=5, sticky='e')

# Add a combobox widget and set its initial value
province_name_label = tk.Label(root, text="Province Name:")
province_name_label.grid(row=1, column=4, padx=10, pady=5, sticky='w')
province_combobox = ttk.Combobox(root, state="readonly")
province_combobox.grid(row=1, column=5, padx=10, pady=5, sticky='e')
province_combobox.set("_____ ")
# Set a default valu
province_combobox['values'] = populate_province_combobox()
# Add a combobox widget and set its initial value
province_name_label = tk.Label(root, text="Province Name:")
province_name_label.grid(row=1, column=4, padx=10, pady=5, sticky='w')
province_combobox = ttk.Combobox(root, state="readonly")
province_combobox.grid(row=1, column=5, padx=10, pady=5, sticky='e')
# Set a default value and populate the combobox
province_combobox.set("Select a Province")
province_combobox['values'] = populate_province_combobox()  # You need to define this function
province_combobox.bind("<<ComboboxSelected>>", update_province_id)

district_name_label = tk.Label(root, text="District Name:")
district_name_label.grid(row=2, column=4, padx=10, pady=5, sticky='w')
district_combobox = ttk.Combobox(root, state="readonly")
district_combobox.grid(row=2, column=5, padx=10, pady=5, sticky='e')
district_combobox.set("_____ ")
# Set a default valu
district_combobox['values'] = populate_province_combobox()
# Add a combobox widget and set its initial value
district_name_label = tk.Label(root, text="District Name:")
district_name_label.grid(row=2, column=4, padx=10, pady=5, sticky='w')
district_combobox = ttk.Combobox(root, state="readonly")
district_combobox.grid(row=2, column=5, padx=10, pady=5, sticky='e')
# Set a default value and populate the combobox
district_combobox.set("Select a District")
district_combobox['values'] = populate_district_combobox()  # You need to define this function
district_combobox.bind("<<ComboboxSelected>>", update_district_id)

village_name_label = tk.Label(root, text="Village Name:")
village_name_label.grid(row=3, column=4, padx=10, pady=5, sticky='w')
village_combobox = ttk.Combobox(root, state="readonly")
village_combobox.grid(row=3, column=5, padx=10, pady=5, sticky='e')
village_combobox.set("_____ ")
# Set a default valu
village_combobox['values'] = populate_province_combobox()
# Add a combobox widget and set its initial value
village_name_label = tk.Label(root, text="Village Name:")
village_name_label.grid(row=3, column=4, padx=10, pady=5, sticky='w')
village_combobox = ttk.Combobox(root, state="readonly")
village_combobox.grid(row=3, column=5, padx=10, pady=5, sticky='e')
# Set a default value and populate the combobox
village_combobox.set("Select a Village")
village_combobox['values'] = populate_village_combobox()  # You need to define this function
village_combobox.bind("<<ComboboxSelected>>", update_village_id)

education_label = tk.Label(root, text="Education:")
education_label.grid(row=4, column=4, padx=10, pady=5, sticky='w')
education_combobox = ttk.Combobox(root, state="readonly")
education_combobox.grid(row=4, column=5, padx=10, pady=5, sticky='e')
education_combobox.set("_____ ")
# Set a default valu
education_combobox['values'] = populate_province_combobox()
# Add a combobox widget and set its initial value
education_label = tk.Label(root, text="Education:")
education_label.grid(row=4, column=4, padx=10, pady=5, sticky='w')
education_combobox = ttk.Combobox(root, state="readonly")
education_combobox.grid(row=4, column=5, padx=10, pady=5, sticky='e')
# Set a default value and populate the combobox
education_combobox.set("Select a Education")
education_combobox['values'] = populate_education_combobox()  # You need to define this function
education_combobox.bind("<<ComboboxSelected>>", update_education_id)

photo_label.bind("<Button-1>", lambda event: select_photo())

result_label = tk.Label(root, text="")
result_label.grid(row=len(label_entries) + 7, column=0, columnspan=2)

time_label = tk.Label(root, text="")
time_label.grid(row=len(label_entries) + 8, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
