
def prime_factorization(n):
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


number = 60
factors = prime_factorization(number)

print("Number:", number)
print("Prime factors:", factors)

result = " x ".join(map(str, factors))
print("Factorization:", result)
