# Create a Backup Folder

import os

backup_folder = "file-handling/backups"

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
    print("Backup folder created successfully!")
else:
    print("Backup folder already exists.")