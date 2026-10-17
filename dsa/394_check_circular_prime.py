
def is_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


def is_circular_prime(n):
    digits = str(n)

    for i in range(len(digits)):
        rotation = int(digits[i:] + digits[:i])

        if not is_prime(rotation):
            return False

    return True


number = 197

print("Number:", number)

if is_circular_prime(number):
    print("It is a Circular Prime.")
else:
    print("It is not a Circular Prime.")
