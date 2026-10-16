
def sum_divisors(n, divisor=1):
    if divisor >= n:
        return 0

    if n % divisor == 0:
        return divisor + sum_divisors(n, divisor + 1)

    return sum_divisors(n, divisor + 1)


def is_perfect(n):
    if n <= 1:
        return False

    return sum_divisors(n) == n


number = 6

print("Number:", number)

if is_perfect(number):
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
