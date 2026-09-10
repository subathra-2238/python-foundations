# Copy Multiple Files

import os
import shutil

source_folder = "file-handling"
destination_folder = "file-handling/my_python_files"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):

    if file.endswith(".txt"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.copy(source_path, destination_path)

        print("Copied:", file)

print("All text files copied successfully!")