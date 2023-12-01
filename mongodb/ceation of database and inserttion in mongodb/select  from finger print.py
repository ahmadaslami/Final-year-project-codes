import pymongo
from PIL import ImageTk, Image
import io
import tkinter as tk

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["NSIA"]
collection = db["finger_print_citizen"]

# Create the Tkinter window
window = tk.Tk()

# Retrieve a random image from MongoDB
random_image_data = collection.aggregate([{ "$sample": { "size": 1 } }])
random_image_data = list(random_image_data)[0]

# Extract the image data
image_bytes = random_image_data["image"]

# Open the image from bytes
image = Image.open(io.BytesIO(image_bytes))

# Resize the image to fit the window
image = image.resize((400, 400))

# Convert the image to Tkinter PhotoImage format
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(window, image=photo)
label.pack()

# Run the Tkinter event loop
window.mainloop()

# Close the MongoDB connection
client.close()