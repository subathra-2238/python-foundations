from pathlib import Path

folder = Path("file-handling/data/projects/python")

folder.mkdir(parents=True, exist_ok=True)

print("Created:", folder)
print("Exists:", folder.exists())
print("Is directory:", folder.is_dir())