
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def armstrong_sum(n, power):
    if n == 0:
        return 0

    digit = n % 10
    return digit ** power + armstrong_sum(n // 10, power)


def is_armstrong(n):
    if n < 0:
        return False

    power = count_digits(n)
    return armstrong_sum(n, power) == n


number = 153

print("Number:", number)

if is_armstrong(number):
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
