# Get File Information

import os

file_path = "file-handling/sample.txt"

if os.path.exists(file_path):
    file_info = os.stat(file_path)

    print("File name:", os.path.basename(file_path))
    print("File size:", file_info.st_size, "bytes")
    print("File location:", os.path.abspath(file_path))
else:
    print("File does not exist.")