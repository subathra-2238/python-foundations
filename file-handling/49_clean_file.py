# Remove Blank Lines and Save Clean File

source_file = "file-handling/sample.txt"
output_file = "file-handling/cleaned_sample.txt"

with open(source_file, "r") as file:
    lines = file.readlines()

cleaned_lines = []

for line in lines:
    if line.strip():
        cleaned_lines.append(line)

with open(output_file, "w") as file:
    file.writelines(cleaned_lines)

print("Cleaned file created successfully!")