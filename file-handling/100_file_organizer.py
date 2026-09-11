from pathlib import Path
import shutil

source_folder = Path("file-handling/organizer_demo")

# Create demo folder
source_folder.mkdir(exist_ok=True)

# Create sample files
(source_folder / "notes.txt").write_text("Python notes")
(source_folder / "data.csv").write_text("Name,Age\nSubathra,18")
(source_folder / "config.json").write_text('{"language": "Python"}')
(source_folder / "program.py").write_text("print('Hello Python')")

# Create category folders
folders = {
    ".txt": "text_files",
    ".csv": "csv_files",
    ".json": "json_files",
    ".py": "python_files"
}

for folder_name in folders.values():
    (source_folder / folder_name).mkdir(exist_ok=True)

# Organize files
for file in source_folder.iterdir():

    if file.is_file():
        extension = file.suffix.lower()

        if extension in folders:
            destination_folder = source_folder / folders[extension]
            shutil.move(str(file), str(destination_folder / file.name))

print("Files organized successfully!")

# Display organized files
for folder in source_folder.iterdir():

    if folder.is_dir():
        print(f"\n{folder.name}:")

        for file in folder.iterdir():
            print("  -", file.name)