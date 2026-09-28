# Error Handling with Functions


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = divide_numbers(num1, num2)

print("Result:", result)