# Reading a File

file = open("file-handling/sample.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()