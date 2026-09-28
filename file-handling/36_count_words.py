# Count Words in a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    content = file.read()

words = content.split()

print("Number of words:", len(words))
