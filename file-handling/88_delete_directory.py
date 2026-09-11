from pathlib import Path

folder = Path("file-handling/test_folder")

if folder.exists() and folder.is_dir():
    folder.rmdir()
    print("Folder deleted:", folder)
else:
    print("Folder not found")