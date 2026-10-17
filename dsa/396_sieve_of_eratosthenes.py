
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)

    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    return [
        number
        for number in range(2, limit + 1)
        if is_prime[number]
    ]


limit = 30
print("Prime numbers:", sieve_of_eratosthenes(limit))
