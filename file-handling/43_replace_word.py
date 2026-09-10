# Replace a Word in a File

file_path = "file-handling/sample.txt"

with open(file_path, "r") as file:
    content = file.read()

old_word = "Python"
new_word = "Programming"

updated_content = content.replace(old_word, new_word)

print("Updated content:")
print(updated_content)