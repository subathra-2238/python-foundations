# Renaming a Directory

import os

old_name = "file-handling/my_files"
new_name = "file-handling/my_python_files"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("Directory renamed successfully!")
else:
    print("Directory does not exist.")