# Count Files by Extension

import os

folder_path = "file-handling"

extension_counts = {}

for root, directories, files in os.walk(folder_path):

    for file in files:

        extension = os.path.splitext(file)[1]

        if extension:
            if extension in extension_counts:
                extension_counts[extension] += 1
            else:
                extension_counts[extension] = 1

print("File Extension Counts")
print("---------------------")

for extension, count in extension_counts.items():
    print(extension, ":", count)