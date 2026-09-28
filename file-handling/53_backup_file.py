# Create a Backup of a File

import shutil
import os

source_file = "file-handling/sample.txt"
backup_file = "file-handling/sample_backup.txt"

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print("Backup created successfully!")
else:
    print("Source file does not exist.")