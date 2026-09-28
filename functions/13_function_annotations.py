# Function Annotations


def add_numbers(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


result = add_numbers(10, 20)

print("Sum:", result)
print(greet("Subathra"))