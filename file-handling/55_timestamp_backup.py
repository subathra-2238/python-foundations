# Create a Timestamped Backup

import shutil
import os
from datetime import datetime

source_file = "file-handling/sample.txt"

if os.path.exists(source_file):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = f"file-handling/sample_backup_{timestamp}.txt"

    shutil.copy(source_file, backup_file)

    print("Backup created successfully!")
    print("Backup file:", backup_file)

else:
    print("Source file does not exist.")