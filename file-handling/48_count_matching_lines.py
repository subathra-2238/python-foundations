# Count Lines Containing a Specific Word

file_path = "file-handling/sample.txt"
target_word = "Python"

count = 0

with open(file_path, "r") as file:
    for line in file:
        if target_word in line:
            count += 1

print("Lines containing", target_word + ":", count)