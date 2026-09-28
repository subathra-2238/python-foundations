# Moving a File

import shutil

source = "file-handling/sample_copy.txt"
destination = "file-handling/my_files/sample_copy.txt"

shutil.move(source, destination)

print("File moved successfully!")