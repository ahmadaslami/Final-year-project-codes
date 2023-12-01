import tkinter as tk
from tkinter import Label, Entry, Button, ttk
import pymongo
import time
from tkinter import Label, Entry, Button, filedialog
from PIL import Image, ImageTk
import pymongo
import io

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NSIA"]  # Replace with your actual database name
collection = db["citiz"]
# Create a Tkinter window
window = tk.Tk()
window.title("MongoDB Data Retrieval by ID")


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

            update_button = Button(window, text="Update Data", command=update_data_by_id, font=('Arial', 14))
            update_button.grid(row=25, column=1)
        else:
            result_label1.config(text="Document not found.")
 
    except Exception as e:
        result_label1.config(text=f"Error: {e}")


# Function to update data by ID
def update_data_by_id(new_Faith=None):
    user_input = entry.get()
    new_first_name = first_name_entry.get()
    new_last_name = last_name_entry.get()
    new_fathername = fathername_entry.get()
    new_father_last_name = father_last_name_entry.get()
    new_grand_father_name = grand_father_name_entry.get()
    new_grand_father_last_name = grand_father_last_name_entry.get()
    new_mother_name = mother_name_entry.get()

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
                    "mother_name": new_mother_name
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
