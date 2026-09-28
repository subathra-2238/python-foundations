# Delete Text Files

import os

folder_path = "file-handling"

for file in os.listdir(folder_path):

    if file.endswith(".txt"):

        file_path = os.path.join(folder_path, file)

        print("Deleting:", file)

        os.remove(file_path)

print("Text file cleanup completed!")
