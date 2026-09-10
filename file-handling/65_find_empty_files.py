# Find Empty Files

import os

folder_path = "file-handling"

print("Empty files:")

found = False

for root, directories, files in os.walk(folder_path):

    for file in files:
        file_path = os.path.join(root, file)

        if os.path.getsize(file_path) == 0:
            print("-", file_path)
            found = True

if not found:
    print("No empty files found.")