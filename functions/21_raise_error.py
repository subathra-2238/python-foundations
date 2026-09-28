# Raising Errors


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


age = int(input("Enter your age: "))

try:
    result = check_age(age)
    print("Valid age:", result)
except ValueError as error:
    print("Error:", error)