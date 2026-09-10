# Count Lines in a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))