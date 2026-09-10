# Check if a File Exists

import os

file_path = "file-handling/sample.txt"

if os.path.exists(file_path):
    print("File exists!")
else:
    print("File does not exist.")