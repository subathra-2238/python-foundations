# Reading One Line from a File

with open("file-handling/sample.txt", "r") as file:
    first_line = file.readline()

print("First line:")
print(first_line.strip())