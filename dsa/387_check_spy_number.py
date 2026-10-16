
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


def digit_product(n):
    if n < 10:
        return n
    return (n % 10) * digit_product(n // 10)


def is_spy(n):
    if n <= 0:
        return False

    return digit_sum(n) == digit_product(n)


number = 1124

print("Number:", number)
print("Sum of digits:", digit_sum(number))
print("Product of digits:", digit_product(number))

if is_spy(number):
    print("It is a Spy number.")
else:
    print("It is not a Spy number.")
