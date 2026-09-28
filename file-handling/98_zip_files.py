from pathlib import Path
import zipfile

folder = Path("file-handling/zip_source")
zip_path = Path("file-handling/backup.zip")

# Create sample folder
folder.mkdir(exist_ok=True)

(folder / "file1.txt").write_text("Hello from file 1")
(folder / "file2.txt").write_text("Hello from file 2")

# Create ZIP file
with zipfile.ZipFile(zip_path, "w") as zip_file:
    for file in folder.iterdir():
        zip_file.write(file, arcname=file.name)

print("ZIP created:", zip_path)
print("Exists:", zip_path.exists())

# Show files inside ZIP
with zipfile.ZipFile(zip_path, "r") as zip_file:
    print("\nFiles inside ZIP:")

    for file in zip_file.namelist():
        print(file)