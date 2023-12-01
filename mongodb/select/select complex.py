import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import Tk,Label
from bson import ObjectId
import pymongo
from PIL import Image, ImageTk
import io
import time

# start time


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NSIA"]  # Replace with your actual database name
collection = db["citiz"]  # Replace with your actual collection name


# Create a Tkinter window
# start time
# Function to fetch data by ID (you can define this below)
def fetch_data_by_id():
    user_input = entry.get()
    start_time = time.time()

    # Get user input from the Entry widget

    # Accept user input for the target student_id
    #target_student_id = input("Enter the student_id to search for: ")

    try:
        # Create an ObjectId from the user input
        #document_id = ObjectId(user_input.strip())  # Remove leading/trailing spaces
        result = collection.find_one({"citizen_id": user_input})
        #result = collection.find_one({"_id": document_id})

        if result:

            # Extract and display the province name from the MongoDB document
            first_name = result.get("first_name", "not found")
            result_label1.config(text=f"First Name: {first_name}")

            province_id = result.get("Province_id", None)
            if province_id:
                province_data = db["province"].find_one({"_id": province_id})
                province_name = province_data.get("province_name", "not Found")
                result_label23.config(text = f"Province Name :{province_name}")

            district_id = result.get("District_id",None)
            if district_id:
                district_data = db["district"].find_one({"_id":district_id})
                district_name = district_data.get("district_name","not Found")
                result_label24.config(text = f"District Name :{district_name}")


            #Village_id

            village_id = result.get("Village_id",None)
            if village_id:
                village_data = db["village"].find_one({"_id":village_id})
                village_name = village_data.get("village_name","not Found")
                result_label25.config(text = f"Village Name :{village_name}")


            birth_id = result.get("date_of_birth_id",None)
            if birth_id:
                birth_data = db["date_of_birth"].find_one({"_id":birth_id})
                birth_date = birth_data.get("birth_date","not Found")
                result_label26.config(text = f"Date Of Birth :{birth_date}")

            edu_id = result.get("Education",None)
            if edu_id:
                edu_data = db["education"].find_one({"_id":edu_id})
                edu = edu_data.get("edu","not Found")
                result_label27.config(text = f"Education :{edu}")

               # if province_id:
                #    province_data = db["province"].find_one({"_id": province_id})
                 #   province_name = province_data.get("province_name", "not Found")
                  #  result_label28.config(text=f"Province Name :{province_name}")

            real_id = result.get("real_residence_id", None)

            if real_id:
                # Query the "real_re" collection to retrieve the province_id
                real_re_data = db["real_residence"].find_one({"_id": real_id})

                if real_re_data:
                    province_id = real_re_data.get("province_id", None)
                    district_id = real_re_data.get("district_id", None)
                    if province_id and district_id:
                        # Query the "province" collection to retrieve the province_name
                        province_data = db["province"].find_one({"_id": province_id})
                        district_data = db["district"].find_one({"_id": district_id})

                        province_name = province_data.get("province_name", "Not Found")
                        district_name = district_data.get("district_name", "not Found")
                        result_label28.config(text=f"Real Residence : {province_name},{district_name}")
                    else:
                        result_label28.config(text="Real Re Data Not Found")
            else:
                result_label28.config(text="Real ID Not Found")

            kochi_id = result.get("Kochi_id", None)
            if kochi_id:
                # Query the "real_re" collection to retrieve the province_id
                kochi_data = db["kochi"].find_one({"_id": kochi_id})
                if kochi_data:
                    winter_kochi_id = kochi_data.get("winter_kochi_id", None)
                    summer_kochi_id = kochi_data.get("summer_kochi_id", None)
                    if winter_kochi_id:
                        winter_data = db["winter_kochi"].find_one({"_id": winter_kochi_id})
                        if winter_data:
                            province_id = winter_data.get("province_id", None)
                            district_id = winter_data.get("district_id", None)
                            if province_id and district_id:

                                province_data = db["province"].find_one({"_id": province_id})
                                district_data = db["district"].find_one({"_id": district_id})

                                province_name = province_data.get("province_name", "Not Found")
                                district_name = district_data.get("district_name", "not Found")
                                result_label31.config(text=f" Winter Kochi: {province_name},{district_name}")
                            else:
                                result_label31.config(text="Real Re Data Not Found")
                        else:
                            result_label31.config(text="Real Re Data Not Found")
                    else:
                        result_label31.config(text="Real Re Data Not Found")
                else:
                    result_label31.config(text="Real Re Data Not Found")
            else:
                result_label31.config(text="winter Data Not Found")
            kochi_id = result.get("Kochi_id", None)
            if kochi_id:
                # Query the "real_re" collection to retrieve the province_id
                kochi_data = db["kochi"].find_one({"_id": kochi_id})
                if kochi_data:
                    summer_kochi_id = kochi_data.get("summer_kochi_id", None)
                    if summer_kochi_id:
                        summer_data = db["summer_kochi"].find_one({"_id": summer_kochi_id})
                        if summer_data:
                            province_id = summer_data.get("province_id", None)
                            district_id = summer_data.get("district_id", None)
                            if province_id and district_id:

                                province_data = db["province"].find_one({"_id": province_id})
                                district_data = db["district"].find_one({"_id": district_id})

                                province_name = province_data.get("province_name", "Not Found")
                                district_name = district_data.get("district_name", "not Found")
                                result_label32.config(text=f"Summer Kochi : {province_name},{district_name}")
                            else:
                                result_label32.config(text="Real Re Data Not Found")
                        else:
                            result_label32.config(text="Real Re Data Not Found")
                    else:
                        result_label32.config(text="Real Re Data Not Found")
                else:
                    result_label32.config(text="Real Re Data Not Found")
            else:
                result_label32.config(text="Summer data not found")


            job_id = result.get("Job_id",None)
            if job_id:
                job_data = db["job"].find_one({"_id":job_id})
                job_name = job_data.get("job_name","not Found")
                result_label33.config(text = f"Job Name :{job_name}")


            second_nature_id = result.get("second_nature_id",None)
            if second_nature_id:
                second_nature_data = db["second_nature"].find_one({"_id":second_nature_id})
                second_nature_name = second_nature_data.get("country_name","not Found")
                result_label34.config(text = f"Country Name :{second_nature_name}")



            electronic_idcard_id = result.get("electronic_idcard_id",None)
            if electronic_idcard_id:
                electronic_idcard_data = db["electronic_idcard"].find_one({"_id":electronic_idcard_id})
                electronic_idcard_name = electronic_idcard_data.get("IdCarnumber","not Found")
                result_label35.config(text = f" ID Card Number :{electronic_idcard_name}")


            self_confirmation_id = result.get("self_confirmation_id", None)

            if self_confirmation_id:
                self_confirmation_data = db["self_confirmation"].find_one({"_id": self_confirmation_id})

                if self_confirmation_data:
                    finger_print_citizen_id = self_confirmation_data.get("finger_print_citizen_id", None)
                    if finger_print_citizen_id:
                       fingerprint_data = db["finger_print_citizen"].find_one({"_id": finger_print_citizen_id})
                       if fingerprint_data:
                           fingerprint_photo = fingerprint_data.get("image", None)
                           if fingerprint_photo:
                               image = Image.open(io.BytesIO(fingerprint_photo))
                               # Resize the image to 60x60 pixels using ANTIALIAS
                               image = image.resize((60, 60), Image.NEAREST)
                               # Convert the PIL Image to a PhotoImage object
                               photo = ImageTk.PhotoImage(image)
                               # Set the PhotoImage on result_label6
                               result_label37.config(image=photo)
                               result_label37.image = photo
                               result_label37.grid(row=15, column=4, columnspan=3)

                               # Add a label for the photo
                               photo_label1.config(text="Fingerprint Citizen:")
                               photo_label1.grid(row=15, column=3, sticky="w")
                           else:
                               result_label37.grid_forget()  # Hide result_label6 if no image data is found
                               photo_label1.grid_forget()



                               # Add a label for the photo
                       else:
                            result_label37.config(text="Fingerprint Photo Not Found")
                    else:
                        result_label37.config(text="Fingerprint Photo Not Found")
                else:
                    result_label37.config(text="Fingerprint Photo Not Found")
            else:
                result_label37.config(text="Fingerprint Photo Not Found")

            self_confirmation_id = result.get("self_confirmation_id", None)

            if self_confirmation_id:
                self_confirmation_data = db["self_confirmation"].find_one({"_id": self_confirmation_id})

                if self_confirmation_data:
                    signature_citizen_id = self_confirmation_data.get("signature_citizen_id", None)
                    if signature_citizen_id:
                        signature_citizen_data = db["signature_citizen"].find_one({"_id": signature_citizen_id})
                        if signature_citizen_data:
                            signature_photo = signature_citizen_data.get("image", None)
                            if signature_photo:
                                image = Image.open(io.BytesIO(signature_photo))
                                # Resize the image to 60x60 pixels using ANTIALIAS
                                image = image.resize((50, 50), Image.NEAREST)
                                # Convert the PIL Image to a PhotoImage object
                                photo = ImageTk.PhotoImage(image)
                                # Set the PhotoImage on result_label6
                                result_label38.config(image=photo)
                                result_label38.image = photo
                                result_label38.grid(row=17, column=5, columnspan=3)

                                # Add a label for the photo
                                photo_label2.config(text="Signature Citizen:")
                                photo_label2.grid(row=17, column=3, sticky="w")
                            else:
                                result_label38.grid_forget()  # Hide result_label6 if no image data is found
                                photo_label2.grid_forget()

                                # Add a label for the photo
                        else:
                            result_label38.config(text="Fingerprint Photo Not Found")
                    else:
                        result_label38.config(text="Fingerprint Photo Not Found")
                else:
                    result_label38.config(text="Fingerprint Photo Not Found")
            else:
                result_label38.config(text="Fingerprint Photo Not Found")

            cur_id = result.get("current_residence_id", None)

            if cur_id:
                # Query the "real_re" collection to retrieve the province_id
                cur_re_data = db["current_residence"].find_one({"_id": cur_id})

                if cur_re_data:
                    province_id = cur_re_data.get("province_id", None)
                    district_id = cur_re_data.get("district_id", None)
                    if province_id and district_id:
                        # Query the "province" collection to retrieve the province_name
                        province_data = db["province"].find_one({"_id": province_id})
                        district_data = db["district"].find_one({"_id": district_id})

                        province_name = province_data.get("province_name", "Not Found")
                        district_name = district_data.get("district_name", "not Found")
                        result_label29.config(text=f"Current Residence : {province_name},{district_name}")
                    else:
                        result_label29.config(text="Current  Data Not Found")
            else:
                result_label29.config(text="Current ID Not Found")


            civil_status_id = result.get("civil_status_id",None)
            if civil_status_id:
                civil_data = db["civil_status"].find_one({"_id":civil_status_id})
                civil_status = civil_data.get("civil_status","not Found")
                result_label30.config(text = f"civil_status :{civil_status}")
#year,volume,page_no,registeration_no,sukuk_no
            paper_id_id = result.get("paper_id_id",None)
            if paper_id_id:
                paper_data = db["paper_id"].find_one({"_id":paper_id_id})
                year_name = paper_data.get("year","not Found")
                volume_name = paper_data.get("volume","not Found")
                page_no_name = paper_data.get("page_no","not Found")
                registeration_no_name = paper_data.get("registeration_no","not Found")
                sukuk_no_name = paper_data.get("sukuk_no","not Found")
                result_label36.config(text = f"Paper ID Info :{year_name},{volume_name},{page_no_name},{registeration_no_name},{sukuk_no_name}")

            # Use "N/A" if the name field is missing
            last_name = result.get("last_name", "not found")
            result_label2.config(text=f"Last Name: {last_name}")

            fathername = result.get("fathername", "not found")
            result_label3.config(text=f"Father Name: {fathername}")

            father_last_name = result.get("father_last_name", "not found")
            result_label4.config(text=f"Father Last Name: {father_last_name}")
            # grand_father_name

            grand_father_name = result.get("grand_father_name", "not found")
            result_label5.config(text=f"Grand Father Name: {grand_father_name}")

            # grand_father_last_name
            grand_father_last_name = result.get("grand_father_last_name", "not found")
            result_label6.config(text=f"Grand Father Last Name: {grand_father_last_name}")
            # mother_name

            mother_name = result.get("mother_name", "not found")
            result_label7.config(text=f"Mother Name: {mother_name}")

            # ID_Card_NO

            ID_Card_NO = result.get("ID_Card_NO", "not found")
            result_label8.config(text=f"ID_Card_NO : {ID_Card_NO}")

            # militry_service

            militry_service = result.get("militry_service", "not found")
            result_label9.config(text=f"militry_service : {militry_service}")

            ##phone_number

            phone_number = result.get("phone_number", "not found")
            result_label10.config(text=f"phone_number : {phone_number}")

            ##Email_address

            Email_address = result.get("Email_address", "not found")
            result_label11.config(text=f"Email_address : {Email_address}")
            # Native_language

            Native_language = result.get("Native_language", "not found")
            result_label12.config(text=f"Native_language : {Native_language}")

            # foregin_language
            foregin_language = result.get("foregin_language", "not found")
            result_label13.config(text=f"foregin_language : {foregin_language}")

            # Retrieve the image data from the database
            # Internal_language

            Internal_language = result.get("Internal_language", "not found")
            result_label15.config(text=f"Internal_language : {Internal_language}")
            # Blood_Group

            Blood_Group = result.get("Blood_Group", "not found")
            result_label16.config(text=f"Blood_Group : {Blood_Group}")


            # Nationality
            Nationality = result.get("Nationality", "not found")
            result_label17.config(text=f"Nationality : {Nationality}")

            # Religion
            Religion = result.get("Religion", "not found")
            result_label18.config(text=f"Religion : {Religion}")

            # Faith

            Faith = result.get("Faith", "not found")
            result_label19.config(text=f"Faith : {Faith}")

            # Disability_type
            Disability_type = result.get("Disability_type", "not found")
            result_label20.config(text=f"Disability_type : {Disability_type}")

            # Gender

            Gender = result.get("Gender", "not found")
            result_label21.config(text=f"Gender : {Gender}")

            # Voting_place
            #Voting_place = result.get("Voting_place", "not found")
            #result_label22.config(text=f"Voting_place : {Voting_place}")
            # Province_id


            image_data = result.get("photo")
            if image_data:
                # Create a PIL Image object from the image data
                image = Image.open(io.BytesIO(image_data))
                # Resize the image to 60x60 pixels using ANTIALIAS
                image = image.resize((60, 60), Image.NEAREST)
                # Convert the PIL Image to a PhotoImage object
                photo = ImageTk.PhotoImage(image)
                # Set the PhotoImage on result_label6
                result_label14.config(image=photo)
                result_label14.image = photo
                result_label14.grid(row=14, column=0, columnspan=3)

                # Add a label for the photo
                photo_label.config(text="Photo:")
                photo_label.grid(row=14, column=0, sticky="w")


            else:
                result_label14.grid_forget()  # Hide result_label6 if no image data is found
                photo_label.grid_forget()  # Hide photo_label if no image data is found
            end_time = time.time()
            total_time = end_time-start_time
            print(total_time)

            time_label.config(text=f" Query run time: {total_time:.2f} seconds")

        else:
            result_label1.config(text="Document not found.")
            result_label2.config(text="Document not found.")
            result_label3.config(text="Document not found.")
            result_label4.config(text="Document not found.")
            result_label5.config(text="Document not found.")
            result_label6.config(text="Document not found.")
            result_label7.config(text="Document not found.")
            result_label8.config(text="Document not found.")
            result_label9.config(text="Document not found.")
            result_label10.config(text="Document not found.")
            result_label11.config(text="Document not found.")
            result_label12.config(text="Document not found.")
            result_label13.config(text="Document not found.")
            result_label14.grid_forget()  # Hide result_label6 if document not found
            photo_label.grid_forget()
            result_label15.config(text="Document not found.")
            result_label16.config(text="Document not found.")
            result_label17.config(text="Document not found.")
            result_label18.config(text="Document not found.")
            result_label19.config(text="Document not found.")
            result_label20.config(text="Document not found.")
            result_label21.config(text="Document not found.")
            result_label22.config(text="Document not found.")
            result_label23.config(text="Document not found.")
            result_label24.config(text="Document not found.")
            result_label25.config(text="Document not found.")
            result_label26.config(text="Document not found.")
            result_label27.config(text="Document not found.")
            result_label28.config(text="Document not found.")
            result_label29.config(text="Document not found.")
            result_label30.config(text="Document not found.")
            result_label31.config(text="Document not found.")
            result_label32.config(text="Document not found.")
            result_label33.config(text="Document not found.")
            result_label34.config(text="Document not found.")
            result_label35.config(text="Document not found.")
            result_label36.config(text="Document not found.")
            result_label37.grid_forget()  # Hide result_label6 if document not found
            photo_label1.grid_forget()
            result_label38.grid_forget()  # Hide result_label6 if document not found
            photo_label2.grid_forget()

    except Exception as e:
        result_label1.config(text=f"Error: {e}")
        result_label2.config(text=f"Error: {e}")
        result_label3.config(text=f"Error: {e}")
        result_label4.config(text=f"Error: {e}")
        result_label5.config(text=f"Error: {e}")
        result_label6.config(text=f"Error: {e}")
        result_label7.config(text=f"Error: {e}")
        result_label8.config(text=f"Error: {e}")
        result_label9.config(text=f"Error: {e}")
        result_label10.config(text=f"Error: {e}")
        result_label11.config(text=f"Error: {e}")
        result_label12.config(text=f"Error: {e}")
        result_label13.config(text=f"Error: {e}")
        result_label14.grid_forget()  # Hide result_label6 on error
        photo_label.grid_forget()
        result_label15.config(text=f"Error: {e}")
        result_label16.config(text=f"Error: {e}")
        result_label17.config(text=f"Error: {e}")
        result_label18.config(text=f"Error: {e}")
        result_label19.config(text=f"Error: {e}")
        result_label20.config(text=f"Error: {e}")
        result_label21.config(text=f"Error: {e}")
        result_label22.config(text=f"Error: {e}")
        result_label23.config(text=f"Error: {e}")
        result_label24.config(text=f"Error: {e}")
        result_label25.config(text=f"Error: {e}")
        result_label26.config(text=f"Error: {e}")
        result_label27.config(text=f"Error: {e}")
        result_label28.config(text=f"Error: {e}")
        result_label29.config(text=f"Error: {e}")
        result_label30.config(text=f"Error: {e}")
        result_label31.config(text=f"Error: {e}")
        result_label32.config(text=f"Error: {e}")
        result_label33.config(text=f"Error: {e}")
        result_label34.config(text=f"Error: {e}")
        result_label35.config(text=f"Error: {e}")
        result_label36.config(text=f"Error: {e}")
        result_label37.grid_forget()  # Hide result_label6 if document not found
        photo_label1.grid_forget()

        result_label38.grid_forget()  # Hide result_label6 if document not found
        photo_label2.grid_forget()


# Hide photo_label on error
window = tk.Tk()
window.title("MongoDB Data Retrieval by ID")

# Define a grid layout for the window
label = Label(window, text="Enter Citizen ID:", font=('Helvetica', 14))
label.grid(row=0, column=0, sticky="w")

entry = Entry(window, font=('Helvetica', 14))
entry.grid(row=0, column=1)

button = Button(window, text="Search by ID", command=fetch_data_by_id, font=('Arial', 16),
                relief=tk.RAISED, fg="white", bg="skyblue")
button.grid(row=0, column=2, sticky='w')

result_label1 = Label(window, text="", font=('Helvetica', 14))
result_label1.grid(row=1, column=0, columnspan=3, sticky='w')

result_label2 = Label(window, text="", font=('Helvetica', 14))
result_label2.grid(row=2, column=0, columnspan=3, sticky='w')

result_label3 = Label(window, text="", font=('Helvetica', 14))
result_label3.grid(row=3, column=0, columnspan=3, sticky='w')

result_label4 = Label(window, text="", font=('Helvetica', 14))
result_label4.grid(row=4, column=0, columnspan=3, sticky='w')

result_label5 = Label(window, text="", font=('Helvetica', 14))
result_label5.grid(row=5, column=0, columnspan=3, sticky='w')

result_label6 = Label(window, text="", font=('Helvetica', 14))
result_label6.grid(row=6, column=0, columnspan=3, sticky='w')

result_label7 = Label(window, text="", font=('Helvetica', 14))
result_label7.grid(row=7, column=0, columnspan=3, sticky='w')

result_label8 = Label(window, text="", font=('Helvetica', 14))
result_label8.grid(row=8, column=0, columnspan=3, sticky='w')

result_label9 = Label(window, text="", font=('Helvetica', 14))
result_label9.grid(row=9, column=0, columnspan=3, sticky='w')

result_label10 = Label(window, text="", font=('Helvetica', 14))
result_label10.grid(row=10, column=0, columnspan=3, sticky='w')

result_label11 = Label(window, text="", font=('Helvetica', 14))
result_label11.grid(row=11, column=0, columnspan=3, sticky='w')

result_label12 = Label(window, text="", font=('Helvetica', 14))
result_label12.grid(row=12, column=0, columnspan=3, sticky='w')

result_label13 = Label(window, text="", font=('Helvetica', 14))
result_label13.grid(row=13, column=0, columnspan=3, sticky='w')

result_label14 = Label(window)
result_label14.grid(row=14, column=0, columnspan=3)

photo_label = Label(window, text="", font=('Helvetica', 14))
photo_label.grid(row=14, column=0, sticky="w")

result_label15 = Label(window, text="", font=('Helvetica', 14))
result_label15.grid(row=15, column=0, columnspan=3, sticky='w')

result_label16 = Label(window, text="", font=('Helvetica', 14))
result_label16.grid(row=16, column=0, columnspan=3, sticky='w')

result_label17 = Label(window, text="", font=('Helvetica', 14))
result_label17.grid(row=17, column=0, columnspan=3, sticky='w')

result_label18 = Label(window, text="", font=('Helvetica', 14))
result_label18.grid(row=18, column=0, columnspan=3, sticky='w')

result_label19 = Label(window, text="", font=('Helvetica', 14))
result_label19.grid(row=19, column=0, columnspan=3, sticky='w')

result_label20 = Label(window, text="", font=('Helvetica', 14))
result_label20.grid(row=20, column=0, columnspan=3, sticky='w')

result_label21 = Label(window, text="", font=('Helvetica', 14))
result_label21.grid(row=21, column=0, columnspan=3, sticky='w')

result_label22 = Label(window, text="", font=('Helvetica', 14))
result_label22.grid(row=22, column=0, columnspan=3, sticky='w')

result_label23 = Label(window, text="", font=('Helvetica', 14))
result_label23.grid(row=1, column=3, columnspan=3, sticky='w')


result_label24 = Label(window, text="", font=('Helvetica', 14))
result_label24.grid(row=2, column=3, columnspan=3, sticky='w')



result_label25 = Label(window, text="", font=('Helvetica', 14))
result_label25.grid(row=3, column=3, columnspan=3, sticky='w')



result_label26 = Label(window, text="", font=('Helvetica', 14))
result_label26.grid(row=4, column=3, columnspan=3, sticky='w')

result_label27 = Label(window, text="", font=('Helvetica', 14))
result_label27.grid(row=5, column=3, columnspan=3, sticky='w')


result_label28 = Label(window, text="", font=('Helvetica', 14))
result_label28.grid(row=6, column=3, columnspan=3, sticky='w')


result_label29 = Label(window, text="", font=('Helvetica', 14))
result_label29.grid(row=7, column=3, columnspan=3, sticky='w')


result_label30 = Label(window, text="", font=('Helvetica', 14))
result_label30.grid(row=8, column=3, columnspan=3, sticky='w')


result_label31 = Label(window, text="", font=('Helvetica', 14))
result_label31.grid(row=9, column=3, columnspan=3, sticky='w')

result_label32 = Label(window, text="", font=('Helvetica', 14))
result_label32.grid(row=10, column=3, columnspan=3, sticky='w')

result_label33 = Label(window, text="", font=('Helvetica', 14))
result_label33.grid(row=11, column=3, columnspan=3, sticky='w')

result_label34 = Label(window, text="", font=('Helvetica', 14))
result_label34.grid(row=12, column=3, columnspan=3, sticky='w')


result_label35 = Label(window, text="", font=('Helvetica', 14))
result_label35.grid(row=13, column=3, columnspan=3, sticky='w')



result_label36 = Label(window, text="", font=('Helvetica', 14))
result_label36.grid(row=14, column=3, columnspan=3, sticky='w')

result_label37 = Label(window,text="", font=('Helvetica', 14))
result_label37.grid(row=15, column=3, columnspan=3, sticky='w')

photo_label1 = Label(window, text="", font=('Helvetica', 14))
photo_label1.grid(row=15, column=3, columnspan=3, sticky='w')


result_label38 = Label(window,text="", font=('Helvetica', 14))
result_label38.grid(row=17, column=3, columnspan=3, sticky='w')

photo_label2 = Label(window, text="", font=('Helvetica', 14))
photo_label2.grid(row=17, column=3, columnspan=3, sticky='w')




time_label = Label(window, text="", font=('Helvetica', 14))
time_label.grid(row=19, column=3, columnspan=3, sticky='w')


window.mainloop()
