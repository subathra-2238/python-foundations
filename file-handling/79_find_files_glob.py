from pathlib import Path

folder = Path("file-handling")

python_files = folder.glob("*.py")

for file in python_files:
    print(file)