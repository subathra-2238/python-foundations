from pathlib import Path

file_path = Path("file-handling") / "sample.txt"

print("Full path:", file_path)
print("Parent:", file_path.parent)
print("Name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)