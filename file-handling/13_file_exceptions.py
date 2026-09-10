# Handling File Errors

file_path = "file-handling/missing.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File not found.")