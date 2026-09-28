# File Statistics

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("File Statistics")
print("----------------")
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)