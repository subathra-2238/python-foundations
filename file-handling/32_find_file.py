# Find a File

import os

folder_path = "file-handling"
target_file = "sample.txt"

for root, directories, files in os.walk(folder_path):
    if target_file in files:
        file_path = os.path.join(root, target_file)
        print("File found!")
        print("Location:", file_path)