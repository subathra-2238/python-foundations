
def is_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


def is_twisted_prime(n):
    if not is_prime(n):
        return False

    reversed_number = int(str(n)[::-1])

    return is_prime(reversed_number)


number = 13
reversed_number = int(str(number)[::-1])

print("Number:", number)
print("Reversed number:", reversed_number)

if is_twisted_prime(number):
    print("It is a Twisted Prime number.")
else:
    print("It is not a Twisted Prime number.")
