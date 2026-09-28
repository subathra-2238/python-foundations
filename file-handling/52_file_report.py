# Create a File Report

import os

file_path = "file-handling/sample.txt"

if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)

    with open(file_path, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("File Report")
    print("-----------")
    print("File:", os.path.basename(file_path))
    print("Size:", file_size, "bytes")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)
else:
    print("File does not exist.")