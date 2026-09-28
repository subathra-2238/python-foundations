import tempfile
from pathlib import Path

with tempfile.NamedTemporaryFile(
    mode="w",
    suffix=".txt",
    delete=False
) as temp_file:

    temp_file.write("This is temporary data.")
    temp_path = Path(temp_file.name)

print("Temporary file:", temp_path)
print("Exists:", temp_path.exists())

# Read the temporary file
print("Content:", temp_path.read_text())

# Clean it up
temp_path.unlink()

print("Exists after cleanup:", temp_path.exists())