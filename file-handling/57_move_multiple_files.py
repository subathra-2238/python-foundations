# Move Multiple Files

import os
import shutil

source_folder = "file-handling"
destination_folder = "file-handling/my_python_files"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):

    if file.endswith(".txt"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print("Moved:", file)

print("All text files moved successfully!")