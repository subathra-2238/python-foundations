# Find Large Files

import os

folder_path = "file-handling"
minimum_size = 100  # bytes

print("Files larger than", minimum_size, "bytes:")

for root, directories, files in os.walk(folder_path):

    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)

        if size > minimum_size:
            print(file, "-", size, "bytes")