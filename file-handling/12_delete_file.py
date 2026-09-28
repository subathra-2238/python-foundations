# Delete a File

import os

file_path = "file-handling/temp.txt"

# Create a temporary file
with open(file_path, "w") as file:
    file.write("This file will be deleted.")

print("Temporary file created.")

# Delete the file
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")