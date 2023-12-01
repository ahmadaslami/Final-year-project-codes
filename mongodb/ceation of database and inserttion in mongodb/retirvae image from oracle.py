import io
import cx_Oracle
import tkinter as tk
from PIL import Image, ImageTk
# Establish a connection
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)

# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Create the main application window
root = tk.Tk()

# Function to display the selected image
def display_image(image_data):
    # Create an in-memory stream for the image data
    image_stream = io.BytesIO(image_data)

    # Open the image using Pillow (PIL)
    image = Image.open(image_stream)

    # Create a Tkinter-compatible image object
    tk_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # Keep a reference to prevent garbage collection
    label.pack()

# Execute a SQL query to retrieve the image data
cursor.execute("SELECT image FROM image")

# Fetch all rows
rows = cursor.fetchall()

# Iterate over the rows and display each image
for row in rows:
    # Get the image data from the result row
    image_data = row[0].read()

    # Display the image
    display_image(image_data)

# Close the cursor and database connection
cursor.close()
connection.close()

# Start the Tkinter event loop
root.mainloop()
