from pathlib import Path
import shutil

source = Path("file-handling/move_source")
destination = Path("file-handling/move_destination")

# Create source directory
source.mkdir(exist_ok=True)

# Create a file inside it
(source / "sample.txt").write_text("This directory will be moved.")

# Move the entire directory
shutil.move(source, destination)

print("Moved from:", source)
print("Moved to:", destination)
print("Destination exists:", destination.exists())