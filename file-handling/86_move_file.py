from pathlib import Path

source = Path("file-handling/test_folder/new_name.txt")
destination = Path("file-handling/data/new_name.txt")

source.rename(destination)

print("Moved to:", destination)
print("Exists:", destination.exists())