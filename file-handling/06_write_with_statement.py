# Writing Using the with Statement

with open("file-handling/student.txt", "w") as file:
    file.write("Name: Subathra\n")
    file.write("Department: AI & ML\n")
    file.write("Year: 2")

print("Student information saved successfully!")