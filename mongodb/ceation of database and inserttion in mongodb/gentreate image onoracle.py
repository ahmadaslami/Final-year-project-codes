import io
import cx_Oracle
from PIL import Image

# Establish a connection to the Oracle database
# Establish a connection
connection = cx_Oracle.connect(
    "system",
    "oracle",
    "localhost:1521/xe"  # Replace with your Oracle connection details
)

# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Generate and insert 10 fake images
for i in range(2):
    # Generate a fake image
    image = Image.new("RGB", (200, 200), "green")

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_data = image_bytes.getvalue()

    # Insert the image data into the database
    cursor.execute("INSERT INTO image (image) VALUES (:image_data)",
                   {"image_data": image_data})

# Commit the changes to the database
    connection.commit()
    image.show()
# Close the cursor and database connection
cursor.close()
connection.close()
