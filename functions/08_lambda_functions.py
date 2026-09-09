# Lambda Functions

# Normal function
def square(number):
    return number * number


print("Normal function:", square(5))


# Lambda function
square_lambda = lambda number: number * number

print("Lambda function:", square_lambda(5))


# Lambda with two arguments
add = lambda a, b: a + b

print("Addition:", add(10, 20))