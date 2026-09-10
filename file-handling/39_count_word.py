# Count a Specific Word in a File

file_path = "file-handling/sample.txt"
target_word = "Python"

with open(file_path, "r") as file:
    content = file.read()

words = content.split()

count = 0

for word in words:
    if word.strip(".,!?") == target_word:
        count += 1

print("Word:", target_word)
print("Count:", count)