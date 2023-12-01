import cx_Oracle
import tkinter as tk
from tkinter import Label, Entry, Button
from cx_Oracle import connect, DatabaseError
from tkinter import messagebox
import time

# Create a connection pool
pool = cx_Oracle.SessionPool("system", "oracle", "localhost:1521/xe", min=1, max=5, increment=1, threaded=True)

def fetch_province_data():
    try:
        user_input_id = int(id_entry.get())


        with pool.acquire() as connection:
            start_time = time.time()
            sql_query = """
                SELECT province_id, name FROM province
                WHERE province_id = :user_input_id
            """
            with connection.cursor() as cursor:
                cursor.execute(sql_query, user_input_id=user_input_id)
                results = cursor.fetchall()
            end_time = time.time()
            total_time = end_time - start_time

            time_label.config(text=f" Query run time: {total_time:.5f} seconds")


        if results:
            province_id, province_name = results[0]
            citizen_id_label.config(text=f"Province ID: {province_id}")
            citizen_firstname_label.config(text=f"Peovince Name: {province_name}")

        else:
            result_label.config(text="Citizen not found.")

    except (ValueError, DatabaseError) as error:
        result_label.config(text=f"Error: {error}")



# Create a tkinter window
window = tk.Tk()
window.title("Citizen Information")
window.geometry("600x400")

# Create and pack tkinter widgets using the grid manager
id_label = Label(window, text="Province ID:", font=('Helvetica', 10))
id_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

id_entry = Entry(window, font=('Helvetica', 10))
id_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = Button(window, text="Search Button", command=fetch_province_data, font=("Helvetica", 10), bg="green",
                      fg="white", relief=tk.RAISED, padx=5, pady=5)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

# Labels for citizen data
citizen_id_label = Label(window, text="Province ID:", font=('Helvetica', 10))
citizen_id_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

citizen_firstname_label = Label(window, text="Province Name:", font=('Helvetica', 10))
citizen_firstname_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

result_label = Label(window, text="", font=('Helvetica', 10))
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

time_label = Label(window, text="", font=('Helvetica', 10))
time_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
