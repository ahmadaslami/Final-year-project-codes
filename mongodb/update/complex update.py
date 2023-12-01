import tkinter as tk
from tkinter import Label, Entry, Button, ttk
#import pymongo
import time
from tkinter import Label, Entry, Button, filedialog
from PIL import Image, ImageTk
import pymongo
import io

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NSIA"]  # Replace with your actual database name
collection = db["citiz"]
# Replace with your actual collection name

collection_province = db["province"]
# Create a Tkinter window
window = tk.Tk()
window.title("MongoDB Data Retrieval by ID")

militry_service_entry = None
phone_number = None
Email_address = None
Native_language = None
foregin_language = None
Internal_language = None
Blood_Group = None

# Function to update the province name in MongoDB
def update_province_name():
    province_name_combobox = ttk.Combobox(window, text="province name", font=('Helvetica', 11))
    province_name_combobox.grid(row=2, column=3)
    user_input = entry.get()
    new_province_name = province_name_combobox.get()  # Get the selected province name from the Combobox

    try:
        # Find the province document using the selected name
        new_province_data = collection_province.find_one({"province_name": new_province_name})
        new_province_id = new_province_data["_id"]

        # Update the citizen's province with the new province ID
        collection.update_one({"citizen_id": user_input}, {"$set": {"Province_id": new_province_id}})
        province_name_combobox.set(new_province_name)
        result_label1.config(text="Province name updated successfully!")

    except Exception as e:
        result_label1.config(text=f"Error updating province name: {e}")

# Function to fetch data by ID
def fetch_data_by_id():
    user_input = entry.get()

    try:
        result = collection.find_one({"citizen_id": user_input})

        if result:
            first_name = result.get("first_name", "not found")
            last_name = result.get("last_name", "not found")
            fathername = result.get("fathername", "not found")
            father_last_name = result.get("father_last_name", "not found")
            grand_father_name = result.get("grand_father_name", "not found")
            grand_father_last_name = result.get("grand_father_last_name", "not found")
            mother_name = result.get("mother_name", "not found")
            ID_Card_NO = result.get("ID_Card_NO", "not found")
            militry_service = result.get("militry_service", "not found")
            phone_number = result.get("phone_number", "not found")
            Email_address = result.get("Email_address", "not found")
            Native_language = result.get("Native_language", "not found")
            foregin_language = result.get("foregin_language", "not found")
            Internal_language = result.get("Internal_language", "not found")
            Blood_Group = result.get("Blood_Group", "not found")
            Nationality = result.get("Nationality", "not found")
            Religion = result.get("Religion", "not found")
            Faith = result.get("Faith", "not found")
            Voting_place = result.get("Voting_place", "not found")

            # Create a Combobox for province names
            province_name_combobox = ttk.Combobox(window, text="province name", font=('Helvetica', 11))
            province_name_combobox.grid(row=2, column=3)

            # Function to populate province names in the Combobox
            def populate_province_names():
                province_names = [province["province_name"] for province in collection_province.find()]
                province_name_combobox['values'] = province_names

            # Call this function to populate the Combobox initially
            populate_province_names()

            province_id = result.get("Province_id", None)
            province_name = "not found"  # Default value

            if province_id:
                province_data = collection_province.find_one({"_id": province_id})
                province_name = province_data.get("province_name", "not Found")
                province_name_combobox.set(province_name)  # Set the value in the combobox

            pro_label = Label(window, text="Province Name", font=('Helvetica', 12))
            pro_label.grid(row=2, column=2)

            # Insert the retrieved first name into the Entry

            first_name_label = Label(window, text="First Name", font=('Helvetica', 12))
            first_name_label.grid(row=2, column=0)

            # Create a new Entry widget to display the retrieved first name
            global first_name_entry
            first_name_entry = Entry(window, font=('Helvetica', 12))
            first_name_entry.grid(row=2, column=1)
            first_name_entry.insert(0, first_name)

            # You can also clear and update the result label

            last_name_label = Label(window, text="Last Name", font=('Helvetica', 12))
            last_name_label.grid(row=3, column=0)

            # Create a new Entry widget to display the retrieved first name
            global last_name_entry
            last_name_entry = Entry(window, font=('Helvetica', 12))
            last_name_entry.grid(row=3, column=1)
            last_name_entry.insert(0, last_name)

            fathername_label = Label(window, text="Father Name", font=('Helvetica', 12))
            fathername_label.grid(row=4, column=0)

            # Create a new Entry widget to display the retrieved first name
            global fathername_entry
            fathername_entry = Entry(window, font=('Helvetica', 12))
            fathername_entry.grid(row=4, column=1)
            fathername_entry.insert(0, fathername)

            father_last_name_label = Label(window, text="father_last_name", font=('Helvetica', 12))
            father_last_name_label.grid(row=5, column=0)

            # Create a new Entry widget to display the retrieved first name
            global father_last_name_entry
            father_last_name_entry = Entry(window, font=('Helvetica', 12))
            father_last_name_entry.grid(row=5, column=1)
            father_last_name_entry.insert(0, father_last_name)

            grand_father_name_label = Label(window, text="grand_father_name", font=('Helvetica', 12))
            grand_father_name_label.grid(row=6, column=0)

            # Create a new Entry widget to display the retrieved first name
            global grand_father_name_entry
            grand_father_name_entry = Entry(window, font=('Helvetica', 12))
            grand_father_name_entry.grid(row=6, column=1)
            grand_father_name_entry.insert(0, grand_father_name)

            grand_father_last_name_label = Label(window, text="Grand Father LastName", font=('Helvetica', 12))
            grand_father_last_name_label.grid(row=7, column=0)

            # Create a new Entry widget to display the retrieved first name
            global grand_father_last_name_entry
            grand_father_last_name_entry = Entry(window, font=('Helvetica', 12))
            grand_father_last_name_entry.grid(row=7, column=1)
            grand_father_last_name_entry.insert(0, grand_father_last_name)

            mother_name_label = Label(window, text="Mother Name", font=('Helvetica', 12))
            mother_name_label.grid(row=8, column=0)

            # Create a new Entry widget to display the retrieved first name
            global mother_name_entry
            mother_name_entry = Entry(window, font=('Helvetica', 12))
            mother_name_entry.grid(row=8, column=1)
            mother_name_entry.insert(0, mother_name)

            ID_Card_NO_label = Label(window, text="ID Card NO", font=('Helvetica', 12))
            ID_Card_NO_label.grid(row=9, column=0)

            # Create a new Entry widget to display the retrieved first name
            global ID_Card_NO_entry
            ID_Card_NO_entry = Entry(window, font=('Helvetica', 12))
            ID_Card_NO_entry.grid(row=9, column=1)
            ID_Card_NO_entry.insert(0, ID_Card_NO)
            if militry_service is None:
                militry_service_label = Label(window, text="No information for this ID", font=('Helvetica', 12))
                militry_service_label.grid(row=10, column=0)
            else:
                militry_service_label = Label(window, text="Militry Service", font=('Helvetica', 12))
                militry_service_label.grid(row=10, column=0)
                # Create a new Entry widget to display the retrieved militry service
                global militry_service_entry
                militry_service_entry = Entry(window, font=('Helvetica', 12))
                militry_service_entry.grid(row=10, column=1)
                militry_service_entry.insert(0, militry_service)

            # Now, conditionally create these global Entry fields
            if phone_number is not None:
                phone_number_label = Label(window, text="Phone Number", font=('Helvetica', 12))
                phone_number_label.grid(row=13, column=0)
                global phone_number_entry
                phone_number_entry = Entry(window, font=('Helvetica', 12))
                phone_number_entry.grid(row=13, column=1)
                phone_number_entry.insert(0, phone_number)

            if Email_address is not None:
                Email_address_label = Label(window, text="Email Address", font=('Helvetica', 12))
                Email_address_label.grid(row=14, column=0)
                global Email_address_entry
                Email_address_entry = Entry(window, font=('Helvetica', 12))
                Email_address_entry.grid(row=14, column=1)
                Email_address_entry.insert(0, Email_address)

            if Native_language is not None:
                Native_language_label = Label(window, text="Native Language", font=('Helvetica', 12))
                Native_language_label.grid(row=15, column=0)
                global Native_language_entry
                Native_language_entry = Entry(window, font=('Helvetica', 12))
                Native_language_entry.grid(row=15, column=1)
                Native_language_entry.insert(0, Native_language)

            if foregin_language is not None:
                foregin_language_label = Label(window, text="Foreign Language", font=('Helvetica', 12))
                foregin_language_label.grid(row=16, column=0)
                global foregin_language_entry
                foregin_language_entry = Entry(window, font=('Helvetica', 12))
                foregin_language_entry.grid(row=16, column=1)
                foregin_language_entry.insert(0, foregin_language)

            if Internal_language is not None:
                Internal_language_label = Label(window, text="Internal Language", font=('Helvetica', 12))
                Internal_language_label.grid(row=17, column=0)
                global Internal_language_entry
                Internal_language_entry = Entry(window, font=('Helvetica', 12))
                Internal_language_entry.grid(row=17, column=1)
                Internal_language_entry.insert(0, Internal_language)

            if Blood_Group is not None:
                Blood_Group_label = Label(window, text="Blood Group", font=('Helvetica', 12))
                Blood_Group_label.grid(row=18, column=0)
                global Blood_Group_entry
                Blood_Group_entry = Entry(window, font=('Helvetica', 12))
                Blood_Group_entry.grid(row=18, column=1)
                Blood_Group_entry.insert(0, Blood_Group)

            Nationality_label = Label(window, text="Nationality", font=('Helvetica', 12))
            Nationality_label.grid(row=19, column=0)

            # Create a new Entry widget to display the retrieved first name
            global Nationality_entry
            Nationality_entry = Entry(window, font=('Helvetica', 12))
            Nationality_entry.grid(row=19, column=1)
            Nationality_entry.insert(0, Nationality)

            Religion_label = Label(window, text="Religion", font=('Helvetica', 12))
            Religion_label.grid(row=20, column=0)

            # Create a new Entry widget to display the retrieved first name

            global Religion_entry
            Religion_entry = Entry(window, font=('Helvetica', 12))
            Religion_entry.grid(row=20, column=1)
            Religion_entry.insert(0, Religion)
            # Create an "Update" button


            Faith_label = Label(window, text="Faith", font=('Helvetica', 12))
            Faith_label.grid(row=21, column=0)

            # Create a new Entry widget to display the retrieved first name

            global Faith_entry
            Faith_entry = Entry(window, font=('Helvetica', 12))
            Faith_entry.grid(row=21, column=1)
            Faith_entry.insert(0, Faith)
            # Create an "Update" button

            #Voting_place
            Voting_place_label = Label(window, text="Voting Place", font=('Helvetica', 12))
            Voting_place_label.grid(row=3, column=2)

            # Create a new Entry widget to display the retrieved first name

            global Voting_place_entry
            Voting_place_entry = Entry(window, font=('Helvetica', 12))
            Voting_place_entry.grid(row=3, column=3)
            Voting_place_entry.insert(0, Voting_place)
            # Create an "Update" button

            update_button = Button(window, text="Update Data", command=update_data_by_id, font=('Arial', 14))
            update_button.grid(row=25, column=1)
            display_photo(result.get("photo"))

            # Make the displayed photo clickable
            photo_label.bind("<Button-1>", update_photo)


        else:
            result_label1.config(text="Document not found.")

    except Exception as e:
        result_label1.config(text=f"Error: {e}")

# Function to update the photo


def update_photo(event):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])

    if file_path:
        try:
            with open(file_path, "rb") as image_file:
                image_data = image_file.read()

            update_photo_in_mongodb(entry.get(), image_data)
            display_photo(image_data)
        except Exception as e:
            result_label1.config(text=f"Error updating photo: {e}")

# Function to update the photo in MongoDB
def update_photo_in_mongodb(user_input, image_data):
    try:
        start_time = time.time()

        collection.update_one({"citizen_id": user_input}, {"$set": {"photo": image_data}})
        result_label1.config(text="Photo updated successfully!")

        end_time = time.time()
        total_time = end_time - start_time
        print(total_time)

        time_label.config(text=f" Query run time: {total_time:.4f} seconds")
        result_label1.config(text="Data updated successfully!")
    except Exception as e:
        result_label1.config(text=f"Error updating photo in MongoDB: {e}")

# Function to display the photo
def display_photo(image_data):
    image = Image.open(io.BytesIO(image_data))
    image.thumbnail((80, 80))  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    photo_label.config(image=photo)
    photo_label.photo = photo
    Internal_language_label = Label(window, text="Photo", font=('Helvetica', 12))
    Internal_language_label.grid(row=11, column=0)

# Function to update data by ID

# Placeholder for your variables, make sure to define them or fetch them properly
phone_number_entry = None
Email_address_entry = None
Native_language_entry = None
foregin_language_entry = None
Internal_language_entry = None
Blood_Group_entry = None
Nationality_entry = None
Religion_entry = None
Faith_entry = None
Voting_place_entry = None
def update_data_by_id(new_Faith=None):
    user_input = entry.get()
    new_first_name = first_name_entry.get()
    new_last_name = last_name_entry.get()
    new_fathername = fathername_entry.get()
    new_father_last_name = father_last_name_entry.get()
    new_grand_father_name = grand_father_name_entry.get()
    new_grand_father_last_name = grand_father_last_name_entry.get()
    new_mother_name = mother_name_entry.get()
    new_ID_Card_NO = ID_Card_NO_entry.get()

    # Handle missing fields
    if militry_service_entry is not None:
        new_militry_service = militry_service_entry.get()
    else:
        new_militry_service = None

    if phone_number_entry is not None:
        new_phone_number = phone_number_entry.get()
    else:
        new_phone_number = None

    if Email_address_entry is not None:
        new_Email_address = Email_address_entry.get()
    else:
        new_Email_address = None

    if Native_language_entry is not None:
        new_Native_language = Native_language_entry.get()
    else:
        new_Native_language = None

    if foregin_language_entry is not None:
        new_foregin_language = foregin_language_entry.get()
    else:
        new_foregin_language = None

    if Internal_language_entry is not None:
        new_Internal_language = Internal_language_entry.get()
    else:
        new_Internal_language = None

    if Blood_Group_entry is not None:
        new_Blood_Group = Blood_Group_entry.get()
    else:
        new_Blood_Group = None




    new_Nationality = Nationality_entry.get()
    new_Religion = Religion_entry.get()
    new_Faith = Faith_entry.get()
    new_Voting_place = Voting_place_entry.get()

    update_province_name()

    try:
        start_time = time.time()
        collection.update_one(
            {"citizen_id": user_input},
            {
                "$set": {
                    "first_name": new_first_name,
                    "last_name": new_last_name,
                    "fathername": new_fathername,
                    "father_last_name": new_father_last_name,
                    "grand_father_name": new_grand_father_name,
                    "grand_father_last_name": new_grand_father_last_name,
                    "mother_name": new_mother_name,
                    "ID_Card_NO": new_ID_Card_NO,
                    "militry_service": new_militry_service,
                    "phone_number": new_phone_number,
                    "Email_address": new_Email_address,
                    "Native_language": new_Native_language,
                    "foregin_language":new_foregin_language,
                    "Internal_language":new_Internal_language,
                    "Blood_Group":new_Blood_Group,
                    "Nationality":new_Nationality,
                    "Religion":new_Religion,
                    "Faith":new_Faith,
                    "Voting_place":new_Voting_place
                }
            }
        )
        end_time = time.time()
        total_time = end_time - start_time
        print(total_time)

        time_label.config(text=f" Query run time: {total_time:.4f} seconds")
        result_label1.config(text="Data updated successfully!")

    except Exception as e:
        result_label1.config(text=f"Error updating data: {e}")

# Define a grid layout for the window
label = Label(window, text="Enter Citizen ID:", font=('Helvetica', 14))
label.grid(row=0, column=0, sticky="w")

entry = Entry(window, font=('Helvetica', 14))
entry.grid(row=0, column=1)

button = Button(window, text="Search by ID", command=fetch_data_by_id, font=('Arial', 16),
                relief=tk.RAISED, fg="white", bg="skyblue")
button.grid(row=0, column=2, sticky='w')

result_label1 = Label(window, text="", font=('Helvetica', 14))
result_label1.grid(row=25, column=0, columnspan=3, sticky='w')

# Other labels, photos, and widgets can follow...
time_label = Label(window, text="", font=('Helvetica', 10))
time_label.grid(row=12, column=2, columnspan=3, padx=10, pady=10)

result_label14 = Label(window)
result_label14.grid(row=11, column=0, columnspan=3)

photo_label = Label(window, text="", font=('Helvetica', 14))
photo_label.grid(row=11, column=1, sticky="w")

window.mainloop()
