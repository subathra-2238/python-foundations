# Read User Notes from a File

file_path = "file-handling/user_notes.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()

    print("Saved Information")
    print("-----------------")
    print(content)

except FileNotFoundError:
    print("No saved information found.")