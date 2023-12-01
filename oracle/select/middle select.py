import cx_Oracle
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
from tkinter import Label, Entry, Button
import io
import time

# start time
# Function to fetch and display citizen data
def fetch_citizen_data():
    start_time = time.time()

    user_input_id = int(id_entry.get())

    try:
        # Connect to the Oracle database
        connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")

        # Define the SQL query to select citizen data
        sql_query = """
        SELECT c.citizen_id, c.firstname, c.lastname, c.fathername, c.father_lastname, c.grand_father_name, grand_father_last_name,
        mother_name, c.photo, c.military_service, c.phone_number, c.email_address, c.native_language,
        c.foreign_language, c.internal_language,c.blood_group, c.nationality,c.religion,c.faith,c.disability_type,
        c.gender,c.voting_place,p.province_id, p.name,d.district_id,d.name,v.village_id, v.name
        FROM citizen c
        INNER JOIN province p ON c.province_id = p.province_id
        INNER JOIN district d ON c.district_id = d.district_id
        INNER JOIN village v ON c.village_id = v.village_id



        WHERE c.citizen_id = :user_input_id
        """

        cursor = connection.cursor()
        cursor.execute(sql_query, user_input_id=user_input_id)

        result = cursor.fetchone()
        print(result)

        if result:

            citizen_id, firstname, lastname, fathername, father_lastname, grand_father_name, grand_father_last_name, mother_name, citizen_image_path, military_service, phone_number, email_address, native_language, foreign_language, internal_language, blood_group, nationality, religion, faith, disability_type, gender, voting_place, province_id, name, district_id, district_name, village_id, village_name = result

            citizen_id_label.config(text=f"Citizen ID: {citizen_id}")
            citizen_firstname_label.config(text=f"First Name: {firstname}")
            citizen_lastname_label.config(text=f"Last Name: {lastname}")
            citizen_fathername_label.config(text=f"Father Name: {fathername}")
            citizen_father_lastname_label.config(text=f"Father Last Name: {father_lastname}")
            citizen_grand_father_name_label.config(text=f"Grand Father  Name: {grand_father_name}")
            citizen_grand_father_last_name_label.config(text=f"Grand Father Last Name: {grand_father_last_name}")
            citizen_mother_name_label.config(text=f"Mother Name: {mother_name}")
            citizen_military_service_label.config(text=f"Military Service: {military_service}")
            citizen_phone_number_label.config(text=f"Phone Number: {phone_number}")
            citizen_email_address_label.config(text=f"Email Address: {email_address}")
            citizen_native_language_label.config(text=f"Native Language: {native_language}")
            citizen_foreign_language_label.config(text=f"Foreign Language: {foreign_language}")
            citizen_internal_language_label.config(text=f"Internal Language: {internal_language}")
            citizen_blood_group_label.config(text=f"Blood Group: {blood_group}")
            citizen_nationality_label.config(text=f"Nationality: {nationality}")
            citizen_religion_label.config(text=f"Religion: {religion}")
            citizen_faith_label.config(text=f"Faith: {faith}")
            citizen_disability_type_label.config(text=f"Disability Type : {disability_type}")
            citizen_gender_label.config(text=f"Gender : {gender}")
            citizen_voting_place_label.config(text=f"Voting Place : {voting_place}")

            # Load and display the student's image
            # gen_id,firstname,lastname,fathername,father_lastname,finger_print_confirmer_id,photo,signature_confirmer_id,photo,electronic_id_card,idcard_number,paper_id,year,volume,page_no,registeration_no,sukuk_no

            student_image = Image.open(citizen_image_path)
            student_image = student_image.resize((30, 30))  # Adjust the size as needed
            student_image = ImageTk.PhotoImage(student_image)
            image_label.config(image=student_image)
            image_label.image = student_image  # To prevent garbage collection

            end_time = time.time()
            total_time = end_time-start_time
            print(total_time)

            time_label.config(text=f" Query run time: {total_time:.2f} seconds")





        else:
            result_label.config(text="Citizen not found.")

        # Close the cursor and the database connection
        cursor.close()
        connection.close()
    except cx_Oracle.Error as error:
        result_label.config(text=f"Database Error: {error}")

# Create a tkinter window
window = tk.Tk()
window.title("Citizen Information")
window.geometry("1200x1200")
# Create and pack tkinter widgets using the grid manager
id_label = Label(window, text="Citizen ID:", font=('Helvetica', 10))
id_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

id_entry = Entry(window, font=('Helvetica', 10))
id_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = Button(window, text="Search Button", command=fetch_citizen_data, font=("Helvetica", 10), bg="green",
                      fg="white", relief=tk.RAISED, padx=5, pady=5)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

# Labels for citizen data
citizen_id_label = Label(window, text="Citizen ID:", font=('Helvetica', 10))
citizen_id_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

citizen_firstname_label = Label(window, text="First Name:", font=('Helvetica', 10))
citizen_firstname_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

citizen_lastname_label = Label(window, text="Last Name:", font=('Helvetica', 10))
citizen_lastname_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

citizen_fathername_label = Label(window, text="Father Name:", font=('Helvetica', 10))
citizen_fathername_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')

citizen_father_lastname_label = Label(window, text="Father Last Name:", font=('Helvetica', 10))
citizen_father_lastname_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

citizen_grand_father_name_label = Label(window, text="Grand Father Name:", font=('Helvetica', 10))
citizen_grand_father_name_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

citizen_grand_father_last_name_label = Label(window, text="Grand Father Last  Name:", font=('Helvetica', 10))
citizen_grand_father_last_name_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')

citizen_mother_name_label = Label(window, text="Mother Name:", font=('Helvetica', 10))
citizen_mother_name_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')

# Labels to display student's image and class photo
citizen_image_label = Label(window, text="Citizen Image:", font=('Helvetica', 10))
citizen_image_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')  # Align to the right

image_label = Label(window)
image_label.grid(row=9, column=0, padx=10, pady=10)

citizen_military_service_label = Label(window, text="Military Service:", font=('Helvetica', 10))
citizen_military_service_label.grid(row=10, column=0, padx=10, pady=10, sticky='w')  # Align to the right

citizen_phone_number_label = Label(window, text="Phone Number:", font=('Helvetica', 10))
citizen_phone_number_label.grid(row=11, column=0, padx=10, pady=10, sticky='w')  # Align to the right

citizen_email_address_label = Label(window, text="Email Address:", font=('Helvetica', 10))
citizen_email_address_label.grid(row=12, column=0, padx=10, pady=10, sticky='w')  # Align to the right

citizen_native_language_label = Label(window, text="Native Language:", font=('Helvetica', 10))
citizen_native_language_label.grid(row=13, column=0, padx=10, pady=10, sticky='w')  # Align to the right

citizen_foreign_language_label = Label(window, text="Foreign Language:", font=('Helvetica', 10))
citizen_foreign_language_label.grid(row=14, column=0, padx=10, pady=10,
                                    sticky='w')  # Align to the right internal_language

citizen_internal_language_label = Label(window, text="Internal Language:", font=('Helvetica', 10))
citizen_internal_language_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')  # Align to the right blood_group

citizen_blood_group_label = Label(window, text="Blood Group :", font=('Helvetica', 10))
citizen_blood_group_label.grid(row=2, column=1, padx=10, pady=10,
                               sticky='w')  # Align to the right blood_group nationality

citizen_nationality_label = Label(window, text="Nationality :", font=('Helvetica', 10))
citizen_nationality_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Align to the right blood_group nationality


citizen_religion_label = Label(window, text="Religion:", font=('Helvetica', 10))
citizen_religion_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

citizen_faith_label = Label(window, text="Faith:", font=('Helvetica', 10))
citizen_faith_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

citizen_disability_type_label = Label(window, text="Disability Type:", font=('Helvetica', 10))
citizen_disability_type_label.grid(row=6, column=1, padx=10, pady=10, sticky='w')

citizen_gender_label = Label(window, text="gender:", font=('Helvetica', 10))
citizen_gender_label.grid(row=7, column=1, padx=10, pady=10, sticky='w')

citizen_voting_place_label = Label(window, text="voting_place:", font=('Helvetica', 10))
citizen_voting_place_label.grid(row=8, column=1, padx=10, pady=10, sticky='w')

# citizen_province_label = Label(window, text="Province Name:", font=('Helvetica', 14))
# citizen_province_label.grid(row=11, column=1, padx=10, pady=10, sticky='w')

# citizen_district_label = Label(window, text="District Name:", font=('Helvetica', 14))
# citizen_district_label.grid(row=12, column=1, padx=10, pady=10, sticky='w')

# citizen_village_label = Label(window, text="Village Name:", font=('Helvetica', 14))
# citizen_village_label.grid(row=1, column=3, padx=10, pady=10, sticky='w')
result_label = Label(window, text="", font=('Helvetica', 10))
result_label.grid(row=11, column=2, columnspan=3, padx=10, pady=10)


time_label = Label(window, text="", font=('Helvetica', 10))
time_label.grid(row=12, column=2, columnspan=3, padx=10, pady=10)



window.mainloop()

