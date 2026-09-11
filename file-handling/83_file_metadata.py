from pathlib import Path
from datetime import datetime

file_path = Path("file-handling/01_read_file.py")

if file_path.exists() and file_path.is_file():
    modified_time = file_path.stat().st_mtime
    readable_time = datetime.fromtimestamp(modified_time)

    print("File:", file_path)
    print("Last modified:", readable_time)
else:
    print("File not found")