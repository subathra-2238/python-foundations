# Append Multiple Lines

file_path = "file-handling/sample.txt"

new_lines = [
    "I am currently in my second year.\n",
    "I am building my Python foundations.\n",
    "My goal is to become a developer.\n"
]

with open(file_path, "a") as file:
    file.writelines(new_lines)

print("New lines added successfully!")