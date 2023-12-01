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


# Function to retrieve and display data


def fetch_data():
    citizen_id = id_entry.get()

    # Establish a database connection
    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    # Fetch all data based on the entered ID

    cursor.execute(
        "SELECT c.firstname,c.lastname,c.fathername,c.father_lastname,c.grand_father_name,c.grand_father_last_name,c.mother_name,"
        "c.photo,c.phone_number,c.email_address"
        " FROM citizen c"
        " WHERE citizen_id = :citizen_id",
        {'citizen_id': citizen_id})

    data = cursor.fetchone()

    if data:
        firstname, lastname, fathername, father_lastname, grand_father_name, grand_father_last_name, mother_name, photo,phone_number, email_address = data
        print(data)


        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        fathername_entry.delete(0, tk.END)
        father_lastname_entry.delete(0, tk.END)
        grand_father_name_entry.delete(0, tk.END)
        grand_father_last_name_entry.delete(0, tk.END)
        mother_name_entry.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
        email_address_entry.delete(0, tk.END)


        firstname_entry.insert(0, firstname)
        lastname_entry.insert(0, lastname)
        fathername_entry.insert(0, fathername)
        father_lastname_entry.insert(0, father_lastname)
        grand_father_name_entry.insert(0, grand_father_name)
        grand_father_last_name_entry.insert(0, grand_father_last_name)
        mother_name_entry.insert(0, mother_name)

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

    else:
        result_label.config(text="No data found for this ID")

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

    connection = cx_Oracle.connect("system", "oracle", "localhost:1521/xe")
    cursor = connection.cursor()

    global new_photo_bytes

    if new_photo_bytes:
        # Update all fields except the photo based on the entered ID
        cursor.execute(
            "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, fathername = :new_father_name,"
            " father_lastname = :new_father_lastname, grand_father_name = :new_grand_father_name, grand_father_last_name = :new_grand_father_last_name,"
            " mother_name = :new_mother_name, phone_number = :new_phone_number,"
            " email_address = :new_email_address, photo = :new_photo"  # Update photo here
            " WHERE citizen_id = :citizen_id",

            {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_father_name': new_father_name,
             'new_father_lastname': new_father_lastname, 'new_grand_father_name': new_grand_father_name,
             'new_grand_father_last_name': new_grand_father_last_name, 'new_mother_name': new_mother_name,
             'new_phone_number': new_phone_number,
             'new_email_address': new_email_address,
             'new_photo': new_photo_bytes,  # Bind the photo data last
             'citizen_id': citizen_id}
        )
    else:
        # Update all fields except the photo based on the entered ID
        cursor.execute(
            "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, fathername = :new_father_name,"
            " father_lastname = :new_father_lastname, grand_father_name = :new_grand_father_name, grand_father_last_name = :new_grand_father_last_name,"
            " mother_name = :new_mother_name, phone_number = :new_phone_number,"
            " email_address = :new_email_address"
            " WHERE citizen_id = :citizen_id",

            {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_father_name': new_father_name,
             'new_father_lastname': new_father_lastname, 'new_grand_father_name': new_grand_father_name,
             'new_grand_father_last_name': new_grand_father_last_name, 'new_mother_name': new_mother_name,
             'new_phone_number': new_phone_number,
             'new_email_address': new_email_address,
             'citizen_id': citizen_id})

    connection.commit()
    cursor.close()
    connection.close()

    result_label.config(text="Data updated successfully")
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)

    time_label.config(text=f"Query run time: {total_time:.2f} seconds")


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


photo_label.bind("<Button-1>", lambda event: select_photo())

result_label = tk.Label(root, text="")
result_label.grid(row=len(label_entries) + 7, column=0, columnspan=2)

time_label = tk.Label(root, text="")
time_label.grid(row=len(label_entries) + 8, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
