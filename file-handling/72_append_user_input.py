# Append User Input to a File

file_path = "file-handling/user_notes.txt"

note = input("Enter a new note: ")

with open(file_path, "a") as file:
    file.write("Note: " + note + "\n")

print("New note added successfully!")