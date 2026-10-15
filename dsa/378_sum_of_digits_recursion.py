
def sum_of_digits(n):
    n = abs(n)

    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)


number = 1234

print("Number:", number)
print("Sum of digits:", sum_of_digits(number))
