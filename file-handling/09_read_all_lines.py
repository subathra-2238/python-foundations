# Reading All Lines from a File

with open("file-handling/sample.txt", "r") as file:
    lines = file.readlines()

print("Lines in the file:")

for line in lines:
    print(line.strip())