# Function Docstrings


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def greet(name):
    """Print a greeting message for the given name."""
    print("Hello,", name)


print("Sum:", add_numbers(10, 20))

greet("Subathra")

print("\nFunction Documentation:")
print(add_numbers.__doc__)
print(greet.__doc__)