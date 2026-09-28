import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as temp_dir:

    folder = Path(temp_dir)

    print("Temporary directory:", folder)
    print("Exists:", folder.exists())

    # Create files inside it
    (folder / "file1.txt").write_text("Temporary data")
    (folder / "file2.txt").write_text("More temporary data")

    print("Files created:")
    for file in folder.iterdir():
        print(file.name)

print("Exists after cleanup:", folder.exists())