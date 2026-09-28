# Count Characters in a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    content = file.read()

print("Number of characters:", len(content))