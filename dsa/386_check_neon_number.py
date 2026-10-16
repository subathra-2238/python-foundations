
def sum_of_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)


def is_neon(n):
    if n < 0:
        return False

    square = n * n
    return sum_of_digits(square) == n


number = 9
square = number * number

print("Number:", number)
print("Square:", square)
print("Sum of square's digits:", sum_of_digits(square))

if is_neon(number):
    print("It is a Neon number.")
else:
    print("It is not a Neon number.")
