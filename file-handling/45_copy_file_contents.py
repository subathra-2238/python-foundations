# Copy File Contents

source_file = "file-handling/sample.txt"
destination_file = "file-handling/copied_content.txt"

with open(source_file, "r") as source:
    content = source.read()

with open(destination_file, "w") as destination:
    destination.write(content)

print("File contents copied successfully!")