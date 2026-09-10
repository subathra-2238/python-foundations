# Count Files by Extension

import os

folder_path = "file-handling"
extension = ".txt"

count = 0

for root, directories, files in os.walk(folder_path):
    for file in files:
        if file.endswith(extension):
            count += 1

print("Number of text files:", count)