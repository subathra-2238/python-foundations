
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digit_factorials(n):
    if n == 0:
        return 0

    digit = n % 10
    return factorial(digit) + sum_digit_factorials(n // 10)


def is_strong(n):
    if n < 0:
        return False

    return sum_digit_factorials(n) == n


number = 145

print("Number:", number)

if is_strong(number):
    print("It is a Strong number.")
else:
    print("It is not a Strong number.")
