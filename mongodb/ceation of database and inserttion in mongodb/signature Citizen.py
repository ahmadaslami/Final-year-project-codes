import pymongo
from PIL import Image
import io
import random
import os

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["signature_citizen"]
collection = db["signature_citizen
# Path to the folder containing the images
folder_path = "E:\Every thing\Mobile Applications\image2"

# Number of MongoDB documents to generate
N = 10

# Get a list of image files from the folder
image_files = os.listdir(folder_path)

# Randomly select 10 images from the list
selected_images = random.sample(image_files, 7)

# Generate and store N documents with random images
for _ in range(N):
    # Randomly select an image from the selected images list
    image_file = random.choice(selected_images)

    # Open the image file
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_data = image_bytes.getvalue()

    # Insert the image data into MongoDB
    collection.insert_one({"image": image_data})

# Close the MongoDB connection
client.close()
