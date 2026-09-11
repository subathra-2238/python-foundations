import json
from pathlib import Path

file_path = Path("file-handling/student.json")

student = {
    "name": "Subathra",
    "age": 18,
    "department": "AI & ML",
    "skills": ["Python", "IoT", "Cybersecurity"]
}

# Write Python data to JSON
with file_path.open("w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")

# Read JSON back into Python
with file_path.open("r") as file:
    data = json.load(file)

print("\nStudent data:")
print(data)

print("\nName:", data["name"])
print("Department:", data["department"])