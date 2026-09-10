# List Only Directories

import os

folder_path = "file-handling"

items = os.listdir(folder_path)

print("Directories:")

for item in items:
    item_path = os.path.join(folder_path, item)

    if os.path.isdir(item_path):
        print(item)