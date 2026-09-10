# Get File Extension

import os

file_path = "file-handling/sample.txt"

file_name = os.path.basename(file_path)
file_name_without_extension, extension = os.path.splitext(file_name)

print("File name:", file_name)
print("Name without extension:", file_name_without_extension)
print("Extension:", extension)