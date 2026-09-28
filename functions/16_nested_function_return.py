# Nested Function with Return Value


def calculate_square(number):

    def square():
        return number * number

    return square()


result = calculate_square(6)

print("Square:", result)