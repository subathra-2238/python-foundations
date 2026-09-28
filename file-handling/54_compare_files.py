# Compare Two Files

file1 = "file-handling/sample.txt"
file2 = "file-handling/copied_content.txt"

with open(file1, "r") as first:
    content1 = first.read()

with open(file2, "r") as second:
    content2 = second.read()

if content1 == content2:
    print("The files have the same content.")
else:
    print("The files are different.")
    