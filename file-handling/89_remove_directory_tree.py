from pathlib import Path
import shutil

folder = Path("file-handling/delete_test")

# Create a folder
folder.mkdir(exist_ok=True)

# Create files inside it
(folder / "file1.txt").write_text("Temporary file 1")
(folder / "file2.txt").write_text("Temporary file 2")

print("Folder exists before deletion:", folder.exists())

# Delete the folder and everything inside it
shutil.rmtree(folder)

print("Folder exists after deletion:", folder.exists())