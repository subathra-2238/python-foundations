# Default and Keyword Arguments


def greet(name, message="Welcome to Python!"):
    print("Hello,", name)
    print(message)


# Using the default value
greet("Subathra")


# Providing our own value
greet("Sivasri", "Keep learning and building!")


# Keyword arguments
def student_info(name, department, year):
    print("\nStudent Information")
    print("Name:", name)
    print("Department:", department)
    print("Year:", year)


student_info(
    department="AI & ML",
    name="Subathra",
    year=2
)