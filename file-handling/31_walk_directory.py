# Walk Through a Directory

import os

folder_path = "file-handling"

for root, directories, files in os.walk(folder_path):
    print("\nCurrent directory:", root)

    print("Directories:")
    for directory in directories:
        print(" -", directory)

    print("Files:")
    for file in files:
        print(" -", file)