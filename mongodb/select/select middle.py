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



            province_id = result.get("Province_id", None)
            if province_id:
                province_data = db["province"].find_one({"_id": province_id})
                province_name = province_data.get("province_name", "not Found")
                result_label15.config(text = f"Province Name :{province_name}")

            district_id = result.get("District_id",None)
            if district_id:
                district_data = db["district"].find_one({"_id":district_id})
                district_name = district_data.get("district_name","not Found")
                result_label16.config(text = f"District Name :{district_name}")


            #Village_id

            village_id = result.get("Village_id",None)
            if village_id:
                village_data = db["village"].find_one({"_id":village_id})
                village_name = village_data.get("village_name","not Found")
                result_label17.config(text = f"Village Name :{village_name}")
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

photo_label2 = Label(window, text="", font=('Helvetica', 14))
photo_label2.grid(row=18, column=3, columnspan=3, sticky='w')




time_label = Label(window, text="", font=('Helvetica', 14))
time_label.grid(row=19, column=0, columnspan=3, sticky='w')


window.mainloop()
