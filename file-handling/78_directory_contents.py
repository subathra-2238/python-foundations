from pathlib import Path

folder = Path("file-handling")

print("Contents:")

for item in folder.iterdir():
    print(item)