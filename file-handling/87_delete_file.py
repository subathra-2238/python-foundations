from pathlib import Path

file_path = Path("file-handling/data/new_name.txt")

if file_path.exists() and file_path.is_file():
    file_path.unlink()
    print("File deleted:", file_path)
else:
    print("File not found")