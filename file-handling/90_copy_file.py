from pathlib import Path
import shutil

source = Path("file-handling/01_read_file.py")
destination = Path("file-handling/01_read_file_backup.py")

shutil.copy2(source, destination)

print("Original:", source)
print("Backup:", destination)
print("Backup exists:", destination.exists())