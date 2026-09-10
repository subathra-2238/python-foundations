# Copying a File

import shutil

source = "file-handling/sample.txt"
destination = "file-handling/sample_copy.txt"

shutil.copy(source, destination)

print("File copied successfully!")