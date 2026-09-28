# Save User Input to a File

file_path = "file-handling/user_notes.txt"

name = input("Enter your name: ")
goal = input("Enter your current goal: ")

with open(file_path, "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Goal: " + goal + "\n")

print("Your information was saved successfully!")