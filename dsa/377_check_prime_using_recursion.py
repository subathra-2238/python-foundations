
def is_prime(n, divisor=2):
    if n < 2:
        return False

    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)


number = 17

print("Number:", number)

if is_prime(number):
    print("It is a prime number.")
else:
    print("It is not a prime number.")
