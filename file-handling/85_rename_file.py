from pathlib import Path

old_file = Path("file-handling/test_folder/old_name.txt")
new_file = Path("file-handling/test_folder/new_name.txt")

# Create the old file for practice
old_file.write_text("This file will be renamed.")

# Rename it
old_file.rename(new_file)

print("Old file:", old_file)
print("New file:", new_file)
print("New file exists:", new_file.exists())