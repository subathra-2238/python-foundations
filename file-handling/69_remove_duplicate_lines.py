# Remove Duplicate Lines

source_file = "file-handling/sample.txt"
output_file = "file-handling/unique_lines.txt"

with open(source_file, "r") as file:
    lines = file.readlines()

unique_lines = []
seen = set()

for line in lines:
    cleaned_line = line.strip()

    if cleaned_line and cleaned_line not in seen:
        unique_lines.append(cleaned_line + "\n")
        seen.add(cleaned_line)

with open(output_file, "w") as file:
    file.writelines(unique_lines)

print("Duplicate lines removed successfully!")
print("Unique file created:", output_file)