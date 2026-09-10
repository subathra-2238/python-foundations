# Creating a Directory

import os

folder_path = "file-handling/my_files"

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Directory created successfully!")
else:
    print("Directory already exists.")