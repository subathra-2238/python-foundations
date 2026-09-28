from pathlib import Path

folder = Path("file-handling")

for item in folder.iterdir():
    if item.is_file():
        print("FILE:", item)
    elif item.is_dir():
        print("FOLDER:", item)