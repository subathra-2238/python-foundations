from pathlib import Path
from datetime import datetime

file_path = Path("file-handling/01_read_file.py")

if file_path.exists() and file_path.is_file():
    info = file_path.stat()

    print("File:", file_path)
    print("Size:", info.st_size, "bytes")
    print("Modified:", datetime.fromtimestamp(info.st_mtime))
    print("Created:", datetime.fromtimestamp(info.st_ctime))
else:
    print("File not found")