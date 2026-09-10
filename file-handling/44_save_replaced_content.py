# Save Replaced Content to a New File

source_file = "file-handling/sample.txt"
output_file = "file-handling/updated_sample.txt"

old_word = "Python"
new_word = "Programming"

with open(source_file, "r") as file:
    content = file.read()

updated_content = content.replace(old_word, new_word)

with open(output_file, "w") as file:
    file.write(updated_content)

print("Updated file created successfully!")