# Search for a Word and Display Its Lines

file_path = "file-handling/sample.txt"
target_word = "Python"

with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        if target_word in line:
            print("Found on line", line_number)
            print("Content:", line.strip())