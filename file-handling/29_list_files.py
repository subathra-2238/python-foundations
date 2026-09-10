# List Only Files in a Directory

import os

folder_path = "file-handling"

items = os.listdir(folder_path)

print("Files:")

for item in items:
    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
        print(item)