# Reading Specific Number of Characters

with open("file-handling/sample.txt", "r") as file:
    content = file.read(10)

print("First 10 characters:")
print(content)