# Count Matching Lines with Line Numbers

file_path = "file-handling/sample.txt"
target_word = "Python"

count = 0

with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):

        if target_word in line:
            count += 1
            print("Found on line", line_number, ":", line.strip())

print("\nTotal matching lines:", count)