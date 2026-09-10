# Remove Empty Lines from a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

print("File without empty lines:")

for line in lines:
    if line.strip():
        print(line.strip())