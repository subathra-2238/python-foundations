# Renaming a File

import os

old_name = "file-handling/output.txt"
new_name = "file-handling/renamed_output.txt"

os.rename(old_name, new_name)

print("File renamed successfully!")