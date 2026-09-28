import csv
from pathlib import Path

file_path = Path("file-handling/students.csv")

students = [
    ["Name", "Age", "Department"],
    ["Subathra", 18, "AI & ML"],
    ["Sivasri", 18, "CSE"],
    ["Thilaga", 18, "AI & ML"]
]

# Write CSV
with file_path.open("w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created.")

# Read CSV
with file_path.open("r", newline="") as file:
    reader = csv.reader(file)

    print("\nStudent records:")

    for row in reader:
        print(row)