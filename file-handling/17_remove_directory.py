# Remove a Directory

import os

folder_path = "file-handling/my_files"

if os.path.exists(folder_path):
    try:
        os.rmdir(folder_path)
        print("Directory removed successfully.")
    except PermissionError:
        print("Error: Directory is currently in use.")
else:
    print("Directory does not exist.")