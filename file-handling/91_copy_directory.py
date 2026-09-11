from pathlib import Path
import shutil

source = Path("file-handling/copy_source")
destination = Path("file-handling/copy_backup")

# Create a sample directory
source.mkdir(exist_ok=True)

# Create files inside it
(source / "file1.txt").write_text("Hello from file 1")
(source / "file2.txt").write_text("Hello from file 2")

# Copy the entire directory
shutil.copytree(source, destination)

print("Source:", source)
print("Backup:", destination)
print("Backup exists:", destination.exists())