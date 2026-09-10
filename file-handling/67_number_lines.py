# Number Each Line in a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, ":", line.strip())