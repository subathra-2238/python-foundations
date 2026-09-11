from pathlib import Path

file_path = Path("data.txt")

print("Path:", file_path)
print("Exists:", file_path.exists())
print("Is file:", file_path.is_file())
print("Is directory:", file_path.is_dir())