from pathlib import Path

file_path = Path("file-handling/01_read_file.py")

if file_path.exists() and file_path.is_file():
    size = file_path.stat().st_size
    print("File:", file_path)
    print("Size:", size, "bytes")
else:
    print("File not found")