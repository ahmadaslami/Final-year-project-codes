import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import Tk,Label
import pymongo
import time

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NSIA"]  # Replace with your actual database name
collection = db["province1"]  # Replace with your actual collection name

def fetch_data_by_id():


    user_input =entry.get()

    try:
        user_input = int(user_input)
        start_time = time.time()
        result = collection.find_one({"province_id": user_input})

        if result:

            first_name = result.get("name", "not found")
            result_label1.config(text=f"First Name: {first_name}")


            # grand_father_name

            end_time = time.time()
            total_time = end_time-start_time
            print(total_time)

            time_label.config(text=f" Query run time: {total_time:.4f} seconds")

        else:
            result_label1.config(text="Document not found.")

    except Exception as e:
        result_label1.config(text=f"Error: {e}")


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





time_label = Label(window, text="", font=('Helvetica', 14))
time_label.grid(row=19, column=3, columnspan=3, sticky='w')


window.mainloop()
