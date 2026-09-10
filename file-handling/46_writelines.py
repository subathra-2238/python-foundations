# Writing Multiple Lines Using writelines()

file_path = "file-handling/subjects.txt"

subjects = [
    "Python\n",
    "Data Structures\n",
    "Machine Learning\n",
    "Cybersecurity\n"
]

with open(file_path, "w") as file:
    file.writelines(subjects)

print("Subjects written successfully!")