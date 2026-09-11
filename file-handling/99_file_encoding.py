from pathlib import Path

file_path = Path("file-handling/99_file_encoding.txt")

content = "Hello, Subathra! 🚀\nPython supports Unicode text."

file_path.write_text(content, encoding="utf-8")

print("File written using UTF-8.")

text = file_path.read_text(encoding="utf-8")

print("Content:")
print(text)