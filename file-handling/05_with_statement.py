# Using the with Statement

with open("file-handling/sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

print("\nFile closed automatically!")