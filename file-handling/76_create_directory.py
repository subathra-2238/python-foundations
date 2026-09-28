from pathlib import Path

folder = Path("file-handling/test_folder")

folder.mkdir(exist_ok=True)

print("Folder created:", folder)
print("Exists:", folder.exists())
print("Is directory:", folder.is_dir())