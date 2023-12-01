import cx_Oracle
import tkinter as tk
import time
import cx_Oracle
from cx_Oracle import SessionPool
import tkinter as tk
import time

# Set up a connection pool
pool = SessionPool(user="system", password="oracle", dsn="localhost:1521/xe", min=1, max=5, increment=1)

# Function to acquire a connection from the pool
def get_connection():
    return pool.acquire()

# ... (rest of the code)


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

# Function to retrieve and display data
def fetch_data():
    citizen_id = id_entry.get()

    # Establish a database connection
    with cx_Oracle.connect("system", "oracle", "localhost:1521/xe") as connection:
        with connection.cursor() as cursor:
            # Fetch specific columns based on the entered ID
            cursor.execute(
                "SELECT c.firstname, c.lastname, c.fathername, c.father_lastname"
                " FROM citizen c"
                " WHERE citizen_id = :citizen_id",
                {'citizen_id': citizen_id}
            )

            data = cursor.fetchone()

            if data:
                firstname, lastname, fathername, father_lastname = data
                print(data)

                firstname_entry.delete(0, tk.END)
                lastname_entry.delete(0, tk.END)
                fathername_entry.delete(0, tk.END)
                father_lastname_entry.delete(0, tk.END)

                firstname_entry.insert(0, firstname)
                lastname_entry.insert(0, lastname)
                fathername_entry.insert(0, fathername)
                father_lastname_entry.insert(0, father_lastname)
            else:
                result_label.config(text="No data found for this ID")







def update_data():
    start_time = time.time()
    citizen_id = id_entry.get()
    new_first_name = firstname_entry.get()
    new_last_name = lastname_entry.get()
    new_father_name = fathername_entry.get()
    new_father_lastname = father_lastname_entry.get()

    try:
        with get_connection() as connection:
            cursor = connection.cursor()

            global new_photo_bytes

            if new_photo_bytes:
                # Update all fields except the photo based on the entered ID
                cursor.execute(
                    "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, "
                    "fathername = :new_father_name, father_lastname = :new_father_lastname "
                    "WHERE citizen_id = :citizen_id",
                    {'new_first_name': new_first_name, 'new_last_name': new_last_name,
                     'new_father_name': new_father_name, 'new_father_lastname': new_father_lastname,
                     'citizen_id': citizen_id}
                )


            else:
                # Update all fields except the photo based on the entered ID
                cursor.execute(
                    "UPDATE citizen SET firstname = :new_first_name, lastname = :new_last_name, "
                    "fathername = :new_father_name, father_lastname = :new_father_lastname "
                    "WHERE citizen_id = :citizen_id",
                    {'new_first_name': new_first_name, 'new_last_name': new_last_name,
                     'new_father_name': new_father_name, 'new_father_lastname': new_father_lastname,
                     'citizen_id': citizen_id}
                )


        result_label.config(text="Data updated successfully")
        end_time = time.time()
        total_time = end_time - start_time
        print(total_time)

        time_label.config(text=f"Query run time: {total_time:.3f} seconds")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# ... (rest of the code)


label_entries = [
    ("Citizen ID:", id_entry),
    ("First Name:", firstname_entry),
    ("Last Name:", lastname_entry),
    ("Father Name:", fathername_entry),
    ("Father Last Name:", father_lastname_entry),
]

for i, (label_text, entry_widget) in enumerate(label_entries):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry_widget.grid(row=i, column=1, padx=10, pady=5, sticky='e')


fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=11, column=0, pady=10)

update_button = tk.Button(root, text="Update", command=update_data)
update_button.grid(row=11, column=1, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=len(label_entries) + 7, column=0, columnspan=2)

time_label = tk.Label(root, text="")
time_label.grid(row=len(label_entries) + 8, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()

# Start the Tkinter main loop
root.mainloop()
