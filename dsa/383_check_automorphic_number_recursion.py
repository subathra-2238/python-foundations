
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def is_automorphic(n):
    if n < 0:
        return False

    digits = count_digits(n)
    divisor = 10 ** digits

    return n * n % divisor == n


number = 25

print("Number:", number)
print("Square:", number * number)

if is_automorphic(number):
    print("It is an Automorphic number.")
else:
    print("It is not an Automorphic number.")
