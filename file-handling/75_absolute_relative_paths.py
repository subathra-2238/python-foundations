from pathlib import Path

relative_path = Path("file-handling/sample.txt")

print("Relative path:", relative_path)
print("Absolute path:", relative_path.absolute())
print("Resolved path:", relative_path.resolve())