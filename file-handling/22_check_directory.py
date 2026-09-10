# Check if a Directory Exists

import os

folder_path = "file-handling/my_python_files"

if os.path.exists(folder_path):
    print("Directory exists!")
else:
    print("Directory does not exist.")