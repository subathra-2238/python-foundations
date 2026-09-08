# Python Dictionaries

student = {
    "name": "Subathra",
    "age": 18,
    "department": "AI & ML",
    "cgpa": 9.1
}

print("Student:", student)

# Accessing values
print("\nName:", student["name"])
print("Department:", student["department"])

# Adding a new key-value pair
student["year"] = 2
print("\nAfter adding year:", student)

# Updating a value
student["cgpa"] = 9.2
print("After updating CGPA:", student)

# Removing a key-value pair
student.pop("age")
print("After removing age:", student)

# Loop through dictionary
print("\nStudent Details:")

for key, value in student.items():
    print(key, ":", value)