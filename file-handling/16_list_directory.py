# List Files and Folders

import os

folder_path = "file-handling"

items = os.listdir(folder_path)

print("Files and folders:")

for item in items:
    print(item)