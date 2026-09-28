# Search for a Word in a File

file_path = "file-handling/sample.txt"
target_word = "Python"

with open(file_path, "r") as file:
    content = file.read()

if target_word in content:
    print("Word found!")
else:
    print("Word not found.")