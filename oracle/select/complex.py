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
        c.gender,c.voting_place,p.province_id, p.name,d.district_id,d.name,v.village_id, v.name,d.date_birth_id,
        TO_CHAR(d.birth_year) || '-' || TO_CHAR(d.birth_month) || '-' || TO_CHAR(d.birth_day) AS concatenated_date,
        e.edu_id,e.education,r.real_residence_id,p1.name,d1.name,v1.name,c1.current_id,p2.name,d2.name,v2.name,
        c2.civil_status_id,c2.civil_statu,k.kochi_id,s3.summer_id,w3.winter_id,p3.province_id,p3.name,d3.district_id,d3.name,
        p4.province_id,p4.name,d4.district_id,d4.name,j.job_id,j.job_name,s4.se_na_id,s4.name_country,
        p5.paper_id,p5.year,p5.volume,p5.page_no,p5.registeration_no,p5.sukuk_no,
        p6.paper_place_id,p6.date1,p7.province_id,p7.name,d5.district_id,d5.name,
        s4.self_confirmation_id,s4.date1,s5.signature_citizen_id,s5.photo,
        f.finger_print_citizen_id,f.photo,g.gen_id,g.firstname,g.lastname,g.fathername,g.father_lastname,f1.finger_print_confirmer_id,f1.photo,
        s6.signature_confirmer_id,s6.photo,e1.electronic_id_card,e1.idcard_number,p7.paper_id,p7.year,p7.volume,p7.page_no,p7.registeration_no,p7.sukuk_no
        FROM citizen c
        INNER JOIN province p ON c.province_id = p.province_id
        INNER JOIN district d ON c.district_id = d.district_id
        INNER JOIN village v ON c.village_id = v.village_id
        INNER JOIN date_birth d ON c.date_birth_id = d.date_birth_id
        INNER JOIN education e ON c.edu_id = e.edu_id
        INNER JOIN real_residence r ON c.real_residence_id = r.real_residence_id
        INNER JOIN province p1 ON r.province_id = p1.province_id
        INNER JOIN district d1 ON r.district_id = d1.district_id
        INNER JOIN village v1 ON r.village_id = v1.village_id
        INNER JOIN current_station c1 ON c.current_id = c1.current_id
        INNER JOIN province p2 ON c1.province_id = p2.province_id
        INNER JOIN district d2 ON c1.district_id = d2.district_id
        INNER JOIN village v2 ON c1.village_id = v2.village_id
        INNER JOIN civil_status c2 ON c.civil_status_id = c2.civil_status_id
        LEFT JOIN kochi k ON c.kochi_id = k.kochi_id
        LEFT JOIN summer s3 ON k.summer_id = s3.summer_id
        LEFT JOIN winter w3 ON k.winter_id = w3.winter_id
        LEFT JOIN province p3 ON s3.province_id = p3.province_id
        LEFT JOIN district d3 ON s3.district_id = d3.district_id
        LEFT JOIN province p4 ON w3.province_id = p4.province_id
        LEFT JOIN district d4 ON w3.district_id = d4.district_id
        LEFT JOIN job j ON c.job_id = j.job_id
        LEFT JOIN second_nature s4 ON c.se_na_id = s4.se_na_id
        LEFT JOIN paper_id p5 ON c.paper_id = p5.paper_id
        LEFT JOIN paper_id_place p6 ON c.paper_place_id = p6.paper_place_id
        LEFT JOIN province p7 ON p6.province_id = p7.province_id
        LEFT JOIN district d5 ON p6.district_id = d5.district_id
        LEFT JOIN self_confirmation s4 ON c.self_confirmation_id = s4.self_confirmation_id
        LEFT JOIN signature_citizen s5 ON s4.signature_citizen_id = s5.signature_citizen_id
        LEFT JOIN finger_print_citizen f ON s4.finger_print_citizen_id = f.finger_print_citizen_id
        LEFT JOIN general_confirmation g ON c.gen_id = g.gen_id
        LEFT JOIN finger_print_confirmer f1 ON g.finger_print_confirmer_id = f1.finger_print_confirmer_id
        LEFT JOIN signature_confirmer s6 ON g.signature_confirmer_id = s6.signature_confirmer_id
        LEFT JOIN electronic_idcard e1 ON g.electronic_id_card = e1.electronic_id_card
        LEFT JOIN paper_id p7 ON g.paper_id = p7.paper_id


        WHERE c.citizen_id = :user_input_id
        """

        cursor = connection.cursor()
        cursor.execute(sql_query, user_input_id=user_input_id)

        result = cursor.fetchone()
        print(result)

        if result:

            citizen_id, firstname, lastname, fathername, father_lastname, grand_father_name, grand_father_last_name, mother_name, citizen_image_path, military_service, phone_number, email_address, native_language, foreign_language, internal_language, blood_group, nationality, religion, faith, disability_type, gender, voting_place, province_id, name, district_id, district_name, village_id, village_name, date_birth_id, concatenated_date, edu_id, education, real_residence_id, province_name1, district_name1, village_name1, current_id, province_name2, district_name2, village_name2,civil_status_id,civil_statu,kochi_id,summer_id,winter_id,province_id,province_name3,district_id,district_name3,province_id,province_name4,district_id,district_name4,job_id,job_name,se_na_id,name_country,paper_id,year,volume,page_no,registeration_no,sukuk_no,paper_place_id,date1,province_id,name5,district_id,dis_name5,self_confirmation_id,date2,signature_citizen_id,signature_photo,finger_print_citizen_id,finger_photo1,gen_id,firstname,lastname,fathername,father_lastname,finger_print_confirmer_id,photo,signature_confirmer_id,photo,electronic_id_card,idcard_number,paper_id,year,volume,page_no,registeration_no,sukuk_no = result

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
            citizen_date_of_birth_label.config(text=f"Date_birth : {concatenated_date}")
            citizen_education_label.config(text=f"Education : {education}")
            citizen_real_residence_label.config(text=f"Real Residence : {province_name1},{district_name1},{village_name1}")
            citizen_current_station_label.config(text=f"Current Residence : {province_name2},{district_name2},{village_name2}")
            citizen_civil_statu_label.config(text=f"Civil Statu : {civil_statu}")
            citizen_date_label.config(text=f"Date : {date2}")

            # Load and display the student's image
            # gen_id,firstname,lastname,fathername,father_lastname,finger_print_confirmer_id,photo,signature_confirmer_id,photo,electronic_id_card,idcard_number,paper_id,year,volume,page_no,registeration_no,sukuk_no

            student_image = Image.open(citizen_image_path)
            student_image = student_image.resize((30, 30))  # Adjust the size as needed
            student_image = ImageTk.PhotoImage(student_image)
            image_label.config(image=student_image)
            image_label.image = student_image  # To prevent garbage collection




            citizen_Kochi_Summer_label.config(text=f"Kochi Summer : {province_name3},{district_name3}")

            citizen_Kochi_Winter_label.config(text=f"Kochi Winter : {province_name4},{district_name4}")

            citizen_job_label.config(text=f"Job : {job_name}")
            citizen_name_country_label.config(text=f"Country Name : {name_country}")
            citizen_paper_id_label.config(text=f"Paper ID : {year},{volume},{page_no},{registeration_no},{sukuk_no}")
            citizen_paper_id_place_label.config(text=f"Paper ID Place : {date1},{name5},{dis_name5}")
            citizen_gen_first_info_label.config(text=f"gen first info : {firstname},{lastname},{fathername},{father_lastname}")

            if signature_photo:
                try:
                    # Check if signature_photo is an image path or image object
                    if isinstance(signature_photo, str):
                        # Load and display the signature image
                        signature_photo_image = Image.open(signature_photo)
                        signature_photo_image = signature_photo_image.resize((30, 30))  # Adjust the size as needed
                        signature_photo_image = ImageTk.PhotoImage(signature_photo_image)
                        image1_label.config(image=signature_photo_image)
                        image1_label.image = signature_photo_image  # To prevent garbage collection
                    elif isinstance(signature_photo, cx_Oracle.LOB):
                        # Handle if signature_photo is a BLOB object
                        signature_photo_data = signature_photo.read()
                        signature_photo_image = Image.open(io.BytesIO(signature_photo_data))
                        signature_photo_image = signature_photo_image.resize((30, 30))  # Adjust the size as needed
                        signature_photo_image = ImageTk.PhotoImage(signature_photo_image)
                        image1_label.config(image=signature_photo_image)
                        image1_label.image = signature_photo_image  # To prevent garbage collection
                except Exception as e:
                    result_label.config(text=f"Error loading signature photo: {e}")
            else:
                # Handle the case when signature_photo is None
                image1_label.config(image=None)

            if finger_photo1:
                try:
                    # Check if finger_photo1 is an image path or image object
                    if isinstance(finger_photo1, str):
                        # Load and display the finger image
                        finger_photo_image = Image.open(finger_photo1)
                        finger_photo_image = finger_photo_image.resize((30, 30))  # Adjust the size as needed
                        finger_photo_image = ImageTk.PhotoImage(finger_photo_image)
                        image2_label.config(image=finger_photo_image)
                        image2_label.image = finger_photo_image  # To prevent garbage collection
                    elif isinstance(finger_photo1, cx_Oracle.LOB):
                        # Handle if finger_photo1 is a BLOB object
                        finger_photo_data = finger_photo1.read()
                        finger_photo_image = Image.open(io.BytesIO(finger_photo_data))
                        finger_photo_image = finger_photo_image.resize((30, 30))  # Adjust the size as needed
                        finger_photo_image = ImageTk.PhotoImage(finger_photo_image)
                        image2_label.config(image=finger_photo_image)
                        image2_label.image = finger_photo_image  # To prevent garbage collection
                except Exception as e:
                    result_label.config(text=f"Error loading finger photo: {e}")
            else:
                # Handle the case when finger_photo1 is None
                image2_label.config(image=None)
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

citizen_date_of_birth_label = Label(window, text="Date_Birth:", font=('Helvetica', 10))
citizen_date_of_birth_label.grid(row=9, column=1, padx=10, pady=10, sticky='w')

citizen_education_label = Label(window, text="Education:", font=('Helvetica', 10))
citizen_education_label.grid(row=10, column=1, padx=10, pady=10, sticky='w')

citizen_real_residence_label = Label(window, text="Real Residence:", font=('Helvetica', 10))

citizen_real_residence_label.grid(row=11, column=1, padx=10, pady=10, sticky='w')

citizen_current_station_label = Label(window, text="Current Residence:", font=('Helvetica', 10))
citizen_current_station_label.grid(row=12, column=1, padx=10, pady=10, sticky='w')

citizen_civil_statu_label = Label(window, text="Civil Status :", font=('Helvetica', 10))
citizen_civil_statu_label.grid(row=13, column=1, padx=10, pady=10, sticky='w')

citizen_Kochi_Summer_label = Label(window, text="Kochi Summer :", font=('Helvetica', 10))
citizen_Kochi_Summer_label.grid(row=14, column=1, padx=10, pady=10, sticky='w')

citizen_Kochi_Winter_label = Label(window, text="Kochi Winter :", font=('Helvetica', 10))
citizen_Kochi_Winter_label.grid(row=1, column=2, padx=10, pady=10, sticky='w')



citizen_job_label = Label(window, text="Job Nmae :", font=('Helvetica', 10))
citizen_job_label.grid(row=2, column=2, padx=10, pady=10, sticky='w')


citizen_name_country_label = Label(window, text="Country Name :", font=('Helvetica', 10))
citizen_name_country_label.grid(row=3, column=2, padx=10, pady=10, sticky='w')


citizen_paper_id_label = Label(window, text="Paper ID :", font=('Helvetica', 10))
citizen_paper_id_label.grid(row=4, column=2, padx=10, pady=10, sticky='w')



citizen_paper_id_place_label = Label(window, text="Paper ID Place :", font=('Helvetica', 10))
citizen_paper_id_place_label.grid(row=5, column=2, padx=10, pady=10, sticky='w')



citizen_date_label = Label(window,text="Date :", font=('Helvetica', 10))
citizen_date_label.grid(row=6, column=2, padx=10, pady=10, sticky='w')

signature_photo_label = Label(window,text="Self Signature:", font=('Helvetica', 10))
signature_photo_label.grid(row=7, column=2, padx=10, pady=10, sticky='w')  # Align to the right


image1_label = Label(window)
image1_label.grid(row=7, column=2, padx=10, pady=10)




finger_photo_label = Label(window, text="Self Finger :", font=('Helvetica', 10))
finger_photo_label.grid(row=9, column=2, padx=10, pady=10, sticky='w')


image2_label = Label(window)
image2_label.grid(row=9, column=2, padx=10, pady=10)

citizen_gen_first_info_label = Label(window, text="Gen first Info :", font=('Helvetica', 10))
citizen_gen_first_info_label.grid(row=10, column=2, padx=10, pady=10, sticky='w')

result_label = Label(window, text="", font=('Helvetica', 10))
result_label.grid(row=11, column=2, columnspan=3, padx=10, pady=10)


time_label = Label(window, text="", font=('Helvetica', 10))
time_label.grid(row=12, column=2, columnspan=3, padx=10, pady=10)



window.mainloop()

