# Reading a File Line by Line

file = open("file-handling/sample.txt", "r")

for line in file:
    print(line.strip())

file.close()