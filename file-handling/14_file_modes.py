# File Modes

# Write mode
with open("file-handling/modes.txt", "w") as file:
    file.write("Python File Handling\n")

# Append mode
with open("file-handling/modes.txt", "a") as file:
    file.write("Learning file modes.\n")

# Read mode
with open("file-handling/modes.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)