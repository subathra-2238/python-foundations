# Backup File into a Folder

import shutil
import os

source_file = "file-handling/sample.txt"
backup_folder = "file-handling/backups"
backup_file = os.path.join(backup_folder, "sample_backup.txt")

if os.path.exists(source_file):

    os.makedirs(backup_folder, exist_ok=True)

    shutil.copy(source_file, backup_file)

    print("Backup created successfully!")
    print("Saved to:", backup_file)

else:
    print("Source file does not exist.")