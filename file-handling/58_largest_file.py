# Find the Largest File

import os

folder_path = "file-handling"

largest_file = None
largest_size = 0

for root, directories, files in os.walk(folder_path):

    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)

        if size > largest_size:
            largest_size = size
            largest_file = file_path

if largest_file:
    print("Largest file:", largest_file)
    print("Size:", largest_size, "bytes")
else:
    print("No files found.")