# Find Files by Extension

import os

folder_path = "file-handling"
extension = ".txt"

print("Text files found:")

for root, directories, files in os.walk(folder_path):
    for file in files:
        if file.endswith(extension):
            file_path = os.path.join(root, file)
            print(file_path)