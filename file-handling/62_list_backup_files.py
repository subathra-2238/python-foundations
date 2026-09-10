# List Backup Files

import os

backup_folder = "file-handling/backups"

if os.path.exists(backup_folder):

    files = os.listdir(backup_folder)

    print("Backup files:")

    for file in files:
        print("-", file)

else:
    print("Backup folder does not exist.")